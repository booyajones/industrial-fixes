#!/usr/bin/env python3
"""
Parallel batch generator for the consumer-codes pivot.

Reuses the grounding (Perplexity) + quality gate (claude_review) + house template
from generate-articles.py, but runs many topics CONCURRENTLY. Article generation
is I/O-bound on API calls, so a thread pool gives near-linear speedup and lets us
ship grounded content at scale without a parallel engine rewrite.

Each topic runs: Perplexity research -> Claude write -> Claude review gate
(publish only if the code is real AND score >= 7; otherwise draft:true, held and
NOT built). Per-slug .md writes are independent; the shared `have` set and the
state file are guarded so the run is thread-safe.

TOPIC SOURCE (pick one):
  --batch-json PATH   a consumer-pivot batch file; uses first_batch/ranked_full
  --pool              scripts/.code-pool.json candidates (real mined codes)
  --topics-file PATH  one topic per line

REQUIRES (in env, same as generate-articles.py): ANTHROPIC_API_KEY,
PERPLEXITY_API_KEY. Env must be set BEFORE running (keys are captured at import).

USAGE:
  python scripts/generate-batch.py --batch-json automation/consumer-pivot-batch1.json --field ranked_full --jobs 10
  python scripts/generate-batch.py --pool --count 300 --jobs 10
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"

# Load generate-articles.py as a module despite the hyphen in its name.
_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_lock = threading.Lock()
_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}


def gen_one(topic: str, have: set) -> tuple[str, str, str]:
    slug = G.slugify(topic)
    with _lock:
        if slug in have:
            return (slug, "skip", "exists")
        have.add(slug)
    try:
        research = G.perplexity_research(topic)
        content = G.claude_write(topic, research)
        if not content:
            return (slug, "fail", "no content")
        verdict = G.claude_review(topic, content, research)
        publish = bool(verdict.get("publish")) and int(verdict.get("score", 0)) >= 7
        md = G.assemble_md(topic, content, slug, draft=not publish)
        if G.BANNED.search(md):
            md = G.BANNED.sub(lambda m: _FIX.get(m.group(0).lower(), m.group(0)), md)
        (G.BLOG_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
        return (slug, "publish" if publish else "draft", f"score={verdict.get('score')}")
    except Exception as e:  # one bad topic must never kill the wave
        return (slug, "fail", str(e)[:120])


def load_topics(args) -> list[str]:
    if args.topics_file:
        return [l.strip() for l in Path(args.topics_file).read_text(encoding="utf-8").splitlines() if l.strip()]
    if args.batch_json:
        d = json.loads(Path(args.batch_json).read_text(encoding="utf-8"))
        items = d.get(args.field) or d.get("first_batch") or d.get("ranked_full") or []
        out = []
        for x in items:
            if isinstance(x, str):
                out.append(x)
            else:
                out.append(" ".join(filter(None, [x.get("brand", ""), x.get("appliance", ""), x.get("code", ""), "error code"])))
        return out
    if args.pool:
        p = ROOT / "scripts" / ".code-pool.json"
        return json.loads(p.read_text(encoding="utf-8")).get("candidates", []) if p.exists() else []
    return []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", action="store_true")
    ap.add_argument("--topics-file")
    ap.add_argument("--batch-json")
    ap.add_argument("--field", default="ranked_full", help="which array in the batch-json to use")
    ap.add_argument("--count", type=int, default=0, help="cap number generated (0 = all)")
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()

    # Fail loud if keys are missing — otherwise every topic silently returns
    # "no content" and a whole wave looks like a content problem, not config.
    if not getattr(G, "ANTHROPIC_KEY", "") or not getattr(G, "PERPLEXITY_KEY", ""):
        print("[!] ANTHROPIC_API_KEY and PERPLEXITY_API_KEY must be set in env before running.")
        return 1

    topics = load_topics(args)
    have = G.existing_slugs()
    seen, uniq = set(), []
    for t in topics:
        s = G.slugify(t)
        if s in seen or s in have:
            continue
        seen.add(s)
        uniq.append(t)
    if args.count:
        uniq = uniq[: args.count]
    print(f"[i] {len(uniq)} new topics to generate (jobs={args.jobs})")

    res = {"publish": 0, "draft": 0, "fail": 0, "skip": 0}
    new_state: dict[str, dict] = {}
    done = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(gen_one, t, have): t for t in uniq}
        for f in as_completed(futs):
            slug, status, info = f.result()
            res[status] = res.get(status, 0) + 1
            done += 1
            if status in ("publish", "draft"):
                new_state[slug] = {"topic": futs[f], "date": date.today().isoformat()}
            if done % 10 == 0 or status == "fail":
                print(f"  [{done}/{len(uniq)}] {status:7} {slug}  {info}")

    sp = ROOT / "scripts" / ".generated-articles.json"
    old = json.loads(sp.read_text()) if sp.exists() else {"generated": {}}
    old.setdefault("generated", {}).update(new_state)
    tmp = sp.with_suffix(".json.tmp")  # atomic replace so a crash can't truncate state
    tmp.write_text(json.dumps(old, indent=2))
    tmp.replace(sp)
    print(f"\n[+] done: {res}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
