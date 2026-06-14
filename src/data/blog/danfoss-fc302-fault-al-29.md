---
title: "Danfoss FC302 Alarm AL 29 — Causes & Fix"
description: "What Danfoss FC302 Alarm AL 29 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "FC302 cooling fan assembly"
most_likely_cause: "Clogged cooling fan or heat sink fins"
---

## Danfoss FC302 Alarm AL 29 — What It Means

Alarm AL 29 on the Danfoss FC302 (VLT AutomationDrive) indicates heat sink overtemperature — the drive's power module heat sink exceeded the maximum allowable temperature and the drive shut down to prevent IGBT damage. The FC302 monitors heat sink temperature continuously; when it reaches the trip threshold (typically 90–95°C), AL 29 triggers immediately.

[Jump to Fix](#fix)

## Common Causes

- **Clogged cooling fan or heat sink fins** — Dust and debris accumulate in the drive's internal fan and heat sink fins, reducing airflow and causing heat buildup. Most common cause.
- **Ambient temperature too high** — The FC302 is rated for ambient temperatures up to 45°C (113°F) at full load. Operating in a hot panel or enclosure above this triggers AL 29.
- **Duty cycle exceeded** — Running the drive at 100% output continuously without adequate derating causes sustained high heat sink temperatures.
- **Cooling fan motor failure** — A failed internal cooling fan allows the heat sink to overheat even with clean fins and correct ambient temperature.

## Step-by-Step Fix {#fix}

1. **Power down and clean the drive** — Remove power, then use compressed air to blow out the heat sink fins and fan blades. Danfoss FC302 units in industrial environments need cleaning every 6–12 months.
2. **Check ambient temperature** — Measure the temperature inside the panel. If above 40°C, add ventilation, relocate the drive, or derate per the FC302 derating table in the manual.
3. **Test the cooling fan** — Power up (without enabling the drive output) and listen/feel for the internal fan. The FC302 fan runs continuously when powered. No airflow = failed fan.
4. **Check for duty cycle overload** — Review the load profile. If the motor runs at 100% continuously on a demanding application, check the drive's current derating at the actual ambient and derate if needed.
5. **Reset and restart** — Press [Reset] on the LCP panel or toggle the reset input. Monitor heat sink temperature (parameter 16-34) after restart to confirm it stays below the trip level.

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-fault-al-29&k=FC302+cooling+fan+assembly&tag=errorcodefixes-20) \| Match to drive frame size — A2/A3/B1/B2/etc. |
| Panel ventilation / cooling unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-fault-al-29&k=Panel+ventilation+%2F+cooling+unit&tag=errorcodefixes-20) \| If ambient temp is the root cause |
## When to Call a Pro

If the drive trips AL 29 immediately after restart with clean fins and correct ambient, the thermal sensor or IGBT module may have failed. Danfoss authorized service handles internal component replacement.

## See Also

- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
