---
title: "Generac Generator Error Codes — Complete Guide"
description: "Generac generator error codes for Guardian, Protector, and PowerPact series: all alarm codes, causes, and step-by-step fixes for Generac standby generators."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - generator
  - generac
  - electrical
---

## Generac Generator Error Codes — Quick Reference

Generac standby generators display alarm codes on the Evolution controller display. Alarms are classified as Warnings (generator continues to run) or Shutdowns (generator stops and requires reset). The controller also stores fault history for the last 50 events. Access fault history: Menu → View History.

| Code | Type | Meaning | Quick Fix |
|------|------|---------|-----------|
| [1100](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1100&tag=errorcodefixes-20) | Warning | Low battery | Charge or replace battery |
| [1200](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1200&tag=errorcodefixes-20) | Warning | Low coolant | Add coolant; check for leaks |
| [1205](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1205&tag=errorcodefixes-20) | Shutdown | High coolant temperature | Check coolant; check fan |
| [1300](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1300&tag=errorcodefixes-20) | Warning | Low oil pressure warning | Check oil level |
| [1302](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1302&tag=errorcodefixes-20) | Shutdown | Low oil pressure shutdown | Add oil; check for leaks |
| [1400](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1400&tag=errorcodefixes-20) | Warning | Overcrank warning | Check battery; check starter |
| [1401](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1401&tag=errorcodefixes-20) | Shutdown | Overcrank — failed to start | Check fuel, spark, battery |
| [1500](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1500&tag=errorcodefixes-20) | Shutdown | Overspeed | Governor fault; speed sensor |
| [1501](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1501&tag=errorcodefixes-20) | Shutdown | Underspeed | Engine load, governor fault |
| [1600](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1600&tag=errorcodefixes-20) | Shutdown | Overfrequency | Governor problem |
| [1601](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1601&tag=errorcodefixes-20) | Shutdown | Underfrequency | Engine load, governor |
| [1700](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1700&tag=errorcodefixes-20) | Shutdown | Overvoltage | Voltage regulator fault |
| [1701](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1701&tag=errorcodefixes-20) | Shutdown | Undervoltage | AVR fault; load too high |
| [1900](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=1900&tag=errorcodefixes-20) | Shutdown | RPM sense loss | Magnetic pickup fault |
| [2100](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=2100&tag=errorcodefixes-20) | Warning | Check | General warning — see history |
| [2800](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=2800&tag=errorcodefixes-20) | Warning | Low fuel | Add fuel |
| [2900](https://www.amazon.com/s?ascsubtag=ecf-generac-generator-error-codes&k=2900&tag=errorcodefixes-20) | Shutdown | High AC voltage | Voltage regulator fault |

## Most Common Faults

### 1401 — Overcrank Shutdown (Failed to Start)
The most common Generac fault, especially on generators that are not exercised regularly. The engine cranked the maximum number of times without starting. 

**Most common causes and fixes:**
1. **Low battery:** Even if the battery holds a static charge, it may lack cranking amps. Test with a battery load tester. Generac uses 12V Group 26 or similar batteries — replace every 3–4 years.
2. **Stale fuel:** Gasoline degrades in 30–60 days. If the generator hasn't run on fresh fuel in months, drain the carburetor and add fresh fuel.
3. **Choke stuck:** On air-cooled generators, the automatic choke can stick. Check the choke plate on the carburetor — it should be nearly closed on a cold start.
4. **Spark plug fouled:** Remove and inspect the spark plug. A black, sooty plug indicates a rich condition; a white plug indicates lean. Gap should be 0.028–0.030 inches.

### 1302 — Low Oil Pressure Shutdown
The oil pressure sensor detected pressure below the minimum safe level. Always check the oil level first — if it's low, add the correct viscosity oil (typically SAE 5W-30 for most Generac air-cooled engines). If oil level is correct, the oil pressure sensor may have failed, or the engine may have an internal oil pressure issue (worn pump, worn bearings).

### 1205 — High Coolant Temperature (Liquid-Cooled Models)
Check the coolant level in the radiator overflow reservoir and the radiator itself. Inspect the radiator fins for debris (leaves, dirt). Verify the cooling fan is operating when the engine is running. Check the thermostat — a stuck-closed thermostat will rapidly overheat the engine.

### 1500 / 1501 — Overspeed / Underspeed
Engine speed is directly tied to output frequency (60 Hz requires ~3600 RPM for 2-pole alternators). Speed issues indicate:
- **Overspeed:** Governor spring has broken or governor linkage is stuck open
- **Underspeed:** Engine is overloaded, governor is stuck closed, or low fuel pressure
Check the governor linkage and spring on air-cooled units. On electronic governors, check the governor actuator wiring.

### 1900 — RPM Sense Loss
The magnetic pickup sensor (Hall effect sensor) that monitors flywheel speed has failed or lost its signal. This sensor is mounted close to the flywheel ring gear. Check the gap between the sensor tip and the ring gear teeth (typically 0.020–0.030 inches). Also inspect the sensor wiring for damage.

## Generac Weekly Exercise Reminder
Generac generators should run under load for 20+ minutes per week. Configure the exercise schedule on the Evolution controller: Menu → Setup → Exercise. Generators that only run the 5-minute default exercise cycle accumulate carbon deposits and are more likely to fail to start during actual outages.

## When to Call a Pro
Voltage regulator faults (1700, 1701, 2900) and governor problems require a Generac-certified service technician. Do not attempt to adjust AVR (automatic voltage regulator) trim pots without proper load bank equipment.
