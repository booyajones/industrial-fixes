# Industrial Error Code — Revenue-First Topic Plan

**Framework:** Topics ranked by composite revenue score = (Part AOV × Monthly Search Volume × Downtime Urgency × Amazon Availability). Higher score = faster revenue.

**Not covered** = confirmed absent from `src/data/blog/` as of 2026-04-24.

---

## Scoring Rubric

| Factor | Weight | Rationale |
|--------|--------|-----------|
| Part AOV ($) | 30% | Higher parts spend = higher affiliate commission |
| Monthly search volume | 25% | Traffic floor determines revenue ceiling |
| Downtime urgency | 25% | High urgency → same-day parts purchase, not comparison shopping |
| Amazon parts availability | 20% | Can't earn commission if parts aren't on Amazon |

**Revenue Score** = composite 0–100. Tier 1 = 85+. Tier 2 = 70–84. Tier 3 = 55–69.

---

## TIER 1 — Write These First (Score 85–100)

### #1 — Schneider Electric Altivar ATV71 Fault Codes
- **Revenue Score: 96**
- **Why:** ATV71 is Schneider's dominant HVAC/pump drive — hundreds of thousands installed in North American commercial buildings, water plants, and process facilities. Drives run $600–$2,500. Key faults (OBF, OCF, OHF, USF) are searched constantly during building equipment failures. The ATV61 (single-fault article) is in the repo but **ATV71 has no coverage at all**.
- **Part AOV:** $700 avg (drive replacement + braking resistor + control board)
- **Est. monthly searches:** 2,400 (ATV71 fault codes, ATV71 OBF, ATV71 OCF, ATV71 overtemp)
- **Downtime urgency:** Very High — chiller plants, AHUs, cooling towers
- **Amazon availability:** High — Schneider drives and accessories widely listed
- **Target slug:** `schneider-atv71-fault-codes`
- **Content:** Full fault table (OBF, OCF, OHF, USF, PHF, SOF, LFF, bUF), 8-step diagnosis, 6-entry parts table

### #2 — Yaskawa P1000 (CIMR-PU) Fault Codes
- **Revenue Score: 93**
- **Why:** The P1000 is Yaskawa's HVAC/pump-specific drive, one of the most-specified drives in commercial building fan and pump applications. Widely installed from ~2010 onward, so the fleet is now aging into service calls. Drives run $800–$3,000. Key faults (OC, OV, UV1, OH, LF) are well-searched. **No P1000-specific article in repo** (only A1000, GA700, V1000 covered).
- **Part AOV:** $600 avg
- **Est. monthly searches:** 1,800 (Yaskawa P1000 fault codes, P1000 OC fault, CIMR-PU error codes)
- **Downtime urgency:** Very High — commercial HVAC, pumping stations
- **Amazon availability:** High
- **Target slug:** `yaskawa-p1000-fault-codes`
- **Content:** Full fault table, OC/OV/UV1/OH/LF diagnosis, parameter tuning (C1-01, L3-04, E2-01), parts table

### #3 — Danfoss VLT Micro Drive FC 51 Fault Codes
- **Revenue Score: 88**
- **Why:** The FC 51 is Danfoss's entry-level drive, used in tens of thousands of small HVAC, pump, and conveyor applications. It's a replacement cycle driver — older units fail and get swapped. Key faults (AL.13 overvoltage, AL.14 undervoltage, AL.29 heatsink overtemp) are searched constantly. **Not in repo** — Danfoss coverage is FC102, FC301, FC302, VLT 2900 only.
- **Part AOV:** $350 avg (complete drive replacements are common at this price point)
- **Est. monthly searches:** 1,500 (Danfoss FC 51 alarm, FC51 AL 29, Danfoss Micro Drive fault)
- **Downtime urgency:** High — HVAC and pump applications
- **Amazon availability:** High — FC51 drives and accessories on Amazon
- **Target slug:** `danfoss-vlt-micro-fc51-fault-codes`
- **Content:** Full alarm table, heatsink cleaning procedure, fan replacement, parts table

---

## TIER 2 — High Value, Write After Tier 1 (Score 70–84)

### #4 — ABB ACS355 Complete Fault Code Guide (Score: 85)
- **Why:** ACS355 (compact industrial drive) has only two single-fault articles (2330, 3130). A complete guide capturing 2310, 3210, 3220, 4110, 7121 searches would consolidate traffic. Drives $400–$1,800.
- **Target slug:** `abb-acs355-fault-codes`

### #5 — Siemens SINAMICS V90 Fault Codes (Score: 83)
- **Why:** V90 is Siemens' small servo drive, very common in packaging and material handling. F07900, F30001, F52100 are well-searched. No V90-specific article in repo. Drives $500–$2,000.
- **Target slug:** `siemens-sinamics-v90-fault-codes`

### #6 — Allen-Bradley PowerFlex 755 Fault F12 / F14 (Score: 81)
- **Why:** PF755 is the high-end 700/750 series replacement. Very high AOV ($800–$2,500 for replacement drives). F12 (HW overcurrent) and F14 (ground fault) are top searched. F7 (fault-7) is covered but F12/F14 are not.
- **Target slug:** `allen-bradley-powerflex-755-f12-fault`

### #7 — Mitsubishi FR-F800 VFD Fault Codes (Score: 79)
- **Why:** FR-F800 is Mitsubishi's HVAC/fan-specific drive, widely used in Japan and increasingly in North American commercial HVAC. FR-A800 is covered but FR-F800 is not. E.OC1, E.OV1, E.THM are top searched.
- **Target slug:** `mitsubishi-fr-f800-fault-codes`

### #8 — Bosch Rexroth IndraDrive C Fault Codes (Score: 78)
- **Why:** IndraDrive is common in injection molding presses and die casting — very high AOV ($1,500–$5,000 drives). F2100 (overcurrent), F2120 (overvoltage), E8079 (motor overtemp) are well-searched. Amazon availability is partial (some components; drives from industrial suppliers).
- **Target slug:** `bosch-rexroth-indradrive-fault-codes`

### #9 — Yaskawa J1000 (CIMR-JA) Fault Codes (Score: 72)
- **Why:** J1000 is Yaskawa's smallest/cheapest drive, used in huge OEM quantities. Very high install base → high search volume. Drives are cheap ($150–$400) but volume compensates. OC, OV, UV1, OH are top faults.
- **Target slug:** `yaskawa-j1000-fault-codes`

### #10 — Siemens SINAMICS G120 F30001 Overcurrent (Score: 70)
- **Why:** G120 is in the repo (G120, G120C, G120X) with general fault articles, but F30001 (power unit overcurrent — the most common hard fault) has no dedicated article. Power unit faults are parts-replacement events ($600–$1,500 for power modules).
- **Target slug:** `siemens-g120-fault-f30001`

---

## TIER 3 — Long-Tail / Lower Volume (Score 55–69)

- Omron MX2 (3G3MX2) fault codes — OEM machine drive, moderate volume
- Lenze i550 fault codes — newer drive, growing install base
- Yaskawa Z1000 (CIMR-ZU) fault codes — HVAC variant, similar to P1000
- Parker AC10 VFD fault codes — common in water/waste water
- WEG CFW11 fault codes — growing in North America, high AOV

---

## Assessment of Wave 4 Articles Already Written

Wave 4 created 5 articles before this plan was written. Assessment against revenue-first criteria:

| File | Revenue Score | Verdict |
|------|--------------|---------|
| `allen-bradley-powerflex-4m-fault-codes.md` | 85 | ✅ **KEEP** — High-install-base OEM drive, fits Tier 1-adjacent |
| `abb-acs580-fault-codes.md` | 82 | ✅ **KEEP** — General-purpose drive, water/HVAC, fits Tier 2 well |
| `yaskawa-sigma7-sgd7s-alarm-codes.md` | 75 | ✅ **KEEP** — High AOV servo, fits Tier 2, lower volume but high urgency |
| `mitsubishi-mr-j4-servo-alarm-codes.md` | 72 | ✅ **KEEP** — High AOV servo, Tier 2 level, machining center downtime |
| `siemens-sinamics-s120-fault-f07900.md` | 68 | ⚠️ **MARGINAL** — Specialized CNC servo, lower search volume; keep because content quality is high and AOV is very high, but deprioritize for future batches |

**Bottom line:** All 5 Wave 4 articles are worth keeping — none are wasted. The PowerFlex 4M and ACS580 are the strongest earners in the batch. Going forward, the **next batch** should lead with Schneider ATV71, Yaskawa P1000, and Danfoss FC51 (the true Tier 1 revenue topics).

---

## Recommended Execution Order (Next Batches)

**Wave 5 (Batch Next):** Schneider ATV71 (#1) + Yaskawa P1000 (#2) + Danfoss FC51 (#3)  
**Wave 6:** ABB ACS355 complete (#4) + Siemens V90 (#5) + PF755 F12 (#6)  
**Wave 7:** Mitsubishi FR-F800 (#7) + Rexroth IndraDrive (#8) + Yaskawa J1000 (#9)

---

*Last updated: 2026-04-24 | Repo: industrial-fixes | Generated by: Wave 4 pivot analysis*
