"""Google Sheets sink for reddit-intel.

Reads service-account JSON from GOOGLE_APPLICATION_CREDENTIALS_JSON env var
(GitHub Actions secret) OR GOOGLE_APPLICATION_CREDENTIALS file path (local).
Per finexio-automation precedent in CLAUDE.md memory.

Writes to a tab named YYYY-WW (ISO year+week) in the configured spreadsheet.
Appending only — never overwrites historical weeks. The Tier A → content
roadmap conversion happens by reading the sheet, not by mutating it.

If SPREADSHEET_ID isn't set, falls back to writing a local JSON file in
./out/ so the pipeline is still smoke-testable.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, UTC
from pathlib import Path
from typing import Iterable

LOG = logging.getLogger("reddit-intel.sink")

HEADERS = [
    "fetched_at_utc", "subreddit", "brand", "codes", "title", "url",
    "equipment_category", "urgency", "age_hours", "score", "num_comments",
    "gap_kind", "matched_slug", "article_url", "video_target", "post_id",
]


def _load_sa_creds():
    """Returns google.oauth2.service_account.Credentials or None."""
    sa_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    sa_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    info = None
    if sa_json:
        info = json.loads(sa_json)
    elif sa_path and Path(sa_path).exists():
        info = json.loads(Path(sa_path).read_text())
    if info is None:
        return None
    from google.oauth2 import service_account
    return service_account.Credentials.from_service_account_info(
        info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )


def _local_fallback(rows: list[dict], spreadsheet_id: str | None) -> str:
    out_dir = Path(__file__).parent / "out"
    out_dir.mkdir(exist_ok=True)
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    p = out_dir / f"reddit-intel-{stamp}.json"
    p.write_text(json.dumps({"rows": rows, "spreadsheet_id": spreadsheet_id}, indent=2))
    LOG.warning("no SA creds / no SPREADSHEET_ID — wrote local fallback %s", p)
    return str(p)


def write(rows: Iterable[dict]) -> str:
    """Returns the spreadsheet URL (or local path on fallback)."""
    rows = list(rows)
    spreadsheet_id = os.environ.get("REDDIT_INTEL_SPREADSHEET_ID")
    creds = _load_sa_creds()

    if not creds or not spreadsheet_id:
        return _local_fallback(rows, spreadsheet_id)

    # Lazy import so the local fallback path doesn't need googleapiclient
    from googleapiclient.discovery import build

    svc = build("sheets", "v4", credentials=creds, cache_discovery=False)
    now = datetime.now(UTC)
    tab = now.strftime("%G-W%V")  # ISO year + week, e.g. "2026-W20"
    fetched_at = now.isoformat(timespec="seconds")

    # Ensure tab exists (create if needed). Single batch request.
    try:
        svc.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={"requests": [{"addSheet": {"properties": {"title": tab}}}]},
        ).execute()
        # Write header row on a freshly-created tab
        svc.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{tab}!A1",
            valueInputOption="RAW",
            body={"values": [HEADERS]},
        ).execute()
    except Exception as e:
        # Tab already exists — that's the happy path on most runs
        if "already exists" not in str(e):
            LOG.warning("addSheet failed (continuing): %s", e)

    values = [[fetched_at] + [r.get(h, "") for h in HEADERS if h != "fetched_at_utc"]
              for r in rows]
    svc.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{tab}!A1",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": values},
    ).execute()

    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid=0"
    LOG.info("wrote %d rows to %s tab=%s", len(values), url, tab)
    return url
