# Requirements — Consumer Orientation v1

REQ-ID format: `[CATEGORY]-[NN]`. Each maps to exactly one phase (see Traceability).

## v1 Requirements

### UX & Internal Linking (UX)

- [ ] **UX-01**: Every consumer-brand page (Samsung/LG/Whirlpool/GE/Frigidaire/Maytag/
  Bosch/KitchenAid/Kenmore/Electrolux/Amana + more) shows a working "See all {brand}
  error codes" link to its brand hub.
- [ ] **UX-02**: Related Fix Guides on a page are topically relevant (same brand +
  appliance first, then same appliance, then brand) — never the 4 newest random pages.
- [ ] **UX-03**: No industrial wording in site chrome — logo alt/aria text reads as a
  consumer appliance brand, not "Industrial Error Code Fixes".
- [ ] **UX-04**: FAQ schema is brand+appliance-appropriate and not identical industrial
  boilerplate templated across every page.
- [ ] **UX-05**: Author/reviewer attribution is honest (no fabricated named experts with
  safety credentials on YMYL content); E-E-A-T is truthful.
- [ ] **UX-06**: No empty ad/whitespace void mid-article (ad slots suppressed until live).
- [ ] **UX-07**: Search snippets are clean — UI chrome ("Copy") and the author byline are
  excluded from the Pagefind index.
- [ ] **UX-08**: The at-a-glance difficulty strip never says "DIY" on a guide whose fix is
  gated to a professional.
- [ ] **UX-09**: Homepage category icons/labels read as appliances (no mismatched emoji).

### Engine & Search (ENG)

- [ ] **ENG-01**: The daily autonomous pipeline generates consumer-only topics (no
  industrial brands/appliances re-enter the published set).
- [ ] **ENG-02**: Industrial seeds are purged from the code pool and topic miner so drift
  cannot recur.
- [ ] **ENG-03**: A bare code search (e.g. "LE", "OE", "5E", "F21") surfaces the correct
  brand+appliance guide at or near the top, with low-noise ranking.
- [ ] **ENG-04**: A code-disambiguation affordance routes an ambiguous code to the right
  brand/appliance (e.g. "LE" → LG washer vs Samsung washer).
- [ ] **ENG-05**: A full content build + deploy completes fast enough to ship paced daily
  waves without the build time becoming the bottleneck.

### Content Build-out (CON)

- [ ] **CON-01**: DIY part-replacement pages cover the common failure parts for each
  consumer appliance across the top brands (the highest-conversion type).
- [ ] **CON-02**: Symptom pages cover both branded ("Samsung washer won't drain") and
  generic ("dishwasher not draining") high-volume queries.
- [ ] **CON-03**: Model-specific long-tail pages cover the common model numbers per brand.
- [ ] **CON-04**: Error-code coverage is weighted toward DIY-fixable codes (a buyable part)
  over pro-only codes, and is verified-accurate per brand+appliance.
- [ ] **CON-05**: Reset / maintenance / how-to guides cover common funnel intents
  (reset {brand} {appliance}, clean filter, descale, etc.).
- [ ] **CON-06**: Coverage extends to missing brands (Miele, Speed Queen, Café, Haier,
  Fisher & Paykel, Asko, Thermador) and appliances (freezers, garbage disposals, ice
  makers, cooktops, range hoods, central AC, thermostats).
- [ ] **CON-07**: Every new page is Perplexity-grounded and passes the claude_review gate
  (score ≥ 7, real content) or is held as draft; no cross-brand code-meaning contamination.
- [ ] **CON-08**: Each new page cross-links to its related codes/symptoms/parts and brand
  hub at creation time (compounds internal linking).

### Conversion (CONV)

- [ ] **CONV-01**: Each page presents one clear primary "Get the exact part" CTA above the
  fold of the fix, with secondary options de-emphasized (resolve Amazon vs Skimlinks).
- [ ] **CONV-02**: Pro-only pages offer a relevant non-dead-end action (find a local pro /
  the few buyable parts) instead of a buy CTA with nothing to buy.

### Measurement & Guardrails (MEAS)

- [ ] **MEAS-01**: Local GSC visibility is restored (indexed count, impressions, clicks per
  page) so progress is measured, not guessed.
- [ ] **MEAS-02**: mC/1000 (monetized affiliate clicks per 1,000 engaged sessions) is
  tracked from analytics + affiliate click events.
- [ ] **MEAS-03**: An HCU/quality watch flags thin, duplicative, or low-CTR pages for prune
  or improvement.
- [ ] **MEAS-04**: A fresh sample of newly generated pages is adversarially QA'd before each
  scale-up (the "don't scale until proven" gate).

## v2 / Deferred

- AdSense activation (display ads) once approved and once it won't degrade UX
- Pinterest pin blast (blocked on Pinterest's external pins:write approval)
- Programmatic comparison / part-number landing pages ("WPW10730972 — what it fits")

## Out of Scope

- Deleting legacy industrial pages — leave live for now (may hold current rankings)
- Re-platforming, paid acquisition, owned checkout, native app (see PROJECT.md)

## Traceability

| REQ-ID | Phase |
|--------|-------|
| UX-01, UX-02, UX-03, UX-04, UX-05, UX-06, UX-07, UX-08, UX-09 | Phase 1 |
| ENG-01, ENG-02 | Phase 2 |
| ENG-03, ENG-04 | Phase 3 |
| CON-01, CON-07, CON-08 | Phase 4 |
| CON-02, CON-03, CON-04, CON-06 | Phase 5 |
| CONV-01, CONV-02, CON-05, ENG-05 | Phase 6 |
| MEAS-01, MEAS-02, MEAS-03, MEAS-04 | Phase 7 |
