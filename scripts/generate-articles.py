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
import random
import re
import sys
import time
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

AUTHORS = ["Error Code Fixes Editorial Team"]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ecf-gen/1.0"

# Error-code intent: a brand-ish token plus a code-ish token. Keeps us on the
# repair-guide topic and away from generic queries.
CODE_RE = re.compile(r"\b([a-z]{1,4}\s?-?\s?\d{1,4}[a-z]?)\b", re.I)
INTENT_RE = re.compile(r"error|code|fault|fxxx|e\d|f\d|flash|blink|lockout|alarm|trouble", re.I)


def _post_json(url: str, headers: dict, payload: dict, timeout: int, retries: int = 9) -> dict:
    """POST JSON with exponential backoff on rate-limit (429), overload (529),
    and transient 5xx/network errors. Raises the last error if all retries fail.
    This is what lets the parallel batch runner use real concurrency without
    losing articles to momentary 'concurrent connections exceeded' 429s."""
    data = json.dumps(payload).encode()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="POST", headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 529):
                if attempt < retries - 1:  # don't sleep after the final attempt
                    time.sleep(min(2 ** attempt + random.random(), 45))
                continue
            raise
        except Exception as e:  # timeouts, connection resets
            last_err = e
            if attempt < retries - 1:
                time.sleep(min(2 ** attempt + random.random(), 45))
            continue
    raise last_err if last_err else RuntimeError("post failed")


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
        d = _post_json("https://api.perplexity.ai/chat/completions",
            {"Authorization": f"Bearer {PERPLEXITY_KEY}", "Content-Type": "application/json"},
            body, 60)
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"    [perplexity] {e}")
        return ""


def claude_write(topic: str, research: str) -> dict | None:
    if not ANTHROPIC_KEY:
        print("    [claude] ANTHROPIC_API_KEY not set"); return None
    schema = (
        '{"title": "<Brand Code Error Code — Causes & Fix, <=70 chars>",'
        ' "description": "<meta description, answer-first TL;DR, 120-155 chars>",'
        ' "equipment_category": "<one of: hvac, boiler, refrigeration, cnc, vfd, appliance, water-heater, generator, other>",'
        ' "brand_slug": "<lowercase-hyphenated brand, e.g. weil-mclain>",'
        ' "what_it_means": "<1-2 paragraph plain-English explanation of the code>",'
        ' "most_likely_cause": "<the single most common cause of THIS code on THIS appliance, a short noun phrase, only if the research supports one; else empty string>",'
        ' "likelihood": "<plain qualitative phrase for how often that cause applies, e.g. the most common cause or often; NEVER a made-up percentage; empty string if unsure>",'
        ' "diy_or_pro": "<diy if a typical homeowner can fix it with basic hand tools and a part, or pro if it needs gas, refrigerant, sealed-system, compressor, or high-voltage work>",'
        ' "misdiagnosis_warning": "<1-2 sentences naming the part people wrongly replace first and the cheap test to do instead; empty string if none>",'
        ' "cost_diy": "<rough DIY cost and time as a general range, e.g. $20-60 in parts, 30-60 min; empty string if unknown>",'
        ' "cost_pro": "<rough pro service cost as a general range, e.g. $150-300; empty string if unknown>",'
        ' "causes": [{"lead": "<short bold lead-in>", "text": "<one sentence>", "share": <integer 0-100: rough share of how often this is the actual cause>}],'
        ' "decision_tree": [{"question": "<a yes/no check a homeowner can actually do>", "if_yes": "<what it means and what to do next>", "if_no": "<what it means and what to do next>"}],'
        ' "steps": ["<imperative step with a bolded first phrase>", "..."],'
        ' "parts": [{"name": "<part name a buyer would search>", "note": "<short selection note>"}],'
        ' "when_to_call_pro": "<1 paragraph>"}'
    )
    rules = (
        "STYLE RULES (hard): no em dashes anywhere; no semicolons; do not use the words "
        "ensure, crucial, vital, leverage, robust, seamless. Write like a working technician, "
        "concrete and calm. Only state specific numeric specs or part numbers that appear in the "
        "research below; if the research does not give a number, stay general (say 'consult your "
        "model's table') rather than inventing one. 4-6 causes, 5-7 steps, 2-4 parts. "
        "The description field must be an ANSWER-FIRST TL;DR a homeowner can act on: state what "
        "the code means and the single most likely fix in plain words, 120-155 chars. For "
        "residential kitchen and laundry appliances (washer, dryer, dishwasher, refrigerator, "
        "range, oven, cooktop, microwave) set equipment_category to \"appliance\". "
        "ACCURACY (critical): only state the specific meaning of this code if the RESEARCH clearly "
        "documents it for THIS exact brand AND this exact appliance. If the research is thin, "
        "ambiguous, about a different brand, or about a different appliance, do NOT invent a meaning "
        "and do NOT borrow another brand's meaning for the same code letters. A code can be real for "
        "one brand or appliance and mean something different (or not exist) on another. When unsure, "
        "say the exact meaning varies by model and to check the owner's manual or wiring diagram, and "
        "keep causes general rather than asserting a specific wrong cause. "
        "DIAGNOSTIC DEPTH: set diy_or_pro to \"pro\" whenever the real fix involves gas, "
        "refrigerant, a sealed system, the compressor, or high-voltage work, and \"diy\" when a "
        "homeowner can swap a sensor, switch, pump, valve, belt, filter, door lock, igniter, or "
        "control board with basic tools. most_likely_cause and likelihood must come from the "
        "research; never invent a percentage (use words like \"the most common cause\" or \"often\"). "
        "Give 2-3 decision_tree checks a homeowner can actually perform (for example \"Does the drum "
        "spin freely by hand?\"), each with a clear if_yes and if_no. cost_diy and cost_pro are rough "
        "GENERAL ranges; leave them empty if the research gives no basis. misdiagnosis_warning names "
        "the expensive part people replace by mistake and the cheap test that finds the real cause. "
        "RANKED CAUSES: order causes most likely first and give each a rough share (integer percent) "
        "of how often it is the actual cause; the shares should sum to about 100. Shares are field-"
        "frequency estimates from typical repair experience, not guarantees and not invented numeric specs."
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
        d = _post_json("https://api.anthropic.com/v1/messages",
            {"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01",
             "Content-Type": "application/json"}, body, 120)
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
        f"Judge on: (1) is this code REAL and documented for THIS EXACT brand AND appliance "
        f"(not a different brand's or a different appliance's code) - if the research does not "
        f"confirm it for this brand+appliance, FAIL; (2) is the stated MEANING/cause correct vs "
        f"the research and not borrowed from another brand - if the meaning is contradicted or "
        f"invented, FAIL; (3) specificity and usefulness (not vague filler); "
        f"(4) appropriate safety guidance. "
        f"Return ONLY JSON: {{\"score\": <0-10>, \"publish\": <true/false>, \"reason\": \"<one line>\"}}. "
        f"Publish true only if it is a real code AND accurate AND specific (score >= 7)."
    )
    body = {"model": "claude-sonnet-4-5-20250929", "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}]}
    try:
        d = _post_json("https://api.anthropic.com/v1/messages",
            {"x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01",
             "Content-Type": "application/json"}, body, 60)
        text = "".join(b.get("text", "") for b in d.get("content", []))
        m = re.search(r"\{.*\}", text, re.DOTALL)
        return json.loads(m.group(0)) if m else {"score": 0, "publish": False, "reason": "unparseable"}
    except Exception as e:
        return {"score": 0, "publish": False, "reason": f"review error: {e}"}


BANNED = re.compile(r"\b(ensure|crucial|vital|leverage|robust|seamless)\b", re.I)


def assemble_md(topic: str, c: dict, slug: str, draft: bool = False) -> str:
    title = c["title"].replace("—", "-").replace('"', '\\"').strip()
    desc = c["description"].replace("—", "-").replace('"', '\\"').strip()
    author = AUTHORS[abs(hash(slug)) % len(AUTHORS)]
    cat = c.get("equipment_category", "other")
    brand = c.get("brand_slug", "").strip()
    # Derive a precise equipment tag from the topic so triage difficulty and the
    # parts-specialist routing are correct (washer/dryer/.../furnace/water-heater).
    equip_tag = None
    tl = topic.lower()
    for pat, tag in (
        (r"\bdryer\b", "dryer"), (r"washing machine|\bwasher", "washer"),
        (r"\bdishwasher", "dishwasher"), (r"refrigerator|\bfridge|freezer", "refrigerator"),
        (r"microwave", "microwave"), (r"\b(range|oven|stove|cooktop)\b", "oven"),
        (r"\bfurnace", "furnace"), (r"mini.?split|heat pump", "mini-split"),
        (r"tankless|water heater", "water-heater"),
    ):
        if re.search(pat, tl):
            equip_tag = tag
            break
    tags = []
    for t in [cat if cat != "other" else None, equip_tag, brand or None]:
        if t and t not in tags:
            tags.append(t)
    # Gas combustion safety: if the topic involves gas, force a "gas" tag so triage
    # escalates to "Pro recommended" (PRO_TAGS includes "gas"), regardless of the
    # appliance DIY mapping. Gas valve/igniter/burner work is not a DIY default.
    if re.search(r"\bgas\b", tl) and "gas" not in tags:
        tags.append("gas")
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

    def _share_int(x):
        try:
            return int(float(x.get("share")))
        except (TypeError, ValueError):
            return 0

    def _cause_line(x):
        lead = str(x.get("lead", "") or "").strip()
        text = str(x.get("text", "") or "").strip()
        sh = _share_int(x)
        pct = f" (~{sh}%)" if sh else ""
        if not lead:
            return f"- {text}" if text else ""
        return f"- **{lead}{pct}** {text}".rstrip()

    _causes = sorted(c.get("causes", []) or [], key=_share_int, reverse=True)
    causes = "\n".join(filter(None, (_cause_line(x) for x in _causes)))
    steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(c.get("steps", [])))

    # ---- Diagnosis Command Center depth (all optional, backward compatible) ----
    def _clean(v):
        # Collapse newlines too: an embedded \n in a frontmatter value would write
        # invalid YAML and break the Astro content parse for the whole build.
        return (str(v or "").replace('"', "'").replace("—", "-")
                .replace("\n", " ").replace("\r", " ").strip())

    mlc = _clean(c.get("most_likely_cause"))
    likelihood = _clean(c.get("likelihood"))
    diy_or_pro = _clean(c.get("diy_or_pro")).lower()
    misdiag = _clean(c.get("misdiagnosis_warning"))
    cost_diy = _clean(c.get("cost_diy"))
    cost_pro = _clean(c.get("cost_pro"))
    tree = c.get("decision_tree", []) or []

    # Frontmatter the template reads to render the verdict block + DIY/Pro badge.
    extra_fm = ""
    if mlc:
        extra_fm += f'most_likely_cause: "{mlc}"\n'
    if likelihood:
        extra_fm += f'likelihood: "{likelihood}"\n'
    if diy_or_pro in ("diy", "pro"):
        extra_fm += f'diy_or_pro: "{diy_or_pro}"\n'

    # Misdiagnosis callout: the costly part people wrongly replace first.
    misdiag_block = f"\n## Before You Replace Anything\n\n{misdiag}\n" if misdiag else ""

    # Quick-diagnosis decision tree as raw HTML. Body is a <div> (not <p>) so the
    # typography rule that hides <p> inside <details> does not blank it out.
    tree_block = ""
    rows = []
    for q in tree:
        qq = _clean(q.get("question"))
        qy = _clean(q.get("if_yes"))
        qn = _clean(q.get("if_no"))
        if qq and (qy or qn):
            rows.append(
                f'<details class="dtree"><summary>{qq}</summary>\n'
                f'<div class="dtree-body"><strong>Yes:</strong> {qy}<br><strong>No:</strong> {qn}</div>\n'
                f'</details>'
            )
    if rows:
        tree_block = "\n## Quick Diagnosis\n\nAnswer these to narrow it down fast.\n\n" + "\n\n".join(rows) + "\n"

    # Honest cost framing appended to the pro section.
    cost_line = ""
    if cost_diy or cost_pro:
        bits = []
        if cost_diy:
            bits.append(f"DIY runs about {cost_diy}")
        if cost_pro:
            bits.append(f"A pro service call runs about {cost_pro}")
        cost_line = "\n\n**Rough cost:** " + ". ".join(bits) + "."

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
{extra_fm}---

## {title.split(' — ')[0].split(' - ')[0]} — What It Means

{c['what_it_means']}
{misdiag_block}
[Jump to Fix](#fix)

## Common Causes

{causes}
{tree_block}
## Step-by-Step Fix {{#fix}}

{steps}

## Parts Often Needed

| Part | Notes |
|------|-------|
{parts_rows}

## When to Call a Pro

{c['when_to_call_pro']}{cost_line}
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
    publish = bool(verdict.get("publish")) and int(verdict.get("score") or 0) >= 7
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
