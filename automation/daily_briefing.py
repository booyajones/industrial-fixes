"""
Daily briefing orchestrator for errorcodefixes.com.

Runs all monitors in sequence and produces a single consolidated
daily_briefing_YYYY-MM-DD.md file that lists the day's highest-value
community engagement opportunities ranked across all sources.

This is what you read at 7am with your coffee.

USAGE:
    python daily_briefing.py
    python daily_briefing.py --hours 24

WHAT IT DOES:
    1. Runs monitor_reddit.py
    2. Runs monitor_forums.py
    3. Reads both digests, merges into one ranked list
    4. Writes consolidated daily_briefing_YYYY-MM-DD.md
    5. (Optional) emails the briefing if SMTP env vars are set

SCHEDULING (Windows Task Scheduler, daily at 7:00 AM):
    Program: C:\\Python314\\python.exe
    Arguments: C:\\errorcodefixes-improvements\\automation\\daily_briefing.py

EMAIL (optional — set these env vars):
    ECF_SMTP_HOST   — e.g. smtp.gmail.com
    ECF_SMTP_PORT   — e.g. 587
    ECF_SMTP_USER   — your email
    ECF_SMTP_PASS   — app password
    ECF_TO_ADDR     — recipient (yourself)
"""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import subprocess
import sys
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
PYTHON = sys.executable


def run_monitor(script_name: str, hours: float) -> int:
    """Run one of the monitor scripts and return its exit code."""
    cmd = [PYTHON, str(SCRIPT_DIR / script_name), "--hours", str(hours)]
    print(f"\n>>> Running {script_name} (lookback {hours}h)")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode


def load_digest(path: Path) -> dict:
    if not path.exists():
        return {"count": 0, "posts": []}
    return json.loads(path.read_text(encoding="utf-8"))


def consolidate(date_stamp: str) -> Path:
    """Merge the reddit + forum digests into one ranked file."""
    reddit_json = OUTPUT_DIR / f"reddit_digest_{date_stamp}.json"
    pm_json = OUTPUT_DIR / f"pm_digest_{date_stamp}.json"
    reddit_data = load_digest(reddit_json)
    pm_data = load_digest(pm_json)

    all_posts: list[dict] = []
    for p in reddit_data["posts"]:
        all_posts.append({
            "source": "reddit",
            "venue": f"r/{p['subreddit']}",
            "title": p["title"],
            "link": p["permalink"],
            "author": p["author"],
            "age_hours": p["age_hours"],
            "score": p["opportunity_score"],
            "keywords": p["matched_keywords"],
            "guide": p["suggested_guide"],
            "template": p["suggested_answer_template"],
            "preview": p["selftext"][:300],
        })
    for p in pm_data["posts"]:
        all_posts.append({
            "source": "practicalmachinist",
            "venue": f"PM/{p['forum']}",
            "title": p["title"],
            "link": p["link"],
            "author": p["author"],
            "age_hours": p["age_hours"],
            "score": p["opportunity_score"],
            "keywords": p["matched_keywords"],
            "guide": p["suggested_guide"],
            "template": p["suggested_answer_template"],
            "preview": p["description"][:300],
        })

    all_posts.sort(key=lambda x: -x["score"])

    # Build markdown briefing
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Daily Briefing — {now}",
        "",
        f"**{len(all_posts)} opportunities** across Reddit ({reddit_data['count']}) and Practical Machinist ({pm_data['count']}).",
        "",
        "## Your three priority moves today",
        "",
    ]
    top3 = all_posts[:3]
    if not top3:
        lines.append("_No opportunities scored above threshold. Hunt manually today — see `community/COMMUNITY_PLAYBOOK.md`._")
    else:
        for i, p in enumerate(top3, 1):
            lines.extend([
                f"### {i}. {p['venue']} — score {p['score']}",
                f"**{p['title']}**",
                f"",
                f"- Link: {p['link']}",
                f"- Suggested guide: `{p['guide']}`" if p['guide'] else "- (No direct guide match — focus on karma)",
                f"- Adapt answer from: `community/answers/{p['template']}`" if p['template'] else "- (Write fresh — no template fit)",
                "",
            ])

    lines.extend([
        "",
        "---",
        "",
        "## Full opportunity list (ranked)",
        "",
        "| # | Venue | Score | Age | Title |",
        "|---|---|---|---|---|",
    ])
    for i, p in enumerate(all_posts, 1):
        title = p["title"].replace("|", "\\|")
        if len(title) > 60:
            title = title[:60] + "…"
        lines.append(f"| {i} | {p['venue']} | {p['score']} | {p['age_hours']}h | [{title}]({p['link']}) |")

    lines.extend([
        "",
        "---",
        "",
        "## Reminders",
        "- Lead with the answer; the link is earned, not given",
        "- Log every post in `community/tracker.csv`",
        "- Aim for 5 helpful replies total today (mix of linked + unlinked)",
        "- If a post is >24h old and has many replies, skip — your reply gets buried",
        "",
    ])

    out_path = OUTPUT_DIR / f"daily_briefing_{date_stamp}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[+] Consolidated briefing: {out_path}")
    return out_path


def email_briefing(briefing_path: Path) -> None:
    host = os.environ.get("ECF_SMTP_HOST")
    if not host:
        print("[i] No SMTP env vars set; skipping email.")
        return
    port = int(os.environ.get("ECF_SMTP_PORT", "587"))
    user = os.environ.get("ECF_SMTP_USER")
    password = os.environ.get("ECF_SMTP_PASS")
    to_addr = os.environ.get("ECF_TO_ADDR")
    if not all([user, password, to_addr]):
        print("[!] SMTP_HOST set but other env vars missing; skipping email.")
        return

    msg = EmailMessage()
    msg["Subject"] = f"ErrorCodeFixes Daily Briefing — {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = user
    msg["To"] = to_addr
    msg.set_content(briefing_path.read_text(encoding="utf-8"))

    try:
        with smtplib.SMTP(host, port) as s:
            s.starttls()
            s.login(user, password)
            s.send_message(msg)
        print(f"[+] Emailed briefing to {to_addr}")
    except Exception as e:
        print(f"[!] Email send failed: {e}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Daily briefing orchestrator")
    ap.add_argument("--hours", type=float, default=24)
    ap.add_argument("--min-score-reddit", type=float, default=3.0)
    ap.add_argument("--min-score-forums", type=float, default=2.0)
    ap.add_argument("--no-email", action="store_true")
    args = ap.parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Run each monitor — we pass --hours; min-score uses defaults inside each
    run_monitor("monitor_reddit.py", args.hours)
    run_monitor("monitor_forums.py", args.hours)

    date_stamp = datetime.now().strftime("%Y-%m-%d")
    briefing_path = consolidate(date_stamp)

    if not args.no_email:
        email_briefing(briefing_path)

    print(f"\nAll done. Briefing: {briefing_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
