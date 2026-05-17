#!/usr/bin/env python3
"""Council fix: strip overly-restrictive &i=industrial + add per-article
ascsubtag for free Amazon attribution.

Council run 0a4eea (2026-05-17) flagged two issues with the first URL
upgrade pass:

1. `&i=industrial` suppresses good results in Amazon's
   Appliance Parts & Accessories category. The 4 new appliance articles
   (LG washer, etc) need to surface results from that category. Strip
   `&i=industrial` from ALL upgraded URLs — the gain from category-
   constraint is less than the loss from suppressed results on the
   appliance and consumer-equipment-heavy 60% of the corpus.

2. `&ascsubtag=ecf-{slug}` provides per-article attribution that Amazon
   exposes in Associates reports without any PA-API setup. Once a sale
   lands, Chris can immediately see which article drove it — solving
   the GA4-blind-spot for affiliate revenue specifically.

Idempotent. {slug} is derived from the filename stem.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"

URL_RE = re.compile(
    # Allow literal " inside the URL — the first upgrade pass left unencoded
    # quotes in the markdown source for exact-match keywords. Browsers
    # percent-encode them on click, but our regex has to walk past them or
    # it stops at the first quote and misses half the URL.
    r"https?://(?:www\.)?amazon\.com/[^)\s']*tag=errorcodefixes-20[^)\s']*",
    re.IGNORECASE,
)


def _finalize(url: str, slug: str) -> str:
    try:
        p = urlparse(url)
    except ValueError:
        return url
    qs = parse_qs(p.query, keep_blank_values=True)
    if "tag" not in qs or qs["tag"][0] != "errorcodefixes-20":
        return url
    # Drop &i=industrial — too restrictive across the mixed corpus
    qs.pop("i", None)
    # Add &ascsubtag=ecf-<slug> if not already present
    if "ascsubtag" not in qs:
        qs["ascsubtag"] = [f"ecf-{slug}"]
    new_query = urlencode(sorted(qs.items()), doseq=True, safe='"')
    return urlunparse((p.scheme, p.netloc, p.path, p.params, new_query, p.fragment))


def process(path: Path, apply: bool) -> int:
    slug = path.stem
    text = path.read_text(encoding="utf-8")
    changed = 0

    def _sub(m: re.Match) -> str:
        nonlocal changed
        old = m.group(0)
        new = _finalize(old, slug)
        if new != old:
            changed += 1
        return new

    new_text = URL_RE.sub(_sub, text)
    if changed and apply:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    total = 0
    files = 0
    for f in sorted(BLOG.glob("*.md")):
        n = process(f, args.apply)
        if n:
            total += n
            files += 1
    verb = "would finalize" if not args.apply else "finalized"
    print(f"{verb} {total} URLs across {files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
