#!/usr/bin/env python3
"""
Money-ordered content runner. Takes a list of revenue-priority slugs (from the
Money Map). For each: if the page is missing -> CREATE it deep; if it exists but
is not deep yet -> DEEPEN it (overwrite only when the deep version passes review,
so a live page is never downgraded). Reuses generate-articles.py end to end.

USAGE:
  python scripts/money-gen.py --file .planning/money-targets.txt --jobs 1
  python scripts/money-gen.py --file .planning/money-targets.txt --dry
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"
_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_lock = threading.Lock()
_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}


def slug_to_topic(slug: str) -> str:
    return slug.replace("-error-code", "").replace("-", " ").strip() + " error code"


def run_one(slug: str) -> tuple[str, str, str]:
    path = G.BLOG_DIR / f"{slug}.md"
    exists = path.exists()
    if exists:
        head = path.read_text(encoding="utf-8")[:600]
        if re.search(r"^diy_or_pro:", head, re.M):
            return (slug, "skip", "already deep")
    topic = slug_to_topic(slug)
    try:
        research = G.perplexity_research(topic)
        content = G.claude_write(topic, research)
        if not content:
            return (slug, "fail", "no content")
        verdict = G.claude_review(topic, content, research)
        ok = bool(verdict.get("publish")) and int(verdict.get("score") or 0) >= 7
        if exists and not ok:
            return (slug, "keep", f"review={verdict.get('score')} kept existing")
        md = G.assemble_md(topic, content, slug, draft=not ok)
        if G.BANNED.search(md):
            md = G.BANNED.sub(lambda m: _FIX.get(m.group(0).lower(), m.group(0)), md)
        with _lock:
            path.write_text(md, encoding="utf-8")
        action = ("created" if not exists else "deepened") if ok else "drafted"
        return (slug, action, f"score={verdict.get('score')}")
    except Exception as e:
        return (slug, "fail", str(e)[:120])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    if not args.dry and not getattr(G, "ANTHROPIC_KEY", ""):
        print("[!] set ANTHROPIC_API_KEY first.")
        return 1
    slugs = [s.strip() for s in Path(args.file).read_text(encoding="utf-8").splitlines() if s.strip()]
    if args.limit:
        slugs = slugs[: args.limit]
    print(f"[i] {len(slugs)} money targets (jobs={args.jobs})")
    if args.dry:
        for s in slugs[:40]:
            print("   ", s, "->", slug_to_topic(s))
        return 0
    res: dict[str, int] = {}
    done = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(run_one, s): s for s in slugs}
        for f in as_completed(futs):
            slug, status, info = f.result()
            res[status] = res.get(status, 0) + 1
            done += 1
            if done % 5 == 0 or status in ("fail", "created", "deepened"):
                print(f"  [{done}/{len(slugs)}] {status:8} {slug}  {info}")
    print(f"\n[+] done: {res}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
