#!/usr/bin/env python3
"""AI-citation proxy — does errorcodefixes.com get cited by AI answer engines?

The site's core thesis is winning AI-answer citations, not just blue links. This
measures it directly + cheaply: ask a basket of real error-code questions to
Perplexity (whose API returns the actual source URLs it cited) and check whether
errorcodefixes.com appears — and which competitors (RepairClinic, etc.) win when
we don't. Uses PERPLEXITY_API_KEY already in the master .env. ~$0.01/query.

This is a PROXY for Google AI Overviews / ChatGPT-search (which aren't cleanly
API-measurable). Perplexity is web-grounded with explicit citations, so it's the
best available read on "are we in the AI answer set for these queries."

Usage:
  python scripts/ecf-ai-citation.py            # full basket
  python scripts/ecf-ai-citation.py --n 5      # quick smoke test
  python scripts/ecf-ai-citation.py --json
"""
from __future__ import annotations
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATHS = [ROOT / ".env", Path("C:/Users/chris/OneDrive/Desktop/Claude/.env")]
SNAPSHOT = ROOT / ".planning" / "ai-citation-history.jsonl"
OUR_DOMAIN = "errorcodefixes.com"
COMPETITORS = ["repairclinic.com", "appliancepartspros.com", "partselect.com",
               "partstown.com", "justanswer.com", "manualslib.com", "fixya.com",
               "youtube.com", "reddit.com", "ifixit.com"]

# Representative queries — a mix of CONSUMER (the no-buy investment) and INDUSTRIAL
# (where real traffic is today), phrased the way a person actually asks an AI.
QUERIES = [
    "Samsung dishwasher 3C error code meaning and fix",
    "LG washer OE error code how to fix",
    "Whirlpool washer F21 error code",
    "Bosch dishwasher E15 error",
    "GE dishwasher C1 error code",
    "Frigidaire dryer not heating error code",
    "Maytag dishwasher E1 error code fix",
    "Samsung refrigerator 22 E error code",
    "Whirlpool oven F2 error code",
    "LG refrigerator error code chart",
    # industrial / commercial (where the site already ranks)
    "ABB ACS880 fault code F0001",
    "ABB ACS580 fault codes list",
    "Vacon VFD fault codes",
    "Daikin VRV error codes list",
    "Doosan CNC fault codes",
    "APC UPS error codes",
    "Trane chiller fault codes",
    "Hoshizaki ice machine E7 error",
    "Mitsubishi mini split P8 error code",
    "Rational iCombi service 20.1 error",
]


def load_env():
    env = {}
    for p in ENV_PATHS:
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env.setdefault(k, v.strip().strip('"').strip("'"))
    return env


def ask_perplexity(key, query):
    """Return (answer_text, [citation_urls]) or (None, error)."""
    body = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "Answer concisely with sources. The user is troubleshooting an appliance/equipment error code."},
            {"role": "user", "content": query},
        ],
        "max_tokens": 400,
    }
    req = urllib.request.Request("https://api.perplexity.ai/chat/completions",
                                 data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode()[:150]}"
    except Exception as e:
        return None, str(e)[:150]
    text = (r.get("choices", [{}])[0].get("message", {}) or {}).get("content", "")
    # citations live at top level (search_results / citations depending on API version)
    cites = r.get("citations") or []
    if not cites:
        cites = [s.get("url", "") for s in r.get("search_results", []) if isinstance(s, dict)]
    # also catch domains mentioned inline in the answer text
    return text, [c for c in cites if c]


def domain_in(urls, text, domain):
    if any(domain in (u or "") for u in urls):
        return True
    return domain in (text or "")


def main():
    args = sys.argv[1:]
    n = int(args[args.index("--n") + 1]) if "--n" in args else len(QUERIES)
    env = load_env()
    key = env.get("PERPLEXITY_API_KEY", "")
    if not key:
        print("PERPLEXITY_API_KEY not set in .env"); return 2
    queries = QUERIES[:n]
    results = []
    our_hits = 0
    comp_tally = {c: 0 for c in COMPETITORS}
    for i, q in enumerate(queries, 1):
        text, cites = ask_perplexity(key, q)
        if text is None:
            print(f"[{i}/{len(queries)}] ERR {q[:40]}: {cites}")
            continue
        we = domain_in(cites, text, OUR_DOMAIN)
        comps = [c for c in COMPETITORS if domain_in(cites, text, c)]
        for c in comps:
            comp_tally[c] += 1
        our_hits += 1 if we else 0
        results.append({"query": q, "cited": we, "competitors": comps, "n_sources": len(cites)})
        mark = "✅ CITED" if we else "—"
        print(f"[{i}/{len(queries)}] {mark:8} {q[:46]:46} comps: {', '.join(c.split('.')[0] for c in comps[:4]) or 'none'}")
    rate = round(our_hits / max(1, len(results)) * 100, 1)
    print(f"\n{'='*60}")
    print(f"  errorcodefixes.com cited in {our_hits}/{len(results)} AI answers ({rate}%)")
    top_comp = sorted(comp_tally.items(), key=lambda kv: -kv[1])
    print("  Who wins the citations: " + ", ".join(f"{c.split('.')[0]}={n}" for c, n in top_comp if n) or "  (none of the tracked competitors cited)")
    if "--json" in args:
        SNAPSHOT.parent.mkdir(exist_ok=True)
        import datetime
        with open(SNAPSHOT, "a", encoding="utf-8") as f:
            f.write(json.dumps({"date": datetime.date.today().isoformat(),
                                "queries": len(results), "cited": our_hits, "rate_pct": rate,
                                "competitor_tally": comp_tally}) + "\n")
        print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
