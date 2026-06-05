# Roadmap — Error Code Fixes Consumer Orientation v1

**7 phases** | **27 requirements mapped** | All v1 requirements covered ✓

North Star: **mC/1000** (monetized affiliate clicks per 1,000 engaged sessions).
Dependency logic: fix the surfaces that make content compound (links, search) and
stop the industrial leak BEFORE scaling content, then scale, then optimize conversion,
then measure.

| # | Phase | Goal | Requirements | Success Criteria |
|---|-------|------|--------------|------------------|
| 1 | Consumer Coherence & Internal-Link Foundation | Every consumer page links right and carries zero pivot leaks | UX-01..UX-09 | 5 |
| 2 | Re-anchor the Autonomous Engine | The daily engine makes consumer-only content; drift can't recur | ENG-01, ENG-02 | 3 |
| 3 | Code-Search Precision | A bare code finds the right brand+appliance page fast | ENG-03, ENG-04 | 3 |
| 4 | DIY Part-Replacement Engine (the money type) | Big, paced, grounded build-out of the highest-conversion pages | CON-01, CON-07, CON-08 | 4 |
| 5 | Symptom + Model + DIY-Code Breadth | Cover the full consumer matrix incl. missing brands/appliances | CON-02, CON-03, CON-04, CON-06 | 4 |
| 6 | Conversion + Maintenance + Build Perf | One clear part CTA, funnel how-tos, fast ships | CONV-01, CONV-02, CON-05, ENG-05 | 4 |
| 7 | Measurement, Guardrails & Iteration | Measure indexing + mC/1000, stay HCU-safe | MEAS-01..MEAS-04 | 4 |

---

## Phase Details

### Phase 1: Consumer Coherence & Internal-Link Foundation
**Goal:** Every consumer page links to its brand hub and topically-relevant guides, and
the site carries no industrial or dishonest-attribution leaks. Do this FIRST so all
subsequent content compounds through internal links instead of piling up.
**Requirements:** UX-01, UX-02, UX-03, UX-04, UX-05, UX-06, UX-07, UX-08, UX-09
**UI hint:** yes
**Success criteria:**
1. On a sample of consumer-brand pages, the brand-hub link renders and resolves 200.
2. Related Fix Guides on a dryer page are dryer/brand-relevant, never random microwaves.
3. View-source on any page shows consumer logo alt/aria, brand+appliance-aware FAQ schema,
   and honest reviewer attribution.
4. No empty ad void renders mid-article; Pagefind snippets contain no "Copy"/byline noise.
5. `npm run build` passes (mojibake + astro check) and the changes deploy green.

### Phase 2: Re-anchor the Autonomous Engine
**Goal:** The daily pipeline generates consumer-only topics; industrial drift cannot recur.
**Requirements:** ENG-01, ENG-02
**UI hint:** no
**Success criteria:**
1. Topic selection (gsc_demand / reddit / code_pool / miner) excludes industrial brands
   and appliances; a dry-run of the daily generator yields only consumer topics.
2. `.code-pool.json` and mine-code-lists seeds contain no VFD/PLC/servo/industrial entries.
3. One full daily-pipeline cycle (or simulation) publishes zero industrial pages.

### Phase 3: Code-Search Precision
**Goal:** A bare code search returns the correct brand+appliance guide near the top.
**Requirements:** ENG-03, ENG-04
**UI hint:** yes
**Success criteria:**
1. Searching "LE", "OE", "5E", "F21" surfaces the canonical brand+appliance guide in the
   top results (not an off-appliance page), with materially less noise than the 708-for-LE baseline.
2. An ambiguous bare code presents a brand/appliance disambiguation affordance.
3. Change is verified in-browser on the live (or preview) site.

### Phase 4: DIY Part-Replacement Engine (the money type)
**Goal:** A large, paced, grounded build-out of DIY part-replacement pages across the
consumer appliance × brand matrix — the highest-conversion content.
**Requirements:** CON-01, CON-07, CON-08
**UI hint:** no
**Success criteria:**
1. A demand pass expands the parts universe (appliance × common failure parts × top brands).
2. Paced waves publish grounded, gated part-replacement pages (draft on gate-fail).
3. Each published page cross-links to related codes/symptoms and its brand hub.
4. A fresh adversarial QA sample of the new parts pages is ≥ 90% clean before scaling further.

### Phase 5: Symptom + Model + DIY-Code Breadth
**Goal:** Cover the full consumer demand spectrum — branded + generic symptoms, model
long-tail, DIY-fixable codes — and add the missing brands and appliances.
**Requirements:** CON-02, CON-03, CON-04, CON-06
**UI hint:** no
**Success criteria:**
1. Symptom pages exist for branded and generic high-volume queries per appliance.
2. Model long-tail and DIY-fixable-code waves ship, grounded + gated, weighted away from pro-only.
3. New brands (Miele, Speed Queen, Café, Haier, Fisher & Paykel, Asko, Thermador) and
   appliances (freezers, disposals, ice makers, cooktops, range hoods, central AC, thermostats)
   have at least starter coverage.
4. Fresh QA sample across the new types is ≥ 90% clean; no cross-brand contamination.

### Phase 6: Conversion + Maintenance + Build Perf
**Goal:** Turn the landing traffic into affiliate clicks, fill the funnel with how-tos,
and make builds fast enough to ship daily.
**Requirements:** CONV-01, CONV-02, CON-05, ENG-05
**UI hint:** yes
**Success criteria:**
1. Each page shows one clear primary "Get the exact part" CTA; competing CTAs de-emphasized.
2. Pro-only pages offer a relevant non-dead-end action instead of an empty buy prompt.
3. Reset/maintenance how-to guides are published for common intents.
4. Full build+deploy time is materially reduced from the ~20-min baseline.

### Phase 7: Measurement, Guardrails & Iteration
**Goal:** Measure what matters and stay clear of a Helpful-Content penalty.
**Requirements:** MEAS-01, MEAS-02, MEAS-03, MEAS-04
**UI hint:** no
**Success criteria:**
1. Local GSC visibility restored: indexed count + impressions/clicks per page readable on demand.
2. mC/1000 computed from analytics + affiliate click events and trending over time.
3. A quality watch flags thin/duplicative/low-CTR pages for prune-or-improve.
4. A pre-scale adversarial QA gate runs on a fresh sample before each new content scale-up.
