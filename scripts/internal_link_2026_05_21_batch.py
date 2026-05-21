#!/usr/bin/env python3
"""Inject internal links FROM existing articles TO the 2026-05-21 catalog
expansion targets. Reuses the same pattern + injection logic as
internal_link_for_new_articles.py but with a wider target set.

Strategy: pick the highest-value subset of the 131 net-new articles
(comparisons + buying guides + brand cluster keystones) and inject links
from existing articles that share tags. Cap conservative (4-6 per target)
to avoid look-spammy linking patterns.

Dry-run by default. Pass --apply to write.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
LINK_SECTION_MARKER = "<!-- INTERNAL-LINK-AUTO-2026-05-21 -->"

# Highest-value targets from the 2026-05-21 catalog expansion.
# Comparisons + buying guides + brand-cluster keystones.
NEW_ARTICLES = [
    # === Brand-vs-brand comparisons (8) ===
    {"slug": "carrier-vs-trane-furnaces", "anchor": "Carrier vs Trane furnaces compared",
     "match_tags": {"carrier", "trane", "furnace", "hvac"}, "max_links": 6},
    {"slug": "goodman-vs-bryant-furnaces", "anchor": "Goodman vs Bryant furnaces compared",
     "match_tags": {"goodman", "bryant", "furnace", "hvac"}, "max_links": 6},
    {"slug": "hoshizaki-vs-manitowoc-ice-machines", "anchor": "Hoshizaki vs Manitowoc ice machines",
     "match_tags": {"hoshizaki", "manitowoc", "ice-machine", "commercial-refrigeration"}, "max_links": 6},
    {"slug": "manitowoc-vs-scotsman-ice-machines", "anchor": "Manitowoc vs Scotsman ice machines",
     "match_tags": {"manitowoc", "scotsman", "ice-machine", "commercial-refrigeration"}, "max_links": 6},
    {"slug": "powerflex-vs-sinamics-vfd", "anchor": "PowerFlex vs SINAMICS VFD compared",
     "match_tags": {"allen-bradley", "siemens", "vfd", "drives"}, "max_links": 6},
    {"slug": "fanuc-vs-mazak-cnc-controls", "anchor": "Fanuc vs Mazak CNC controls compared",
     "match_tags": {"fanuc", "mazak", "cnc"}, "max_links": 6},
    {"slug": "mitsubishi-vs-daikin-mini-splits", "anchor": "Mitsubishi vs Daikin mini splits",
     "match_tags": {"mitsubishi", "daikin", "mini-split", "hvac"}, "max_links": 6},
    {"slug": "samsung-vs-lg-french-door-refrigerators", "anchor": "Samsung vs LG French door refrigerators",
     "match_tags": {"samsung", "lg", "refrigerator", "appliances"}, "max_links": 6},

    # === Buying guides (12) — high commercial intent ===
    {"slug": "best-multimeter-for-hvac", "anchor": "Best multimeter for HVAC techs (2026)",
     "match_tags": {"hvac", "tools", "industrial-maintenance"}, "max_links": 8},
    {"slug": "best-combustion-analyzer", "anchor": "Best combustion analyzer (2026)",
     "match_tags": {"hvac", "furnace", "boiler", "tools"}, "max_links": 6},
    {"slug": "best-manometer-for-hvac", "anchor": "Best HVAC manometer (2026)",
     "match_tags": {"hvac", "tools", "furnace"}, "max_links": 6},
    {"slug": "best-refrigerant-gauge-set", "anchor": "Best refrigerant gauge set (2026)",
     "match_tags": {"hvac", "refrigeration", "tools", "commercial-refrigeration"}, "max_links": 6},
    {"slug": "best-megohmmeter-for-electricians", "anchor": "Best megohmmeter for electricians",
     "match_tags": {"vfd", "drives", "industrial-maintenance", "cnc"}, "max_links": 6},
    {"slug": "best-thermal-imager-for-hvac", "anchor": "Best thermal imager for HVAC",
     "match_tags": {"hvac", "tools"}, "max_links": 4},
    {"slug": "best-clamp-meter-for-electricians", "anchor": "Best clamp meter (2026)",
     "match_tags": {"vfd", "industrial-maintenance", "tools"}, "max_links": 6},
    {"slug": "best-vacuum-pump-for-refrigeration", "anchor": "Best refrigeration vacuum pump",
     "match_tags": {"refrigeration", "commercial-refrigeration", "tools"}, "max_links": 6},
    {"slug": "best-refrigerant-leak-detector", "anchor": "Best refrigerant leak detector",
     "match_tags": {"refrigeration", "hvac", "tools"}, "max_links": 6},
    {"slug": "best-loop-calibrator-for-vfd-techs", "anchor": "Best 4-20mA loop calibrator",
     "match_tags": {"vfd", "drives", "industrial-maintenance"}, "max_links": 4},
    {"slug": "best-boiler-test-kit", "anchor": "Best boiler test kit",
     "match_tags": {"boiler", "hydronic", "hvac"}, "max_links": 4},
    {"slug": "best-cnc-touch-probe", "anchor": "Best CNC touch probe (2026)",
     "match_tags": {"cnc", "industrial-maintenance"}, "max_links": 4},

    # === Brand-cluster keystones (highest-volume code per brand we shipped) ===
    {"slug": "manitowoc-e01-error-code", "anchor": "Manitowoc E01 long freeze cycle fix",
     "match_tags": {"manitowoc", "ice-machine"}, "max_links": 6},
    {"slug": "manitowoc-hpco-error-code", "anchor": "Manitowoc HPCO high pressure cutout",
     "match_tags": {"manitowoc", "ice-machine"}, "max_links": 4},
    {"slug": "hoshizaki-e2-error-code", "anchor": "Hoshizaki E2 long freeze cycle fix",
     "match_tags": {"hoshizaki", "ice-machine"}, "max_links": 6},
    {"slug": "scotsman-1-flash-code", "anchor": "Scotsman 1-flash bin full fix",
     "match_tags": {"scotsman", "ice-machine"}, "max_links": 6},
    {"slug": "allen-bradley-powerflex-f004-fault", "anchor": "PowerFlex F004 undervoltage fix",
     "match_tags": {"allen-bradley", "powerflex", "vfd"}, "max_links": 6},
    {"slug": "allen-bradley-powerflex-f012-fault", "anchor": "PowerFlex F012 hardware overcurrent",
     "match_tags": {"allen-bradley", "powerflex", "vfd"}, "max_links": 6},
    {"slug": "mitsubishi-p5-error-code", "anchor": "Mitsubishi mini split P5 drain fault",
     "match_tags": {"mitsubishi", "mini-split"}, "max_links": 6},
    {"slug": "weil-mclain-error-code-3", "anchor": "Weil-McLain code 3 low water cutoff",
     "match_tags": {"weil-mclain", "boiler", "hydronic"}, "max_links": 4},
    {"slug": "rinnai-error-code-11", "anchor": "Rinnai code 11 no-ignition fix",
     "match_tags": {"rinnai", "tankless", "water-heater"}, "max_links": 4},
    {"slug": "daikin-error-code-u4", "anchor": "Daikin U4 indoor-outdoor comm fault",
     "match_tags": {"daikin", "mini-split"}, "max_links": 4},
    {"slug": "fanuc-alarm-401", "anchor": "Fanuc alarm 401 servo ready off",
     "match_tags": {"fanuc", "cnc"}, "max_links": 4},
    {"slug": "mazak-alarm-218", "anchor": "Mazak alarm 218 spindle overheat",
     "match_tags": {"mazak", "cnc"}, "max_links": 4},
    {"slug": "haas-alarm-114", "anchor": "Haas alarm 114 servo error too large",
     "match_tags": {"haas", "cnc"}, "max_links": 4},
]


def parse_frontmatter_tags(text: str) -> set[str]:
    m = re.search(r"^---\s*\n(.*?)^---\s*\n", text, re.DOTALL | re.MULTILINE)
    if not m:
        return set()
    fm = m.group(1)
    tags: set[str] = set()
    inline = re.search(r"^tags\s*:\s*\[(.*?)\]", fm, re.MULTILINE)
    if inline:
        for t in inline.group(1).split(","):
            t = t.strip().strip('"').strip("'").lower()
            if t:
                tags.add(t)
        return tags
    list_m = re.search(r"^tags\s*:\s*\n((?:\s+-\s+.+\n)+)", fm, re.MULTILINE)
    if list_m:
        for line in list_m.group(1).splitlines():
            t = line.strip().lstrip("-").strip().strip('"').strip("'").lower()
            if t:
                tags.add(t)
    return tags


def already_links(text: str, slug: str) -> bool:
    return f"/posts/{slug}/" in text or f"/posts/{slug})" in text


def inject_callout(text: str, slug: str, anchor: str) -> str:
    callout = (
        f"\n\n{LINK_SECTION_MARKER}\n"
        f"**Related:** [{anchor}](/posts/{slug}/)\n"
    )
    return text.rstrip() + callout + "\n"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    candidates_by_target: dict[str, list[Path]] = {a["slug"]: [] for a in NEW_ARTICLES}
    all_files = sorted(BLOG.glob("*.md"))

    for f in all_files:
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        tags = parse_frontmatter_tags(text)
        if not tags:
            continue
        for target in NEW_ARTICLES:
            if f.stem == target["slug"]:
                continue
            if tags & target["match_tags"]:
                if already_links(text, target["slug"]):
                    continue
                candidates_by_target[target["slug"]].append(f)

    # Rank by stem length (shorter = brand-overview = higher authority)
    for slug, candidates in candidates_by_target.items():
        candidates.sort(key=lambda p: len(p.stem))

    total = 0
    for target in NEW_ARTICLES:
        candidates = candidates_by_target[target["slug"]][: target["max_links"]]
        print(f"\n--> {target['slug']}: linking from {len(candidates)} files (cap {target['max_links']})")
        for f in candidates:
            text = f.read_text(encoding="utf-8")
            new = inject_callout(text, target["slug"], target["anchor"])
            if args.apply:
                f.write_text(new, encoding="utf-8")
            total += 1

    verb = "would inject" if not args.apply else "INJECTED"
    print(f"\n{verb} {total} internal links total across {len(NEW_ARTICLES)} new targets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
