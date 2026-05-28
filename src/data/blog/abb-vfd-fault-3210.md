---
title: "ABB VFD Fault 3210 — Causes & Fix"
description: "What ABB VFD fault 3210 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB VFD Fault 3210 — What It Means

ABB fault code 3210 (DC UNDERVOLT) indicates the DC bus voltage dropped below the minimum operating threshold. ABB ACS drives monitor the DC link voltage continuously. When input voltage sags or disappears, the DC bus capacitors discharge. Once bus voltage falls below the programmed undervoltage trip level (typically around 333 VDC on a 480V system, or 200 VDC on a 240V system), the drive trips with fault 3210 to prevent the motor from losing speed control in an uncontrolled way. This fault points to the input power supply, not the drive itself.

[Jump to Fix](#fix)

## Common Causes

- **Input power sag or interruption** — Utility voltage dips below nominal, a breaker trips, or a fuse on the input supply blows. Even momentary sags during motor starting elsewhere on the same feeder can trigger 3210.
- **Loose or corroded input terminals** — A high-resistance connection on any input phase produces a voltage drop under load that causes DC bus undervoltage during acceleration.
- **Blown input fuse or open input contactor** — If one or more phases are missing from the drive's input, the DC bus charges from fewer phases and sags when the motor loads the output.
- **Line reactor failure** — If a line reactor on the drive's input is failing (open winding), effective input voltage drops and DC bus undervoltage results.

## Step-by-Step Fix {#fix}

1. **Measure input voltage under load** — With the drive attempting to run, measure L1-L2, L2-L3, and L1-L3 at the drive input terminals. All three should be within 3% of each other and within ±10% of nominal. A low or missing phase is immediately obvious.
2. **Check input fuses and contactors** — Verify all three input fuses are intact (test for continuity). If an input contactor is present, confirm all 3 poles close fully.
3. **Tighten input terminals** — With power isolated, torque all input terminal screws to the drive manufacturer's specification. Oxidized or undersized wire should be addressed.
4. **Check the utility supply** — If the building is experiencing voltage sags during large motor starts elsewhere on the same panel, contact the utility or install a line conditioner.
5. **Reset the system** — After restoring proper input voltage, reset the fault and restart. Monitor DC bus voltage readout (usually available in the diagnostics menu) during startup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (class J or RK5) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-3210&k=Input+fuses+%28class+J+or+RK5%29&tag=errorcodefixes-20) \| Match AIC rating and current rating to drive nameplate |
| Line reactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-vfd-fault-3210&k=Line+reactor&tag=errorcodefixes-20) \| Install if not present; reduces voltage sag and protects drive from line transients |
| Input contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-abb-vfd-fault-3210&tag=errorcodefixes-20) \| Replace if any pole shows excessive arcing or fails to close fully |
## When to Call a Pro

Persistent undervoltage faults on a properly sized supply indicate the drive's DC bus capacitors may have degraded (reduced capacitance allows faster sag). Capacitor testing and replacement requires a qualified drive technician.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [PowerFlex vs SINAMICS VFD compared](/posts/powerflex-vs-sinamics-vfd/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [PowerFlex F004 undervoltage fix](/posts/allen-bradley-powerflex-f004-fault/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [PowerFlex F012 hardware overcurrent](/posts/allen-bradley-powerflex-f012-fault/)

## See Also

- [ABB ACS580 A2B1 Fault Code - Causes & Fix](/posts/abb-acs580-a2b1-fault-code/)
- [ABB VFD Fault Codes — ACS550, ACS880, ACS310 Reference](/posts/abb-vfd-fault-codes/)
- [ABB ACS580 A2A1 - Causes & Fix](/posts/abb-acs580-a2a1-fault-code/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
