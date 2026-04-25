# Brand Improvements — errorcodefixes.com

**Deployed:** 2026-04-24  
**Commit:** `8f7511c`  
**Status:** Live on Cloudflare Pages (triggers deploy via GitHub push)

---

## What Was Built

### Task 1: Brand Error Code Hub Pages

Two new Astro pages added under `src/pages/brands/`:

**`/brands/` — Brand Index**  
Lists all 18 supported brands grouped by category (HVAC, Refrigeration, CNC/Industrial, Drives/VFD), each with article count and a link to its cheat sheet. Includes a fallback CTA to `/tags/` and `/search/` for edge cases.

**`/brands/[brand]/` — Per-Brand Cheat Sheet**  
Dynamically generated for all 18 brands using `getStaticPaths()`. Each page shows:
- Headline: "[Brand] Error Code Reference — All N Codes"
- A zebra-striped table: Error Code | What It Means | Fix link
- The error code column uses the first part of the post title (before the " — " separator)
- "What It Means" uses the rest of the title or falls back to the post description
- A "View all [Brand] guides →" CTA linking to the existing `/tags/[brand]/` page

**Brands covered:** Carrier, Goodman, Lennox, Trane, Rheem, York, Daikin, Mitsubishi, Fujitsu, Hoshizaki, Manitowoc, Fanuc, Haas, Yaskawa, ABB, Siemens, Allen-Bradley, Danfoss

**Article counts at build time (approx):**  
Carrier ~55 | Trane ~39 | Lennox ~35 | Goodman ~25 | ABB ~25 | Siemens ~20 | Haas ~20 | Allen-Bradley ~20 | Fanuc ~20 | Mitsubishi ~20 | Daikin ~20 | Manitowoc ~18 | Rheem ~17 | York ~17 | Yaskawa ~15 | Hoshizaki ~15 | Danfoss ~13 | Fujitsu ~5

---

### Task 2: Internal "See Also" Links

**Script:** `scripts/add_internal_links.py`

Added `## See Also` sections to the first 5 eligible articles per brand for the top 5 HVAC brands (25 files total).

**Files modified:**
- carrier-11, 12, 13, 13-soft-lockout, 14
- goodman-1, 2, 3, 4, 5 flash
- lennox-292, elite-series, 103, 111, 114
- trane-1-flash, 126, 2-flashes, 3-flashes, 3-flashes-pressure-switch
- rheem-classic-furnace, e1, 2-flashes, 3-flashes, 4-flashes

Each See Also section contains 4 links to other articles from the same brand. Links follow the format:
```
- [Title of Related Article](/posts/slug/)
```

To run on more articles: increase `MAX_PER_BRAND` in the script or expand the `BRANDS` list.

---

### Task 3: Nav Update

Added **"By Brand"** nav item to `src/components/Header.astro`, positioned after "By Equipment" and before "About". Links to `/brands/`. Uses the same `isActive()` pattern as other nav items for active-state highlighting.

---

### Task 4: TypeScript Check

`npx astro check` passes with **0 errors, 0 warnings** (5 pre-existing hints in other files unrelated to this PR).

One error was found and fixed during development: `post.data.slug` does not exist in the content schema. Replaced with `getPath(post.id, post.filePath)` using the project's existing `getPath` utility.

---

## SEO Impact (Expected)

- 18 new `/brands/[brand]/` pages — each targets "[Brand] error code reference" queries
- `/brands/` index — targets "error codes by brand" navigational queries
- 25 internal links added — improves crawl depth and PageRank flow from high-traffic posts to related articles
- Nav "By Brand" — increases discoverability and reduces bounce rate

---

## Next Steps (Optional)

- Run `add_internal_links.py` with higher `MAX_PER_BRAND` (e.g., 10 or 20) to cover more articles
- Expand See Also to industrial brands (fanuc, haas, abb, siemens, etc.)
- Add breadcrumb structured data to brand hub pages
- Consider adding brand logo images to `/brands/` index for visual appeal
