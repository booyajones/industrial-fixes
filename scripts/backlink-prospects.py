#!/usr/bin/env python3
"""
Backlink prospect generator.

Uses the Brave Search API to find HVAC trade schools, contractor blogs,
and manufacturer resource pages that maintain "useful resources" link
lists. These are the highest-conversion outreach targets because they're
already in the habit of curating external links.

Brave Search free tier = 2000 queries/month. Need BRAVE_API_KEY env var.

USAGE:
    BRAVE_API_KEY=... python scripts/backlink-prospects.py
    python scripts/backlink-prospects.py --topic boiler --limit 30

OUTPUT: growth-pipeline/outreach/YYYY-MM-DD_prospects.csv + .md

The CSV is ready to import into a CRM or Google Sheet for tracking.
The .md has personalized outreach drafts referencing one of our articles.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "growth-pipeline" / "outreach"
SITE = "https://errorcodefixes.com"

BRAVE_API_KEY = os.environ.get("BRAVE_API_KEY", "")

# Queries crafted to find pages with curated external link lists in our niche.
# Simpler queries return more DDG results than complex Boolean expressions.
PROSPECT_QUERIES = {
    "HVAC trade school resources": [
        "HVAC training program resources",
        "HVAC apprentice helpful links",
        "HVAC certification study resources",
    ],
    "Contractor blog resource pages": [
        "HVAC contractor blog troubleshooting resources",
        "HVAC service company reference page",
        "appliance repair blog recommended resources",
    ],
    "Boiler / hydronic resource pages": [
        "boiler service hydronic resources",
        "tankless water heater installer resources",
        "boiler troubleshooting reference",
    ],
    "VFD / industrial controls": [
        "PowerFlex troubleshooting resources",
        "industrial electrician VFD resources",
        "automation engineer reference links",
    ],
    "Manufacturer authorized service": [
        "Hoshizaki service technician resources",
        "Manitowoc ice machine troubleshooting reference",
        "commercial refrigeration technician resources",
    ],
}

# Domains to skip in results (these are not link-target candidates)
SKIP_DOMAINS = {
    "errorcodefixes.com", "pinterest.com", "youtube.com", "facebook.com",
    "amazon.com", "reddit.com", "wikipedia.org", "linkedin.com",
    "homedepot.com", "lowes.com", "amazon.co", "google.com", "bing.com",
    "duckduckgo.com", "yelp.com", "yahoo.com", "twitter.com", "x.com",
    "instagram.com", "tiktok.com",
}

# Articles to reference in personalized outreach (highest-quality candidates)
SAMPLE_ARTICLES = {
    "hvac": ("carrier-13-error-code", "Carrier furnace code 13 troubleshooting guide"),
    "appliance": ("samsung-refrigerator-error-codes", "Samsung refrigerator error codes guide"),
    "boiler": ("weil-mclain-error-code-3", "Weil-McLain code 3 troubleshooting"),
    "vfd": ("allen-bradley-powerflex-f004-fault", "PowerFlex F004 undervoltage diagnostic"),
    "refrigeration": ("manitowoc-e01-error-code", "Manitowoc E01 long-freeze cycle fix"),
}


def fetch_brave(query: str) -> list[tuple[str, str]]:
    """Returns list of (url, title) from Brave Search API."""
    if not BRAVE_API_KEY:
        print("[!] BRAVE_API_KEY not set. Skipping.")
        return []
    q = urllib.parse.quote_plus(query)
    url = f"https://api.search.brave.com/res/v1/web/search?q={q}&count=20&country=US&search_lang=en"
    req = urllib.request.Request(url, headers={
        "X-Subscription-Token": BRAVE_API_KEY,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"[!] Failed Brave query '{query[:40]}': {e}")
        return []
    results = []
    for r in (data.get("web", {}).get("results", []) or []):
        href = r.get("url")
        title = r.get("title", "")
        if href and href.startswith("http"):
            results.append((href, title))
    return results


def domain_of(url: str) -> str:
    m = re.match(r"https?://(?:www\.)?([^/]+)/?", url)
    return m.group(1).lower() if m else ""


def filter_prospects(results: list[tuple[str, str]]) -> list[dict]:
    """Filter to reasonable backlink targets."""
    seen_domains = set()
    out = []
    for url, title in results:
        d = domain_of(url)
        if not d or d in seen_domains:
            continue
        if any(skip in d for skip in SKIP_DOMAINS):
            continue
        # Avoid commercial parts retailers (they don't link out)
        if any(s in d for s in ("repairclinic", "partsdirect", "ereplacement", "supplyhouse", "automationdirect")):
            continue
        out.append({"url": url, "title": title, "domain": d})
        seen_domains.add(d)
    return out


def pick_article_for_outreach(topic: str) -> tuple[str, str]:
    """Match a topic to one of our sample articles."""
    t = topic.lower()
    if "boiler" in t or "hydronic" in t or "tankless" in t:
        return SAMPLE_ARTICLES["boiler"]
    if "vfd" in t or "industrial" in t or "automation" in t:
        return SAMPLE_ARTICLES["vfd"]
    if "appliance" in t:
        return SAMPLE_ARTICLES["appliance"]
    if "refrigeration" in t or "manufacturer" in t or "hoshizaki" in t or "manitowoc" in t:
        return SAMPLE_ARTICLES["refrigeration"]
    return SAMPLE_ARTICLES["hvac"]


def build_outreach_email(prospect: dict, topic: str) -> str:
    slug, article_label = pick_article_for_outreach(topic)
    url = f"{SITE}/posts/{slug}/"
    domain = prospect["domain"]
    return (
        f"Subject: Resource for your {topic.lower()} page on {domain}\n"
        f"\n"
        f"Hi,\n"
        f"\n"
        f"I noticed your team curates a list of {topic.lower()} on {domain}. We just shipped a comprehensive diagnostic guide that fits your existing collection well: {article_label}.\n"
        f"\n"
        f"Direct link: {url}\n"
        f"\n"
        f"It is technician-written with real OEM part numbers, microamp readings, and a step-by-step diagnostic tree. No paywall, no email gate, no marketing fluff.\n"
        f"\n"
        f"If it's a fit for your resources page, no rush — happy to write a 2-sentence blurb in your house style if useful.\n"
        f"\n"
        f"Either way, thanks for keeping a useful resource list. Those are increasingly rare.\n"
        f"\n"
        f"Best,\n"
        f"[YOUR NAME]\n"
        f"errorcodefixes.com\n"
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--topic", help="Filter to one specific topic from the query set")
    p.add_argument("--limit", type=int, default=40, help="Max prospects to surface")
    p.add_argument("--sleep", type=float, default=3.0, help="Seconds between DDG queries")
    args = p.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")

    all_prospects: list[dict] = []
    queries_run = PROSPECT_QUERIES
    if args.topic:
        queries_run = {k: v for k, v in PROSPECT_QUERIES.items() if args.topic.lower() in k.lower()}

    for topic, queries in queries_run.items():
        print(f"\n=== {topic} ===")
        topic_results = []
        for q in queries:
            print(f"  Querying: {q[:60]}...")
            raw = fetch_brave(q)
            topic_results.extend(raw)
            time.sleep(args.sleep)
        filtered = filter_prospects(topic_results)
        for f in filtered:
            f["topic"] = topic
        all_prospects.extend(filtered[:15])  # cap per topic
        print(f"  -> {len(filtered)} unique prospects")

    # De-dupe by domain
    seen = set()
    deduped = []
    for p_ in all_prospects:
        if p_["domain"] in seen:
            continue
        seen.add(p_["domain"])
        deduped.append(p_)
        if len(deduped) >= args.limit:
            break

    # Write CSV
    csv_path = OUT_DIR / f"{date_stamp}_prospects.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["domain", "url", "title", "topic", "outreach_status", "sent_date", "reply_status", "linked", "notes"])
        w.writeheader()
        for prosp in deduped:
            w.writerow({
                "domain": prosp["domain"],
                "url": prosp["url"],
                "title": prosp["title"],
                "topic": prosp["topic"],
                "outreach_status": "queued",
                "sent_date": "",
                "reply_status": "",
                "linked": "",
                "notes": "",
            })

    # Write outreach drafts MD
    md_path = OUT_DIR / f"{date_stamp}_outreach_drafts.md"
    lines = [
        f"# Backlink Outreach Batch — {date_stamp}",
        "",
        f"{len(deduped)} prospects identified. Each has a personalized draft below.",
        "",
        f"**How to use:** review each draft, edit lightly, copy/paste into Gmail (booyajones222@gmail.com), send. Update {csv_path.name} with sent_date as you go.",
        "",
        f"**Realistic reply rate:** 5-15%. Expect 2-6 actual backlinks earned from a batch of 40 outreach emails.",
        "",
        f"**Common rejection reasons:** \"we don't add new links\", \"send a guest post instead\", \"contact someone else\". File polite responses, don't argue.",
        "",
        "---",
        "",
    ]
    for i, prosp in enumerate(deduped, 1):
        lines.append(f"## {i}. {prosp['domain']} — {prosp['topic']}")
        lines.append(f"")
        lines.append(f"**Page:** {prosp['url']}")
        lines.append(f"**Page title:** {prosp['title']}")
        lines.append(f"")
        lines.append(f"### Draft (copy + edit + send)")
        lines.append(f"")
        lines.append(f"```")
        lines.append(build_outreach_email(prosp, prosp["topic"]))
        lines.append(f"```")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[+] Wrote {len(deduped)} prospects to:")
    print(f"    {csv_path}")
    print(f"    {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
