#!/usr/bin/env python3
"""
Submit sitemap to Google Search Console via Webmasters API.

WHY:
  IndexNow pings Bing + Yandex but Google ignores IndexNow. Google reads
  sitemap.xml on its own crawl schedule, which can take weeks for new
  domains. Calling the Webmasters Sitemaps API explicitly tells Google
  "go crawl this", and the site rises from "5 organic visitors / 30d"
  in days instead of months.

PREREQUISITES:
  1. A Google Cloud project with the Search Console API enabled.
  2. A service account JSON key file with the Search Console Owner role.
  3. The service account's email added as an Owner of the
     `sc-domain:errorcodefixes.com` property in Search Console.
  4. Env var GSC_SERVICE_ACCOUNT_JSON pointing at the key file.

If those aren't set yet, the script prints exactly what to do and exits.
The fallback (still better than nothing) is to log into search.google.com/
search-console once a week and click Submit Sitemap manually.

USAGE:
    python scripts/submit-to-gsc.py
    python scripts/submit-to-gsc.py --sitemap https://errorcodefixes.com/sitemap-index.xml

This script is idempotent — Google will treat repeat submissions as
"already received" and won't penalize.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

SITE = "https://errorcodefixes.com"
# Use the URL-prefix property (https://errorcodefixes.com/) — that is the one
# the wyattbot-reader@wyattplayground.iam.gserviceaccount.com SA is verified
# Owner of. The sc-domain:errorcodefixes.com property exists separately but
# only Chris's personal Google account owns that one.
PROPERTY = "https://errorcodefixes.com/"
DEFAULT_SITEMAP = f"{SITE}/sitemap-index.xml"

SETUP_HELP = """
Google Search Console API submission is NOT YET SET UP on this host.

To enable autonomous sitemap submission, do this once:

  1. https://console.cloud.google.com → New project (or pick existing).
  2. APIs & Services → Library → search "Search Console API" → Enable.
  3. APIs & Services → Credentials → Create credentials → Service account.
     Name it "errorcodefixes-gsc-bot". Grant role "Owner" (or "Editor").
  4. After creation, click the service account → Keys → Add Key → JSON.
     Download the JSON file.
  5. Store it at C:\\Users\\Administrator\\.claude\\secrets\\gsc-sa.json
     and add to the ecf.env file:
       GSC_SERVICE_ACCOUNT_JSON=C:\\Users\\Administrator\\.claude\\secrets\\gsc-sa.json
  6. https://search.google.com/search-console → Settings → Users and permissions
     → Add user → paste the service-account email (ends in
     `.iam.gserviceaccount.com`) → role "Owner".
  7. Install: pip install google-auth google-api-python-client
  8. Re-run this script.

Manual fallback (no API needed): once a week, log into search console,
go to the Sitemaps section, and re-submit https://errorcodefixes.com/sitemap-index.xml.
That's a 30-second task. The API path is just nice-to-have automation.
"""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sitemap", default=DEFAULT_SITEMAP)
    p.add_argument("--property", default=PROPERTY)
    args = p.parse_args()

    sa_path = os.environ.get("GSC_SERVICE_ACCOUNT_JSON")
    if not sa_path or not Path(sa_path).exists():
        print(SETUP_HELP)
        return 0  # not an error — just not configured

    try:
        from google.oauth2 import service_account  # noqa: F401
        from googleapiclient.discovery import build
    except ImportError:
        print("[!] Missing deps. Install: pip install google-auth google-api-python-client")
        return 1

    creds = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=["https://www.googleapis.com/auth/webmasters"],
    )
    svc = build("searchconsole", "v1", credentials=creds)
    try:
        svc.sitemaps().submit(siteUrl=args.property, feedpath=args.sitemap).execute()
        print(f"[+] Submitted {args.sitemap} to {args.property}")
        # List recent status for confirmation
        resp = svc.sitemaps().list(siteUrl=args.property).execute()
        for s in resp.get("sitemap", []):
            print(f"    {s.get('path')}  lastSubmitted={s.get('lastSubmitted')}  isPending={s.get('isPending')}")
        return 0
    except Exception as e:
        print(f"[!] Submit failed: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
