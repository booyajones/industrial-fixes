# Project State — Error Code Fixes Consumer Orientation

## Project Reference

See: .planning/PROJECT.md (updated 2026-06-05)

**Core value:** A consumer finds the real cause of their error code/symptom and the
exact part to fix it in under a minute, and we earn a commission when they buy it.
**North Star:** mC/1000 (monetized affiliate clicks / 1,000 engaged sessions).
**Current focus:** Phase 1 — Consumer Coherence & Internal-Link Foundation.

## Status (council-revised roadmap, see ROADMAP.md)

| # | Phase | Status |
|---|-------|--------|
| 1 | Consumer Coherence & Internal Links | SHIPPED + verified live (commits b1c9ac8d) |
| 2 | Diagnosis Command Center redesign | 2a IDENTITY SHIPPED (c93dfdbe): navy mono code-hero, honest trust line, service-blue + semantic tokens, mono codes. 2b PENDING: decision tree, verdict+confidence, Safe-to-run badge, cost-math pro section, sticky mobile part bar, homepage triage, branded OG image |
| 3 | Re-anchor the autonomous engine (deep) | NEXT: upgrade generators to Command Center content schema (verdict, misdiagnosis warning, cost math, accurate DIY/pro signal, decision-tree branches). Test on a DRY SAMPLE before any storm — this is the autonomous daily pipeline. |
| 4 | Deep money pages (top ~150-200) | pending (agent storm after Phase 3 generator upgrade + sample QA) |
| 5 | Quality-gate + code-search precision | pending |
| 6 | Link & traffic engine (/diagnose + magnets) | pending |
| 7 | Measurement, guardrails & iteration | pending |

## Next-effort entry point
Phase 3 generator upgrade: read scripts/generate-articles.py (574 lines) fully; extend the
claude_write schema (line ~320) with most_likely_cause + confidence, misdiagnosis_warning,
cost_diy + cost_pro, diy_or_pro; update the assemble template (line ~440) + claude_review gate;
add corresponding render in PostDetails (verdict block, Safe-to-run/diy badge with semantic
colors, cost-math "when to call a pro", native <details> decision tree). DRY-RUN test on ~5
codes and adversarially QA before regenerating top pages. UX-08 (DIY/pro label accuracy)
resolves here via the new diy_or_pro content signal.

## Baseline (2026-06-05)

- Published: ~3,561 pages (~63% consumer, ~12% legacy industrial, rest mixed). Drafts: 731.
- Money: ~$0. Traffic ~0 (content days old). Indexing = multi-week clock = binding constraint.
- GSC: not readable locally (service-account JSON absent on this machine) — restore in Phase 7.
- Known generator + QA fixes already landed (cross-brand code contamination root-caused/fixed).

## Execution Model

- Code/template fixes (Phases 1-3, 6): deterministic source edits + browser/build verify.
- Content build-out (Phases 4-5): deterministic Python generators (Perplexity + Claude,
  jobs=3, retry/backoff) orchestrated/QA'd by Workflow agent storms. Subagents cannot
  write to the repo; only Python does.
- Ship: build-gate (npm run build) → fetch + conditional-rebase + push → Cloudflare → verify 200 → IndexNow.

---
*Last updated: 2026-06-05 after initialization*
