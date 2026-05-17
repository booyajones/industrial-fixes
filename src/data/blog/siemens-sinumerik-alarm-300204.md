---
title: "Siemens Sinumerik Alarm 300204 — Causes & Fix"
description: "What Siemens Sinumerik 300204 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - siemens
---

## Siemens Sinumerik Alarm 300204 — What It Means

Siemens Sinumerik alarm 300204 means axis overcurrent — the drive detected motor current exceeding the maximum permissible threshold on the specified axis. On Sinumerik 840D, 840Di sl, and 828D controls with Sinamics S120 or 611 drives, alarm 300204 is a drive-level fault reported to the CNC. The alarm text typically reads "Axis [axis name] drive fault 300204" and the associated Sinamics fault code is F30004 (overcurrent). This is a hard trip that powers down the axis immediately to protect the IGBT modules and motor winding.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical binding or jam** — The most common cause. A seized bearing, contaminated spindle bearing, worn ball screw, or chip jam in a linear axis causes the motor to demand excessive torque, driving current above the trip threshold.
- **Short circuit in motor winding or cable** — A phase-to-phase or phase-to-ground fault in the servo motor or its power cable produces catastrophic overcurrent at startup.
- **Incorrect drive parameters** — If the motor current limit parameters (p0640, p0323) in the Sinamics drive don't match the actual motor, the limits may be set too low relative to what the motor legitimately needs.
- **IGBT module degradation** — An aging or partially failed IGBT in the Sinamics drive module can produce false overcurrent readings due to asymmetric output.

## Step-by-Step Fix {#fix}

1. **Check mechanical freedom of the axis** — With the machine in a safe state (power removed from drives, axis brake released if applicable), manually move the affected axis. Should move smoothly. Any resistance means a mechanical issue must be resolved first.
2. **Inspect motor power cable** — Check the cable from the Sinamics module to the motor for visible damage: burnt connectors, crushed insulation, or chafed shielding. Disconnect and test insulation resistance.
3. **Test motor winding insulation** — With the power cable disconnected at the drive, test each motor lead to ground with a 500V megohm meter. Below 1 MΩ = motor insulation fault.
4. **Read Sinamics fault history** — On the Sinamics drive (or through the Sinumerik NC), navigate to drive diagnostics and read the fault buffer. The Sinamics F-fault code alongside alarm 300204 gives more detail.
5. **Reset the system** — After resolving the mechanical or electrical fault, acknowledge the alarm on the Sinumerik control and confirm the drive fault clears. Rehome the affected axis and run a slow manual cycle to verify.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Sinamics S120 motor module | [Amazon](https://www.amazon.com/s?i=industrial&k=Sinamics+S120+motor+module&tag=errorcodefixes-20) \| Specific to axis current rating; part number from drive module label |
| Servo motor | [Amazon](https://www.amazon.com/s?i=industrial&k=Servo+motor&tag=errorcodefixes-20) \| Replace if winding insulation fails megohm test |
| Motor power cable (pre-assembled, shielded) | [Amazon](https://www.amazon.com/s?i=industrial&k=Motor+power+cable+%28pre-assembled%2C+shielded%29&tag=errorcodefixes-20) \| Siemens specifies cable type for Sinamics; use correct shield termination |
## When to Call a Pro

Sinamics S120 drive module repair and parameter verification requires Siemens-trained technicians with TIA Portal access. Incorrect parameter restoration after a module swap will generate additional alarms.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
