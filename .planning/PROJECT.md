# Error Code Fixes — Consumer Orientation

## What This Is

errorcodefixes.com is a free, ad-and-affiliate-supported library of appliance
error-code, symptom, part-replacement, and model repair guides for ordinary
consumers (someone standing at a washer flashing "LE" with a phone in hand). It
earns money when a reader clicks through to buy the exact replacement part
(Amazon Associates + Skimlinks to RepairClinic / PartSelect). It began life as an
*industrial* error-code site and is mid-pivot to consumer appliances.

## Core Value

A consumer with a broken appliance finds the real cause of their error code or
symptom AND the exact part to fix it, in under a minute, and we earn a commission
when they buy that part. If everything else fails, that one path must work.

## Requirements

### Validated

<!-- Shipped and confirmed working (brownfield, observed live this session). -->

- ✓ Consumer homepage, 9 appliance categories, instant search — live
- ✓ ~3,561 published pages (~63% consumer); 731 unreliable pages correctly drafted
- ✓ Article template with answer-first Quick Answer, difficulty/time/tools strip,
  FTC disclosure, Amazon-link-as-button styling, category-routed parts specialist,
  intent-timed email capture, breadcrumb + FAQ schema, responsive nav, dark mode
- ✓ Grounded generation engine (Perplexity + Claude write + claude_review gate),
  four generators (codes / parts / symptoms / models), thread-pooled with backoff
- ✓ Daily autonomous cloud pipeline (article-gen, pins, IndexNow/Bing submission)

### Active

<!-- This milestone. Hypotheses until shipped + validated by GSC/conversion data. -->

- [ ] Every consumer page links correctly to its brand hub and topically-related guides
- [ ] No industrial/pivot leaks in chrome, schema, or author E-E-A-T
- [ ] The autonomous engine generates consumer-only content (no industrial drift)
- [ ] Code search returns the right brand+appliance page for a bare code
- [ ] A large, paced, grounded build-out of DIY part-replacement, symptom, model,
      and DIY-fixable-code pages across the full consumer brand/appliance matrix
- [ ] One clear primary "get the part" CTA per page (no competing affiliate CTAs)
- [ ] We can measure indexing + mC/1000 and stay clear of a Helpful-Content penalty

### Out of Scope

- Deleting/de-listing the ~428 legacy industrial pages — Chris decided to leave
  them live for now (they may carry our only current rankings); just stop adding more
- Re-platforming off Astro/AstroPaper or Cloudflare Pages — works, no reason to churn
- Paid acquisition / ads spend — the model is organic SEO + affiliate
- Building our own parts store / checkout — we are an affiliate referrer, not a retailer
- Mobile-native app — the web experience is the product

## Context

- Stack: Astro + AstroPaper v5 static site. Repo booyajones/industrial-fixes.
  Deploy = push to main → GitHub Actions deploy.yml → Cloudflare Pages.
- Search is Pagefind (client-side index). Edge cache: s-maxage=300, swr=86400.
- Money is ~$0 today: content is days old, Google indexing is a multi-week clock.
  Traffic, not output rate, is the binding constraint on revenue timing.
- A two-swarm adversarial QA found ~20% code-accuracy errors concentrated in
  HVAC/mini-split (cross-brand contamination); those are now drafted, generator
  root cause fixed. Mainstream washer/dryer/fridge/dishwasher codes + all parts/
  symptoms/models sampled clean.
- Empirical UX audit (this session) surfaced the Active requirements above.

## Constraints

- **Generation**: Anthropic .env key has low concurrency (~3-4, shared with Finexio).
  Run deterministic Python at jobs=3 with 429/5xx retry+backoff. Subagents can only
  Write within session root (C:\Users\chris\OneDrive\Desktop\Claude), NOT the repo —
  so content is produced by Python, not subagent file writes.
- **HCU safety**: paced waves (~150-300/day), varied templates, every page grounded
  + claude_review gated. Quality and topical focus over raw count.
- **Brand voice**: no em dashes, no semicolons, no banned words (ensure/crucial/
  vital/leverage/robust/seamless). Peer, plain, technician tone.
- **Build perf**: ~20 min at current page count; a throughput constraint on waves.
- **Push race**: daily [cloud] pipeline commits to main; pushes need fetch +
  conditional-rebase + retry.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Leave legacy industrial pages live | May hold our only current rankings; low effort to ignore | — Pending |
| Fix internal-linking template BEFORE scaling content | New content must compound through links, not just pile up | — Pending |
| Weight content toward DIY-fixable, part-driven pages | Pro-only codes are conversion dead ends; DIY parts are the buy moment | — Pending |
| Execute content via deterministic Python + Workflow storms | Subagents can't write to repo; .env key is rate-limited | — Pending |
| North Star = mC/1000 | Ties effort to money, not vanity page count | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition:**
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone:**
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state (traffic, mC/1000, indexed count)

---
*Last updated: 2026-06-05 after initialization*
