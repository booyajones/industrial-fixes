#!/usr/bin/env python3
"""
Pinterest pin description batch generator.

Picks the highest-traffic-potential residential appliance + HVAC posts
from the catalog and writes 10-50 ready-to-paste Pinterest pin descriptions
with brand-driven keyword targeting.

WHY: Pinterest is the easiest residential repair traffic source. Pins
compound for years. Residential appliance audience does NOT mind clicking
out to merchant articles. Most pins are saved into "DIY home" boards that
re-surface seasonally.

USAGE:
    python scripts/pinterest-pin-batch.py
    python scripts/pinterest-pin-batch.py --limit 30 --topic refrigerator

OUTPUT: growth-pipeline/pinterest/YYYY-MM-DD_pins.md
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
OUT_DIR = ROOT / "growth-pipeline" / "pinterest"
SITE = "https://errorcodefixes.com"

# Pinterest works best on RESIDENTIAL/DIY content. Commercial refrigeration
# and industrial VFD pin terribly. Filter accordingly.
PINTEREST_FRIENDLY_TAGS = {
    "samsung", "whirlpool", "maytag", "bosch", "lg", "ge", "frigidaire", "sub-zero", "viking",
    "carrier", "trane", "goodman", "lennox", "rheem", "york", "bryant", "amana",
    "mitsubishi", "daikin", "fujitsu", "mini-split",
    "appliances", "appliance-repair", "hvac", "furnace", "refrigerator", "washer", "dishwasher", "dryer",
    "boiler", "water-heater", "tankless", "navien", "rinnai", "weil-mclain", "lochinvar",
}

NON_PINTEREST_TAGS = {
    "vfd", "drives", "cnc", "industrial-maintenance", "powerflex", "siemens", "abb",
    "yaskawa", "danfoss", "fanuc", "mazak", "haas", "commercial-refrigeration",
    "ice-machine", "hoshizaki", "manitowoc", "scotsman",  # commercial is wrong audience for Pinterest
}

# Pin templates by content type
TEMPLATE_FIX = """
**Pin {n}: {title}**
- **Pin title:** {pin_title}
- **Description:**
{description}
- **Destination URL:** {url}
- **Hashtags:** {hashtags}
- **Board fit:** Home Repair, DIY Tips, {board_fit}
- **Image idea:** Reference chart with error code on left, fix on right. Brand color background, large legible numbers. Add "save for later" hint in corner.

"""


def parse_post(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^---\s*\n(.*?)^---\s*\n", text, re.DOTALL | re.MULTILINE)
    fm = {}
    tags = []
    if m:
        for line in m.group(1).splitlines():
            if line.strip().startswith("- "):
                tags.append(line.strip().lstrip("-").strip())
                continue
            if ":" not in line:
                continue
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return {
        "slug": path.stem,
        "title": fm.get("title", path.stem),
        "description": fm.get("description", ""),
        "tags": [t.lower() for t in tags],
    }


def is_pinterest_friendly(post: dict) -> bool:
    tags = set(post["tags"])
    if tags & NON_PINTEREST_TAGS:
        return False
    if tags & PINTEREST_FRIENDLY_TAGS:
        return True
    # Slug-based fallback
    slug = post["slug"]
    if any(b in slug for b in ("samsung", "whirlpool", "maytag", "bosch", "lg-", "ge-", "frigidaire",
                                "carrier", "trane", "goodman", "lennox", "rheem", "york",
                                "bryant", "amana", "mitsubishi", "daikin", "fujitsu",
                                "boiler", "water-heater", "tankless", "navien", "rinnai")):
        return True
    return False


def shorten_title_for_pin(title: str) -> str:
    """Pinterest pin titles max 100 chars. Aim for 60-80 with action verb."""
    title = re.sub(r'\s+', ' ', title.strip())
    if len(title) <= 80:
        return title
    # Truncate at last space before 77 chars
    cut = title[:77].rsplit(' ', 1)[0]
    return cut + "..."


def build_description(post: dict) -> str:
    """Build a Pinterest description: ~300 chars, no marketing fluff, helpful action verb upfront."""
    title = post["title"]
    desc = post["description"] or ""

    # Extract a tight action line from the title
    if " — " in title:
        code_part, action_part = title.split(" — ", 1)
    else:
        code_part = title
        action_part = ""

    return f"""  {code_part}. {desc[:200]}

  Save this pin for the next time the appliance acts up. Full diagnostic at errorcodefixes.com.""".strip()


def derive_hashtags(post: dict) -> str:
    """3-5 Pinterest hashtags."""
    tags = post["tags"]
    out = []
    brand_tags = [t for t in tags if t in PINTEREST_FRIENDLY_TAGS][:2]
    for bt in brand_tags:
        out.append(f"#{bt.title().replace('-', '')}")
    if "refrigerator" in tags or "fridge" in post["slug"]:
        out.append("#ApplianceRepair")
        out.append("#KitchenTips")
    elif "washer" in tags:
        out.append("#LaundryRepair")
        out.append("#HomeOwnership")
    elif "dishwasher" in tags:
        out.append("#DishwasherFix")
        out.append("#KitchenAppliance")
    elif "furnace" in tags or "hvac" in tags:
        out.append("#HVACTips")
        out.append("#HomeMaintenance")
    elif "boiler" in tags or "tankless" in tags or "water-heater" in tags:
        out.append("#PlumbingTips")
        out.append("#HomeRepair")
    else:
        out.append("#HomeRepair")
        out.append("#DIY")
    if len(out) < 5:
        out.append("#FixIt")
    return " ".join(out[:5])


def derive_board_fit(post: dict) -> str:
    tags = post["tags"]
    if any(t in tags for t in ("refrigerator", "washer", "dishwasher", "dryer", "appliances", "appliance-repair")):
        return "Appliance Repair, Kitchen, Laundry"
    if any(t in tags for t in ("furnace", "hvac", "mini-split")):
        return "HVAC, Home Cooling, Winter Prep"
    if any(t in tags for t in ("boiler", "tankless", "water-heater")):
        return "Plumbing, Home Maintenance"
    return "Home Repair, DIY"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--topic", help="Filter to a specific keyword in slug (e.g. 'samsung', 'refrigerator')")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    out_path = OUT_DIR / f"{date_stamp}_pins.md"

    all_posts = sorted(BLOG.glob("*.md"))
    selected = []
    for path in all_posts:
        post = parse_post(path)
        if not is_pinterest_friendly(post):
            continue
        if args.topic and args.topic.lower() not in post["slug"].lower():
            continue
        selected.append(post)
        if len(selected) >= args.limit:
            break

    lines = [
        f"# Pinterest Pin Batch — {date_stamp}",
        f"",
        f"**{len(selected)} pins ready to publish.**",
        f"",
        f"## Workflow",
        f"1. Sign up for a Pinterest business account at pinterest.com/business/create if you haven't (5 min, instant).",
        f"2. Build a single 1000x1500 vertical pin template in Canva (30 min, free tier). Brand-consistent header bar, error-code on left, fix-summary on right, save-for-later corner.",
        f"3. For each pin below, duplicate the template, swap title text, save as PNG.",
        f"4. Upload to Pinterest with the title, description, hashtags, and destination URL shown.",
        f"5. Schedule 1-2 pins per business day. Pinterest's algorithm rewards consistency over volume.",
        f"6. Optional: use Tailwind ($15/mo) to schedule the whole batch in one sitting.",
        f"",
        f"## Critical do-not-do",
        f"- Do NOT pin commercial-refrigeration, VFD, or CNC content. Pinterest audience is residential.",
        f"- Do NOT use generic stock images. Real appliance failure images or branded reference charts only.",
        f"- Do NOT crowd the pin with text. Two phrases max.",
        f"",
        f"## The {len(selected)} pins",
        "",
    ]

    for i, post in enumerate(selected, 1):
        pin = TEMPLATE_FIX.format(
            n=i,
            title=post["title"],
            pin_title=shorten_title_for_pin(post["title"]),
            description=build_description(post),
            url=f"{SITE}/posts/{post['slug']}/",
            hashtags=derive_hashtags(post),
            board_fit=derive_board_fit(post),
        )
        lines.append(pin)

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {len(selected)} pin descriptions to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
