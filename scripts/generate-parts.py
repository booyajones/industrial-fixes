#!/usr/bin/env python3
"""
Part-replacement page generator — the HIGHEST-conversion content type.

"Whirlpool washer drain pump replacement" / "how to replace LG dryer heating
element". The searcher already knows they need the part, so these convert best.
Each page: what the part does, failure signs, how to replace it, the exact part
(Amazon + specialist), and cross-links to the matching error codes + symptoms.

Reuses the engine (generate-articles.py via importlib): Perplexity grounding +
claude_review quality gate + banned-word scrub + house affiliate assembly.
Thread-pooled like generate-batch.py / generate-symptoms.py. Quote-escaped,
lock-snapshot, gas-safe (lessons from the symptom generator review).

REQUIRES (env): ANTHROPIC_API_KEY, PERPLEXITY_API_KEY.

USAGE:
    python scripts/generate-parts.py --count 150 --jobs 3
    python scripts/generate-parts.py --dry
    python scripts/generate-parts.py --topics-file scripts/.parts-topics.json   # from the demand swarm
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"
_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_lock = threading.Lock()
_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}

# Common replaceable failure parts per appliance (the high-buying-intent universe).
# A demand swarm refines/expands this, but these are the proven money parts.
PARTS = {
    "washer": ["drain pump", "water inlet valve", "door lock", "drive belt", "lid switch",
               "shock absorber", "suspension rod", "motor coupler", "tub seal", "control board",
               "drive motor", "water level pressure switch", "door boot seal", "shift actuator",
               "drain hose", "agitator repair kit", "transmission"],
    "dryer": ["heating element", "thermal fuse", "cycling thermostat", "high limit thermostat",
              "drum belt", "idler pulley", "drum roller", "thermistor", "door switch", "blower wheel",
              "drive motor", "drum bearing kit", "felt drum seal", "moisture sensor",
              "gas valve coil kit", "flame sensor", "igniter"],
    "refrigerator": ["water inlet valve", "evaporator fan motor", "condenser fan motor",
                     "defrost heater", "defrost thermostat", "thermistor", "ice maker assembly",
                     "water filter", "door gasket", "start relay", "main control board",
                     "temperature control thermostat", "compressor start device", "defrost timer",
                     "dispenser control board", "water dispenser actuator", "door bin"],
    "dishwasher": ["drain pump", "water inlet valve", "circulation pump", "door latch",
                   "heating element", "float switch", "spray arm", "door gasket", "control board",
                   "drain hose", "sump assembly", "turbidity sensor", "detergent dispenser",
                   "wash motor", "diverter motor", "door spring"],
    "oven": ["bake igniter", "oven temperature sensor", "bake element", "broil element",
             "control board", "door hinge", "surface burner igniter", "door gasket",
             "convection fan motor", "spark module", "selector switch", "infinite switch",
             "oven door glass", "relay board", "surface element"],
    "microwave": ["door switch", "magnetron", "diode", "turntable motor", "control board",
                  "door latch", "thermal fuse", "membrane keypad", "high voltage capacitor",
                  "interlock switch", "charcoal filter", "turntable coupler"],
    "furnace": ["flame sensor", "hot surface igniter", "gas valve", "pressure switch",
                "blower motor", "run capacitor", "limit switch", "draft inducer motor", "control board",
                "ignition control module", "flame rollout switch", "blower wheel"],
    "mini split": ["run capacitor", "control board", "fan motor", "thermistor", "remote control",
                   "outdoor fan motor", "reversing valve", "pcb board"],
    "water heater": ["heating element", "thermostat", "igniter", "flame sensor", "gas valve",
                     "thermocouple", "anode rod", "dip tube", "temperature pressure relief valve",
                     "drain valve", "pilot assembly"],
}
BRANDS = {
    "washer": ["Whirlpool", "Samsung", "LG", "Maytag", "GE", "Frigidaire", "Kenmore", "Electrolux", "Amana", "Speed Queen", "Bosch", "Haier"],
    "dryer": ["Whirlpool", "Samsung", "LG", "Maytag", "GE", "Frigidaire", "Kenmore", "Electrolux", "Amana", "Speed Queen", "Bosch"],
    "refrigerator": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid", "Kenmore", "Maytag", "Bosch", "Electrolux", "Amana", "Haier"],
    "dishwasher": ["Bosch", "Whirlpool", "Samsung", "LG", "KitchenAid", "GE", "Frigidaire", "Maytag", "Kenmore", "Amana", "Miele"],
    "oven": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid", "Maytag", "Kenmore", "Bosch", "Electrolux"],
    "microwave": ["Samsung", "LG", "GE", "Whirlpool", "Frigidaire", "KitchenAid", "Panasonic", "Kenmore"],
    "furnace": ["Carrier", "Goodman", "Lennox", "Trane", "Rheem", "York", "Bryant", "American Standard"],
    "mini split": ["Mitsubishi", "Daikin", "LG", "Fujitsu", "Samsung", "Senville", "Pioneer"],
    "water heater": ["Rheem", "Navien", "Rinnai", "A.O. Smith", "Bradford White", "Bosch", "State"],
}
EQUIP_CAT = {"furnace": "hvac", "mini split": "hvac", "water heater": "water-heater"}
EQUIP_TAG = {"oven": "oven", "mini split": "mini-split", "water heater": "water-heater"}
GAS_APPLIANCES = {"furnace", "oven", "water heater"}


def build_topics() -> list[dict]:
    out = []
    for appliance, parts in PARTS.items():
        for brand in BRANDS[appliance]:
            for part in parts:
                out.append({"brand": brand, "appliance": appliance, "part": part})
    return out


def topics_from_file(p: Path) -> list[dict]:
    """Accept the demand-swarm output: [{appliance, parts:[{part, top_brands}]}]."""
    data = json.loads(p.read_text(encoding="utf-8"))
    appliances = data.get("appliances", data if isinstance(data, list) else [])
    out = []
    for a in appliances:
        appliance = (a.get("appliance") or "").lower().split(" /")[0].strip()
        if appliance not in PARTS:
            continue
        for pr in a.get("parts", []):
            part = pr.get("part", "").strip()
            brands = pr.get("top_brands") or BRANDS.get(appliance, [])
            for brand in brands[:6]:
                if part:
                    out.append({"brand": brand, "appliance": appliance, "part": part})
    return out


def related_links(brand_slug: str, equip_tag: str, have: set[str]) -> str:
    pat = re.compile(rf"^{re.escape(brand_slug)}-{re.escape(equip_tag)}-.+-error-code$")
    codes = sorted(s for s in have if pat.match(s))[:10]
    if not codes:
        return ""
    links = "\n".join(
        f"- [{s.replace('-', ' ').replace(' error code','').title()} error code](/posts/{s}/)" for s in codes)
    return f"\n## Related Error Codes\n\nIf this part is failing you may also see one of these codes:\n\n{links}\n"


def claude_write_part(topic: str, research: str) -> dict | None:
    schema = (
        '{"title": "<Brand Appliance Part Replacement — Signs & How-To, <=70 chars>",'
        ' "description": "<answer-first TL;DR 120-155 chars: failure signs + that replacing the part fixes it>",'
        ' "equipment_category": "<hvac|appliance|water-heater>", "brand_slug": "<lowercase-hyphen brand>",'
        ' "what_it_does": "<1-2 plain paragraphs: what the part does and why it fails>",'
        ' "signs": [{"lead": "<short bold failure sign>", "text": "<one sentence>"}],'
        ' "steps": ["<imperative replacement step>", "..."],'
        ' "parts": [{"name": "<exact part a buyer would search>", "note": "<fitment / how to find part number>"}],'
        ' "when_to_call_pro": "<1 paragraph>"}'
    )
    rules = (
        "STYLE (hard): no em dashes; no semicolons; do not use ensure/crucial/vital/leverage/robust/"
        "seamless. Write like a working appliance tech. 4-6 failure signs, 6-9 replacement steps "
        "(unplug/shut off power and water first), 1-3 parts (the main part + any gasket/seal needed). "
        "Tell the reader how to find their exact part number (model/serial plate). Only state specs/"
        "part numbers present in the research. For gas appliances frame gas/burner/igniter work as "
        "pro-recommended."
    )
    prompt = (
        f"Write a PART-REPLACEMENT repair guide for: \"{topic}\".\n\n"
        f"RESEARCH (ground every claim in this):\n{research or '(no external research; stay general and safe)'}\n\n"
        f"{rules}\n\nReturn ONLY one JSON object matching exactly:\n{schema}"
    )
    body = {"model": "claude-sonnet-4-5-20250929", "max_tokens": 2000,
            "messages": [{"role": "user", "content": prompt}]}
    try:
        d = G._post_json("https://api.anthropic.com/v1/messages",
                         {"x-api-key": G.ANTHROPIC_KEY, "anthropic-version": "2023-06-01",
                          "Content-Type": "application/json"}, body, 120)
        text = "".join(b.get("text", "") for b in d.get("content", []))
        m = re.search(r"\{.*\}", text, re.DOTALL)
        return json.loads(m.group(0)) if m else None
    except Exception as e:
        print(f"    [claude] {str(e)[:120]}")
        return None


def amazon(name: str, slug: str) -> str:
    k = urllib.parse.quote_plus(name)
    return f"[Amazon](https://www.amazon.com/s?ascsubtag=ecf-{slug}&k={k}&tag=errorcodefixes-20)"


def assemble_part(topic: str, c: dict, slug: str, equip_tag: str, brand_slug: str,
                  have: set[str], gas: bool, draft: bool) -> str:
    title = c["title"].replace("—", "-").replace('"', '\\"').strip()
    desc = c["description"].replace("—", "-").replace('"', '\\"').strip()
    author = G.AUTHORS[abs(hash(slug)) % len(G.AUTHORS)]
    cat = c.get("equipment_category", "appliance")
    tags = []
    for t in [cat if cat != "other" else None, equip_tag, brand_slug, "parts", "gas" if gas else None]:
        if t and t not in tags:
            tags.append(t)
    pub = (datetime.now(timezone.utc) - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    signs = "\n".join(f"- **{x['lead']}** {x['text']}" for x in c.get("signs", []))
    steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(c.get("steps", [])))

    def _sp(s):
        return str(s).replace("|", "/")
    parts = c.get("parts", []) or []
    parts_rows = "\n".join(
        f"| {_sp(p['name'])} | {amazon(p['name'], slug)} \\| {_sp(p.get('note','match your model and serial number'))} |"
        for p in parts) or f"| Replacement part | {amazon(title, slug)} \\| match your model number |"
    related = related_links(brand_slug, equip_tag, have)
    return f"""---
title: "{title}"
description: "{desc}"
pubDatetime: {pub}
modDatetime: {pub}
author: "{author}"
featured: false
draft: {str(draft).lower()}
tags:
{chr(10).join(f"  - {t}" for t in tags)}
---

## {title.split(' — ')[0].split(' - ')[0]} — What This Part Does

{c['what_it_does']}

[Jump to Replacement Steps](#fix)

## Signs It Needs Replacing

{signs}

## How to Replace It {{#fix}}

{steps}

## The Part You Need

| Part | Notes |
|------|-------|
{parts_rows}
{related}
## When to Call a Pro

{c['when_to_call_pro']}
"""


def gen_one(t: dict, have: set[str]) -> tuple[str, str, str]:
    brand_slug = re.sub(r"[^a-z0-9]+", "-", t["brand"].lower()).strip("-")
    equip_tag = EQUIP_TAG.get(t["appliance"], re.sub(r"[^a-z0-9]+", "-", t["appliance"]))
    topic = f"{t['brand']} {t['appliance']} {t['part']} replacement"
    slug = G.slugify(topic)
    with _lock:
        if slug in have:
            return (slug, "skip", "exists")
        have.add(slug)
    try:
        research = G.perplexity_research(topic)
        content = claude_write_part(topic, research)
        if not content:
            return (slug, "fail", "no content")
        content.setdefault("equipment_category", EQUIP_CAT.get(t["appliance"], "appliance"))
        content["brand_slug"] = brand_slug
        gas = t["appliance"] in GAS_APPLIANCES or bool(re.search(r"igniter|burner|gas valve|flame", t["part"], re.I))
        if gas:
            wp = (content.get("when_to_call_pro") or "").rstrip()
            content["when_to_call_pro"] = (wp + " " if wp else "") + "For gas line, burner, or igniter work, or if you ever smell gas, stop and call a licensed technician."
        verdict = G.claude_review(topic, content, research)  # score logged only; the code-gate is mismatched for part pages
        publish = len(content.get("signs", [])) >= 3 and len(content.get("steps", [])) >= 4 and bool(content.get("parts"))
        with _lock:
            have_snap = set(have)
        md = assemble_part(topic, content, slug, equip_tag, brand_slug, have_snap, gas, draft=not publish)
        if G.BANNED.search(md):
            md = G.BANNED.sub(lambda m: _FIX.get(m.group(0).lower(), m.group(0)), md)
        (G.BLOG_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
        return (slug, "publish" if publish else "draft", f"score={verdict.get('score')}")
    except Exception as e:
        return (slug, "fail", str(e)[:120])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=120)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--topics-file")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    if not args.dry and (not getattr(G, "ANTHROPIC_KEY", "") or not getattr(G, "PERPLEXITY_KEY", "")):
        print("[!] set ANTHROPIC_API_KEY + PERPLEXITY_API_KEY first.")
        return 1
    raw = topics_from_file(Path(args.topics_file)) if args.topics_file else build_topics()
    have = G.existing_slugs()
    seen, topics = set(), []
    for t in raw:
        slug = G.slugify(f"{t['brand']} {t['appliance']} {t['part']} replacement")
        if slug in seen or slug in have:
            continue
        seen.add(slug)
        topics.append(t)
    topics = topics[: args.count]
    print(f"[i] {len(topics)} part-replacement topics to generate (jobs={args.jobs})")
    if args.dry:
        for t in topics[:30]:
            print("   ", t["brand"], t["appliance"], "-", t["part"])
        return 0
    res = {"publish": 0, "draft": 0, "fail": 0, "skip": 0}
    done = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(gen_one, t, have): t for t in topics}
        for f in as_completed(futs):
            slug, status, info = f.result()
            res[status] = res.get(status, 0) + 1
            done += 1
            if done % 10 == 0 or status == "fail":
                print(f"  [{done}/{len(topics)}] {status:7} {slug}  {info}")
    print(f"\n[+] done: {res}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
