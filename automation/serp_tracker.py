"""
SERP position tracker for errorcodefixes.com.

Tracks where our guides rank in DuckDuckGo's organic results for our
target keywords. DDG's market share is small (~2-3%) but its results
correlate strongly with Google's ranking signals for technical/long-tail
queries (DDG uses Bing's index + their own re-ranker), so position trends
over time are a useful proxy. And it doesn't block scrapers.

USAGE:
    python serp_tracker.py
        Tracks all keywords in keywords.txt against errorcodefixes.com.
        Writes output/serp_YYYY-MM-DD.{md,json}.

    python serp_tracker.py --keyword "carrier code 13"
        One-off check on a single keyword.

DEPENDENCIES: stdlib only (urllib, re, html).

LIMITATIONS:
    Bing detects bot traffic; Google detects bot traffic; DDG HTML endpoint
    is more permissive. We use DDG as the daily polling source. For
    higher-fidelity Google data, sign up for the Brave Search API (free
    tier: 2000 queries/month) or SerpAPI ($50/mo) and swap the fetch_serp
    implementation accordingly.

SCHEDULING (Windows Task Scheduler, daily at 7:15 AM):
    Program: C:\\Python314\\python.exe
    Arguments: C:\\errorcodefixes-improvements\\automation\\serp_tracker.py
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
KEYWORDS_FILE = SCRIPT_DIR / "keywords.txt"

TARGET_DOMAIN = "errorcodefixes.com"
COMPETITOR_DOMAINS = [
    "partstown.com",
    "repairclinic.com",
    "thermostating.com",
    "dimaticcontrol.com",
    "fixurge.com",
    "cnccode.com",
    "cnccookbook.com",
    "inspectapedia.com",
    "manualslib.com",
    "samsung.com",
]


@dataclass
class SerpResult:
    keyword: str
    our_position: int | None   # None = not in top 50
    our_url: str | None
    top_competitor: dict | None  # {position, domain, url, title}
    total_results_seen: int
    timestamp: str


def fetch_ddg_serp(keyword: str) -> str:
    """Fetch DuckDuckGo HTML SERP for a keyword. Returns raw HTML."""
    q = urllib.parse.quote_plus(keyword)
    url = f"https://html.duckduckgo.com/html/?q={q}"
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    }, method="POST", data=b"")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"[!] HTTP {e.code} on '{keyword}': {e.reason}")
        return ""
    except Exception as e:
        print(f"[!] Failed to fetch '{keyword}': {e}")
        return ""


def parse_ddg_serp(html_text: str) -> list[dict]:
    """Extract organic results from DDG HTML SERP. Returns list of {url, title}."""
    results = []
    # Each result block has <a class="result__a" href="...">TITLE</a>
    # DDG wraps the href in a redirect; the actual URL is in the uddg parameter
    # but newer responses contain the raw URL. Handle both.
    block_re = re.compile(
        r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        re.DOTALL,
    )
    for m in block_re.finditer(html_text):
        href = m.group(1)
        # Handle wrapped redirect
        if href.startswith("/l/?") and "uddg=" in href:
            uddg_match = re.search(r"uddg=([^&]+)", href)
            if uddg_match:
                href = urllib.parse.unquote(uddg_match.group(1))
        # Strip HTML from title
        title = re.sub(r"<[^>]+>", "", m.group(2))
        title = html.unescape(title).strip()
        if href.startswith("http"):
            results.append({"url": href, "title": title})
    return results


def analyze_serp(keyword: str, results: list[dict]) -> SerpResult:
    our_position: int | None = None
    our_url: str | None = None
    top_competitor: dict | None = None
    for i, r in enumerate(results, start=1):
        domain_match = re.search(r"https?://(?:www\.)?([^/]+)/?", r["url"])
        if not domain_match:
            continue
        domain = domain_match.group(1).lower()
        if TARGET_DOMAIN in domain and our_position is None:
            our_position = i
            our_url = r["url"]
        elif top_competitor is None and any(c in domain for c in COMPETITOR_DOMAINS):
            top_competitor = {"position": i, "domain": domain, "url": r["url"], "title": r["title"]}
    return SerpResult(
        keyword=keyword,
        our_position=our_position,
        our_url=our_url,
        top_competitor=top_competitor,
        total_results_seen=len(results),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


def load_keywords() -> list[str]:
    if not KEYWORDS_FILE.exists():
        # Bootstrap default keyword list
        default_keywords = [
            "carrier code 13",
            "carrier code 21",
            "carrier code 33",
            "carrier code 34",
            "hoshizaki E1",
            "hoshizaki E2",
            "manitowoc E01",
            "manitowoc HPCO",
            "scotsman 1 flash",
            "scotsman 2 flash",
            "mitsubishi mini split E6",
            "mitsubishi P5",
            "powerflex F004",
            "powerflex F005",
            "powerflex F012",
            "fanuc alarm 300",
            "samsung refrigerator 22C",
            "samsung refrigerator 39E",
            "whirlpool washer F21",
            "bosch dishwasher E15",
            "goodman 3 flash",
            "goodman 4 flash",
            "trane 2 blink",
            "trane 4 blink",
            "lennox 240",
            "york 1 blink",
            "weil-mclain code 3",
            "rinnai code 11",
            "daikin U4",
            "fujitsu 11:4",
        ]
        KEYWORDS_FILE.write_text("\n".join(default_keywords), encoding="utf-8")
        print(f"[i] Created default keywords file at {KEYWORDS_FILE}")
        return default_keywords
    return [
        line.strip()
        for line in KEYWORDS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]


def write_outputs(results: list[SerpResult], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")

    # JSON
    json_path = output_dir / f"serp_{date_stamp}.json"
    json_path.write_text(json.dumps([asdict(r) for r in results], indent=2), encoding="utf-8")

    # Markdown summary
    md_path = output_dir / f"serp_{date_stamp}.md"
    ranked = sum(1 for r in results if r.our_position is not None)
    top10 = sum(1 for r in results if r.our_position and r.our_position <= 10)
    top3 = sum(1 for r in results if r.our_position and r.our_position <= 3)

    lines = [
        f"# SERP Position Tracker — {date_stamp}",
        "",
        f"Tracked **{len(results)}** keywords on Bing.",
        "",
        f"- **Ranking somewhere in top 50:** {ranked} ({ranked*100//max(len(results),1)}%)",
        f"- **Ranking in top 10:** {top10}",
        f"- **Ranking in top 3:** {top3}",
        "",
        "## Detailed rankings",
        "",
        "| Keyword | Our position | Top competitor (pos / domain) |",
        "|---|---|---|",
    ]
    for r in sorted(results, key=lambda x: (x.our_position is None, x.our_position or 999)):
        pos = str(r.our_position) if r.our_position else "—"
        comp = f"{r.top_competitor['position']} / {r.top_competitor['domain']}" if r.top_competitor else "—"
        lines.append(f"| {r.keyword} | {pos} | {comp} |")

    lines.extend(["", "## Action items", ""])
    # Action: keywords ranking 4-15 are the prime push-up candidates
    push_candidates = [r for r in results if r.our_position and 4 <= r.our_position <= 15]
    if push_candidates:
        lines.append("**Push candidates (rank 4-15 — winnable to top 3 with content tuning):**")
        for r in sorted(push_candidates, key=lambda x: x.our_position or 99):
            lines.append(f"- `{r.keyword}` (pos {r.our_position}) — audit H2 phrasing + FAQ; check featured-snippet structure")
    not_ranked = [r for r in results if r.our_position is None]
    if not_ranked:
        lines.append("")
        lines.append("**Not in top 50 — investigate:**")
        for r in not_ranked[:10]:
            lines.append(f"- `{r.keyword}` — does the guide exist? Is it indexed in Bing Webmaster Tools?")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {md_path}")
    print(f"[+] Wrote {json_path}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Bing SERP position tracker")
    ap.add_argument("--keyword", type=str, help="One-off check for a single keyword")
    ap.add_argument("--sleep", type=float, default=3.0, help="Seconds between requests")
    args = ap.parse_args(argv)

    if args.keyword:
        kw_list = [args.keyword]
    else:
        kw_list = load_keywords()

    results: list[SerpResult] = []
    for kw in kw_list:
        print(f"[+] Checking '{kw}'")
        html_text = fetch_ddg_serp(kw)
        if not html_text:
            continue
        serp = parse_ddg_serp(html_text)
        result = analyze_serp(kw, serp)
        results.append(result)
        pos_str = f"pos {result.our_position}" if result.our_position else "not ranked"
        print(f"    {pos_str} ({len(serp)} results parsed)")
        time.sleep(args.sleep)

    write_outputs(results, OUTPUT_DIR)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
