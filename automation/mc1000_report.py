"""
errorcodefixes.com — Weekly mC/1000 readout (the North Star optimization loop).

North Star (set by council 2026-06-01): mC/1000 = monetized affiliate clicks per
1,000 sessions. This job reads GA4, computes mC/1000 for the last 7 days vs the
prior 7 (WoW trend), and — crucially — auto-surfaces the highest-traffic /
lowest-converting pages as the next conversion-optimization targets, then posts
to Slack. This is what makes "don't stop until achieved" run on its own: every
week it tells us where the next swarm should focus, driven by real data.

Monetized clicks = GA4 events `affiliate_click` + `lead_click` (emitted by
src/scripts/analytics.ts on every Amazon/Impact/Angi outbound click).

Env (provided by the workflow): GOOGLE_APPLICATION_CREDENTIALS (SA file with GA4
read on the property), GA4_PROPERTY_ID, SLACK_BOT_TOKEN.
"""
import os
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request as GoogleRequest

PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "534919316")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", os.environ.get("SLACK_TOKEN", ""))
SLACK_CHANNEL = "C0AQZ85MCEN"  # #proj-industrial-code-errors
MONETIZED_EVENTS = ["affiliate_click", "lead_click"]
GA4_URL = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"


def _token():
    creds = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=["https://www.googleapis.com/auth/analytics.readonly"],
    )
    creds.refresh(GoogleRequest())
    return creds.token


def _run(headers, body):
    r = requests.post(GA4_URL, headers=headers, json=body, timeout=60)
    if r.status_code != 200:
        print(f"GA4 error {r.status_code}: {r.text[:300]}")
        return {}
    return r.json()


def sessions(headers, start, end):
    d = _run(headers, {"dateRanges": [{"startDate": start, "endDate": end}],
                       "metrics": [{"name": "sessions"}]})
    rows = d.get("rows", [])
    return int(rows[0]["metricValues"][0]["value"]) if rows else 0


def monetized_clicks(headers, start, end):
    d = _run(headers, {
        "dateRanges": [{"startDate": start, "endDate": end}],
        "dimensions": [{"name": "eventName"}],
        "metrics": [{"name": "eventCount"}],
        "dimensionFilter": {"filter": {"fieldName": "eventName",
                                       "inListFilter": {"values": MONETIZED_EVENTS}}},
    })
    return sum(int(r["metricValues"][0]["value"]) for r in d.get("rows", []))


def by_page(headers, start, end, metric, event=None):
    body = {
        "dateRanges": [{"startDate": start, "endDate": end}],
        "dimensions": [{"name": "pagePath"}],
        "metrics": [{"name": metric}],
        "orderBys": [{"metric": {"metricName": metric}, "desc": True}],
        "limit": 200,
    }
    if event:
        body["dimensionFilter"] = {"filter": {"fieldName": "eventName",
                                              "stringFilter": {"value": event}}}
    d = _run(headers, body)
    return {r["dimensionValues"][0]["value"]: int(r["metricValues"][0]["value"])
            for r in d.get("rows", [])}


def clicks_by_placement(headers, start, end):
    """Monetized clicks broken down by the `placement` custom dimension
    (at_a_glance / parts_table / ...). Registered 2026-06-01; populates as
    data accrues. This is the A/B signal: which placement converts best."""
    d = _run(headers, {
        "dateRanges": [{"startDate": start, "endDate": end}],
        "dimensions": [{"name": "customEvent:placement"}],
        "metrics": [{"name": "eventCount"}],
        "dimensionFilter": {"filter": {"fieldName": "eventName",
                                       "inListFilter": {"values": MONETIZED_EVENTS}}},
        "orderBys": [{"metric": {"metricName": "eventCount"}, "desc": True}],
    })
    out = {}
    for r in d.get("rows", []):
        name = r["dimensionValues"][0]["value"] or "(unset)"
        out[name] = int(r["metricValues"][0]["value"])
    return out


def mc1000(clicks, sess):
    return round(clicks / sess * 1000, 1) if sess else 0.0


def build_report():
    headers = {"Authorization": f"Bearer {_token()}", "Content-Type": "application/json"}

    s_now = sessions(headers, "7daysAgo", "yesterday")
    s_prev = sessions(headers, "14daysAgo", "8daysAgo")
    c_now = monetized_clicks(headers, "7daysAgo", "yesterday")
    c_prev = monetized_clicks(headers, "14daysAgo", "8daysAgo")
    mc_now, mc_prev = mc1000(c_now, s_now), mc1000(c_prev, s_prev)

    sess_pp = by_page(headers, "7daysAgo", "yesterday", "sessions")
    click_pp = by_page(headers, "7daysAgo", "yesterday", "eventCount", event="affiliate_click")

    # Pages with enough traffic to be worth optimizing, ranked by mC/1000.
    MIN_SESS = 15
    scored = []
    for path, sess in sess_pp.items():
        if sess < MIN_SESS or not path.startswith("/posts/"):
            continue
        clicks = click_pp.get(path, 0)
        scored.append((path, sess, clicks, mc1000(clicks, sess)))
    worst = sorted(scored, key=lambda x: (x[3], -x[1]))[:6]   # low mC/1000, high traffic first
    best = sorted(scored, key=lambda x: -x[3])[:4]

    trend = ""
    if mc_prev:
        delta = round((mc_now - mc_prev) / mc_prev * 100)
        trend = f" ({'+' if delta >= 0 else ''}{delta}% WoW)"
    elif mc_now:
        trend = " (first week of data)"

    L = ["*📊 errorcodefixes.com — Weekly North Star: mC/1000*",
         f"_Monetized affiliate clicks per 1,000 sessions. Last 7 days._",
         "",
         f"*mC/1000: {mc_now}*{trend}   ·   {c_now:,} monetized clicks / {s_now:,} sessions",
         f"Prior week: {mc_prev} ({c_prev:,} / {s_prev:,})"]

    if not scored:
        L += ["", "_Not enough page-level data yet — baseline still accumulating "
              "(tool-link + placement tracking went live recently). Numbers firm up over 1–2 weeks._"]
    else:
        L += ["", "*🎯 Next-wave targets (high traffic, low mC/1000):*"]
        for path, sess, clicks, mc in worst:
            L.append(f"• `{path}` — {sess:,} sess, {clicks} clicks, *mC/1000 {mc}*")
        L += ["", "*✅ Best converters (what's working — copy the pattern):*"]
        for path, sess, clicks, mc in best:
            L.append(f"• `{path}` — mC/1000 *{mc}* ({clicks}/{sess})")

    placements = clicks_by_placement(headers, "7daysAgo", "yesterday")
    if placements:
        L += ["", "*🅰️🅱️ Monetized clicks by placement (where they convert):*"]
        for name, n in sorted(placements.items(), key=lambda x: -x[1]):
            L.append(f"• {name}: *{n}*")
    else:
        L += ["", "_Placement A/B: custom dimensions registered 2026-06-01; "
              "breakdown populates as clicks accrue (none yet)._"]
    return "\n".join(L)


def main():
    try:
        msg = build_report()
    except Exception as e:
        msg = f"*mC/1000 weekly report FAILED:* {e}"
    if SLACK_BOT_TOKEN:
        r = requests.post("https://slack.com/api/chat.postMessage",
                          headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}",
                                   "Content-Type": "application/json"},
                          json={"channel": SLACK_CHANNEL, "text": msg,
                                "unfurl_links": False}, timeout=30)
        ok = r.json().get("ok")
        print("Slack posted" if ok else f"Slack error: {r.json().get('error')}")
    print(msg)


if __name__ == "__main__":
    main()
