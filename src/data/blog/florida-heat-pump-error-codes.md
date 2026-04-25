---
title: "Florida Heat Pump Error Codes Guide"
description: "Complete guide to Florida Heat Pump (FHP) error codes for water-to-air and water-to-water geothermal units. Fault codes, diagnostic steps, and fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - florida-heat-pump
  - geothermal
  - heat-pump
---

# Florida Heat Pump Error Codes: Complete Technician Guide

Florida Heat Pump (FHP), now part of Bosch Thermotechnology, manufactures water-source and geothermal heat pumps used in commercial and residential applications. FHP units display fault codes on the DDC (digital display controller) or communicate via the optional ECA (extended control accessory) board.

## FHP Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| E1 | High-pressure lockout | High loop/water temp, low airflow, dirty coil |
| E2 | Low-pressure lockout | Low refrigerant, low airflow, low loop flow |
| E3 | Freeze protection — refrigerant | Low refrigerant temp — airside issue |
| E4 | Freeze protection — water coil | Low entering water temperature |
| E5 | High discharge temperature | Low refrigerant, restricted TXV |
| E6 | Compressor overload | High amps — check compressor and supply voltage |
| E7 | Low voltage lockout | Supply voltage below minimum |
| E8 | Communication fault | Check wiring between control boards |
| E9 | Condensate overflow | Clogged drain pan or condensate pump |
| F1 | Entering water sensor fault | Check sensor wiring and resistance |
| F2 | Leaving water sensor fault | Check sensor at water outlet |
| F3 | Entering air sensor fault | Check sensor at return air |
| F4 | Leaving air sensor fault | Check sensor at supply air |
| H1 | Hard lockout | 3 fault trips — manual reset required |

## Most Common FHP Faults

### E1 — High Pressure Lockout
The most common FHP commercial fault, especially in summer:
1. Check entering water temperature — above 90°F causes high head pressure
2. Inspect air filter and blower motor
3. Check refrigerant charge (subcooling)
4. Verify cooling tower or loop system operation

### E2 — Low Pressure Lockout
1. Check air filter and blower
2. Check loop pump operation and flow rate
3. Check refrigerant charge with gauges
4. Inspect TXV for restriction

### E3 / E4 — Freeze Protection
- E3: Air-side issue — dirty filter or low airflow in cooling
- E4: Water-side issue — low loop water temperature (below 40°F entering)
- Check antifreeze concentration in loop (propylene glycol recommended)

### F1 / F2 / F3 / F4 — Sensor Faults
FHP temperature sensors are typically 10K ohm NTC thermistors. Check:
- Sensor resistance at known temperature (10K ohm at 77°F)
- Wiring continuity
- Sensor position and mounting

## FHP vs Bosch Branding Note

FHP units manufactured after 2015 may show Bosch Thermotechnology branding. The fault codes and diagnostic procedures are identical. Service manuals reference both FHP and Bosch part numbers.

## FHP Parts Reference

| Part | Notes |
|---|---|
| [High/low pressure switch](https://www.amazon.com/s?k=High%2Flow+pressure+switch&tag=errorcodefixes-20) | Match refrigerant and trip pressure |
| [Temperature sensor](https://www.amazon.com/s?k=Temperature+sensor&tag=errorcodefixes-20) | 10K NTC thermistor — FHP part 02531-016 |
| [TXV assembly](https://www.amazon.com/s?k=TXV+assembly&tag=errorcodefixes-20) | Match capacity and refrigerant type |
| [DDC control board](https://www.amazon.com/s?k=DDC+control+board&tag=errorcodefixes-20) | FHP/Bosch part — match model number |
| [ECA accessory board](https://www.amazon.com/s?k=ECA+accessory+board&tag=errorcodefixes-20) | For advanced controls and monitoring |

> **Note:** FHP/Bosch geothermal units have a hard lockout after 3 consecutive fault trips. After correcting the root cause, reset via the DDC controller or by cycling power at the breaker for 60 seconds.
