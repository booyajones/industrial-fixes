#!/usr/bin/env python3
"""
Deep-regenerate existing top consumer error-code pages to Diagnosis Command
Center depth (most-likely-cause verdict, decision tree, misdiagnosis warning,
cost math, accurate DIY/Pro signal).

Reuses generate-articles.py (Perplexity research + deep claude_write + review +
assemble_md). It OVERWRITES an existing page only when the new deep version
passes the review gate (score >= 7), so regeneration can only improve a live
page, never downgrade a good one to a draft.

USAGE:
  python scripts/regen-deep.py --dry --count 30        # list targets, write nothing
  python scripts/regen-deep.py --count 3 --jobs 3      # deep-regen 3 (sample test)
  python scripts/regen-deep.py --count 150 --jobs 3    # the storm
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"
_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_lock = threading.Lock()
_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}

CONSUMER_BRANDS = ["samsung", "lg", "whirlpool", "ge", "maytag", "frigidaire",
                   "bosch", "kitchenaid", "kenmore", "electrolux", "amana"]
APPLIANCES = ["washer", "dryer", "refrigerator", "dishwasher", "range", "oven", "microwave"]
PRIORITY = {b: i for i, b in enumerate(CONSUMER_BRANDS)}


def is_target(slug: str, head: str) -> bool:
    if not slug.endswith("-error-code"):
        return False
    if re.search(r"^draft:\s*true", head, re.M):
        return False
    if re.search(r"^diy_or_pro:", head, re.M):  # already deepened; skip so re-runs are idempotent
        return False
    if not any(b in slug for b in CONSUMER_BRANDS):
        return False
    if not any(a in slug for a in APPLIANCES):
        return False
    return True


def topic_from(md: str) -> str | None:
    m = re.search(r'^title:\s*"(.+?)"', md, re.M)
    if not m:
        return None
    t = re.sub(r'\s*[-–—]\s*(causes|signs|what|how).*$', '', m.group(1), flags=re.I).strip()
    return t or None


def regen_one(path: Path) -> tuple[str, str, str]:
    slug = path.stem
    md = path.read_text(encoding="utf-8")
    topic = topic_from(md)
    if not topic:
        return (slug, "skip", "no title")
    try:
        research = G.perplexity_research(topic)
        content = G.claude_write(topic, research)
        if not content:
            return (slug, "fail", "no content")
        verdict = G.claude_review(topic, content, research)
        ok = bool(verdict.get("publish")) and int(verdict.get("score") or 0) >= 7
        if not ok:
            return (slug, "keep", f"review={verdict.get('score')} kept existing")
        new_md = G.assemble_md(topic, content, slug, draft=False)
        if G.BANNED.search(new_md):
            new_md = G.BANNED.sub(lambda m: _FIX.get(m.group(0).lower(), m.group(0)), new_md)
        with _lock:
            path.write_text(new_md, encoding="utf-8")
        return (slug, "deep", f"score={verdict.get('score')}")
    except Exception as e:
        return (slug, "fail", str(e)[:120])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    if not args.dry and not getattr(G, "ANTHROPIC_KEY", ""):
        print("[!] set ANTHROPIC_API_KEY first.")
        return 1

    targets: list[Path] = []
    for p in sorted(G.BLOG_DIR.glob("*.md")):
        head = p.read_text(encoding="utf-8")[:600]
        if is_target(p.stem, head):
            targets.append(p)

    def prio(p: Path):
        for b, i in PRIORITY.items():
            if b in p.stem:
                return (i, p.stem)
        return (99, p.stem)

    targets.sort(key=prio)
    targets = targets[: args.count]
    print(f"[i] {len(targets)} consumer code pages to deep-regenerate (jobs={args.jobs})")
    if args.dry:
        for p in targets[:40]:
            print("   ", p.stem)
        return 0

    res: dict[str, int] = {}
    done = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(regen_one, p): p for p in targets}
        for f in as_completed(futs):
            slug, status, info = f.result()
            res[status] = res.get(status, 0) + 1
            done += 1
            if done % 5 == 0 or status in ("fail", "deep"):
                print(f"  [{done}/{len(targets)}] {status:5} {slug}  {info}")
    print(f"\n[+] done: {res}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
