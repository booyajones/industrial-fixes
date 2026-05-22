#!/usr/bin/env python3
"""
Weekly traffic and search-performance report.

Pulls last-28-day data from:
  - Plausible (visitors, pageviews, bounce, top pages)
  - Google Search Console (impressions, clicks, position, top queries)

Writes a markdown report to growth-pipeline/reports/YYYY-MM-DD_traffic.md.

Designed to run weekly via Windows Task Scheduler so Chris gets a
Monday-morning view of what moved the previous week.

USAGE:
    python scripts/weekly-traffic-report.py
"""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "growth-pipeline" / "reports"
SITE = "errorcodefixes.com"


def plausible(plk: str, period: str = "30d") -> dict:
    """Pull aggregate + top pages from Plausible API."""
    base = "https://plausible.io/api/v1/stats"
    req = lambda u: urllib.request.Request(u, headers={"Authorization": f"Bearer {plk}"})

    agg_url = f"{base}/aggregate?site_id={SITE}&period={period}&metrics=visitors,pageviews,bounce_rate,visit_duration"
    with urllib.request.urlopen(req(agg_url), timeout=30) as r:
        agg = json.loads(r.read())["results"]

    pages_url = (
        f"{base}/breakdown?site_id={SITE}&period={period}"
        "&property=event:page&metrics=visitors,pageviews,bounce_rate&limit=30"
    )
    with urllib.request.urlopen(req(pages_url), timeout=30) as r:
        pages = json.loads(r.read()).get("results", [])

    sources_url = (
        f"{base}/breakdown?site_id={SITE}&period={period}"
        "&property=visit:source&metrics=visitors&limit=15"
    )
    with urllib.request.urlopen(req(sources_url), timeout=30) as r:
        sources = json.loads(r.read()).get("results", [])

    return {"agg": agg, "pages": pages, "sources": sources}


def gsc(sa_path: str, days: int = 28) -> dict:
    """Pull search analytics from GSC API."""
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    creds = service_account.Credentials.from_service_account_file(
        sa_path, scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    svc = build("searchconsole", "v1", credentials=creds)
    site_url = f"https://{SITE}/"
    end = date.today() - timedelta(days=2)
    start = end - timedelta(days=days)

    def q(dims, limit=30):
        return svc.searchanalytics().query(siteUrl=site_url, body={
            "startDate": str(start),
            "endDate": str(end),
            "dimensions": dims,
            "rowLimit": limit,
        }).execute().get("rows", [])

    queries = q(["query"], 25)
    pages = q(["page"], 30)
    # Bonus: country breakdown lets us see if traffic skews to one geo
    countries = q(["country"], 10)

    return {"queries": queries, "pages": pages, "countries": countries}


def fmt_pl_row(r: dict) -> str:
    return f"{r['visitors']:>5}  {r['pageviews']:>5}  br={r.get('bounce_rate','?')}%  {r['page']}"


def fmt_gsc_row(r: dict) -> str:
    return (f"imp={r['impressions']:>5}  clicks={r['clicks']:>3}  "
            f"pos={r['position']:>5.1f}  ctr={r['ctr']*100:>4.1f}%")


def main() -> int:
    plk = os.environ.get("PLAUSIBLE_API_KEY")
    sa_path = os.environ.get("GSC_SERVICE_ACCOUNT_JSON",
                             r"C:\Users\Administrator\.claude\secrets\gsc-sa.json")
    if not plk:
        print("[!] PLAUSIBLE_API_KEY missing")
        return 1
    if not Path(sa_path).exists():
        print(f"[!] GSC SA JSON missing at {sa_path}")
        return 1

    pl = plausible(plk)
    gs = gsc(sa_path)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    out_path = OUT_DIR / f"{date_stamp}_traffic.md"

    agg = pl["agg"]

    lines = [
        f"# Traffic & Search Report — {date_stamp}",
        "",
        f"Window: last 30 days (Plausible) / 28 days excluding latest 2 days (GSC).",
        "",
        "## Topline",
        "",
        f"- Visitors: **{agg['visitors']['value']}**",
        f"- Pageviews: **{agg['pageviews']['value']}**",
        f"- Pageviews / visitor: **{agg['pageviews']['value']/max(agg['visitors']['value'],1):.2f}**",
        f"- Bounce rate: **{agg['bounce_rate']['value']}%**",
        f"- Avg visit duration: **{agg['visit_duration']['value']}s**",
        "",
        "## Traffic sources (Plausible)",
        "",
        "| Visitors | Source |",
        "|---|---|",
    ]
    for s in pl["sources"][:10]:
        src = s.get("source") or "(direct)"
        lines.append(f"| {s['visitors']} | {src} |")

    lines.extend([
        "",
        "## Top pages by visitors (Plausible)",
        "",
        "| Visitors | Pageviews | Bounce | Page |",
        "|---|---|---|---|",
    ])
    for r in pl["pages"][:15]:
        lines.append(f"| {r['visitors']} | {r['pageviews']} | {r.get('bounce_rate','?')}% | `{r['page']}` |")

    lines.extend([
        "",
        "## Top search queries (GSC)",
        "",
        "Position 1-3 with low CTR = title/meta description optimization candidate.",
        "",
        "| Imp | Clk | Pos | CTR | Query |",
        "|---|---|---|---|---|",
    ])
    # Sort by impressions
    queries = sorted(gs["queries"], key=lambda r: -r["impressions"])[:20]
    for r in queries:
        q = r["keys"][0]
        lines.append(f"| {r['impressions']} | {r['clicks']} | {r['position']:.1f} | "
                     f"{r['ctr']*100:.1f}% | {q} |")

    lines.extend([
        "",
        "## Top SERP pages (GSC)",
        "",
        "Pages with impressions > 5 and 0 clicks = needs title surgery or backlinks to climb past page 5.",
        "",
        "| Imp | Clk | Pos | CTR | Page |",
        "|---|---|---|---|---|",
    ])
    pages = sorted(gs["pages"], key=lambda r: -r["impressions"])[:20]
    for r in pages:
        p = r["keys"][0].replace(f"https://{SITE}", "")
        lines.append(f"| {r['impressions']} | {r['clicks']} | {r['position']:.1f} | "
                     f"{r['ctr']*100:.1f}% | `{p}` |")

    lines.extend([
        "",
        "## Country breakdown (GSC)",
        "",
        "| Country | Imp | Clk |",
        "|---|---|---|",
    ])
    for r in gs["countries"][:10]:
        lines.append(f"| {r['keys'][0]} | {r['impressions']} | {r['clicks']} |")

    # Auto-generated takeaways
    lines.extend([
        "",
        "## Auto-takeaways",
        "",
    ])

    # 1. Find pages with high impressions but 0 clicks (ranking-but-not-clicked)
    bad_ctr = [r for r in pages if r["impressions"] >= 5 and r["clicks"] == 0]
    if bad_ctr:
        lines.append(f"- **{len(bad_ctr)} pages with 5+ impressions but 0 clicks** "
                     "→ title/meta description surgery candidates:")
        for r in bad_ctr[:5]:
            p = r["keys"][0].replace(f"https://{SITE}", "")
            lines.append(f"  - `{p}` (pos {r['position']:.1f}, imp {r['impressions']})")

    # 2. Find queries we rank top-3 for but get 0 clicks
    top3_no_click = [r for r in queries if r["position"] <= 3 and r["clicks"] == 0]
    if top3_no_click:
        lines.append(f"- **{len(top3_no_click)} queries where we rank top-3 but get 0 clicks** "
                     "→ user intent mismatch:")
        for r in top3_no_click[:5]:
            lines.append(f"  - `{r['keys'][0]}` (pos {r['position']:.1f}, imp {r['impressions']})")

    # 3. Find queries on page 2 (pos 11-20) where one push could land page 1
    near_p1 = [r for r in queries if 11 <= r["position"] <= 20 and r["impressions"] >= 3]
    if near_p1:
        lines.append(f"- **{len(near_p1)} queries on page 2 (pos 11-20) with 3+ impressions** "
                     "→ internal-link + content depth could move to page 1:")
        for r in near_p1[:5]:
            lines.append(f"  - `{r['keys'][0]}` (pos {r['position']:.1f}, imp {r['impressions']})")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Report: {out_path}")
    print(f"    Visitors: {agg['visitors']['value']}, Pageviews: {agg['pageviews']['value']}, "
          f"Bounce: {agg['bounce_rate']['value']}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
