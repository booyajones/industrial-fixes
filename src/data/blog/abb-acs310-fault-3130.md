---
title: "ABB ACS310 Fault 3130 — Causes & Fix"
description: "What ABB ACS310 Fault 3130 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS310 Fault 3130 — What It Means

Fault 3130 on the ABB ACS310 variable frequency drive indicates an input phase loss — one or more of the three input supply phases is missing or has dropped below the threshold the drive requires for stable operation. The ACS310 monitors input voltage symmetry; if any phase is absent or severely unbalanced, it faults to protect the internal rectifier and DC bus capacitors from unbalanced voltage stress.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse on one phase** — The most common cause. A single blown fuse in the incoming supply creates single-phase input on a three-phase drive.
- **Loose or corroded input terminal connection** — A loose lug at the drive's L1, L2, or L3 terminal creates intermittent phase loss under load.
- **Tripped breaker on one leg** — A three-phase breaker with one tripped pole (common in thermal-magnetic breakers) creates the exact same symptom as a blown fuse.
- **Upstream contactor with a failed contact** — A worn contactor contact on one phase passes no current under load, even if it appears closed when de-energized.

## Step-by-Step Fix {#fix}

1. **Measure input voltage at the drive terminals** — With a multimeter, measure L1-L2, L2-L3, and L1-L3 at the drive's input terminals under load. All three readings should be equal (within 2%). A missing or low reading identifies the faulted phase.
2. **Check input fuses** — Open the upstream disconnect and test all three input fuses with a multimeter. A blown fuse reads open. Replace if bad — always replace all three when one blows.
3. **Inspect input terminal connections** — Check the torque on all L1/L2/L3 lug screws at the drive. Loose connections cause intermittent phase loss that gets worse under heat.
4. **Inspect the upstream contactor (if installed)** — Check contactor contacts for pitting or burning on the affected phase. A failed contact often shows burn marks or unequal wear vs. the other phases.
5. **Reset the fault** — After correcting the input issue, restore power and reset the ACS310 (press STOP/RESET on the keypad). Confirm 3130 does not return on restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (Class J or equivalent) | [Amazon](https://www.amazon.com/s?k=Input+fuses+%28Class+J+or+equivalent%29&tag=errorcodefixes-20) \| Match to ACS310 input current rating — replace all three |
| Input contactor | [Amazon](https://www.amazon.com/s?k=Input+contactor&tag=errorcodefixes-20) \| Replace if contacts are burned or pitted |
| Input terminal block | [Amazon](https://www.amazon.com/s?k=Input+terminal+block&tag=errorcodefixes-20) \| If lug damage is found during inspection |
## When to Call a Pro

Phase loss diagnosis requires working in live panels with dangerous voltages. If you're not qualified to work on industrial electrical enclosures with exposed live terminals, have a licensed electrician trace and repair the input circuit.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
- [ABB ACS550 AF10 Fault — Causes & Fix](/posts/abb-acs550-af10-heatsink/)
