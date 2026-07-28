# industrial-fixes (errorcodefixes.com) — agent guardrails

Astro static site → Cloudflare Pages. **Every push to main auto-deploys production**
(.github/workflows/deploy.yml). There is no human gate between commit and prod.

## Strategy (decided 2026-07, do not silently reverse)

The site was rejected by AdSense ("Low value content") and sandboxed by Google Search
as a ~5,800-page auto-generated content farm. The recovery strategy is **QUALITY
CONSOLIDATION**: a ~1,156-post indexable quality core (everything else live but
noindexed + de-linked), with all new investment going to **verified industrial/
commercial content only** (Fanuc, ABB, Siemens, Yaskawa, SEW, York, Hoshizaki,
Rational, APC...) — the only segment with real human traffic (~150 engaged
sessions/28d) and the growing AI-assistant referral channel.

- **No new consumer-appliance content.** Washers/dryers/ovens/consumer brands are done.
- **Content generation is FROZEN** (2026-07-28): the eight generator workflows
  (article-gen, content-pipeline, deepen, models-gen, parts-gen, symptoms-gen,
  code-mine, video-batch) are dispatch-only and disabled. Do not re-add cron
  schedules or re-enable them without an explicit decision from Chris.
  History: the Perplexity key died ~6/27; the pipeline then generated 629
  ungrounded, partly hallucinated drafts in 21 days (all held by its own review
  gate). generate-articles.py now fails closed on empty research and blocks
  non-industrial topics.
- Don't re-request the AdSense review until the site is genuinely clean; never
  spam re-reviews.

## Hard don'ts

1. **Never delete noindexed posts.** The 4,495 pruned posts stay live (no 404s),
   noindexed via `src/data/noindex-slugs.ts` — the single source of truth.
   Header-level `X-Robots-Tag` must NOT be reintroduced in `public/_headers`
   (it would override per-page meta robots).
2. **Never guess Amazon ASINs.** Verified ASINs live in `src/data/parts.json` /
   `asin_map.json` only. Unknown part → search URL or no link.
3. **Static JSON imports only** in site code — dynamic `await import()` of JSON
   breaks the Cloudflare/esbuild build.
4. **No fabricated personas or credentials, ever.** Named "technician" authors were
   scrubbed for honesty (see src/data/authors.ts). BOTH fake-persona outreach
   workflows (outreach.yml AND backlink-outreach.yml) and
   automation/trade_assoc_outreach.py were deleted 2026-07-28 — do not restore
   any of them. Marketing copy must only make claims the site can defend.
5. **Verify against live URLs** (curl the production page) before declaring any
   SEO/robots/deploy change done.

## Build gotchas

- `npm run build` needs the Node heap flag (in the script now:
  `NODE_OPTIONS=--max-old-space-size=6144`) — default heap OOMs on ~4.7k pages.
  Full build takes ~14 min.
- postbuild regenerates `public/search-index.json` AND copies it to
  `dist/search-index.json` (astro copies public/ before postbuild — the dist copy
  is the one that ships). The index feeds /tools/fault-code-lookup, /embed/lookup,
  and the chat worker, and filters out drafts + noindexed slugs.
- Local intermittent `@tailwindcss/node` ESM error on the big page set — retry;
  passes on Ubuntu CI.
- Commit messages containing `[skip deploy]` skip the Cloudflare deploy.

## Deploy / infra map

- Site: Cloudflare Pages, deployed by deploy.yml (wrangler) on push to main.
- Ask-AI chat: separate Worker `errorcodefixes-chat` (workers/chat-api/), deployed
  MANUALLY via wrangler — not in CI.
- Newsletter signup: functions/api/subscribe.ts (CF Pages Function + Resend).
- Sister property: industrial-fixes-reviews.pages.dev (separate repo, wrangler
  direct-upload, orphaned as of 2026-07) — shares the brand + Skimlinks account.

## Analytics / accounts

- GA4 property 534919316 (G-083FJXZNP7); use the wyattbot-reader SA (the
  other locally-configured SA gets 403 on this property). AdSense publisher: pub-8658387753904693.
- Amazon tag: errorcodefixes-20. Skimlinks: 303448X1791493 (amazon links carry
  class="noskim" via rehype plugin so Skimlinks doesn't skim them).
