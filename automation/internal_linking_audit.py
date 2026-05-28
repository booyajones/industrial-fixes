"""
Internal linking audit + suggester for errorcodefixes.com.

Scans every guide's content + extracts existing internal links, then
identifies missed opportunities where a guide mentions a brand/code that
matches another guide's slug but doesn't link to it.

Internal linking is the highest-leverage SEO lever for an established
content site. Most catalogs leave 50-80% of their internal-link potential
on the floor. This finds the gaps.

USAGE:
    python internal_linking_audit.py
        Writes output/internal_links_YYYY-MM-DD.md with suggestions

    python internal_linking_audit.py --file ../new-guides/carrier-13-error-code.md
        Audit one specific guide

DEPENDENCIES: stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
BUNDLE_ROOT = SCRIPT_DIR.parent
GUIDES_DIR = BUNDLE_ROOT / "new-guides"


@dataclass
class GuideMeta:
    slug: str
    title: str
    brand: str
    category: str
    code: str
    path: Path
    body_lowered: str
    existing_links: set[str] = field(default_factory=set)


@dataclass
class LinkSuggestion:
    source_slug: str
    source_title: str
    target_slug: str
    target_title: str
    reason: str
    anchor_text_options: list[str]
    confidence: str  # high / medium / low


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return ({}, text)
    end = text.find("\n---", 3)
    if end == -1:
        return ({}, text)
    fm_text = text[3:end].strip()
    body = text[end + 4:]
    fm = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return (fm, body)


def extract_existing_internal_links(body: str) -> set[str]:
    """Find all /posts/<slug> references in the guide body."""
    links = set(re.findall(r"/posts/([a-z0-9\-]+)", body))
    return links


def load_catalog() -> list[GuideMeta]:
    catalog: list[GuideMeta] = []
    for md in GUIDES_DIR.glob("*.md"):
        if md.name.upper().startswith("BATCH") or md.name.endswith("SUMMARY.md") or md.name.upper() == "INDEX.MD":
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        if not fm.get("slug"):
            continue
        catalog.append(GuideMeta(
            slug=fm["slug"],
            title=fm.get("title", md.stem),
            brand=fm.get("brand", "").lower(),
            category=fm.get("category", "").lower(),
            code=fm.get("code", ""),
            path=md,
            body_lowered=body.lower(),
            existing_links=extract_existing_internal_links(body),
        ))
    return catalog


def find_suggestions(catalog: list[GuideMeta]) -> list[LinkSuggestion]:
    by_slug = {g.slug: g for g in catalog}
    suggestions: list[LinkSuggestion] = []

    for source in catalog:
        for target in catalog:
            if source.slug == target.slug:
                continue
            if target.slug in source.existing_links:
                continue  # already linked

            reasons: list[str] = []
            confidence = "low"
            anchors: list[str] = []

            # Brand-match — same brand often justifies a sibling link
            if target.brand and target.brand == source.brand:
                if source.category == target.category:
                    reasons.append(f"Same brand ({target.brand}) and category ({target.category})")
                    confidence = "high"
                    anchors.append(f"{target.brand.title()} code {target.code}")
                    anchors.append(target.title.split(" — ")[0])
                else:
                    reasons.append(f"Same brand ({target.brand}) — cross-category")
                    confidence = "medium"

            # Code mentioned in source body
            if target.code:
                code_lower = target.code.lower()
                if len(code_lower) > 1 and code_lower in source.body_lowered:
                    reasons.append(f"Source mentions code '{target.code}'")
                    confidence = "high"
                    anchors.append(f"{target.brand.title()} {target.code}".strip())

            # Brand mentioned in source body and we have a code-specific guide
            if target.brand and target.code and target.brand in source.body_lowered:
                # Only add if not already qualified above
                if not any(r.startswith("Same brand") for r in reasons):
                    if f"{target.brand} {target.code.lower()}" in source.body_lowered:
                        reasons.append(f"Source mentions '{target.brand} {target.code}'")
                        confidence = "high"
                        anchors.append(f"{target.brand.title()} {target.code}")

            # Related-fault co-occurrence (e.g., guides on lockout-pair codes like 13/33)
            if confidence == "low" and target.brand == source.brand and target.code and source.code:
                code_pair_patterns = [
                    (source.code, target.code),
                    (target.code, source.code),
                ]
                for a, b in code_pair_patterns:
                    if f"code {a}" in source.body_lowered and f"code {b}" in source.body_lowered:
                        reasons.append(f"Source compares codes {a} vs {b}")
                        confidence = "high"
                        anchors.append(f"code {target.code}")
                        break

            if not reasons:
                continue

            suggestions.append(LinkSuggestion(
                source_slug=source.slug,
                source_title=source.title,
                target_slug=target.slug,
                target_title=target.title,
                reason="; ".join(reasons),
                anchor_text_options=list(dict.fromkeys(anchors))[:3],  # de-dup, top 3
                confidence=confidence,
            ))

    # Sort: high confidence first, grouped by source guide
    return sorted(suggestions, key=lambda s: (s.confidence != "high", s.source_slug))


def write_report(suggestions: list[LinkSuggestion], catalog: list[GuideMeta]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    md_path = OUTPUT_DIR / f"internal_links_{date_stamp}.md"
    json_path = OUTPUT_DIR / f"internal_links_{date_stamp}.json"

    json_path.write_text(json.dumps([asdict(s) for s in suggestions], indent=2), encoding="utf-8")

    high = [s for s in suggestions if s.confidence == "high"]
    medium = [s for s in suggestions if s.confidence == "medium"]

    # Group high-confidence suggestions by source guide
    by_source: dict[str, list[LinkSuggestion]] = {}
    for s in high:
        by_source.setdefault(s.source_slug, []).append(s)

    lines = [
        f"# Internal Linking Audit — {date_stamp}",
        "",
        f"- **Catalog size:** {len(catalog)} guides",
        f"- **High-confidence missed links:** {len(high)}",
        f"- **Medium-confidence missed links:** {len(medium)}",
        "",
        "## Workflow",
        "",
        "1. Open each source guide listed below.",
        "2. For each suggested target, add an inline link in the body where it naturally fits (often inside the 'Related guides' section, or inline where the source already mentions the target's brand/code).",
        "3. Use one of the suggested anchor text variants — don't repeat the same exact-match anchor too often (Google penalizes anchor stuffing).",
        "4. After fixing 5-10 guides, rerun this script to refresh suggestions.",
        "",
        f"## High-priority links (grouped by source guide — {len(by_source)} guides need attention)",
        "",
    ]

    for source_slug in sorted(by_source.keys()):
        targets = by_source[source_slug]
        source_title = targets[0].source_title
        lines.extend([
            f"### {source_title}",
            f"`{source_slug}.md` — add {len(targets)} link(s):",
            "",
        ])
        for s in targets:
            anchors_text = " / ".join(f'"{a}"' for a in s.anchor_text_options) or '"(see related guides)"'
            lines.extend([
                f"- → `/posts/{s.target_slug}`",
                f"  - **Anchor options:** {anchors_text}",
                f"  - **Why:** {s.reason}",
                "",
            ])

    lines.extend([
        "",
        "## Medium-confidence suggestions (review case-by-case)",
        "",
    ])
    for s in medium[:40]:
        lines.append(f"- `{s.source_slug}` → `{s.target_slug}` ({s.reason})")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {md_path}")
    print(f"[+] Wrote {json_path}")
    return md_path


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Internal linking audit + suggester")
    ap.add_argument("--file", type=Path, help="Audit one specific guide")
    args = ap.parse_args(argv)

    catalog = load_catalog()
    print(f"[+] Loaded {len(catalog)} guides")

    suggestions = find_suggestions(catalog)
    if args.file:
        slug = args.file.stem
        suggestions = [s for s in suggestions if s.source_slug == slug]
        print(f"[+] Filtered to {len(suggestions)} suggestions for {slug}")

    write_report(suggestions, catalog)
    print(f"\n{len(suggestions)} total suggestions")
    print(f"  High confidence:   {sum(1 for s in suggestions if s.confidence == 'high')}")
    print(f"  Medium confidence: {sum(1 for s in suggestions if s.confidence == 'medium')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
