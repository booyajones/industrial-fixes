#!/usr/bin/env python3
"""
Send personalized backlink outreach via Gmail SMTP.

Each email is hand-personalized with:
  - Real name where available
  - Page-specific reference detail
  - One concrete article from errorcodefixes.com matched to their audience
  - Real signature from Chris

Pacing: sends a configurable batch size, then exits. Re-run later for
the next batch. Tracks sent_date back to the prospect CSV.

USAGE:
    python scripts/send-personalized-outreach.py --batch 3       # send 3
    python scripts/send-personalized-outreach.py --batch 3 --dry # preview only
    python scripts/send-personalized-outreach.py --draft-only    # write drafts, no send
"""

from __future__ import annotations

import argparse
import csv
import imaplib
import os
import smtplib
import sys
import time
from datetime import date
from email.message import EmailMessage
from email.utils import formatdate
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSPECT_CSV = ROOT / "growth-pipeline" / "outreach" / "2026-05-22_prospects.csv"
GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
SENDER_NAME = "Chris Wyatt"

# Personalized prospect queue — hand-curated. Only the 10 realistic
# targets from the 25-prospect list. Manufacturers, large industry orgs,
# universities, and individual contractor sites stripped out.
PROSPECTS = [
    {
        "domain": "esub.com",
        "to_email": "contact@esub.com",
        "name": "",   # blog signed only "Admin"
        "subject": "Quick note re: your Top 15 HVAC Blogs list",
        "ref": "your Top 15 HVAC Blogs post for contractors and subcontractors",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "real Carrier furnace fault diagnosis with microamp readings and OEM part numbers",
    },
    {
        "domain": "getjobber.com",
        "to_email": "press@getjobber.com",
        "name": "Andrew",   # author Andrew Robichaud
        "subject": "Quick add for your Top 24 HVAC Blogs roundup",
        "ref": "your Top 24 HVAC Blogs roundup (2026 edition)",
        "article_path": "/posts/rinnai-error-code-11/",
        "article_pitch": "tankless water heater diagnostics with real microamp + flame-rod readings",
    },
    {
        "domain": "hvacknowitall.com",
        "to_email": "gary@hvacknowitall.com",
        "name": "Gary",
        "subject": "Resource for HVAC Know It All readers",
        "ref": "your General Guide to HVAC Troubleshooting post (loved the trades-detective framing)",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "fault-code-level diagnostics on the brands your readers see daily",
    },
    {
        "domain": "handoff.ai",
        "to_email": "hello@handoff.ai",
        "name": "Dmitry",
        "subject": "Reference for your HVAC troubleshooting post",
        "ref": "your HVAC troubleshooting guide on the Handoff blog",
        "article_path": "/posts/rinnai-error-code-11/",
        "article_pitch": "fault-code-specific repair guides that complement your general troubleshooting framework",
    },
    {
        "domain": "blog.sendwork.com",
        "to_email": "support@sendwork.com",
        "name": "",
        "subject": "Resource for your HVAC tips & resources category",
        "ref": "the HVAC Tips & Resources category on the SendWork blog",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "step-by-step fault-code diagnostics that contractor techs can pull up on a service call",
    },
    {
        "domain": "skillcatapp.com",
        "to_email": "contact@skillcatapp.com",
        "name": "",
        "subject": "Resource for SkillCat HVAC trainees",
        "ref": "your Online HVAC Training program",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "real-world fault-code references for techs in training",
    },
    {
        "domain": "hvactradeschools.org",
        "to_email": "admin@hvactradeschools.org",
        "name": "",
        "subject": "Resource add for your HVAC training program guide",
        "ref": "your 2026 Online HVAC Training Program Guide",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "fault-code diagnostic guides students can use as a real-world reference",
    },
    {
        "domain": "hvacredu.net",
        "to_email": "info@hvacredu.net",
        "name": "",
        "subject": "Resource for HVACRedu trainees",
        "ref": "your online HVAC and refrigeration training program",
        "article_path": "/posts/hoshizaki-e7-error-code/",
        "article_pitch": "refrigeration and HVAC fault-code references your trainees can use post-graduation",
    },
    {
        "domain": "hvacrschool.com",
        "to_email": "info@hvacrschool.com",
        "name": "",
        "subject": "Resource for HVACR free training site",
        "ref": "your free HVAC and refrigeration training",
        "article_path": "/posts/hoshizaki-e7-error-code/",
        "article_pitch": "fault-code-level repair guides on both HVAC and commercial refrigeration",
    },
    {
        "domain": "hvaclearningcampus.com",
        "to_email": "info@hvaclearningcampus.com",
        "name": "",
        "subject": "Resource for HVAC Learning Campus",
        "ref": "your HVAC Learning Campus",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "real-world brand-and-code repair references for learners",
    },
    # Wave 2 — 2026-05-24
    {
        "domain": "generaltools.com",
        "to_email": "info@generaltools.com",
        "name": "",
        "subject": "Reference for your 10 Common HVAC Problems guide",
        "ref": "your '10 of the Most Common HVAC Problems and How to Fix Them' guide",
        "article_path": "/posts/carrier-13-error-code/",
        "article_pitch": "deeper brand-specific fault-code diagnostics that complement your general HVAC troubleshooting content",
    },
]


def build_body(p: dict) -> str:
    """Compose the email body. Plain, brief, no AI-tell phrasing."""
    greeting = f"Hi {p['name']},\n\n" if p["name"] else "Hi,\n\n"
    article = f"https://errorcodefixes.com{p['article_path']}"
    body = (
        f"{greeting}"
        f"I came across {p['ref']} and figured I'd send a quick note.\n\n"
        f"I run errorcodefixes.com, a free repair-guide site that covers "
        f"brand-specific HVAC, refrigeration, CNC, and VFD error codes. "
        f"Each guide is technician-written and includes OEM part numbers, "
        f"voltage and resistance test ranges, and step-by-step diagnostic "
        f"trees. No paywall, no email gate.\n\n"
        f"One that fits your audience: {article}\n"
        f"({p['article_pitch']}.)\n\n"
        f"If it's a fit, no pressure either way. I just figured if you "
        f"curate this kind of thing you'd want to know it exists.\n\n"
        f"Either way, thanks for keeping a useful resource page out there. "
        f"They're getting rarer.\n\n"
        f"Chris Wyatt\n"
        f"errorcodefixes.com\n"
    )
    return body


def send_one(p: dict, smtp: smtplib.SMTP_SSL, dry: bool = False) -> bool:
    body = build_body(p)
    msg = EmailMessage()
    msg["From"] = f"{SENDER_NAME} <{GMAIL_USER}>"
    msg["To"] = p["to_email"]
    msg["Subject"] = p["subject"]
    msg["Date"] = formatdate(localtime=True)
    msg["Reply-To"] = GMAIL_USER
    msg.set_content(body)

    print(f"\n  --- to: {p['to_email']}  subj: {p['subject']}")
    if dry:
        print(body[:200] + ("..." if len(body) > 200 else ""))
        return True
    try:
        smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"  [!] SEND FAIL: {e}")
        return False


def save_draft(p: dict, M: imaplib.IMAP4_SSL) -> bool:
    body = build_body(p)
    msg = EmailMessage()
    msg["From"] = GMAIL_USER
    msg["To"] = p["to_email"]
    msg["Subject"] = p["subject"]
    msg["Date"] = formatdate(localtime=True)
    msg.set_content(body)
    try:
        M.append('"[Gmail]/Drafts"', r"(\Draft)",
                 imaplib.Time2Internaldate(time.time()),
                 str(msg).encode("utf-8"))
        return True
    except Exception as e:
        print(f"  [!] DRAFT FAIL {p['domain']}: {e}")
        return False


def update_csv(domains_sent: list[str]) -> None:
    """Mark domains as sent in the prospect CSV."""
    today = date.today().isoformat()
    rows = []
    with open(PROSPECT_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["domain"] in domains_sent:
                row["outreach_status"] = "sent"
                row["sent_date"] = today
            rows.append(row)
    with open(PROSPECT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def already_sent(domain: str) -> bool:
    if not PROSPECT_CSV.exists():
        return False
    with open(PROSPECT_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["domain"] == domain and row.get("outreach_status") == "sent":
                return True
    return False


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--batch", type=int, default=3, help="how many to send this run")
    p.add_argument("--dry", action="store_true", help="preview, don't send")
    p.add_argument("--draft-only", action="store_true",
                   help="save as Gmail drafts, do not send")
    args = p.parse_args()

    queue = [p for p in PROSPECTS if not already_sent(p["domain"])]
    print(f"[i] {len(queue)} unsent prospects in queue")
    if not queue:
        print("[+] All prospects already sent. Nothing to do.")
        return 0

    batch = queue[: args.batch]
    print(f"[i] This run: {len(batch)} prospect(s)")

    if args.draft_only:
        M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        M.login(GMAIL_USER, GMAIL_PASSWORD)
        M.select('"[Gmail]/Drafts"')
        saved = 0
        for prospect in batch:
            if save_draft(prospect, M):
                saved += 1
                print(f"  [+] Draft: {prospect['domain']} -> {prospect['to_email']}")
        M.close(); M.logout()
        print(f"\n[+] {saved} drafts saved in {GMAIL_USER}.")
        return 0

    # Send via SMTP
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(GMAIL_USER, GMAIL_PASSWORD)
    sent_domains = []
    for prospect in batch:
        ok = send_one(prospect, smtp, dry=args.dry)
        if ok and not args.dry:
            sent_domains.append(prospect["domain"])
            time.sleep(15)   # courteous pacing between sends
    smtp.quit()

    if sent_domains:
        update_csv(sent_domains)
        print(f"\n[+] Sent {len(sent_domains)}. CSV updated. Run again later for next batch.")
    elif args.dry:
        print(f"\n[i] Dry run complete. {len(batch)} previewed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
