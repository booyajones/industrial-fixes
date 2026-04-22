---
title: "York YCD Packaged Unit Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to York YCD packaged rooftop unit error codes, diagnostic LED flash sequences, common fault causes, and step-by-step repair procedures."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
  - packaged-unit
  - commercial
---

## York YCD Packaged Unit Error Codes — What They Mean

The York YCD is a commercial single-packaged gas/electric rooftop unit available in 3–12.5 ton capacities. It is a self-contained unit that integrates the condenser, evaporator, gas furnace, and blower in a single cabinet for rooftop installation. The YCD uses an on-board microprocessor controller that communicates faults through status LEDs and, in Johnson Controls-connected systems, through BACnet or N2 communication protocols.

[Jump to Fix](#fix)

## York YCD Status LED / Fault Code Reference

| [LED Code](https://www.amazon.com/s?k=LED%20Code&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — no fault |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Compressor lockout — 3 consecutive high-pressure trips |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Compressor lockout — 3 consecutive low-pressure trips |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Low ambient lockout |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Outdoor fan fault |
| [8 flashes](https://www.amazon.com/s?k=8%20flashes&tag=errorcodefixe-20) | Return air sensor fault |
| [9 flashes](https://www.amazon.com/s?k=9%20flashes&tag=errorcodefixe-20) | Discharge air sensor fault |
| [10 flashes](https://www.amazon.com/s?k=10%20flashes&tag=errorcodefixe-20) | Communication fault — BACnet/N2 |
| [11 flashes](https://www.amazon.com/s?k=11%20flashes&tag=errorcodefixe-20) | Condenser coil sensor fault |
| [Solid ON](https://www.amazon.com/s?k=Solid%20ON&tag=errorcodefixe-20) | Freeze protection active |

## Common Causes by Code

- **2 flashes — High pressure** — Dirty condenser coil is the dominant cause on packaged rooftop units because they accumulate bird droppings, cottonwood, and rooftop debris. Also check that condenser fan blade pitch hasn't changed (plastic blades warp in high UV environments).
- **3/5 flashes — Low pressure** — Refrigerant undercharge or evaporator freeze. The YCD evaporator can freeze in high-humidity/low-load conditions if the indoor blower motor or filter is restricting airflow.
- **4 flashes — Compressor lockout (high pressure)** — After three high-pressure trips, the YCD locks out the compressor and requires a manual reset (cycle power at the disconnect or reset at the thermostat/DDC controller).
- **7 flashes — Outdoor fan fault** — Failed condenser fan motor or capacitor. YCD units have one or two condenser fan motors depending on tonnage — check both if applicable.
- **10 flashes — Communication** — BACnet or N2 communication loss between the YCD unit controller and the building management system. Check wiring, EOL termination resistors, and BMS addressing.

## Step-by-Step Fix {#fix}

1. **Access the control section** — Open the control box panel on the YCD (usually the end panel facing the building). The unit controller and LED indicator are mounted here. Note the LED flash pattern before clearing.
2. **For 2 or 4 flashes (high pressure)** — Inspect condenser coils on both sides of the unit. On YCD rooftop units, debris accumulates fastest on the prevailing wind side. Use a coil cleaner and low-pressure water rinse. Confirm condenser fan motors are running and drawing correct amperage.
3. **For 3 or 5 flashes (low pressure)** — Check evaporator coil for ice — if the coil is frozen, the airside is restricted. Check filters first. If filters are clean, inspect the blower motor for proper RPM and belt tension (on belt-drive models).
4. **For Code 4 lockout** — After coil cleaning, cycle power at the main disconnect to reset the lockout. Do not manually bypass the high-pressure switch — find the root cause before resuming operation.
5. **Communication fault (10 flashes)** — Check the N2/BACnet wiring for shorts or open circuits. Verify the unit address matches the BMS configuration. Check EOL resistor placement — only the last device on the bus should have the EOL jumper installed.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | For condenser fan motor |
| [Condenser fan motor](https://www.amazon.com/s?k=Condenser%20fan%20motor&tag=errorcodefixe-20) | Match tonnage — 3-ton and 5-ton use different motors |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | 610 PSIG cutout for R-410A |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | 50 PSIG cutout |
| [Discharge air sensor](https://www.amazon.com/s?k=Discharge%20air%20sensor&tag=errorcodefixe-20) | NTC thermistor; check resistance at known temperature |
| [Unit controller board](https://www.amazon.com/s?k=Unit%20controller%20board&tag=errorcodefixe-20) | For persistent communication or sensor faults |

## When to Call a Pro

York YCD packaged units are commercial equipment requiring HVAC-R licensed technicians for refrigerant work. BACnet/N2 communication troubleshooting typically requires access to the building management system and a BMS-capable service technician. Compressor replacement on a YCD is a multi-hour job requiring refrigerant recovery equipment.
