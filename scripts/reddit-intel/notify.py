"""Email digest of the week's top Reddit signal.

Sends a HTML email to Chris with:
  - top 10 content-gap hits (highest leverage — we don't have these yet)
  - top 5 serp-gap hits (we have the article, opportunity to update H2s)
  - top 5 high-urgency hits (best YouTube Shorts script candidates)
  - link to the full Google Sheet

If SMTP creds aren't set, prints to stdout. Matches the
send_chris_email.py pattern from CLAUDE.md memory.
"""

from __future__ import annotations

import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Iterable

LOG = logging.getLogger("reddit-intel.notify")

DEFAULT_FROM = "Wyatt Bot <noreply@chriswyatt.dev>"
DEFAULT_TO = "chris.a.wyatt@gmail.com"


def _top(rows: Iterable[dict], kind: str, n: int) -> list[dict]:
    matching = [r for r in rows if r.get("gap_kind") == kind]
    matching.sort(key=lambda r: (r.get("score", 0), r.get("num_comments", 0)), reverse=True)
    return matching[:n]


def _high_urgency(rows: Iterable[dict], n: int) -> list[dict]:
    matching = [r for r in rows if r.get("urgency") == "high"]
    matching.sort(key=lambda r: r.get("num_comments", 0), reverse=True)
    return matching[:n]


def _row_html(r: dict) -> str:
    codes = r.get("codes") or "—"
    return (
        f"<li><a href='{r['url']}'>{r['title'][:120]}</a> "
        f"<small>· r/{r['subreddit']} · {r.get('brand', '?')} · "
        f"codes: {codes} · "
        f"{r.get('num_comments', 0)} comments · "
        f"{int(r.get('age_hours', 0))}h old</small></li>"
    )


def build_html(rows: list[dict], sheet_url: str) -> tuple[str, str]:
    """Returns (subject, html_body)."""
    content = _top(rows, "content_gap", 10)
    serp = _top(rows, "serp_gap", 5)
    urgent = _high_urgency(rows, 5)

    subject = (
        f"errorcodefixes.com weekly Reddit signal — "
        f"{len(content)} content gaps, {len(serp)} SERP gaps, {len(urgent)} urgent"
    )
    html = f"""
    <h2>errorcodefixes.com — weekly Reddit signal</h2>
    <p>{len(rows)} qualified hits this week. Full sheet: <a href='{sheet_url}'>open</a></p>

    <h3>🔥 Content gaps — we don't have an article for these (publish these first)</h3>
    <ol>{''.join(_row_html(r) for r in content) or '<li><em>None this week</em></li>'}</ol>

    <h3>📈 SERP gaps — we have an article but Reddit phrases it differently</h3>
    <ol>{''.join(_row_html(r) for r in serp) or '<li><em>None this week</em></li>'}</ol>

    <h3>⏱ High-urgency threads — best YouTube Shorts script candidates</h3>
    <ol>{''.join(_row_html(r) for r in urgent) or '<li><em>None this week</em></li>'}</ol>

    <hr>
    <p style='color:#888;font-size:0.85em'>
      Tier A intel engine. Listen-only — no posting. Council-approved plan
      <code>09e591</code>. Pipeline source:
      <a href='https://github.com/booyajones/industrial-fixes/tree/main/scripts/reddit-intel'>
        scripts/reddit-intel
      </a>
    </p>
    """
    return subject, html


def send(rows: list[dict], sheet_url: str) -> bool:
    """Returns True if email was sent, False if printed to stdout instead."""
    subject, html = build_html(rows, sheet_url)

    smtp_host = os.environ.get("SMTP_HOST")
    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASS")
    to_addr = os.environ.get("REDDIT_INTEL_DIGEST_TO", DEFAULT_TO)
    from_addr = os.environ.get("REDDIT_INTEL_DIGEST_FROM", DEFAULT_FROM)

    if not (smtp_host and smtp_user and smtp_pass):
        LOG.warning("no SMTP creds — printing digest to stdout")
        print(f"\n--- {subject} ---\n{html}\n")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(smtp_host, int(os.environ.get("SMTP_PORT", "587"))) as s:
        s.starttls()
        s.login(smtp_user, smtp_pass)
        s.sendmail(smtp_user, [to_addr], msg.as_string())
    LOG.info("digest emailed to %s", to_addr)
    return True
