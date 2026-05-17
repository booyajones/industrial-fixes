#!/usr/bin/env python3
"""Undo over-quoting from the first upgrade_amazon_links run.

Gauntlet caught (run 0a4ee5): the initial part-number regex was too loose,
quoting bare 1-5-digit numerics that weren't actually part numbers — things
like "0004" or "5010" that originated as flash-counts or alarm-bank IDs in
source articles. Amazon treats quoted exact-match against bare numerics as
"find a product whose title literally contains '0004'", which returns
nothing useful.

This script narrows the rule: unquote any `k="..."` where the inside is
ONLY digits (no letters, no hyphens). Real OEM part numbers nearly always
have a letter prefix or a hyphen — those keep their quotes.

Idempotent.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"

# k="DIGITSONLY"  (no letters, no hyphens, 1-5 chars) → k=DIGITSONLY
OVER_QUOTED_RE = re.compile(r'k="(\d{1,5})"')


def fix_file(path: Path, apply: bool) -> int:
    text = path.read_text(encoding="utf-8")
    new, n = OVER_QUOTED_RE.subn(r"k=\1", text)
    if n and apply:
        path.write_text(new, encoding="utf-8")
    return n


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    total = 0
    files = 0
    for f in sorted(BLOG.glob("*.md")):
        n = fix_file(f, args.apply)
        if n:
            total += n
            files += 1
    verb = "would unquote" if not args.apply else "unquoted"
    print(f"{verb} {total} bare-numeric search keys across {files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
