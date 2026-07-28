# Affiliate Link Injection Progress

## Active Programs

### Amazon Associates — tag `errorcodefixes-20` (DIRECT)
- Active on 1,103+ articles
- 100% commission (excluded from Skimlinks rewriting)

### Awin — publisher `2905561` (NETWORK) — APPROVED 2026-05-22
- 10 Awin applications submitted 2026-05-22 (Ebac, Hüga Heat, Haier, Castle Heaters, National Filter Warehouse, Filter King, GE Appliances Parts, Shop Appliances, Tado DE, Tado UK)

- Approved 2026-05-22
- Account holder: Chris Wyatt
- Sign in: https://ui.awin.com/awin-publisher-portal/
- Advertiser directory: https://ui.awin.com/awin-publisher-portal/advertiser-directory
- Strong for industrial parts and electrical distributors that don't have direct/Impact programs
- Target advertisers to apply to (in order): RS Components / RS Pro, Newark / element14 / Farnell, Conrad Electronic, Sonepar, Schneider Electric Boutique, ABB, ToolStation, plus any HVAC parts retailers visible in the directory
- After approvals, add those domains to the Skimlinks Excluded Domains list so the direct Awin commission is preserved instead of Skimlinks taking ~25%

### Skimlinks — publisher `303448X1791493` (NETWORK) — LIVE 2026-05-21
- Approved 2026-05-21
- Script deployed site-wide via `src/layouts/Layout.astro`
- Sister site `industrial-fixes-reviews` (booyajones/industrial-fixes-reviews) also wired
- Auto-rewrites outbound links to ~48,000 merchants in their network
- Covers Parts Town, RepairClinic, Home Depot, AutomationDirect, Galco, Wolf Automation, Supply House, PexUniverse, HVAC Parts Shop, TruTech Tools, Grainger, Johnstone Supply, Lowes — without per-merchant signup
- **CRITICAL CONFIG (do once in dashboard):** Settings > Domain Management > Excluded Domains > add `amazon.com`, `amzn.to`, `amazon.co.uk` so direct Amazon stays 100% commission

## Article Counts (as of 2026-05-21)
- Total articles in catalog: 1,288 (was 1,157)
- New error-code guides added 2026-05-21: 131 (covering Manitowoc E0x, Hoshizaki E2-E7, Scotsman flash codes, Mitsubishi P-codes, PowerFlex F004-F122, SINAMICS G120, ABB ACS580, Yaskawa GA800, Danfoss FC-302, plus boilers, heat pumps, tankless, Mazak, Haas, Fanuc additions, Daikin, Fujitsu, commercial dishwashers, walk-in cooler controllers, Carrier-family rebadges, premium appliances, RTUs)
- Tools/equipment buying guides added: 12 (best-multimeter-for-hvac, best-combustion-analyzer, etc.)
- Brand-vs-brand comparison pages added: 8
- All new articles have affiliate links (Amazon direct + Skimlinks-monetized merchants)

## Next Steps

1. **Do the Skimlinks Amazon exclusion** (2 min in dashboard — biggest single revenue protection)
2. Apply for direct affiliates that beat Skimlinks' 75% pass-through rate:
   - **ShareASale > AutomationDirect** (~5% on $1K-3K drives, 2-3 day approval)
   - **RepairClinic affiliate** (~7%, 5 min apply)
   - **CJ Affiliate** (unlocks PartSelect, eReplacementParts, Sears PartsDirect)
   - **Impact.com Zoro/Grainger/Parts Town** (already in pipeline per AFFILIATE_LOG.md)
3. Verify Skimlinks click tracking by clicking any non-Amazon merchant link on the site
