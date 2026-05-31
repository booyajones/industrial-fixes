#!/usr/bin/env python3
"""
Task 2: Unlink garbage Amazon affiliate anchors.

Some articles wrapped table-cell values (column headers / data cells) in Amazon
search links, e.g. [Code](https://www.amazon.com/s?...&tag=errorcodefixes-20).
Those anchors are non-product strings, never convert, and look spammy.

This script finds markdown links whose href contains "amazon" AND whose visible
anchor text is one of a CONSERVATIVE allow-list of non-product strings, then
replaces the whole [anchor](url) with just the plain `anchor` text (unlinks it).

Allow-list (case-insensitive):
  - Code, Fault, Blinks, Flash Pattern, Thermostat, ZN1 FAULT
  - Any "<N> flash" / "<N> flashes" pattern
  - Any "<N> blink" / "<N> blinks" pattern

ONLY these are unlinked. Any other anchor (real part name) is left untouched.
"""
import re
import glob
import os
import sys

BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "data", "blog")

# Fixed non-product strings (compared case-insensitively, whitespace-normalized).
FIXED = {
    "code",
    "fault",
    "blinks",
    "flash pattern",
    "thermostat",
    "zn1 fault",
}

# "<N> flash" / "<N> flashes" / "<N> blink" / "<N> blinks"
NUM_PATTERN = re.compile(r"^\d+\s+(?:flash(?:es)?|blinks?)$", re.IGNORECASE)

# Markdown link: [anchor](url)  -- anchor has no ] or [ inside; url has no ).
LINK_RE = re.compile(r"\[([^\[\]]+?)\]\((https?://[^)]*)\)")


def is_garbage_anchor(anchor: str) -> bool:
    norm = re.sub(r"\s+", " ", anchor).strip().lower()
    if norm in FIXED:
        return True
    if NUM_PATTERN.match(norm):
        return True
    return False


def main():
    files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.md")))
    total_unlinked = 0
    changed_files = 0
    samples = []

    for fp in files:
        with open(fp, encoding="utf-8") as fh:
            txt = fh.read()

        file_unlinked = 0

        def repl(m):
            nonlocal file_unlinked
            anchor, url = m.group(1), m.group(2)
            if "amazon" not in url.lower():
                return m.group(0)
            if not is_garbage_anchor(anchor):
                return m.group(0)
            file_unlinked += 1
            if len(samples) < 3:
                samples.append((os.path.basename(fp), m.group(0), anchor))
            return anchor  # unlink: keep plain anchor text

        new = LINK_RE.sub(repl, txt)

        if new != txt:
            with open(fp, "w", encoding="utf-8", newline="") as fh:
                fh.write(new)
            changed_files += 1
            total_unlinked += file_unlinked

    print("TASK 2 - Unlink garbage Amazon anchors")
    print(f"Total links unlinked: {total_unlinked}")
    print(f"Files changed: {changed_files}")
    print("Samples (before -> after):")
    for fname, before, after in samples:
        print(f"  {fname}")
        print(f"    BEFORE: {before}")
        print(f"    AFTER:  {after}")


if __name__ == "__main__":
    main()
