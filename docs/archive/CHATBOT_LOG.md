# AI Chat Widget — Build Log

**Built:** 2026-04-24  
**Commit:** 5116003  
**Status:** ✅ Deployed and live

---

## What Was Built

A floating AI chat widget that appears on every page of errorcodefixes.com. Users click "🔧 Ask AI" (bottom-right corner), type a question about an industrial error code, and get an AI-generated answer backed by site content.

---

## Architecture

```
User question
    ↓
ChatWidget.astro (browser)
    ↓  POST /  { question }
Cloudflare Worker (errorcodefixes-chat)
    ↓  Strategy 1: brand+code slug → fetch article HTML from site
    ↓  Strategy 2: Pagefind index → score pages → fetch best match
    ↓  OpenAI gpt-4o-mini (question + article context)
AI answer + source URL
    ↓
Chat panel (with "View full guide →" link)
```

---

## Worker URL

```
https://errorcodefixes-chat.errorcodefixes.workers.dev
```

Workers.dev subdomain: `errorcodefixes` (registered 2026-04-24 via Cloudflare API)

---

## Files Created / Modified

| File | Action |
|------|--------|
| `workers/chat-api/index.js` | Created — Cloudflare Worker |
| `workers/chat-api/wrangler.toml` | Created — wrangler config |
| `src/components/ChatWidget.astro` | Created — floating chat UI |
| `src/layouts/Layout.astro` | Modified — imports + renders ChatWidget |

---

## Cloudflare Worker Details

- **Name:** `errorcodefixes-chat`
- **Version ID:** `922c39f8-d481-4514-998f-9f251c2ebf95`
- **Secrets:** `OPENAI_API_KEY` (set via `wrangler secret put`)
- **Env vars:** `SITE_URL = https://errorcodefixes.com`
- **Model:** `gpt-4o-mini`, max_tokens=500, temperature=0.3

### Article lookup — two strategies

1. **Brand + code slug match** — extracts brand name (carrier, fanuc, yaskawa, etc.) and numeric/alphanumeric code from the question, builds `/posts/{brand}-{code}-error-code/`, fetches it. Fast and precise.
2. **Pagefind index fallback** — fetches `/pagefind/pagefind-index.json`, scores pages by keyword overlap with the question, fetches the best match. Catches questions that don't follow the exact brand+code pattern.

Both strategies strip HTML and pass up to 4000 chars of article content to the LLM as grounding context.

---

## How to Update the Worker URL

If you need to change or redeploy the Worker:

1. Update `CHAT_API_URL` constant in **`src/components/ChatWidget.astro`** (line ~180 in the `<script is:inline>` block)
2. Push to trigger Cloudflare Pages deployment

---

## How to Redeploy the Worker

```powershell
cd workers/chat-api
$env:CLOUDFLARE_API_TOKEN = "REDACTED_CF_TOKEN"
npx wrangler deploy
```

To update the OpenAI key:
```powershell
echo "sk-..." | npx wrangler secret put OPENAI_API_KEY --name errorcodefixes-chat
```

---

## Notes

- `astro check` passed with 0 errors before commit
- The Cloudflare Pages build runs separately via `deploy.ps1` — this commit only changes source files and triggers the Pages build via GitHub Actions / Cloudflare git integration
- The Worker runs independently from the Pages site — it's always live at the workers.dev URL
- CORS is open (`*`) since the widget is a public-facing tool on a public site
- Dark mode is supported via `@media (prefers-color-scheme: dark)`
- Full keyboard/a11y: Escape closes panel, Enter submits, ARIA labels throughout
