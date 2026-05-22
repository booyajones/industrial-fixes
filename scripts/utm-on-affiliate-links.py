#!/usr/bin/env python3
"""
UTM tagging + placeholder cleanup for outbound merchant links.

Two related cleanups, idempotent:

  (1) Strip leftover `?aff=PLACEHOLDER-*` query strings that were inserted
      by an earlier automation pass when real affiliate IDs were unknown.
      These are user-visible junk and confer no attribution.

  (2) Add UTM params (utm_source=errorcodefixes, utm_medium=affiliate,
      utm_campaign=<article-slug>) to outbound links pointing at a known
      merchant domain that does NOT already carry UTM tagging.

WHY:
  Skimlinks intercepts the click and rewrites outbound merchant URLs at
  runtime, but Plausible captures the link.href on click as the goal
  value. Without UTMs, every Plausible "outbound click" row shows just
  the bare URL and we cannot attribute clicks to specific articles.

  After this pass, Plausible "Outbound Link: Click" goal rows show URLs
  with utm_campaign=<slug>, letting us group by article.

WHITELIST (only these get UTMs added):
  - repairclinic.com, partstown.com, partselect.com
  - homedepot.com, lowes.com, wayfair.com
  - automationdirect.com, wolfautomation.com, galco.com
  - grainger.com, mscdirect.com, mcmaster.com
  - johnstone.com, johnstonesupply.com
  - trutechtools.com, hvacpartshop.com, pexuniverse.com

EXPLICITLY EXCLUDED (already tracked or wrong-tool):
  - amazon.com / amzn.to  (already use ascsubtag)
  - errorcodefixes.com    (internal)
  - github.com, wikipedia.org, manufacturer help pages (not affiliate)

Run safely as many times as desired — markers prevent double-tagging.

USAGE:
    python scripts/utm-on-affiliate-links.py                 # dry-run
    python scripts/utm-on-affiliate-links.py --apply         # actually edit
    python scripts/utm-on-affiliate-links.py --apply --only repairclinic

OUTPUT:
  - In dry-run: writes growth-pipeline/utm-tagging/<date>_report.md
  - In --apply: edits .md files in-place + writes same report
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
OUT_DIR = ROOT / "growth-pipeline" / "utm-tagging"

WHITELIST = {
    "repairclinic.com", "partstown.com", "partselect.com",
    "homedepot.com", "lowes.com", "wayfair.com",
    "automationdirect.com", "wolfautomation.com", "galco.com",
    "grainger.com", "mscdirect.com", "mcmaster.com",
    "johnstone.com", "johnstonesupply.com",
    "trutechtools.com", "hvacpartshop.com", "pexuniverse.com",
    "ebay.com",
}

# URL pattern: captures anything that looks like http(s)://...
URL_RE = re.compile(r'(https?://[^\s"\)<>\]]+)')

PLACEHOLDER_RE = re.compile(r'\?aff=PLACEHOLDER-[A-Z0-9_]+', re.I)


def host_of(url: str) -> str:
    try:
        return urlparse(url).netloc.lower().lstrip("www.")
    except Exception:
        return ""


def is_whitelist(url: str) -> bool:
    h = host_of(url)
    return any(h == w or h.endswith("." + w) for w in WHITELIST)


def already_has_utm(url: str) -> bool:
    return "utm_source=" in url or "utm_campaign=" in url


def add_utm(url: str, slug: str) -> str:
    """Append UTM params idempotently. Preserves existing query."""
    parsed = urlparse(url)
    q = dict(parse_qsl(parsed.query, keep_blank_values=True))
    if "utm_source" in q or "utm_campaign" in q:
        return url
    q["utm_source"] = "errorcodefixes"
    q["utm_medium"] = "affiliate"
    q["utm_campaign"] = slug
    new_query = urlencode(q)
    return urlunparse(parsed._replace(query=new_query))


def process_text(text: str, slug: str, only_host: str | None = None) -> tuple[str, dict]:
    stats = Counter()

    # Step 1: strip ?aff=PLACEHOLDER- placeholders
    def strip_placeholder(m: re.Match) -> str:
        return ""

    placeholders_before = len(PLACEHOLDER_RE.findall(text))
    text = PLACEHOLDER_RE.sub("", text)
    stats["placeholders_stripped"] = placeholders_before

    # Step 2: UTM-tag whitelisted outbound URLs
    def tag_url(m: re.Match) -> str:
        url = m.group(1)
        # Strip trailing punctuation that's often grabbed by accident
        trailing = ""
        while url and url[-1] in ').,;:':
            trailing = url[-1] + trailing
            url = url[:-1]
        if not is_whitelist(url):
            return url + trailing
        if only_host and host_of(url).find(only_host) < 0:
            return url + trailing
        if already_has_utm(url):
            stats["already_tagged"] += 1
            return url + trailing
        new_url = add_utm(url, slug)
        stats["tagged"] += 1
        return new_url + trailing

    text = URL_RE.sub(tag_url, text)
    return text, stats


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="Actually edit files (default: dry-run)")
    p.add_argument("--only", help="Limit to URLs containing this host substring")
    p.add_argument("--max-files", type=int, default=0, help="Stop after N files (testing)")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")

    files = sorted(BLOG.glob("*.md"))
    if args.max_files:
        files = files[: args.max_files]

    total = Counter()
    per_file = []

    for path in files:
        slug = path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        new_text, stats = process_text(text, slug, only_host=args.only)
        if stats["tagged"] or stats["placeholders_stripped"]:
            per_file.append((slug, stats))
            total["files_touched"] += 1
        total["tagged"] += stats["tagged"]
        total["placeholders_stripped"] += stats["placeholders_stripped"]
        total["already_tagged"] += stats["already_tagged"]
        if args.apply and new_text != text:
            path.write_text(new_text, encoding="utf-8")

    report_path = OUT_DIR / f"{date_stamp}_report.md"
    lines = [
        f"# UTM Tagging Report — {date_stamp}",
        "",
        f"**Mode:** {'APPLY (files written)' if args.apply else 'DRY-RUN (no changes)'}",
        f"**Filter:** {args.only or 'all whitelisted merchants'}",
        "",
        f"## Totals",
        f"- Files scanned: {len(files)}",
        f"- Files with at least one change: {total['files_touched']}",
        f"- Outbound merchant URLs newly tagged: {total['tagged']}",
        f"- Placeholder `?aff=PLACEHOLDER-*` stripped: {total['placeholders_stripped']}",
        f"- URLs already correctly tagged (skipped): {total['already_tagged']}",
        "",
        "## Per-file (top 50 by change count)",
        "",
    ]
    per_file.sort(key=lambda kv: -(kv[1]["tagged"] + kv[1]["placeholders_stripped"]))
    for slug, st in per_file[:50]:
        lines.append(f"- `{slug}`: tagged={st['tagged']}, placeholders={st['placeholders_stripped']}")
    if len(per_file) > 50:
        lines.append(f"- _(+ {len(per_file) - 50} more files with smaller change counts)_")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Report: {report_path}")
    print(f"    Files touched: {total['files_touched']}")
    print(f"    URLs tagged: {total['tagged']}")
    print(f"    Placeholders stripped: {total['placeholders_stripped']}")
    if not args.apply:
        print("    (dry-run — re-run with --apply to write changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
