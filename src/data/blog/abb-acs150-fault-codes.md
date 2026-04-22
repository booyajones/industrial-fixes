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

| [Fault Code](https://www.amazon.com/s?k=Fault%20Code&tag=errorcodefixe-20) | Meaning |
|---|---|
| [0001](https://www.amazon.com/s?k=0001&tag=errorcodefixe-20) | Overcurrent |
| [0002](https://www.amazon.com/s?k=0002&tag=errorcodefixe-20) | DC overvoltage |
| [0003](https://www.amazon.com/s?k=0003&tag=errorcodefixe-20) | DC undervoltage |
| [0004](https://www.amazon.com/s?k=0004&tag=errorcodefixe-20) | Short circuit |
| [0005](https://www.amazon.com/s?k=0005&tag=errorcodefixe-20) | Overtemperature |
| [0006](https://www.amazon.com/s?k=0006&tag=errorcodefixe-20) | Output phase loss |
| [0007](https://www.amazon.com/s?k=0007&tag=errorcodefixe-20) | Motor stall |
| [0008](https://www.amazon.com/s?k=0008&tag=errorcodefixe-20) | Motor overload |
| [0009](https://www.amazon.com/s?k=0009&tag=errorcodefixe-20) | Panel communication fault |
| [0010](https://www.amazon.com/s?k=0010&tag=errorcodefixe-20) | AI1 analog input loss |
| [0012](https://www.amazon.com/s?k=0012&tag=errorcodefixe-20) | External fault |
| [0016](https://www.amazon.com/s?k=0016&tag=errorcodefixe-20) | Earth fault |
| [0018](https://www.amazon.com/s?k=0018&tag=errorcodefixe-20) | Internal control fault |

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
| [Cooling fan](https://www.amazon.com/s?k=Cooling%20fan&tag=errorcodefixe-20) | Common wear item in hot panels |
| [Keypad panel](https://www.amazon.com/s?k=Keypad%20panel&tag=errorcodefixe-20) | For display or navigation issues |
| [Complete ACS150 drive](https://www.amazon.com/s?k=Complete%20ACS150%20drive&tag=errorcodefixe-20) | For persistent internal faults |
| [Motor cable](https://www.amazon.com/s?k=Motor%20cable&tag=errorcodefixe-20) | Replace if insulation is damaged |

## When to Call a Pro

If the ACS150 repeatedly throws 0018 internal control faults or trips immediately with the motor disconnected, the drive has likely failed internally. ABB support or an industrial drive specialist should confirm replacement rather than continued resets.
