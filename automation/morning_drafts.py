"""
Morning reply drafter for errorcodefixes.com.

The last 90 seconds of the autonomous loop. Runs AFTER daily_briefing.py.
Takes the top 3 highest-scored threads from this morning's digest, fetches
the actual thread text from each, runs it through the response suggester,
and assembles 3 pre-drafted replies in a single output file.

You open that file at 7am, tune each reply, copy + paste into the
relevant platform, click submit. Total time per reply: 3-5 minutes.

USAGE:
    python morning_drafts.py
        Uses today's daily_briefing JSON; writes drafts to output/

    python morning_drafts.py --top 5
        Draft 5 replies instead of 3

    python morning_drafts.py --date 2026-05-21
        Process a specific date's briefing

DEPENDENCIES: stdlib only. Reuses logic from suggest_response.py.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
ANSWERS_DIR = SCRIPT_DIR.parent / "community" / "answers"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


@dataclass
class ThreadContext:
    venue: str
    title: str
    link: str
    keywords: list[str]
    suggested_guide: str | None
    suggested_template_path: str | None
    fetched_body: str
    matched_template_text: str | None


def load_briefing(date_stamp: str) -> dict:
    """Load the merged daily_briefing JSON. If missing, fall back to reddit_digest."""
    # The daily_briefing.py orchestrator writes a markdown briefing but
    # consolidates from per-source JSON; we read the per-source JSON here.
    reddit_path = OUTPUT_DIR / f"reddit_digest_{date_stamp}.json"
    pm_path = OUTPUT_DIR / f"pm_digest_{date_stamp}.json"
    combined: list[dict] = []
    if reddit_path.exists():
        data = json.loads(reddit_path.read_text(encoding="utf-8"))
        for p in data.get("posts", []):
            combined.append({
                "venue": f"r/{p['subreddit']}",
                "title": p["title"],
                "link": p["permalink"],
                "score": p["opportunity_score"],
                "keywords": p["matched_keywords"],
                "suggested_guide": p.get("suggested_guide"),
                "suggested_template": p.get("suggested_answer_template"),
                "selftext": p.get("selftext", ""),
            })
    if pm_path.exists():
        data = json.loads(pm_path.read_text(encoding="utf-8"))
        for p in data.get("posts", []):
            combined.append({
                "venue": f"PM/{p['forum']}",
                "title": p["title"],
                "link": p["link"],
                "score": p["opportunity_score"],
                "keywords": p["matched_keywords"],
                "suggested_guide": p.get("suggested_guide"),
                "suggested_template": p.get("suggested_answer_template"),
                "selftext": p.get("description", ""),
            })
    combined.sort(key=lambda x: -x["score"])
    return {"posts": combined}


def fetch_thread_body(url: str) -> str:
    """Try to fetch the thread body. Returns empty string if we can't.

    Reddit blocks the JSON endpoint for unauthenticated clients but allows
    RSS — so for Reddit threads we hit `<post-url>.rss` and extract from
    the Atom <content> element. For PM forum threads we fall back to
    raw HTML scraping + tag stripping.
    """
    if not url:
        return ""
    req_url = url
    if "reddit.com" in url:
        # Convert post URL to its RSS variant
        stripped = url.rstrip("/")
        if stripped.endswith(".json"):
            stripped = stripped[:-5]
        if stripped.endswith(".rss"):
            req_url = stripped
        else:
            req_url = stripped + ".rss"
    req = urllib.request.Request(req_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return ""

    if "reddit.com" in url:
        # Atom feed for a single post — extract <content> element
        m = re.search(r"<content[^>]*>(.*?)</content>", data, re.DOTALL)
        if m:
            raw = m.group(1)
            # Reddit double-encodes HTML inside the Atom content node.
            # Unescape once to turn &lt;p&gt; into <p>, then strip all tags.
            import html as html_mod
            raw = html_mod.unescape(raw)
            # Strip HTML comments
            raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.DOTALL)
            # Strip all remaining tags
            text = re.sub(r"<[^>]+>", " ", raw)
            # Collapse entities and whitespace
            text = re.sub(r"&\w+;", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            return text[:3000]
        return ""

    # PM forum HTML — strip tags and extract the OP content block
    text = re.sub(r"<script[^>]*>.*?</script>", "", data, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text[2000:5000][:3000]


def load_template(template_rel_path: str | None) -> str | None:
    if not template_rel_path:
        return None
    full = ANSWERS_DIR / template_rel_path
    if not full.exists():
        return None
    return full.read_text(encoding="utf-8", errors="replace")


def extract_answer_body(template_text: str) -> str:
    """Pull the actual answer body from a template file (skip frontmatter + 'Why this works')."""
    if template_text.startswith("---"):
        end = template_text.find("\n---", 3)
        if end != -1:
            template_text = template_text[end + 4:]
    # Drop trailing "Why this answer works" section
    why_idx = template_text.lower().find("why this answer works")
    if why_idx > 0:
        template_text = template_text[:why_idx]
    return template_text.strip()


def write_drafts(threads: list[ThreadContext], path: Path) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Morning Drafts — {now}",
        "",
        f"Pre-drafted replies for today's top {len(threads)} opportunities.",
        "",
        "## Workflow",
        "1. For each draft below, read the thread (link provided)",
        "2. Edit the draft to match the specific situation (5-10 min/reply)",
        "3. Lead with the answer, link only if it deepens the help",
        "4. Post yourself — never automate the click",
        "5. Log each post in `community/tracker.csv` afterward",
        "",
        "---",
        "",
    ]
    for i, t in enumerate(threads, 1):
        lines.extend([
            f"## Draft {i} — {t.venue}",
            "",
            f"**Thread:** [{t.title}]({t.link})",
            "",
            f"**Matched keywords:** {', '.join(t.keywords) or 'none'}",
        ])
        if t.suggested_guide:
            lines.append(f"**Suggested guide link:** `https://errorcodefixes.com{t.suggested_guide}`")
        lines.extend([
            "",
            "### Original post context",
            "",
        ])
        if t.fetched_body:
            preview = t.fetched_body.strip()[:1000]
            lines.append(f"> {preview.replace(chr(10), chr(10) + '> ')}")
        else:
            lines.append("_(Could not fetch thread body automatically — open the link above to read.)_")
        lines.extend([
            "",
            "### Reply draft (template-based — edit before posting)",
            "",
            "```",
        ])
        if t.matched_template_text:
            body = extract_answer_body(t.matched_template_text)
            # Trim to a reasonable length for inline editing
            if len(body) > 2000:
                body = body[:2000] + "\n\n[...continue with rest of template; full file at the path above...]"
            lines.append(body)
        else:
            lines.append(
                "(No close-matching template — write fresh.)\n\n"
                "Start with: the most likely fix for what they're describing, in 1-2 sentences.\n"
                "Then: the specific diagnostic step they should do next (with a value — ohms, µA, PSI).\n"
                "Then: when to call a pro vs. when they can keep going.\n"
                "Close: one short observation, no CTA."
            )
        lines.extend([
            "```",
            "",
            "### Pre-post checklist",
            "- [ ] Reply is genuinely useful even if no link is included",
            "- [ ] Voice matches the venue (Reddit warmer, PM/HVAC-Talk terse, PLCTalk parameter-heavy)",
            "- [ ] No marketing language, no exclamation points",
            "- [ ] Specific numbers / part numbers included",
            "- [ ] Link to our guide only if it deepens what was said",
            "- [ ] Posted from the venue-appropriate account (real history, not throwaway)",
            "- [ ] Logged in `community/tracker.csv` after submitting",
            "",
            "---",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {path}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Morning reply drafter")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--date", type=str, default=datetime.now().strftime("%Y-%m-%d"))
    args = ap.parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    briefing = load_briefing(args.date)
    if not briefing["posts"]:
        print(f"[!] No briefing data for {args.date}. Run daily_briefing.py first.")
        return 1

    top = briefing["posts"][:args.top]
    print(f"[+] Drafting replies for top {len(top)} threads")
    threads: list[ThreadContext] = []
    for p in top:
        print(f"    Processing: {p['title'][:60]}…")
        body = fetch_thread_body(p["link"])
        template_text = load_template(p.get("suggested_template"))
        threads.append(ThreadContext(
            venue=p["venue"],
            title=p["title"],
            link=p["link"],
            keywords=p["keywords"],
            suggested_guide=p.get("suggested_guide"),
            suggested_template_path=p.get("suggested_template"),
            fetched_body=body,
            matched_template_text=template_text,
        ))

    out_path = OUTPUT_DIR / f"morning_drafts_{args.date}.md"
    write_drafts(threads, out_path)
    print(f"\nOpen {out_path} to tune and post.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
