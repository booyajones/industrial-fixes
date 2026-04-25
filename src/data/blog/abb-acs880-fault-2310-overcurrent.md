---
title: "ABB ACS880 Fault 2310 Overcurrent — Causes & Fix"
description: "What ABB ACS880 Fault 2310 overcurrent means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS880 Fault 2310 Overcurrent — What It Means

The ABB ACS880 **Fault 2310** is an **Overcurrent** fault — the drive's output current has exceeded the instantaneous overcurrent trip level (typically 2× the drive's rated current). The ACS880 shuts down immediately to protect its IGBTs from a shoot-through event. Fault 2310 is a hard, fast-trip protection; it is not the same as the thermal overload (Fault 2310 OL). The fault appears in the drive's fault log with a timestamp, and the sub-code in the fault data narrows down which phase tripped.

[Jump to Fix](#fix)

## Common Causes

- **Motor output short circuit** — A phase-to-phase or phase-to-ground short in the motor winding or output cable causes a current spike that instantly exceeds the 2310 threshold.
- **Acceleration ramp too fast** — Accelerating a high-inertia load too quickly demands peak current that exceeds the drive's trip level.
- **Motor insulation breakdown** — Aged motor insulation fails at the moment of startup (high dV/dt stress from the drive's PWM switching), causing a momentary short and 2310 trip.
- **Mechanical jam at startup** — A seized or jammed load at startup demands near-locked-rotor current, which can exceed 2× FLA on a properly sized drive.

## Step-by-Step Fix {#fix}

1. **Check for an output short circuit** — Power off, lock out. Disconnect the motor from the drive output terminals. Measure phase-to-phase and phase-to-ground resistance on the motor cable and on the motor terminals. Any low-resistance ground reading = winding or cable fault.
2. **Identify the sub-code** — Read the fault log (parameter group 08) and note the sub-code with fault 2310. Sub-code 1 = U phase, 2 = V phase, 3 = W phase. This narrows whether it's a specific winding issue.
3. **Extend the acceleration ramp** — In parameter 23.12 (Acceleration Time 1), increase the ramp time by 50% and test. If 2310 clears with a longer ramp, the original ramp was too aggressive for the load inertia.
4. **Megohm test the motor** — After clearing the output cable, megohm test the motor windings at 1000V. Any reading below 1 MΩ indicates degraded insulation that will cause intermittent 2310 faults.
5. **Reset and test with no load** — Reconnect motor, reset fault (parameter 96.09 = 1 or use the panel), and test the drive with motor decoupled from load. If 2310 trips with no mechanical load, the motor has a winding fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (replacement) | [Amazon](https://www.amazon.com/s?k=Motor+%28replacement%29&tag=errorcodefixes-20) \| Replace when megohm test shows degraded insulation |
| Output motor cable | [Amazon](https://www.amazon.com/s?k=Output+motor+cable&tag=errorcodefixes-20) \| Replace if cable insulation has failed; use VFD-rated cable |
| ACS880 IGBT module | [Amazon](https://www.amazon.com/s?k=ACS880+IGBT+module&tag=errorcodefixes-20) \| Replace only after confirming the fault was caused by an external short that damaged internal semiconductors |
## When to Call a Pro

If 2310 trips with no load connected and the motor tests clean, the ACS880's current sensing circuit or IGBT module may have been damaged by a prior short circuit event. ABB-certified drive technicians should perform IGBT gate signal testing and bus capacitor verification.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
