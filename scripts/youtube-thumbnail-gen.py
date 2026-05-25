#!/usr/bin/env python3
"""
YouTube thumbnail generator (1280x720).

Produces a clean branded thumbnail for each Shorts video. Saves to
growth-pipeline/shorts/thumbnails/{slug}.png so it can be uploaded as
the YouTube video thumbnail when publishing.

USAGE:
    python scripts/youtube-thumbnail-gen.py --slug rinnai-error-code-11
    python scripts/youtube-thumbnail-gen.py            # all videos
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SHORTS_DIR = ROOT / "growth-pipeline" / "shorts"
OUT_DIR = SHORTS_DIR / "thumbnails"
VIDEO_DIR = SHORTS_DIR / "videos"

W, H = 1280, 720
ACCENT = (217, 119, 6)
DARK = (24, 18, 10)
LIGHT = (250, 248, 244)
WHITE = (255, 255, 255)
TEXT_DARK = (32, 24, 12)
RED = (220, 38, 38)


def find_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    name = "arialbd.ttf" if bold else "arial.ttf"
    for p in [f"C:/Windows/Fonts/{name}", f"/usr/share/fonts/truetype/dejavu/{name}", name]:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines, cur = [], words[0]
    for w in words[1:]:
        trial = cur + " " + w
        if font.getbbox(trial)[2] - font.getbbox(trial)[0] > max_w:
            lines.append(cur); cur = w
        else:
            cur = trial
    lines.append(cur)
    return lines


def parse_thumbnail_copy(md_path: Path) -> tuple[str, str, str]:
    """Pull title + thumbnail top/bottom from the script .md."""
    text = md_path.read_text(encoding="utf-8")
    title_m = re.match(r"^# YouTube Short [—–-] (.+)", text)
    title = title_m.group(1).strip() if title_m else md_path.stem

    top, bot = "", ""
    tb = re.search(r"## Thumbnail copy.*?\*\*Top line:\*\*\s*(.+?)\n.*?\*\*Bottom line:\*\*\s*(.+?)$",
                   text, re.DOTALL | re.MULTILINE)
    if tb:
        top = tb.group(1).strip()
        bot = tb.group(2).strip().split("\n")[0].strip()

    if not top:
        # Synthesize from title — first 4 words
        words = title.split()
        top = " ".join(words[:4])
        bot = "FIX IT IN 60s"

    return title, top, bot


def render_thumbnail(top: str, bottom: str, slug: str) -> Image.Image:
    img = Image.new("RGB", (W, H), LIGHT)
    d = ImageDraw.Draw(img)

    # Left dark panel (40% of width)
    panel_w = int(W * 0.42)
    d.rectangle([(0, 0), (panel_w, H)], fill=DARK)

    # Brand bar across the top
    d.rectangle([(0, 0), (W, 80)], fill=ACCENT)
    bf = find_font(40)
    d.text((30, 22), "ERRORCODEFIXES.COM", fill=WHITE, font=bf)
    rb = find_font(28, bold=False)
    rb_txt = "60-Second Fix"
    rb_w = rb.getbbox(rb_txt)[2]
    d.text((W - rb_w - 30, 28), rb_txt, fill=WHITE, font=rb)

    # Left panel: badge + "FIX" stamp
    badge_y = 200
    d.ellipse([(50, badge_y), (50 + 220, badge_y + 220)], outline=ACCENT, width=10)
    bf2 = find_font(78)
    d.text((90, badge_y + 70), "FIX", fill=WHITE, font=bf2)

    # RED warning chip below badge
    chip_y = badge_y + 260
    chip_w = 260
    d.rounded_rectangle([(50, chip_y), (50 + chip_w, chip_y + 60)], radius=12, fill=RED)
    cf = find_font(28)
    chip_txt = "ERROR CODE"
    cw = cf.getbbox(chip_txt)[2]
    d.text((50 + (chip_w - cw) // 2, chip_y + 14), chip_txt, fill=WHITE, font=cf)

    # Right side: big text
    right_x = panel_w + 50
    right_w = W - right_x - 50

    # Top line — biggest
    top_size = 96
    while top_size > 50:
        tf = find_font(top_size)
        lines = wrap(top, tf, right_w)
        if len(lines) <= 2:
            break
        top_size -= 8
    line_h = int(top_size * 1.1)
    top_y = 160
    for i, line in enumerate(lines):
        d.text((right_x, top_y + i * line_h), line, fill=TEXT_DARK, font=tf)

    # Bottom line — punchier
    bottom_y = top_y + len(lines) * line_h + 40
    bot_size = 72
    while bot_size > 38:
        bf3 = find_font(bot_size)
        bot_lines = wrap(bottom, bf3, right_w)
        if len(bot_lines) <= 2:
            break
        bot_size -= 6
    bline_h = int(bot_size * 1.1)
    for i, line in enumerate(bot_lines):
        d.text((right_x, bottom_y + i * bline_h), line, fill=ACCENT, font=bf3)

    # Bottom URL bar
    d.rectangle([(0, H - 90), (W, H)], fill=DARK)
    uf = find_font(42)
    url = "errorcodefixes.com"
    uw = uf.getbbox(url)[2]
    d.text(((W - uw) // 2, H - 65), url, fill=ACCENT, font=uf)

    return img


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", help="single slug")
    args = p.parse_args()

    scripts = sorted(SHORTS_DIR.glob("*.md"))
    if args.slug:
        scripts = [s for s in scripts if args.slug in s.stem]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for sp in scripts:
        title, top, bottom = parse_thumbnail_copy(sp)
        # Slug = filename without date prefix
        slug = sp.stem.split("_", 1)[1] if "_" in sp.stem else sp.stem
        out = OUT_DIR / f"{slug}.png"
        if out.exists():
            continue
        img = render_thumbnail(top, bottom, slug)
        img.save(out, "PNG", optimize=True)
        print(f"  {slug}.png")

    total = len(list(OUT_DIR.glob("*.png")))
    print(f"\n[+] {total} thumbnails in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
