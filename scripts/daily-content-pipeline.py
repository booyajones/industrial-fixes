#!/usr/bin/env python3
"""
Daily auto-content pipeline.

Detects any article published or modified in the last N days that does
NOT yet have a Pinterest pin image, a Shorts MP4, or a YouTube thumbnail.
For each missing piece, runs the appropriate generator.

Designed to run as a daily cron (6am ET via Windows Task Scheduler).
Each run is idempotent — re-running won't regenerate existing artifacts
unless --force is passed.

USAGE:
    python scripts/daily-content-pipeline.py            # last 7 days, gen anything missing
    python scripts/daily-content-pipeline.py --days 30
    python scripts/daily-content-pipeline.py --slug carrier-13-error-code
    python scripts/daily-content-pipeline.py --dry      # report what would gen, don't do it
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "src" / "data" / "blog"
SHORTS_DIR = ROOT / "growth-pipeline" / "shorts"
SHORTS_VIDEO_DIR = SHORTS_DIR / "videos"
SHORTS_THUMB_DIR = SHORTS_DIR / "thumbnails"
PIN_IMG_DIR = ROOT / "growth-pipeline" / "pinterest" / "images"

PY = sys.executable


def article_date(md_path: Path) -> datetime:
    """Most recent of pubDatetime / modDatetime from frontmatter."""
    text = md_path.read_text(encoding="utf-8", errors="replace")
    fm = re.search(r"^---\s*\n(.*?)^---", text, re.DOTALL | re.MULTILINE)
    if not fm:
        return datetime.now(timezone.utc)
    block = fm.group(1)
    dates = []
    for field in ("pubDatetime", "modDatetime"):
        m = re.search(rf"^{field}:\s*(.+)$", block, re.MULTILINE)
        if m:
            v = m.group(1).strip().strip('"').strip("'")
            try:
                if v.endswith("Z"):
                    dates.append(datetime.fromisoformat(v.replace("Z", "+00:00")))
                else:
                    dates.append(datetime.fromisoformat(v))
            except Exception:
                pass
    return max(dates) if dates else datetime.now(timezone.utc)


def run(cmd: list[str], dry: bool = False) -> bool:
    """Run a subprocess; return True on success."""
    print(f"    $ {' '.join(cmd)}")
    if dry:
        return True
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"      FAIL ({r.returncode}):  {r.stderr.strip()[:300]}")
        return False
    return True


def need(slug: str, kind: str) -> bool:
    """Does this artifact need to be generated?"""
    if kind == "shorts_script":
        # Look for any *_<slug>.md in SHORTS_DIR
        return not any(SHORTS_DIR.glob(f"*_{slug}.md"))
    if kind == "shorts_video":
        return not (SHORTS_VIDEO_DIR / f"{slug}.mp4").exists()
    if kind == "shorts_thumb":
        return not (SHORTS_THUMB_DIR / f"{slug}.png").exists()
    if kind == "pin_image":
        return not (PIN_IMG_DIR / f"{slug}.png").exists()
    return False


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=7, help="article freshness window")
    p.add_argument("--slug", help="single article slug")
    p.add_argument("--dry", action="store_true")
    p.add_argument("--limit", type=int, default=20, help="max articles per run")
    p.add_argument("--no-video", action="store_true", help="skip MP4 generation (expensive)")
    args = p.parse_args()

    if args.slug:
        targets = [BLOG_DIR / f"{args.slug}.md"]
        if not targets[0].exists():
            print(f"[!] article not found: {args.slug}")
            return 1
    else:
        cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
        candidates = []
        for md in BLOG_DIR.glob("*.md"):
            try:
                d = article_date(md)
                if d.tzinfo is None:
                    d = d.replace(tzinfo=timezone.utc)
                if d >= cutoff:
                    candidates.append((d, md))
            except Exception:
                continue
        candidates.sort(reverse=True)
        targets = [m for _, m in candidates[: args.limit]]

    print(f"[i] {len(targets)} candidate article(s)")

    total = {"shorts_script": 0, "shorts_video": 0, "shorts_thumb": 0, "pin_image": 0}
    for md in targets:
        slug = md.stem
        missing = [k for k in ("shorts_script", "pin_image", "shorts_thumb", "shorts_video") if need(slug, k)]
        if not missing:
            continue
        print(f"\n  -> {slug}  needs: {', '.join(missing)}")

        # 1. Shorts script (cheap, no API)
        if "shorts_script" in missing:
            if run([PY, "scripts/shorts-script-gen.py", "--slug", slug], dry=args.dry):
                total["shorts_script"] += 1

        # 2. Pinterest pin image — pinterest-pin-image-gen reads from a pin .md
        # The simpler path: render directly from article title. We synthesize
        # a single-pin .md on the fly and feed it. Or build a 1-pin path.
        if "pin_image" in missing:
            # Use single-slug subprocess to render just this pin
            tmp_md = SHORTS_DIR / "_tmp" / f"_pin_{slug}.md"
            tmp_md.parent.mkdir(parents=True, exist_ok=True)
            # Read article title from frontmatter
            article_text = md.read_text(encoding="utf-8", errors="replace")
            title_m = re.search(r'^title:\s*"?([^"\n]+)"?', article_text, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else slug.replace("-", " ").title()
            tmp_md.write_text(
                f"# Pin batch (auto)\n\n**Pin 1: {title}**\n"
                f"- **Destination URL:** https://errorcodefixes.com/posts/{slug}/\n",
                encoding="utf-8",
            )
            if run([PY, "scripts/pinterest-pin-image-gen.py", "--pins", str(tmp_md)], dry=args.dry):
                total["pin_image"] += 1

        # 3. YouTube thumbnail (cheap, no API) — needs script .md
        if "shorts_thumb" in missing and not need(slug, "shorts_script"):
            if run([PY, "scripts/youtube-thumbnail-gen.py", "--slug", slug], dry=args.dry):
                total["shorts_thumb"] += 1

        # 4. Shorts MP4 (ElevenLabs TTS — expensive; gated by --no-video)
        if "shorts_video" in missing and not args.no_video and not need(slug, "shorts_script"):
            if run([PY, "scripts/shorts-video-gen.py", "--slug", slug], dry=args.dry):
                total["shorts_video"] += 1

    print("\n[+] Summary:")
    for k, v in total.items():
        print(f"    {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
