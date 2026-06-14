#!/usr/bin/env python3
"""Deterministic no-buy enrichment — research + adversarial honesty-judge per code.

The agent-storm version hits the shared Anthropic key's concurrency throttle
(it runs ~14 agents at once; the key tolerates ~3-4). This does the same work
sequentially with the repo's proven _post_json backoff (retries=9), so it
actually completes. Two calls per code:
  1. research  -> a master-tech estimate of {no_buy_pct, free_checks, part_price}
  2. judge     -> an independent adversarial pass that may null an over-confident
                  pct or reject (HARD rule: never fabricate a number; never call a
                  sealed/refrigerant/compressor/igniter fault a cheap fix)

Writes a JSON list of judged enrichments (the shape apply-nobuy-enrichment.py
consumes). Apply with: python scripts/apply-nobuy-enrichment.py <out.json> --apply

Usage: python scripts/enrich-nobuy.py <targets.json> <out.json>
"""
from __future__ import annotations
import json
import os
import re
import sys
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent.parent
# Reuse the generator's hardened HTTP-with-backoff helper.
spec = importlib.util.spec_from_file_location("genart", ROOT / "scripts" / "generate-articles.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-sonnet-4-5-20250929"
HARD = (
    "HARD HONESTY RULE (non-negotiable): NEVER fabricate a number. A no_buy_pct must be a "
    "defensible field-frequency estimate from well-established appliance-repair knowledge, not "
    "invented precision; when unsure return null. NEVER label a refrigerant / sealed-system / "
    "compressor / high-voltage / igniter / heating-element fault a 'cheap fix' — those are usually "
    "the part itself. Round honest estimates (say '70%', not '68%')."
)


def call(prompt: str, max_tokens: int = 700) -> dict | None:
    if not KEY:
        print("  [no ANTHROPIC_API_KEY]"); return None
    body = {"model": MODEL, "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]}
    try:
        resp = G._post_json(
            "https://api.anthropic.com/v1/messages",
            {"x-api-key": KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
            body, 60, retries=9,
        )
        text = "".join(b.get("text", "") for b in resp.get("content", []))
        m = re.search(r"\{.*\}", text, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception as e:
        print(f"  call failed: {str(e)[:90]}")
        return None


def research(t: dict) -> dict | None:
    return call(
        f"{HARD}\nYou are a master appliance-repair tech with deep field experience on "
        f"{t['brand'].upper()} {t['appl']}s. For the {t['brand'].upper()} {t['appl']} {t['code']} "
        f"error code (the page's #1 part is \"{t['part']}\"), return ONLY a JSON object:\n"
        '{"no_buy_pct": "<e.g. 70%, the share of real-world cases that are a free/cheap fix '
        '(clog, kink, reset, loose connector) rather than a failed part; null if this code is '
        'genuinely usually the part itself>", '
        '"free_checks": ["<2-3 specific $0/near-$0 things to try FIRST, in order>"], '
        '"part_price": "<typical US street price RANGE for the part, e.g. $45-90>", '
        '"confidence": "<high|medium|low>", "rationale": "<one line>"}'
    )


def judge(t: dict, res: dict) -> dict | None:
    return call(
        f"{HARD}\nAdversarial honesty auditor. A tech proposed this no-buy data for the "
        f"{t['brand'].upper()} {t['appl']} {t['code']} code (part: \"{t['part']}\"):\n{json.dumps(res)}\n\n"
        "Return ONLY a JSON object:\n"
        '{"verdict": "<apply | apply_qualitative | reject>", '
        '"no_buy_pct_final": "<kept+rounded percent string, or null>", '
        '"free_checks_final": ["<2-3 cleaned imperative checks>"], '
        '"part_price_final": "<sane range string or null>", "reason": "<one line>"}\n'
        "apply = no_buy_pct is a defensible estimate AND checks are free/safe/correct. "
        "apply_qualitative = checks good but pct not safely groundable (no_buy_pct_final=null). "
        "reject = code is genuinely usually the part itself, or checks wrong/unsafe."
    )


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: enrich-nobuy.py <targets.json> <out.json>"); return 2
    targets = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = []
    for i, t in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {t['brand']} {t['code']} ...", flush=True)
        r = research(t)
        if not r:
            print("  research failed; skip"); continue
        j = judge(t, r)
        if not j:
            print("  judge failed; skip"); continue
        j["slug"] = t["slug"]  # ensure slug is exact
        out.append(j)
        print(f"  {j.get('verdict')}: pct={j.get('no_buy_pct_final')} "
              f"checks={len(j.get('free_checks_final') or [])} price={j.get('part_price_final')}")
    Path(sys.argv[2]).write_text(json.dumps(out, indent=2), encoding="utf-8")
    va = sum(1 for j in out if j.get("verdict") == "apply")
    vq = sum(1 for j in out if j.get("verdict") == "apply_qualitative")
    vr = sum(1 for j in out if j.get("verdict") == "reject")
    print(f"\nwrote {sys.argv[2]}: {len(out)} judged | apply {va} | qualitative {vq} | reject {vr}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
