---
title: "ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference"
description: "Complete guide to ABB ACS150 micro drive fault codes, causes, and step-by-step repair procedures for industrial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - abb
  - industrial
---

## ABB ACS150 Micro Drive Fault Codes — What They Mean

The ABB ACS150 is a compact micro drive built for simple machine control, including conveyors, fans, mixers, and light-duty pumps. It uses ABB's standard fault structure with a numeric code shown on the keypad display. Because the ACS150 is often installed in small OEM panels with minimal cooling, many of its common faults come from overheating, wiring mistakes, and parameter issues rather than true hardware failure.

[Jump to Fix](#fix)

## ABB ACS150 Common Fault Code Reference

| Fault Code | Meaning |
|---|---|
| 0001 | Overcurrent |
| 0002 | DC overvoltage |
| 0003 | DC undervoltage |
| 0004 | Short circuit |
| 0005 | Overtemperature |
| 0006 | Output phase loss |
| 0007 | Motor stall |
| 0008 | Motor overload |
| 0009 | Panel communication fault |
| 0010 | AI1 analog input loss |
| 0012 | External fault |
| 0016 | Earth fault |
| 0018 | Internal control fault |

## Common Causes by Fault

- **0001 — Overcurrent** — Jammed load, too-short acceleration time, or motor cable short.
- **0002 — Overvoltage** — Deceleration time too short on a high-inertia load. Extend ramp-down or add braking strategy.
- **0005 — Overtemperature** — Blocked airflow, failed cooling fan, or enclosure too hot. The ACS150 needs vertical mounting clearance to cool properly.
- **0007 — Motor stall** — The drive is commanded to run but current rises without the motor reaching speed. Check for seized bearings or mechanical obstruction.
- **0016 — Earth fault** — Motor winding or cable insulation fault to ground.

## Step-by-Step Fix {#fix}

1. **Read the displayed fault code** — Record the number before resetting.
2. **For 0001 or 0007** — Disconnect the mechanical load if possible and test the motor free-running. Increase acceleration time.
3. **For 0005** — Clean vents, confirm fan operation, and verify enclosure temperature is within spec.
4. **For 0016** — Megger the motor and cable to ground with the drive disconnected.
5. **Reset and monitor** — After correcting the issue, reset the drive and confirm it runs through a full cycle.

## Parts Often Needed

| Part | Notes |
|---|---|
| Cooling fan | [Amazon](https://www.amazon.com/s?k=Cooling+fan&tag=errorcodefixes-20) \| Common wear item in hot panels |
| Keypad panel | [Amazon](https://www.amazon.com/s?k=Keypad+panel&tag=errorcodefixes-20) \| For display or navigation issues |
| Complete ACS150 drive | [Amazon](https://www.amazon.com/s?k=Complete+ACS150+drive&tag=errorcodefixes-20) \| For persistent internal faults |
| Motor cable | [Amazon](https://www.amazon.com/s?k=Motor+cable&tag=errorcodefixes-20) \| Replace if insulation is damaged |
## When to Call a Pro

If the ACS150 repeatedly throws 0018 internal control faults or trips immediately with the motor disconnected, the drive has likely failed internally. ABB support or an industrial drive specialist should confirm replacement rather than continued resets.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
- [ABB ACS550 AF10 Fault — Causes & Fix](/posts/abb-acs550-af10-heatsink/)
