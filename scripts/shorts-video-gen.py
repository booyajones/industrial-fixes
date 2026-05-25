#!/usr/bin/env python3
"""
YouTube Shorts video generator.

Reads a Shorts script .md from growth-pipeline/shorts/, generates ElevenLabs
voiceover for the hook + problem + fix sequence + CTA, then assembles a
1080x1920 vertical MP4 with branded background + on-screen text overlays
synced to the voiceover timing.

Output: growth-pipeline/shorts/videos/{slug}.mp4 — ready to upload to
YouTube Shorts, Instagram Reels, TikTok.

USAGE:
    python scripts/shorts-video-gen.py --slug rinnai-error-code-11
    python scripts/shorts-video-gen.py --limit 5    # first 5 scripts in dir
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

import urllib.request
import json

ROOT = Path(__file__).resolve().parents[1]
SHORTS_DIR = ROOT / "growth-pipeline" / "shorts"
VIDEO_DIR = SHORTS_DIR / "videos"
TMP_DIR = SHORTS_DIR / "_tmp"

W, H = 1080, 1920
FPS = 30

ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"  # Roger - laid-back, casual, resonant (American)

ACCENT = (217, 119, 6)
DARK = (24, 18, 10)
LIGHT = (250, 248, 244)
WHITE = (255, 255, 255)
TEXT_DARK = (32, 24, 12)


def find_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    candidates = ["arialbd.ttf"] if bold else ["arial.ttf"]
    for name in candidates:
        for p in [f"C:/Windows/Fonts/{name}", f"/usr/share/fonts/truetype/dejavu/{name}", name]:
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def parse_script(md_path: Path) -> dict:
    """Pull hook, problem, fix steps, CTA, slug from the .md."""
    text = md_path.read_text(encoding="utf-8")
    name = md_path.stem.split("_", 1)[1] if "_" in md_path.stem else md_path.stem

    def section(header_re: str, body_re: str = r">\s*(.+?)(?:\n\n|\n\*\*)") -> str:
        m = re.search(rf"^## {header_re}.*?{body_re}", text, re.DOTALL | re.MULTILINE)
        return m.group(1).strip() if m else ""

    hook = section(r"Hook")
    problem = section(r"Problem")
    cta = section(r"CTA")

    steps = []
    fix_block = re.search(r"^## Fix sequence.*?(?=^## )", text, re.DOTALL | re.MULTILINE)
    if fix_block:
        for sm in re.finditer(r"\*\*Step \d+:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)", fix_block.group(0), re.DOTALL):
            steps.append(sm.group(1).strip().replace("\n", " "))

    # Bio link slug
    link_m = re.search(r"errorcodefixes\.com/posts/([a-z0-9\-]+)/", text)
    slug = link_m.group(1) if link_m else name

    # Title for thumbnail
    title_m = re.match(r"^# YouTube Short [—–-] (.+)", text)
    title = title_m.group(1).strip() if title_m else name.replace("-", " ").title()

    return {
        "slug": slug,
        "title": title,
        "hook": hook,
        "problem": problem,
        "steps": steps,
        "cta": cta,
        "url": f"errorcodefixes.com/posts/{slug}",
    }


def elevenlabs_tts(text: str, out_path: Path) -> None:
    """Call ElevenLabs TTS, save MP3 to out_path."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    body = json.dumps({
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.3, "use_speaker_boost": True},
    }).encode()
    req = urllib.request.Request(
        url, data=body,
        headers={
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r, open(out_path, "wb") as f:
        f.write(r.read())


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines = []
    cur = words[0]
    for w in words[1:]:
        trial = cur + " " + w
        if font.getbbox(trial)[2] - font.getbbox(trial)[0] > max_w:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    lines.append(cur)
    return lines


def render_frame(text: str, badge: str, accent_top: bool = True) -> Image.Image:
    """One vertical frame: brand bar + badge + big text + URL footer."""
    img = Image.new("RGB", (W, H), LIGHT)
    d = ImageDraw.Draw(img)

    # Top accent bar
    d.rectangle([(0, 0), (W, 130)], fill=ACCENT if accent_top else DARK)
    bf = find_font(46)
    d.text((50, 38), "ERRORCODEFIXES.COM", fill=WHITE, font=bf)

    # Badge
    badge_font = find_font(64)
    bw = badge_font.getbbox(badge)[2] + 60
    bh = 100
    by = 230
    d.rounded_rectangle(
        [((W - bw) // 2, by), ((W + bw) // 2, by + bh)],
        radius=20, fill=ACCENT,
    )
    bx = (W - badge_font.getbbox(badge)[2]) // 2
    d.text((bx, by + 14), badge, fill=WHITE, font=badge_font)

    # Big text in middle
    text_size = 90
    while text_size > 44:
        tf = find_font(text_size)
        lines = wrap_text(text, tf, W - 120)
        line_h = int(text_size * 1.18)
        total_h = len(lines) * line_h
        if total_h < H - 600 and len(lines) <= 6:
            break
        text_size -= 6
    y_start = (H - total_h) // 2 - 40
    for i, line in enumerate(lines):
        lw = tf.getbbox(line)[2]
        d.text(((W - lw) // 2, y_start + i * line_h), line, fill=TEXT_DARK, font=tf)

    # Bottom URL bar
    d.rectangle([(0, H - 160), (W, H)], fill=DARK)
    uf = find_font(50)
    url = "errorcodefixes.com"
    uw = uf.getbbox(url)[2]
    d.text(((W - uw) // 2, H - 110), url, fill=ACCENT, font=uf)

    return img


def assemble_video(script: dict, slug: str) -> Path:
    """Generate VO, render frames per segment, assemble MP4 via FFmpeg."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    # Build the full VO script. Combine hook + problem + steps + CTA into
    # one VO file. Then split visually into frames by section.
    vo_text_full = " ".join(filter(None, [
        script["hook"],
        script["problem"],
        *[f"Step {i+1}: {s}" for i, s in enumerate(script["steps"])],
        script["cta"],
    ]))[:1800]   # cap so TTS stays under 60s

    audio_path = TMP_DIR / f"{slug}.mp3"
    print(f"  [{slug}] ElevenLabs TTS ({len(vo_text_full)} chars)...")
    elevenlabs_tts(vo_text_full, audio_path)

    # Probe audio duration
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)],
        capture_output=True, text=True,
    )
    duration_s = float(probe.stdout.strip() or "30")
    print(f"  [{slug}] VO duration: {duration_s:.1f}s")

    # Build sequence of (image, seconds) for the slideshow
    segments = []
    segments.append(("HOOK", script["hook"][:120], 3.0))
    if script["problem"]:
        segments.append(("THE PROBLEM", script["problem"][:160], 6.0))
    for i, s in enumerate(script["steps"]):
        segments.append((f"STEP {i+1}", s[:160], 7.0))
    cta_text = script["cta"][:140] if script["cta"] else f"Full fix at {script['url']}"
    segments.append(("FULL FIX", cta_text, 4.0))

    # Normalize segment durations to actual audio duration
    target = duration_s - 0.3
    sum_planned = sum(s[2] for s in segments)
    scale = target / sum_planned if sum_planned > 0 else 1
    segments = [(badge, txt, max(2.0, sec * scale)) for badge, txt, sec in segments]

    # Render each frame to PNG + build FFmpeg concat list
    list_path = TMP_DIR / f"{slug}_list.txt"
    with open(list_path, "w", encoding="utf-8") as f:
        for i, (badge, txt, sec) in enumerate(segments):
            frame_path = TMP_DIR / f"{slug}_{i:02d}.png"
            img = render_frame(txt, badge, accent_top=(i % 2 == 0))
            img.save(frame_path, "PNG")
            # FFmpeg concat list format
            f.write(f"file '{frame_path.as_posix()}'\n")
            f.write(f"duration {sec:.2f}\n")
        # last entry must repeat without duration (FFmpeg quirk)
        last_frame = TMP_DIR / f"{slug}_{len(segments)-1:02d}.png"
        f.write(f"file '{last_frame.as_posix()}'\n")

    out_path = VIDEO_DIR / f"{slug}.mp4"
    print(f"  [{slug}] FFmpeg assemble...")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(list_path),
        "-i", str(audio_path),
        "-vf", f"scale={W}:{H},fps={FPS},format=yuv420p",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-shortest",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)
    print(f"  [{slug}] DONE -> {out_path}")
    return out_path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", help="single article slug to render")
    p.add_argument("--limit", type=int, default=0, help="batch first N scripts")
    args = p.parse_args()

    scripts = sorted(SHORTS_DIR.glob("*.md"))
    if args.slug:
        scripts = [s for s in scripts if args.slug in s.stem]
    if args.limit:
        scripts = scripts[: args.limit]

    if not scripts:
        print("[!] No matching shorts scripts found")
        return 1

    print(f"[i] Rendering {len(scripts)} videos")
    for i, sp in enumerate(scripts, 1):
        try:
            data = parse_script(sp)
            if not data["hook"] and not data["problem"]:
                print(f"  [{i}/{len(scripts)}] {sp.stem} - SKIPPED (no parseable hook/problem)")
                continue
            slug = data["slug"]
            out = VIDEO_DIR / f"{slug}.mp4"
            if out.exists():
                print(f"  [{i}/{len(scripts)}] {slug} - already exists, skip")
                continue
            print(f"\n[{i}/{len(scripts)}] {slug}")
            assemble_video(data, slug)
        except Exception as e:
            print(f"  [{i}/{len(scripts)}] {sp.stem} - FAIL: {e}")

    print(f"\n[+] Videos in: {VIDEO_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
