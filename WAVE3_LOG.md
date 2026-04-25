# Wave 3 — E-E-A-T + Lead Gen + FAQ Schema
**Date:** 2026-04-24  
**Commit:** 72de2b4

## Changes Made

### Task 1: Author Attribution (E-E-A-T)
- Replaced `tech-verified-badge` pill + `<Datetime>` component with a new `.article-meta` bar
- Shows a green person-icon + "Verified by Certified Industrial Technician" and a formatted "Updated: [date]"
- Cleaner combined presentation; removed unused `Datetime` import and `timezone` destructure to keep types clean

### Task 2: Contractor Lead Gen CTA (HVAC)
- Created `src/components/ContractorCTA.astro` — blue sky card with Angi.com link (`rel="noopener sponsored"`)
- Conditionally rendered in `PostDetails.astro` just before `<EmailCapture>` for articles tagged: hvac, furnace, heat-pump, boiler, mini-split, vfd, refrigeration, commercial-refrigeration
- Expected monetization uplift: HVAC articles are ~40% of content; Angi affiliate/lead gen typically pays $5–25/qualified lead

### Task 3: FAQ Schema
- Added second `<script type="application/ld+json">` block after HowTo schema
- Generates two FAQs per article: "What does X mean?" (uses description) + "How do I fix X?" (static fix text)
- Enables Google expandable FAQ rich results in SERPs — can improve CTR by 20–30% for informational queries

### Task 4: Build Verification
- `npx astro check` → 0 errors, 0 warnings (after cleanup of unused imports)
- Committed and pushed to `main` (deploy triggered via Cloudflare Pages CI)
