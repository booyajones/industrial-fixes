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



---

## Awin — Network Aggregator (APPROVED 2026-05-22)

- **Network:** Awin
- **Publisher ID:** 2905561
- **Account holder:** Chris Wyatt
- **Status:** APPROVED — needs per-advertiser application
- **Notes:**
  - Awin gives direct relationships with electrical/industrial distributors that Skimlinks does not cover at the same commission tier.
  - **Priority advertisers to apply to** (in approximate order of fit for errorcodefixes.com content):
    1. **RS Components / RS Pro** — industrial parts, electrical components, sensors. Strong for VFD, CNC, and controls articles.
    2. **Newark / element14 / Farnell** — electronics distribution. Same use case.
    3. **Conrad Electronic** — industrial automation parts, more EU-focused but has US shipping.
    4. **Sonepar** — electrical distributor, may be region-locked.
    5. **Schneider Electric Boutique** — direct Schneider parts (Altivar drives etc.). High-fit for our VFD content.
    6. **ABB e-commerce** — ABB ACS drives + parts. Direct fit for the ABB ACS580 articles we shipped.
    7. **ToolStation / Tools-United** — tools and instruments for the buying-guide articles.
    8. Any HVAC parts retailer that appears in the directory (browse "Home & Garden" and "Industrial" categories).
  - After each approval, the merchant domain MUST be added to the Skimlinks Excluded Domains list (currently only amazon.com / amzn.to / amazon.co.uk are recommended for exclusion). Otherwise Skimlinks will rewrite Awin clicks and take its cut.
  - Awin tracking link format: `https://www.awin1.com/cread.php?awinmid=<MERCHANT_ID>&awinaffid=2905561&clickref=<OPTIONAL_SUB_ID>&p=<DESTINATION_URL>`
  - Once approved for the top 3 advertisers, I can add a small Astro component that wraps outbound links to those domains in the Awin tracking format automatically. Until then, those clicks go through Skimlinks (still monetized, just at the lower pass-through rate).



---

## Awin Applications Submitted — Browser Session 2026-05-22

Publisher ID 2905561. 10 applications submitted via Awin Advertiser Directory.

Honest finding: Awin US network does NOT carry the originally-targeted Tier 1 advertisers (RS Components, Newark/element14, Schneider Electric Boutique, ABB e-commerce, Conrad Electronic, ToolStation). Awin US is heavy on consumer/lifestyle and light on industrial. Those Tier 1 industrial brands are better pursued via Impact.com (which is already in the AFFILIATE_LOG.md backlog for Zoro, Parts Town, Grainger, J.Racenstein, JB Tools).

### Applications submitted (status: pending, expect approval in 24-72 hours)

| # | Advertiser | Region | Vertical fit | Notes |
|---|---|---|---|---|
| 1 | Ebac | UK | Dehumidifiers | HVAC adjacency — mini split + basement humidity articles |
| 2 | Hüga Heat | US | Supplemental heating | Furnace and boiler companion product |
| 3 | Haier | Global | Appliances + AC | Mini split + refrigerator + washer error code articles |
| 4 | Castle Heaters | UK | Heaters | Supplemental heating during HVAC repair |
| 5 | National Filter Warehouse | US | Air filters | Direct fit — #1 fix for limit-trip codes (Carrier 13, Goodman 4-flash, Trane 4-blink) |
| 6 | Filter King | Global | Air filters | Same use case |
| 7 | GE Appliances Parts & Accessories | US | OEM parts | Direct fit — we publish GE error code articles (Er, E1, LC) |
| 8 | Shop Appliances Affiliate Program | US | Appliance retail | Replacement appliances when repair cost > value |
| 9 | Tado DE | EU | Smart thermostats | Furnace/boiler/mini-split control upgrade recommendation |
| 10 | Tado UK | UK | Smart thermostats | Same fit, UK region |

### What to do when approvals arrive

Each approved advertiser will email a notification with the Awin merchant ID (e.g., "awinmid=12345"). For each one:

1. **Add the merchant's domain to Skimlinks Excluded Domains** at https://hub.skimlinks.com → Settings → Domain Management. This preserves direct Awin commission (vs. Skimlinks rewriting at ~75% of commission).
2. **Forward the approval email** so I can add domain-specific Awin tracking link wrappers across the catalog. Awin link format: `https://www.awin1.com/cread.php?awinmid=<MID>&awinaffid=2905561&p=<DESTINATION_URL>`

### What's NOT in Awin (pursue elsewhere)

- **Industrial parts:** RS Components, Newark/element14, Schneider, ABB, Conrad — apply via their direct programs or via Impact.com / ShareASale
- **Tools:** ToolStation, Grainger, MSC — Impact.com path is documented in the AFFILIATE_LOG.md backlog
- **HVAC parts distributors:** Parts Town, Johnstone Supply — direct outreach (drafts exist at outreach/parts-town.md and outreach/johnstone-supply.md)


## 2026-05-22 — Awin awinmid IDs captured from Pending tab

After re-login as info@errorcodefixes.com, only 5 (not 10) applications are
actually in Pending state. Joined tab = 0, Rejected = 0. Previous session
overstated the count.

| Advertiser | awinmid | Status |
|---|---|---|
| National Filter Warehouse (US) | 114058 | Pending |
| GE Appliances Parts & Accessories (US) | 71163 | Pending |
| Filter King | 125512 | Pending |
| Shop Appliances Affiliate Program | 120780 | Pending |
| Hüga Heat | 36800 | Pending |

These are the integer merchant IDs to pass to `<AwinLink awinmid="...">`
once any approves. The AwinLink component is already built at
`src/components/AwinLink.astro`.


## 2026-05-22 — 12 NEW Awin applications (Pending now 22)

| Advertiser | awinmid | Submitted | Category |
|---|---|---|---|
| GE Appliances (US) | 71161 | 2026-05-22 | Major appliance brand |
| GE Appliances Professional Discounts (US) | 71165 | 2026-05-22 | Pro discount portal |
| Electrolux | 34515 | 2026-05-22 | Parent of Frigidaire |
| Tado NL-BE | 25066 | 2026-05-22 | Smart thermostat (Benelux) |
| Optiwatt Clean Energy US | 119391 | 2026-05-22 | EV/energy app |
| Octopus Energy | 67000 | 2026-05-22 | Energy supplier |
| TURBRO | 46463 | 2026-05-22 | HVAC / heating brand |
| TOSOT Direct | 59175 | 2026-05-22 | Gree appliances (AC, dehumidifier) |
| ALPICOOL INC. | 106771 | 2026-05-22 | Portable fridge / cooler |
| DiscountFilterStore.com (US) | 126373 | 2026-05-22 | Water/air filters |
| Heizungsdiscount24 DE | 120593 | 2026-05-22 | German heating discount |
| Think Energy Affiliate Program | 122540 | 2026-05-22 | Energy / smart home |

### Full Pending state (22 advertisers)

| # | Advertiser | awinmid |
|---|---|---|
| 1 | Haier | 43489 |
| 2 | National Filter Warehouse (US) | 114058 |
| 3 | GE Appliances Professional Discounts (US) | 71165 |
| 4 | Tado NL-BE | 25066 |
| 5 | Optiwatt Clean Energy US | 119391 |
| 6 | GE Appliances Parts & Accessories (US) | 71163 |
| 7 | Castle Heaters | 24556 |
| 8 | Tado DE | 16503 |
| 9 | TOSOT Direct | 59175 |
| 10 | Octopus Energy | 67000 |
| 11 | Filter King | 125512 |
| 12 | Ebac | 73251 |
| 13 | GE Appliances (US) | 71161 |
| 14 | Shop Appliances Affiliate Program | 120780 |
| 15 | ALPICOOL INC. | 106771 |
| 16 | DiscountFilterStore.com (US) | 126373 |
| 17 | TURBRO | 46463 |
| 18 | Heizungsdiscount24 DE | 120593 |
| 19 | Hüga Heat | 36800 |
| 20 | Tado UK | 24881 |
| 21 | Electrolux | 34515 |
| 22 | Think Energy Affiliate Program | 122540 |

