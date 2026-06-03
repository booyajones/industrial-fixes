#!/usr/bin/env python3
"""
Model-specific page generator — the long-tail volume play.

"Samsung WF45T6000AW washer problems & error codes". Model numbers are the long
tail competitors win. Each page: a grounded overview of that model's common
problems, the error codes it throws (linked to our code articles), the parts that
commonly fail on it (affiliate), and cross-links. Funnels model-searchers into the
money pages.

Reuses the engine (generate-articles.py). Thread-pooled, quote-escaped,
lock-snapshot, gas-safe. Reads models from scripts/.content-universe.json (the
demand-research swarm output) or a built-in seed.

USAGE:
    python scripts/generate-models.py --topics-file scripts/.content-universe.json --count 125 --jobs 3
    python scripts/generate-models.py --dry
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts" / "generate-articles.py"
_spec = importlib.util.spec_from_file_location("genmod", GEN)
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)

_lock = threading.Lock()
_FIX = {"ensure": "make sure", "crucial": "important", "vital": "important",
        "leverage": "use", "robust": "reliable", "seamless": "smooth"}
EQUIP_CAT = {"furnace": "hvac", "mini split": "hvac", "water heater": "water-heater"}
EQUIP_TAG = {"oven": "oven", "mini split": "mini-split", "water heater": "water-heater"}
GAS_APPLIANCES = {"furnace", "oven", "water heater"}


def topics_from_universe(p: Path) -> list[dict]:
    data = json.loads(p.read_text(encoding="utf-8"))
    out = []
    for a in data.get("appliances", []):
        appliance = (a.get("appliance") or "").lower().split(" /")[0].strip()
        if not appliance:
            continue
        for m in a.get("models", []):
            brand, model = (m.get("brand") or "").strip(), (m.get("model") or "").strip()
            if brand and model:
                out.append({"brand": brand, "model": model, "appliance": appliance})
    return out


def related_links(brand_slug: str, equip_tag: str, have: set[str]) -> str:
    pat = re.compile(rf"^{re.escape(brand_slug)}-{re.escape(equip_tag)}-.+-error-code$")
    codes = sorted(s for s in have if pat.match(s))[:12]
    if not codes:
        return ""
    links = "\n".join(
        f"- [{s.replace('-', ' ').replace(' error code','').title()} error code](/posts/{s}/)" for s in codes)
    return f"\n## {equip_tag.title()} Error Codes for This Model\n\nThese codes apply to this model line:\n\n{links}\n"


def claude_write_model(topic: str, research: str) -> dict | None:
    schema = (
        '{"title": "<Brand Model Problems & Error Codes, <=70 chars>",'
        ' "description": "<answer-first TL;DR 120-155 chars: the most common problem on this model + fix>",'
        ' "equipment_category": "<hvac|appliance|water-heater>", "brand_slug": "<lowercase-hyphen brand>",'
        ' "overview": "<1-2 plain paragraphs on this model and its common reliability issues>",'
        ' "problems": [{"lead": "<short bold problem>", "text": "<one sentence: cause + the part or fix>"}],'
        ' "parts": [{"name": "<part that commonly fails on this model>", "note": "<short note>"}],'
        ' "when_to_call_pro": "<1 paragraph>"}'
    )
    rules = (
        "STYLE (hard): no em dashes; no semicolons; do not use ensure/crucial/vital/leverage/robust/"
        "seamless. Write like a working appliance tech. 5-8 common problems for THIS model (most "
        "frequent first), each tied to the cause and the part or fix. 2-4 parts that commonly fail on "
        "this model. Only state specs/part numbers present in the research. If you are unsure this exact "
        "model exists, keep guidance to the model line/series. For gas appliances frame gas work as pro."
    )
    prompt = (
        f"Write a model overview repair guide for: \"{topic}\".\n\n"
        f"RESEARCH (ground every claim in this):\n{research or '(no external research; stay general, cover the series)'}\n\n"
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


def assemble_model(topic: str, c: dict, slug: str, equip_tag: str, brand_slug: str,
                   have: set[str], gas: bool, draft: bool) -> str:
    title = c["title"].replace("—", "-").replace('"', '\\"').strip()
    desc = c["description"].replace("—", "-").replace('"', '\\"').strip()
    author = G.AUTHORS[abs(hash(slug)) % len(G.AUTHORS)]
    cat = c.get("equipment_category", "appliance")
    tags = []
    for t in [cat if cat != "other" else None, equip_tag, brand_slug, "model", "gas" if gas else None]:
        if t and t not in tags:
            tags.append(t)
    pub = (datetime.now(timezone.utc) - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    problems = "\n".join(f"- **{x['lead']}** {x['text']}" for x in c.get("problems", []))

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

## {title.split(' — ')[0].split(' - ')[0]} — Overview

{c['overview']}

[Jump to Common Problems](#fix)

## Most Common Problems on This Model {{#fix}}

{problems}

## Parts That Commonly Fail

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
    topic = f"{t['brand']} {t['model']} {t['appliance']} problems and error codes"
    slug = G.slugify(f"{t['brand']} {t['model']} {t['appliance']} problems")
    with _lock:
        if slug in have:
            return (slug, "skip", "exists")
        have.add(slug)
    try:
        research = G.perplexity_research(topic)
        content = claude_write_model(topic, research)
        if not content:
            return (slug, "fail", "no content")
        content.setdefault("equipment_category", EQUIP_CAT.get(t["appliance"], "appliance"))
        content["brand_slug"] = brand_slug
        gas = t["appliance"] in GAS_APPLIANCES
        if gas:
            wp = (content.get("when_to_call_pro") or "").rstrip()
            content["when_to_call_pro"] = (wp + " " if wp else "") + "For gas line, burner, or igniter work, or if you ever smell gas, stop and call a licensed technician."
        verdict = G.claude_review(topic, content, research)
        publish = bool(verdict.get("publish")) and int(verdict.get("score", 0)) >= 7
        with _lock:
            have_snap = set(have)
        md = assemble_model(topic, content, slug, equip_tag, brand_slug, have_snap, gas, draft=not publish)
        if G.BANNED.search(md):
            md = G.BANNED.sub(lambda m: _FIX.get(m.group(0).lower(), m.group(0)), md)
        (G.BLOG_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
        return (slug, "publish" if publish else "draft", f"score={verdict.get('score')}")
    except Exception as e:
        return (slug, "fail", str(e)[:120])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=125)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--topics-file", default=str(ROOT / "scripts" / ".content-universe.json"))
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    if not args.dry and (not getattr(G, "ANTHROPIC_KEY", "") or not getattr(G, "PERPLEXITY_KEY", "")):
        print("[!] set ANTHROPIC_API_KEY + PERPLEXITY_API_KEY first.")
        return 1
    p = Path(args.topics_file)
    raw = topics_from_universe(p) if p.exists() else []
    have = G.existing_slugs()
    seen, topics = set(), []
    for t in raw:
        slug = G.slugify(f"{t['brand']} {t['model']} {t['appliance']} problems")
        if slug in seen or slug in have:
            continue
        seen.add(slug)
        topics.append(t)
    topics = topics[: args.count]
    print(f"[i] {len(topics)} model topics to generate (jobs={args.jobs})")
    if args.dry:
        for t in topics[:30]:
            print("   ", t["brand"], t["model"], t["appliance"])
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
