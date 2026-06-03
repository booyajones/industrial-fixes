#!/usr/bin/env python3
"""
Symptom-page generator — the high-volume consumer content surface.

"Samsung washer won't drain", "LG refrigerator not cooling" get 5-10x the search
volume of code queries, are a DIFFERENT template (so the corpus growth looks
natural, not mass-produced), and FUNNEL the searcher into our error-code articles
+ the OEM part. Each page cross-links to the matching {brand}-{appliance}-*-error-code
articles already on the site (internal linking + topical authority).

Reuses the engine: Perplexity grounding + claude_review quality gate + banned-word
scrub + the house affiliate-link assembly. Thread-pooled like generate-batch.py.

REQUIRES (env): ANTHROPIC_API_KEY, PERPLEXITY_API_KEY (set before running).

USAGE:
    python scripts/generate-symptoms.py --count 150 --jobs 3
    python scripts/generate-symptoms.py --dry            # list topics only
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"
_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_lock = threading.Lock()
_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}

# High-volume symptoms per appliance (how homeowners actually search).
SYMPTOMS = {
    "washer": ["wont drain", "wont spin", "wont start", "leaking water", "wont fill with water",
               "stops mid cycle", "door wont unlock", "shaking and loud", "wont turn on"],
    "dryer": ["not heating", "wont start", "takes too long to dry", "wont tumble",
              "stops mid cycle", "no power", "squeaking", "shuts off early"],
    "refrigerator": ["not cooling", "freezer not freezing", "too warm", "ice maker not working",
                     "water dispenser not working", "leaking water", "freezing food",
                     "running constantly", "not making ice"],
    "dishwasher": ["not draining", "not cleaning dishes", "not drying", "leaking",
                   "wont start", "wont fill with water", "stuck mid cycle", "smells bad"],
    "oven": ["not heating", "wont turn on", "temperature not accurate", "broiler not working",
             "igniter not working", "burner wont light", "door wont lock", "self clean not working"],
    "microwave": ["not heating", "turntable not turning", "wont start", "sparking",
                  "buttons not working", "runs but no heat"],
    "furnace": ["not heating", "wont turn on", "blowing cold air", "short cycling",
                "blower wont shut off", "igniter not working"],
    "mini split": ["not cooling", "not heating", "leaking water", "wont turn on",
                   "blowing warm air", "ice on coils"],
    "water heater": ["no hot water", "not enough hot water", "water too hot", "leaking", "no ignition"],
}
# Brands per appliance (US consumer demand).
BRANDS = {
    "washer": ["Samsung", "LG", "Whirlpool", "Maytag", "GE", "Frigidaire", "Kenmore"],
    "dryer": ["Samsung", "LG", "Whirlpool", "Maytag", "GE", "Kenmore"],
    "refrigerator": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid", "Kenmore"],
    "dishwasher": ["Bosch", "Samsung", "LG", "Whirlpool", "KitchenAid", "GE", "Frigidaire"],
    "oven": ["Samsung", "LG", "Whirlpool", "GE", "Frigidaire", "KitchenAid"],
    "microwave": ["Samsung", "LG", "GE", "Whirlpool"],
    "furnace": ["Carrier", "Goodman", "Lennox", "Trane", "Rheem"],
    "mini split": ["Mitsubishi", "Daikin", "LG", "Fujitsu"],
    "water heater": ["Rheem", "Navien", "Rinnai", "A.O. Smith"],
}
EQUIP_CAT = {"furnace": "hvac", "mini split": "hvac", "water heater": "water-heater"}
EQUIP_TAG = {"oven": "oven", "mini split": "mini-split", "water heater": "water-heater"}


def build_topics() -> list[dict]:
    out = []
    for appliance, symptoms in SYMPTOMS.items():
        for brand in BRANDS[appliance]:
            for sym in symptoms:
                out.append({"brand": brand, "appliance": appliance, "symptom": sym})
    return out


def related_codes(brand_slug: str, equip_tag: str, have: set[str]) -> list[str]:
    """Existing {brand}-{equip}-*-error-code slugs to cross-link to."""
    pat = re.compile(rf"^{re.escape(brand_slug)}-{re.escape(equip_tag)}-.+-error-code$")
    return sorted(s for s in have if pat.match(s))[:12]


def claude_write_symptom(topic: str, research: str) -> dict | None:
    schema = (
        '{"title": "<Brand Appliance Symptom — Causes & Fix, <=70 chars>",'
        ' "description": "<answer-first TL;DR 120-155 chars: the single most likely cause + fix>",'
        ' "equipment_category": "<hvac|appliance|water-heater>", "brand_slug": "<lowercase-hyphen brand>",'
        ' "whats_happening": "<1-2 plain paragraphs on what the symptom means>",'
        ' "causes": [{"lead": "<short bold cause>", "text": "<one sentence, most likely first>"}],'
        ' "steps": ["<imperative diagnostic step>", "..."],'
        ' "parts": [{"name": "<part a buyer would search>", "note": "<short note>"}],'
        ' "when_to_call_pro": "<1 paragraph>"}'
    )
    rules = (
        "STYLE (hard): no em dashes; no semicolons; do not use ensure/crucial/vital/leverage/robust/"
        "seamless. Write like a working appliance tech, concrete and calm. Order causes MOST LIKELY "
        "first. Only state specific part numbers/specs present in the research; otherwise stay general. "
        "5-7 causes, 5-8 diagnostic steps, 2-4 parts. For gas appliances frame gas/burner/igniter work "
        "as pro-recommended."
    )
    prompt = (
        f"Write a repair guide for this SYMPTOM (not an error code): \"{topic}\".\n\n"
        f"RESEARCH (ground every claim in this; do not contradict it):\n{research or '(no external research; stay general and safe)'}\n\n"
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


def assemble_symptom(topic: str, c: dict, slug: str, equip_tag: str, brand_slug: str,
                     have: set[str], draft: bool) -> str:
    title = c["title"].replace("—", "-").replace('"', '\\"').strip()
    desc = c["description"].replace("—", "-").replace('"', '\\"').strip()
    author = G.AUTHORS[abs(hash(slug)) % len(G.AUTHORS)]
    cat = c.get("equipment_category", "appliance")
    tags = []
    for t in [cat if cat != "other" else None, equip_tag, brand_slug, "symptom",
              "gas" if c.get("_gas") else None]:
        if t and t not in tags:
            tags.append(t)
    pub = (datetime.now(timezone.utc) - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    causes = "\n".join(f"- **{x['lead']}** {x['text']}" for x in c.get("causes", []))
    steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(c.get("steps", [])))
    parts = c.get("parts", []) or []

    def _sp(s):
        return str(s).replace("|", "/")
    parts_rows = "\n".join(
        f"| {_sp(p['name'])} | {amazon(p['name'], slug)} \\| {_sp(p.get('note','verify fitment for your model'))} |"
        for p in parts) or f"| Replacement part | {amazon(title, slug)} \\| verify fitment |"
    # cross-link to existing error-code articles for this brand+appliance
    codes = related_codes(brand_slug, equip_tag, have)
    related = ""
    if codes:
        links = "\n".join(
            f"- [{s.replace('-', ' ').replace(' error code','').title()} error code](/posts/{s}/)"
            for s in codes)
        related = f"\n## Related Error Codes\n\nIf your appliance also shows a code on the display, these match this problem:\n\n{links}\n"
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

## {title.split(' — ')[0].split(' - ')[0]} — What's Happening

{c['whats_happening']}

[Jump to Fix](#fix)

## Most Likely Causes

{causes}

## How to Diagnose and Fix {{#fix}}

{steps}

## Parts You Might Need

| Part | Notes |
|------|-------|
{parts_rows}
{related}
## When to Call a Pro

{c['when_to_call_pro']}
"""


def gen_one(t: dict, have: set[str]) -> tuple[str, str, str]:
    brand_slug = re.sub(r"[^a-z0-9]+", "-", t["brand"].lower()).strip("-")
    equip_tag = EQUIP_TAG.get(t["appliance"], t["appliance"])
    topic = f"{t['brand']} {t['appliance']} {t['symptom']}"
    slug = G.slugify(topic)
    with _lock:
        if slug in have:
            return (slug, "skip", "exists")
        have.add(slug)
    try:
        research = G.perplexity_research(topic)
        content = claude_write_symptom(topic, research)
        if not content:
            return (slug, "fail", "no content")
        content.setdefault("equipment_category", EQUIP_CAT.get(t["appliance"], "appliance"))
        content["brand_slug"] = brand_slug
        # Gas safety: structural pro-referral + "gas" tag (-> triage "Pro recommended").
        if t["appliance"] in ("furnace", "oven", "water heater") or re.search(r"igniter|burner|gas", t["symptom"], re.I):
            content["_gas"] = True
            wp = (content.get("when_to_call_pro") or "").rstrip()
            content["when_to_call_pro"] = (wp + " " if wp else "") + "For gas line, burner, or igniter work, or if you ever smell gas, stop and call a licensed technician."
        verdict = G.claude_review(topic, content, research)
        publish = bool(verdict.get("publish")) and int(verdict.get("score", 0)) >= 7
        with _lock:
            have_snap = set(have)
        md = assemble_symptom(topic, content, slug, equip_tag, brand_slug, have_snap, draft=not publish)
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
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    if not args.dry and (not getattr(G, "ANTHROPIC_KEY", "") or not getattr(G, "PERPLEXITY_KEY", "")):
        print("[!] set ANTHROPIC_API_KEY + PERPLEXITY_API_KEY first.")
        return 1
    have = G.existing_slugs()
    topics = [t for t in build_topics() if G.slugify(f"{t['brand']} {t['appliance']} {t['symptom']}") not in have]
    topics = topics[: args.count]
    print(f"[i] {len(topics)} symptom topics to generate (jobs={args.jobs})")
    if args.dry:
        for t in topics[:30]:
            print("   ", t["brand"], t["appliance"], "-", t["symptom"])
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
