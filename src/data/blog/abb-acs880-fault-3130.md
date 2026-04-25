---
title: "ABB ACS880 Fault 3130 — Input Phase Loss Causes & Fix"
description: "What ABB ACS880 fault 3130 means, why input phase loss occurs, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS880 Fault 3130 — What It Means

Fault 3130 (Input Phase Loss) on an ABB ACS880 drive means the drive's input phase monitor has detected that one phase of the incoming three-phase supply is missing or severely unbalanced. The ACS880 monitors all three input phases continuously; a missing phase forces the drive to rectify on two legs, producing abnormal DC bus ripple and causing overheating of the input rectifier. The drive trips immediately to protect the power electronics. This fault is identical in meaning to 3130 on the ACS550 and ACS580, though the ACS880's higher power rating means the consequences of ignoring it are more severe.

[Jump to Fix](#fix)

## Common Causes

- **Open fuse or circuit breaker on one phase** — A blown input fuse or a tripped breaker pole is the most frequent cause. Check all three phases of the upstream protective device.
- **Loose or failed input contactor** — An input contactor with a damaged contact on one pole passes power intermittently, causing the drive to see a phase drop under load.
- **Damaged input cable or terminal lug** — A loose terminal lug on R, S, or T causes resistance heating and eventual open-circuit on that phase, particularly in high-vibration environments.
- **Utility supply problem** — A blown transformer fuse or utility line fault upstream of the facility can drop one phase. Check at the service entrance.

## Step-by-Step Fix {#fix}

1. **Identify the faulted phase** — Use a multimeter or clamp meter to measure voltage at the ACS880's R, S, and T input terminals with the drive powered on (use appropriate PPE — high voltage). Identify which phase is missing or low.
2. **Trace upstream to the fault** — Check the input fuses or circuit breaker. A blown fuse or a breaker with one tripped pole explains the missing phase immediately.
3. **Inspect input contactor contacts** — If the protective device is intact, inspect the input contactor. Measure contact voltage drop across each pole under load; a high drop indicates a damaged contact.
4. **Check cable terminations** — Inspect the ACS880's input cable lugs for signs of overheating (discoloration, melted insulation), looseness, or corrosion. Retorque to the specified Nm value in the ACS880 hardware manual.
5. **Verify at the service entrance** — If all downstream checks are normal, have an electrician verify three-phase supply at the panel feeding the drive.
6. **Reset the fault** — After the root cause is corrected, press the RESET button or issue a fault reset command via the panel or fieldbus. The drive will not restart until the fault is cleared.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (semiconductor type) | [Amazon](https://www.amazon.com/s?k=Input+fuses+%28semiconductor+type%29&tag=errorcodefixes-20) \| ACS880 requires gR or aR semiconductor fuses — not standard HRC fuses |
| Input contactor | [Amazon](https://www.amazon.com/s?k=Input+contactor&tag=errorcodefixes-20) \| Match voltage and current rating for the ACS880 frame size |
| Input cable lugs | [Amazon](https://www.amazon.com/s?k=Input+cable+lugs&tag=errorcodefixes-20) \| Use the torque-rated lugs specified in the ACS880 hardware manual |
## When to Call a Pro

Fault 3130 diagnosis involves live three-phase voltages up to 690 VAC. All measurements must be made by a qualified electrical technician wearing appropriate PPE. Never probe input terminals on a live drive without arc-flash assessment.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
