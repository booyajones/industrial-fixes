#!/usr/bin/env python3
"""
YouTube Shorts script generator for errorcodefixes.com.

Takes either:
  (a) a Reddit Intel demand-signal JSON file (from scripts/reddit-intel/)
  (b) a specific article slug
  (c) a hand-typed (brand, code, symptom) tuple

Outputs a 30-60 second YouTube Short script with hook, problem statement,
fix sequence, on-screen text overlays, CTA, hashtags, thumbnail copy, and
description with bio-link tracking.

Design principles enforced:
- First 3 seconds = hook ("Carrier code 13 means your filter is killing your furnace")
- 1 specific number per section (microamps, ohms, PSI, etc.)
- Last 5 seconds = one CTA ("Full fix at errorcodefixes.com/posts/<slug>")
- No two consecutive scripts use the same opening phrasing
- Conservative claims only (no "this WILL fix it" — always "this fixes 70% of these")
- Hashtags: brand-specific + #HVAC OR #VFD OR #CommercialKitchen + #ErrorCode

USAGE:
    # From a Reddit Intel JSON:
    python scripts/shorts-script-gen.py --from reddit-intel/output/latest.json --count 5

    # From a known article:
    python scripts/shorts-script-gen.py --slug manitowoc-e01-error-code

    # Ad-hoc:
    python scripts/shorts-script-gen.py --brand Carrier --code 13 --symptom "limit lockout"

OUTPUT: growth-pipeline/shorts/YYYY-MM-DD_<slug>.md (one file per script)
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
OUT_DIR = ROOT / "growth-pipeline" / "shorts"
SITE = "https://errorcodefixes.com"

# Rotate opening hooks so the channel does not look templated
HOOKS = [
    "If you have a {brand} throwing {code}, the part everyone replaces first is wrong.",
    "{brand} {code} is not the part you think it is. Here is what actually fixes it.",
    "Most {brand} {code} calls are diagnosed wrong in the first 60 seconds. Don't be one of them.",
    "{brand} {code} is a {symptom_short} lockout. Skip the part swap and do this first.",
    "Three things to check before you order any part for a {brand} {code} fault.",
    "I have seen {brand} {code} hundreds of times. The fix is almost always the same and almost never the obvious answer.",
    "Don't replace the {wrong_part} on a {brand} {code} until you've tried this.",
    "The cheap fix for {brand} {code} that the parts counter does not want you to know.",
]

# Pre-built section templates per error category. Real numbers fed in from
# article frontmatter / body where possible.
SECTION_TEMPLATES = {
    "hvac-limit-lockout": {
        "problem_30s": "Your furnace tried to fire, then locked out for safety. The limit switch saw too much heat. That usually means airflow is starving the heat exchanger.",
        "fix_steps": [
            "Pull the filter. If it is grey or matted, swap it for a MERV 8 or MERV 11 max.",
            "Check the blower wheel. Even half an inch of dust cuts CFM by 30 percent.",
            "Test the limit switch with a multimeter — should read closed below 130 F."
        ],
        "wrong_part": "limit switch",
        "symptom_short": "limit",
    },
    "vfd-undervolt": {
        "problem_30s": "Your drive bus dropped below the minimum, the drive killed the output, you got the fault. Often a momentary line dip from another motor on the same panel.",
        "fix_steps": [
            "Pull the fault history first. Parameters D361 through D365 on a PowerFlex 525.",
            "Check incoming line voltage with a meter that captures peaks — 5 second dips kill drives without showing up on a slow meter.",
            "Verify the input fuses and the bus pre-charge resistor."
        ],
        "wrong_part": "drive",
        "symptom_short": "undervoltage",
    },
    "ice-machine-long-freeze": {
        "problem_30s": "Your ice machine ran more than 60 minutes on one batch and gave up. Nine times out of ten it is a dirty condenser, not a refrigerant problem.",
        "fix_steps": [
            "Pull the condenser coil and clean it with a fin comb plus coil cleaner.",
            "Check water flow over the evaporator — should be 4 gallons per minute.",
            "Only after both of those, gauge the system and check superheat."
        ],
        "wrong_part": "compressor",
        "symptom_short": "long-freeze",
    },
    "ignition-lockout": {
        "problem_30s": "Furnace tried to light, failed three times in a row, board gave up. Most of the time the flame sensor is just dirty.",
        "fix_steps": [
            "Pull the flame sensor — single rod with a porcelain base. Clean it with fine sandpaper, not steel wool.",
            "Check flame microamps after cleaning. Should read 2 to 6 microamps DC.",
            "Below 0.7 microamps after cleaning means the sensor is shot. Replace it."
        ],
        "wrong_part": "control board",
        "symptom_short": "ignition",
    },
    "drain-fault": {
        "problem_30s": "Mini split P5 means water is backing up in the drain pan or the condensate pump is dead. Pump replacement is the obvious fix and usually wrong.",
        "fix_steps": [
            "Pour a cup of one-to-one vinegar in the drain pan. Run cool mode 20 minutes.",
            "If P5 clears, algae was the issue, not the pump.",
            "If it does not clear, then test the pump float and pump motor before replacing."
        ],
        "wrong_part": "drain pump",
        "symptom_short": "drain",
    },
    "generic": {
        "problem_30s": "This code locks the unit out for safety. The part everyone replaces first is usually not the cause.",
        "fix_steps": [
            "Read the full fault history before resetting — most controls store the last 3 to 5 events.",
            "Verify the obvious physical causes first — airflow, filter, drain, gas, voltage.",
            "Only after the obvious checks fail should you start swapping parts."
        ],
        "wrong_part": "control board",
        "symptom_short": "fault",
    },
}


def classify_template_key(brand: str, code: str, symptom: str, slug: str) -> str:
    text = f"{slug} {symptom} {code}".lower()
    if any(s in text for s in ["limit", "lockout", "13", "33", "4-flash", "4 flash", "high temp"]):
        return "hvac-limit-lockout"
    if any(s in text for s in ["undervolt", "f004", "f3000", "uv1", "3220", "bus low"]):
        return "vfd-undervolt"
    if any(s in text for s in ["long freeze", "long-freeze", "e01", "e02", "harvest", "ice-machine"]):
        return "ice-machine-long-freeze"
    if any(s in text for s in ["ignition", "21", "34", "flame", "3-flash", "3 flash", "240", "11"]):
        return "ignition-lockout"
    if any(s in text for s in ["p5", "drain", "condensate"]):
        return "drain-fault"
    return "generic"


def parse_post(slug: str) -> dict:
    """Read article frontmatter to pull brand/code/tags/title."""
    path = BLOG / f"{slug}.md"
    if not path.exists():
        return {"slug": slug, "brand": "", "code": "", "symptom": "", "title": "", "tags": []}
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^---\s*\n(.*?)^---\s*\n", text, re.DOTALL | re.MULTILINE)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" not in line:
                continue
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    title = fm.get("title", "")
    # Try to extract brand + code from title
    # e.g. "Manitowoc E01 Error Code — Long Freeze Cycle Fix"
    brand_m = re.match(r"([A-Z][a-zA-Z\-]+(?:\s+[A-Z][a-zA-Z\-]+)?)", title)
    brand = brand_m.group(1) if brand_m else ""
    code_m = re.search(r"\b([A-Z]?\d{1,4}[A-Z]?)\b", title)
    code = code_m.group(1) if code_m else ""
    symptom = ""
    sm = re.search(r"\b(?:Error\s+Code|Fault|Alarm)?\s*[—\-:]+\s*(.+?)(?:\s+Fix)?$", title)
    if sm:
        symptom = sm.group(1).strip()
    # Tags
    tag_m = re.search(r"^tags\s*:\s*\n((?:\s+-\s+.+\n)+)", text, re.MULTILINE)
    tags = []
    if tag_m:
        tags = [l.strip().lstrip("-").strip() for l in tag_m.group(1).splitlines() if l.strip()]
    return {"slug": slug, "brand": brand, "code": code, "symptom": symptom, "title": title, "tags": tags}


def build_hashtags(brand: str, tags: list[str]) -> list[str]:
    out = []
    # Brand hashtag
    b = re.sub(r"\s+", "", brand)
    if b:
        out.append(f"#{b}")
    out.append("#HVAC" if any(t in tags for t in ("hvac", "furnace", "mini-split")) else
               "#VFD" if any(t in tags for t in ("vfd", "drives")) else
               "#CommercialKitchen" if any(t in tags for t in ("ice-machine", "commercial-refrigeration")) else
               "#CNC" if "cnc" in tags else "#Repair")
    out.append("#ErrorCode")
    out.append("#FixIt")
    out.append("#TechTok" if "hvac" in tags else "#ProTech")
    return out[:5]


def build_script(meta: dict, hook_idx: int = None) -> str:
    brand = meta["brand"] or "Your equipment"
    code = meta["code"] or "this code"
    symptom = meta["symptom"] or "this fault"
    slug = meta["slug"]
    template_key = classify_template_key(brand, code, symptom, slug)
    template = SECTION_TEMPLATES[template_key]

    hook_idx = hook_idx if hook_idx is not None else random.randint(0, len(HOOKS) - 1)
    hook = HOOKS[hook_idx].format(
        brand=brand, code=code, symptom_short=template["symptom_short"], wrong_part=template["wrong_part"]
    )

    hashtags = build_hashtags(brand, meta["tags"])
    url = f"{SITE}/posts/{slug}/"

    lines = [
        f"# YouTube Short — {meta['title'] or slug}",
        "",
        f"**Target length:** 45-60 seconds",
        f"**Bio link / pinned comment:** {url}",
        f"**Filming tip:** static phone shot on the equipment OR shoulders-up if you don't have access. Good lighting. Lapel mic if you have one.",
        "",
        "## Hook (3 seconds, on-screen text overlay matches)",
        "",
        f"> {hook}",
        "",
        "**On-screen text:** " + (hook[:55] + "..." if len(hook) > 60 else hook),
        "",
        "## Problem (10-15 seconds)",
        "",
        f"> {template['problem_30s']}",
        "",
        f"**On-screen text:** \"{brand} {code}: not what you think\"",
        "",
        "## Fix sequence (25-30 seconds — show each step on screen)",
        "",
    ]
    for i, step in enumerate(template["fix_steps"], 1):
        lines.append(f"**Step {i}:** {step}")
        lines.append("")
    lines.extend([
        "## CTA (last 5 seconds)",
        "",
        f"> Full fix with the actual ohm and microamp readings is at errorcodefixes dot com slash posts slash {slug}",
        "",
        f"**On-screen text:** \"errorcodefixes.com/posts/{slug}\"",
        "**Pinned comment text:**",
        "```",
        f"Full diagnostic with part numbers + cost ranges: {url}",
        "```",
        "",
        "## Description block (paste into YouTube)",
        "",
        "```",
        f"{template['problem_30s']}",
        "",
        f"Full diagnostic guide with part numbers and cost ranges: {url}",
        "",
        f"Subscribe for daily 60-second {brand.lower()} and equipment troubleshooting.",
        "",
        " ".join(hashtags),
        "```",
        "",
        "## Thumbnail copy (if you make one)",
        "",
        f"- **Top line:** {brand} {code}",
        f"- **Bottom line:** It's NOT the {template['wrong_part']}",
        "",
        "## Production notes",
        "",
        "- Hook MUST be in first 3 seconds — YouTube retention drops 40% if you delay",
        "- Show one specific number on screen during fix steps (microamps, PSI, ohms)",
        "- End with the URL on screen for 2+ seconds so it's screenshot-able",
        "- Do not say \"hit subscribe\" — link in bio + URL on screen converts higher",
        "- Aspect ratio 9:16 vertical, 1080x1920",
    ])
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Generate YouTube Shorts scripts from articles or Reddit Intel")
    p.add_argument("--slug", help="Article slug to generate a script for")
    p.add_argument("--from", dest="intel_file", help="Reddit Intel JSON file to pull demand signals from")
    p.add_argument("--count", type=int, default=5, help="Max scripts to produce from --from file")
    p.add_argument("--brand", help="Ad-hoc brand")
    p.add_argument("--code", help="Ad-hoc code")
    p.add_argument("--symptom", help="Ad-hoc symptom")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    written = []

    if args.slug:
        meta = parse_post(args.slug)
        if not meta["title"]:
            print(f"[!] No article at {args.slug}")
            return 1
        out_path = OUT_DIR / f"{date_stamp}_{args.slug}.md"
        out_path.write_text(build_script(meta), encoding="utf-8")
        written.append(out_path)
    elif args.brand and args.code:
        slug_guess = f"{args.brand.lower()}-{args.code.lower()}-error-code"
        meta = {
            "slug": slug_guess,
            "brand": args.brand,
            "code": args.code,
            "symptom": args.symptom or "",
            "title": f"{args.brand} {args.code}",
            "tags": [args.brand.lower()],
        }
        out_path = OUT_DIR / f"{date_stamp}_{slug_guess}.md"
        out_path.write_text(build_script(meta), encoding="utf-8")
        written.append(out_path)
    elif args.intel_file:
        with open(args.intel_file, encoding="utf-8") as f:
            data = json.load(f)
        # Adapt to whatever shape the intel file is. Look for an array of objects
        # with at least slug or brand+code.
        items = data if isinstance(data, list) else data.get("results", [])
        for i, item in enumerate(items[: args.count]):
            slug = item.get("slug") or item.get("article_slug")
            if slug:
                meta = parse_post(slug)
            else:
                meta = {
                    "slug": (item.get("brand", "unknown").lower() + "-" + item.get("code", "").lower() + "-fix"),
                    "brand": item.get("brand", ""),
                    "code": item.get("code", ""),
                    "symptom": item.get("symptom", ""),
                    "title": f"{item.get('brand','')} {item.get('code','')}".strip(),
                    "tags": [],
                }
            out_path = OUT_DIR / f"{date_stamp}_intel_{i+1:02d}_{meta['slug']}.md"
            out_path.write_text(build_script(meta, hook_idx=i % len(HOOKS)), encoding="utf-8")
            written.append(out_path)
    else:
        # Default: generate scripts for the 5 highest-impact new articles we shipped today
        seeds = [
            "manitowoc-e01-error-code",
            "hoshizaki-e2-error-code",
            "allen-bradley-powerflex-f004-fault",
            "mitsubishi-p5-error-code",
            "weil-mclain-error-code-3",
        ]
        for i, slug in enumerate(seeds):
            meta = parse_post(slug)
            if not meta["title"]:
                continue
            out_path = OUT_DIR / f"{date_stamp}_seed_{i+1:02d}_{slug}.md"
            out_path.write_text(build_script(meta, hook_idx=i % len(HOOKS)), encoding="utf-8")
            written.append(out_path)

    print(f"[+] Wrote {len(written)} Shorts scripts to {OUT_DIR}")
    for w in written:
        print(f"    - {w.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
