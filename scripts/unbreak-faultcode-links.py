#!/usr/bin/env python3
"""Unwrap fault-code-as-Amazon-search links — a generation bug that converts $0.

Many industrial fault-code TABLES wrapped the fault code itself in an Amazon
search link, e.g.  [2310](amazon.com/s?...&k=2310&tag=...)  — clicking the code
searches Amazon for "2310" (garbage), some with literal quotes (k="FA81"). These
cannot convert, look spammy, and risk Amazon Associates ToS (non-product search
cloaking). This unwraps ONLY the broken pattern — a markdown link whose anchor
text IS a fault-code-like token AND equals the Amazon search query — back to
plain text. It deliberately KEEPS legitimate part-name search links
(e.g. [Samsung dishwasher drain pump](amazon.com/s?k=Samsung+...)).

Usage: python scripts/unbreak-faultcode-links.py [--apply]   (default dry run)
"""
from __future__ import annotations
import re
import sys
import urllib.parse
from pathlib import Path

BLOG = Path(__file__).resolve().parent.parent / "src" / "data" / "blog"

# A markdown link to an Amazon search: [ANCHOR](https://www.amazon.com/s?...k=KVAL...)
LINK = re.compile(
    r'\[([^\]]{1,40})\]\(https?://(?:www\.)?amazon\.com/s\?[^)]*?\bk=([^)&]*)[^)]*\)'
)


def is_faultcode_token(s: str) -> bool:
    """True if s looks like a fault/alarm CODE, not a descriptive part name.
    Codes: short, single token, has a digit or is short all-caps (E1, F21, 2310,
    FA81, A2310, U4, SUD, LE, OE, P8). Part names are multi-word / long."""
    s = s.strip().strip('"').strip("'").strip()
    if not s or " " in s or len(s) > 8:
        return False
    if any(ch in s for ch in "+-/.,"):  # part-ish punctuation
        return False
    has_digit = any(c.isdigit() for c in s)
    short_caps = s.isupper() and len(s) <= 5
    return has_digit or short_caps


def unbreak(text: str):
    n = [0]

    def repl(m):
        anchor, kval = m.group(1), m.group(2)
        kdec = urllib.parse.unquote_plus(kval).strip().strip('"').strip("'")
        a = anchor.strip().strip('"').strip("'")
        # Only unwrap when the link text IS the search query (you're "searching
        # for the thing you clicked") AND it's a code-like token.
        if a == kdec and is_faultcode_token(a):
            n[0] += 1
            return anchor  # plain text, drop the link
        return m.group(0)

    return LINK.sub(repl, text), n[0]


def main() -> int:
    apply = "--apply" in sys.argv
    files = sorted(BLOG.glob("*.md"))
    touched = total = 0
    samples = []
    for f in files:
        t = f.read_text(encoding="utf-8")
        new, cnt = unbreak(t)
        if cnt:
            touched += 1
            total += cnt
            if len(samples) < 10:
                samples.append((f.name, cnt))
            if apply:
                f.write_text(new, encoding="utf-8")
    mode = "APPLIED" if apply else "DRY RUN (pass --apply to write)"
    for name, c in samples:
        print(f"  {name}: unwrapped {c} fault-code links")
    print(f"\n{mode}\n  pages touched : {touched}\n  links unwrapped: {total}\n  files scanned : {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
