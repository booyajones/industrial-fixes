"""Firecrawl-backed Reddit search transport.

Reddit aggressively 403s unauthenticated requests from datacenter IP ranges
(GitHub Actions, AWS, GCP, Azure). The canary on 2026-05-17 hit this wall
hard — every public-JSON request from the GHA runner came back 403 Blocked.
Council's exact blind-spot prediction.

Firecrawl's /v1/search endpoint hits Google with rotating residential
IPs, indexes Reddit results natively, and returns title + URL + snippet
in a single call. Two key wins:

1. One broad search per (sub, pattern_keyword) replaces N per-brand
   searches: 13 subs × 3 patterns = 39 calls instead of 13 × 40 × 3 = 1,560.
   Brand extraction happens post-hoc in classify.py from the result text,
   which is MORE accurate than self-fulfilling brand-substitution searches.

2. Bypasses Reddit's anti-datacenter blocks without needing a Reddit OAuth
   app (which would require a Reddit user account this pipeline doesn't have).

LISTEN-ONLY. Same contract as fetch.py.
"""

from __future__ import annotations

import os
import re
import time
import logging
from typing import Iterable, Iterator

import requests

from fetch import RedditHit  # reuse dataclass

LOG = logging.getLogger("reddit-intel.fetch_firecrawl")

FIRECRAWL_SEARCH_URL = "https://api.firecrawl.dev/v1/search"

# Reddit thread URL → post_id (e.g. .../comments/1h4jil7/title/ → "1h4jil7")
_POST_ID_RE = re.compile(r"/comments/([a-z0-9]+)/")


def _extract_post_id(url: str) -> str | None:
    m = _POST_ID_RE.search(url)
    return m.group(1) if m else None


def _extract_brand(text: str, brands: list[str]) -> str:
    """Pick the first brand mentioned in the title/description. Case-insensitive,
    word-boundary match so "True" doesn't match "truely" but DOES match
    "True T-49"."""
    lower = text.lower()
    # Sort by length descending so "Beverage-Air" wins over "Air"
    for brand in sorted(brands, key=len, reverse=True):
        b = brand.lower()
        # Use word boundary on the brand name itself
        if re.search(rf"\b{re.escape(b)}\b", lower):
            return brand
    return ""


def search(
    subreddits: Iterable[str],
    pattern_keywords: Iterable[str],
    brands: list[str],
    limit_per_query: int = 25,
    polite_delay_sec: float = 0.5,
) -> Iterator[RedditHit]:
    """One Firecrawl search per (subreddit, pattern_keyword) pair.

    `pattern_keywords` are the verb/noun roots ("error", "fault",
    "flashing") — we do NOT iterate per-brand. Brand detection is post-hoc
    from the returned text.
    """
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        raise RuntimeError("FIRECRAWL_API_KEY not set — Firecrawl transport unavailable")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    seen: set[str] = set()

    for sub in subreddits:
        for kw in pattern_keywords:
            query = f'site:reddit.com/r/{sub} "{kw}" code'
            try:
                resp = requests.post(
                    FIRECRAWL_SEARCH_URL,
                    headers=headers,
                    json={"query": query, "limit": limit_per_query, "tbs": "qdr:w"},
                    timeout=30,
                )
                if resp.status_code != 200:
                    LOG.warning("firecrawl %s/%s -> %d %s",
                                sub, kw, resp.status_code, resp.text[:200])
                    continue
                # /v1/search returns {"success": true, "data": [...]}; older
                # MCP wrapper returns {"data": {"web": [...]}}. Handle both.
                body = resp.json().get("data") or []
                if isinstance(body, dict):
                    results = body.get("web") or []
                else:
                    results = body
            except requests.RequestException as e:
                LOG.warning("firecrawl %s/%s failed: %s", sub, kw, e)
                results = []

            for item in results:
                url = item.get("url", "")
                pid = _extract_post_id(url)
                if not pid or pid in seen or "/comments/" not in url:
                    continue
                seen.add(pid)
                title = item.get("title", "") or ""
                desc = item.get("description", "") or ""
                brand = _extract_brand(f"{title} {desc}", brands)
                yield RedditHit(
                    post_id=pid,
                    subreddit=sub,
                    title=title,
                    selftext=desc,  # description is the SERP snippet; close enough
                    url=url,
                    author="",  # firecrawl SERP doesn't include author
                    # Firecrawl SERP doesn't return created_utc — use "now" as
                    # ceiling so tbs=qdr:w filtering keeps us in-window.
                    created_utc=time.time(),
                    score=0,
                    num_comments=0,
                    link_flair=None,
                    matched_query=query,
                    matched_brand=brand,
                )
            time.sleep(polite_delay_sec)
