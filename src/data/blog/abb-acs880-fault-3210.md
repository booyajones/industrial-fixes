---
title: "ABB ACS880 Fault 3210 — DC Bus Undervoltage Causes & Fix"
description: "What ABB ACS880 fault 3210 means, why DC bus undervoltage trips the drive, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS880 Fault 3210 — What It Means

Fault 3210 (DC Undervoltage) on an ABB ACS880 drive means the DC bus voltage dropped below the drive's minimum operating threshold. The ACS880 rectifies incoming AC to a DC bus nominally at 1.35× the input line voltage; for a 400 V supply this is approximately 540 VDC. If the bus drops below the low-voltage trip threshold — typically around 300–330 VDC on 400 V models — the drive trips 3210 to prevent output current distortion and to protect the DC capacitors. This fault can occur during a supply sag, at startup, or if the supply voltage is simply too low for the configured application.

[Jump to Fix](#fix)

## Common Causes

- **Low incoming supply voltage** — Supply voltage below the ACS880's minimum rating (−10% of nominal). Can be caused by a utility sag, an undersized transformer, or excessive voltage drop in the supply cable.
- **Input phase loss (related to 3130)** — A missing input phase produces only a partial rectified DC bus, which will drop below the 3210 trip level. Check for fault 3130 as well.
- **Mains supply interruption during deceleration** — If the supply drops during regenerative braking, the drive may see 3210 before it sees 3130 depending on timing.
- **Undersized supply conductors** — Long supply cable runs with undersized wire cause voltage drop under load sufficient to pull the bus below the trip level.
- **Pre-charge circuit fault** — The ACS880's soft-charge circuit pre-charges the DC capacitors before the main contactor closes. A failed pre-charge relay or resistor can prevent the bus from reaching operating voltage, tripping 3210 at startup.

## Step-by-Step Fix {#fix}

1. **Measure supply voltage at the drive input terminals** — With appropriate PPE, measure L-L voltage at R, S, T. Compare to the drive's rated input voltage range (e.g., 380–415 VAC for a 400 V model). Voltages more than 10% below nominal are the problem.
2. **Check for phase imbalance** — Measure all three L-L voltages. Imbalance greater than 2–3% causes increased ripple and can trigger 3210 even when peak voltages are within range.
3. **Inspect input fuses and contactor** — A partially blown fuse increases resistance on one phase, lowering effective bus voltage.
4. **Check supply cable sizing** — For long runs, verify the cable cross-section against the ACS880 hardware manual's voltage-drop guidelines. Undersized cables cause voltage sag under full load.
5. **Inspect the pre-charge circuit** — If 3210 trips at every startup before the motor begins to run, the pre-charge resistor or relay may be faulty. Measure the DC bus voltage progression during startup (should ramp to nominal in 1–2 seconds).
6. **Reset and test under load** — After correcting supply voltage issues, reset the fault and ramp the drive to full speed while monitoring the DC bus voltage via parameter 1.7 (DC Voltage) on the ACS880 panel.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Pre-charge resistor / relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs880-fault-3210&k=Pre-charge+resistor+%2F+relay&tag=errorcodefixes-20) \| ACS880 frame-size specific; replace as a kit |
| Input fuses (semiconductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs880-fault-3210&k=Input+fuses+%28semiconductor%29&tag=errorcodefixes-20) \| aR or gR type; match frame size current rating |
## When to Call a Pro

DC bus measurements and pre-charge circuit diagnosis require a qualified electrical engineer familiar with ACS880 hardware. DC bus voltages can exceed 1000 VDC on high-voltage models and retain charge after power-down for several minutes.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

## See Also

- [ABB ACS880 Complete Fault Code Guide — All Faults and Fixes](/posts/abb-acs880-complete-guide/)
- [ABB VFD Fault 4110 — Causes & Fix](/posts/abb-vfd-fault-4110/)
- [ABB VFD Fault 3130 — Input Phase Loss Fix](/posts/abb-vfd-fault-3130/)
- [ABB VFD Fault 9300 — Causes & Fix](/posts/abb-vfd-fault-9300/)
