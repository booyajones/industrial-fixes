"""
Site health monitor for errorcodefixes.com.

Pings each of our published guide URLs and validates:
- HTTP 200 response
- Schema (JSON-LD) presence and parseability
- Critical meta tags present (title, description, OG)
- dateModified within freshness threshold (default 365 days)
- Schema dateModified matches visible "Updated:" stamp

USAGE:
    python site_health.py
    python site_health.py --url-list urls.txt
    python site_health.py --freshness-days 180  # tighter staleness check

DEPENDENCIES: stdlib only.

OUTPUT: output/health_YYYY-MM-DD.md and output/health_YYYY-MM-DD.json
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone, timedelta
from pathlib import Path

USER_AGENT = "ErrorCodeFixes-HealthBot/1.0 (https://errorcodefixes.com)"
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output"
URL_LIST = SCRIPT_DIR / "urls.txt"


@dataclass
class HealthCheck:
    url: str
    http_status: int | None
    response_time_ms: float
    has_title: bool
    has_meta_description: bool
    has_og_image: bool
    has_canonical: bool
    schema_blocks_found: int
    schema_types: list[str] = field(default_factory=list)
    schema_valid: bool = False
    article_modified_iso: str | None = None
    visible_updated_text: str | None = None
    days_since_modified: int | None = None
    is_stale: bool = False
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def fetch_url(url: str) -> tuple[int | None, str, float]:
    start = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return (resp.status, body, (time.time() - start) * 1000)
    except urllib.error.HTTPError as e:
        return (e.code, "", (time.time() - start) * 1000)
    except Exception as e:
        return (None, str(e), (time.time() - start) * 1000)


def check_url(url: str, freshness_days: int) -> HealthCheck:
    status, body, elapsed = fetch_url(url)
    check = HealthCheck(
        url=url,
        http_status=status,
        response_time_ms=round(elapsed, 1),
        has_title=False,
        has_meta_description=False,
        has_og_image=False,
        has_canonical=False,
        schema_blocks_found=0,
    )
    if status != 200:
        check.errors.append(f"HTTP {status}")
        return check
    if not body:
        check.errors.append("Empty body")
        return check

    # Basic meta checks
    if re.search(r"<title[^>]*>[^<]+</title>", body):
        check.has_title = True
    else:
        check.errors.append("Missing <title>")

    if re.search(r'<meta[^>]+name=["\']description["\']', body):
        check.has_meta_description = True
    else:
        check.errors.append("Missing meta description")

    if re.search(r'<meta[^>]+property=["\']og:image["\']', body):
        check.has_og_image = True
    else:
        check.warnings.append("Missing og:image")

    if re.search(r'<link[^>]+rel=["\']canonical["\']', body):
        check.has_canonical = True
    else:
        check.warnings.append("Missing canonical link")

    # Schema parsing
    schema_blocks = re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        body,
        re.DOTALL,
    )
    check.schema_blocks_found = len(schema_blocks)
    if not schema_blocks:
        check.errors.append("No JSON-LD schema blocks found")
        return check

    types_found: list[str] = []
    article_modified = None
    for block in schema_blocks:
        try:
            data = json.loads(html.unescape(block))
        except json.JSONDecodeError as e:
            check.errors.append(f"Invalid JSON-LD: {e}")
            continue
        # Handle @graph
        nodes = data if isinstance(data, list) else [data]
        if isinstance(data, dict) and "@graph" in data:
            nodes = data["@graph"]
        for node in nodes:
            if not isinstance(node, dict):
                continue
            t = node.get("@type")
            if isinstance(t, str):
                types_found.append(t)
            elif isinstance(t, list):
                types_found.extend(t)
            if t in ("Article", "TechArticle", "BlogPosting"):
                article_modified = node.get("dateModified")
    check.schema_types = list(dict.fromkeys(types_found))  # de-duped
    check.schema_valid = bool(check.schema_types) and not any(
        "Invalid JSON-LD" in e for e in check.errors
    )

    if article_modified:
        check.article_modified_iso = article_modified
        try:
            mod_dt = datetime.fromisoformat(article_modified.replace("Z", "+00:00"))
            days = (datetime.now(timezone.utc) - mod_dt).days
            check.days_since_modified = days
            if days > freshness_days:
                check.is_stale = True
                check.warnings.append(f"dateModified {days}d old (> {freshness_days}d threshold)")
        except ValueError:
            check.warnings.append(f"Cannot parse dateModified: {article_modified}")
    else:
        check.warnings.append("Article schema present but no dateModified")

    # Try to find visible "Updated:" stamp and cross-check
    m = re.search(r"Updated[:\s]+([A-Z][a-z]+ \d{1,2}, \d{4})", body)
    if m:
        check.visible_updated_text = m.group(1)
        # Soft check — don't fail, just warn if they look very different
        if check.article_modified_iso:
            try:
                visible_dt = datetime.strptime(m.group(1), "%B %d, %Y")
                schema_dt = datetime.fromisoformat(check.article_modified_iso.replace("Z", "+00:00")).replace(tzinfo=None)
                if abs((visible_dt - schema_dt).days) > 7:
                    check.warnings.append(
                        f"Visible 'Updated: {m.group(1)}' differs from schema dateModified by >7 days"
                    )
            except ValueError:
                pass

    return check


def load_urls() -> list[str]:
    if not URL_LIST.exists():
        default = [
            "https://errorcodefixes.com/",
            "https://errorcodefixes.com/posts/carrier-13-error-code",
            "https://errorcodefixes.com/posts/hoshizaki-e1-error-code",
            "https://errorcodefixes.com/posts/mitsubishi-e6-error-code",
            "https://errorcodefixes.com/posts/samsung-refrigerator-error-codes",
            "https://errorcodefixes.com/posts/fanuc-alarm-300",
        ]
        URL_LIST.write_text("\n".join(default), encoding="utf-8")
        print(f"[i] Created default urls.txt at {URL_LIST}")
        return default
    return [
        line.strip()
        for line in URL_LIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]


def write_outputs(checks: list[HealthCheck], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    json_path = output_dir / f"health_{date_stamp}.json"
    md_path = output_dir / f"health_{date_stamp}.md"
    json_path.write_text(json.dumps([asdict(c) for c in checks], indent=2), encoding="utf-8")

    total = len(checks)
    healthy = sum(1 for c in checks if c.http_status == 200 and not c.errors)
    has_errors = sum(1 for c in checks if c.errors)
    stale = sum(1 for c in checks if c.is_stale)
    no_schema = sum(1 for c in checks if c.schema_blocks_found == 0)

    lines = [
        f"# Site Health Report — {date_stamp}",
        "",
        f"Checked **{total}** URLs.",
        "",
        f"- ✅ Healthy: {healthy}",
        f"- ❌ Errors: {has_errors}",
        f"- ⏰ Stale (older than threshold): {stale}",
        f"- 🚫 No schema detected: {no_schema}",
        "",
        "## URLs with errors (fix these first)",
        "",
    ]
    error_checks = [c for c in checks if c.errors]
    if not error_checks:
        lines.append("_None. All checked URLs returned 200 with no errors._")
    for c in error_checks:
        lines.extend([
            f"### {c.url}",
            f"- HTTP: {c.http_status}",
            f"- Errors: {'; '.join(c.errors)}",
            "",
        ])

    lines.extend(["", "## URLs with warnings (lower priority)", ""])
    warn_checks = [c for c in checks if c.warnings and not c.errors]
    for c in warn_checks:
        lines.extend([
            f"### {c.url}",
            f"- Warnings: {'; '.join(c.warnings)}",
            "",
        ])

    lines.extend([
        "",
        "## All checks (detailed)",
        "",
        "| URL | Status | Time | Schema types | Days old | Stale? |",
        "|---|---|---|---|---|---|",
    ])
    for c in checks:
        types = ", ".join(c.schema_types[:3]) if c.schema_types else "—"
        days = str(c.days_since_modified) if c.days_since_modified is not None else "—"
        stale = "yes" if c.is_stale else ""
        lines.append(f"| {c.url} | {c.http_status} | {c.response_time_ms}ms | {types} | {days} | {stale} |")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote {md_path}")
    print(f"[+] Wrote {json_path}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Site health monitor")
    ap.add_argument("--url-list", type=Path, default=URL_LIST)
    ap.add_argument("--freshness-days", type=int, default=365)
    ap.add_argument("--sleep", type=float, default=1.5)
    args = ap.parse_args(argv)

    urls = load_urls() if args.url_list == URL_LIST else [
        line.strip() for line in args.url_list.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    checks: list[HealthCheck] = []
    for url in urls:
        print(f"[+] Checking {url}")
        c = check_url(url, args.freshness_days)
        checks.append(c)
        if c.errors:
            print(f"    ❌ {'; '.join(c.errors)}")
        elif c.warnings:
            print(f"    ⚠️  {'; '.join(c.warnings)}")
        else:
            print(f"    ✅ OK ({c.response_time_ms}ms, schema: {', '.join(c.schema_types) or 'none'})")
        time.sleep(args.sleep)

    write_outputs(checks, OUTPUT_DIR)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
