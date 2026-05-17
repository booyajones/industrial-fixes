#!/usr/bin/env python3
"""Upgrade Amazon search URLs across the article corpus.

Gauntlet + council blocker fix: AmazonPartLink component shipped, parts.json
seeded, but ZERO existing articles were using either. Every "Check price on
Amazon" link in 1,148 articles still went to a generic search URL with no
category constraint and no exact-match quoting — the lowest-converting
variant of an affiliate link.

This script does two narrow, safe transformations to every markdown file in
src/data/blog/:

1. If a part number (alphanumeric, mostly digits, 4-12 chars) appears
   unquoted in the search keyword, quote it for exact-match. Amazon's
   relevance algorithm treats "T-84984" very differently from T-84984.

2. Add &i=industrial to every search URL that doesn't already have it.
   Constrains results to the Industrial & Scientific category, which is
   where commercial-equipment parts actually live and where conversion is
   materially higher than mixed-category search.

The tag query parameter (&tag=errorcodefixes-20) is preserved verbatim.
ASIN-style /dp/B0XXXXXXXX/ links are not touched — those are already optimal.

Idempotent: running twice produces identical output.

Usage:
    python scripts/upgrade_amazon_links.py            # dry-run
    python scripts/upgrade_amazon_links.py --apply    # write changes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"

# Match Amazon search URLs with our tag. Captures the full URL for replacement.
URL_RE = re.compile(
    r"https?://(?:www\.)?amazon\.com/s\?[^)\s\"']*tag=errorcodefixes-20[^)\s\"']*",
    re.IGNORECASE,
)

# A "part number" looks like 4-12 chars, mostly digits, optionally with a
# letter prefix or one internal hyphen. T-84984, 915146, WR02X12345, A101.
PART_RE = re.compile(r"^[A-Z]{0,3}-?\d{2,8}[A-Z0-9]{0,5}$", re.IGNORECASE)


def _upgrade_url(url: str) -> str:
    """Returns the upgraded URL (or original if no change applicable)."""
    try:
        p = urlparse(url)
    except ValueError:
        return url
    qs = parse_qs(p.query, keep_blank_values=True)
    if "tag" not in qs or qs["tag"][0] != "errorcodefixes-20":
        return url

    k = qs.get("k", [""])[0]
    if not k:
        return url

    # If the keyword is a single token that looks like a part number,
    # quote it for exact-match. Skip if already quoted (idempotent).
    tokens = k.split()
    if len(tokens) == 1 and PART_RE.match(tokens[0].strip('"')):
        bare = tokens[0].strip('"')
        if not k.startswith('"'):
            qs["k"] = [f'"{bare}"']

    # Constrain to industrial category unless explicitly set otherwise.
    qs.setdefault("i", ["industrial"])

    # rebuild deterministically (sorted) to keep diffs stable
    new_query = urlencode(sorted(qs.items()), doseq=True, safe='"')
    return urlunparse((p.scheme, p.netloc, p.path, p.params, new_query, p.fragment))


def upgrade_file(path: Path, apply: bool) -> int:
    """Returns count of URLs changed in this file."""
    text = path.read_text(encoding="utf-8")
    changed = 0

    def _sub(m: re.Match) -> str:
        nonlocal changed
        old = m.group(0)
        new = _upgrade_url(old)
        if new != old:
            changed += 1
        return new

    new_text = URL_RE.sub(_sub, text)
    if changed and apply:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> int:
    p = argparse.ArgumentParser(description="Upgrade Amazon search URLs")
    p.add_argument("--apply", action="store_true",
                   help="write changes (omit for dry-run summary)")
    args = p.parse_args()

    files = sorted(BLOG.glob("*.md"))
    total_changed = 0
    total_files = 0
    for f in files:
        n = upgrade_file(f, args.apply)
        if n > 0:
            total_files += 1
            total_changed += n
    verb = "would upgrade" if not args.apply else "upgraded"
    print(f"{verb} {total_changed} URLs across {total_files}/{len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
