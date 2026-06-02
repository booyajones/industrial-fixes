#!/usr/bin/env python3
"""
Pre-ship content QA scan for generated articles.

Fast, deterministic checks that catch the failure modes the LLM gate can miss:
thin content, empty sections, banned words, leftover placeholders/anchors, broken
frontmatter, missing parts table. Complements (does not replace) the FQE gate
(mojibake + astro check) and any adversarial QA swarm.

USAGE:
  python scripts/qa-scan.py FILE [FILE ...]      # scan specific files
  python scripts/qa-scan.py --git                # scan new/modified blog .md vs HEAD
  python scripts/qa-scan.py --all                # scan every blog .md
Exit code 0 if no HARD failures, 1 otherwise (so it can gate CI).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
BANNED = re.compile(r"\b(ensure|crucial|vital|leverage|robust|seamless)\b", re.I)
PLACEHOLDER = re.compile(r"\b(lorem ipsum|TODO|FIXME|TBD|xxxx|insert here)\b", re.I)
# NOTE: raw "{#fix}" in headings is INTENTIONAL Pandoc anchor syntax that the
# remark-heading-ids build plugin strips to an id. It is NOT garbage, so we do
# not flag it here.


def fm_field(block: str, name: str) -> str | None:
    m = re.search(rf"^{name}:\s*(.+)$", block, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else None


def scan(path: Path) -> list[str]:
    """Return a list of HARD failures for this file (empty = clean)."""
    fails: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"unreadable: {e}"]
    fm = re.search(r"^---\s*\n(.*?)^---\s*$", text, re.DOTALL | re.MULTILINE)
    if not fm:
        return ["no frontmatter"]
    block = fm.group(1)
    body = text[fm.end():]

    title = fm_field(block, "title")
    desc = fm_field(block, "description")
    if not title:
        fails.append("missing title")
    elif len(title) > 90:
        fails.append(f"title too long ({len(title)})")
    if not desc:
        fails.append("missing description")
    elif not (40 <= len(desc) <= 200):
        fails.append(f"description length {len(desc)} (want 40-200)")
    if not fm_field(block, "pubDatetime"):
        fails.append("missing pubDatetime")
    if "tags:" not in block:
        fails.append("missing tags")

    # body checks
    headings = re.findall(r"^##\s+(.+)$", body, re.MULTILINE)
    if len(headings) < 3:
        fails.append(f"only {len(headings)} sections (thin)")
    if len(body.strip()) < 600:
        fails.append(f"body too short ({len(body.strip())} chars)")
    if BANNED.search(body):
        fails.append(f"banned word: {BANNED.search(body).group(0)}")
    if PLACEHOLDER.search(body):
        fails.append(f"placeholder: {PLACEHOLDER.search(body).group(0)}")
    # parts/affiliate presence: at least one amazon link or specialist
    if "amazon.com" not in text and "Parts" not in body:
        fails.append("no parts/affiliate content")
    # empty section check (split on headings; avoids regex DOTALL greediness)
    for sec in re.split(r"^##\s+", body, flags=re.MULTILINE)[1:]:
        parts = sec.split("\n", 1)
        content = parts[1].strip() if len(parts) > 1 else ""
        if len(content) < 20:
            fails.append("empty/near-empty section")
            break
    return fails


def git_new_files() -> list[Path]:
    out = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain", "--", "src/data/blog"],
                         capture_output=True, text=True).stdout
    files = []
    for line in out.splitlines():
        # format: "XY path"
        p = line[3:].strip().strip('"')
        if p.endswith(".md"):
            files.append(ROOT / p)
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--git", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--show", type=int, default=25, help="max failing files to list")
    args = ap.parse_args()

    if args.git:
        targets = git_new_files()
    elif args.all:
        targets = sorted(BLOG.glob("*.md"))
    else:
        targets = [Path(f) for f in args.files]
    if not targets:
        print("[i] no files to scan")
        return 0

    bad: dict[str, list[str]] = {}
    from collections import Counter
    by_type: Counter = Counter()
    for p in targets:
        fails = scan(p)
        if fails:
            bad[p.name] = fails
            for f in fails:
                by_type[f.split(":")[0].split("(")[0].strip()] += 1

    print(f"[i] scanned {len(targets)} files | {len(bad)} with issues")
    if by_type:
        print("[i] issue counts by type:")
        for t, n in by_type.most_common():
            print(f"      {n:4}  {t}")
    if bad:
        print(f"[i] first {min(args.show, len(bad))} failing files:")
        for name, fails in list(bad.items())[: args.show]:
            print(f"   - {name}: {'; '.join(fails)}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
