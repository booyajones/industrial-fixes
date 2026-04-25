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
| Internal cooling fan (drive-specific) | [Amazon](https://www.amazon.com/s?k=Internal+cooling+fan+%28drive-specific%29&tag=errorcodefixes-20) \| Required when fan bearing has seized; AB part number varies by frame size |
| Enclosure thermostat-controlled fan | [Amazon](https://www.amazon.com/s?k=Enclosure+thermostat-controlled+fan&tag=errorcodefixes-20) \| Add when ambient temps run high |
| Compressed air canister or shop air | [Amazon](https://www.amazon.com/s?k=Compressed+air+canister+or+shop+air&tag=errorcodefixes-20) \| For routine cleaning every 6–12 months |
## When to Call a Pro

If F35 returns immediately after cleaning and the internal fan is confirmed running, the thermistor itself may have failed (reading falsely high). Thermistor replacement requires drive disassembly and an authorized AB service provider or qualified industrial electrician.

## Related Articles

- [Allen-Bradley MicroLogix 1400 Common Fault Codes](/posts/allen-bradley-micrologix-fault/)
- [Allen-Bradley PowerFlex 40 Complete Fault Code Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen Bradley PowerFlex 40 F2 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f2-fault/)
- [Allen-Bradley PowerFlex 40 F3 Fault — Power Loss](/posts/allen-bradley-powerflex-40-f3/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)
