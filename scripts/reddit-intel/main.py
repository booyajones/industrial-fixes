"""Tier A Reddit intel runner — listen-only.

  python main.py                      # full run
  python main.py --dry-run            # don't write sheet, don't email
  python main.py --max-queries 5      # smoke test against small subset
  python main.py --subs hvacadvice    # limit to one subreddit

Designed to be invoked from .github/workflows/reddit-intel.yml on a weekly
cron, but runnable locally for development.

Env vars (all optional except where noted for production):
  REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET  — OAuth (optional; falls back to
                                            unauthenticated public JSON)
  GOOGLE_APPLICATION_CREDENTIALS_JSON     — finexio-automation SA JSON, used
                                            to write the weekly tab. Without
                                            this, writes local JSON only.
  REDDIT_INTEL_SPREADSHEET_ID             — target spreadsheet
  SMTP_HOST / SMTP_USER / SMTP_PASS       — for the email digest
  REDDIT_INTEL_DIGEST_TO                  — override recipient (default Chris)
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

import yaml  # PyYAML

# scripts/reddit-intel/ is on sys.path when run via `python main.py` from
# that directory; pad it anyway so module-style runs work.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import os

import fetch
import classify as classify_mod
import match_articles
import sink_sheet
import notify


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )


def _load_config() -> dict:
    return yaml.safe_load((Path(__file__).resolve().parent / "queries.yml").read_text())


def _filter_hits(records: list[dict], cfg: dict) -> list[dict]:
    """Drop hits that fail the configured filters."""
    import re as _re
    f = cfg.get("filters", {})
    max_age = (f.get("max_age_days") or 14) * 24
    excl_flair = {x.lower() for x in (f.get("exclude_flair") or [])}
    excl_re = [_re.compile(p) for p in (f.get("exclude_title_regex") or [])]
    out: list[dict] = []
    for r in records:
        if r["age_hours"] > max_age:
            continue
        flair = (r.get("link_flair") or "").lower() if isinstance(r, dict) else ""
        # filter_hits operates on the *annotated* records which don't carry
        # link_flair — keep this dropper here only as a no-op for the dict path
        if flair and flair in excl_flair:
            continue
        if any(rx.search(r.get("title", "")) for rx in excl_re):
            continue
        out.append(r)
    return out


def _strict_mode_or_die() -> None:
    """On scheduled GitHub Actions runs, missing prod creds = hard fail.

    Council blocker fix: the fallback to local-JSON-and-stdout is helpful
    for local dev but actively dangerous in a cron context — the workflow
    shows green while the pipeline silently drops data into an artifact
    Chris will never look at. Force a loud red failure so secret rotations
    actually get noticed.
    """
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return
    if os.environ.get("GITHUB_EVENT_NAME") != "schedule":
        return  # workflow_dispatch keeps fallbacks for ad-hoc smoke tests
    missing: list[str] = []
    if not os.environ.get("REDDIT_INTEL_SPREADSHEET_ID"):
        missing.append("REDDIT_INTEL_SPREADSHEET_ID")
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON"):
        missing.append("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not (os.environ.get("SMTP_HOST") and os.environ.get("SMTP_USER")):
        missing.append("SMTP_HOST/SMTP_USER")
    if missing:
        logging.error(
            "scheduled run is missing required prod env vars: %s. "
            "Refusing to fall back to local JSON / stdout on a cron run.",
            ", ".join(missing),
        )
        sys.exit(1)


def run(args: argparse.Namespace) -> int:
    _strict_mode_or_die()
    cfg = _load_config()
    subs = args.subs or cfg["subreddits"]
    patterns = cfg["patterns"]
    brands = cfg["brands"]

    if args.max_queries:
        patterns = patterns[: args.max_queries]
        brands = brands[: args.max_queries]
        logging.info(
            "smoke mode: %d patterns x %d brands x %d subs = %d queries",
            len(patterns), len(brands), len(subs),
            len(patterns) * len(brands) * len(subs),
        )

    started = time.time()
    raw_hits = list(fetch.search(
        subreddits=subs,
        patterns=patterns,
        brands=brands,
        limit_per_query=args.limit_per_query,
        polite_delay_sec=args.polite_delay_sec,
    ))
    logging.info("fetched %d unique hits in %.1fs", len(raw_hits), time.time() - started)

    if not raw_hits:
        logging.info("no hits — exiting early")
        return 0

    classified = classify_mod.classify(
        fetch.hits_to_records(raw_hits),
        now_utc=time.time(),
    )

    blog_dir = Path(__file__).resolve().parents[2] / "src" / "data" / "blog"
    annotated = match_articles.annotate(classified, blog_dir)
    annotated = _filter_hits(annotated, cfg)

    # Cross-week dedup. The sheet is the state store — every weekly tab
    # already contains post_id. If we've written this id before, skip.
    if not args.no_dedup:
        seen = sink_sheet.read_seen_post_ids()
        if seen:
            before = len(annotated)
            annotated = [r for r in annotated if r["post_id"] not in seen]
            logging.info("dedup: dropped %d already-seen posts (%d → %d)",
                         before - len(annotated), before, len(annotated))

    by_gap = {"content_gap": 0, "serp_gap": 0, "covered": 0, "unknown": 0}
    for r in annotated:
        by_gap[r["gap_kind"]] = by_gap.get(r["gap_kind"], 0) + 1
    logging.info("gap breakdown: %s", by_gap)

    if args.dry_run:
        logging.info("--dry-run set; skipping sheet write + email")
        print(annotated[:3])
        return 0

    sheet_url = sink_sheet.write(annotated)
    notify.send(annotated, sheet_url)
    return 0


def _parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Reddit intel runner (listen-only)")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--verbose", "-v", action="store_true")
    p.add_argument("--subs", nargs="*", help="override subreddit list")
    p.add_argument("--max-queries", type=int, default=0,
                   help="smoke test: cap both patterns and brands to this N")
    p.add_argument("--limit-per-query", type=int, default=25)
    p.add_argument("--polite-delay-sec", type=float, default=1.0)
    p.add_argument("--no-dedup", action="store_true",
                   help="skip cross-week dedup (debug only)")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv or sys.argv[1:])
    _setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
