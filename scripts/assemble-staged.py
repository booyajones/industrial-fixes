#!/usr/bin/env python3
"""
Assemble staged article JSON (from the generation swarm) into house-template .md.

Each scripts/staging/*.json holds the claude_write JSON shape (title, description,
equipment_category, brand_slug, what_it_means, causes, steps, parts,
when_to_call_pro) plus topic/slug. This reuses generate-articles.assemble_md so the
template, frontmatter, Amazon noskim links, equip tag, gas-safety tag, and
banned-word scrub are byte-identical to the deterministic engine. Skips slugs that
already exist on disk and within-run duplicates. Idempotent.

USAGE:  python scripts/assemble-staged.py
        python scripts/assemble-staged.py --dir scripts/staging
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"

_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}
# assemble_md accesses these with [] (hard-required); causes/steps/parts via .get.
REQ = ["title", "description", "what_it_means", "when_to_call_pro",
       "causes", "steps", "parts"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(ROOT / "scripts" / "staging"))
    args = ap.parse_args()
    staging = Path(args.dir)
    if not staging.exists():
        print(f"[!] staging dir not found: {staging}")
        return 1

    have = G.existing_slugs()
    seen: set[str] = set()
    res = {"written": 0, "skip_exist": 0, "skip_dup": 0, "bad": 0}
    for f in sorted(staging.glob("*.json")):
        try:
            c = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            res["bad"] += 1
            print(f"  [bad json] {f.name}: {str(e)[:80]}")
            continue
        topic = c.get("topic") or c.get("title", "")
        slug = c.get("slug") or G.slugify(topic)
        if not slug or any(k not in c for k in REQ):
            res["bad"] += 1
            print(f"  [missing fields] {f.name}")
            continue
        if slug in have:
            res["skip_exist"] += 1
            continue
        if slug in seen:
            res["skip_dup"] += 1
            continue
        seen.add(slug)
        try:
            md = G.assemble_md(topic, c, slug, draft=False)
            if G.BANNED.search(md):
                md = G.BANNED.sub(lambda m: _FIX.get(m.group(0).lower(), m.group(0)), md)
            (G.BLOG_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
            res["written"] += 1
        except Exception as e:
            res["bad"] += 1
            print(f"  [assemble fail] {slug}: {str(e)[:120]}")
    print(f"[+] assembled: {res}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
