#!/usr/bin/env python3
"""
add_internal_links.py
Adds a "## See Also" section to HVAC brand articles that don't already have one.
Targets: carrier, goodman, lennox, trane, rheem (top 5 brands)
Processes max 5 articles per brand (25 total edits).
"""

import os
import re
import random

BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "data", "blog")
BRANDS = [
    # Wave 1 — top HVAC brands
    "carrier", "goodman", "lennox", "trane", "rheem",
    # Wave 2 — HVAC + commercial refrigeration + CNC
    "york", "mitsubishi", "daikin", "haas", "fanuc", "siemens",
    "abb", "allen", "yaskawa", "manitowoc", "hoshizaki",
    # Wave 3 — tankless/boilers + appliances + CNC depth
    "navien", "rinnai", "mazak", "scotsman", "lg", "danfoss",
    "true", "okuma", "weil",
]
MAX_PER_BRAND = 5
SEE_ALSO_LINKS = 4  # number of cross-links to add


def get_slug(filename: str) -> str:
    """Return the slug (filename without .md extension)."""
    return filename.replace(".md", "").replace(".md.bak", "")


def get_title_from_file(filepath: str) -> str:
    """Extract the title from a markdown file's frontmatter."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return ""


def has_see_also(content: str) -> bool:
    return bool(re.search(r'^##\s+See Also', content, re.MULTILINE | re.IGNORECASE))


def build_see_also_section(current_slug: str, brand_files: list, blog_dir: str) -> str:
    """Pick 3-4 other articles from same brand and build the See Also section."""
    others = [f for f in brand_files if get_slug(f) != current_slug and not f.endswith(".bak")]
    
    # Shuffle deterministically based on slug so it's reproducible
    rng = random.Random(current_slug)
    rng.shuffle(others)
    picks = others[:SEE_ALSO_LINKS]

    if not picks:
        return ""

    lines = ["\n## See Also\n"]
    for fname in picks:
        slug = get_slug(fname)
        title = get_title_from_file(os.path.join(blog_dir, fname))
        if not title:
            title = slug.replace("-", " ").title()
        lines.append(f"- [{title}](/posts/{slug}/)")

    return "\n".join(lines) + "\n"


def process_file(filepath: str, current_slug: str, brand_files: list, blog_dir: str) -> bool:
    """Add See Also section to a file if it doesn't already have one. Returns True if modified."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_see_also(content):
        print(f"  SKIP (already has See Also): {os.path.basename(filepath)}")
        return False

    see_also = build_see_also_section(current_slug, brand_files, blog_dir)
    if not see_also:
        print(f"  SKIP (no other articles): {os.path.basename(filepath)}")
        return False

    # Append before the very end (strip trailing whitespace first)
    new_content = content.rstrip() + "\n" + see_also

    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)

    print(f"  ADDED See Also: {os.path.basename(filepath)}")
    return True


def main():
    all_files = [f for f in os.listdir(BLOG_DIR) if f.endswith(".md") and not f.endswith(".bak")]
    total_modified = 0

    for brand in BRANDS:
        brand_files = [f for f in all_files if f.startswith(brand + "-")]
        print(f"\n[{brand.upper()}] Found {len(brand_files)} articles")

        if not brand_files:
            print(f"  No files found for brand: {brand}")
            continue

        # Pick first MAX_PER_BRAND files that don't already have See Also
        eligible = []
        for fname in sorted(brand_files):
            if len(eligible) >= MAX_PER_BRAND:
                break
            filepath = os.path.join(BLOG_DIR, fname)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                if not has_see_also(content):
                    eligible.append(fname)
            except Exception as e:
                print(f"  ERROR reading {fname}: {e}")

        print(f"  Processing {len(eligible)} eligible files (max {MAX_PER_BRAND})")

        for fname in eligible:
            slug = get_slug(fname)
            filepath = os.path.join(BLOG_DIR, fname)
            if process_file(filepath, slug, brand_files, BLOG_DIR):
                total_modified += 1

    print(f"\nDone. Modified {total_modified} files.")


if __name__ == "__main__":
    main()
