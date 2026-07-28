# Industrial Wave 4 — New Articles Log

## Batch Published: 2026-04-24

### 5 High-Intent Industrial Drive / CNC / Controls Error-Code Articles Added

---

### 1. Yaskawa Sigma-7 (SGD7S) Servo Drive Alarm Codes
- **File:** `src/data/blog/yaskawa-sigma7-sgd7s-alarm-codes.md`
- **Slug:** `/posts/yaskawa-sigma7-sgd7s-alarm-codes/`
- **Target keywords:** "Yaskawa Sigma-7 alarm codes", "SGD7S AL.10", "SGD7S AL.16 encoder error", "Yaskawa Sigma-7 servo fault"
- **Commercial intent:** VERY HIGH — SGD7S servo amplifiers are in CNC machines, robots, and semiconductor equipment. Replacement units cost $1,500–$8,000; encoder cables $80–$250. Plant maintenance engineers searching during axis downtime.
- **Content:** Full alarm code table (AL.10–AL.92), step-by-step megohm/encoder/encoder-battery diagnostics, SigmaWin+ data capture guidance, 5-entry parts table.
- **Why it earns:** Sigma-7 servo faults stop production lines. Engineers need the exact alarm meaning and fix procedure immediately. No generic article covers this — searches land here.

---

### 2. Mitsubishi MR-J4 Servo Amplifier Alarm Codes
- **File:** `src/data/blog/mitsubishi-mr-j4-servo-alarm-codes.md`
- **Slug:** `/posts/mitsubishi-mr-j4-servo-alarm-codes/`
- **Target keywords:** "Mitsubishi MR-J4 alarm codes", "MR-J4 AL.16 encoder error", "MR-J4 AL.30 regeneration error", "MR-J4 AL.50 overload", "Mitsubishi servo amplifier fault"
- **Commercial intent:** VERY HIGH — MR-J4 is in Mazak, DMG Mori, and Okuma machine tools across Japan and North America. Encoder cables $60–$220; regen resistors $120–$500; amplifiers $1,200–$5,500. Machine operators buying during downtime.
- **Content:** Full alarm table (AL.10–AL.9F), encoder cable inspection and continuity test procedure, regeneration circuit verification, overload mechanical check, MR Configurator2 diagnostic guidance, 5-entry parts table.
- **Why it earns:** MR-J4 alarms stop entire machining centers. Maintenance teams search exact alarm codes within minutes of the fault. This article owns that search.

---

### 3. Allen-Bradley PowerFlex 4M Fault Codes
- **File:** `src/data/blog/allen-bradley-powerflex-4m-fault-codes.md`
- **Slug:** `/posts/allen-bradley-powerflex-4m-fault-codes/`
- **Target keywords:** "Allen-Bradley PowerFlex 4M fault codes", "PowerFlex 4M F5 overvoltage", "PowerFlex 4M F12 overcurrent", "22A drive fault codes"
- **Commercial intent:** HIGH — PowerFlex 4M (catalog 22A) is one of the most deployed OEM machine drives in North America. Replacement drives $300–$800; braking resistors $60–$200. Machine builders and plant electricians searching during production stops.
- **Content:** Full fault table (F2–F63), parameter-level fix steps (P033, P034, A090), megohm test procedure, thermistor wiring check, 5-entry parts table.
- **Why it earns:** Massive install base means steady search volume. "PowerFlex 4M F5" and "PowerFlex 4M F12" are typed into Google on production floors daily. The 4M is missing from the existing repo (only PowerFlex 40/523/525/70/700/753/755 covered).

---

### 4. Siemens SINAMICS S120 Fault F07900 Motor Overtemperature
- **File:** `src/data/blog/siemens-sinamics-s120-fault-f07900.md`
- **Slug:** `/posts/siemens-sinamics-s120-fault-f07900/`
- **Target keywords:** "Siemens SINAMICS S120 F07900", "S120 motor overtemperature fault", "SINAMICS S120 F07901", "S120 servo fault motor temp"
- **Commercial intent:** HIGH — S120 drives power Siemens SINUMERIK 840D CNC machine tools and servo presses. KTY84 sensors $15–$50; DRIVE-CLiQ cables $60–$180; Motor Modules $800–$4,500. CNC service engineers searching during machine tool downtime.
- **Content:** F07900 vs. F07901 distinction (actual vs. thermal model), KTY84 resistance table, cooling system inspection checklist, STARTER/Startdrive parameter verification (p0307, p0311, p0344, p0612, p0625), fault history export guidance, 5-entry parts table.
- **Why it earns:** SINAMICS S120 is covered in the repo only by G120/G120x/G120C (general purpose) and SINUMERIK alarms. The S120 servo-specific faults are a gap. High-value industrial buyers with specific fault codes.

---

### 5. ABB ACS580 Fault Codes — Complete Guide
- **File:** `src/data/blog/abb-acs580-fault-codes.md`
- **Slug:** `/posts/abb-acs580-fault-codes/`
- **Target keywords:** "ABB ACS580 fault codes", "ACS580 2310 overcurrent", "ACS580 4110 heatsink overtemp", "ACS580 7121 fan fault", "ACS580 3210 overvoltage"
- **Commercial intent:** HIGH — ACS580 is ABB's general-purpose drive in water/wastewater plants, HVAC, and food/beverage. Cooling fans $80–$250; control panels $150–$220; full drives $600–$6,000. Plant operators and HVAC technicians searching during pump/fan failures.
- **Content:** Full fault table (2310–FA81), Drive composer data logging guidance, SD card parameter backup, decel ramp / braking resistor fix for 3210, heatsink fan replacement steps, 6-entry parts table.
- **Why it earns:** The existing repo has only `abb-acs580-fault-3130.md` (one fault). A complete ACS580 guide fills a large gap and captures all ACS580 fault searches that don't already have individual pages.

---

## Revenue Projection

| Article | Avg Part AOV | Monthly Traffic Estimate | CVR | Monthly Revenue Potential |
|---------|-------------|-------------------------|-----|--------------------------|
| Yaskawa Sigma-7 alarm codes | $180 | 600 | 2.5% | $270 |
| Mitsubishi MR-J4 alarm codes | $200 | 500 | 2.5% | $250 |
| Allen-Bradley PowerFlex 4M | $150 | 800 | 3% | $360 |
| Siemens SINAMICS S120 F07900 | $250 | 400 | 2% | $200 |
| ABB ACS580 complete guide | $160 | 900 | 3% | $432 |
| **TOTAL** | | **3,200** | | **$1,512/month** |

*Estimates at steady-state traffic (3–6 months post-publish). Conservative assumptions.*

---

## Astro Check Result

```
Result (57 files):
- 0 errors
- 0 warnings
- 5 hints
```

All 5 hints are pre-existing in the repo (unused imports in `src/constants.ts`, `src/components/Header.astro`, and `src/components/QuickAnswer.astro`) — not introduced by Wave 4 articles.

**Status: CLEAN — safe to deploy.**

---

## Files Created (Wave 4)

1. `src/data/blog/yaskawa-sigma7-sgd7s-alarm-codes.md`
2. `src/data/blog/mitsubishi-mr-j4-servo-alarm-codes.md`
3. `src/data/blog/allen-bradley-powerflex-4m-fault-codes.md`
4. `src/data/blog/siemens-sinamics-s120-fault-f07900.md`
5. `src/data/blog/abb-acs580-fault-codes.md`

Log file: `INDUSTRIAL_WAVE4_LOG.md` (this file)
