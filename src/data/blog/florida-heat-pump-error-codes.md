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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| E1 | [High-pressure lockout](https://www.amazon.com/s?k=High-pressure%20lockout&tag=errorcodefixe-20) | High loop/water temp, low airflow, dirty coil |
| [E2](https://www.amazon.com/s?k=E2&tag=errorcodefixe-20) | Low-pressure lockout | Low refrigerant, low airflow, low loop flow | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E3 | Freeze protection — refrigerant | [Low refrigerant temp — airside issue](https://www.amazon.com/s?k=Low%20refrigerant%20temp%20%E2%80%94%20airside%20issue&tag=errorcodefixe-20) |  | E4 | [Freeze protection — water coil](https://www.amazon.com/s?k=Freeze%20protection%20%E2%80%94%20water%20coil&tag=errorcodefixe-20) | Low entering water temperature |
| [E5](https://www.amazon.com/s?k=E5&tag=errorcodefixe-20) | High discharge temperature | Low refrigerant, restricted TXV | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E6 | Compressor overload | [High amps — check compressor and supply voltage](https://www.amazon.com/s?k=High%20amps%20%E2%80%94%20check%20compressor%20and%20supply%20voltage&tag=errorcodefixe-20) |  | E7 | [Low voltage lockout](https://www.amazon.com/s?k=Low%20voltage%20lockout&tag=errorcodefixe-20) | Supply voltage below minimum |
| [E8](https://www.amazon.com/s?k=E8&tag=errorcodefixe-20) | Communication fault | Check wiring between control boards | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E9 | Condensate overflow | [Clogged drain pan or condensate pump](https://www.amazon.com/s?k=Clogged%20drain%20pan%20or%20condensate%20pump&tag=errorcodefixe-20) |  | F1 | [Entering water sensor fault](https://www.amazon.com/s?k=Entering%20water%20sensor%20fault&tag=errorcodefixe-20) | Check sensor wiring and resistance |
| [F2](https://www.amazon.com/s?k=F2&tag=errorcodefixe-20) | Leaving water sensor fault | Check sensor at water outlet | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | F3 | Entering air sensor fault | [Check sensor at return air](https://www.amazon.com/s?k=Check%20sensor%20at%20return%20air&tag=errorcodefixe-20) |  | F4 | [Leaving air sensor fault](https://www.amazon.com/s?k=Leaving%20air%20sensor%20fault&tag=errorcodefixe-20) | Check sensor at supply air |
| [H1](https://www.amazon.com/s?k=H1&tag=errorcodefixe-20) | Hard lockout | 3 fault trips — manual reset required | [## Most Common FHP Faults

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

## FHP Parts Reference](https://www.amazon.com/s?k=%23%23%20Most%20Common%20FHP%20Faults%0A%0A%23%23%23%20E1%20%E2%80%94%20High%20Pressure%20Lockout%0AThe%20most%20common%20FHP%20commercial%20fault%2C%20especially%20in%20summer%3A%0A1.%20Check%20entering%20water%20temperature%20%E2%80%94%20above%2090%C2%B0F%20causes%20high%20head%20pressure%0A2.%20Inspect%20air%20filter%20and%20blower%20motor%0A3.%20Check%20refrigerant%20charge%20(subcooling)%0A4.%20Verify%20cooling%20tower%20or%20loop%20system%20operation%0A%0A%23%23%23%20E2%20%E2%80%94%20Low%20Pressure%20Lockout%0A1.%20Check%20air%20filter%20and%20blower%0A2.%20Check%20loop%20pump%20operation%20and%20flow%20rate%0A3.%20Check%20refrigerant%20charge%20with%20gauges%0A4.%20Inspect%20TXV%20for%20restriction%0A%0A%23%23%23%20E3%20%2F%20E4%20%E2%80%94%20Freeze%20Protection%0A-%20E3%3A%20Air-side%20issue%20%E2%80%94%20dirty%20filter%20or%20low%20airflow%20in%20cooling%0A-%20E4%3A%20Water-side%20issue%20%E2%80%94%20low%20loop%20water%20temperature%20(below%2040%C2%B0F%20entering)%0A-%20Check%20antifreeze%20concentration%20in%20loop%20(propylene%20glycol%20recommended)%0A%0A%23%23%23%20F1%20%2F%20F2%20%2F%20F3%20%2F%20F4%20%E2%80%94%20Sensor%20Faults%0AFHP%20temperature%20sensors%20are%20typically%2010K%20ohm%20NTC%20thermistors.%20Check%3A%0A-%20Sensor%20resistance%20at%20known%20temperature%20(10K%20ohm%20at%2077%C2%B0F)%0A-%20Wiring%20continuity%0A-%20Sensor%20position%20and%20mounting%0A%0A%23%23%20FHP%20vs%20Bosch%20Branding%20Note%0A%0AFHP%20units%20manufactured%20after%202015%20may%20show%20Bosch%20Thermotechnology%20branding.%20The%20fault%20codes%20and%20diagnostic%20procedures%20are%20identical.%20Service%20manuals%20reference%20both%20FHP%20and%20Bosch%20part%20numbers.%0A%0A%23%23%20FHP%20Parts%20Reference&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | High/low pressure switch | Match refrigerant and trip pressure | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Temperature sensor | 10K NTC thermistor — FHP part 02531-016 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | TXV assembly | Match capacity and refrigerant type | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | DDC control board | FHP/Bosch part — match model number | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ECA accessory board | For advanced controls and monitoring |

> **Note:** FHP/Bosch geothermal units have a hard lockout after 3 consecutive fault trips. After correcting the root cause, reset via the DDC controller or by cycling power at the breaker for 60 seconds.
