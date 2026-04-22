---
title: "Cummins Onan Generator Fault Codes — Complete Guide"
description: "Cummins Onan generator fault codes for RV QG, commercial RS, and MDKD series: all fault codes, alarm meanings, causes, and fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - generator
  - cummins
  - onan
  - electrical
---

## Cummins Onan Generator Fault Codes — Quick Reference

Cummins Onan generators cover the range from compact RV gensets (QG 2500, QD 3200) to commercial diesel generators (MDKD, DSGAA series). Fault codes are displayed on the generator control panel or via the Onan app. RV-series generators use a simplified blink code system.

| Code | Series | Meaning | Quick Fix |
|------|--------|---------|-----------|
| 2 blinks | RV QG/QD | Low oil pressure | Add oil; check oil sender |
| 3 blinks | RV QG/QD | High coolant temperature | Check coolant; check fan |
| 4 blinks | RV QG/QD | Overcrank (fail to start) | Check fuel, spark, choke |
| 5 blinks | RV QG/QD | Field (voltage) fault | AVR or control board issue |
| 6 blinks | RV QG/QD | Governor fault | Governor calibration needed |
| 7 blinks | RV QG/QD | Controller fault | Replace control board |
| 8 blinks | RV QG/QD | Low voltage / high voltage | Load issue or AVR fault |
| Code 13 | Commercial | Low oil pressure warning | Check oil level |
| Code 14 | Commercial | Low oil pressure shutdown | Immediate shutdown — add oil |
| Code 22 | Commercial | High coolant temp warning | Check cooling system |
| Code 23 | Commercial | High coolant temp shutdown | Stop generator; check coolant |
| Code 35 | Commercial | Engine fail to start | Check fuel, battery, starter |
| Code 36 | Commercial | Engine overspeed | Governor problem |
| Code 45 | Commercial | Low fuel | Refuel |
| Code 54 | Commercial | Battery charger fault | Check charger AC supply |

## Most Common Faults

### 4 Blinks / Code 35 — Fail to Start (Overcrank)
**RV Generators (QG 2500, QD 3200):**
The most common failure on RV Onan generators. Root causes by frequency:
1. **Fuel delivery:** RV generators pull fuel from the main fuel tank via a small pickup tube. If the tank is below 1/4 full, the pickup may not reach fuel, especially on grades. Fill the tank and retry.
2. **Carburetor varnish:** RV generators often sit for months between uses. A varnished carburetor main jet is very common. Remove the bowl, clean the jet with a fine wire, and spray carburetor cleaner.
3. **Choke:** Onan RV generators have a vacuum-operated automatic choke. If the choke stays open on a cold start, the engine won't start. Check the choke vacuum hose and the choke butterfly plate.
4. **Spark plugs:** Replace spark plugs if the generator hasn't been serviced in 2+ years.

### 2 Blinks / Code 14 — Low Oil Pressure
For RV generators: use SAE 30 or 10W-30 per the Onan manual. Check the dipstick. If oil level is correct and the generator immediately shuts down on restart, the oil pressure sender may be failed. Bypass test: a technician can temporarily jumper the oil pressure switch to verify the engine actually has oil pressure.

### 5 Blinks — Field Fault (Voltage Fault)
The generator's field excitation circuit has a fault. This is usually the AVR (automatic voltage regulator) or the excitation winding in the alternator. The AVR on Onan QG/QD generators is a small board inside the control compartment. Inspect for burned components or loose connectors. If the AVR board shows burn damage, replace it.

### 3 Blinks / Code 22/23 — High Engine Temperature
On liquid-cooled commercial Onan generators, check the coolant level, radiator fins, thermostat, and water pump impeller. On the air-cooled RV QG series, check that the generator's cooling air inlet and exhaust openings are not blocked by debris or insulation material.

### Code 36 — Engine Overspeed
Onan commercial generators (MDKD, DSGAA) use a mechanical governor with electronic trim. Overspeed faults indicate the governor has lost control. Check the governor actuator wiring first — a failed or disconnected actuator is a common cause. On mechanical governors, check the flyweight assembly and governor spring.

## Onan RV Generator Maintenance

| Service Item | Interval |
|-------------|----------|
| Engine oil | Every 150 hours or annually |
| Air filter | Every 150 hours |
| Spark plugs | Every 150 hours |
| Fuel filter | Every 150 hours |
| Carburetor cleaning | As needed (every 2–3 seasons if run infrequently) |

## When to Call a Pro
Onan commercial generator faults (Code 22+, voltage faults, governor faults) require a Cummins-authorized service center. Do not attempt to adjust AVR or governor settings without proper test equipment and Onan service training.
