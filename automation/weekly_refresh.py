"""
Weekly refresh planner for errorcodefixes.com.

Scans the local catalog (or a remote sitemap) to identify the oldest 5-10
guides, generates a refresh checklist for each, and produces a weekly
refresh task list. This is how you avoid SEO decay from stale dateModified.

USAGE:
    python weekly_refresh.py
        Looks at all .md guides in ../new-guides and existing schema/ folder,
        picks the 5 oldest by updated date, writes a refresh briefing.

    python weekly_refresh.py --count 10 --include-existing
        Pick 10 guides, including the original 15 existing guides.

DEPENDENCIES: stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
BUNDLE_ROOT = SCRIPT_DIR.parent
NEW_GUIDES_DIR = BUNDLE_ROOT / "new-guides"
SCHEMA_DIR = BUNDLE_ROOT / "schema"


@dataclass
class GuideCatalogEntry:
    slug: str
    title: str
    brand: str
    category: str
    updated: str
    updated_days_ago: int
    source: str  # "new-guides" or "schema-only" or "existing"
    refresh_priority_score: float
    refresh_actions: list[str]


def parse_md_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    body = text[3:end].strip()
    out = {}
    for line in body.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip().strip('"').strip("'")
        out[k.strip()] = v
    return out


def parse_schema_dates(schema_html: str) -> tuple[str | None, str | None]:
    """Extract datePublished and dateModified from a schema HTML file."""
    pub_match = re.search(r'"datePublished":\s*"([^"]+)"', schema_html)
    mod_match = re.search(r'"dateModified":\s*"([^"]+)"', schema_html)
    return (
        pub_match.group(1) if pub_match else None,
        mod_match.group(1) if mod_match else None,
    )


def parse_date(s: str) -> datetime | None:
    if not s:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s.split("+")[0].split("Z")[0], fmt.replace("%z", "").replace("Z", ""))
        except ValueError:
            continue
    return None


def load_catalog() -> list[GuideCatalogEntry]:
    catalog: list[GuideCatalogEntry] = []
    today = datetime.now()

    # 1. Scan new-guides/*.md
    if NEW_GUIDES_DIR.exists():
        for md in NEW_GUIDES_DIR.glob("*.md"):
            if md.name.upper().startswith("BATCH") or md.name.endswith("SUMMARY.md"):
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            fm = parse_md_frontmatter(text)
            updated_str = fm.get("updated", "")
            updated_dt = parse_date(updated_str)
            days_ago = (today - updated_dt).days if updated_dt else 9999
            catalog.append(GuideCatalogEntry(
                slug=fm.get("slug", md.stem),
                title=fm.get("title", md.stem),
                brand=fm.get("brand", ""),
                category=fm.get("category", ""),
                updated=updated_str,
                updated_days_ago=days_ago,
                source="new-guides",
                refresh_priority_score=0.0,
                refresh_actions=[],
            ))

    # 2. Existing guides (no .md in new-guides) — read from schema files
    if SCHEMA_DIR.exists():
        slugs_already = {e.slug for e in catalog}
        for html in SCHEMA_DIR.glob("*.html"):
            slug = html.stem
            if slug in slugs_already or slug.startswith("NEW_GUIDES"):
                continue
            content = html.read_text(encoding="utf-8", errors="replace")
            _, mod_iso = parse_schema_dates(content)
            mod_dt = parse_date(mod_iso) if mod_iso else None
            days_ago = (today - mod_dt).days if mod_dt else 9999
            # Try to extract title from headline field
            title_match = re.search(r'"headline":\s*"([^"]+)"', content)
            title = title_match.group(1) if title_match else slug
            brand_match = re.search(r'"name":\s*"([A-Z][a-zA-Z\-]+)"', content)
            brand = brand_match.group(1) if brand_match else ""
            catalog.append(GuideCatalogEntry(
                slug=slug,
                title=title,
                brand=brand,
                category="",
                updated=mod_iso or "",
                updated_days_ago=days_ago,
                source="existing",
                refresh_priority_score=0.0,
                refresh_actions=[],
            ))
    return catalog


def score_refresh_priority(entry: GuideCatalogEntry) -> tuple[float, list[str]]:
    """Higher score = more urgent to refresh."""
    score = 0.0
    actions: list[str] = []

    # Days since updated — main signal
    days = entry.updated_days_ago
    if days > 365:
        score += 10
        actions.append(f"Critical: {days}d since updated — Google rankings decay above 365d")
    elif days > 180:
        score += 6
        actions.append(f"Stale: {days}d since updated — refresh recommended")
    elif days > 90:
        score += 3
        actions.append(f"{days}d since updated — within normal cadence, optional refresh")

    # Existing guides (original 15) likely have older content
    if entry.source == "existing":
        score += 2
        actions.append("Original guide — likely needs photo + named-tech byline update if not done")

    # No category metadata
    if not entry.category and entry.source == "existing":
        actions.append("Verify schema + FAQ block deployed")

    # High-value brand keywords
    if entry.brand.lower() in ("carrier", "hoshizaki", "manitowoc", "mitsubishi"):
        score += 1.5
        actions.append(f"High-value brand ({entry.brand}) — prioritize refresh")

    return (round(score, 2), actions)


def write_refresh_briefing(entries: list[GuideCatalogEntry], count: int) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    path = OUTPUT_DIR / f"refresh_briefing_{date_stamp}.md"

    selected = sorted(entries, key=lambda e: -e.refresh_priority_score)[:count]

    lines = [
        f"# Weekly Refresh Briefing — {date_stamp}",
        "",
        f"**Total catalog:** {len(entries)} guides",
        f"**Stale (>180d):** {sum(1 for e in entries if e.updated_days_ago > 180)}",
        f"**Critical (>365d):** {sum(1 for e in entries if e.updated_days_ago > 365)}",
        "",
        f"## This week's refresh queue ({count} guides)",
        "",
    ]
    for i, e in enumerate(selected, 1):
        lines.extend([
            f"### {i}. {e.title}",
            f"- **Slug:** `{e.slug}`",
            f"- **Brand:** {e.brand or '—'}",
            f"- **Last updated:** {e.updated or 'unknown'} ({e.updated_days_ago}d ago)",
            f"- **Priority score:** {e.refresh_priority_score}",
            "",
            "**Refresh checklist:**",
        ])
        for action in e.refresh_actions:
            lines.append(f"- [ ] {action}")
        lines.extend([
            "- [ ] Bump `dateModified` to today in schema + visible 'Updated:' stamp",
            "- [ ] Add 1 new FAQ entry (Q&A) matching a current Google PAA question for this code",
            "- [ ] Verify all affiliate links still resolve (run `affiliate_link_check.py` after refresh)",
            "- [ ] Add 1 internal link to a sibling guide published since last refresh",
            "- [ ] Validate schema in Google Rich Results Test",
            "- [ ] Re-request indexing in Search Console",
            "",
        ])

    lines.extend([
        "",
        "## Full catalog (sorted by staleness)",
        "",
        "| Slug | Brand | Days old | Score | Source |",
        "|---|---|---|---|---|",
    ])
    for e in sorted(entries, key=lambda x: -x.updated_days_ago):
        lines.append(f"| `{e.slug}` | {e.brand or '—'} | {e.updated_days_ago} | {e.refresh_priority_score} | {e.source} |")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Weekly refresh planner")
    ap.add_argument("--count", type=int, default=5, help="Number of guides to surface in this week's queue")
    args = ap.parse_args(argv)

    catalog = load_catalog()
    for e in catalog:
        e.refresh_priority_score, e.refresh_actions = score_refresh_priority(e)

    path = write_refresh_briefing(catalog, args.count)
    print(f"[+] Refresh briefing: {path}")
    print(f"    Catalog size: {len(catalog)}")
    print(f"    Stale (>180d): {sum(1 for e in catalog if e.updated_days_ago > 180)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
