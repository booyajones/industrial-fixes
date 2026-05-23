#!/usr/bin/env python3
"""
Delete the 25 generic backlink-outreach drafts I (claude) created earlier,
identified by their distinctive auto-drafted preamble. Leaves any real
Chris-authored drafts untouched.
"""

import imaplib
import os

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
MARKER = "[Auto-drafted by Claude. Find the right contact at"


def main() -> int:
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(GMAIL_USER, GMAIL_PASSWORD)
    M.select('"[Gmail]/Drafts"')

    # Search for messages containing the auto-drafted preamble
    typ, data = M.search(None, 'BODY', f'"{MARKER}"')
    if typ != "OK":
        print("[!] Search failed")
        return 1
    ids = data[0].split()
    print(f"[i] Found {len(ids)} generic auto-drafts to delete")

    for uid in ids:
        M.store(uid, "+FLAGS", "\\Deleted")
    M.expunge()
    M.close()
    M.logout()
    print(f"[+] Deleted {len(ids)} generic drafts. Drafts inbox is clean.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
