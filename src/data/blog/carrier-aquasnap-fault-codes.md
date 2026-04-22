---
title: "Carrier AquaSnap Chiller Fault Codes — 30RB/30RQ Guide"
description: "Carrier AquaSnap 30RB and 30RQ chiller fault codes for i-Vue and Pro-Dialog controllers: alarms, safety shutdowns, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - chiller
  - carrier
  - aquasnap
  - hvac
---

## Carrier AquaSnap Chiller Fault Codes — Quick Reference

Carrier AquaSnap 30RB (air-cooled liquid chiller) and 30RQ (heat pump) use the Pro-Dialog+ or i-Vue controller. Alarms appear as codes with descriptions on the controller display.

| [Alarm Code](https://www.amazon.com/s?k=Alarm%20Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|-----------|
| A1 — Low Pressure | [Suction pressure safety](https://www.amazon.com/s?k=Suction%20pressure%20safety&tag=errorcodefixe-20) | Check refrigerant charge and evap flow |
| [A2 — High Pressure](https://www.amazon.com/s?k=A2%20%E2%80%94%20High%20Pressure&tag=errorcodefixe-20) | Discharge pressure safety | Check fans and condenser coil | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | A3 — Low LWT | Leaving water temp below limit | [Check flow and freeze protection](https://www.amazon.com/s?k=Check%20flow%20and%20freeze%20protection&tag=errorcodefixe-20) |  | A4 — Compressor Overload | [Compressor motor tripped](https://www.amazon.com/s?k=Compressor%20motor%20tripped&tag=errorcodefixe-20) | Check current, voltage, and contacts |
| [A5 — High Discharge Temp](https://www.amazon.com/s?k=A5%20%E2%80%94%20High%20Discharge%20Temp&tag=errorcodefixe-20) | Compressor discharge too hot | Check charge and condenser | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | A6 — Loss of Flow | Chilled water flow lost | [Check pump, filter, and flow switch](https://www.amazon.com/s?k=Check%20pump%2C%20filter%2C%20and%20flow%20switch&tag=errorcodefixe-20) |  | A7 — Loss of Phase | [Phase loss detected](https://www.amazon.com/s?k=Phase%20loss%20detected&tag=errorcodefixe-20) | Check electrical supply |
| [A8 — High Motor Temp](https://www.amazon.com/s?k=A8%20%E2%80%94%20High%20Motor%20Temp&tag=errorcodefixe-20) | Compressor thermal protection | Check voltage and cooling | [## Most Common Faults

### A1 — Low Pressure Alarm
Low refrigerant suction pressure is the top alarm on AquaSnap chillers. Check chilled water flow rate first — a closed pump valve, blocked strainer, or pump failure causes the evaporator to starve. If flow is confirmed, check the refrigerant charge.

### A2 — High Pressure Alarm
High discharge pressure trips are common in summer. Check: all condenser fans are running (visually verify), condenser coil is clean, and ambient temperature is within the unit's rating. 30RB units use multiple fans — if one fan fails, high pressure can follow on hot days.

### A6 — Loss of Flow
The flow switch in the evaporator has opened. Check: pump breaker, pump rotation (check at VFD if applicable), strainer, and flow switch condition. A dirty flow switch can give false trips.

## Pro-Dialog+ Controller Navigation

- **ALARM** button → shows active alarms and history
- **STATUS** button → live operating data (pressures, temperatures, current)
- **SETPOINTS** → operating limits configuration

## i-Vue Controller

The i-Vue touchscreen shows alarm icons in the top bar. Tap the icon to see fault description. The event history shows the last 200 events with timestamps.

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Faults%0A%0A%23%23%23%20A1%20%E2%80%94%20Low%20Pressure%20Alarm%0ALow%20refrigerant%20suction%20pressure%20is%20the%20top%20alarm%20on%20AquaSnap%20chillers.%20Check%20chilled%20water%20flow%20rate%20first%20%E2%80%94%20a%20closed%20pump%20valve%2C%20blocked%20strainer%2C%20or%20pump%20failure%20causes%20the%20evaporator%20to%20starve.%20If%20flow%20is%20confirmed%2C%20check%20the%20refrigerant%20charge.%0A%0A%23%23%23%20A2%20%E2%80%94%20High%20Pressure%20Alarm%0AHigh%20discharge%20pressure%20trips%20are%20common%20in%20summer.%20Check%3A%20all%20condenser%20fans%20are%20running%20(visually%20verify)%2C%20condenser%20coil%20is%20clean%2C%20and%20ambient%20temperature%20is%20within%20the%20unit's%20rating.%2030RB%20units%20use%20multiple%20fans%20%E2%80%94%20if%20one%20fan%20fails%2C%20high%20pressure%20can%20follow%20on%20hot%20days.%0A%0A%23%23%23%20A6%20%E2%80%94%20Loss%20of%20Flow%0AThe%20flow%20switch%20in%20the%20evaporator%20has%20opened.%20Check%3A%20pump%20breaker%2C%20pump%20rotation%20(check%20at%20VFD%20if%20applicable)%2C%20strainer%2C%20and%20flow%20switch%20condition.%20A%20dirty%20flow%20switch%20can%20give%20false%20trips.%0A%0A%23%23%20Pro-Dialog%2B%20Controller%20Navigation%0A%0A-%20**ALARM**%20button%20%E2%86%92%20shows%20active%20alarms%20and%20history%0A-%20**STATUS**%20button%20%E2%86%92%20live%20operating%20data%20(pressures%2C%20temperatures%2C%20current)%0A-%20**SETPOINTS**%20%E2%86%92%20operating%20limits%20configuration%0A%0A%23%23%20i-Vue%20Controller%0A%0AThe%20i-Vue%20touchscreen%20shows%20alarm%20icons%20in%20the%20top%20bar.%20Tap%20the%20icon%20to%20see%20fault%20description.%20The%20event%20history%20shows%20the%20last%20200%20events%20with%20timestamps.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condenser fan motor | Replace on A2 high pressure faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Flow switch | Replace on repeated A6 faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Refrigerant charge | After leak repair | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | High pressure switch | Replace if repeatedly tripping |

## Jump to Fix

- **A1 low pressure** → Check chilled water flow → Check refrigerant charge → Inspect evap
- **A2 high pressure** → Verify all fans running → Clean condenser coil
- **A6 loss of flow** → Check pump → Inspect strainer → Test flow switch

## When to Call a Pro
Carrier (Carrier Commercial Service) handles refrigerant work and compressor replacement. Call 1-800-379-6484 for service support.
