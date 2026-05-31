#!/usr/bin/env python3
"""
Task 3: Convert wrong-product placeholder ASIN /dp/ links into Amazon SEARCH links.

Two ASINs were reused as stand-ins for many DIFFERENT parts:
  - B0CNZGZ1HS  (~221 files) -> assorted control boards
  - B0CZ7M9V4D  (~118 files) -> assorted flame sensors

A /dp/<ASIN> link to the WRONG product is worse than a search link. For every
Amazon link whose href contains one of these two ASINs, rewrite the href to:
    https://www.amazon.com/s?k=<urlencoded part name>&tag=errorcodefixes-20
keeping the SAME visible anchor text.

Part-name derivation (in priority order):
  1. If the anchor text is a real part name, use it (lightly cleaned of trailing
     " on Amazon" / "replacement on Amazon" noise for the SEARCH QUERY only).
  2. Else (anchor is a generic CTA like "Amazon" / "View on Amazon" /
     "Search on Amazon"), use the first cell ("Part" column) of the same markdown
     table row that contains the link.
  3. If neither yields a confident part name, leave that occurrence UNCHANGED and
     report it.

The anchor text is NEVER changed -- only the href.
"""
import re
import glob
import os
from urllib.parse import quote_plus

BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "data", "blog")
ASINS = ("B0CNZGZ1HS", "B0CZ7M9V4D")
TAG = "errorcodefixes-20"

# Generic, non-part anchors: must derive part name from the table row instead.
GENERIC_ANCHORS = {
    "amazon",
    "view on amazon",
    "search on amazon",
    "buy on amazon",
    "shop on amazon",
    "on amazon",
    "link",
    "here",
}

# A markdown link whose href contains one of the placeholder ASINs.
ASIN_LINK_RE = re.compile(
    r"\[([^\[\]]+?)\]\((https?://[^)]*(?:" + "|".join(ASINS) + r")[^)]*)\)"
)


def clean_query(anchor: str) -> str:
    """Turn a real-part-name anchor into a clean search query string."""
    q = anchor.strip()
    # Strip markdown emphasis markers if present (e.g. **text**).
    q = q.strip("*").strip()
    # Drop trailing CTA noise like "... on Amazon".
    q = re.sub(r"\s*\bon amazon\b\s*$", "", q, flags=re.IGNORECASE).strip()
    # Normalize internal whitespace.
    q = re.sub(r"\s+", " ", q)
    return q


def first_cell_part(line: str) -> str | None:
    """Given a markdown table-row line, return the trimmed first data cell.

    Rows look like:  | Drive control board | [Amazon](...) \\| notes |
    We take the first cell after the leading pipe. Returns None if not a usable
    table row or the first cell is empty / clearly not a part (a separator).
    """
    s = line.strip()
    if not s.startswith("|"):
        return None
    # Split on unescaped pipes only.
    parts = re.split(r"(?<!\\)\|", s)
    # parts[0] is '' (before leading pipe); first cell is parts[1].
    if len(parts) < 2:
        return None
    cell = parts[1].strip()
    if not cell:
        return None
    # Skip separator rows like ---, :---: etc.
    if re.fullmatch(r":?-{2,}:?", cell):
        return None
    # If the first cell itself is just a markdown link, pull its anchor.
    m = re.fullmatch(r"\[([^\[\]]+?)\]\([^)]*\)", cell)
    if m:
        cell = m.group(1).strip()
    # A header cell like "Part" or "Component" is not a real part name.
    if cell.lower() in {"part", "component", "parts", "item", "code", "fault"}:
        return None
    return cell


def main():
    files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.md")))
    converted = 0
    left = 0
    files_changed = 0
    samples = []
    left_report = []

    for fp in files:
        with open(fp, encoding="utf-8") as fh:
            txt = fh.read()
        lines = txt.split("\n")
        changed = False

        for i, line in enumerate(lines):
            if not any(a in line for a in ASINS):
                continue

            def repl(m):
                nonlocal converted, left, changed
                anchor, url = m.group(1), m.group(2)
                anchor_norm = re.sub(r"\s+", " ", anchor).strip().lower().strip("*").strip()

                # Determine the part name.
                part = None
                if anchor_norm in GENERIC_ANCHORS:
                    part = first_cell_part(line)
                else:
                    # Anchor is (presumably) a real part name.
                    cand = clean_query(anchor)
                    if cand:
                        part = cand

                if not part:
                    left += 1
                    if len(left_report) < 25:
                        left_report.append((os.path.basename(fp), i + 1, m.group(0)))
                    return m.group(0)  # leave unchanged

                new_url = f"https://www.amazon.com/s?k={quote_plus(part)}&tag={TAG}"
                converted += 1
                changed = True
                new_link = f"[{anchor}]({new_url})"
                if len(samples) < 3:
                    samples.append((os.path.basename(fp), m.group(0), new_link))
                return new_link

            lines[i] = ASIN_LINK_RE.sub(repl, line)

        if changed:
            new_txt = "\n".join(lines)
            with open(fp, "w", encoding="utf-8", newline="") as fh:
                fh.write(new_txt)
            files_changed += 1

    print("TASK 3 - Convert placeholder ASIN /dp/ links to SEARCH links")
    print(f"Links converted: {converted}")
    print(f"Links left unchanged (no confident part name): {left}")
    print(f"Files changed: {files_changed}")
    print("Samples (before -> after):")
    for fname, before, after in samples:
        print(f"  {fname}")
        print(f"    BEFORE: {before}")
        print(f"    AFTER:  {after}")
    if left_report:
        print("Left-unchanged occurrences:")
        for fname, ln, snippet in left_report:
            print(f"  {fname}:{ln}  {snippet}")


if __name__ == "__main__":
    main()
