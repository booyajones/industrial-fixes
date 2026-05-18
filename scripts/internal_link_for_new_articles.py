#!/usr/bin/env python3
"""Inject internal links FROM existing articles TO the recently-shipped
demand-validated articles. Council 0a4eea recommendation: "Get the 4 new
Reddit-sourced articles internally linked from 5-10 relevant existing
articles this week so they index fast."

How it works:
  1. NEW_ARTICLES is a hand-curated list of (slug, anchor_text, match_tags).
  2. For each existing article, if any of its tags overlap with match_tags
     AND the article doesn't already link to the new slug, append a
     'Related guides' callout that points to the new article.
  3. Skip articles that ARE the target. Skip if max-existing-per-new is hit.

Idempotent — checks for existing link before injecting. Dry-run by default.

Usage:
    python scripts/internal_link_for_new_articles.py            # dry-run
    python scripts/internal_link_for_new_articles.py --apply    # write changes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"

# Each entry: (slug, anchor text, source-article tag set that should link here).
# Cap of 8 linking articles per new target to avoid look-spammy patterns.
NEW_ARTICLES = [
    {
        "slug": "rheem-econet-a101-error-code",
        "anchor": "Rheem EcoNet A101 error code fix",
        "match_tags": {"rheem", "thermostat", "econet", "hvac"},
        "max_links": 8,
    },
    {
        "slug": "rheem-performance-platinum-pdn-error-codes",
        "anchor": "Rheem Performance Platinum PDN tankless error codes",
        "match_tags": {"rheem", "tankless", "water-heater", "plumbing"},
        "max_links": 8,
    },
    {
        "slug": "lg-washer-error-codes",
        "anchor": "LG washer error codes (complete guide)",
        "match_tags": {"lg", "washer", "laundry", "appliances"},
        "max_links": 8,
    },
    {
        "slug": "lg-washer-error-code-31",
        "anchor": "LG washer error code 31 (pressure / suspension fault)",
        "match_tags": {"lg", "washer", "laundry"},
        "max_links": 6,
    },
    # Second wave 2026-05-17 — major appliance brand coverage from canary
    {
        "slug": "lg-refrigerator-error-codes",
        "anchor": "LG refrigerator error codes (complete guide)",
        "match_tags": {"lg", "refrigerator", "fridge", "appliances"},
        "max_links": 8,
    },
    {
        "slug": "bosch-dishwasher-error-codes",
        "anchor": "Bosch dishwasher error codes",
        "match_tags": {"bosch", "dishwasher", "kitchen", "appliances"},
        "max_links": 8,
    },
    {
        "slug": "whirlpool-washer-error-codes",
        "anchor": "Whirlpool washer error codes (F-codes + Cabrio)",
        "match_tags": {"whirlpool", "washer", "laundry", "appliances"},
        "max_links": 8,
    },
    {
        "slug": "maytag-washer-error-codes",
        "anchor": "Maytag washer error codes (Bravos + Centennial)",
        "match_tags": {"maytag", "washer", "laundry", "appliances"},
        "max_links": 8,
    },
    {
        "slug": "samsung-refrigerator-error-codes",
        "anchor": "Samsung refrigerator error codes",
        "match_tags": {"samsung", "refrigerator", "fridge", "appliances"},
        "max_links": 8,
    },
]

LINK_SECTION_MARKER = "<!-- INTERNAL-LINK-AUTO -->"


def parse_frontmatter_tags(text: str) -> set[str]:
    """Extract tags array from the frontmatter block. Returns lowercased set."""
    m = re.search(r"^---\s*\n(.*?)^---\s*\n", text, re.DOTALL | re.MULTILINE)
    if not m:
        return set()
    fm = m.group(1)
    tags: set[str] = set()
    # Match either inline `tags: [a, b]` or YAML list form
    inline = re.search(r"^tags\s*:\s*\[(.*?)\]", fm, re.MULTILINE)
    if inline:
        for t in inline.group(1).split(","):
            t = t.strip().strip('"').strip("'").lower()
            if t:
                tags.add(t)
        return tags
    # YAML list form
    list_m = re.search(r"^tags\s*:\s*\n((?:\s+-\s+.+\n)+)", fm, re.MULTILINE)
    if list_m:
        for line in list_m.group(1).splitlines():
            t = line.strip().lstrip("-").strip().strip('"').strip("'").lower()
            if t:
                tags.add(t)
    return tags


def already_links(text: str, slug: str) -> bool:
    """Does the body already reference this slug?"""
    return f"/posts/{slug}/" in text or f"/posts/{slug})" in text or slug in text


def inject_callout(text: str, slug: str, anchor: str) -> str:
    """Append an internal-link callout to the article body."""
    callout = (
        f"\n\n{LINK_SECTION_MARKER}\n"
        f"**Related:** [{anchor}](/posts/{slug}/)\n"
    )
    return text.rstrip() + callout + "\n"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    # Plan: per target, find candidate source files (tag overlap, not the
    # target itself, doesn't already link), cap at max_links per target,
    # prefer files most-likely to actually rank (heuristic: files with
    # short slugs are usually brand-level overviews that earn the most
    # search traffic).
    candidates_by_target: dict[str, list[Path]] = {a["slug"]: [] for a in NEW_ARTICLES}
    all_files = sorted(BLOG.glob("*.md"))

    for f in all_files:
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        tags = parse_frontmatter_tags(text)
        if not tags:
            continue
        for target in NEW_ARTICLES:
            if f.stem == target["slug"]:
                continue
            if tags & target["match_tags"]:
                if already_links(text, target["slug"]):
                    continue
                candidates_by_target[target["slug"]].append(f)

    # Rank candidates per target by slug length (shorter = brand-level
    # overview = higher SEO authority once it ranks)
    for slug, candidates in candidates_by_target.items():
        candidates.sort(key=lambda p: len(p.stem))

    # Apply caps + inject
    total = 0
    for target in NEW_ARTICLES:
        candidates = candidates_by_target[target["slug"]][: target["max_links"]]
        print(f"\n--> {target['slug']}: linking from {len(candidates)} files (cap {target['max_links']})")
        for f in candidates:
            text = f.read_text(encoding="utf-8")
            new = inject_callout(text, target["slug"], target["anchor"])
            if args.apply:
                f.write_text(new, encoding="utf-8")
            print(f"   - {f.name}")
            total += 1

    verb = "would inject" if not args.apply else "injected"
    print(f"\n{verb} {total} internal links total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
