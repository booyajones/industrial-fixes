#!/usr/bin/env python3
"""
Beehiiv weekly digest builder.

Reads the last 7 days of new + modified articles and assembles a 4-section
newsletter draft (HVAC / Refrigeration / Drives & CNC / Buying Guides)
ready to paste into the Beehiiv composer.

USAGE:
    python scripts/newsletter-digest.py            # last 7 days
    python scripts/newsletter-digest.py --days 14  # last 14 days

OUTPUT: growth-pipeline/newsletters/YYYY-MM-DD_digest.md

The output includes:
- Plain-text subject line A/B options
- Preheader text
- HTML body for Beehiiv composer
- Plain-text fallback
- Plausible UTM-tagged link variants for each article (so you can measure
  which sections of the newsletter drive the most clicks)
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "src" / "data" / "blog"
OUT_DIR = ROOT / "growth-pipeline" / "newsletters"
SITE = "https://errorcodefixes.com"


def parse_post(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^---\s*\n(.*?)^---\s*\n", text, re.DOTALL | re.MULTILINE)
    fm = {}
    tags = []
    if m:
        in_tags = False
        for line in m.group(1).splitlines():
            if in_tags and line.startswith("  - "):
                tags.append(line[4:].strip().strip('"').strip("'").lower())
                continue
            if line.strip().startswith("tags:") and ":" in line and line.strip().endswith(":"):
                in_tags = True
                continue
            in_tags = False
            if ":" not in line:
                continue
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return {
        "slug": path.stem,
        "title": fm.get("title", path.stem),
        "description": fm.get("description", ""),
        "pubDatetime": fm.get("pubDatetime", ""),
        "modDatetime": fm.get("modDatetime", ""),
        "tags": tags,
    }


def classify(post: dict) -> str:
    tags = set(post["tags"])
    slug = post["slug"]
    if any(t in tags for t in ("buying-guide", "tools", "comparison")):
        return "Buying Guides & Comparisons"
    if any(t in tags for t in ("refrigeration", "commercial-refrigeration", "ice-machine")):
        return "Refrigeration"
    if any(t in tags for t in ("vfd", "drives", "cnc")):
        return "Drives & CNC"
    if any(t in tags for t in ("hvac", "furnace", "mini-split", "boiler", "tankless", "heat-pump")):
        return "HVAC"
    if any(t in tags for t in ("appliances", "appliance-repair")):
        return "Appliances"
    if any(b in slug for b in ("samsung", "whirlpool", "maytag", "bosch", "lg-", "ge-", "frigidaire", "viking", "sub-zero")):
        return "Appliances"
    return "Other Fixes"


def parse_dt(s: str) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=7)
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)

    by_section: dict[str, list[dict]] = {}
    for path in sorted(BLOG.glob("*.md")):
        post = parse_post(path)
        pub_dt = parse_dt(post["pubDatetime"])
        mod_dt = parse_dt(post["modDatetime"])
        latest = max([d for d in [pub_dt, mod_dt] if d is not None], default=None)
        if not latest or latest < cutoff:
            continue
        section = classify(post)
        by_section.setdefault(section, []).append(post)

    if not any(by_section.values()):
        print("[!] No new/modified articles in the last N days. Skipping draft.")
        return 0

    # UTM-tagged URLs
    utm_base = "?utm_source=newsletter&utm_medium=email&utm_campaign=weekly-digest"
    date_stamp = datetime.now().strftime("%Y-%m-%d")

    SECTION_ORDER = [
        "HVAC", "Refrigeration", "Drives & CNC", "Appliances",
        "Buying Guides & Comparisons", "Other Fixes",
    ]

    # Build subject line options based on what's most-shipped
    biggest_section = max(by_section.items(), key=lambda kv: len(kv[1]))[0] if by_section else "fixes"
    total_new = sum(len(v) for v in by_section.values())

    subjects = [
        f"This week: {total_new} new error code fixes (incl. {biggest_section})",
        f"{total_new} new guides — what we shipped this week",
        f"New on errorcodefixes: {biggest_section} deep dives + {total_new - len(by_section.get(biggest_section, []))} more",
    ]
    preheader = f"Quick rundown of every guide we published or refreshed in the last {args.days} days, organized by equipment type. Skim and save the ones you'll need."

    lines = [
        f"# Beehiiv Weekly Digest — {date_stamp}",
        "",
        "## Subject line options (pick one and A/B test)",
        "",
    ]
    for i, s in enumerate(subjects, 1):
        lines.append(f"{i}. **{s}**  ({len(s)} chars — Gmail truncates at 60)")
    lines.append("")
    lines.append(f"## Preheader text")
    lines.append(f"")
    lines.append(f"> {preheader}")
    lines.append(f"")
    lines.append(f"## Schedule")
    lines.append(f"")
    lines.append(f"- **Best send time:** Tuesday or Thursday 10am Eastern (B2B technical audience)")
    lines.append(f"- **From name:** Industrial Error Code Fixes (or your real name)")
    lines.append(f"- **Reply-to:** chris.a.wyatt@gmail.com")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Newsletter body (paste into Beehiiv composer)")
    lines.append(f"")
    lines.append(f"### Opening")
    lines.append(f"")
    lines.append(f"We shipped {total_new} new and refreshed error-code guides this week. The most popular sections by request: {', '.join(list(by_section.keys())[:3])}.")
    lines.append(f"")
    lines.append(f"If anything below saves you a service call, forward it to a colleague. The button at the bottom unsubscribes one click if it ever stops being useful.")
    lines.append(f"")

    for section in SECTION_ORDER:
        posts = by_section.get(section, [])
        if not posts:
            continue
        lines.append(f"### {section}")
        lines.append(f"")
        # Cap each section at 8 items to keep the email scannable
        for post in posts[:8]:
            url = f"{SITE}/posts/{post['slug']}/{utm_base}"
            desc = (post["description"] or "")[:120]
            lines.append(f"- **[{post['title']}]({url})** — {desc}")
        if len(posts) > 8:
            lines.append(f"- _(+{len(posts) - 8} more in this category — full list at {SITE}/{utm_base})_")
        lines.append(f"")

    lines.extend([
        "### Closing CTA",
        "",
        f"All {total_new} of this week's guides are organized by brand at [errorcodefixes.com]({SITE}/{utm_base}). If a code you've been hunting isn't on the site, reply to this email with the brand + model + code and we'll prioritize it next week.",
        "",
        f"— Industrial Error Code Fixes",
        "",
        "---",
        "",
        "## Plain-text fallback",
        "",
        "(Beehiiv auto-generates this, but if you want to customize, here it is)",
        "",
        f"This week: {total_new} new error code guides.",
        "",
    ])
    for section in SECTION_ORDER:
        posts = by_section.get(section, [])
        if not posts:
            continue
        lines.append(f"{section}:")
        for post in posts[:5]:
            url = f"{SITE}/posts/{post['slug']}/{utm_base}"
            lines.append(f"- {post['title']}: {url}")
        lines.append("")
    lines.append(f"Read everything at {SITE}/{utm_base}")
    lines.append("")
    lines.append("Unsubscribe anytime — link below.")

    out_path = OUT_DIR / f"{date_stamp}_digest.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote newsletter digest covering {total_new} articles across {len([k for k in by_section if by_section[k]])} sections")
    print(f"    {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
