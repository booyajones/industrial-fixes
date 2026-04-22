---
title: "Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes"
description: "Complete fault code guide for the Danfoss VLT AutomationDrive FC302, covering alarm and warning codes, causes, and step-by-step troubleshooting."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning |
|------|---------|
| [Alarm 14](https://www.amazon.com/s?k=Alarm%2014&tag=errorcodefixe-20) | Earth fault |
| [Alarm 16](https://www.amazon.com/s?k=Alarm%2016&tag=errorcodefixe-20) | Short circuit |
| [Alarm 29](https://www.amazon.com/s?k=Alarm%2029&tag=errorcodefixe-20) | Heatsink temperature |
| [Alarm 30](https://www.amazon.com/s?k=Alarm%2030&tag=errorcodefixe-20) | Motor phase U missing |
| [Alarm 31](https://www.amazon.com/s?k=Alarm%2031&tag=errorcodefixe-20) | Motor phase V missing |
| [Alarm 32](https://www.amazon.com/s?k=Alarm%2032&tag=errorcodefixe-20) | Motor phase W missing |
| [Alarm 38](https://www.amazon.com/s?k=Alarm%2038&tag=errorcodefixe-20) | Internal fault |
| [Alarm 46](https://www.amazon.com/s?k=Alarm%2046&tag=errorcodefixe-20) | Power card supply |
| [Alarm 51](https://www.amazon.com/s?k=Alarm%2051&tag=errorcodefixe-20) | AMA check failed |
| [Alarm 57](https://www.amazon.com/s?k=Alarm%2057&tag=errorcodefixe-20) | DC link undervoltage |
| [Alarm 59](https://www.amazon.com/s?k=Alarm%2059&tag=errorcodefixe-20) | Current limit |
| [Alarm 80](https://www.amazon.com/s?k=Alarm%2080&tag=errorcodefixe-20) | Drive initialized to default value |

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
| [Cooling fan kit](https://www.amazon.com/s?k=Cooling%20fan%20kit&tag=errorcodefixe-20) | Common maintenance item on older FC302 drives |
| [Input fuses](https://www.amazon.com/s?k=Input%20fuses&tag=errorcodefixe-20) | Check for undervoltage or single-phasing |
| [Motor cable](https://www.amazon.com/s?k=Motor%20cable&tag=errorcodefixe-20) | Replace if insulation is damaged |
| [LCP keypad](https://www.amazon.com/s?k=LCP%20keypad&tag=errorcodefixe-20) | Useful when display or navigation is unreliable |
| [Power card](https://www.amazon.com/s?k=Power%20card&tag=errorcodefixe-20) | Possible cause of Alarm 46 or internal faults |
| [Drive](https://www.amazon.com/s?k=Drive&tag=errorcodefixe-20) | For persistent Alarm 38 or output section failures |

## When to Call a Pro

Alarm 38 and repeated short-circuit trips with the motor disconnected usually point to internal drive damage. Danfoss service or a qualified repair shop can often test the power module before you replace the whole FC302.
