---
title: "ABB ACS580 Fault 3130 — Input Phase Loss Fix"
description: "What ABB ACS580 fault 3130 means, why input phase loss triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 Fault 3130 — What It Means

The ABB ACS580 is a general-purpose all-compatible drive designed for industrial pump, fan, and compressor applications. It is the successor to the ACS550 in the ABB product line. Fault 3130 (INPUT PHASE LOSS) indicates the drive has detected a missing or severely unbalanced phase on its three-phase input supply. Like other ABB drives, the ACS580 detects phase loss by monitoring DC bus ripple — a lost input phase creates a characteristic 2× ripple frequency on the DC bus. When ripple exceeds the threshold, the drive trips on 3130 to protect the rectifier and DC bus capacitors from unbalanced stress.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse** — An upstream fuse on one phase has failed, creating a single-phase condition at the drive input. This is the most common cause of 3130 on the ACS580.
- **Loose input power terminal (L1, L2, or L3)** — The ACS580 uses compression lugs for power terminals. A terminal that wasn't fully tightened during installation creates a high-resistance joint that causes voltage drop and apparent phase loss under load.
- **Upstream contactor contact failure** — An AC contactor with a burned or pitted contact drops that phase under load. The contactor may appear to pull in normally but the damaged contact can't carry full load current.
- **Utility supply imbalance** — Severe voltage imbalance (>3%) from the utility can cause nuisance 3130 faults. Voltage imbalance heats the rectifier and reduces drive output capacity.
- **Fault sensitivity setting** — Parameter 31.22 (SUPPLY PHASE LOSS) on the ACS580 controls how the drive responds to phase loss. If set to WARNING instead of FAULT, the drive logs a warning (A3130) rather than a fault trip. Some applications benefit from this to avoid nuisance trips.

## Step-by-Step Fix {#fix}

1. **Check all three input voltages at L1, L2, L3** — Measure each phase-to-phase voltage at the drive input terminal block with the drive powered. All three readings should be within 3% of each other and within ±10% of nominal.
2. **Identify the missing phase** — A zero or significantly reduced reading on one pair of measurements identifies the missing phase. For example, if L1-L2 and L2-L3 are both normal but L1-L3 is zero or very low, L2 is the problem.
3. **Check upstream fuses for that phase** — Go to the upstream distribution panel and test the fuse on the affected phase. Replace if blown. Look for signs of the fault that caused the blow (discoloration, melting in the fuse holder).
4. **Inspect the input terminal at the drive** — With power off and capacitors discharged (minimum 5-minute wait), inspect the terminal lug for the affected phase. It should be tight, clean, and copper-bright. Re-torque all input terminals to the specification in the ACS580 hardware manual (typically 8–12 Nm for the standard frame sizes).
5. **Inspect the upstream contactor** — If fuses are good, energize the contactor and measure voltage on both sides of each contact. A contact with voltage on the upstream side but not the downstream side under load has failed.
6. **Adjust parameter 31.22 if appropriate** — If input voltage quality is marginal and 3130 is causing nuisance trips, consider setting parameter 31.22 to WARNING to allow the drive to ride through brief phase imbalance events. Do not do this if the underlying phase loss is a persistent fault.
7. **Reset the drive** — After restoring balanced three-phase input, press RESET on the ACS580 panel or control keypad. Confirm fault 3130 clears and monitor the DC bus voltage on startup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses | [Amazon](https://www.amazon.com/s?k=Input+fuses&tag=errorcodefixes-20) \| Match the type and amperage from the ACS580 hardware manual for the specific frame size |
| AC contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?tag=errorcodefixes-20) \| Replace if contact inspection shows pitting or high resistance under load |
| Power terminal lug | [Amazon](https://www.amazon.com/s?k=Power+terminal+lug&tag=errorcodefixes-20) \| Replace if existing lug is corroded or cracked |
## When to Call a Pro

If all three supply voltages are confirmed balanced and correct at the drive input terminals but fault 3130 persists, the rectifier input section may have been damaged by a prior phase loss event. ABB has an authorized drive repair center network for board-level diagnosis and repair. The ACS580 hardware warranty covers manufacturing defects; a phase-loss-induced rectifier failure may or may not be covered depending on the cause.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
