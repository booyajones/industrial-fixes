# Claude Code Prompt: Independent Review of errorcodefixes.com

Copy everything below into Claude Code.

---

You are doing an independent, skeptical review of `errorcodefixes.com`.

## Objective
Produce a fresh, evidence-based review of the site's current state, biggest revenue blockers, highest-value content opportunities, and next implementation priorities.

Do not trust prior claims until you verify them yourself.
Assume worst case. Dig until you have evidence.

## Environment
- Repo root: `C:\Users\Administrator\.openclaw\workspace\industrial-fixes`
- Workspace root: `C:\Users\Administrator\.openclaw\workspace`
- Live site: `https://errorcodefixes.com`

## Important operating rules
1. This is an independent review, not a rubber stamp.
2. Verify against the live site and the actual repo.
3. Do not print, paste, or copy raw secrets, tokens, API keys, JSON credentials, or private keys into chat or markdown.
4. If you need local credentials, use the existing files or environment already on this machine. Reference their paths if needed, but do not echo contents.
5. Prefer read-only review first. Do not deploy or mutate production unless the prompt explicitly asks for it later.
6. If a prior note conflicts with live evidence, trust live evidence.

## Credential and access policy
Use local credentials already available on this machine if you truly need them. Do not dump them.

Primary reference:
- `C:\Users\Administrator\.openclaw\workspace\TOOLS.md`

If you need deployment or infra context, look there for:
- Cloudflare Pages project details
- Google auth file locations
- local token file paths
- API environment variable names

Again: do not print the secret values.

## Files to read first
Read these before forming conclusions:

### Core audit and strategy
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\SITE_AUDIT.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\EXPERT_EVALUATION.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\REVENUE_FIRST_CONTENT_PLAN.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\REVENUE_PLAN.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\FIX_LOG.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\BRAND_IMPROVEMENTS.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\NEW_ARTICLES_LOG.md`

### Sample content and implementation references
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog\carrier-13-error-code.md`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\pages\index.astro`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\pages\brands\[brand].astro`
- `C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\layouts\Layout.astro`

### Prior judge outputs
- `C:\Users\Administrator\.openclaw\workspace\gauntlet_judge_claude_output.md`
- `C:\Users\Administrator\.openclaw\workspace\gauntlet_judge_gpt_output.md`

## Live URLs to inspect
- `https://errorcodefixes.com/`
- `https://errorcodefixes.com/search`
- `https://errorcodefixes.com/brands/`
- `https://errorcodefixes.com/brands/carrier/`
- `https://errorcodefixes.com/posts/carrier-13-error-code/`
- `https://errorcodefixes.com/robots.txt`
- `https://errorcodefixes.com/sitemap-index.xml`
- `https://errorcodefixes.com/google2bdf1b5dc8c418e0.html`

## What to evaluate

### 1. Revenue
- Which content types can make money fastest
- Which pages have the best combination of search demand and buyer intent
- Whether the current affiliate strategy is structurally weak
- Where contractor lead gen should sit
- Which CTAs are missing on the highest-intent pages
- Which 10 pages should be written next if revenue by next week matters most

### 2. SEO and indexing
- Whether crawl/indexation foundations are actually healthy now
- Whether brand hubs help or need more work
- Whether /posts/ discoverability, internal links, and sitemap structure are enough
- Which pages are most likely to rank fastest with low competition
- Whether article freshness, author trust, schema, and internal linking are sufficient

### 3. UX and conversion
- Homepage clarity and search flow
- Whether the chat widget, quick answers, parts CTAs, and article layout help conversion
- Whether related articles and brand hubs are correctly weighted
- Where the site leaks users before monetization

### 4. Competitive position
- Compare against the most relevant competitors you can verify live
- Identify what they do better
- Identify where errorcodefixes.com has a real moat

### 5. Implementation priorities
- Separate foundational must-fix items from nice-to-have items
- Rank next steps by revenue impact times speed to ship

## Required commands
Run the smallest set of commands needed to verify reality.
At minimum, do these if the environment allows:

- `git status`
- `npx astro check`

If you need build verification and the repo is stable, also run:
- `pnpm build`

## Required outputs
Write these files into the repo root:

1. `CLAUDE_CODE_INDEPENDENT_REVIEW.md`
   - Executive summary
   - What is working
   - What is broken or weak
   - Biggest revenue blockers
   - Biggest SEO blockers
   - Biggest UX blockers
   - Competitive read
   - Final verdict with a score out of 100

2. `CLAUDE_CODE_PRIORITY_ACTIONS.md`
   - Top 10 actions ranked by impact and speed
   - Owner for each action if obvious
   - Estimated effort
   - Expected payoff

3. `CLAUDE_CODE_NEXT_20_PAGES.md`
   - The next 20 pages to write
   - Ranked in order
   - Keyword target
   - Why it should make money
   - What monetization path it maps to

## Review standard
Your review should be hard-nosed and specific.
Do not write generic advice.
Every claim should tie back to a file, live page, or observed behavior.

If you disagree with the current `REVENUE_FIRST_CONTENT_PLAN.md`, say so plainly and replace it with a better one.

---

End of prompt.
