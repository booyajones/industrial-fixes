"""
build-lead-magnet.py
Generates the lead-magnet PDF that subscribers receive after opting in.

Output: public/resources/industrial-error-code-cheat-sheet.pdf

Strategy:
- Pull `featured: true` posts from src/data/blog (manual editorial picks).
- Group into 4 sections: HVAC, CNC, Refrigeration, Boilers/Plumbing.
- For each post, render: title, error meaning, top fix step, parts hint.
- Brand header with logo + footer with disclosure + URL.
- Single 4-6 page PDF, professional layout, no AI slop.

Run:  python scripts/build-lead-magnet.py
Idempotent. Safe to run on every content refresh.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from datetime import date

try:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        PageBreak,
        Table,
        TableStyle,
        KeepTogether,
    )
except ImportError:
    sys.stderr.write(
        "reportlab not installed. Run: pip install reportlab\n"
    )
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
BLOG_DIR = REPO / "src" / "data" / "blog"
OUT_DIR = REPO / "public" / "resources"
OUT_PDF = OUT_DIR / "industrial-error-code-cheat-sheet.pdf"

NAVY = HexColor("#1E3A5F")
RED = HexColor("#F04E4E")
GREEN = HexColor("#22C55E")
GREY = HexColor("#475569")
LIGHT = HexColor("#F1F5F9")

# Section assignment by tag overlap. Mirrors equipmentCategories.ts.
SECTION_TAGS = {
    "HVAC": {"hvac", "furnace", "heat-pump", "mini-split", "thermostat"},
    "Refrigeration": {
        "refrigeration",
        "commercial-refrigeration",
        "ice-machine",
        "commercial-refrigerator",
    },
    "CNC & Drives": {"cnc", "fanuc", "haas", "mazak", "vfd", "industrial"},
    "Boilers & Water Heaters": {"boiler", "tankless", "water-heater"},
}


def parse_post(path: Path) -> dict | None:
    """Read frontmatter + first paragraph from a blog markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_block = text[3:end].strip()
    body = text[end + 4 :].lstrip()

    fm: dict = {}
    current_list: list[str] | None = None
    current_key: str | None = None
    for line in fm_block.splitlines():
        if not line.strip():
            current_list = None
            current_key = None
            continue
        if line.startswith("  - ") and current_list is not None:
            current_list.append(line[4:].strip())
            continue
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            current_list = []
            fm[key] = current_list
            current_key = key
        else:
            current_list = None
            current_key = None
            fm[key] = val.strip('"').strip("'")
    # Body excerpt: first non-empty paragraph after H2 strip.
    excerpt = ""
    for paragraph in re.split(r"\n\s*\n", body):
        cleaned = re.sub(r"^#+\s+.*$", "", paragraph, flags=re.M).strip()
        cleaned = re.sub(r"\*\*(.+?)\*\*", r"\1", cleaned)
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
        cleaned = cleaned.replace("\n", " ").strip()
        if cleaned and len(cleaned) > 80:
            excerpt = cleaned[:280] + ("…" if len(cleaned) > 280 else "")
            break

    fm["_excerpt"] = excerpt
    fm["_slug"] = path.stem
    return fm


def assign_section(tags: list[str]) -> str | None:
    tag_set = {t.lower() for t in tags}
    for section, allowed in SECTION_TAGS.items():
        if tag_set & allowed:
            return section
    return None


def collect_entries() -> dict[str, list[dict]]:
    """Build sections: prefer `featured: true`, then top up with the most
    recently-modified guides until each section has up to 8 entries."""
    target_per_section = 8
    sections: dict[str, list[dict]] = {s: [] for s in SECTION_TAGS}
    pool: dict[str, list[dict]] = {s: [] for s in SECTION_TAGS}

    for path in sorted(BLOG_DIR.glob("*.md")):
        post = parse_post(path)
        if not post:
            continue
        if post.get("draft", "").lower() == "true":
            continue
        sec = assign_section(post.get("tags", []))
        if not sec:
            continue
        if post.get("featured", "").lower() in ("true", "yes"):
            sections[sec].append(post)
        else:
            pool[sec].append(post)

    def post_date(p: dict) -> str:
        return (p.get("modDatetime") or p.get("pubDatetime") or "0")

    for sec, picks in sections.items():
        if len(picks) >= target_per_section:
            sections[sec] = picks[:target_per_section]
            continue
        # Sort the unfeatured pool by mod date desc and top up.
        topup = sorted(pool[sec], key=post_date, reverse=True)
        need = target_per_section - len(picks)
        sections[sec] = picks + topup[:need]
    return sections


def build_pdf(sections: dict[str, list[dict]]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT_PDF),
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Industrial Error Code Quick Reference",
        author="Industrial Error Code Fixes",
    )

    base = getSampleStyleSheet()
    styles = {
        "h1": ParagraphStyle(
            "H1", parent=base["Title"], fontSize=24, leading=28,
            textColor=NAVY, spaceAfter=4, alignment=TA_LEFT,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle", parent=base["Normal"], fontSize=11, leading=14,
            textColor=GREY, spaceAfter=18, alignment=TA_LEFT,
        ),
        "section": ParagraphStyle(
            "Section", parent=base["Heading2"], fontSize=15, leading=18,
            textColor=NAVY, spaceBefore=14, spaceAfter=8, alignment=TA_LEFT,
        ),
        "title": ParagraphStyle(
            "EntryTitle", parent=base["Normal"], fontSize=11, leading=14,
            textColor=RED, spaceAfter=2, alignment=TA_LEFT, leftIndent=0,
            fontName="Helvetica-Bold",
        ),
        "body": ParagraphStyle(
            "EntryBody", parent=base["Normal"], fontSize=9.5, leading=13,
            textColor=HexColor("#1c1917"), spaceAfter=4, alignment=TA_LEFT,
            leftIndent=0,
        ),
        "url": ParagraphStyle(
            "EntryUrl", parent=base["Normal"], fontSize=8.5, leading=11,
            textColor=GREEN, spaceAfter=10, alignment=TA_LEFT,
            fontName="Helvetica-Oblique",
        ),
        "footer": ParagraphStyle(
            "Footer", parent=base["Normal"], fontSize=8, leading=11,
            textColor=GREY, alignment=TA_LEFT,
        ),
    }

    flow: list = []

    # Header
    flow.append(Paragraph("Industrial Error Code<br/>Quick Reference", styles["h1"]))
    flow.append(
        Paragraph(
            f"errorcodefixes.com  ·  Updated {date.today().strftime('%B %Y')}  "
            "·  HVAC · CNC · Refrigeration · Boilers",
            styles["subtitle"],
        )
    )

    intro = (
        "This is a triage-first reference for the fault codes that show up "
        "most often on industrial equipment. Each entry tells you what the "
        "code actually means, the most likely cause, and the first thing to "
        "check before pulling parts. For full step-by-step diagnostics, every "
        "entry links to the complete fix guide on errorcodefixes.com."
    )
    flow.append(Paragraph(intro, styles["body"]))
    flow.append(Spacer(1, 12))

    # Body
    total = 0
    for section_name, entries in sections.items():
        if not entries:
            continue
        flow.append(Paragraph(section_name, styles["section"]))
        flow.append(
            Table(
                [[""]],
                colWidths=[7.1 * inch],
                rowHeights=[1.2],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                        ("LINEBELOW", (0, 0), (-1, -1), 0, NAVY),
                    ]
                ),
            )
        )
        flow.append(Spacer(1, 6))

        for entry in entries:
            slug = entry["_slug"]
            url = f"https://errorcodefixes.com/posts/{slug}/"
            block = [
                Paragraph(entry.get("title", "Untitled"), styles["title"]),
                Paragraph(entry.get("description", entry.get("_excerpt", "")), styles["body"]),
                Paragraph(url, styles["url"]),
            ]
            flow.append(KeepTogether(block))
            total += 1

    # Footer
    flow.append(Spacer(1, 18))
    flow.append(
        Paragraph(
            f"{total} fault codes covered · Full library at errorcodefixes.com · "
            "Affiliate disclosure: errorcodefixes.com/disclosure/ · "
            f"© {date.today().year} Industrial Error Code Fixes",
            styles["footer"],
        )
    )

    doc.build(flow)
    print(f"OK  wrote {OUT_PDF}  ({OUT_PDF.stat().st_size:,} bytes, {total} entries)")


# Slugs match the equipment-hub URLs and the EmailCapture category prop.
SECTION_SLUG = {
    "HVAC": "hvac",
    "CNC & Drives": "cnc",
    "Refrigeration": "refrigeration",
    "Boilers & Water Heaters": "boilers",
}


def collect_section_pool(section_name: str, target: int) -> list[dict]:
    """Pull the deepest pool of posts for a single section (featured first,
    then most-recent unfeatured) up to `target` entries."""
    allowed = SECTION_TAGS[section_name]
    featured: list[dict] = []
    unfeatured: list[dict] = []
    for path in sorted(BLOG_DIR.glob("*.md")):
        post = parse_post(path)
        if not post:
            continue
        if post.get("draft", "").lower() == "true":
            continue
        tags = {t.lower() for t in post.get("tags", [])}
        if not (tags & allowed):
            continue
        if post.get("featured", "").lower() in ("true", "yes"):
            featured.append(post)
        else:
            unfeatured.append(post)
    unfeatured.sort(
        key=lambda p: p.get("modDatetime") or p.get("pubDatetime") or "0",
        reverse=True,
    )
    return (featured + unfeatured)[:target]


def build_section_pdf(section_name: str, slug: str, entries: list[dict]) -> None:
    out = OUT_DIR / f"{slug}-error-code-cheat-sheet.pdf"
    doc = SimpleDocTemplate(
        str(out), pagesize=LETTER,
        leftMargin=0.7 * inch, rightMargin=0.7 * inch,
        topMargin=0.6 * inch, bottomMargin=0.6 * inch,
        title=f"{section_name} Error Code Quick Reference",
        author="Industrial Error Code Fixes",
    )
    base = getSampleStyleSheet()
    s = {
        "h1": ParagraphStyle("H1", parent=base["Title"], fontSize=22, leading=26,
                             textColor=NAVY, spaceAfter=4, alignment=TA_LEFT),
        "subtitle": ParagraphStyle("Subtitle", parent=base["Normal"], fontSize=11,
                                   leading=14, textColor=GREY, spaceAfter=18, alignment=TA_LEFT),
        "title": ParagraphStyle("EntryTitle", parent=base["Normal"], fontSize=11, leading=14,
                                textColor=RED, spaceAfter=2, alignment=TA_LEFT,
                                fontName="Helvetica-Bold"),
        "body": ParagraphStyle("EntryBody", parent=base["Normal"], fontSize=9.5, leading=13,
                               textColor=HexColor("#1c1917"), spaceAfter=4, alignment=TA_LEFT),
        "url": ParagraphStyle("EntryUrl", parent=base["Normal"], fontSize=8.5, leading=11,
                              textColor=GREEN, spaceAfter=10, alignment=TA_LEFT,
                              fontName="Helvetica-Oblique"),
        "footer": ParagraphStyle("Footer", parent=base["Normal"], fontSize=8, leading=11,
                                 textColor=GREY, alignment=TA_LEFT),
    }
    flow: list = []
    flow.append(Paragraph(f"{section_name} Error Code<br/>Quick Reference", s["h1"]))
    flow.append(Paragraph(
        f"errorcodefixes.com  ·  Updated {date.today().strftime('%B %Y')}  ·  "
        f"Deep-dive cheat sheet on {section_name.lower()} fault codes.",
        s["subtitle"],
    ))
    flow.append(Paragraph(
        f"This is the focused {section_name} cheat sheet — every entry below is a "
        f"common fault you'll see in the field, with the meaning, the most likely "
        f"cause, and a link to the full diagnostic guide on errorcodefixes.com.",
        s["body"],
    ))
    flow.append(Spacer(1, 12))
    flow.append(Table([[""]], colWidths=[7.1 * inch], rowHeights=[1.2],
                      style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY)])))
    flow.append(Spacer(1, 8))
    for entry in entries:
        slug_p = entry["_slug"]
        url = f"https://errorcodefixes.com/posts/{slug_p}/"
        flow.append(KeepTogether([
            Paragraph(entry.get("title", "Untitled"), s["title"]),
            Paragraph(entry.get("description", entry.get("_excerpt", "")), s["body"]),
            Paragraph(url, s["url"]),
        ]))
    flow.append(Spacer(1, 18))
    flow.append(Paragraph(
        f"{len(entries)} {section_name.lower()} fault codes covered · "
        f"Full library at errorcodefixes.com · "
        f"Affiliate disclosure: errorcodefixes.com/disclosure/ · "
        f"© {date.today().year} Industrial Error Code Fixes",
        s["footer"],
    ))
    doc.build(flow)
    print(f"OK  wrote {out}  ({out.stat().st_size:,} bytes, {len(entries)} entries)")


def main() -> None:
    sections = collect_entries()
    build_pdf(sections)
    # Per-category PDFs: deeper pool (up to 16 entries each).
    for section_name, slug in SECTION_SLUG.items():
        entries = collect_section_pool(section_name, target=16)
        if entries:
            build_section_pdf(section_name, slug, entries)


if __name__ == "__main__":
    main()
