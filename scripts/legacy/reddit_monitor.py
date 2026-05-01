"""
reddit_monitor.py - Scan Reddit for HVAC/equipment error code questions
and draft responses pointing to errorcodefixes.com articles.

Posts results to Slack #proj-industrial-code-errors for Chris to review and post manually.
Run daily via cron.
"""
import os
import json
import time
import re
import smtplib
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

# Use Exa for Reddit search since we don't have Reddit API creds
import subprocess
import sys

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN', '')
CHANNEL_ID = 'C0AQZ85MCEN'  # #proj-industrial-code-errors

# Search queries to find error code questions
SEARCH_QUERIES = [
    'site:reddit.com HVAC "error code" furnace OR "heat pump" fix help',
    'site:reddit.com r/hvacadvice "error code" furnace flashing',
    'site:reddit.com r/DIY furnace "error code" help fix',
    'site:reddit.com r/homeowners "error code" OR "fault code" HVAC',
    'site:reddit.com furnace "3 flashes" OR "4 flashes" OR "5 flashes" help',
    'site:reddit.com "heat pump" "fault code" OR "error code" not heating',
    'site:reddit.com tankless "error code" Navien OR Rinnai OR Bradford',
    'site:reddit.com "commercial refrigerator" "error code" OR "not cooling"',
]

# Map common error code patterns to our URLs
URL_MAP = {
    'carrier': 'https://errorcodefixes.com/brands/carrier/',
    'trane': 'https://errorcodefixes.com/brands/trane/',
    'lennox': 'https://errorcodefixes.com/brands/lennox/',
    'goodman': 'https://errorcodefixes.com/brands/goodman/',
    'rheem': 'https://errorcodefixes.com/brands/rheem/',
    'navien': 'https://errorcodefixes.com/brands/navien/',
    'rinnai': 'https://errorcodefixes.com/brands/rinnai/',
    'hoshizaki': 'https://errorcodefixes.com/brands/hoshizaki/',
    'mitsubishi': 'https://errorcodefixes.com/brands/mitsubishi/',
    'daikin': 'https://errorcodefixes.com/brands/daikin/',
    'furnace': 'https://errorcodefixes.com/posts/furnace-blowing-cold-air/',
    'heat pump': 'https://errorcodefixes.com/posts/heat-pump-not-heating/',
    'water heater': 'https://errorcodefixes.com/posts/water-heater-no-hot-water/',
}

def search_exa(query):
    """Use Exa API to search Reddit for error code questions."""
    api_key = os.environ.get('EXA_API_KEY', '')
    if not api_key:
        return []
    
    import urllib.request
    import json as jsonlib
    
    payload = json.dumps({
        "query": query,
        "numResults": 5,
        "type": "auto",
        "includeDomains": ["reddit.com"],
        "startPublishedDate": "2026-04-01T00:00:00Z"
    })
    
    req = urllib.request.Request(
        "https://api.exa.ai/search",
        data=payload.encode(),
        headers={
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = jsonlib.loads(response.read())
            return data.get('results', [])
    except Exception as e:
        print(f"Exa search error: {e}")
        return []

def find_relevant_url(title, body=""):
    """Find the most relevant errorcodefixes.com URL for a Reddit post."""
    text = (title + " " + body).lower()
    
    # Check for brand-specific
    for brand, url in URL_MAP.items():
        if brand in text:
            return url
    
    return "https://errorcodefixes.com"

def draft_response(post_title, post_url, relevant_url):
    """Draft a helpful Reddit response."""
    return (
        f"Here's a diagnostic guide that covers this: {relevant_url}\n\n"
        f"It walks through the most common causes in order of frequency, "
        f"with step-by-step checks. Should help you narrow it down before "
        f"calling a tech."
    )

def post_to_slack(opportunities):
    """Post found opportunities to Slack for Chris to review."""
    if not opportunities:
        return
    
    import urllib.request
    import json as jsonlib
    
    text = "*Reddit backlink opportunities - review and post these manually:*\n\n"
    
    for i, opp in enumerate(opportunities[:8], 1):
        text += (
            f"*{i}. {opp['title'][:80]}*\n"
            f"Reddit: {opp['url']}\n"
            f"*Suggested reply:*\n{opp['response']}\n\n"
        )
    
    text += "_Post these as your Reddit account (errorcodefixes doesn't have one). These are people actively asking for help._"
    
    payload = json.dumps({
        "channel": CHANNEL_ID,
        "text": text
    })
    
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload.encode(),
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read())
            if result.get('ok'):
                print(f"Posted {len(opportunities)} opportunities to Slack")
            else:
                print(f"Slack error: {result.get('error')}")
    except Exception as e:
        print(f"Slack post error: {e}")

def main():
    print(f"[{datetime.now(timezone.utc).isoformat()}] Starting Reddit monitor...")
    
    seen_urls = set()
    opportunities = []
    
    for query in SEARCH_QUERIES[:4]:  # Limit to 4 queries to save API credits
        print(f"Searching: {query[:60]}...")
        results = search_exa(query)
        
        for result in results:
            url = result.get('url', '')
            title = result.get('title', '')
            
            if url in seen_urls:
                continue
            if 'reddit.com' not in url:
                continue
            # Skip if it's just a brand page, not a question
            if '/wiki/' in url or '/r/HVAC/wiki' in url:
                continue
                
            seen_urls.add(url)
            
            relevant_url = find_relevant_url(title)
            response = draft_response(title, "", relevant_url)
            
            opportunities.append({
                "title": title,
                "url": url,
                "relevant_url": relevant_url,
                "response": response
            })
        
        time.sleep(1)
    
    print(f"Found {len(opportunities)} opportunities")
    
    if opportunities:
        post_to_slack(opportunities)
    else:
        print("No new opportunities found today")

if __name__ == "__main__":
    main()
