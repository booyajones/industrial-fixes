#!/usr/bin/env python3
"""
Self-verify the Google service account as owner of errorcodefixes.com via DNS.

Background:
  Adding a service-account email through the GSC "Users and permissions"
  UI is blocked for Domain Properties (Google's directory-validator
  rejects non-Workspace emails). The clean workaround is to make the SA
  prove ownership itself via DNS TXT challenge, which the Site Verification
  API supports.

Flow:
  1. SA calls siteVerification.webResource.getToken with method=DNS_TXT
     and site={type: INET_DOMAIN, identifier: errorcodefixes.com}.
     Returns a `google-site-verification=...` token value.
  2. We add that TXT to the errorcodefixes.com zone via Cloudflare API
     using CLOUDFLARE_FULL_TOKEN.
  3. SA calls siteVerification.webResource.insert to register ownership.
     Google retries the DNS lookup; success returns 200.
  4. SA is now Owner on sc-domain:errorcodefixes.com.
  5. Sitemap submit (separate script) should now succeed.

PREREQUISITES:
  Site Verification API must be enabled on the SA's Cloud project.
  If not, getToken returns 403 with a clear message and a console URL.

USAGE:
    python scripts/gsc-self-verify.py
    python scripts/gsc-self-verify.py --cleanup   # remove the TXT record after
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

DOMAIN = "errorcodefixes.com"

CLOUDFLARE_API = "https://api.cloudflare.com/client/v4"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--cleanup", action="store_true",
                   help="After successful verification, delete the TXT record")
    args = p.parse_args()

    sa_path = os.environ.get("GSC_SERVICE_ACCOUNT_JSON",
                              r"C:\Users\Administrator\.claude\secrets\gsc-sa.json")
    cf_token = os.environ.get("CLOUDFLARE_FULL_TOKEN")
    if not Path(sa_path).exists():
        print(f"[!] SA JSON not found at {sa_path}")
        return 1
    if not cf_token:
        print("[!] CLOUDFLARE_FULL_TOKEN env var missing")
        return 1

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        import requests
    except ImportError:
        print("[!] pip install google-auth google-api-python-client requests")
        return 1

    creds = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=[
            "https://www.googleapis.com/auth/siteverification",
            "https://www.googleapis.com/auth/webmasters",
        ],
    )

    sv = build("siteVerification", "v1", credentials=creds)
    wm = build("searchconsole", "v1", credentials=creds)

    # 1. Get the TXT token
    print("[1/5] Requesting DNS TXT challenge token from Google...")
    try:
        token_resp = sv.webResource().getToken(body={
            "verificationMethod": "DNS_TXT",
            "site": {"type": "INET_DOMAIN", "identifier": DOMAIN},
        }).execute()
    except HttpError as e:
        msg = str(e)
        print(f"[!] getToken failed: {msg[:400]}")
        if "Site Verification API has not been used" in msg or "siteverification.googleapis.com" in msg:
            print("\n>>> Action required: enable Site Verification API")
            print(">>> https://console.developers.google.com/apis/api/siteverification.googleapis.com/overview?project=wyattplayground")
            print(">>> Click Enable, wait 60s, re-run this script.")
        return 2

    token = token_resp.get("token")
    method = token_resp.get("method")
    print(f"      token={token[:48]}...  method={method}")

    # 2. Find the Cloudflare zone ID for errorcodefixes.com
    print(f"[2/5] Looking up Cloudflare zone for {DOMAIN}...")
    cf_headers = {"Authorization": f"Bearer {cf_token}", "Content-Type": "application/json"}
    zr = requests.get(f"{CLOUDFLARE_API}/zones?name={DOMAIN}", headers=cf_headers, timeout=30)
    zr.raise_for_status()
    zones = zr.json().get("result", [])
    if not zones:
        print(f"[!] CF token cannot see zone {DOMAIN}")
        return 3
    zone_id = zones[0]["id"]
    print(f"      zone_id={zone_id}")

    # 3. Add the TXT record
    print("[3/5] Adding TXT record to Cloudflare DNS...")
    add_resp = requests.post(
        f"{CLOUDFLARE_API}/zones/{zone_id}/dns_records",
        headers=cf_headers,
        json={
            "type": "TXT",
            "name": DOMAIN,
            "content": token,
            "ttl": 60,
            "comment": "Google Search Console SA verification (gsc-self-verify.py)",
        },
        timeout=30,
    )
    if add_resp.status_code >= 400:
        body = add_resp.json()
        # Maybe it already exists from a prior run — fine
        if any("already exists" in (e.get("message") or "").lower()
               for e in body.get("errors") or []):
            print("      (TXT already present from prior run, continuing)")
            record_id = None
        else:
            print(f"[!] CF DNS create failed: {add_resp.status_code} {add_resp.text[:300]}")
            return 4
    else:
        record_id = add_resp.json()["result"]["id"]
        print(f"      record_id={record_id}")

    # 4. Wait for DNS propagation. Cloudflare's authoritative servers
    #    answer almost immediately, so 30s is plenty.
    print("[4/5] Waiting 30s for DNS propagation...")
    time.sleep(30)

    # 5. Tell Google to verify
    print("[5/5] Asking Google to verify ownership...")
    last_err = None
    for attempt in range(1, 4):
        try:
            ins = sv.webResource().insert(
                verificationMethod="DNS_TXT",
                body={"site": {"type": "INET_DOMAIN", "identifier": DOMAIN}},
            ).execute()
            print(f"      VERIFIED. id={ins.get('id')}  owners={ins.get('owners')}")
            break
        except HttpError as e:
            last_err = str(e)[:400]
            print(f"      attempt {attempt} failed, waiting 20s. ({last_err[:120]})")
            time.sleep(20)
    else:
        print(f"[!] Verification failed after 3 attempts: {last_err}")
        return 5

    # Confirm sitemap submit now works
    print("\n[+] Testing sitemap submit...")
    try:
        wm.sitemaps().submit(
            siteUrl=f"sc-domain:{DOMAIN}",
            feedpath=f"https://{DOMAIN}/sitemap-index.xml",
        ).execute()
        print("    sitemap submitted to Google Search Console")
    except HttpError as e:
        print(f"    sitemap submit failed: {str(e)[:200]}")

    if args.cleanup and record_id:
        print("\n[+] Cleaning up TXT record...")
        requests.delete(f"{CLOUDFLARE_API}/zones/{zone_id}/dns_records/{record_id}",
                        headers=cf_headers, timeout=30)
        print("    TXT removed")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
