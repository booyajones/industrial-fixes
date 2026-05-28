"""
Affiliate link verifier for errorcodefixes.com.

Scans the new-guides markdown files for outbound links and verifies each
returns HTTP 200. Broken affiliate links cost real money (a 404 is a
conversion lost). Run weekly.

USAGE:
    python affiliate_link_check.py
        Scans all .md files in ../new-guides/

    python affiliate_link_check.py --file ../new-guides/carrier-13-error-code.md
        Check one file only.

OUTPUT: output/affiliate_links_YYYY-MM-DD.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
BUNDLE_ROOT = SCRIPT_DIR.parent
GUIDES_DIR = BUNDLE_ROOT / "new-guides"

# Affiliate domains we care about. Hits to these get HEAD-checked.
AFFILIATE_DOMAINS = [
    "amazon.com", "amzn.to",
    "partstown.com",
    "repairclinic.com",
    "homedepot.com",
    "lowes.com",
    "grainger.com",
    "johnstonesupply.com",
    "automationdirect.com",
    "galco.com",
    "wolfautomation.com",
    "supplyhouse.com",
    "pexuniverse.com",
    "hvacpartsshop.com",
    "ebay.com",
    "angi.com",
]


@dataclass
class LinkCheck:
    source_file: str
    url: str
    domain: str
    http_status: int | None
    response_time_ms: float
    is_affiliate: bool
    is_broken: bool
    error: str | None


def extract_links(text: str) -> list[str]:
    """Pull all http(s) URLs from a markdown blob."""
    # Markdown link: [text](url)
    md_links = re.findall(r"\[[^\]]+\]\((https?://[^\)]+)\)", text)
    # Bare URLs
    bare_links = re.findall(r"(?<![(\[])https?://[^\s\)\]]+", text)
    return list(dict.fromkeys(md_links + bare_links))


def domain_of(url: str) -> str:
    m = re.match(r"https?://(?:www\.)?([^/]+)/?", url)
    return m.group(1).lower() if m else ""


def is_affiliate(url: str) -> bool:
    d = domain_of(url)
    return any(aff in d for aff in AFFILIATE_DOMAINS)


def check_link(url: str, source_file: str) -> LinkCheck:
    start = time.time()
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            elapsed = (time.time() - start) * 1000
            return LinkCheck(
                source_file=source_file,
                url=url,
                domain=domain_of(url),
                http_status=resp.status,
                response_time_ms=round(elapsed, 1),
                is_affiliate=is_affiliate(url),
                is_broken=False,
                error=None,
            )
    except urllib.error.HTTPError as e:
        # Many sites return 405 for HEAD but the page is fine — retry GET
        if e.code in (405, 403, 503):
            try:
                req2 = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req2, timeout=15) as resp:
                    elapsed = (time.time() - start) * 1000
                    return LinkCheck(
                        source_file=source_file, url=url, domain=domain_of(url),
                        http_status=resp.status, response_time_ms=round(elapsed, 1),
                        is_affiliate=is_affiliate(url), is_broken=False, error=None,
                    )
            except Exception as inner:
                return LinkCheck(
                    source_file=source_file, url=url, domain=domain_of(url),
                    http_status=e.code, response_time_ms=round((time.time()-start)*1000, 1),
                    is_affiliate=is_affiliate(url),
                    is_broken=(e.code >= 400 and e.code != 405),
                    error=str(inner),
                )
        return LinkCheck(
            source_file=source_file, url=url, domain=domain_of(url),
            http_status=e.code, response_time_ms=round((time.time()-start)*1000, 1),
            is_affiliate=is_affiliate(url), is_broken=True, error=e.reason,
        )
    except Exception as e:
        return LinkCheck(
            source_file=source_file, url=url, domain=domain_of(url),
            http_status=None, response_time_ms=round((time.time()-start)*1000, 1),
            is_affiliate=is_affiliate(url), is_broken=True, error=str(e),
        )


def write_report(checks: list[LinkCheck]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    json_path = OUTPUT_DIR / f"affiliate_links_{date_stamp}.json"
    md_path = OUTPUT_DIR / f"affiliate_links_{date_stamp}.md"
    json_path.write_text(json.dumps([asdict(c) for c in checks], indent=2), encoding="utf-8")

    total = len(checks)
    affiliate = sum(1 for c in checks if c.is_affiliate)
    broken = sum(1 for c in checks if c.is_broken)
    broken_affiliate = sum(1 for c in checks if c.is_broken and c.is_affiliate)

    lines = [
        f"# Affiliate Link Check — {date_stamp}",
        "",
        f"- **Total links scanned:** {total}",
        f"- **Affiliate links:** {affiliate}",
        f"- **Broken links:** {broken}",
        f"- **Broken affiliate links (revenue impact):** {broken_affiliate}",
        "",
        "## Broken affiliate links (highest priority — money on the floor)",
        "",
    ]
    broken_aff = [c for c in checks if c.is_broken and c.is_affiliate]
    if not broken_aff:
        lines.append("_None. All affiliate links resolve._")
    for c in broken_aff:
        lines.extend([
            f"- **{c.url}**",
            f"  - Source: `{c.source_file}`",
            f"  - HTTP: {c.http_status} / Error: {c.error}",
            "",
        ])

    lines.extend(["", "## All broken links (incl. non-affiliate)", ""])
    for c in checks:
        if c.is_broken and not c.is_affiliate:
            lines.append(f"- {c.url} (in `{c.source_file}`) → HTTP {c.http_status}")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {md_path}")
    print(f"[+] Wrote {json_path}")
    return md_path


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Affiliate link checker")
    ap.add_argument("--file", type=Path, help="Check one file only")
    ap.add_argument("--sleep", type=float, default=0.5)
    args = ap.parse_args(argv)

    if args.file:
        md_files = [args.file]
    else:
        md_files = sorted(GUIDES_DIR.glob("*.md"))

    checks: list[LinkCheck] = []
    seen_urls: set[str] = set()
    for md in md_files:
        if md.name.upper().startswith("BATCH") or md.name.endswith("SUMMARY.md"):
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for url in extract_links(text):
            if url in seen_urls:
                continue
            seen_urls.add(url)
            if "errorcodefixes.com" in url:
                continue  # skip self-links
            c = check_link(url, md.name)
            checks.append(c)
            tag = "AFFIL" if c.is_affiliate else "    "
            status = "BROKEN" if c.is_broken else f"{c.http_status}"
            print(f"[{tag}] {status:6} {url[:80]}")
            time.sleep(args.sleep)

    write_report(checks)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
