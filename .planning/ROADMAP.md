# Roadmap — Error Code Fixes Consumer Orientation v1 (council-revised 2026-06-06)

North Star: **mC/1000** (monetized affiliate clicks per 1,000 engaged sessions).

Revised after a heavy multi-LLM council (Claude + GPT + DeepSeek + Gemini chairman).
Unanimous direction: "amazing" = a technician's confidence for a panicked person on a
phone. Win on **diagnostic precision, honesty, a distinctive service-manual design, and
a linkable tool**, NOT on scaling thin templated pages (the #1 Helpful-Content risk).
Strategy = raise the template floor for every page, go DEEP on the top commercial-intent
pages, quality-gate the thin majority, and build linkable assets to pull traffic.

| # | Phase | Goal | Status |
|---|-------|------|--------|
| 1 | Consumer Coherence & Internal Links | Pages link right, no pivot/E-E-A-T leaks | SHIPPING |
| 2 | Diagnosis Command Center redesign | Amazing service-manual template + identity that lifts every page | NEXT |
| 3 | Re-anchor the autonomous engine | Consumer-only generation, tuned to the new deep bar | pending |
| 4 | Deep money pages (top ~150-200) | Make the highest-intent guides the best on the internet | pending |
| 5 | Quality-gate + code-search precision | Hide/upgrade thin pages; fix code search | pending |
| 6 | Link & traffic engine | /diagnose tool + link magnets to pull links/traffic at ~0 traffic | pending |
| 7 | Measurement, guardrails & iteration | Measure mC/1000 + indexing; stay HCU-safe | pending |

---

## Phase Details

### Phase 1: Consumer Coherence & Internal Links — SHIPPING
Done: consumer brand-hub links (UX-01), related-posts relevance + draft exclusion (UX-02),
de-industrialized logo/chat/FAQ schema (UX-03/04), honest editorial attribution (UX-05),
ad-void collapse (UX-06), search-index noise removed (UX-07), FAQ brand-bug fix, meta-author
honesty, AmazonPartLink category fix. UX-08 (DIY-vs-pro label) deferred into generators.

### Phase 2: Diagnosis Command Center redesign (the "amazing")
**Goal:** A distinctive, trustworthy, mobile-first service-manual design and a rebuilt
article template that raises the quality floor of every page automatically.
**Success criteria:**
1. Visual identity shipped: service blue (#1B2A4A) + safety amber accent (action/warning only)
   + paper off-white; monospace for error codes and part numbers; original art, no stock.
2. Article template rebuilt: code-as-hero (mono), most-likely-cause verdict + confidence,
   Safe-to-run badge, native `<details>` decision tree, honest "when to call a pro" with
   cost math, exact-part box, sticky mobile "get the part" bar that appears post-diagnostic.
3. Homepage moves toward a triage funnel ("What's broken?" → "What's it doing?") while
   keeping code search; honest "independent, not a parts store" trust line.
4. Verified in-browser (desktop + mobile), council/codex-reviewed, gauntlet-scored before ship.
5. Build passes; deploys green; Core Web Vitals not regressed (LCP < 2.5s mobile target).

### Phase 3: Re-anchor the autonomous engine
**Goal:** Daily pipeline makes consumer-only content, tuned to the new deep template bar.
**Success criteria:**
1. Topic selection excludes industrial brands/appliances; dry-run yields only consumer topics.
2. Generators emit the new deep structure (verdict, decision-tree branches, verified part,
   cost math, pro/DIY signal for the AtAGlance label) — not the old thin 4-causes/6-steps.
3. One cycle publishes zero industrial pages and zero pages below the new quality bar.

### Phase 4: Deep money pages (top ~150-200 commercial-intent)
**Goal:** Make the highest-intent error-code + part pages the best resources on the internet.
**Success criteria:**
1. Top ~150-200 codes/parts selected by commercial intent (clear $30-150 DIY part) and demand.
2. Each upgraded to depth: confident verdict, verified OEM part number, model-variant notes,
   misdiagnosis warning, decision tree, honest cost math, original diagram/photo where feasible.
3. Each cross-links related codes/symptoms/parts + brand hub; agent storms do DEPTH not breadth.
4. Fresh adversarial QA sample ≥ 90% clean; no cross-brand contamination; honest claims only.

### Phase 5: Quality-gate + code-search precision
**Goal:** Stop the thin majority dragging the domain; make code search return the right page.
**Success criteria:**
1. Analysis pass classifies every page (deep / salvageable / thin-duplicate) with a report.
2. Thin/duplicate pages that cannot be upgraded are noindexed or consolidated (reversible,
   reviewed) so the domain is judged on its strong average.
3. Bare-code search ("LE","OE","5E","F21") returns the canonical brand+appliance guide near
   the top with low noise; an ambiguous code gets a disambiguation affordance.

### Phase 6: Link & traffic engine
**Goal:** Pull links and traffic at ~0 organic traffic; create destination assets.
**Success criteria:**
1. `/diagnose` interactive symptom checker (client-side, static result routes) shipped and shareable.
2. Link magnets shipped: brand service-mode cheat sheets, model-number-location gallery,
   error-code master reference (downloadable). Seeded honestly on relevant forums/communities.
3. Client-side brand+code search and model finder in the header.

### Phase 7: Measurement, guardrails & iteration
**Goal:** Measure what matters; stay clear of a Helpful-Content penalty.
**Success criteria:**
1. Local GSC visibility restored (indexed count + impressions/clicks per page).
2. mC/1000 computed from analytics + affiliate click events and trending.
3. Quality watch flags thin/low-CTR pages; pre-scale adversarial QA gate before any scale-up.

---

## Key strategic decision (council-driven, 2026-06-06)
Depth + distinctive design + linkable tool > scaling thin templated pages. The ~3,500-page
templated corpus is the top HCU risk per all four advisors. We raise the floor (template),
concentrate firepower (top ~150-200), and quality-gate the rest — deliberately, after analysis,
not rashly. Legacy industrial pages stay live for now (prior decision) but are candidates for
the Phase 5 quality-gate. Affiliate routing favors OEM/verified sellers; trust > a single click.
