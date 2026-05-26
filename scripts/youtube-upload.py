#!/usr/bin/env python3
"""
YouTube Shorts auto-uploader.

Uploads MP4s from growth-pipeline/shorts/videos/ to the errorcodefixes
YouTube channel via the YouTube Data API v3, paced at N/day. Pulls
title/description/tags from the matching shorts script .md, sets the
thumbnail from growth-pipeline/shorts/thumbnails/{slug}.png, and tags
#Shorts so YouTube classifies it correctly.

Tracks posted videos in growth-pipeline/shorts/posted.json.

REQUIRES (in env):
    YOUTUBE_CLIENT_ID
    YOUTUBE_CLIENT_SECRET
    YOUTUBE_REFRESH_TOKEN   (from one-time OAuth flow; scope youtube.upload)

USAGE:
    python scripts/youtube-upload.py --count 1
    python scripts/youtube-upload.py --count 1 --dry
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTS_DIR = ROOT / "growth-pipeline" / "shorts"
VIDEO_DIR = SHORTS_DIR / "videos"
THUMB_DIR = SHORTS_DIR / "thumbnails"
STATE = SHORTS_DIR / "posted.json"

CLIENT_ID = os.environ.get("YOUTUBE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("YOUTUBE_CLIENT_SECRET", "")
REFRESH_TOKEN = os.environ.get("YOUTUBE_REFRESH_TOKEN", "")


def access_token() -> str:
    """Exchange the long-lived refresh token for a short-lived access token."""
    data = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["access_token"]


def parse_script(slug: str) -> dict:
    """Pull title/description/tags from the shorts script .md for this slug."""
    for md in sorted(SHORTS_DIR.glob(f"*_{slug}.md"), reverse=True):
        text = md.read_text(encoding="utf-8")
        title_m = re.match(r"^# YouTube Short [—–-] (.+)", text)
        title = title_m.group(1).strip() if title_m else slug.replace("-", " ").title()
        desc_m = re.search(r"## Description block.*?```\s*\n(.*?)```", text, re.DOTALL)
        desc = desc_m.group(1).strip() if desc_m else ""
        tags = re.findall(r"#(\w+)", desc)
        return {"title": (title + " #Shorts")[:100], "description": desc, "tags": tags}
    title = slug.replace("-", " ").title()
    return {"title": (title + " #Shorts")[:100],
            "description": f"Fix guide: https://errorcodefixes.com/posts/{slug}/",
            "tags": ["Shorts", "Repair", "ErrorCode"]}


def load_state() -> dict:
    return json.loads(STATE.read_text()) if STATE.exists() else {"posted": {}}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2))


def upload(slug: str, token: str, dry: bool) -> bool:
    video = VIDEO_DIR / f"{slug}.mp4"
    if not video.exists():
        print(f"  [!] no video for {slug}")
        return False
    meta = parse_script(slug)
    print(f"  -> {slug}: {meta['title']}")
    if dry:
        print(f"     tags: {meta['tags'][:8]}")
        return True

    # Resumable upload: step 1 init
    init_body = json.dumps({
        "snippet": {
            "title": meta["title"],
            "description": meta["description"],
            "tags": meta["tags"][:15],
            "categoryId": "26",  # Howto & Style
        },
        "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False},
    }).encode()
    init_req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        data=init_body, method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Upload-Content-Type": "video/mp4",
        },
    )
    try:
        with urllib.request.urlopen(init_req, timeout=30) as r:
            upload_url = r.headers["Location"]
        # step 2 upload bytes
        vbytes = video.read_bytes()
        up_req = urllib.request.Request(
            upload_url, data=vbytes, method="PUT",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "video/mp4",
                     "Content-Length": str(len(vbytes))},
        )
        with urllib.request.urlopen(up_req, timeout=300) as r:
            res = json.load(r)
        vid = res.get("id")
        print(f"     uploaded video id: {vid}")
        # step 3 thumbnail (best-effort)
        thumb = THUMB_DIR / f"{slug}.png"
        if vid and thumb.exists():
            tb = thumb.read_bytes()
            treq = urllib.request.Request(
                f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}",
                data=tb, method="POST",
                headers={"Authorization": f"Bearer {token}", "Content-Type": "image/png"},
            )
            try:
                urllib.request.urlopen(treq, timeout=60)
                print("     thumbnail set")
            except Exception as e:
                print(f"     thumbnail skip: {e}")
        return True
    except Exception as e:
        print(f"     FAIL: {e}")
        return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    if not (CLIENT_ID and CLIENT_SECRET and REFRESH_TOKEN):
        print("[!] YouTube OAuth env not set (YOUTUBE_CLIENT_ID / _SECRET / _REFRESH_TOKEN).")
        return 1

    token = "DRY" if args.dry else access_token()
    state = load_state()
    all_slugs = sorted(p.stem for p in VIDEO_DIR.glob("*.mp4"))
    queue = [s for s in all_slugs if s not in state["posted"]]
    print(f"[i] {len(queue)} unposted / {len(all_slugs)} total videos")

    posted = 0
    for slug in queue[: args.count]:
        if upload(slug, token, args.dry):
            if not args.dry:
                state["posted"][slug] = date.today().isoformat()
                posted += 1
    if not args.dry:
        save_state(state)
        print(f"\n[+] Uploaded {posted}. {len(queue) - posted} remain.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
