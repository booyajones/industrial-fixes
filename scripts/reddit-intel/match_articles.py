"""Match classified Reddit hits against our existing article corpus.

Outputs a gap classification per hit:
  - "covered"      — we already have an article whose slug matches brand+code
  - "serp_gap"     — brand+code are in our corpus but the Reddit phrasing
                     doesn't match our H2s (this surfaces SEO opportunities)
  - "content_gap"  — no article for this brand+code combo. Highest-value.

The corpus is just the union of slugs under src/data/blog/*.md. We don't need
to parse frontmatter — slugs already encode brand+code (e.g.
'rinnai-error-code-11', 'true-refrigeration-e1-error-code').
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from classify import Classified  # noqa: F401  — re-exported for type hint clarity


def load_corpus(blog_dir: Path) -> set[str]:
    """Set of article slug-stems (filename without .md)."""
    return {p.stem.lower() for p in blog_dir.glob("*.md")}


def _candidate_slugs(brand: str, code: str) -> list[str]:
    """Plausible slug variants for a brand+code pair.

    Articles in src/data/blog/ use mixed conventions — some keep the leading
    letter prefix (e.g. true-refrigeration-e1-error-code) and some strip it
    (e.g. carrier-error-code-13 from a Carrier E13 fault). Generate both
    so we don't miss matches just because of a naming convention drift.
    """
    b = brand.lower().replace(" ", "-").replace("'", "")
    c = code.lower()
    # Numeric-only variant when the extracted code has a single-letter prefix
    digits = re.sub(r"^[a-z]", "", c) if c and c[0].isalpha() else ""
    code_variants = [c]
    if digits and digits != c:
        code_variants.append(digits)
    out: list[str] = []
    for cv in code_variants:
        out.extend([
            f"{b}-error-code-{cv}",
            f"{b}-{cv}-error-code",
            f"{b}-{cv}",
            f"{b}-error-{cv}",
            f"{b}-fault-{cv}",
            f"{b}-code-{cv}",
        ])
    # Whole-brand fallback pages
    out.extend([f"{b}-error-codes", f"{b}-fault-codes"])
    return out


def classify_gap(hit: Classified, corpus: set[str]) -> tuple[str, str | None]:
    """Returns (gap_kind, matched_slug_or_None)."""
    if not hit.brand:
        return ("unknown", None)
    if not hit.extracted_codes:
        # Brand mentioned but no specific code surfaced. Check if we have a
        # brand-level overview article.
        for slug in _candidate_slugs(hit.brand, "x"):
            if not slug.endswith("-x") and slug in corpus:
                return ("covered", slug)
        return ("content_gap", None)
    for code in hit.extracted_codes:
        for slug in _candidate_slugs(hit.brand, code):
            if slug in corpus:
                # We have an article but the Reddit thread might use a
                # different phrasing than our H2s. Flag for SERP review.
                return ("serp_gap", slug)
    return ("content_gap", None)


def annotate(
    hits: Iterable[Classified], blog_dir: Path
) -> list[dict]:
    corpus = load_corpus(blog_dir)
    out: list[dict] = []
    for h in hits:
        gap_kind, matched_slug = classify_gap(h, corpus)
        out.append({
            "post_id": h.post_id,
            "subreddit": h.subreddit,
            "title": h.title,
            "url": h.url,
            "brand": h.brand,
            "codes": ",".join(h.extracted_codes),
            "equipment_category": h.equipment_category or "",
            "urgency": h.urgency,
            "age_hours": round(h.age_hours, 1),
            "score": h.score,
            "num_comments": h.num_comments,
            "gap_kind": gap_kind,
            "matched_slug": matched_slug or "",
            "article_url": (
                f"https://errorcodefixes.com/posts/{matched_slug}/" if matched_slug else ""
            ),
            # Video Target signal — high-urgency or content-gap hits are the
            # best YouTube Shorts script candidates per council recommendation
            "video_target": (
                "yes" if (h.urgency == "high" or gap_kind == "content_gap") else "no"
            ),
        })
    return out
