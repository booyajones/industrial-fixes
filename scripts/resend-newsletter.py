#!/usr/bin/env python3
"""
Resend Broadcasts weekly digest publisher.

Reads the latest growth-pipeline/newsletters/*_digest.md and pushes it as a
Broadcast to the errorcodefixes "General" audience via the Resend API, then
(optionally) sends it. Replaces the Beehiiv publisher: Beehiiv gates post
creation behind its Enterprise plan, Resend Broadcasts is free and fully
programmatic, and we already own the verified errorcodefixes.com domain.

REQUIRES (in env):
    RESEND_API_KEY        re_...  (already in ecf.env)
    RESEND_AUDIENCE_ID    audience to send to (defaults to the "General" audience)

USAGE:
    python scripts/resend-newsletter.py --dry          # parse + preview only
    python scripts/resend-newsletter.py                # create broadcast (no send)
    python scripts/resend-newsletter.py --send         # create + send to the audience
    python scripts/resend-newsletter.py --test a@b.com # one-off test email to one address
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NL_DIR = ROOT / "growth-pipeline" / "newsletters"
SENT_STATE = NL_DIR / "sent.json"
API = "https://api.resend.com"
# A browser-ish UA: api.resend.com sits behind Cloudflare, which 1010-blocks
# the default python-urllib user-agent.
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ecf-newsletter/1.0"

API_KEY = os.environ.get("RESEND_API_KEY", "")
AUDIENCE_ID = os.environ.get("RESEND_AUDIENCE_ID", "e938e0f3-b84c-4191-a259-eca477f59369")
FROM_ADDR = os.environ.get("RESEND_NEWSLETTER_FROM",
                           "Industrial Error Code Fixes <newsletter@errorcodefixes.com>")
REPLY_TO = os.environ.get("RESEND_NEWSLETTER_REPLY_TO", "frank@errorcodefixes.com")


def call(method: str, path: str, body: dict | None = None) -> tuple[int, dict | str]:
    url = f"{API}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json",
                 "User-Agent": UA, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raw = e.read().decode()[:600]
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw


def latest_digest() -> Path:
    files = sorted(NL_DIR.glob("*_digest.md"), reverse=True)
    if not files:
        raise SystemExit("[!] No digest .md found in growth-pipeline/newsletters/")
    return files[0]


def parse_digest(md: Path) -> dict:
    text = md.read_text(encoding="utf-8")
    subj_m = re.search(r"^\d+\.\s+\*\*(.+?)\*\*", text, re.MULTILINE)
    subject = subj_m.group(1).strip() if subj_m else "This week on errorcodefixes.com"
    pre_m = re.search(r"## Preheader text\s*\n+>\s*(.+)", text)
    preheader = pre_m.group(1).strip() if pre_m else ""
    body_m = re.search(r"## Newsletter body.*?\n(.*?)(?:\n## |\Z)", text, re.DOTALL)
    body_md = body_m.group(1).strip() if body_m else text
    return {"subject": subject, "preheader": preheader, "html": md_to_html(body_md)}


def md_to_html(md: str) -> str:
    """Minimal markdown -> HTML, wrapped so Resend renders a clean email."""
    out = []
    in_list = False
    for line in md.splitlines():
        line = line.rstrip()
        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("")
            continue
        if line.startswith("### "):
            if in_list:
                out.append("</ul>"); in_list = False
            out.append(f"<h3>{line[4:]}</h3>"); continue
        if line.startswith("## "):
            if in_list:
                out.append("</ul>"); in_list = False
            out.append(f"<h2>{line[3:]}</h2>"); continue
        m = re.match(r"^[-*]\s+(.*)", line)
        content = m.group(1) if m else line
        content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', content)
        content = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", content)
        if m:
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{content}</li>")
        else:
            if in_list:
                out.append("</ul>"); in_list = False
            out.append(f"<p>{content}</p>")
    if in_list:
        out.append("</ul>")
    inner = "\n".join(out)
    return (
        '<div style="font-family:Arial,Helvetica,sans-serif;max-width:600px;'
        'margin:0 auto;color:#1c1917;line-height:1.55;font-size:15px">'
        f"{inner}"
        '<hr style="border:none;border-top:1px solid #e7e5e4;margin:24px 0">'
        '<p style="font-size:12px;color:#78716c">You are receiving this because '
        'you subscribed at errorcodefixes.com. '
        '<a href="{{{RESEND_UNSUBSCRIBE_URL}}}">Unsubscribe</a>.</p>'
        "</div>"
    )


def create_broadcast(d: dict) -> str:
    body = {
        "audience_id": AUDIENCE_ID,
        "from": FROM_ADDR,
        "reply_to": REPLY_TO,
        "subject": d["subject"],
        "name": f"Weekly digest — {d['subject']}"[:191],
        "html": d["html"],
    }
    if d.get("preheader"):
        body["preview_text"] = d["preheader"][:200]
    status, res = call("POST", "/broadcasts", body)
    if status not in (200, 201) or not isinstance(res, dict) or not res.get("id"):
        raise SystemExit(f"[!] broadcast create failed ({status}): {res}")
    return res["id"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="parse + preview, create nothing")
    ap.add_argument("--send", action="store_true", help="send the broadcast to the audience")
    ap.add_argument("--test", metavar="EMAIL", help="send a one-off test email to one address")
    args = ap.parse_args()

    if not API_KEY:
        print("[!] RESEND_API_KEY not set."); return 1

    digest_path = latest_digest()
    d = parse_digest(digest_path)
    print(f"[i] subject:  {d['subject']}")
    print(f"[i] body html: {len(d['html'])} chars")
    print(f"[i] from:     {FROM_ADDR}")
    print(f"[i] audience: {AUDIENCE_ID}")

    if args.dry:
        print("\n" + d["html"][:500])
        return 0

    if args.test:
        status, res = call("POST", "/emails", {
            "from": FROM_ADDR, "to": [args.test], "reply_to": REPLY_TO,
            "subject": f"[TEST] {d['subject']}", "html": d["html"],
        })
        print(f"[{'+' if status in (200,201) else '!'}] test send -> {args.test}: {status} {res}")
        return 0 if status in (200, 201) else 1

    # Idempotency: never re-broadcast a digest we already sent (weekly cron-safe).
    sent = json.loads(SENT_STATE.read_text()) if SENT_STATE.exists() else {}
    if args.send and digest_path.name in sent:
        print(f"[i] {digest_path.name} already sent ({sent[digest_path.name]}). Nothing to do.")
        return 0

    bid = create_broadcast(d)
    print(f"[+] broadcast created: {bid}")

    if args.send:
        status, res = call("POST", f"/broadcasts/{bid}/send", {})
        if status in (200, 201):
            print(f"[+] broadcast SENT to audience {AUDIENCE_ID}")
            sent[digest_path.name] = {"broadcast_id": bid, "sent_at": __import__("datetime").date.today().isoformat()}
            SENT_STATE.write_text(json.dumps(sent, indent=2))
            return 0
        print(f"[!] send failed ({status}): {res}")
        return 1

    print("[i] not sent (no --send). Broadcast saved as draft in Resend.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
