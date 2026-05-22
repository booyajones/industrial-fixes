#!/usr/bin/env python3
"""
Weekly traffic and search-performance report — GA4 + GSC.

Pulls last-28-day data from:
  - Google Analytics 4 (users, pageviews, bounce, top pages, sources)
  - Google Search Console (impressions, clicks, position, top queries)

Writes a markdown report to growth-pipeline/reports/YYYY-MM-DD_traffic.md.

Plausible was swapped out 2026-05-22 — it was undercounting by ~65x because
ad-blockers block its script. GA4 captures the real visitor numbers.

USAGE:
    python scripts/weekly-traffic-report.py
"""

from __future__ import annotations

import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "growth-pipeline" / "reports"
SITE = "errorcodefixes.com"
GA4_PROPERTY = "properties/534919316"


def ga4(sa_path: str, days: int = 30) -> dict:
    """Pull aggregate + breakdowns from GA4."""
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        RunReportRequest, DateRange, Metric, Dimension, OrderBy,
    )
    from google.oauth2 import service_account

    creds = service_account.Credentials.from_service_account_file(sa_path)
    c = BetaAnalyticsDataClient(credentials=creds)

    dr = [DateRange(start_date=f"{days}daysAgo", end_date="yesterday")]

    def run(dims, metrics, limit=20, order_metric="screenPageViews"):
        resp = c.run_report(RunReportRequest(
            property=GA4_PROPERTY,
            date_ranges=dr,
            dimensions=[Dimension(name=d) for d in dims],
            metrics=[Metric(name=m) for m in metrics],
            limit=limit,
            order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_metric), desc=True)],
        ))
        return [
            {
                **{dims[i]: row.dimension_values[i].value for i in range(len(dims))},
                **{metrics[i]: row.metric_values[i].value for i in range(len(metrics))},
            }
            for row in resp.rows
        ]

    # Topline
    topline_resp = c.run_report(RunReportRequest(
        property=GA4_PROPERTY,
        date_ranges=dr,
        metrics=[
            Metric(name="totalUsers"),
            Metric(name="screenPageViews"),
            Metric(name="bounceRate"),
            Metric(name="averageSessionDuration"),
            Metric(name="sessions"),
        ],
    ))
    t = topline_resp.rows[0].metric_values if topline_resp.rows else []
    topline = {
        "users": int(float(t[0].value)) if t else 0,
        "pageviews": int(float(t[1].value)) if t else 0,
        "bounce_rate_pct": round(float(t[2].value) * 100, 1) if t else 0,
        "avg_session_sec": round(float(t[3].value), 1) if t else 0,
        "sessions": int(float(t[4].value)) if t else 0,
    }

    pages = run(["pagePath"], ["screenPageViews", "totalUsers", "bounceRate"], limit=30)
    sources = run(["sessionSource"], ["totalUsers", "sessions"], limit=15, order_metric="totalUsers")
    countries = run(["country"], ["totalUsers"], limit=10, order_metric="totalUsers")

    return {
        "topline": topline,
        "pages": pages,
        "sources": sources,
        "countries": countries,
    }


def gsc(sa_path: str, days: int = 28) -> dict:
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

    return {
        "queries": q(["query"], 25),
        "pages": q(["page"], 30),
        "countries": q(["country"], 10),
    }


def main() -> int:
    sa_path = os.environ.get("GSC_SERVICE_ACCOUNT_JSON",
                             r"C:\Users\Administrator\.claude\secrets\gsc-sa.json")
    if not Path(sa_path).exists():
        print(f"[!] SA JSON missing at {sa_path}")
        return 1

    print("Pulling GA4...")
    ga = ga4(sa_path)
    print("Pulling GSC...")
    gs = gsc(sa_path)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    out_path = OUT_DIR / f"{date_stamp}_traffic.md"

    t = ga["topline"]
    pages = ga["pages"]
    sources = ga["sources"]

    lines = [
        f"# Traffic & Search Report — {date_stamp}",
        "",
        "Window: last 30 days (GA4) / 28 days excluding latest 2 days (GSC).",
        "",
        "## Topline (GA4)",
        "",
        f"- Users: **{t['users']:,}**",
        f"- Sessions: **{t['sessions']:,}**",
        f"- Pageviews: **{t['pageviews']:,}**",
        f"- Pageviews / session: **{t['pageviews']/max(t['sessions'],1):.2f}**",
        f"- Bounce rate: **{t['bounce_rate_pct']}%**",
        f"- Avg session duration: **{t['avg_session_sec']}s**",
        "",
        "## Traffic sources (GA4)",
        "",
        "| Users | Sessions | Source |",
        "|---|---|---|",
    ]
    for s in sources[:12]:
        src = s.get("sessionSource") or "(direct)"
        lines.append(f"| {s['totalUsers']} | {s['sessions']} | {src} |")

    lines.extend([
        "",
        "## Top pages by pageviews (GA4)",
        "",
        "| PV | Users | Bounce | Page |",
        "|---|---|---|---|",
    ])
    for r in pages[:20]:
        br = round(float(r.get("bounceRate", 0)) * 100, 1)
        lines.append(f"| {r['screenPageViews']} | {r['totalUsers']} | {br}% | `{r['pagePath']}` |")

    lines.extend([
        "",
        "## Top search queries (GSC)",
        "",
        "Position 1-3 with low CTR = title/meta description optimization candidate.",
        "",
        "| Imp | Clk | Pos | CTR | Query |",
        "|---|---|---|---|---|",
    ])
    queries = sorted(gs["queries"], key=lambda r: -r["impressions"])[:20]
    for r in queries:
        lines.append(
            f"| {r['impressions']} | {r['clicks']} | {r['position']:.1f} | "
            f"{r['ctr']*100:.1f}% | {r['keys'][0]} |"
        )

    lines.extend([
        "",
        "## Top SERP pages (GSC)",
        "",
        "Pages with impressions > 5 and 0 clicks = needs title surgery or backlinks.",
        "",
        "| Imp | Clk | Pos | CTR | Page |",
        "|---|---|---|---|---|",
    ])
    gsc_pages = sorted(gs["pages"], key=lambda r: -r["impressions"])[:20]
    for r in gsc_pages:
        p = r["keys"][0].replace(f"https://{SITE}", "")
        lines.append(
            f"| {r['impressions']} | {r['clicks']} | {r['position']:.1f} | "
            f"{r['ctr']*100:.1f}% | `{p}` |"
        )

    lines.extend([
        "",
        "## Country breakdown (GA4)",
        "",
        "| Country | Users |",
        "|---|---|",
    ])
    for r in ga["countries"][:10]:
        lines.append(f"| {r['country']} | {r['totalUsers']} |")

    lines.extend([
        "",
        "## Auto-takeaways",
        "",
    ])
    bad_ctr = [r for r in gsc_pages if r["impressions"] >= 5 and r["clicks"] == 0]
    if bad_ctr:
        lines.append(
            f"- **{len(bad_ctr)} pages with 5+ impressions but 0 clicks** "
            "→ title/meta description surgery candidates:"
        )
        for r in bad_ctr[:5]:
            p = r["keys"][0].replace(f"https://{SITE}", "")
            lines.append(f"  - `{p}` (pos {r['position']:.1f}, imp {r['impressions']})")

    top3_no_click = [r for r in queries if r["position"] <= 3 and r["clicks"] == 0]
    if top3_no_click:
        lines.append(
            f"- **{len(top3_no_click)} queries where we rank top-3 but get 0 clicks** "
            "→ user intent mismatch:"
        )
        for r in top3_no_click[:5]:
            lines.append(f"  - `{r['keys'][0]}` (pos {r['position']:.1f}, imp {r['impressions']})")

    near_p1 = [r for r in queries if 11 <= r["position"] <= 20 and r["impressions"] >= 3]
    if near_p1:
        lines.append(
            f"- **{len(near_p1)} queries on page 2 (pos 11-20) with 3+ impressions** "
            "→ content depth + internal linking could push to page 1:"
        )
        for r in near_p1[:5]:
            lines.append(f"  - `{r['keys'][0]}` (pos {r['position']:.1f}, imp {r['impressions']})")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Report: {out_path}")
    print(f"    Users: {t['users']:,}  Pageviews: {t['pageviews']:,}  Bounce: {t['bounce_rate_pct']}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
