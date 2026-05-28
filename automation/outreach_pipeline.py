"""
Outreach pipeline for errorcodefixes.com.

Given a CSV of outreach prospects, generates personalized email drafts
using the templates in ../outreach/. Does NOT send — output is .md files
you copy + paste into your email client. The script's job is to remove
the friction of personalization, not to spam.

USAGE:
    python outreach_pipeline.py
        Reads prospects.csv, writes drafts to output/outreach-drafts/

    python outreach_pipeline.py --template parts-town
        Use the Parts Town template instead of auto-detecting

PROSPECTS.CSV FORMAT:
    name,email,company,role,template,context_note,relevant_recent_post
    "Jane Smith","jane@partstown.com","Parts Town","Marketing Director","parts-town",
        "saw her post about CFESA training","https://partstown.com/blog/cfesa-2026"

OUTPUT:
    output/outreach-drafts/YYYY-MM-DD_<email-safe-name>.md
    Each draft is ready to copy into Gmail/Outlook.

DEPENDENCIES: stdlib only.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "output" / "outreach-drafts"
BUNDLE_ROOT = SCRIPT_DIR.parent
TEMPLATES_DIR = BUNDLE_ROOT / "outreach"
PROSPECTS_CSV = SCRIPT_DIR / "prospects.csv"


@dataclass
class Prospect:
    name: str
    email: str
    company: str
    role: str
    template: str
    context_note: str
    relevant_recent_post: str


def slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s[:50] or "unknown"


def load_template(name: str) -> str:
    candidates = [
        TEMPLATES_DIR / f"{name}.md",
        TEMPLATES_DIR / f"{name}-supply.md",
        TEMPLATES_DIR / f"{name.replace('-', '_')}.md",
    ]
    for c in candidates:
        if c.exists():
            return c.read_text(encoding="utf-8", errors="replace")
    # If no match, build a generic shell
    return (
        "# Generic outreach\n\n"
        "Hi [REPLACE - name],\n\n"
        "I run errorcodefixes.com, an editorial site that publishes troubleshooting\n"
        "guides for industrial and commercial equipment error codes. We're sending\n"
        "qualified technician traffic to parts merchants on every guide.\n\n"
        "[REPLACE - 2-3 sentences personalized to their company/role]\n\n"
        "Would you have 20 minutes for a call to explore a partnership?\n\n"
        "Best,\n"
        "[REPLACE - your name]\n"
    )


def personalize(template_text: str, p: Prospect) -> tuple[str, str]:
    """Returns (subject, body) for an email draft."""
    # Pull the subject line from the template if present, else build one
    subject_match = re.search(r"(?im)^#?\s*subject(?:\s*line)?[:\s]+(.+)$", template_text)
    if subject_match:
        subject = subject_match.group(1).strip().strip('"').strip("'")
    else:
        subject = f"Editorial partnership — errorcodefixes.com x {p.company}"

    # Cut the template down to the actual body section
    # Templates have a "## Email body" section; everything between that and the
    # next ## is the substance.
    body_match = re.search(r"##\s*Email body.*?\n(.*?)(?=\n##\s|\Z)", template_text, re.DOTALL)
    body = body_match.group(1).strip() if body_match else template_text

    # Substitute placeholders
    substitutions = {
        "[REPLACE — name]": p.name or "there",
        "[REPLACE - name]": p.name or "there",
        "[REPLACE — your name]": "[YOUR NAME]",
        "[REPLACE - your name]": "[YOUR NAME]",
        "[REPLACE — phone]": "[YOUR PHONE]",
        "[REPLACE - phone]": "[YOUR PHONE]",
        "[REPLACE — site stats one-pager link]": "[STATS LINK]",
        "[REPLACE — your region]": "[YOUR REGION]",
        "[REPLACE - 2-3 sentences personalized to their company/role]": (
            f"I noticed {p.context_note}. {('Your recent ' + p.relevant_recent_post) if p.relevant_recent_post else ''}. "
            f"Given your role at {p.company} as {p.role}, this feels like a relevant fit."
        ).strip(),
    }
    for k, v in substitutions.items():
        body = body.replace(k, v)

    # Personalization line for empty fields
    if "[REPLACE" in body:
        body += "\n\n<!-- WARNING: unfilled [REPLACE] blocks remain in this draft. Review before sending. -->"

    return (subject, body)


def write_draft(p: Prospect, subject: str, body: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now().strftime("%Y-%m-%d")
    name_slug = slug(p.email or p.name or "unknown")
    path = OUTPUT_DIR / f"{date_stamp}_{name_slug}.md"
    lines = [
        f"# Outreach draft — {p.company} ({p.name})",
        "",
        f"- **To:** {p.name} <{p.email}>",
        f"- **Company:** {p.company}",
        f"- **Role:** {p.role}",
        f"- **Template:** {p.template}",
        f"- **Generated:** {date_stamp}",
        "",
        "---",
        "",
        f"**Subject:** {subject}",
        "",
        body,
        "",
        "---",
        "",
        "## Post-send checklist",
        "- [ ] Sent (paste this section back with timestamp)",
        "- [ ] Logged in outreach tracker tab of `community/tracker.csv`",
        "- [ ] Calendar reminder for 7-day follow-up if no reply",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def load_prospects(csv_path: Path) -> list[Prospect]:
    if not csv_path.exists():
        sample = (
            "name,email,company,role,template,context_note,relevant_recent_post\n"
            '"Jane Smith","jane@partstown.com","Parts Town","Marketing Director","parts-town","saw her LinkedIn post about CFESA training","https://example.com"\n'
            '"Tom Lee","tom@johnstonesupply.com","Johnstone Supply","Partner+ Manager","johnstone-supply","they expanded their HVAC technician training program in 2026",""\n'
            '"Sarah Chen","sarah@automationdirect.com","AutomationDirect","Publisher Partnerships","automation-direct","they recently added Allen-Bradley alternative drives to their catalog",""\n'
        )
        csv_path.write_text(sample, encoding="utf-8")
        print(f"[i] Created sample prospects.csv at {csv_path}")
    prospects = []
    with csv_path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            prospects.append(Prospect(
                name=row.get("name", ""),
                email=row.get("email", ""),
                company=row.get("company", ""),
                role=row.get("role", ""),
                template=row.get("template", "parts-town"),
                context_note=row.get("context_note", ""),
                relevant_recent_post=row.get("relevant_recent_post", ""),
            ))
    return prospects


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Outreach draft generator")
    ap.add_argument("--csv", type=Path, default=PROSPECTS_CSV)
    ap.add_argument("--template", type=str, help="Force a specific template name")
    args = ap.parse_args(argv)

    prospects = load_prospects(args.csv)
    print(f"[+] Loaded {len(prospects)} prospects")

    for p in prospects:
        template_name = args.template or p.template
        template_text = load_template(template_name)
        subject, body = personalize(template_text, p)
        path = write_draft(p, subject, body)
        print(f"[+] Draft: {path}")

    print(f"\n{len(prospects)} drafts written to {OUTPUT_DIR}")
    print("Review each, fill any remaining [REPLACE] blocks, then send manually.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
