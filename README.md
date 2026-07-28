# Industrial Error Code Fixes

[errorcodefixes.com](https://errorcodefixes.com) — fast troubleshooting guides
for HVAC, CNC, refrigeration, and commercial equipment fault codes.

Static-rendered Astro site, deployed to Cloudflare Pages. ~4,700 built fix
guides of which a **~1,156-post indexable quality core** is exposed to search
engines (the rest are live but noindexed — see CLAUDE.md for the
quality-consolidation strategy). Auto-generated per-post Open Graph images,
Pagefind static search, and an "Ask AI" chat widget backed by a Cloudflare
Worker.

> **Before working in this repo, read [CLAUDE.md](CLAUDE.md)** — it encodes the
> strategy, the hard don'ts, and the build gotchas.

---

## Stack

| Layer            | Choice                                                      |
| ---------------- | ----------------------------------------------------------- |
| Framework        | [Astro 5](https://astro.build) (static output)              |
| Styling          | [TailwindCSS 4](https://tailwindcss.com)                    |
| Search           | [Pagefind](https://pagefind.app) (static, post-build index) |
| OG images        | [satori](https://github.com/vercel/satori) + resvg          |
| Hosting          | [Cloudflare Pages](https://pages.cloudflare.com)            |
| DNS              | Cloudflare                                                  |
| Analytics        | Plausible + GA4                                             |
| Newsletter       | [Resend](https://resend.com) (functions/api/subscribe.ts)   |
| Chat widget      | Cloudflare Worker → OpenAI gpt-4o-mini                      |
| Affiliate stack  | Amazon Associates, Impact (Repair Clinic, SupplyHouse, …)   |

---

## Repo layout

```
src/
├── components/      ← per-page UI: Header, Footer, Card, ChatWidget, …
├── data/
│   ├── authors.ts                ← author key → name + credentials
│   ├── equipmentCategories.ts    ← /equipment/[slug]/ hub config
│   └── blog/        ← ~6,300 .md files: ~4,700 published + held drafts
├── layouts/         ← Layout, AuthorLayout, AboutLayout, PostDetails, Main
├── pages/
│   ├── index.astro             ← homepage
│   ├── about.md
│   ├── disclosure.md           ← FTC + Amazon Associates disclosure
│   ├── posts/[...slug]/        ← one post per .md file
│   ├── posts/[...page].astro   ← paginated post list
│   ├── tags/                   ← tag landing pages
│   ├── brands/                 ← brand index pages
│   ├── equipment/              ← curated equipment hubs
│   ├── authors/                ← per-author bios with Person schema
│   ├── search.astro            ← Pagefind search UI
│   └── og.png.ts               ← default site OG image
├── styles/global.css
└── config.ts                  ← site-wide settings (postPerPage, etc.)

public/                        ← static assets (logos, favicon, og images)
scripts/
├── build-search-index.mjs     ← postbuild: writes search-index.json for chat
├── fix-mojibake.mjs           ← idempotent CP1252→UTF-8 repair across blog/
├── refresh-moddate.mjs        ← bump modDatetime on a list of files
└── indexnow-ping.mjs          ← post-deploy IndexNow submission (Bing/Yandex)
```

---

## Local development

```bash
npm install
npm run dev          # localhost:4321
```

## Build

```bash
npm run build        # astro build + pagefind + search-index (heap flag built in)
npm run typecheck    # astro check (separate, does NOT block deploy)
```

The build emits one HTML + one OG PNG per published post, plus the Pagefind
index. Total runtime ~14 minutes. The build script sets
`NODE_OPTIONS=--max-old-space-size=6144` — the default Node heap OOMs on this
page count.

## Deploy

**Pushing to main deploys production automatically** via
`.github/workflows/deploy.yml` (build → wrangler pages deploy → cache purge →
health check). Commits with `[skip deploy]` in the message skip it.

Manual fallback only:

```bash
CLOUDFLARE_API_TOKEN=<pages-edit-token> npx wrangler@latest pages deploy dist/ --project-name=industrial-fixes --branch=main --commit-dirty=true
```

After a manual deploy, optionally ping IndexNow so Bing/Yandex re-crawl the
URLs that changed in the last commit:

```bash
node scripts/indexnow-ping.mjs
```

To skip it for a particular run (local dry-deploys, CI without internet):
`NO_INDEXNOW=1`.

---

## Content

Posts live in `src/data/blog/<slug>.md` with frontmatter:

```yaml
---
title: "Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix"
author: "Error Code Fixes Editorial Team"   # anonymous team byline only — no named personas
pubDatetime: 2024-03-13T08:00:00Z
modDatetime: 2026-05-01T08:00:00Z
slug: hoshizaki-e1-error-code
featured: true
draft: false
tags:
  - commercial-refrigeration
  - hoshizaki
  - ice-machine
description: "Hoshizaki E1 means a water inlet problem. Float switch, inlet valve, water supply fixes."
---
```

Bump `modDatetime` whenever the body really changes — never sitewide. Use
`scripts/refresh-moddate.mjs <paths…>` for batched updates.

Authors are configured in `src/data/authors.ts`. Bio pages with Person schema
live at `src/pages/authors/<slug>.md` and use `AuthorLayout.astro`.

Equipment categories (HVAC, CNC, Refrigeration, Boilers, Compressors,
Electrical) are configured once in `src/data/equipmentCategories.ts` —
the homepage card grid, the `/equipment/` index, and each
`/equipment/[slug]/` hub all read from this file.

---

## Affiliate program

- **Amazon Associates** tag: `errorcodefixes-20`
- **Impact partner network**: Repair Clinic, SupplyHouse, Grainger, JB Tools,
  JRacenstein (program approval status: pending for some)

Disclosure page: `/disclosure/` (FTC + Amazon Associates compliant) — linked
from the global footer. Required on every page that contains affiliate
links.

---

## Operational notes

- **DNS**: Cloudflare nameservers `titan.ns.cloudflare.com`, `lia.ns.cloudflare.com`.
- **Cache**: HTML is `max-age=0, must-revalidate`; static assets are immutable.
  After a deploy, purge the zone with the Cloudflare API if needed (the deploy
  token has Cache Purge scope).
- **robots.txt**: explicitly allows GPTBot / ClaudeBot / PerplexityBot.
- **llms.txt**: published at site root.
- **Sitemap**: auto-generated to `/sitemap-index.xml` via `@astrojs/sitemap`.
- **Search**: Pagefind index in `dist/pagefind/`, copied back to
  `public/pagefind/` so subsequent dev runs have search UI.

---

## License

The original [AstroPaper](https://github.com/satnaing/astro-paper) theme by
Sat Naing is MIT-licensed. Site content (fix guides, brand assets) is
proprietary to errorcodefixes.com.
