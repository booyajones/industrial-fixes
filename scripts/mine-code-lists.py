#!/usr/bin/env python3
"""
Manufacturer code-list miner — the renewable REAL-code feeder.

For each brand/equipment we cover, ask Perplexity to enumerate the actual
documented error/fault/alarm codes (grounded in manufacturer docs), parse them
into candidate article topics, dedupe against what we already publish, and write
them to scripts/.code-pool.json. generate-articles.py consumes that pool as a
high-priority demand source.

This is what sustains the paced ramp to thousands WITHOUT inventing codes:
every candidate here came from a real documented list, and the article
generator's quality gate still independently verifies each one before publish.

REQUIRES: PERPLEXITY_API_KEY

USAGE:
    python scripts/mine-code-lists.py                 # mine all seeds, merge pool
    python scripts/mine-code-lists.py --brand "ABB ACS580" --equip "VFD fault"
    python scripts/mine-code-lists.py --limit 5       # only first N seeds (testing)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "src" / "data" / "blog"
POOL = ROOT / "scripts" / ".code-pool.json"
PERPLEXITY_KEY = os.environ.get("PERPLEXITY_API_KEY", "")

# (brand label, equipment + code-term). The code-term matches how people search
# and how we title (error code / fault code / alarm). Derived from our actual
# tag coverage. Add freely; re-run is idempotent.
SEEDS = [
    # VFDs / drives — fault codes
    ("ABB ACS580", "VFD fault code"), ("ABB ACS550", "VFD fault code"),
    ("ABB ACS355", "VFD fault code"), ("Siemens G120", "VFD fault code"),
    ("Siemens Micromaster", "VFD fault code"), ("Danfoss FC302", "VFD fault code"),
    ("Danfoss VLT", "VFD fault code"), ("Yaskawa GA800", "VFD fault code"),
    ("Yaskawa A1000", "VFD fault code"), ("Allen-Bradley PowerFlex 525", "VFD fault code"),
    ("Allen-Bradley PowerFlex 753", "VFD fault code"),
    # CNC — alarm codes
    ("Fanuc", "CNC alarm code"), ("Haas", "CNC alarm code"),
    ("Mazak", "CNC alarm code"), ("Okuma", "CNC alarm code"),
    ("Siemens Sinumerik", "CNC alarm code"),
    # HVAC — error codes
    ("Carrier", "furnace error code"), ("Trane", "furnace error code"),
    ("Lennox", "furnace error code"), ("Goodman", "furnace error code"),
    ("York", "furnace error code"), ("Daikin", "mini split error code"),
    ("Mitsubishi", "mini split error code"), ("LG", "mini split error code"),
    ("Fujitsu", "mini split error code"),
    # Water heaters / boilers — error codes
    ("Rheem", "tankless water heater error code"), ("Navien", "tankless error code"),
    ("Rinnai", "tankless error code"), ("Weil-McLain", "boiler error code"),
    ("Bosch", "tankless error code"), ("Noritz", "tankless error code"),
    # Refrigeration / ice machines — error codes
    ("Hoshizaki", "ice machine error code"), ("Manitowoc", "ice machine error code"),
    ("Scotsman", "ice machine error code"), ("True", "refrigeration error code"),
]

# Consumer / residential appliances + HVAC — the 2026-06 demand pivot. Mainstream
# brands homeowners actually search, phrased the way we title + people search.
# This is the renewable feeder that lets the daily pipeline keep producing
# consumer content after the initial waves. Idempotent: re-runs dedupe.
_CONSUMER = {
    "washer error code": ["Whirlpool", "Samsung", "LG", "Maytag", "GE", "Frigidaire", "Kenmore", "Electrolux", "Bosch", "Speed Queen", "Amana"],
    "dryer error code": ["Whirlpool", "Samsung", "LG", "Maytag", "GE", "Frigidaire", "Kenmore", "Electrolux", "Amana"],
    "dishwasher error code": ["Bosch", "Whirlpool", "Samsung", "LG", "KitchenAid", "GE", "Frigidaire", "Maytag", "Kenmore", "Amana"],
    "refrigerator error code": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid", "Kenmore", "Bosch", "Maytag", "Amana"],
    "oven error code": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid", "Maytag", "Bosch", "Kenmore", "Amana"],
    "range error code": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid", "Maytag", "Kenmore"],
    "microwave error code": ["Samsung", "LG", "GE", "Whirlpool", "Panasonic", "Kenmore"],
    "furnace error code": ["Carrier", "Goodman", "Lennox", "Trane", "Rheem", "York", "Bryant", "American Standard", "Amana", "Ruud", "Payne"],
    "mini split error code": ["Mitsubishi", "Daikin", "LG", "Fujitsu", "Senville", "MRCOOL", "Gree", "Pioneer", "Cooper and Hunter"],
    "heat pump error code": ["Mitsubishi", "Daikin", "Carrier", "Goodman", "Trane", "Bosch", "Rheem"],
    "tankless water heater error code": ["Rheem", "Navien", "Rinnai", "A.O. Smith", "Bosch", "Noritz", "Takagi", "Ruud", "State"],
    "water heater error code": ["Rheem", "A.O. Smith", "Bradford White", "GE", "Whirlpool", "State"],
}
# dict.fromkeys dedupes exact (brand, equip) tuples (some consumer seeds overlap
# the original industrial HVAC seeds) so we don't waste Perplexity calls re-mining.
SEEDS = list(dict.fromkeys(SEEDS + [(brand, equip) for equip, brands in _CONSUMER.items() for brand in brands]))

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ecf-miner/1.0"
STOP = {"error", "code", "codes", "fault", "alarm", "the", "and"}


def slugify(t: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def sig(t: str) -> frozenset:
    return frozenset(x for x in re.findall(r"[a-z0-9]+", t.lower()) if x not in STOP and len(x) >= 2)


def existing_sigs() -> list:
    return [sig(p.stem) for p in BLOG_DIR.glob("*.md")]


def mine(brand: str, equip: str) -> list[str]:
    """Ask Perplexity for the real documented codes for this brand/equipment."""
    if not PERPLEXITY_KEY:
        return []
    prompt = (
        f"List the documented {brand} {equip}s from official manufacturer "
        f"documentation. Output ONLY a plain list, one per line, in the exact "
        f"format: CODE | short meaning. Use the real code as printed (e.g. E04, "
        f"F0001, AL-29, Alarm 401). Include only codes that genuinely exist in "
        f"{brand} documentation. Be comprehensive but do not invent codes."
    )
    body = {"model": "sonar", "messages": [
        {"role": "system", "content": "You are an industrial documentation indexer. Only list real, documented codes."},
        {"role": "user", "content": prompt}], "max_tokens": 1200}
    try:
        req = urllib.request.Request("https://api.perplexity.ai/chat/completions",
            data=json.dumps(body).encode(), method="POST",
            headers={"Authorization": f"Bearer {PERPLEXITY_KEY}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            text = json.load(r)["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  [perplexity] {brand}: {e}")
        return []
    topics = []
    for line in text.splitlines():
        line = line.strip().lstrip("-*•0123456789. ").strip()
        if "|" not in line:
            continue
        code = line.split("|", 1)[0].strip().strip("`*")
        # A plausible code: short, not a sentence, and EITHER contains a digit
        # (F21, E04) OR is a short all-letter code (OE, LE, FF, HE, dE) which is
        # common on consumer appliances. The article generator's review gate still
        # independently verifies each code is real before publish.
        plausible = bool(re.search(r"\d", code)) or bool(re.fullmatch(r"[A-Za-z]{2,4}", code))
        if not plausible or len(code) > 16 or len(code.split()) > 3:
            continue
        code = re.sub(r"\s+", " ", code)
        # Topic phrased the way we title + people search. INCLUDE the appliance /
        # equipment descriptor (washer, dryer, mini split, furnace) so the topic is
        # SPECIFIC: a bare "Whirlpool E02" means different things on a washer vs an
        # oven, which produces ambiguous, low-ranking articles.
        noun = "alarm" if "alarm" in equip else ("fault code" if "fault" in equip else "error code")
        desc = re.sub(r"\b(error|fault|alarm)\b.*$", "", equip, flags=re.I).strip()
        topic = re.sub(r"\s+", " ", f"{brand} {desc} {code} {noun}").strip()
        topics.append(topic)
    return topics


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand"); ap.add_argument("--equip")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    if not PERPLEXITY_KEY:
        print("[!] PERPLEXITY_API_KEY not set."); return 1

    seeds = [(args.brand, args.equip)] if args.brand else SEEDS
    if args.limit:
        seeds = seeds[: args.limit]

    have = existing_sigs()
    pool = json.loads(POOL.read_text()) if POOL.exists() else {"candidates": []}
    seen = {sig(c) for c in pool["candidates"]}
    added = 0
    for brand, equip in seeds:
        found = mine(brand, equip)
        kept = 0
        for t in found:
            s = sig(t)
            if len(s) < 2:
                continue
            if any(s <= es for es in have):   # already covered
                continue
            if any(s <= q or q <= s for q in seen):  # already queued
                continue
            seen.add(s); pool["candidates"].append(t); kept += 1; added += 1
        print(f"  {brand:28} {equip:22} -> {len(found):3} found, {kept:3} new")
    POOL.write_text(json.dumps(pool, indent=2))
    print(f"\n[+] Pool now holds {len(pool['candidates'])} real-code candidates (+{added} this run).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
