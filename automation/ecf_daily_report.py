"""
errorcodefixes.com Daily Traffic Report
Pulls GA4 + Cloudflare data and posts to Slack #proj-industrial-code-errors
"""
import json, requests, os
from datetime import datetime, timezone
from google.oauth2 import service_account
from google.auth.transport.requests import Request as GoogleRequest

PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "534919316")
CF_ZONE_ID = os.environ.get("CLOUDFLARE_ZONE_ID", "813cc094fec38ff0e2e666e534334944")
CF_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", "")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", os.environ.get("SLACK_TOKEN", ""))
SLACK_CHANNEL = "C0AQZ85MCEN"  # #proj-industrial-code-errors

def get_ga4_data():
    creds = service_account.Credentials.from_service_account_file(
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "C:/Users/Administrator/.openclaw/bigquery-key.json"),
        scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    creds.refresh(GoogleRequest())
    headers = {'Authorization': f'Bearer {creds.token}', 'Content-Type': 'application/json'}

    # Yesterday's data
    report_body = {
        "dateRanges": [
            {"startDate": "yesterday", "endDate": "yesterday"},
            {"startDate": "7daysAgo", "endDate": "yesterday"}
        ],
        "metrics": [
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "screenPageViews"},
            {"name": "bounceRate"},
            {"name": "averageSessionDuration"}
        ]
    }
    r = requests.post(
        f'https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport',
        headers=headers, json=report_body
    )
    if r.status_code != 200:
        return None, None
    
    data = r.json()
    rows = data.get('rows', [])
    
    yesterday = None
    week = None
    if rows:
        def parse_row(row):
            return {
                'sessions': int(row['metricValues'][0]['value']),
                'users': int(row['metricValues'][1]['value']),
                'pageviews': int(row['metricValues'][2]['value']),
                'bounce_rate': float(row['metricValues'][3]['value']),
                'avg_duration': float(row['metricValues'][4]['value'])
            }
        if len(rows) >= 1:
            yesterday = parse_row(rows[0])
        if len(rows) >= 2:
            week = parse_row(rows[1])

    # Top 5 pages yesterday
    pages_body = {
        "dateRanges": [{"startDate": "yesterday", "endDate": "yesterday"}],
        "dimensions": [{"name": "pagePath"}],
        "metrics": [{"name": "screenPageViews"}],
        "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}],
        "limit": 5
    }
    r2 = requests.post(
        f'https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport',
        headers=headers, json=pages_body
    )
    top_pages = []
    if r2.status_code == 200:
        for row in r2.json().get('rows', []):
            top_pages.append({
                'path': row['dimensionValues'][0]['value'],
                'views': int(row['metricValues'][0]['value'])
            })

    # Traffic sources
    sources_body = {
        "dateRanges": [{"startDate": "yesterday", "endDate": "yesterday"}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "sessions"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
        "limit": 5
    }
    r3 = requests.post(
        f'https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport',
        headers=headers, json=sources_body
    )
    sources = []
    if r3.status_code == 200:
        for row in r3.json().get('rows', []):
            sources.append({
                'channel': row['dimensionValues'][0]['value'],
                'sessions': int(row['metricValues'][0]['value'])
            })

    return {'yesterday': yesterday, 'week': week, 'top_pages': top_pages, 'sources': sources}

def get_cf_data():
    """Get Cloudflare analytics for yesterday"""
    body = {"query": """{ viewer { zones(filter: { zoneTag: \"""" + CF_ZONE_ID + """\" }) { httpRequests1dGroups(limit: 2, filter: { date_geq: "yesterday", date_leq: "yesterday" }) { sum { requests pageViews bytes threats } uniq { uniques } dimensions { date } } } } }"""}
    
    # Use GraphQL
    body = {
        "query": """
        {
          viewer {
            zones(filter: { zoneTag: "%s" }) {
              httpRequests1dGroups(limit: 1, filter: { date_geq: "yesterday", date_leq: "yesterday" }) {
                sum { requests pageViews bytes threats }
                uniq { uniques }
                dimensions { date }
              }
            }
          }
        }
        """ % CF_ZONE_ID
    }
    r = requests.post(
        "https://api.cloudflare.com/client/v4/graphql",
        headers={"Authorization": f"Bearer {CF_TOKEN}", "Content-Type": "application/json"},
        json=body
    )
    if r.status_code == 200:
        try:
            resp = r.json()
        except Exception:
            return None
        if not resp:
            return None
        zones = (resp.get('data') or {}).get('viewer', {}).get('zones', [{}])
        groups = zones[0].get('httpRequests1dGroups', []) if zones else []
        if groups:
            g = groups[0]
            return {
                'requests': g['sum']['requests'],
                'page_views': g['sum']['pageViews'],
                'uniques': g['uniq']['uniques'],
                'bandwidth_mb': round(g['sum']['bytes'] / 1024 / 1024, 1),
                'threats': g['sum']['threats'],
                'date': g['dimensions']['date']
            }
    return None

def format_duration(seconds):
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m}m {s}s"

def send_report():
    today = datetime.now(timezone.utc).strftime("%A, %B %d %Y")
    
    ga4 = get_ga4_data()
    cf = get_cf_data()
    
    lines = [f"*[ECF] errorcodefixes.com Daily Report - {today}*\n"]
    
    if ga4 and ga4.get('yesterday'):
        y = ga4['yesterday']
        w = ga4.get('week', {})
        lines.append("*GA4 — Yesterday*")
        lines.append(f"• Sessions: *{y['sessions']:,}*")
        lines.append(f"• Users: *{y['users']:,}*")
        lines.append(f"• Page Views: *{y['pageviews']:,}*")
        lines.append(f"• Bounce Rate: *{y['bounce_rate']:.1%}*")
        lines.append(f"• Avg Session: *{format_duration(y['avg_duration'])}*")
        
        if w:
            lines.append(f"\n*GA4 — Last 7 Days*")
            lines.append(f"• Sessions: *{w['sessions']:,}* | Users: *{w['users']:,}* | Views: *{w['pageviews']:,}*")
    else:
        lines.append("*GA4:* No data yet for yesterday")
    
    if cf:
        lines.append(f"\n*Cloudflare — Yesterday ({cf.get('date', '')})*")
        lines.append(f"• Requests: *{cf['requests']:,}* | Unique IPs: *{cf['uniques']:,}*")
        lines.append(f"• Page Views: *{cf['page_views']:,}* | Bandwidth: *{cf['bandwidth_mb']} MB*")
        if cf['threats'] > 0:
            lines.append(f"• ⚠️ Threats blocked: {cf['threats']}")
    
    if ga4 and ga4.get('top_pages'):
        lines.append("\n*Top Pages (yesterday)*")
        for p in ga4['top_pages'][:5]:
            lines.append(f"• `{p['path']}` — {p['views']:,} views")
    
    if ga4 and ga4.get('sources'):
        lines.append("\n*Traffic Sources (yesterday)*")
        for s in ga4['sources']:
            lines.append(f"• {s['channel']}: {s['sessions']:,} sessions")
    
    message = "\n".join(lines)
    
    # Post to Slack
    r = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}", "Content-Type": "application/json"},
        json={"channel": SLACK_CHANNEL, "text": message, "mrkdwn": True}
    )
    result = r.json()
    if result.get('ok'):
        print("Report posted to Slack successfully")
    else:
        print(f"Slack error: {result.get('error')}")
        print(message)

if __name__ == "__main__":
    send_report()
