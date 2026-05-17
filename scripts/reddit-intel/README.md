# Reddit Intel — Tier A (listen-only)

Council-approved [`09e591`](../../../council_runs/) plan, Phase 1.

Scans target subreddits for high-intent error-code discussions, classifies
each by brand + code + urgency + equipment, matches against the existing 1,148
articles, and emits a weekly Google Sheet + email digest of:

- **Content gaps** — Reddit asks about brand+code combos we don't have an article for. **Highest leverage.**
- **SERP gaps** — we have the article, but Reddit phrasing doesn't match our H2s. Update H2s.
- **High-urgency threads** — best YouTube Shorts script candidates (per council recommendation: redirect distribution effort to Shorts instead of Reddit posting).

**This module does NOT post, comment, vote, or write to Reddit.** That's Tier B, which the council killed.

## Quick start (local)

```powershell
cd scripts/reddit-intel
python -m pip install -r requirements.txt

# Smoke test — small subset, no sheet write, no email
python main.py --dry-run --max-queries 2 --subs hvacadvice -v

# Full run (will write local JSON if no SA / sheet creds set)
python main.py
```

## Env vars

All optional. Without them, the runner uses unauthenticated public JSON and writes a local JSON fallback.

| Var | Purpose | Where to set in prod |
|---|---|---|
| `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET` | OAuth app credentials (script type, no user auth) | GitHub repo secret |
| `GOOGLE_APPLICATION_CREDENTIALS_JSON` | Service-account JSON for Sheets write | GitHub repo secret |
| `REDDIT_INTEL_SPREADSHEET_ID` | Target Google Sheet (must be shared with the SA email) | GitHub repo var |
| `SMTP_HOST` / `SMTP_USER` / `SMTP_PASS` / `SMTP_PORT` | Email digest delivery | GitHub repo secret |
| `REDDIT_INTEL_DIGEST_TO` | Override digest recipient (default: chris.a.wyatt@gmail.com) | GitHub repo var |

## Setup (production)

1. Create a Reddit "script" app at <https://www.reddit.com/prefs/apps> — name it `errorcodefixes-intel`, type `script`, redirect URI `http://localhost`. Capture the client ID (under the app name) and the secret.
2. Create a fresh Google Sheet (any name). Share it with the `finexio-automation-claude@wyattplayground.iam.gserviceaccount.com` SA as Editor. Capture the spreadsheet ID from the URL.
3. Set repo secrets + vars in `booyajones/industrial-fixes`:
   ```bash
   gh secret set REDDIT_CLIENT_ID -R booyajones/industrial-fixes < client-id.txt
   gh secret set REDDIT_CLIENT_SECRET -R booyajones/industrial-fixes < client-secret.txt
   gh secret set GOOGLE_APPLICATION_CREDENTIALS_JSON -R booyajones/industrial-fixes < sa.json
   gh secret set SMTP_HOST -R booyajones/industrial-fixes
   gh secret set SMTP_USER -R booyajones/industrial-fixes
   gh secret set SMTP_PASS -R booyajones/industrial-fixes
   gh variable set REDDIT_INTEL_SPREADSHEET_ID -R booyajones/industrial-fixes
   ```
4. The workflow `.github/workflows/reddit-intel.yml` runs Mondays 13:00 UTC. Trigger manually anytime via `gh workflow run reddit-intel.yml`.

## Architecture

```
queries.yml       — subreddit / pattern / brand config (edit freely; re-read every run)
fetch.py          — Reddit transport (OAuth or public JSON)
classify.py       — regex extraction of codes / urgency / equipment category
match_articles.py — gap classification vs src/data/blog/*.md slugs
sink_sheet.py     — Google Sheets writer (or local JSON fallback)
notify.py         — HTML email digest builder + sender
main.py           — orchestrator + CLI
```

Each module is independently testable. The runner is idempotent — same week, same hits.

## What this is NOT

- Not a poster. Will never call any Reddit write endpoint.
- Not a karma farmer. Doesn't even authenticate as a user when OAuth is on (uses app-only `client_credentials` flow).
- Not an alternative to YouTube Shorts. Per council, Shorts is the actual revenue surface; this just feeds the script-writing factory.
