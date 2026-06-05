# Project State — Error Code Fixes Consumer Orientation

## Project Reference

See: .planning/PROJECT.md (updated 2026-06-05)

**Core value:** A consumer finds the real cause of their error code/symptom and the
exact part to fix it in under a minute, and we earn a commission when they buy it.
**North Star:** mC/1000 (monetized affiliate clicks / 1,000 engaged sessions).
**Current focus:** Phase 1 — Consumer Coherence & Internal-Link Foundation.

## Status

| # | Phase | Status |
|---|-------|--------|
| 1 | Consumer Coherence & Internal-Link Foundation | NEXT |
| 2 | Re-anchor the Autonomous Engine | pending |
| 3 | Code-Search Precision | pending |
| 4 | DIY Part-Replacement Engine | pending |
| 5 | Symptom + Model + DIY-Code Breadth | pending |
| 6 | Conversion + Maintenance + Build Perf | pending |
| 7 | Measurement, Guardrails & Iteration | pending |

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
