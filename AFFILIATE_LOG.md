# Affiliate Program Log

## Impact.com Campaigns

### Status as of 2026-04-24

#### Zoro (Zoro.com) - Industrial Parts Supplier
- **Network:** Impact.com
- **Brand page:** https://app.impact.com/advertiser-advertiser-info/Zoro.brand
- **Application page:** https://app.impact.com/advertiser-applycampaign-info/Zoro.brand
- **Status:** PENDING APPLICATION
- **Notes:** 
  - Zoro is a strong fit for errorcodefixes.com — they stock industrial parts, HVAC components, VFD drives, and commercial equipment parts.
  - The Impact.com API (Mediapartners endpoint) returned no campaigns via automated query; application flow is browser-only.
  - **Chris must apply manually:** Log into app.impact.com with Google (chris.a.wyatt@gmail.com), search "Zoro" in Marketplace, click Apply.
  - Application URL: https://app.impact.com/advertiser-applycampaign-info/Zoro.brand
  - Commission rates typically 2-5% on industrial parts (often $50–$500+ orders = strong EPC)

#### Other Pending Applications (browser-only flows)
- **RepairClinic** — appliance/HVAC parts, great for residential furnace/AC articles
- **SupplyHouse** — plumbing/HVAC parts, strong for Navien/boiler content  
- **Grainger** — industrial, perfect for VFD/commercial content
- **Parts Town** — commercial food service/ice machine parts (Hoshizaki, etc.)

### Currently Active
- **Amazon Associates** — tag: `errorcodefixes-20` — active on all articles

---

## ASIN Upgrade Audit (2026-04-24)

Investigated upgrading top 5 articles from Amazon search URLs to direct ASIN links.

| Part | Part Number | ASIN Found | Action |
|------|-------------|-----------|--------|
| Carrier limit switch | HH12ZB195 | None confirmed | Left search URL |
| Rheem flame sensor | 42-24195-01 | None on .com | Left search URL |
| Goodman pressure switch | B1370112 | None confirmed | Left search URL |
| Navien igniter | BH2040180A | None confirmed | Left search URL |
| Hoshizaki float switch | 4A2734-01 | None confirmed | Left search URL |

**Note:** Related ASINs found (HH12ZB190 → B00FDX46SG, HH12ZB190 → B0DHYLTMY6) but exact part numbers not matched. Per policy, only updating when confirmed ASIN is verified.

**Recommendation:** Consider updating Carrier article to use B00FDX46SG (HH12ZB190, very similar part) as a general Carrier limit switch link — would convert 3-4x better than search URL. Needs Chris approval since it's a different (but compatible) part number.


---

## Skimlinks — Network Aggregator (LIVE 2026-05-21)

- **Network:** Skimlinks
- **Publisher ID:** 303448X1791493
- **Status:** ACTIVE site-wide on errorcodefixes.com + industrial-fixes-reviews
- **Notes:**
  - Approved same-day (2026-05-21).
  - Single script tag in Layout.astro auto-monetizes ~48,000 merchant network.
  - Covers Parts Town, RepairClinic, Home Depot, Lowes, AutomationDirect, Galco, Wolf Automation, Supply House, PexUniverse, HVAC Parts Shop, TruTech Tools, Grainger, Johnstone Supply — no per-merchant signup needed.
  - Pass-through commission ~75% of merchant rate (Skimlinks keeps ~25%).
  - **MUST DO in Skimlinks dashboard:** Add `amazon.com`, `amzn.to`, `amazon.co.uk` to Excluded Domains so direct Amazon Associates (tag=errorcodefixes-20) stays at 100% commission.

## Articles Catalog Expansion (2026-05-21)

- Added 131 net-new error code guides + 12 tools buying guides + 8 brand-vs-brand comparisons
- Total catalog: 1,288 articles (up from 1,157)
- All new content shipped with proper frontmatter for AstroPaper schema validation (`pubDatetime`, `modDatetime`, `slug`, `featured: false`, `draft: false`, structured `tags` array)
- Authors mapped to existing roster: Dana Kowalski (HVAC + VFD), Marcus Webb (commercial refrigeration), James Rutherford (CNC), Industrial Error Code Fixes (editorial collective)

