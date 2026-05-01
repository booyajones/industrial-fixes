---
title: "Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes"
description: "Complete fault code guide for the Danfoss VLT AutomationDrive FC302, covering alarm and warning codes, causes, and step-by-step troubleshooting."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
  - industrial
---

## Danfoss FC302 Complete Fault Code Guide — What They Mean

The Danfoss FC302 VLT AutomationDrive is a high-feature industrial VFD used on conveyors, compressors, extruders, pumps, and material handling systems. Faults display as Alarm 14, Alarm 29, Alarm 38, and similar messages on the LCP keypad. Some alarms trip the drive immediately, while others warn before a shutdown.

[Jump to Fix](#fix)

## Danfoss FC302 Common Alarm and Fault Codes

| Code | Meaning |
|------|---------|
| Alarm 14 | Earth fault |
| Alarm 16 | Short circuit |
| Alarm 29 | Heatsink temperature |
| Alarm 30 | Motor phase U missing |
| Alarm 31 | Motor phase V missing |
| Alarm 32 | Motor phase W missing |
| Alarm 38 | Internal fault |
| Alarm 46 | Power card supply |
| Alarm 51 | AMA check failed |
| Alarm 57 | DC link undervoltage |
| Alarm 59 | Current limit |
| Alarm 80 | Drive initialized to default value |

## Common Causes by Code

- **Alarm 14** — Ground leakage on the motor or output cable. Meg the motor and cable separately before blaming the drive.
- **Alarm 16** — Output short circuit or failed power module. Disconnect the motor leads and see if the drive still faults.
- **Alarm 29** — Poor cooling, blocked fan path, or ambient temperature too high. FC302 drives in dirty cabinets collect lint fast.
- **Alarm 30/31/32** — Missing motor phase. Check output terminals, motor leads, and winding continuity.
- **Alarm 38** — Internal electronics fault. Power cycle once, then capture the exact subcode if it returns.
- **Alarm 57** — Incoming line voltage is too low or unstable. Check upstream contactor, fuses, transformer taps, and voltage under load.
- **Alarm 59** — The drive is hitting current limit. The machine may be overloaded, jammed, or tuned too aggressively.

## Step-by-Step Fix {#fix}

1. **Pull the alarm log** — Use the LCP to review active alarm, warning log, and operating values.
2. **Check line power** — Measure incoming voltage and imbalance at the drive terminals under load.
3. **Isolate output wiring** — For ground, short, or missing phase alarms, disconnect the motor and cable and test them independently.
4. **Inspect cooling path** — Clean heatsinks, verify all internal fans, and confirm cabinet ventilation is working.
5. **Review setup and AMA** — Alarm 51 often means motor data is wrong or the motor could not be decoupled for auto-tune.
6. **Reset and monitor** — After fixes, run the machine through the exact process step that previously triggered the alarm.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Cooling fan kit | [Amazon](https://www.amazon.com/s?k=Cooling+fan+kit&tag=errorcodefixes-20) \| Common maintenance item on older FC302 drives |
| Input fuses | [Amazon](https://www.amazon.com/s?k=Input+fuses&tag=errorcodefixes-20) \| Check for undervoltage or single-phasing |
| Motor cable | [Amazon](https://www.amazon.com/s?k=Motor+cable&tag=errorcodefixes-20) \| Replace if insulation is damaged |
| LCP keypad | [Amazon](https://www.amazon.com/s?k=LCP+keypad&tag=errorcodefixes-20) \| Useful when display or navigation is unreliable |
| Power card | [Amazon](https://www.amazon.com/s?k=Power+card&tag=errorcodefixes-20) \| Possible cause of Alarm 46 or internal faults |
| Drive | [Amazon](https://www.amazon.com/s?k=Drive&tag=errorcodefixes-20) \| For persistent Alarm 38 or output section failures |
## When to Call a Pro

Alarm 38 and repeated short-circuit trips with the motor disconnected usually point to internal drive damage. Danfoss service or a qualified repair shop can often test the power module before you replace the whole FC302.
