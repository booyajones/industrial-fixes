#!/usr/bin/env python3
"""errorcodefixes.com unified metrics digest — GA4 + GSC + Cloudflare.

The site COLLECTS data (GA4 + custom affiliate_click event, GSC, Bing, IndexNow)
but until now nothing READ it back. This pulls all readable sources into one
digest, computes the North Star (mC/1000 = monetized affiliate clicks per 1,000
engaged sessions), and tracks the indexed-page count over time (the new-domain
sandbox-lift gauge).

Every source degrades GRACEFULLY: if a credential isn't granted yet it prints the
EXACT one-time action needed instead of failing. So this is useful today (shows
what's pending) and fully live the moment the grants are made.

Grants needed (one-time, see --help output):
  GA4 : add the service-account email as Viewer on the GA4 property
  GSC : add the same SA email as a user on the Search Console property
  CF  : add 'Zone Analytics: Read' to the Cloudflare API token

Usage:
  python scripts/ecf-metrics.py            # 28-day digest to stdout
  python scripts/ecf-metrics.py --days 7
  python scripts/ecf-metrics.py --json     # machine-readable + append snapshot
"""
from __future__ import annotations
import json
import sys
import datetime
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATHS = [ROOT / ".env", Path("C:/Users/chris/OneDrive/Desktop/Claude/.env")]
SNAPSHOT = ROOT / ".planning" / "metrics-history.jsonl"
GA4_MEASUREMENT = "G-083FJXZNP7"
SITE = "https://errorcodefixes.com/"


def load_env() -> dict:
    env = {}
    for p in ENV_PATHS:
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env.setdefault(k, v.strip().strip('"').strip("'"))
    return env


def _post(url, tok, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"})
    try:
        return 200, json.load(urllib.request.urlopen(req, timeout=45))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:400]
    except Exception as e:  # network etc.
        return -1, str(e)[:200]


def _get(url, tok):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
    try:
        return 200, json.load(urllib.request.urlopen(req, timeout=45))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:400]
    except Exception as e:
        return -1, str(e)[:200]


def google_token(env, scopes):
    try:
        from google.oauth2 import service_account
        import google.auth.transport.requests as gtr
    except ImportError:
        return None, "google-auth not installed (pip install google-auth)"
    gac = env.get("GOOGLE_APPLICATION_CREDENTIALS", "")
    if not gac or not Path(gac).exists():
        return None, "GOOGLE_APPLICATION_CREDENTIALS not set / file missing"
    try:
        creds = service_account.Credentials.from_service_account_file(gac, scopes=scopes)
        creds.refresh(gtr.Request())
        sa_email = json.load(open(gac)).get("client_email", "?")
        return (creds.token, sa_email), None
    except Exception as e:
        return None, str(e)[:200]


def ga4(env, days):
    out = {"ok": False}
    prop = env.get("GA4_PROPERTY_ID", "").replace("properties/", "")
    if not prop:
        out["error"] = "GA4_PROPERTY_ID not set in .env"
        return out
    tokinfo, err = google_token(env, ["https://www.googleapis.com/auth/analytics.readonly"])
    if not tokinfo:
        out["error"] = err
        return out
    tok, sa = tokinfo
    base = f"https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport"
    dr = [{"startDate": f"{days}daysAgo", "endDate": "today"}]
    sc, totals = _post(base, tok, {"dateRanges": dr, "metrics": [
        {"name": "sessions"}, {"name": "activeUsers"}, {"name": "engagedSessions"},
        {"name": "engagementRate"}, {"name": "averageSessionDuration"}, {"name": "screenPageViews"}]})
    if sc == 403:
        out["error"] = f"GA4 403 — grant Viewer to {sa} on property {prop} (GA4 Admin > Property Access Management)"
        out["grant_email"] = sa
        return out
    if sc != 200:
        out["error"] = f"GA4 {sc}: {totals}"
        return out
    row = (totals.get("rows") or [{}])[0].get("metricValues", [])
    vals = [m.get("value", "0") for m in row] or ["0"] * 6
    sessions, users, engaged, engrate, dur, views = vals
    # affiliate_click event count
    _, ev = _post(base, tok, {"dateRanges": dr, "dimensions": [{"name": "eventName"}],
                              "metrics": [{"name": "eventCount"}],
                              "dimensionFilter": {"filter": {"fieldName": "eventName", "stringFilter": {"value": "affiliate_click"}}}})
    aff = 0
    if isinstance(ev, dict):
        for r in ev.get("rows", []):
            aff += int(r["metricValues"][0]["value"])
    # top pages
    _, tp = _post(base, tok, {"dateRanges": dr, "dimensions": [{"name": "pagePath"}],
                              "metrics": [{"name": "sessions"}], "limit": 8,
                              "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]})
    top = [(r["dimensionValues"][0]["value"], r["metricValues"][0]["value"])
           for r in (tp.get("rows", []) if isinstance(tp, dict) else [])]
    eng = float(engaged or 0)
    out.update(ok=True, sessions=int(float(sessions)), users=int(float(users)),
               engaged_sessions=int(eng), engagement_rate=round(float(engrate or 0) * 100, 1),
               avg_session_sec=round(float(dur or 0), 1), pageviews=int(float(views)),
               affiliate_clicks=aff,
               mC_per_1000=round((aff / eng * 1000), 2) if eng else 0.0,
               top_pages=top)
    return out


def gsc(env, days):
    out = {"ok": False}
    tokinfo, err = google_token(env, ["https://www.googleapis.com/auth/webmasters.readonly"])
    if not tokinfo:
        out["error"] = err
        return out
    tok, sa = tokinfo
    sc, sites = _get("https://www.googleapis.com/webmasters/v3/sites", tok)
    site_urls = [s["siteUrl"] for s in sites.get("siteEntry", [])] if isinstance(sites, dict) else []
    target = next((s for s in site_urls if "errorcodefixes" in s), None)
    if not target:
        out["error"] = (f"GSC: SA {sa} has no access. Add it as a user in Search Console "
                        f"(Settings > Users and permissions) for the errorcodefixes.com property.")
        out["grant_email"] = sa
        return out
    end = datetime.date.today() - datetime.timedelta(days=2)  # GSC lags ~2d
    start = end - datetime.timedelta(days=days)
    base = f"https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(target, safe='')}/searchAnalytics/query"
    sc, tot = _post(base, tok, {"startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": []})
    agg = (tot.get("rows", [{}])[0] if isinstance(tot, dict) and tot.get("rows") else {})
    _, q = _post(base, tok, {"startDate": start.isoformat(), "endDate": end.isoformat(),
                             "dimensions": ["query"], "rowLimit": 8})
    queries = [(r["keys"][0], r.get("clicks", 0), r.get("impressions", 0))
               for r in (q.get("rows", []) if isinstance(q, dict) else [])]
    # indexed-page count via sitemaps (submitted vs indexed)
    sc2, sm = _get(f"https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(target, safe='')}/sitemaps", tok)
    submitted = indexed = 0
    if isinstance(sm, dict):
        for s in sm.get("sitemap", []):
            for c in s.get("contents", []):
                submitted += int(c.get("submitted", 0))
                indexed += int(c.get("indexed", 0))
    out.update(ok=True, site=target,
               clicks=int(agg.get("clicks", 0)), impressions=int(agg.get("impressions", 0)),
               ctr=round(agg.get("ctr", 0) * 100, 2), position=round(agg.get("position", 0), 1),
               sitemap_submitted=submitted, sitemap_indexed=indexed, top_queries=queries)
    return out


def cloudflare(env, days):
    out = {"ok": False}
    tok = env.get("CLOUDFLARE_FULL_TOKEN") or env.get("CLOUDFLARE_PAGES_TOKEN")
    zone = env.get("CLOUDFLARE_ZONE_ID")
    if not tok or not zone:
        out["error"] = "CLOUDFLARE_FULL_TOKEN / CLOUDFLARE_ZONE_ID not set"
        return out
    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)
    q = {"query": "query($zone:String!,$start:Date!,$end:Date!){viewer{zones(filter:{zoneTag:$zone}){httpRequests1dGroups(limit:31,filter:{date_geq:$start,date_leq:$end}){sum{requests pageViews}uniq{uniques}}}}}",
         "variables": {"zone": zone, "start": start.isoformat(), "end": end.isoformat()}}
    sc, r = _post("https://api.cloudflare.com/client/v4/graphql", tok, q)
    if isinstance(r, dict) and r.get("errors"):
        msg = r["errors"][0].get("message", "")
        if "analytics.read" in msg or "authz" in str(r["errors"][0].get("extensions", {})):
            out["error"] = ("CF token lacks 'Zone Analytics: Read'. Edit the Cloudflare API token "
                            "and add permission Zone > Analytics > Read for this zone.")
            return out
        out["error"] = f"CF: {msg}"
        return out
    if isinstance(r, dict) and r.get("data"):
        zones = r["data"]["viewer"]["zones"]
        if zones:
            reqs = sum(g["sum"]["requests"] for g in zones[0]["httpRequests1dGroups"])
            pv = sum(g["sum"]["pageViews"] for g in zones[0]["httpRequests1dGroups"])
            uniq = sum(g["uniq"]["uniques"] for g in zones[0]["httpRequests1dGroups"])
            out.update(ok=True, requests=reqs, pageviews=pv, uniques=uniq)
            return out
    out["error"] = f"CF unexpected: {str(r)[:150]}"
    return out


def render(ga, gs, cf, days):
    L = []
    L.append(f"\n{'='*64}\n  errorcodefixes.com — metrics digest (last {days} days)\n{'='*64}")
    L.append("\n[ ACQUISITION / TRAFFIC ]")
    if ga.get("ok"):
        L.append(f"  GA4 sessions={ga['sessions']}  users={ga['users']}  engaged={ga['engaged_sessions']}"
                 f"  engagement={ga['engagement_rate']}%  avg={ga['avg_session_sec']}s  views={ga['pageviews']}")
    else:
        L.append(f"  GA4: PENDING — {ga.get('error')}")
    if cf.get("ok"):
        L.append(f"  Cloudflare edge: requests={cf['requests']}  pageViews={cf['pageviews']}  uniques={cf['uniques']}")
    else:
        L.append(f"  Cloudflare: PENDING — {cf.get('error')}")
    L.append("\n[ SEARCH / INDEXATION  (the sandbox-lift gauge) ]")
    if gs.get("ok"):
        L.append(f"  GSC clicks={gs['clicks']}  impressions={gs['impressions']}  CTR={gs['ctr']}%  avg pos={gs['position']}")
        L.append(f"  Indexed pages: {gs['sitemap_indexed']} / {gs['sitemap_submitted']} submitted")
        if gs["top_queries"]:
            L.append("  Top queries: " + "; ".join(f"{k} ({c}c/{i}i)" for k, c, i in gs["top_queries"][:5]))
    else:
        L.append(f"  GSC: PENDING — {gs.get('error')}")
    L.append("\n[ CONVERSION / NORTH STAR ]")
    if ga.get("ok"):
        L.append(f"  affiliate_click events={ga['affiliate_clicks']}")
        L.append(f"  >>> mC/1000 (monetized clicks per 1k engaged sessions) = {ga['mC_per_1000']}")
        if ga["top_pages"]:
            L.append("  Top pages: " + "; ".join(f"{p} ({s})" for p, s in ga["top_pages"][:5]))
    else:
        L.append("  (needs GA4 access — see above)")
    L.append("\n[ REVENUE ]  (not yet automatable — needs API keys; see roadmap)")
    L.append("  Amazon Associates / Skimlinks / AdSense earnings are in their own dashboards.")
    # pending-grant summary
    pend = [n for n, o in [("GA4", ga), ("GSC", gs), ("Cloudflare", cf)] if not o.get("ok")]
    if pend:
        L.append(f"\n[ ACTION NEEDED ] grant access to: {', '.join(pend)} (details above).")
    return "\n".join(L)


def main():
    args = sys.argv[1:]
    days = 28
    if "--days" in args:
        days = int(args[args.index("--days") + 1])
    env = load_env()
    ga, gs, cf = ga4(env, days), gsc(env, days), cloudflare(env, days)
    snap = {"days": days, "ga4": ga, "gsc": gs, "cf": cf}
    if "--json" in args:
        print(json.dumps(snap, indent=2))
        SNAPSHOT.parent.mkdir(exist_ok=True)
        with open(SNAPSHOT, "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessions": ga.get("sessions"), "indexed": gs.get("sitemap_indexed"),
                                "impressions": gs.get("impressions"), "mC_1000": ga.get("mC_per_1000")}) + "\n")
    else:
        print(render(ga, gs, cf, days))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
