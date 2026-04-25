# SEO / LLM Optimization Log — errorcodefixes.com

## 2026-04-24 — HowTo Schema, llms.txt, AI Crawler Permissions

**Commit:** `8e504c7` — "SEO/LLM: HowTo schema, llms.txt, AI crawler permissions"

### Changes Made

#### 1. HowTo Schema Upgrade (`src/layouts/PostDetails.astro`)
- The existing HowTo JSON-LD schema block was upgraded with three new required fields for Google Rich Results eligibility:
  - `supply` — two HowToSupply items: first tag (brand name) + "Multimeter"
  - `tool` — three HowToTool items: Multimeter, Screwdriver set, Service manual
  - `step` — three HowToStep items: Diagnose → Fix → Verify
- Author/publisher org schema retained
- datePublished / dateModified retained
- Astro check: 0 errors, 0 warnings after change

**Why it matters:** Google requires `step` array to qualify for HowTo rich results (carousel, expanded SERP snippets). With 900+ articles all now emitting valid HowTo schema, this could meaningfully increase CTR from Google.

#### 2. `public/llms.txt` (new file)
- Created per the emerging llms.txt standard (analogous to robots.txt, but for LLMs)
- Describes the site's purpose, coverage by equipment category, brand lists, and article format
- Signals to LLM crawlers (Perplexity, ChatGPT browsing, Claude, Gemini) what the site is about and how to cite it
- URL: https://errorcodefixes.com/llms.txt

#### 3. `public/robots.txt` — AI Crawler Permissions
- Added explicit `Allow: /` rules for 6 major AI crawlers:
  - GPTBot (OpenAI)
  - ClaudeBot (Anthropic)
  - PerplexityBot
  - Google-Extended (Gemini training)
  - anthropic-ai
  - ChatGPT-User
- Added comment linking to llms.txt
- Existing `User-agent: * Allow: /` unchanged — AI-specific rules reinforce this explicitly

### Deployment
- Pushed to `origin main` (booyajones/industrial-fixes)
- Cloudflare Pages auto-deploys on push — live within ~2 minutes

### Next Steps
- Submit updated sitemap to Google Search Console
- Validate HowTo schema via Google's Rich Results Test: https://search.google.com/test/rich-results
- Monitor Search Console for HowTo rich result impressions over next 2-4 weeks
- Consider adding `estimatedCost` and `totalTime` fields to HowTo schema once content patterns are consistent
