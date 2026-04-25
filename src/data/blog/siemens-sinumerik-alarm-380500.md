---
title: "Siemens Sinumerik Alarm 380500 — Causes & Fix"
description: "What Siemens Sinumerik alarm 380500 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - siemens
---

## Siemens Sinumerik Alarm 380500 — What It Means

Siemens Sinumerik alarm 380500 (%1 is a group alarm for drive (SINAMICS/611D) faults detected via the DRIVE-CLiQ or PROFIBUS interface between the NCK and the drive system. The %1 parameter in the alarm text substitutes the specific drive component identifier (e.g., "SERVO_1" or "A1:S1.1") and the sub-fault type. Alarm 380500 typically indicates that the Sinumerik NCK received a fault report from the connected SINAMICS S120 or 840D servo drive and shut down the affected axes. The actual root cause is in the drive's own fault memory, not in the CNC alarm directly.

[Jump to Fix](#fix)

## Common Causes

- **SINAMICS S120 drive sub-fault** — The servo drive detected an overcurrent, overvoltage, encoder fault, or thermal overload. The specific SINAMICS fault number (visible in the drive's diagnostics via Starter or HMI Pro) identifies the actual cause.
- **DRIVE-CLiQ cable fault** — The fiber-optic or copper DRIVE-CLiQ cable between the NCK, NX modules, and the motor modules developed a fault. Signal interruption causes alarm 380500 with a communication sub-fault.
- **Motor module (servo drive) hardware fault** — The drive's IGBT module, gate drive, or measurement board failed. This appears as a hardware fault sub-code in the SINAMICS fault buffer.
- **Encoder system fault** — The encoder on the motor or the encoder cable (SMC-to-motor) has a fault that the SINAMICS drive detected, triggering a following error or feedback loss that propagates to alarm 380500.

## Step-by-Step Fix {#fix}

1. **Read the SINAMICS drive fault buffer** — On the Sinumerik 840D HMI, navigate to Commissioning > Drive System > Faults. Read the specific SINAMICS fault code (e.g., F07412, A30014). This is the actual fault; alarm 380500 is the CNC's wrapper around it.
2. **Check DRIVE-CLiQ connections** — Power down the machine and inspect all DRIVE-CLiQ cables at the NCU, NX modules, and motor modules. Each cable has a lock latch; verify all latches are engaged and cables are fully seated.
3. **Inspect motor power cables and encoder cables** — Check the motor cable (U1/V1/W1/PE) and the SMC encoder cable for damage. Pay attention to drag chain segments where cables flex repeatedly.
4. **Check drive module cooling** — SINAMICS S120 motor modules have internal cooling fans. Confirm fans are running and heatsinks are clean. Thermal overload faults are common in enclosures without adequate ventilation.
5. **Clear SINAMICS fault and power-cycle** — After addressing the identified sub-fault, use the SINAMICS fault acknowledgment to clear drive faults, then power-cycle the machine and verify alarm 380500 does not return on startup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| DRIVE-CLiQ cable | [Amazon](https://www.amazon.com/s?k=DRIVE-CLiQ+cable&tag=errorcodefixes-20) \| Replace if signal quality is degraded or cable is physically damaged |
| SINAMICS S120 motor module | [Amazon](https://www.amazon.com/s?k=SINAMICS+S120+motor+module&tag=errorcodefixes-20) \| Replace if hardware fault confirmed in drive diagnostics |
| Encoder cable (SMC to motor) | [Amazon](https://www.amazon.com/s?k=Encoder+cable+%28SMC+to+motor%29&tag=errorcodefixes-20) \| Replace if encoder fault is the confirmed sub-fault |
## When to Call a Pro

Sinumerik 840D/840Dsl systems require Siemens commissioning software (Starter or SINAMICS Startdrive) to properly diagnose drive-level faults and re-commission servo parameters after a motor module replacement. This work is typically performed by a Siemens-certified service engineer.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
