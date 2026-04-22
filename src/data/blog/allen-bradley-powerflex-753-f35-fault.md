---
title: "Allen Bradley PowerFlex 753 F35 Fault — Causes & Fix"
description: "What Allen Bradley PowerFlex 753 F35 Heatsink Overtemp means, why it trips, and how to fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
---

## Allen Bradley PowerFlex 753 F35 Fault — What It Means

The Allen Bradley PowerFlex 753 **F35 fault** is a **Heatsink Overtemperature** trip. The drive's internal NTC thermistor monitors the power semiconductor heatsink temperature. When it exceeds the trip threshold (typically 90–100°C depending on drive rating), F35 fires and output shuts down to prevent IGBT damage. F35 is almost always caused by inadequate cooling rather than a failed drive component — meaning the fix is usually free or very cheap.

[Jump to Fix](#fix)

## Common Causes

- **Clogged cooling fan or blocked vents** — Dust buildup on the internal cooling fan blades or intake/exhaust vents reduces airflow dramatically; the heatsink temperature climbs under load.
- **Enclosure ambient too high** — If the drive enclosure exceeds 40°C ambient without derating, F35 will trip at loads that would be fine in cooler conditions.
- **Internal cooling fan failure** — The drive's internal fan can fail (bearing seized or motor failed). No airflow = rapid heatsink rise under any load.
- **Drive running above rated current continuously** — Extended operation above 100% FLA heats the heatsink faster than the cooling system can dissipate it.

## Step-by-Step Fix {#fix}

1. **Clean the cooling fan and vents** — Power down, lock out/tag out, and use compressed air to blow out the internal fan blades and all vent openings. This alone resolves the majority of F35 faults.
2. **Verify the internal fan runs** — Power up the drive (with no load if possible) and listen for the internal fan. It should run continuously or start when drive temperature reaches ~40°C. No fan sound = fan failure.
3. **Check enclosure temperature** — Use a thermometer to measure ambient temperature inside the enclosure. If above 40°C, add enclosure cooling (fan, AC unit, or heat exchanger) or derate the drive.
4. **Confirm drive loading** — Use the drive's parameter monitoring (Parameter 4 = Output Amps) to check actual current vs. drive rating. If running above 100% continuously, a larger frame drive may be needed.
5. **Reset the fault** — After cooling and cleaning, cycle power or press Stop/Reset. Monitor heatsink temperature via Parameter 35 (Drive Temp) to confirm it's back in range.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Internal cooling fan (drive-specific)](https://www.amazon.com/s?k=Internal%20cooling%20fan%20(drive-specific)&tag=errorcodefixe-20) | Required when fan bearing has seized; AB part number varies by frame size |
| [Enclosure thermostat-controlled fan](https://www.amazon.com/s?k=Enclosure%20thermostat-controlled%20fan&tag=errorcodefixe-20) | Add when ambient temps run high |
| [Compressed air canister or shop air](https://www.amazon.com/s?k=Compressed%20air%20canister%20or%20shop%20air&tag=errorcodefixe-20) | For routine cleaning every 6–12 months |

## When to Call a Pro

If F35 returns immediately after cleaning and the internal fan is confirmed running, the thermistor itself may have failed (reading falsely high). Thermistor replacement requires drive disassembly and an authorized AB service provider or qualified industrial electrician.
