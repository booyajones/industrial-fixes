---
title: "VFD Fault Code Lookup: All Brands"
description: "Master VFD fault code lookup guide covering ABB, Danfoss, Siemens, Schneider, Mitsubishi, Yaskawa, Allen-Bradley, and more."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Dana Kowalski"
featured: true
draft: false
tags:
  - vfd
  - industrial
  - lookup
---

## VFD Fault Code Lookup — Start Here

Variable frequency drive faults look brand-specific on the screen, but most of them reduce to a small set of root causes: overcurrent, overvoltage, undervoltage, overtemperature, communication loss, and motor feedback issues. This page helps technicians classify the fault before going to the drive-specific guide.

[Jump to Fix](#fix)

## Common VFD Fault Patterns

| Fault Type | What It Usually Means |
|---|---|
| Overcurrent | Mechanical bind, cable short, ramp too fast |
| Overvoltage | Decel too fast, regenerative load |
| Undervoltage | Supply loss or weak incoming power |
| Overtemperature | Cooling failure or hot enclosure |
| Ground fault | Motor or cable insulation breakdown |
| Communication fault | PLC, fieldbus, or keypad/network issue |

## Brands Covered

- ABB
- Danfoss
- Siemens
- Schneider Electric
- Mitsubishi
- Yaskawa
- Allen-Bradley PowerFlex
- Toshiba and others

## Step-by-Step Fix {#fix}

1. **Capture the exact code and operating state** — accel, run, decel, or idle.
2. **Separate load issues from drive issues** — Can the motor/load turn freely?
3. **Check incoming power quality**.
4. **Inspect motor cable, grounding, and enclosure cooling**.
5. **Review parameters only after hardware basics are verified**.

## Parts Often Needed

| Part | Notes |
|---|---|
| Cooling fan | [Amazon](https://www.amazon.com/s?i=industrial&k=Cooling+fan&tag=errorcodefixes-20) \| Frequent source of thermal faults |
| Braking resistor | [Amazon](https://www.amazon.com/s?i=industrial&k=Braking+resistor&tag=errorcodefixes-20) \| Needed for fast-stop applications |
| Keypad / HMI | [Amazon](https://www.amazon.com/s?i=industrial&k=Keypad+%2F+HMI&tag=errorcodefixes-20) \| For local diagnostics |
| Replacement drive | [Amazon](https://www.amazon.com/s?i=industrial&k=Replacement+drive&tag=errorcodefixes-20) \| For confirmed internal hardware faults |
## When to Call a Pro

If the drive faults with the motor disconnected, or if you see repeated hardware or DC bus faults, involve a qualified drive technician. Parameter guessing and repeated resets can make a controllable problem much more expensive.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
