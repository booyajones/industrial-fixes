#!/usr/bin/env python3
"""Backfill `most_likely_cause` onto money_part pages from their body — no LLM.

The no-buy card carries a "the usual culprit is X" line only when the page has
most_likely_cause. ~1,944 money_part pages lack it, so their card repeats a
near-identical generic lead (a scaled-content / duplication risk the storm
review flagged). Every deep page's body already has a "## Common Causes" section
whose FIRST bullet is the top cause (assemble_md sorts causes by share desc), so
we lift that bold lead phrase into frontmatter as most_likely_cause.

Conservative: only pages that (a) carry money_part, (b) lack most_likely_cause,
and (c) have a parseable first Common-Cause lead get touched. Never clobbers.

Usage: python scripts/backfill-most-likely-cause.py [--apply]   (default dry run)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

BLOG = Path(__file__).resolve().parent.parent / "src" / "data" / "blog"


def split_frontmatter(text: str):
    """Line-based; the closing delimiter is the first '---' line after line 0."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, None


def has_key(fm: str, key: str) -> bool:
    return re.search(rf"^\s*{re.escape(key)}\s*:", fm, re.MULTILINE) is not None


def yaml_quote(s: str) -> str:
    return (str(s or "").replace("\\", " ").replace('"', "'").replace("—", "-")
            .replace("\n", " ").replace("\r", " ").strip())


def derive_cause(body: str) -> str | None:
    """First bold lead under '## Common Causes' (or '## Causes'), %-stripped."""
    m = re.search(r"^##\s+Common Causes\s*$(.*?)(^##\s|\Z)", body,
                  re.MULTILINE | re.DOTALL)
    if not m:
        m = re.search(r"^##\s+Causes\s*$(.*?)(^##\s|\Z)", body,
                      re.MULTILINE | re.DOTALL)
    if not m:
        return None
    section = m.group(1)
    # First "- **Lead (~NN%)** text" bullet. Lead is the bold span; drop the %.
    b = re.search(r"^\s*-\s+\*\*(.+?)\*\*", section, re.MULTILINE)
    if not b:
        return None
    lead = b.group(1)
    lead = re.sub(r"\s*\(~?\d+%\)\s*$", "", lead).strip()  # strip trailing (~NN%)
    lead = re.sub(r"\s*\(~?\d+%\)", "", lead).strip()       # any stray (~NN%)
    # Strip a leading "E1:" / "F20 -" code prefix that sometimes bleeds into the lead.
    lead = re.sub(r"^[A-Z]{1,3}\d{0,4}\s*[:\-–]\s*", "", lead).strip()
    lead = lead.strip(" :-")
    # Sanity: a real cause phrase, not a whole sentence or empty.
    if not lead or len(lead) < 4 or len(lead) > 90:
        return None
    return lead


def main() -> int:
    apply = "--apply" in sys.argv
    files = sorted(BLOG.glob("*.md"))
    wrote = skip_nopart = skip_has = skip_noparse = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue
        if not has_key(fm, "money_part"):
            skip_nopart += 1
            continue
        if has_key(fm, "most_likely_cause"):
            skip_has += 1
            continue
        cause = derive_cause(body or "")
        if not cause:
            skip_noparse += 1
            continue
        line = f'most_likely_cause: "{yaml_quote(cause)}"'
        # Insert after money_part (keeps the verdict fields grouped).
        new_fm = re.sub(r"(^money_part:.*$)", r"\1\n" + line, fm, count=1,
                        flags=re.MULTILINE)
        if new_fm == fm:  # money_part not at line start for some reason
            new_fm = fm.rstrip("\n") + "\n" + line
        new_text = "---\n" + new_fm + "\n---\n" + body
        wrote += 1
        if apply:
            f.write_text(new_text, encoding="utf-8")
        elif wrote <= 10:
            print(f"  {f.name}: most_likely_cause -> {cause}")

    mode = "APPLIED" if apply else "DRY RUN (pass --apply to write)"
    print(
        f"\n{mode}\n"
        f"  would set most_likely_cause : {wrote}\n"
        f"  already had it              : {skip_has}\n"
        f"  no money_part (skip)        : {skip_nopart}\n"
        f"  no parseable cause          : {skip_noparse}\n"
        f"  total scanned               : {len(files)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
