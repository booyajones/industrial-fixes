---
title: "Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series"
description: "Daikin Applied chiller fault codes for WMC, AGZ, ALZ, and centrifugal chillers: alarm descriptions, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - chiller
  - daikin-applied
  - hvac
  - industrial
---

## Daikin Applied Chiller Fault Codes — Quick Reference

Daikin Applied chillers (WMC water-cooled scroll, AGZ air-cooled, ALZ air-cooled scroll, and centrifugal units) use the MicroTech III or MicroTech 4 controller to display alarms and shutdowns.

| [Fault Code](https://www.amazon.com/s?k=Fault%20Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|-----------|
| Low Pressure Cutout | [Suction pressure too low](https://www.amazon.com/s?k=Suction%20pressure%20too%20low&tag=errorcodefixe-20) | Check refrigerant charge and evaporator flow |
| [High Pressure Cutout](https://www.amazon.com/s?k=High%20Pressure%20Cutout&tag=errorcodefixe-20) | Discharge pressure too high | Check condenser flow/fan and refrigerant | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Low Evaporator LWT | Leaving water temp too low | [Check flow rate and load](https://www.amazon.com/s?k=Check%20flow%20rate%20and%20load&tag=errorcodefixe-20) |  | High Motor Temp | [Compressor motor temperature high](https://www.amazon.com/s?k=Compressor%20motor%20temperature%20high&tag=errorcodefixe-20) | Check voltage, load, and cooling |
| [Freeze Protection](https://www.amazon.com/s?k=Freeze%20Protection&tag=errorcodefixe-20) | Evaporator temperature near freeze | Check flow, setpoints, and antifreeze | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Comm Fault | Controller communication loss | [Check BACnet/Modbus wiring](https://www.amazon.com/s?k=Check%20BACnet%2FModbus%20wiring&tag=errorcodefixe-20) |  | Compressor Fault | [Compressor protection tripped](https://www.amazon.com/s?k=Compressor%20protection%20tripped&tag=errorcodefixe-20) | Check motor protection and contactor |
| [Low Refrigerant](https://www.amazon.com/s?k=Low%20Refrigerant&tag=errorcodefixe-20) | Refrigerant pressure low on both sides | Inspect for leaks, check charge | [## Most Common Faults

### Low Pressure Cutout
Low suction pressure is the most frequent chiller alarm. On water-cooled units, check the chilled water flow rate through the evaporator — low flow causes the refrigerant to get too cold. Also check refrigerant charge. On air-cooled units, verify ambient temperature is within the unit's operating range.

### High Pressure Cutout
Discharge pressure is too high. On air-cooled chillers, check: condenser coil cleanliness, fan operation (all fans running), and ambient temperature. On water-cooled units, check condenser water flow rate and entering condenser water temperature.

### Freeze Protection
The evaporator approach temperature has reached the freeze protection threshold. Check for: low chilled water flow (pump failure, valve closed), low load causing low flow, or incorrect setpoints. Do not defeat freeze protection — a frozen evaporator is a major repair.

## MicroTech III Navigation

1. HOME → ALARMS to view active alarms
2. ALARM HISTORY to view past events with timestamp and conditions
3. SETPOINTS to verify operating limits
4. UNIT STATUS to view live sensor readings

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Faults%0A%0A%23%23%23%20Low%20Pressure%20Cutout%0ALow%20suction%20pressure%20is%20the%20most%20frequent%20chiller%20alarm.%20On%20water-cooled%20units%2C%20check%20the%20chilled%20water%20flow%20rate%20through%20the%20evaporator%20%E2%80%94%20low%20flow%20causes%20the%20refrigerant%20to%20get%20too%20cold.%20Also%20check%20refrigerant%20charge.%20On%20air-cooled%20units%2C%20verify%20ambient%20temperature%20is%20within%20the%20unit's%20operating%20range.%0A%0A%23%23%23%20High%20Pressure%20Cutout%0ADischarge%20pressure%20is%20too%20high.%20On%20air-cooled%20chillers%2C%20check%3A%20condenser%20coil%20cleanliness%2C%20fan%20operation%20(all%20fans%20running)%2C%20and%20ambient%20temperature.%20On%20water-cooled%20units%2C%20check%20condenser%20water%20flow%20rate%20and%20entering%20condenser%20water%20temperature.%0A%0A%23%23%23%20Freeze%20Protection%0AThe%20evaporator%20approach%20temperature%20has%20reached%20the%20freeze%20protection%20threshold.%20Check%20for%3A%20low%20chilled%20water%20flow%20(pump%20failure%2C%20valve%20closed)%2C%20low%20load%20causing%20low%20flow%2C%20or%20incorrect%20setpoints.%20Do%20not%20defeat%20freeze%20protection%20%E2%80%94%20a%20frozen%20evaporator%20is%20a%20major%20repair.%0A%0A%23%23%20MicroTech%20III%20Navigation%0A%0A1.%20HOME%20%E2%86%92%20ALARMS%20to%20view%20active%20alarms%0A2.%20ALARM%20HISTORY%20to%20view%20past%20events%20with%20timestamp%20and%20conditions%0A3.%20SETPOINTS%20to%20verify%20operating%20limits%0A4.%20UNIT%20STATUS%20to%20view%20live%20sensor%20readings%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Refrigerant charge | Common after leaks | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condenser fan motor | Replace on high pressure faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Flow switch | Inspect on low pressure and freeze faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure transducer | Check on unexplained pressure readings |

## Jump to Fix

- **Low pressure** → Check chilled water flow → Check refrigerant charge → Inspect evaporator
- **High pressure** → Check condenser coil → Verify all fans running → Check condenser water
- **Freeze protection** → Confirm flow rate → Check pump and valves → Verify setpoints

## When to Call a Pro
Daikin Applied service providers handle refrigerant work, compressor replacement, and control system configuration. Contact Daikin Applied service at 1-877-554-4834.
