---
title: "Lenze i550 Fault LF — Phase Loss Causes & Fix"
description: "What Lenze i550 fault LF means, why phase loss trips the drive, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - lenze
---

## Lenze i550 Fault LF — What It Means

Fault LF (Line Failure / Phase Loss) on a Lenze i550 drive means the drive has detected that one or more phases of the incoming supply are missing or severely unbalanced. The Lenze i550 is Lenze's compact, application-optimized inverter for pumps, fans, and conveyor applications. LF fires when the monitored input phase voltages deviate beyond the acceptable imbalance threshold. Operating on a single-phase supply (even briefly) forces the drive to rectify on only two legs, causing abnormal DC bus ripple that stresses the capacitors and power bridge.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse on one phase** — A single-phase fuse failure is the most common cause. The other two phases remain powered, so the drive continues to receive partial power but reports LF.
- **Tripped circuit breaker pole** — A thermal-magnetic breaker with one tripped pole passes the same partial-power scenario as a blown fuse.
- **Loose input terminal** — A terminal that was not properly torqued or has vibrated loose creates a high-resistance intermittent connection that reads as phase loss under load.
- **Utility supply fault** — A broken overhead line, a blown utility transformer fuse, or a distribution fault upstream of the facility can drop one phase to the entire site.

## Step-by-Step Fix {#fix}

1. **Measure input voltages at L1, L2, L3** — With appropriate PPE, measure all three L-L voltages at the i550 input terminals. A missing or low phase will be immediately apparent.
2. **Check upstream fuses and breakers** — Inspect the protective device feeding the i550. Replace any blown fuse with the type and rating specified in the Lenze i550 installation manual (semiconductor-type fuses are required for drive protection).
3. **Inspect input terminal tightness** — With power off, check the torque of all three input terminals. Retorque to the Nm value specified in the manual for the cable size being used.
4. **Inspect for heat damage** — A loose terminal that has been arcing will show discoloration on the terminal block or cable lug. Replace any damaged components.
5. **Verify supply at the service entrance** — If all drive-level checks pass, have an electrician verify the utility supply is delivering balanced three-phase voltage at the building's main distribution panel.
6. **Reset and test** — After correcting the supply issue, reset the LF fault from the i550 keypad or via the connected fieldbus, and test the drive under normal operating load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Semiconductor input fuses | [Amazon](https://www.amazon.com/s?k=Semiconductor+input+fuses&tag=errorcodefixes-20) \| Use Lenze-specified aR or gR fuse type; do not substitute standard HRC fuses |
| Input terminal block | [Amazon](https://www.amazon.com/s?k=Input+terminal+block&tag=errorcodefixes-20) \| Replace if arcing damage or severe corrosion is present |
## When to Call a Pro

All input phase fault diagnosis involves live three-phase voltages. Only qualified electricians wearing appropriate PPE should perform live voltage measurements. If the LF fault points to a utility supply problem, the utility company must be notified — do not attempt to bypass or ignore the fault.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
