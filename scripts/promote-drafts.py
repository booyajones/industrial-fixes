#!/usr/bin/env python3
"""
Promote wrongly-drafted non-code pages to published.

The shared claude_review gate is CODE-specific ("is this a real documented error
code?") so it wrongly drafts part/symptom/model pages, which are not about codes.
This flips draft:true -> draft:false for those page types when the article is
clearly well-formed (real sections + parts table + enough body). Code articles are
left alone (their gate is correct). Idempotent.

USAGE: python scripts/promote-drafts.py [--dry]
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
TYPE_TAGS = ("parts", "symptom", "model")


def well_formed(text: str) -> bool:
    body = re.split(r"^---\s*$", text, maxsplit=2, flags=re.M)
    body = body[2] if len(body) >= 3 else text
    sections = len(re.findall(r"^##\s+", body, re.M))
    has_parts = ("| Part |" in body) or ("amazon.com" in body)
    return sections >= 4 and has_parts and len(body.strip()) >= 1200


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    promoted = held = skipped = 0
    for p in BLOG.glob("*.md"):
        text = p.read_text(encoding="utf-8")
        fm = re.search(r"^---\s*\n(.*?)^---", text, re.DOTALL | re.M)
        if not fm:
            continue
        block = fm.group(1)
        if "draft: true" not in block:
            continue
        tags = re.findall(r"^\s*-\s*(\S+)\s*$", block, re.M)
        if not any(t in TYPE_TAGS for t in tags):
            continue  # leave code articles to their (correct) gate
        if not well_formed(text):
            held += 1
            continue
        if args.dry:
            promoted += 1
            continue
        new = text.replace("draft: true", "draft: false", 1)
        p.write_text(new, encoding="utf-8")
        promoted += 1
    print(f"[+] {'(dry) ' if args.dry else ''}promoted {promoted} | left held (not well-formed) {held}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
