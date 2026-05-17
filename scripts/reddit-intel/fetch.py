"""Reddit fetcher for the errorcodefixes.com Tier A intel engine.

LISTEN-ONLY. Does not post, comment, vote, or write to Reddit in any way.

Two transports, picked at runtime:
  1. OAuth (preferred): if REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET are set in
     env, uses Reddit's official OAuth client_credentials flow (no user auth).
     Rate limit ~600 req/10min.
  2. Public JSON (fallback): if no OAuth creds, hits the public *.json
     endpoints with a polite User-Agent and 1 req/sec self-throttle. Lower
     ceiling but no setup required.

The output is a list of normalized RedditHit dicts. Classification and sink
write are done elsewhere — this module is just transport.
"""

from __future__ import annotations

import os
import time
import json
import logging
from dataclasses import dataclass, asdict
from typing import Iterable, Iterator

import requests

LOG = logging.getLogger("reddit-intel.fetch")

UA = (
    "errorcodefixes-intel/1.0 "
    "(+https://errorcodefixes.com; contact: ops@errorcodefixes.com)"
)
OAUTH_TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
OAUTH_BASE = "https://oauth.reddit.com"
PUBLIC_BASE = "https://www.reddit.com"


@dataclass
class RedditHit:
    post_id: str          # Reddit "t3_..." id, stable
    subreddit: str
    title: str
    selftext: str
    url: str              # permalink to the Reddit thread
    author: str
    created_utc: float
    score: int
    num_comments: int
    link_flair: str | None
    matched_query: str    # which pattern surfaced it — debugging signal
    matched_brand: str    # brand substituted into the pattern


# ─────────────────────────── auth ────────────────────────────


def _oauth_token() -> str | None:
    """Fetch an OAuth app-only token. Returns None if no creds in env."""
    cid = os.environ.get("REDDIT_CLIENT_ID")
    sec = os.environ.get("REDDIT_CLIENT_SECRET")
    if not cid or not sec:
        return None
    resp = requests.post(
        OAUTH_TOKEN_URL,
        auth=(cid, sec),
        data={"grant_type": "client_credentials"},
        headers={"User-Agent": UA},
        timeout=15,
    )
    resp.raise_for_status()
    tok = resp.json().get("access_token")
    if not tok:
        raise RuntimeError(f"reddit oauth: no access_token in {resp.text!r}")
    return tok


# ───────────────────────── transport ─────────────────────────


def _search_oauth(token: str, sub: str, query: str, limit: int = 25) -> list[dict]:
    """OAuth-authenticated subreddit search."""
    url = f"{OAUTH_BASE}/r/{sub}/search"
    resp = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}", "User-Agent": UA},
        params={
            "q": query,
            "restrict_sr": "on",
            "sort": "new",
            "t": "week",
            "limit": limit,
        },
        timeout=20,
    )
    if resp.status_code == 429:
        # respect Retry-After if present, otherwise back off 30s
        wait = int(resp.headers.get("Retry-After", "30"))
        LOG.warning("oauth rate-limited; sleeping %ds", wait)
        time.sleep(wait)
        return _search_oauth(token, sub, query, limit)
    resp.raise_for_status()
    return [c["data"] for c in resp.json().get("data", {}).get("children", [])]


def _search_public(sub: str, query: str, limit: int = 25) -> list[dict]:
    """Unauthenticated public JSON search. Self-throttled to 1 req/sec."""
    url = f"{PUBLIC_BASE}/r/{sub}/search.json"
    resp = requests.get(
        url,
        headers={"User-Agent": UA},
        params={
            "q": query,
            "restrict_sr": "on",
            "sort": "new",
            "t": "week",
            "limit": limit,
            "raw_json": 1,
        },
        timeout=20,
    )
    # Reddit 429s unauth flow hard. Honor + sleep aggressively.
    if resp.status_code == 429:
        wait = int(resp.headers.get("Retry-After", "60"))
        LOG.warning("public rate-limited; sleeping %ds", wait)
        time.sleep(wait)
        return _search_public(sub, query, limit)
    if resp.status_code != 200:
        LOG.warning("public search %s/%s -> %d %s", sub, query, resp.status_code, resp.reason)
        return []
    try:
        return [c["data"] for c in resp.json().get("data", {}).get("children", [])]
    except (json.JSONDecodeError, KeyError) as e:
        LOG.warning("public search %s/%s decode err: %s", sub, query, e)
        return []


# ───────────────────────── orchestrator ──────────────────────


def search(
    subreddits: Iterable[str],
    patterns: Iterable[str],
    brands: Iterable[str],
    limit_per_query: int = 25,
    polite_delay_sec: float = 1.0,
) -> Iterator[RedditHit]:
    """Generator over RedditHits. Streams so the caller can checkpoint."""
    token = _oauth_token()
    transport = "oauth" if token else "public"
    LOG.info("reddit-intel using %s transport", transport)

    seen: set[str] = set()
    for sub in subreddits:
        for pattern in patterns:
            for brand in brands:
                q = pattern.replace("{BRAND}", brand)
                try:
                    raw = (
                        _search_oauth(token, sub, q, limit_per_query)
                        if token
                        else _search_public(sub, q, limit_per_query)
                    )
                except requests.RequestException as e:
                    LOG.warning("search %s/%s failed: %s", sub, q, e)
                    raw = []

                for item in raw:
                    pid = item.get("id", "")
                    if not pid or pid in seen:
                        continue
                    seen.add(pid)
                    yield RedditHit(
                        post_id=pid,
                        subreddit=item.get("subreddit", sub),
                        title=item.get("title", "") or "",
                        selftext=item.get("selftext", "") or "",
                        url=f"https://www.reddit.com{item.get('permalink', '')}",
                        author=item.get("author", "") or "",
                        created_utc=float(item.get("created_utc", 0) or 0),
                        score=int(item.get("score", 0) or 0),
                        num_comments=int(item.get("num_comments", 0) or 0),
                        link_flair=item.get("link_flair_text"),
                        matched_query=q,
                        matched_brand=brand,
                    )
                # polite self-throttle: even with OAuth, don't hammer
                time.sleep(polite_delay_sec)


def hits_to_records(hits: Iterable[RedditHit]) -> list[dict]:
    return [asdict(h) for h in hits]
