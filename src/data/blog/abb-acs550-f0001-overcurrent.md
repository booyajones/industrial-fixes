---
title: "ABB ACS550 F0001 Fault — Causes & Fix"
description: "What ABB ACS550 F0001 overcurrent fault means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS550 F0001 Fault — What It Means

The ABB ACS550 **F0001 fault** is an **Overcurrent** fault — the drive's output current has exceeded the instantaneous overcurrent protection threshold, typically 3.5× the drive's rated current. The ACS550 shuts down output immediately to protect its IGBT power modules. F0001 appears in the fault history (parameter group 13) with a sub-code that identifies which phase triggered first. The ACS550 is one of ABB's most widely installed drives in HVAC and industrial pump/fan applications, and F0001 is among its most common service faults.

[Jump to Fix](#fix)

## Common Causes

- **Motor or cable short circuit** — A phase-to-phase or phase-to-ground fault in the output cable or motor winding creates a current spike that triggers F0001.
- **Acceleration ramp too fast** — A ramp time that's too short for the load's rotational inertia demands peak current exceeding the overcurrent threshold.
- **Motor insulation breakdown** — Aging motor insulation stressed by the drive's PWM switching can fail at startup, causing a momentary ground fault.
- **Mechanical jam at startup** — Seized bearings or a jammed load creates near-locked-rotor current at startup.

## Step-by-Step Fix {#fix}

1. **Disconnect the motor and check for shorts** — Power off, lock out/tag out. Remove motor leads from U2, V2, W2 terminals. Measure phase-to-phase and phase-to-ground on the motor cable and motor terminals. Low ground resistance = fault in cable or motor.
2. **Read the F0001 sub-code** — Check parameter 13.03 (FAULT LAST) for the sub-code. Sub-code 1 = U phase, 2 = V phase, 4 = W phase. This tells you which output phase had the overcurrent.
3. **Extend acceleration time** — In parameter 22.01 (ACCEL TIME 1), double the value and test. This is a fast fix for high-inertia loads where the original ramp was too aggressive.
4. **Megohm test the motor** — Test at 1000V DC. Below 1 MΩ phase-to-ground = degraded insulation. Replace the motor or have it rewound.
5. **Reset and test unloaded** — Reset the fault (parameter 16.04 = FAULT RESET), decouple the motor from the load if possible, and run the drive. If F0001 fires with no mechanical load, the fault is in the motor or cable.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-f0001-overcurrent&k=Motor+%28replacement%29&tag=errorcodefixes-20) \| Replace when megohm test indicates failed insulation |
| VFD-rated cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-f0001-overcurrent&k=VFD-rated+cable&tag=errorcodefixes-20) \| Replace damaged output cable; use shielded cable rated for VFD duty |
| ACS550 IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs550-f0001-overcurrent&k=ACS550+IGBT+module&tag=errorcodefixes-20) \| Replace only if drive was damaged by a prior fault event (burn marks, smell of burned components) |
## When to Call a Pro

If F0001 persists with the motor disconnected (no output connected), the ACS550's current sensing or IGBT module has failed. Internal drive repair requires ABB-certified service technicians and proper test equipment.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

## See Also

- [ABB ACS880 Drive Maintenance Guide - Service Intervals, Fault Prevention, and Troubleshooting](/posts/abb-acs880-complete-maintenance-guide/)
- [ABB VFD Fault 2310 — Causes & Fix](/posts/abb-vfd-fault-2310/)
- [ABB ACS880 Fault 2310 Overcurrent — Causes & Fix](/posts/abb-acs880-fault-2310-overcurrent/)
- [ABB ACH580 HVAC VFD Fault Codes — Full Diagnostic Guide - What It Means and How to Fix It](/posts/abb-ach580-fault-codes/)
