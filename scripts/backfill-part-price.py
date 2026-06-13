#!/usr/bin/env python3
"""Backfill `part_price` onto existing deep code pages — no LLM, no fabrication.

The no-buy verdict (NoBuyVerdict.astro) renders qualitatively from
most_likely_cause + money_part alone, but sharpens with a price anchor
("A new drain pump runs about $80-150"). Newer pages already carry an
embedded "Rough cost:" line in the body ("DIY runs about $80-150 ..."), so we
parse that and lift the DIY dollar range into frontmatter as `part_price`.

Conservative by design: only pages that (a) carry a money_part, (b) do NOT
already have part_price, and (c) have a parseable "$N-M" DIY range get touched.
free_checks and no_buy_pct are intentionally NOT derived here — they need the
generator's judgment, not a regex, and we never invent a number.

Usage: python scripts/backfill-part-price.py [--apply]   (default = dry run)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

BLOG = Path(__file__).resolve().parent.parent / "src" / "data" / "blog"

# "DIY runs about $80-150 ..." / "DIY costs around $45 to $70 ..." — grab the
# first dollar amount (optionally a range) after the DIY cue.
DIY_RANGE = re.compile(
    r"DIY[^.$]*?\$\s?(\d[\d,]*)\s*(?:-|–|to)\s*\$?\s?(\d[\d,]*)",
    re.IGNORECASE,
)
DIY_SINGLE = re.compile(r"DIY[^.$]*?\$\s?(\d[\d,]*)", re.IGNORECASE)


def split_frontmatter(text: str):
    """Return (fm, body) or (None, None) if no leading --- block.

    Line-based so a Markdown horizontal rule (`---` on its own line) inside the
    body can never be mistaken for the closing frontmatter delimiter. The
    closing delimiter is the first line *after* line 0 that is exactly '---'.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1:])  # excludes the closing delimiter
            return fm, body
    return None, None


def derive_price(body: str) -> str | None:
    m = DIY_RANGE.search(body)
    if m:
        lo, hi = m.group(1).replace(",", ""), m.group(2).replace(",", "")
        # Guard: hi >= lo, sane ceiling, and a real part costs at least a few
        # dollars — a "$0-15" low bound means the fix is essentially free, where
        # a part-price anchor would mislead (the qualitative verdict carries it).
        try:
            if 5 <= int(lo) and int(hi) >= int(lo) and int(hi) <= 5000:
                return f"${lo}-{hi}"
        except ValueError:
            return None
    m = DIY_SINGLE.search(body)
    if m:
        v = m.group(1).replace(",", "")
        try:
            if 5 <= int(v) <= 5000:
                return f"about ${v}"
        except ValueError:
            return None
    return None


def main() -> int:
    apply = "--apply" in sys.argv
    files = sorted(BLOG.glob("*.md"))
    touched = skipped_no_part = skipped_has_price = skipped_no_price = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            continue
        if "money_part:" not in fm:
            skipped_no_part += 1
            continue
        if re.search(r"^part_price:", fm, re.MULTILINE):
            skipped_has_price += 1
            continue
        price = derive_price(body or "")
        if not price:
            skipped_no_price += 1
            continue
        # Insert part_price right after the money_part line, preserving order.
        new_fm = re.sub(
            r"(^money_part:.*$)",
            r'\1\n' + f'part_price: "{price}"',
            fm,
            count=1,
            flags=re.MULTILINE,
        )
        new_text = "---\n" + new_fm + "\n---\n" + body
        touched += 1
        if apply:
            f.write_text(new_text, encoding="utf-8")
        elif touched <= 8:
            print(f"  {f.name}: part_price -> {price}")

    mode = "APPLIED" if apply else "DRY RUN (pass --apply to write)"
    print(
        f"\n{mode}\n"
        f"  would set part_price on : {touched}\n"
        f"  already had part_price  : {skipped_has_price}\n"
        f"  no money_part (skip)    : {skipped_no_part}\n"
        f"  no parseable DIY price  : {skipped_no_price}\n"
        f"  total files scanned     : {len(files)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
