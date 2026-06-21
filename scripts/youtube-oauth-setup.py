#!/usr/bin/env python3
"""
One-time YouTube OAuth helper — the ONLY step that needs Chris.

Turns the YouTube upload pipeline from "blocked" to "running". After this
runs once, scripts/youtube-upload.py can post the 32 (and counting) rendered
fix-videos autonomously, paced N/day, each description linking errorcodefixes.com.

WHAT YOU NEED FIRST (2 minutes in the Google Cloud Console, one time):
  1. Go to https://console.cloud.google.com/  (sign in as the Google account
     that owns — or will own — the errorcodefixes YouTube channel).
  2. Pick or create a project (the existing "wyattplayground" project is fine).
  3. APIs & Services > Library > search "YouTube Data API v3" > ENABLE.
  4. APIs & Services > OAuth consent screen: set User Type = External, fill the
     app name (e.g. "ECF Uploader") + your email, SAVE. Under "Test users" add
     your own Google address. (No verification/publishing needed for test users.)
  5. APIs & Services > Credentials > Create Credentials > OAuth client ID >
     Application type = "Desktop app" > Create. Copy the Client ID + Client secret.

THEN RUN THIS:
    python scripts/youtube-oauth-setup.py --id <CLIENT_ID>
  You'll be prompted for the client secret (hidden input) so it never lands in
  your shell history or the process list. (Or set YOUTUBE_CLIENT_ID /
  YOUTUBE_CLIENT_SECRET in the env and run with no args.)

A browser opens, you click "Allow" on YOUR channel, and this prints +
appends all three YOUTUBE_* values to the master .env. That's it — the
uploader is then fully autonomous.

This uses a loopback redirect (http://127.0.0.1:PORT) so there is NO code to
copy/paste — the consent round-trips automatically.
"""

from __future__ import annotations

import argparse
import http.server
import json
import os
import secrets
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

SCOPE = "https://www.googleapis.com/auth/youtube.upload"
AUTH = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN = "https://oauth2.googleapis.com/token"
MASTER_ENV = Path(r"C:\Users\chris\OneDrive\Desktop\Claude\.env")


class _Catch(http.server.BaseHTTPRequestHandler):
    code = None
    state = None

    def do_GET(self):  # noqa: N802
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        code = (params.get("code") or [None])[0]
        got_state = (params.get("state") or [None])[0]
        # Ignore stray requests (favicon, etc.) that carry no code, and only
        # accept a code whose state matches — assigning before the state check
        # would let a forged localhost request inject a code.
        if not code:
            self.send_response(204)
            self.end_headers()
            return
        if got_state == _Catch.state:
            _Catch.code = code
            msg = "Authorized. You can close this tab and return to the terminal."
        else:
            msg = "State mismatch. Re-run the helper."
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(f"<html><body style='font-family:system-ui;padding:3rem'>"
                         f"<h2>{msg}</h2></body></html>".encode())

    def log_message(self, *a):  # silence default logging
        pass


def _free_port() -> int:
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", default=os.environ.get("YOUTUBE_CLIENT_ID", ""))
    ap.add_argument("--secret", default=os.environ.get("YOUTUBE_CLIENT_SECRET", ""),
                    help="Client secret. Omit to be prompted (keeps it out of argv / shell history).")
    args = ap.parse_args()

    if not args.id:
        print("ERROR: need a Client ID.\n"
              "       Create a 'Desktop app' OAuth client (see the steps at the top\n"
              "       of this file), then run:\n"
              "         python scripts/youtube-oauth-setup.py --id <ID>\n"
              "       (you'll be prompted for the secret).",
              file=sys.stderr)
        return 2

    if not args.secret:
        import getpass
        args.secret = getpass.getpass("Client secret (input hidden): ").strip()
    if not args.secret:
        print("ERROR: no client secret provided.", file=sys.stderr)
        return 2

    port = _free_port()
    redirect = f"http://127.0.0.1:{port}"
    _Catch.state = secrets.token_urlsafe(16)

    httpd = http.server.HTTPServer(("127.0.0.1", port), _Catch)

    def _serve():
        # Handle requests one at a time until the real callback (code + matching
        # state) lands — so a stray favicon request can't eat the single slot.
        while _Catch.code is None:
            httpd.handle_request()

    threading.Thread(target=_serve, daemon=True).start()

    url = AUTH + "?" + urllib.parse.urlencode({
        "client_id": args.id,
        "redirect_uri": redirect,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent",
        "state": _Catch.state,
    })
    print("Opening your browser to authorize the errorcodefixes channel...")
    print("If it doesn't open, paste this URL:\n  " + url + "\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass

    # Wait for the loopback handler to capture the code.
    import time
    for _ in range(300):  # up to 5 min
        if _Catch.code:
            break
        time.sleep(1)
    if not _Catch.code:
        print("Timed out waiting for authorization.", file=sys.stderr)
        return 1

    data = urllib.parse.urlencode({
        "code": _Catch.code,
        "client_id": args.id,
        "client_secret": args.secret,
        "redirect_uri": redirect,
        "grant_type": "authorization_code",
    }).encode()
    req = urllib.request.Request(TOKEN, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            tok = json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:400]
        print(f"Token exchange failed ({e.code}): {body}", file=sys.stderr)
        return 1
    refresh = tok.get("refresh_token")
    if not refresh:
        print("No refresh_token returned. Re-run (the helper forces prompt=consent, "
              "so this is rare — check the client is a Desktop app type).", file=sys.stderr)
        return 1

    print("\n=== SUCCESS — add these to your environment ===")
    print(f"YOUTUBE_CLIENT_ID={args.id}")
    print(f"YOUTUBE_CLIENT_SECRET={args.secret}")
    print(f"YOUTUBE_REFRESH_TOKEN={refresh}")

    # Append to master .env if not already present.
    try:
        existing = MASTER_ENV.read_text(encoding="utf-8") if MASTER_ENV.exists() else ""
        add = []
        for k, v in (("YOUTUBE_CLIENT_ID", args.id),
                     ("YOUTUBE_CLIENT_SECRET", args.secret),
                     ("YOUTUBE_REFRESH_TOKEN", refresh)):
            if not any(line.startswith(k + "=") for line in existing.splitlines()):
                add.append(f"{k}={v}")
        if add:
            with MASTER_ENV.open("a", encoding="utf-8") as f:
                f.write("\n# YouTube uploader (errorcodefixes) — added by youtube-oauth-setup.py\n")
                f.write("\n".join(add) + "\n")
            print(f"\nAppended {len(add)} var(s) to {MASTER_ENV}")
        else:
            print(f"\n{MASTER_ENV} already had these — nothing to add.")
    except Exception as e:
        print(f"\n(Could not write {MASTER_ENV}: {e} — copy the three lines above manually.)")

    print("\nNext: python scripts/youtube-upload.py --count 1 --dry   # confirm, then drop --dry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
