"""
OEM service bulletin monitor for errorcodefixes.com.

Polls manufacturer-provided RSS/Atom feeds and PDFs to spot newly-published
service bulletins, technical advisories, and recall notices. New OEM
bulletins are extremely high-value content topics — a guide that covers a
fresh bulletin within 48 hours often gets featured snippet treatment
because there's no other content yet.

USAGE:
    python service_bulletin_monitor.py
        Polls all configured sources, writes output/bulletins_YYYY-MM-DD.md

DEPENDENCIES: stdlib only.

LIMITATIONS:
    Many OEMs gate service bulletins behind dealer logins. For those,
    Google Alerts is the practical alternative — see automation/README.md.

    The feeds below are public RSS/Atom feeds and CPSC recall data.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"

# Sources to monitor. Format: (label, url, fetch_type, brand_hint)
# fetch_type:
#   "rss"         — Atom/RSS feed
#   "cpsc_json"   — Consumer Product Safety Commission JSON API
SOURCES: list[tuple[str, str, str, str]] = [
    # CPSC recalls (public JSON API)
    (
        "CPSC HVAC/Refrigeration Recalls",
        "https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallProductCategory=Heating+&+Cooling",
        "cpsc_json",
        "hvac",
    ),
    (
        "CPSC Appliance Recalls",
        "https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallProductCategory=Appliances",
        "cpsc_json",
        "appliances",
    ),
]


@dataclass
class Bulletin:
    source: str
    title: str
    summary: str
    url: str
    published: str
    age_days: int
    brand_hint: str
    relevance_score: int


# Keywords that signal a bulletin worth writing about for our audience
RELEVANCE_KEYWORDS = {
    # Brands we already cover
    "carrier": 5, "trane": 5, "goodman": 5, "lennox": 4, "york": 4,
    "bryant": 4, "heil": 3, "tempstar": 3, "payne": 3,
    "mitsubishi": 5, "daikin": 5, "fujitsu": 4,
    "hoshizaki": 5, "manitowoc": 5, "scotsman": 5,
    "samsung": 3, "lg": 3, "whirlpool": 4, "maytag": 4, "bosch": 4,
    "weil-mclain": 4, "lochinvar": 4, "navien": 5, "rinnai": 5,
    "fanuc": 5, "mazak": 5, "haas": 5,
    "allen-bradley": 5, "powerflex": 5, "siemens": 4, "sinamics": 5,
    # Recall types worth covering
    "recall": 3, "service bulletin": 4, "technical service bulletin": 4,
    "tsb": 4, "advisory": 2, "stop sale": 5, "stop ship": 5,
    # Fault topics
    "fire hazard": 3, "co exposure": 4, "shock hazard": 3,
    "compressor failure": 3, "control board": 3,
}


def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"[!] Failed to fetch {url}: {e}")
        return ""


def parse_cpsc_json(data: str, source_label: str, brand_hint: str) -> list[dict]:
    """Parse CPSC recall JSON response."""
    try:
        records = json.loads(data) if data else []
    except json.JSONDecodeError:
        print(f"[!] Invalid JSON from {source_label}")
        return []
    items = []
    for r in records[:50]:  # cap to last 50 records
        # CPSC JSON keys: Title, Description, RecallDate, URL, Products
        items.append({
            "title": r.get("Title", ""),
            "summary": r.get("Description", "")[:600],
            "url": r.get("URL", ""),
            "published": r.get("RecallDate", ""),
        })
    return items


def parse_rss(data: str) -> list[dict]:
    """Parse generic RSS 2.0 or Atom feed."""
    if not data:
        return []
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return []
    items = []
    # RSS 2.0
    channel = root.find("channel")
    if channel is not None:
        for it in channel.findall("item"):
            items.append({
                "title": (it.findtext("title") or "").strip(),
                "summary": re.sub(r"<[^>]+>", " ", (it.findtext("description") or "")).strip()[:600],
                "url": (it.findtext("link") or "").strip(),
                "published": (it.findtext("pubDate") or "").strip(),
            })
        return items
    # Atom
    atom_ns = "{http://www.w3.org/2005/Atom}"
    for entry in root.findall(f"{atom_ns}entry"):
        link_el = entry.find(f"{atom_ns}link")
        items.append({
            "title": (entry.findtext(f"{atom_ns}title") or "").strip(),
            "summary": re.sub(r"<[^>]+>", " ", (entry.findtext(f"{atom_ns}summary") or "")).strip()[:600],
            "url": link_el.get("href", "") if link_el is not None else "",
            "published": (entry.findtext(f"{atom_ns}updated") or "").strip(),
        })
    return items


def parse_published(s: str) -> datetime | None:
    if not s:
        return None
    # Try RFC 2822
    try:
        return parsedate_to_datetime(s)
    except Exception:
        pass
    # Try ISO
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(s.split(".")[0].replace("Z", ""), fmt.replace("%z", "").replace("Z", ""))
        except ValueError:
            continue
    return None


def score_bulletin(b: dict, brand_hint: str) -> int:
    text = (b["title"] + " " + b["summary"]).lower()
    score = 0
    for kw, w in RELEVANCE_KEYWORDS.items():
        if kw in text:
            score += w
    if brand_hint == "hvac":
        score += 1
    if brand_hint == "appliances":
        score += 0
    return score


def collect_bulletins(min_score: int, max_age_days: int) -> list[Bulletin]:
    out: list[Bulletin] = []
    now = datetime.now(timezone.utc)
    for label, url, fetch_type, brand_hint in SOURCES:
        print(f"[+] {label}")
        data = fetch_url(url)
        if not data:
            continue
        if fetch_type == "cpsc_json":
            items = parse_cpsc_json(data, label, brand_hint)
        elif fetch_type == "rss":
            items = parse_rss(data)
        else:
            items = []
        for it in items:
            pub_dt = parse_published(it["published"])
            if pub_dt is None:
                continue
            if pub_dt.tzinfo is None:
                pub_dt = pub_dt.replace(tzinfo=timezone.utc)
            age = (now - pub_dt).days
            if age > max_age_days:
                continue
            score = score_bulletin(it, brand_hint)
            if score < min_score:
                continue
            out.append(Bulletin(
                source=label,
                title=it["title"],
                summary=it["summary"],
                url=it["url"],
                published=pub_dt.isoformat(),
                age_days=age,
                brand_hint=brand_hint,
                relevance_score=score,
            ))
        time.sleep(2)
    return sorted(out, key=lambda b: (-b.relevance_score, b.age_days))


def write_report(bulletins: list[Bulletin]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    md_path = OUTPUT_DIR / f"bulletins_{date_stamp}.md"
    json_path = OUTPUT_DIR / f"bulletins_{date_stamp}.json"
    json_path.write_text(json.dumps([asdict(b) for b in bulletins], indent=2), encoding="utf-8")

    lines = [
        f"# OEM Service Bulletin / Recall Digest — {date_stamp}",
        "",
        f"**{len(bulletins)} relevant bulletins** in the lookback window.",
        "",
        "**High-value content opportunity:** a guide that covers a fresh bulletin within 48 hours often wins featured snippets because no other site has content yet.",
        "",
    ]
    if not bulletins:
        lines.append("_No bulletins matched the relevance threshold. Widen the keyword filter or check Google Alerts setup for OEM dealer portals (see automation/README.md)._")
    for b in bulletins:
        lines.extend([
            f"## [{b.relevance_score} pts] {b.title}",
            f"_Source: {b.source} · {b.age_days}d old · Published {b.published[:10]}_",
            "",
            f"> {b.summary[:280]}{'…' if len(b.summary) > 280 else ''}",
            "",
            f"- **URL:** {b.url}",
            "- **Action:** if relevant to our audience (HVAC/refrigeration/appliance techs), write a 1,500-word explainer guide within 48h. Title pattern: '[brand] [model] recall — what techs need to know'.",
            "",
        ])
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {md_path}")
    return md_path


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="OEM service bulletin monitor")
    ap.add_argument("--min-score", type=int, default=4)
    ap.add_argument("--max-age-days", type=int, default=30)
    args = ap.parse_args(argv)

    bulletins = collect_bulletins(args.min_score, args.max_age_days)
    write_report(bulletins)
    print(f"\n{len(bulletins)} bulletins surfaced")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
