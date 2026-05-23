#!/usr/bin/env python3
"""
Create Gmail drafts via IMAP APPEND.

Reads the latest backlink outreach drafts markdown and pushes each as a
draft into Chris's Gmail Drafts folder. He reviews + clicks Send.

USAGE:
    python scripts/create-gmail-drafts.py
"""

from __future__ import annotations

import email.utils
import imaplib
import os
import re
import time
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTREACH = ROOT / "growth-pipeline" / "outreach"
GMAIL_USER = os.environ.get("GMAIL_USER", "booyajones222@gmail.com")
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]


def parse_drafts(md_path: Path) -> list[dict]:
    """Pull every {subject, body, recipient_domain, prospect_url} from drafts.md."""
    text = md_path.read_text(encoding="utf-8")
    sections = re.split(r"^## \d+\. ", text, flags=re.MULTILINE)[1:]
    drafts = []
    for s in sections:
        # Section header: "<domain> — <topic>\n\n**Page:** <url>\n..."
        first_line = s.splitlines()[0].strip()
        domain = first_line.split(" ")[0].strip()
        url_m = re.search(r"\*\*Page:\*\*\s*(\S+)", s)
        page_url = url_m.group(1) if url_m else ""
        # Pull subject + body out of the fenced ``` block.
        block = re.search(r"```\s*\n(.+?)\n```", s, re.DOTALL)
        if not block:
            continue
        raw = block.group(1)
        subj_m = re.match(r"Subject:\s*(.+)", raw)
        subject = subj_m.group(1).strip() if subj_m else "Resource for your page"
        body = raw.split("\n", 1)[1].strip() if "\n" in raw else raw
        drafts.append({
            "domain": domain,
            "page": page_url,
            "subject": subject,
            "body": body,
        })
    return drafts


def latest_drafts_md() -> Path:
    """Pick the newest drafts file that has actual content (>1KB)."""
    files = sorted(OUTREACH.glob("*_outreach_drafts.md"), reverse=True)
    for f in files:
        if f.stat().st_size > 2000:
            return f
    raise SystemExit("[!] No non-empty outreach drafts found")


def main() -> int:
    md_path = latest_drafts_md()
    print(f"[i] Reading drafts from: {md_path.name}")
    drafts = parse_drafts(md_path)
    print(f"[i] Parsed {len(drafts)} drafts")

    # Connect to Gmail IMAP
    print(f"[i] Connecting to imap.gmail.com as {GMAIL_USER}")
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    M.select('"[Gmail]/Drafts"')

    pushed = 0
    skipped = 0
    for d in drafts:
        # Body is the human-edit version with placeholder TO.
        # We don't know the prospect's email — leave TO empty for Chris to fill.
        # But we CAN annotate the body with the prospect domain and page URL.
        annotated_body = (
            f"[Auto-drafted by Claude. Find the right contact at {d['domain']} "
            f"and replace TO. Page they curate: {d['page']}]\n\n"
            f"{d['body']}\n\n"
            f"--\nDrafted automatically by errorcodefixes growth pipeline.\n"
        )

        msg = EmailMessage()
        msg["From"] = GMAIL_USER
        msg["To"] = f"contact@{d['domain']}"   # placeholder Chris edits
        msg["Subject"] = d["subject"]
        msg["Date"] = email.utils.formatdate(localtime=True)
        msg.set_content(annotated_body)

        try:
            M.append(
                '"[Gmail]/Drafts"',
                r"(\Draft)",
                imaplib.Time2Internaldate(time.time()),
                str(msg).encode("utf-8"),
            )
            pushed += 1
            print(f"  [+] Draft #{pushed}: {d['domain']}  subj={d['subject'][:50]}")
        except Exception as e:
            skipped += 1
            print(f"  [!] Skipped {d['domain']}: {e}")

    M.close()
    M.logout()
    print(f"\n[+] DONE. {pushed} drafts created in {GMAIL_USER}, {skipped} skipped.")
    print(f"[i] Chris: open Gmail -> Drafts. Each draft has the prospect domain")
    print(f"    annotated at top. Find contact email, replace TO field, hit Send.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
