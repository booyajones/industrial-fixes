#!/usr/bin/env python3
"""
Beehiiv weekly digest publisher.

Reads the latest growth-pipeline/newsletters/*_digest.md and pushes it as
a draft (or scheduled/published) post to the errorcodefixes Beehiiv
publication via the Beehiiv API v2.

REQUIRES (in env):
    BEEHIIV_API_KEY          from app.beehiiv.com -> Settings -> Integrations
    BEEHIIV_PUBLICATION_ID   already in ecf.env (pub_2e4c7f50-...)

USAGE:
    python scripts/beehiiv-publish.py --status draft       # safe default
    python scripts/beehiiv-publish.py --status confirmed   # actually send
    python scripts/beehiiv-publish.py --dry
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NL_DIR = ROOT / "growth-pipeline" / "newsletters"
API = "https://api.beehiiv.com/v2"

API_KEY = os.environ.get("BEEHIIV_API_KEY", "")
PUB_ID = os.environ.get("BEEHIIV_PUBLICATION_ID_V2") or os.environ.get("BEEHIIV_PUBLICATION_ID", "")


def latest_digest() -> Path:
    files = sorted(NL_DIR.glob("*_digest.md"), reverse=True)
    if not files:
        raise SystemExit("[!] No digest .md found in growth-pipeline/newsletters/")
    return files[0]


def parse_digest(md: Path) -> dict:
    text = md.read_text(encoding="utf-8")
    # Subject: first numbered subject-line option
    subj_m = re.search(r"^\d+\.\s+\*\*(.+?)\*\*", text, re.MULTILINE)
    subject = subj_m.group(1).strip() if subj_m else "This week on errorcodefixes.com"
    # Preheader
    pre_m = re.search(r"## Preheader text\s*\n+>\s*(.+)", text)
    preheader = pre_m.group(1).strip() if pre_m else ""
    # Body: everything under "Newsletter body" heading
    body_m = re.search(r"## Newsletter body.*?\n(.*?)(?:\n## |\Z)", text, re.DOTALL)
    body_md = body_m.group(1).strip() if body_m else text
    # Convert the markdown links to simple HTML paragraphs
    html = md_to_html(body_md)
    return {"subject": subject, "preheader": preheader, "html": html}


def md_to_html(md: str) -> str:
    """Minimal markdown -> HTML for Beehiiv body."""
    out = []
    for line in md.splitlines():
        line = line.rstrip()
        if not line:
            out.append("")
            continue
        # headings
        if line.startswith("### "):
            out.append(f"<h3>{line[4:]}</h3>")
            continue
        if line.startswith("## "):
            out.append(f"<h2>{line[3:]}</h2>")
            continue
        # bullets with markdown links
        m = re.match(r"^[-*]\s+(.*)", line)
        content = m.group(1) if m else line
        # [text](url) -> <a>
        content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', content)
        # **bold**
        content = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", content)
        out.append(f"<li>{content}</li>" if m else f"<p>{content}</p>")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", default="draft", choices=["draft", "confirmed"],
                    help="draft = saved for review; confirmed = sends to list")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    if not API_KEY:
        print("[!] BEEHIIV_API_KEY not set. Get it at app.beehiiv.com -> Settings -> Integrations.")
        return 1

    digest = parse_digest(latest_digest())
    print(f"[i] subject: {digest['subject']}")
    print(f"[i] body html: {len(digest['html'])} chars")

    if args.dry:
        print(digest["html"][:500])
        return 0

    body = {
        "title": digest["subject"],
        "subtitle": digest["preheader"][:200],
        "body_content": digest["html"],
        "status": args.status,
        "email_settings": {"email_capture_type_override": "none"},
    }
    url = f"{API}/publications/{PUB_ID}/posts"
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.load(r)
        print(f"[+] Beehiiv post created: status={args.status}  id={res.get('data',{}).get('id','?')}")
        return 0
    except Exception as e:
        print(f"[!] FAIL: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
