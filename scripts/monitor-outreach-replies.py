#!/usr/bin/env python3
"""
Monitor Gmail inbox for replies to the backlink outreach emails.

Runs on a schedule (Windows Task ECF-Outreach-Replies). Each run:
  1. Connects to Gmail IMAP, opens INBOX
  2. Pulls every unread message from prospect domains in the CSV
  3. Categorizes: POSITIVE (likely accept), NEGATIVE (decline), AUTO (bounce
     or auto-reply), UNCLEAR (needs human read)
  4. Writes a per-domain note in the prospect CSV
  5. Posts a Slack/log summary so Chris sees the new replies quickly

USAGE:
    python scripts/monitor-outreach-replies.py
"""

from __future__ import annotations

import csv
import email
import imaplib
import os
import re
from datetime import date
from email.header import decode_header
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSPECT_CSV = ROOT / "growth-pipeline" / "outreach" / "2026-05-22_prospects.csv"
REPLY_LOG = ROOT / "growth-pipeline" / "outreach" / "reply-log.md"
GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

POSITIVE_HINTS = [
    "happy to", "would love", "sure", "added", "great resource",
    "we'll include", "we'll add", "good fit", "looks useful",
    "yes,", "yes please", "send over", "sounds good",
]
NEGATIVE_HINTS = [
    "no thanks", "not a fit", "not interested", "we don't",
    "unfortunately", "decline", "pass", "no longer",
    "stopped accepting", "no new links", "guest post",
]
AUTO_HINTS = [
    "out of office", "auto-reply", "automatic reply",
    "undeliverable", "address not found", "delivery status",
    "mailer-daemon", "delivery failure", "could not be delivered",
    "rejected", "bounced",
]


def decode_subject(raw: str) -> str:
    if not raw:
        return ""
    parts = decode_header(raw)
    out = []
    for chunk, enc in parts:
        if isinstance(chunk, bytes):
            try:
                out.append(chunk.decode(enc or "utf-8", errors="replace"))
            except LookupError:
                out.append(chunk.decode("utf-8", errors="replace"))
        else:
            out.append(chunk)
    return "".join(out)


def categorize(subject: str, body: str) -> str:
    text = (subject + " " + body).lower()
    if any(h in text for h in AUTO_HINTS):
        return "AUTO"
    if any(h in text for h in POSITIVE_HINTS):
        return "POSITIVE"
    if any(h in text for h in NEGATIVE_HINTS):
        return "NEGATIVE"
    return "UNCLEAR"


def get_prospect_domains() -> set[str]:
    if not PROSPECT_CSV.exists():
        return set()
    domains = set()
    with open(PROSPECT_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("outreach_status") == "sent":
                domains.add(row["domain"])
    return domains


def body_text(msg) -> str:
    """Return decoded plain-text body of an email.message.Message."""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    return part.get_payload(decode=True).decode(
                        part.get_content_charset() or "utf-8", errors="replace"
                    )
                except Exception:
                    return ""
        return ""
    try:
        return msg.get_payload(decode=True).decode(
            msg.get_content_charset() or "utf-8", errors="replace"
        )
    except Exception:
        return ""


def update_csv(domain: str, verdict: str, snippet: str) -> None:
    rows = []
    with open(PROSPECT_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row["domain"] == domain:
                row["reply_status"] = verdict
                row["notes"] = (snippet or "")[:200].replace("\n", " ")
            rows.append(row)
    with open(PROSPECT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_log(line: str) -> None:
    REPLY_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(REPLY_LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> int:
    domains = get_prospect_domains()
    if not domains:
        print("[i] No sent prospects in CSV")
        return 0

    print(f"[i] Checking inbox for replies from {len(domains)} prospect domains")
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(GMAIL_USER, GMAIL_PASSWORD)
    M.select("INBOX")

    today_iso = date.today().isoformat()
    seen_count = 0
    for d in domains:
        typ, data = M.search(None, f'(UNSEEN FROM "{d}")')
        if typ != "OK" or not data[0]:
            continue
        ids = data[0].split()
        for uid in ids:
            typ, raw = M.fetch(uid, "(RFC822)")
            if typ != "OK":
                continue
            msg = email.message_from_bytes(raw[0][1])
            subject = decode_subject(msg.get("Subject", ""))
            body = body_text(msg)
            verdict = categorize(subject, body)
            snippet = (body or "").strip().split("\n\n")[0][:300]

            update_csv(d, verdict, snippet)
            append_log(
                f"[{today_iso}] {verdict:<8}  {d}  subj=\"{subject[:60]}\""
            )
            print(f"  [+] {verdict:<8}  {d}  subj=\"{subject[:60]}\"")
            seen_count += 1

    M.close(); M.logout()
    print(f"\n[+] {seen_count} replies processed.")
    print(f"[i] CSV: {PROSPECT_CSV}")
    print(f"[i] Log: {REPLY_LOG}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
