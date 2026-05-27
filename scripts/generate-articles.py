#!/usr/bin/env python3
"""
Demand-driven article generator.

Finds error-code topics people are actually searching/asking about that we do
NOT yet have an article for, researches each against the live web (so we never
fabricate specs on industrial equipment), writes a full guide in the house
template, and saves it to src/data/blog/. The daily content pipeline + internal
linker + auto-deploy then take it the rest of the way (pins, Shorts, links, live).

DEMAND SOURCES (most reliable first):
  A. Google Search Console  — real Google queries hitting the domain that have
     no matching article. Proven demand. Always on (we own the SA).
  B. Reddit intel gaps      — brand+code combos asked about on target subreddits
     that we don't cover (scripts/reddit-intel). Best-effort: if it can't run
     (no Reddit creds / rate limit) the generator continues on GSC alone.

GROUNDING + WRITING:
  - Perplexity (sonar) researches each code -> real causes, steps, specs, parts.
  - Claude returns the content as JSON; THIS script assembles the markdown so the
    template, tags, and Amazon affiliate links are always correct.

REQUIRES (in env):
  ANTHROPIC_API_KEY     content writer
  PERPLEXITY_API_KEY    factual grounding (optional but strongly recommended)
  GSC_SERVICE_ACCOUNT_JSON  path to gsc-sa.json (source A)

USAGE:
  python scripts/generate-articles.py --count 3
  python scripts/generate-articles.py --count 3 --dry      # pick topics, write nothing
  python scripts/generate-articles.py --topic "Lennox E110 error code"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "src" / "data" / "blog"
STATE = ROOT / "scripts" / ".generated-articles.json"
SITE = "errorcodefixes.com"

ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
PERPLEXITY_KEY = os.environ.get("PERPLEXITY_API_KEY", "")
GSC_SA = os.environ.get("GSC_SERVICE_ACCOUNT_JSON", r"C:\Users\Administrator\.claude\secrets\gsc-sa.json")

AUTHORS = ["Dana Kowalski", "Marcus Webb", "James Rutherford"]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ecf-gen/1.0"

# Error-code intent: a brand-ish token plus a code-ish token. Keeps us on the
# repair-guide topic and away from generic queries.
CODE_RE = re.compile(r"\b([a-z]{1,4}\s?-?\s?\d{1,4}[a-z]?)\b", re.I)
INTENT_RE = re.compile(r"error|code|fault|fxxx|e\d|f\d|flash|blink|lockout|alarm|trouble", re.I)


# ----------------------------------------------------------------------------- #
# Existing coverage
# ----------------------------------------------------------------------------- #
def existing_slugs() -> set[str]:
    return {p.stem for p in BLOG_DIR.glob("*.md")}


def existing_titles() -> str:
    """A compact corpus of existing titles for the LLM to dedupe against."""
    out = []
    for p in BLOG_DIR.glob("*.md"):
        out.append(p.stem)
    return "\n".join(sorted(out))


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-+", "-", s)


_STOP = {"error", "code", "codes", "fault", "fix", "causes", "cause", "meaning",
         "light", "lights", "blinking", "flashing", "the", "and", "what", "is",
         "means", "guide", "troubleshooting", "how", "to", "on", "a"}


def topic_signature(text: str) -> frozenset[str]:
    """Order-independent fingerprint of the meaningful tokens (brand words + code).
    'daikin c4 error code' and 'c4 error code daikin' map to the same signature."""
    toks = re.findall(r"[a-z0-9]+", text.lower())
    return frozenset(t for t in toks if t not in _STOP and len(t) >= 2)


def existing_signatures() -> list[frozenset[str]]:
    return [topic_signature(p.stem) for p in BLOG_DIR.glob("*.md")]


# ----------------------------------------------------------------------------- #
# Demand source A: Google Search Console
# ----------------------------------------------------------------------------- #
def gsc_demand(limit: int = 5000) -> list[dict]:
    """Real Google queries hitting the domain. Returns [{query, impressions, position}]."""
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except Exception as e:
        print(f"  [gsc] libs unavailable: {e}")
        return []
    if not Path(GSC_SA).exists():
        print(f"  [gsc] SA missing: {GSC_SA}")
        return []
    try:
        creds = service_account.Credentials.from_service_account_file(
            GSC_SA, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
        svc = build("searchconsole", "v1", credentials=creds)
        from datetime import timedelta
        end = date.today() - timedelta(days=2)
        start = end - timedelta(days=120)
        rows = svc.searchanalytics().query(siteUrl=f"https://{SITE}/", body={
            "startDate": str(start), "endDate": str(end),
            "dimensions": ["query"], "rowLimit": limit,
        }).execute().get("rows", [])
        return [{"query": r["keys"][0], "impressions": r.get("impressions", 0),
                 "position": r.get("position", 99)} for r in rows]
    except Exception as e:
        print(f"  [gsc] query failed: {e}")
        return []


def bing_demand() -> list[dict]:
    """Real Bing search queries for the site (GetQueryStats). Best-effort."""
    key = os.environ.get("BING_API_KEY", "")
    if not key:
        return []
    import urllib.parse
    site = urllib.parse.quote("https://errorcodefixes.com/", safe="")
    url = (f"https://ssl.bing.com/webmaster/api.svc/json/GetQueryStats"
           f"?siteUrl={site}&apikey={key}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.load(r).get("d", []) or []
        out = []
        for row in data:
            q = row.get("Query") or row.get("query")
            if q:
                out.append({"query": q, "impressions": row.get("Impressions", 1), "position": 99})
        return out
    except Exception as e:
        print(f"  [bing] {e}")
        return []


# ----------------------------------------------------------------------------- #
# Demand source B: Reddit intel gaps (best-effort)
# ----------------------------------------------------------------------------- #
def coverage_expansion() -> list[dict]:
    """Renewable, high-confidence demand: find numeric code SERIES we already
    cover and fill the interior gaps. If we have weil-mclain E01/E02/E04/E05 but
    not E03, that missing code is almost certainly real and definitely searched.
    Only fills gaps strictly BETWEEN the min and max we already have, so we never
    invent codes past the end of a series. Perplexity grounding + the quality gate
    still reject anything that turns out not to exist."""
    import collections
    groups: dict[tuple, dict] = collections.defaultdict(dict)
    pat = re.compile(r"^(.*?)(\d+)(\D*)$")
    for p in BLOG_DIR.glob("*.md"):
        m = pat.match(p.stem)
        if not m:
            continue
        prefix, num, suffix = m.group(1), m.group(2), m.group(3)
        key = (prefix, suffix, len(num))
        groups[key][int(num)] = p.stem
    out = []
    for (prefix, suffix, width), nums in groups.items():
        if len(nums) < 3:           # need a real series to interpolate safely
            continue
        lo, hi = min(nums), max(nums)
        if hi - lo > 60:            # avoid absurd ranges from coincidental matches
            continue
        for n in range(lo + 1, hi):
            if n in nums:
                continue
            slug = f"{prefix}{n:0{width}d}{suffix}"
            topic = slug.replace("-", " ").strip()
            out.append({"query": topic, "impressions": 2, "position": 99})
    return out


def code_pool_demand() -> list[dict]:
    """Real documented codes mined from manufacturer docs by mine-code-lists.py.
    This is the renewable feeder that sustains the paced ramp without inventing
    codes. Ranked above interior-gap expansion (these are explicitly documented)
    but below live GSC/Reddit search demand."""
    p = ROOT / "scripts" / ".code-pool.json"
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text())
    except Exception:
        return []
    return [{"query": c, "impressions": 4, "position": 99} for c in data.get("candidates", [])]


def reddit_demand() -> list[dict]:
    """Best-effort: read reddit-intel gap output if present. Never fatal."""
    candidates = list((ROOT / "scripts" / "reddit-intel").glob("*gap*.json"))
    candidates += list((ROOT / "scripts" / "reddit-intel" / "out").glob("*.json")) if (ROOT / "scripts" / "reddit-intel" / "out").exists() else []
    topics = []
    for c in candidates:
        try:
            data = json.loads(c.read_text(encoding="utf-8"))
            rows = data if isinstance(data, list) else data.get("content_gaps", []) or data.get("gaps", [])
            for r in rows:
                t = r.get("topic") or f"{r.get('brand','')} {r.get('code','')}".strip()
                if t:
                    topics.append({"query": t, "impressions": int(r.get("mentions", 1)) * 5, "position": 99})
        except Exception:
            continue
    return topics


# ----------------------------------------------------------------------------- #
# Topic selection
# ----------------------------------------------------------------------------- #
def pick_topics(count: int, have: set[str]) -> list[str]:
    pool = (gsc_demand() + bing_demand() + reddit_demand()
            + code_pool_demand() + coverage_expansion())
    have_sigs = existing_signatures()
    seen, picks = [], []
    scored = sorted(pool, key=lambda r: -float(r.get("impressions", 0)))
    for r in scored:
        q = re.sub(r'["\']', "", r["query"]).strip()
        q = re.sub(r"\s+", " ", q)
        if not INTENT_RE.search(q) or not CODE_RE.search(q):
            continue
        sig = topic_signature(q)
        if len(sig) < 2:  # need at least a brand-ish token + a code-ish token
            continue
        # Covered only if an existing article is at least as specific as this
        # query (candidate tokens are a subset of an existing article's tokens).
        # We do NOT skip when the candidate is a SUPERSET of some short existing
        # signature -- "york chiller e1" is a distinct, more-specific topic than
        # an existing "york chiller" guide and should still be written.
        if any(sig <= es for es in have_sigs):
            continue
        if any(sig <= s or s <= sig for s in seen):  # dedupe within this batch
            continue
        seen.append(sig)
        picks.append(q)
        if len(picks) >= count:
            break
    return picks


# ----------------------------------------------------------------------------- #
# Research + write
# ----------------------------------------------------------------------------- #
def perplexity_research(topic: str) -> str:
    if not PERPLEXITY_KEY:
        return ""
    body = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are an industrial/HVAC service research assistant. "
             "Give only verified, manufacturer-grounded facts. If a spec or part number is uncertain, "
             "say so rather than guessing."},
            {"role": "user", "content":
             f"Research the '{topic}'. Report: (1) exactly what this code/fault means, "
             f"(2) the real common causes, (3) the correct diagnostic + repair steps a technician follows, "
             f"(4) any concrete specs (resistance, voltage, pressure) only if you are confident, "
             f"(5) the specific replacement parts/components involved. Cite manufacturers where possible."},
        ],
        "max_tokens": 900,
    }
    try:
        req = urllib.request.Request("https://api.perplexity.ai/chat/completions",
            data=json.dumps(body).encode(), method="POST",
            headers={"Authorization": f"Bearer {PERPLEXITY_KEY}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"    [perplexity] {e}")
        return ""


def claude_write(topic: str, research: str) -> dict | None:
    if not ANTHROPIC_KEY:
        print("    [claude] ANTHROPIC_API_KEY not set"); return None
    schema = (
        '{"title": "<Brand Code Error Code — Causes & Fix, <=70 chars>",'
        ' "description": "<meta description, 120-155 chars>",'
        ' "equipment_category": "<one of: hvac, boiler, refrigeration, cnc, vfd, appliance, water-heater, generator, other>",'
        ' "brand_slug": "<lowercase-hyphenated brand, e.g. weil-mclain>",'
        ' "what_it_means": "<1-2 paragraph plain-English explanation of the code>",'
        ' "causes": [{"lead": "<short bold lead-in>", "text": "<one sentence>"}],'
        ' "steps": ["<imperative step with a bolded first phrase>", "..."],'
        ' "parts": [{"name": "<part name a buyer would search>", "note": "<short selection note>"}],'
        ' "when_to_call_pro": "<1 paragraph>"}'
    )
    rules = (
        "STYLE RULES (hard): no em dashes anywhere; no semicolons; do not use the words "
        "ensure, crucial, vital, leverage, robust, seamless. Write like a working technician, "
        "concrete and calm. Only state specific numeric specs or part numbers that appear in the "
        "research below; if the research does not give a number, stay general (say 'consult your "
        "model's table') rather than inventing one. 4-6 causes, 5-7 steps, 2-4 parts."
    )
    prompt = (
        f"Write a repair guide for: \"{topic}\".\n\n"
        f"RESEARCH (ground every factual claim in this; do not contradict it):\n{research or '(no external research available — stay general and safe, avoid invented specs)'}\n\n"
        f"{rules}\n\n"
        f"Return ONLY a single JSON object, no prose, matching exactly this shape:\n{schema}"
    )
    body = {
        "model": "claude-sonnet-4-5-20250929",
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": prompt}],
    }
    try:
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
            data=json.dumps(body).encode(), method="POST",
            headers={"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01",
                     "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
        text = "".join(b.get("text", "") for b in d.get("content", []))
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if not m:
            print("    [claude] no JSON in response"); return None
        return json.loads(m.group(0))
    except urllib.error.HTTPError as e:
        print(f"    [claude] HTTP {e.code}: {e.read().decode()[:200]}"); return None
    except Exception as e:
        print(f"    [claude] {e}"); return None


def claude_review(topic: str, content: dict, research: str) -> dict:
    """Second-pass quality gate. Scores the draft and decides publish vs hold.
    Especially guards against coverage-expansion codes that don't actually exist."""
    if not ANTHROPIC_KEY:
        return {"score": 0, "publish": False, "reason": "no API key"}
    draft_json = json.dumps(content)[:6000]
    prompt = (
        f"You are a strict technical editor for an industrial/HVAC error-code repair site. "
        f"Evaluate this draft for the topic \"{topic}\".\n\n"
        f"RESEARCH USED:\n{research[:3000] or '(none — no external grounding was available)'}\n\n"
        f"DRAFT (JSON):\n{draft_json}\n\n"
        f"Judge on: (1) is this a REAL, documented error code/fault for this equipment "
        f"(if the research does not confirm the code exists, this fails); (2) technical "
        f"accuracy vs the research; (3) specificity and usefulness (not vague filler); "
        f"(4) appropriate safety guidance. "
        f"Return ONLY JSON: {{\"score\": <0-10>, \"publish\": <true/false>, \"reason\": \"<one line>\"}}. "
        f"Publish true only if it is a real code AND accurate AND specific (score >= 7)."
    )
    body = {"model": "claude-sonnet-4-5-20250929", "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}]}
    try:
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
            data=json.dumps(body).encode(), method="POST",
            headers={"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01",
                     "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
        text = "".join(b.get("text", "") for b in d.get("content", []))
        m = re.search(r"\{.*\}", text, re.DOTALL)
        return json.loads(m.group(0)) if m else {"score": 0, "publish": False, "reason": "unparseable"}
    except Exception as e:
        return {"score": 0, "publish": False, "reason": f"review error: {e}"}


BANNED = re.compile(r"\b(ensure|crucial|vital|leverage|robust|seamless)\b", re.I)


def assemble_md(topic: str, c: dict, slug: str, draft: bool = False) -> str:
    title = c["title"].replace("—", "-").strip()
    desc = c["description"].replace("—", "-").strip()
    author = AUTHORS[abs(hash(slug)) % len(AUTHORS)]
    cat = c.get("equipment_category", "other")
    brand = c.get("brand_slug", "").strip()
    tags = [t for t in [cat if cat != "other" else None, brand or None] if t]
    # Backdate pubDatetime by 2 days. postFilter.ts drops posts whose pubDatetime
    # is in the future; this host has a clock/timezone skew, so a "now" stamp can
    # look future-dated at build and get filtered out. 48h past is bulletproof and
    # still recent enough for freshness signals.
    from datetime import timedelta
    pub = (datetime.now(timezone.utc) - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    now = pub

    def amazon(name: str) -> str:
        import urllib.parse
        k = urllib.parse.quote_plus(name)
        return (f"[Amazon](https://www.amazon.com/s?ascsubtag=ecf-{slug}"
                f"&k={k}&tag=errorcodefixes-20)")

    parts = c.get("parts", []) or []
    parts_rows = "\n".join(
        f"| {p['name']} | {amazon(p['name'])} \\| {p.get('note','verify fitment for your model')} |"
        for p in parts
    ) or "| Replacement component | " + amazon(title) + " \\| verify fitment for your exact model |"

    causes = "\n".join(f"- **{x['lead']}** {x['text']}" for x in c.get("causes", []))
    steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(c.get("steps", [])))

    md = f"""---
title: "{title}"
description: "{desc}"
pubDatetime: {now}
modDatetime: {now}
author: "{author}"
featured: false
draft: {str(draft).lower()}
tags:
{chr(10).join(f"  - {t}" for t in tags) if tags else "  - error-code"}
---

## {title.split(' — ')[0].split(' - ')[0]} — What It Means

{c['what_it_means']}

[Jump to Fix](#fix)

## Common Causes

{causes}

## Step-by-Step Fix {{#fix}}

{steps}

## Parts Often Needed

| Part | Notes |
|------|-------|
{parts_rows}

## When to Call a Pro

{c['when_to_call_pro']}
"""
    return md


def generate_one(topic: str, have: set[str], dry: bool) -> str | None:
    slug = slugify(topic)
    if slug in have:
        print(f"  [skip] already have {slug}")
        return None
    print(f"  -> {topic}  (slug: {slug})")
    if dry:
        return slug
    research = perplexity_research(topic)
    print(f"     research: {len(research)} chars")
    content = claude_write(topic, research)
    if not content:
        print("     [!] generation failed"); return None
    # Quality gate: score the draft. Weak/unverifiable codes ship as draft:true
    # (saved for human review, NOT built/published) instead of going live.
    verdict = claude_review(topic, content, research)
    publish = bool(verdict.get("publish")) and int(verdict.get("score", 0)) >= 7
    print(f"     review: score={verdict.get('score')} publish={publish} — {verdict.get('reason','')[:80]}")
    md = assemble_md(topic, content, slug, draft=not publish)
    if BANNED.search(md):
        md = BANNED.sub(lambda m: {"ensure": "make sure", "crucial": "important",
                                   "vital": "important", "leverage": "use",
                                   "robust": "reliable", "seamless": "smooth"}.get(m.group(0).lower(), m.group(0)), md)
    (BLOG_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
    if publish:
        print(f"     [+] PUBLISHED src/data/blog/{slug}.md")
    else:
        # log to a review queue so held drafts are easy to find
        rq_path = ROOT / "scripts" / ".article-review-queue.json"
        rq = json.loads(rq_path.read_text()) if rq_path.exists() else {}
        rq[slug] = {"topic": topic, "score": verdict.get("score"),
                    "reason": verdict.get("reason"), "date": date.today().isoformat()}
        rq_path.write_text(json.dumps(rq, indent=2))
        print(f"     [~] HELD as draft (review queue): {slug}")
    return slug


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=3)
    ap.add_argument("--topic", help="generate one explicit topic, skip demand mining")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    have = existing_slugs()
    state = json.loads(STATE.read_text()) if STATE.exists() else {"generated": {}}

    if args.topic:
        topics = [args.topic]
    else:
        print("[i] mining demand (GSC + Reddit gaps)...")
        topics = pick_topics(args.count, have)
    if not topics:
        print("[i] no new in-demand topics found (we may already cover the top gaps).")
        return 0

    print(f"[i] {len(topics)} topic(s) selected")
    written = []
    for t in topics:
        slug = generate_one(t, have, args.dry)
        if slug and not args.dry:
            have.add(slug)
            state["generated"][slug] = {"topic": t, "date": date.today().isoformat()}
            written.append(slug)

    if written:
        STATE.write_text(json.dumps(state, indent=2))
    print(f"\n[+] {'(dry) ' if args.dry else ''}{len(written) if not args.dry else len(topics)} article(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
