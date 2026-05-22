#!/usr/bin/env python3
"""
Repair leftover `*/PLACEHOLDER-<slug>` URL paths.

The earlier amazon-link injector left `https://amzn.to/PLACEHOLDER-XYZ` and
`https://<domain>/PLACEHOLDER-XYZ` patterns in dozens of articles when it
could not resolve a real short-link or product URL. These render as broken
clicks (amzn.to → 404; merchant domain → homepage with garbage path).

Repair strategy (conservative, idempotent):

  1. `https://amzn.to/PLACEHOLDER-<token>`
       → `https://www.amazon.com/s?k=<token-as-search>&tag=errorcodefixes-20`
     (Amazon's `/s?k=` search reliably returns relevant SKUs; tag preserves
     Amazon Associates attribution.)

  2. `https://<other-domain>/PLACEHOLDER-<token>` (optionally with query)
       → `https://<other-domain>/`
     (Strip the placeholder path; Skimlinks intercepts the click anyway.
     Preserves any UTM query string that was added previously.)

USAGE:
    python scripts/fix-placeholder-urls.py            # dry-run
    python scripts/fix-placeholder-urls.py --apply    # actually edit
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
OUT_DIR = ROOT / "growth-pipeline" / "utm-tagging"

AMZN_RE = re.compile(r'https://amzn\.to/PLACEHOLDER-([A-Z0-9_-]+)', re.I)
OTHER_RE = re.compile(r'(https?://[a-z0-9.-]+)/PLACEHOLDER-[A-Z0-9_-]+(\?[^"\s\)\]]*)?', re.I)


def fix_amzn(m: re.Match) -> str:
    token = m.group(1)
    # Convert PLACEHOLDER-XYZ-ABC into a search query "XYZ ABC"
    search = token.replace("-", " ").replace("_", " ").strip()
    return f"https://www.amazon.com/s?k={search.replace(' ', '+')}&tag=errorcodefixes-20"


def fix_other(m: re.Match) -> str:
    base = m.group(1)
    query = m.group(2) or ""
    return f"{base}/{query}"


def process(text: str) -> tuple[str, Counter]:
    stats = Counter()
    new_text, n1 = AMZN_RE.subn(fix_amzn, text)
    stats["amzn_fixed"] = n1
    new_text, n2 = OTHER_RE.subn(fix_other, new_text)
    stats["other_fixed"] = n2
    return new_text, stats


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")

    total = Counter()
    per_file = []
    files = sorted(BLOG.glob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        new_text, stats = process(text)
        if stats["amzn_fixed"] or stats["other_fixed"]:
            per_file.append((path.stem, stats))
            total["files_touched"] += 1
        total["amzn_fixed"] += stats["amzn_fixed"]
        total["other_fixed"] += stats["other_fixed"]
        if args.apply and new_text != text:
            path.write_text(new_text, encoding="utf-8")

    report = OUT_DIR / f"{date_stamp}_placeholder_fix_report.md"
    lines = [
        f"# Placeholder URL Repair — {date_stamp}",
        "",
        f"**Mode:** {'APPLY' if args.apply else 'DRY-RUN'}",
        "",
        f"- Files scanned: {len(files)}",
        f"- Files touched: {total['files_touched']}",
        f"- `amzn.to/PLACEHOLDER-*` converted to amazon search: {total['amzn_fixed']}",
        f"- Other `/PLACEHOLDER-*` paths stripped to root: {total['other_fixed']}",
        "",
        "## Top files",
        "",
    ]
    per_file.sort(key=lambda kv: -(kv[1]["amzn_fixed"] + kv[1]["other_fixed"]))
    for slug, st in per_file[:50]:
        lines.append(f"- `{slug}`: amzn_fixed={st['amzn_fixed']}, other_fixed={st['other_fixed']}")
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Report: {report}")
    print(f"    Files touched: {total['files_touched']}, amzn_fixed: {total['amzn_fixed']}, other_fixed: {total['other_fixed']}")
    if not args.apply:
        print("    (dry-run — re-run with --apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
