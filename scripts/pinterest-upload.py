#!/usr/bin/env python3
"""
Pinterest auto-uploader.

Posts pins from growth-pipeline/pinterest/images/ to the errorcodefixes
Pinterest business account via the Pinterest API v5, paced at N pins/day.
Tracks what's been posted in growth-pipeline/pinterest/posted.json so it
never double-posts and so it picks up where it left off each day.

REQUIRES (in env):
    PINTEREST_ACCESS_TOKEN   OAuth token with scope pins:write,boards:read
    PINTEREST_BOARD_ID       (optional) target board; auto-picks first if unset

Descriptions come from the matching pin .md (the pinterest-pin-batch.py
output) so each post has the keyword-tuned description + hashtags.

USAGE:
    python scripts/pinterest-upload.py --count 2          # post next 2
    python scripts/pinterest-upload.py --count 2 --dry    # preview only
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN_DIR = ROOT / "growth-pipeline" / "pinterest"
IMG_DIR = PIN_DIR / "images"
STATE = PIN_DIR / "posted.json"
API = "https://api.pinterest.com/v5"

TOKEN = os.environ.get("PINTEREST_ACCESS_TOKEN", "")
BOARD_ID = os.environ.get("PINTEREST_BOARD_ID", "")


def api(method: str, path: str, body: dict | None = None) -> dict:
    url = f"{API}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def pick_board() -> str:
    if BOARD_ID:
        return BOARD_ID
    boards = api("GET", "/boards?page_size=25").get("items", [])
    if not boards:
        raise SystemExit("[!] No boards on the account. Create one in Pinterest first.")
    # Prefer a board named like 'Error Codes' / 'Fix Guides' / 'HVAC'
    for b in boards:
        if re.search(r"error|fix|repair|hvac|guide", b.get("name", ""), re.I):
            return b["id"]
    return boards[0]["id"]


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"posted": {}, "last_run": None}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2))


def description_for(slug: str) -> tuple[str, str]:
    """Find the pin description + destination URL for a slug from any pins.md."""
    url = f"https://errorcodefixes.com/posts/{slug}/"
    desc = ""
    for md in sorted(PIN_DIR.glob("*_pins.md"), reverse=True):
        text = md.read_text(encoding="utf-8")
        m = re.search(
            rf"\*\*Description:\*\*\s*\n(.+?)(?:\n\n|\n\s+Save this)",
            text, re.DOTALL,
        )
        if slug in text and m:
            desc = m.group(1).strip()
            break
    if not desc:
        title = slug.replace("-", " ").title()
        desc = (f"{title}: technician-written fix guide with OEM part numbers, "
                f"voltage/resistance ranges, and step-by-step diagnosis. Free, "
                f"no paywall. #HVAC #Repair #ErrorCode #FixIt")
    return desc, url


def upload_pin(slug: str, board_id: str, dry: bool) -> bool:
    img_path = IMG_DIR / f"{slug}.png"
    if not img_path.exists():
        print(f"  [!] no image for {slug}")
        return False
    desc, link = description_for(slug)
    title = slug.replace("-", " ").title()[:100]
    print(f"  -> {slug}  (board {board_id})")
    if dry:
        print(f"     title: {title}")
        print(f"     desc:  {desc[:120]}...")
        print(f"     link:  {link}")
        return True
    b64 = base64.b64encode(img_path.read_bytes()).decode()
    body = {
        "board_id": board_id,
        "title": title,
        "description": desc[:800],
        "link": link,
        "media_source": {"source_type": "image_base64", "content_type": "image/png", "data": b64},
    }
    try:
        res = api("POST", "/pins", body)
        print(f"     posted pin id: {res.get('id')}")
        return True
    except Exception as e:
        print(f"     FAIL: {e}")
        return False


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=2, help="pins to post this run")
    p.add_argument("--dry", action="store_true")
    args = p.parse_args()

    if not TOKEN:
        print("[!] PINTEREST_ACCESS_TOKEN not set. Aborting.")
        print("    Get it from the OAuth flow once the Pinterest app exists.")
        return 1

    board_id = pick_board() if not args.dry else (BOARD_ID or "DRY_BOARD")
    state = load_state()
    all_slugs = sorted(p.stem for p in IMG_DIR.glob("*.png"))
    queue = [s for s in all_slugs if s not in state["posted"]]
    print(f"[i] {len(queue)} unposted / {len(all_slugs)} total pins")

    batch = queue[: args.count]
    posted = 0
    for slug in batch:
        if upload_pin(slug, board_id, args.dry):
            if not args.dry:
                state["posted"][slug] = date.today().isoformat()
                posted += 1
                time.sleep(8)   # polite pacing between API calls

    if not args.dry:
        state["last_run"] = date.today().isoformat()
        save_state(state)
        print(f"\n[+] Posted {posted} pins. {len(queue) - posted} remain in queue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
