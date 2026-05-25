# Deploy Pipeline — errorcodefixes.com

**TL;DR:** The GitHub→Cloudflare Pages webhook integration has a `source: None` state in the CF Pages project config (verified 2026-05-25 via API). Commits to main no longer auto-trigger CF Pages builds. We work around this with a local-build + wrangler-direct-upload pipeline, scheduled daily.

## Why the webhook doesn't fire

`curl https://api.cloudflare.com/.../pages/projects/industrial-fixes` returns
`source: None`. The project was originally created with a GitHub source on
2026-04-05 and auto-deployed for ~7 weeks. Sometime between 2026-05-24 23:52
(last auto-deploy: DMARC commit) and 2026-05-25 the source connection was
unlinked or migrated. CF API doesn't expose a way to relink — it has to be
done in the dashboard:

  Cloudflare Pages → industrial-fixes → Settings → Git → Manage connection

For now we ignore the dashboard fix and use the bypass below.

## Bypass: wrangler direct upload

`C:\Users\Administrator\Claude\ecf-auto-deploy.bat` is the canonical
deploy path. What it does:

1. `cd C:\tmp\ecf-deploy\industrial-fixes`
2. `git pull origin main`
3. `npx astro build` (10 min for 2,092 pages)
4. `npx wrangler pages deploy dist --project-name=industrial-fixes --branch=main --commit-hash=<HEAD> --commit-dirty=true`
5. Verify a key URL is live with new content

Auth: uses `CLOUDFLARE_PAGES_TOKEN` from `~/.claude/secrets/ecf.env`
(re-stored as `CLOUDFLARE_API_TOKEN` env var inside the .bat for wrangler).

## When it runs

| Trigger | Cron | Cadence |
|---|---|---|
| Scheduled | `ECF-Auto-Deploy` | Daily 5am ET |
| Tail of weekly traffic report | `ECF-Weekly-Traffic-Report` | Mon 7am ET (after the report commits) |
| Manual | `cmd /c "C:\Users\Administrator\Claude\ecf-auto-deploy.bat"` | On-demand |

The crons that commit but don't need a rebuild (Bing daily URL submit,
outreach batch CSV updates) intentionally don't call deploy — those
only change non-rendered files.

## Verification

Logs: `C:\Users\Administrator\Claude\ecf-auto-deploy.log` accumulates per-run
output. Each run starts with `=== <date> <time> ===` so failures are
easy to spot.

Last test-run (2026-05-25 ~15:30): build = 619s, wrangler upload =
8.79s, verified `1,288+ fix guides` text on homepage.

## Restoring the GitHub integration (optional)

To go back to webhook-driven deploys:

1. Open https://dash.cloudflare.com → Pages → industrial-fixes →
   Settings → Git
2. Click "Connect to Git" if disconnected, or "Manage" if it claims to
   be connected
3. Select GitHub → booyajones → industrial-fixes → main branch
4. Save

Once relinked, future commits should trigger CF Pages builds within
~30s. We can leave the wrangler cron in place as a safety net — both
paths produce the same artifact, last-write-wins.
