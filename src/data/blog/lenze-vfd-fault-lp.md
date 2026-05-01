---
title: "Lenze VFD Fault LP — Causes & Fix"
description: "What Lenze VFD fault LP means, why phase loss triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - lenze
---

## Lenze VFD Fault LP — What It Means

Lenze fault **LP** (Phase Loss) indicates the drive detected a missing or severely unbalanced input phase on its 3-phase AC supply. On Lenze 8200, 9300, and i550 series drives, the rectifier monitors all three input phases (L1, L2, L3); if one phase is absent or drops significantly below the others, LP is triggered and the drive shuts down to prevent DC bus ripple damage and overloading the remaining input phases. Single-phase operation of a 3-phase drive can destroy the rectifier diodes within minutes.

[Jump to Fix](#fix)

## Common Causes

- **Open fuse or tripped breaker on one input phase** — A blown fuse in the panel supplying the drive leaves one phase open; most common cause of LP.
- **Loose or corroded input terminal** — A loose L1, L2, or L3 terminal creates a high-resistance connection that drops out under load, triggering LP.
- **Upstream contactor with a failed contact** — An input line contactor with a burnt contact opens one phase under load.
- **Utility supply phase loss** — Infrequently, one utility phase is interrupted at the transformer or on the incoming service.

## Step-by-Step Fix {#fix}

1. **Apply LOTO and measure input voltage** — With the drive energized and the fault present, measure voltage between all three phase pairs at the drive's L1/L2/L3 input terminals: L1-L2, L2-L3, and L1-L3. All three should be within ±10% of each other.
2. **Identify the missing phase** — If one measurement is significantly low or zero, that phase is absent. Trace back from the drive terminal to the source.
3. **Check panel fuses** — Inspect the fuses in the disconnect or panel feeding the drive. Test each fuse with a multimeter (continuity or voltage drop). Replace any blown fuse with the correct amperage and type.
4. **Check input terminals on the drive** — With LOTO applied, inspect L1, L2, and L3 terminals inside the drive enclosure. Tighten any loose terminal screws. Look for burning or corrosion on terminal lugs.
5. **Inspect the input contactor** — If there's a line contactor between the panel and the drive, check all three sets of contacts for burning or incomplete closure.
6. **Reset and retest** — After restoring all three phases, clear the LP fault (power cycle or keypad reset), run the drive at low speed, and confirm voltage balance at the input.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses | [Amazon](https://www.amazon.com/s?k=Input+fuses&tag=errorcodefixes-20) \| Match voltage, amperage, and fuse class exactly (often aR or gG type on European drives) |
| Input line contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?tag=errorcodefixes-20) \| If contact burning is confirmed; match coil voltage and current rating |
## When to Call a Pro

If all three input phases measure correctly at the drive terminals but LP persists, the drive's rectifier or input phase loss detection circuit may have failed. Lenze rectifier replacement requires drive board disassembly — contact a Lenze service center or certified integrator.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
