#!/usr/bin/env python3
"""
add_internal_links.py
Adds a "Related Articles" section to each blog post on errorcodefixes.com,
grouped by brand/manufacturer prefix extracted from the filename.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

BLOG_DIR = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog")

# Brand prefixes to group articles by (order matters — longer prefixes first to avoid partial matches)
BRAND_PREFIXES = [
    "allen-bradley",
    "bradford-white",
    "ao-smith",
    "beverage-air",
    "mitsubishi",
    "manitowoc",
    "hoshizaki",
    "scotsman",
    "navien",
    "carrier",
    "lennox",
    "goodman",
    "trane",
    "york",
    "daikin",
    "rheem",
    "rinnai",
    "yaskawa",
    "siemens",
    "fanuc",
    "haas",
    "true",
    "abb",
]

RELATED_SECTION_HEADER = "## Related Articles"


def extract_frontmatter_title(content: str) -> str | None:
    """Extract title from YAML frontmatter."""
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    fm = match.group(1)
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip().strip('"\'')
    return None


def get_brand(filename: str) -> str | None:
    """Return the matching brand prefix for a given filename (stem only)."""
    stem = filename.lower()
    for brand in BRAND_PREFIXES:
        if stem.startswith(brand + "-") or stem == brand:
            return brand
    return None


def slug_from_path(filepath: Path) -> str:
    """Return the URL slug (no extension)."""
    return filepath.stem


def has_related_section(content: str) -> bool:
    return RELATED_SECTION_HEADER in content


def build_related_section(links: list[tuple[str, str]]) -> str:
    """Build the markdown Related Articles section."""
    lines = [RELATED_SECTION_HEADER, ""]
    for title, slug in links:
        lines.append(f"- [{title}](/posts/{slug}/)")
    lines.append("")
    return "\n".join(lines)


def append_related_section(content: str, related_md: str) -> str:
    """Append related section at the end of the file (after stripping trailing whitespace)."""
    return content.rstrip() + "\n\n" + related_md


def main():
    md_files = list(BLOG_DIR.glob("*.md"))
    print(f"Found {len(md_files)} markdown files.")

    # Build article index: {filepath: (title, brand)}
    articles = {}
    for fp in md_files:
        content = fp.read_text(encoding="utf-8", errors="replace")
        title = extract_frontmatter_title(content)
        brand = get_brand(fp.stem)
        if title and brand:
            articles[fp] = (title, brand, content)

    print(f"Matched {len(articles)} articles to known brands.")

    # Group by brand
    by_brand: dict[str, list[tuple[Path, str]]] = defaultdict(list)
    for fp, (title, brand, _) in articles.items():
        by_brand[brand].append((fp, title))

    # Print brand group sizes
    for brand in sorted(by_brand.keys()):
        print(f"  {brand}: {len(by_brand[brand])} articles")

    updated = 0
    skipped_small = 0
    skipped_existing = 0

    for fp, (title, brand, content) in articles.items():
        group = by_brand[brand]

        # Skip brands with fewer than 3 articles
        if len(group) < 3:
            skipped_small += 1
            continue

        # Skip if already has Related Articles section
        if has_related_section(content):
            skipped_existing += 1
            continue

        # Pick up to 5 related articles (not self)
        slug_self = slug_from_path(fp)
        candidates = [(p, t) for p, t in group if p != fp]

        # Limit to 5
        selected = candidates[:5]

        if len(selected) < 3:
            skipped_small += 1
            continue

        links = [(t, slug_from_path(p)) for p, t in selected]
        related_md = build_related_section(links)
        new_content = append_related_section(content, related_md)

        fp.write_text(new_content, encoding="utf-8")
        updated += 1

    print(f"\n=== RESULTS ===")
    print(f"Articles updated:              {updated}")
    print(f"Skipped (existing section):    {skipped_existing}")
    print(f"Skipped (brand group < 3):     {skipped_small}")
    print(f"Total processed:               {len(articles)}")


if __name__ == "__main__":
    main()
