---
title: "ABB ACS550 AF10 Fault — Causes & Fix"
description: "What ABB ACS550 AF10 heatsink overtemperature means, why it trips, and how to clean and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS550 AF10 Fault — What It Means

The ABB ACS550 **AF10 fault** is a **Heatsink Overtemperature** fault. The drive's internal NTC thermistor monitors heatsink temperature. When it exceeds the protection limit (approximately 115°C for most frame sizes), AF10 fires and the drive shuts down output to protect the IGBTs. AF10 is almost always a maintenance or installation issue — dirty cooling fan, insufficient ventilation, or an ambient temperature problem — and resolves without replacing any drive hardware.

[Jump to Fix](#fix)

## Common Causes

- **Dirty internal cooling fan and heatsink fins** — Dust accumulation on the cooling fan blades and heatsink fins is the leading cause of AF10; airflow drops dramatically with even moderate buildup.
- **Cooling fan failure** — The ACS550's internal cooling fan can fail (bearing or motor); no airflow means the heatsink reaches trip temperature under any significant load.
- **Insufficient enclosure ventilation** — The drive requires minimum clearances and an ambient temperature below 40°C at full load. Tight enclosures trap heat.
- **Drive running above rated current** — Continuous operation above 100% of the drive's rated current generates more heat than the cooling system can dissipate.

## Step-by-Step Fix {#fix}

1. **Clean the cooling fan and heatsink** — Power off, lock out/tag out, and remove the drive's top cover. Use compressed air to clean the cooling fan blades, heatsink fins, and intake vents. This is the most common resolution — free and takes 10 minutes.
2. **Confirm the cooling fan operates** — Reconnect power (carefully, with cover off or using the viewing port). Verify the internal fan runs. A fan that doesn't spin, runs slowly, or makes grinding noises needs replacement.
3. **Check enclosure ambient temperature** — Measure the temperature inside the enclosure during operation. Above 40°C requires enclosure cooling equipment (thermostatically controlled fan, heat exchanger, or air conditioner).
4. **Verify mounting clearances** — ACS550 requires minimum 150mm clearance above and below the drive. Check that neighboring components aren't blocking airflow paths.
5. **Monitor heatsink temperature** — After cleaning, use parameter 01.19 (HEATSINK TEMP) to monitor the heatsink temperature in real time. Normal operating temperature should stay below 70–80°C at full load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Internal cooling fan | [Amazon](https://www.amazon.com/s?k=Internal+cooling+fan&tag=errorcodefixes-20) \| ABB part number varies by frame size (R1–R6); confirm before ordering |
| Enclosure thermostat fan unit | [Amazon](https://www.amazon.com/s?k=Enclosure+thermostat+fan+unit&tag=errorcodefixes-20) \| Install when ambient routinely exceeds 40°C |
## When to Call a Pro

If AF10 returns immediately after cleaning and the internal fan is confirmed running, and the drive is within its rated ambient and load limits, the heatsink thermistor may have drifted or failed. Internal thermistor replacement requires drive disassembly and ABB-certified service.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
