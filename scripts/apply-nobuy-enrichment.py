#!/usr/bin/env python3
"""Apply honesty-judged no-buy enrichments to deep-page frontmatter.

Consumes the JSON the ecf-nobuy-storm workflow returns (a list of judged
enrichments) and writes no_buy_pct / free_checks / part_price into each target
page's frontmatter — deterministically, in the main loop, because workflow
subagents can't reliably write files.

Honesty is enforced upstream by the adversarial judge; this script only writes
what the judge approved:
  verdict "apply"             -> write no_buy_pct + free_checks + part_price
  verdict "apply_qualitative" -> write free_checks (+ part_price); pct stays null
  verdict "reject"            -> write nothing

Idempotent: a field already present in frontmatter is left as-is (never
clobbered), so re-runs and prior backfills are respected.

Usage:
  python scripts/apply-nobuy-enrichment.py <enrichments.json> [--apply]
  (default = dry run)
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

BLOG = Path(__file__).resolve().parent.parent / "src" / "data" / "blog"


def split_frontmatter(text: str):
    """Line-based split so a body `---` hrule can't be mistaken for the close."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, None


def yaml_quote(s: str) -> str:
    """Safe double-quoted YAML scalar: strip quotes/backslashes/em-dash/newlines.
    Backslash is neutralized because inside a double-quoted YAML scalar it is an
    escape introducer (a stray `\\n` two-char sequence would misparse)."""
    return (str(s or "").replace("\\", " ").replace('"', "'").replace("—", "-")
            .replace("\n", " ").replace("\r", " ").strip())


def has_key(fm: str, key: str) -> bool:
    """True iff `key` exists as an actual frontmatter key (line-anchored), not as
    a substring of a value or comment."""
    return re.search(rf"^\s*{re.escape(key)}\s*:", fm, re.MULTILINE) is not None


def insert_after(fm: str, anchor_keys, new_lines: str) -> str:
    """Insert new_lines after the first frontmatter line whose key is in
    anchor_keys; if none present, append at the end of the frontmatter."""
    fm_lines = fm.split("\n")
    for i, ln in enumerate(fm_lines):
        key = ln.split(":", 1)[0].strip()
        if key in anchor_keys:
            return "\n".join(fm_lines[: i + 1] + [new_lines] + fm_lines[i + 1:])
    return fm.rstrip("\n") + "\n" + new_lines


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: apply-nobuy-enrichment.py <enrichments.json> [--apply]")
        return 2
    apply = "--apply" in sys.argv
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    # Accept either the full workflow return ({applies|enrichments|...}) or a list.
    if isinstance(data, dict):
        items = data.get("applies") or data.get("enrichments") or []
    else:
        items = data

    wrote = skipped_reject = missing_file = nochange = 0
    for it in items:
        slug = it.get("slug", "")
        verdict = it.get("verdict", "")
        if verdict == "reject" or not slug:
            skipped_reject += 1
            continue
        f = BLOG / f"{slug}.md"
        if not f.exists():
            missing_file += 1
            print(f"  MISSING: {slug}.md")
            continue
        text = f.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if fm is None:
            missing_file += 1
            continue

        pct = it.get("no_buy_pct_final")
        checks = [yaml_quote(c) for c in (it.get("free_checks_final") or []) if yaml_quote(c)][:3]
        price = it.get("part_price_final")

        additions = []
        # free_checks (only if the page lacks them)
        if checks and not has_key(fm, "free_checks"):
            additions.append("free_checks:\n" + "\n".join(f'  - "{c}"' for c in checks))
        # no_buy_pct (only on verdict "apply", grounded, and not already present)
        if verdict == "apply" and pct and not has_key(fm, "no_buy_pct"):
            additions.append(f'no_buy_pct: "{yaml_quote(pct)}"')
        # part_price (only if the page lacks one — never clobber the backfill)
        if price and not has_key(fm, "part_price"):
            additions.append(f'part_price: "{yaml_quote(price)}"')

        if not additions:
            nochange += 1
            continue

        new_fm = insert_after(fm, {"diy_or_pro", "money_part", "likelihood", "most_likely_cause"},
                              "\n".join(additions))
        new_text = "---\n" + new_fm + "\n---\n" + body
        wrote += 1
        if apply:
            f.write_text(new_text, encoding="utf-8")
        elif wrote <= 10:
            print(f"  {slug}: +{', '.join(a.split(':')[0].split(chr(10))[0] for a in additions)}"
                  f"  (pct={pct if verdict=='apply' else 'qual'})")

    mode = "APPLIED" if apply else "DRY RUN (pass --apply to write)"
    print(
        f"\n{mode}\n"
        f"  pages written : {wrote}\n"
        f"  no change     : {nochange}\n"
        f"  rejected      : {skipped_reject}\n"
        f"  missing file  : {missing_file}\n"
        f"  total items   : {len(items)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
