---
title: "York Rooftop Unit Error Codes: Technician Guide"
description: "Complete York RTU error code guide for Predator, Affinity, and ZF series. Flash codes, alphanumeric faults, and field fixes for commercial rooftop units."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
  - rooftop-unit
  - commercial-hvac
---

# York Rooftop Unit Error Codes: Complete Technician Guide

York commercial RTUs (Predator, Affinity, ZF, YCIV series) use LED flash codes and alphanumeric displays to communicate faults. York RTU equipment is also sold under the Luxaire and Coleman commercial brands with identical codes.

## Reading York RTU Flash Codes

The IFC diagnostic LED flashes codes in groups:
- Single-digit faults: X flashes, pause, repeat
- Two-digit faults: X flashes, short pause, Y flashes, long pause

## York RTU Flash Code Table

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Fault | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| 2 | [Low-pressure lockout](https://www.amazon.com/s?k=Low-pressure%20lockout&tag=errorcodefixe-20) | Low refrigerant charge |
| [3](https://www.amazon.com/s?k=3&tag=errorcodefixe-20) | High-pressure lockout | Dirty condenser coil, fan failure | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 4 | Limit switch open | [Airflow restriction, dirty filter](https://www.amazon.com/s?k=Airflow%20restriction%2C%20dirty%20filter&tag=errorcodefixe-20) |  | 5 | [Rollout switch open](https://www.amazon.com/s?k=Rollout%20switch%20open&tag=errorcodefixe-20) | Cracked heat exchanger, blocked burner |
| [6](https://www.amazon.com/s?k=6&tag=errorcodefixe-20) | Ignition lockout | No ignition after 3 attempts | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 7 | Flame signal lost | [Dirty or failed flame sensor](https://www.amazon.com/s?k=Dirty%20or%20failed%20flame%20sensor&tag=errorcodefixe-20) |  | 8 | [Blower motor fault](https://www.amazon.com/s?k=Blower%20motor%20fault&tag=errorcodefixe-20) | Motor or capacitor failed |
| [2-2](https://www.amazon.com/s?k=2-2&tag=errorcodefixe-20) | Low-pressure switch stuck closed | Replace pressure switch | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 3-3 | High-pressure switch stuck closed | [Replace pressure switch](https://www.amazon.com/s?k=Replace%20pressure%20switch&tag=errorcodefixe-20) |  | 4-1 | [Primary limit fault](https://www.amazon.com/s?k=Primary%20limit%20fault&tag=errorcodefixe-20) | Overtemperature — check airflow |
| [4-2](https://www.amazon.com/s?k=4-2&tag=errorcodefixe-20) | Secondary limit fault | Overtemperature — check secondary limit | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 5-1 | Gas valve fault | [Check valve and wiring](https://www.amazon.com/s?k=Check%20valve%20and%20wiring&tag=errorcodefixe-20) |  | 6-1 | [Inducer fault](https://www.amazon.com/s?k=Inducer%20fault&tag=errorcodefixe-20) | Check inducer motor and flue |

## York Predator/YSC Alphanumeric Codes

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Description | Action | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| E1 | [Control board communication fault](https://www.amazon.com/s?k=Control%20board%20communication%20fault&tag=errorcodefixe-20) | Check wiring, replace board |
| [E2](https://www.amazon.com/s?k=E2&tag=errorcodefixe-20) | Supply air sensor open/shorted | Check sensor resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E3 | Return air sensor fault | [Check or replace sensor](https://www.amazon.com/s?k=Check%20or%20replace%20sensor&tag=errorcodefixe-20) |  | E4 | [Outdoor sensor fault](https://www.amazon.com/s?k=Outdoor%20sensor%20fault&tag=errorcodefixe-20) | Check or replace outdoor sensor |
| [E6](https://www.amazon.com/s?k=E6&tag=errorcodefixe-20) | High-pressure lockout — compressor 1 | Check condenser, coil, charge | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E7 | High-pressure lockout — compressor 2 | [Check condenser, coil, charge](https://www.amazon.com/s?k=Check%20condenser%2C%20coil%2C%20charge&tag=errorcodefixe-20) |  | E8 | [Low-pressure lockout](https://www.amazon.com/s?k=Low-pressure%20lockout&tag=errorcodefixe-20) | Check refrigerant charge |
| [P1](https://www.amazon.com/s?k=P1&tag=errorcodefixe-20) | Low-ambient compressor lockout | Ambient below min — check lockout settings | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | P2 | Low-ambient heating lockout | [Ambient below heating minimum](https://www.amazon.com/s?k=Ambient%20below%20heating%20minimum&tag=errorcodefixe-20) | ## Most Common York RTU Faults

### Flash 4 — Open Limit Switch
Dirty filter is the number-one cause. Check:
1. Filter condition — replace if dirty
2. All supply registers — confirm open
3. Blower operation — check run capacitor
4. Limit switch continuity — open at room temp = failed switch

### Flash 6 — Ignition Lockout
- Check gas pressure: 3.5 in. w.c. natural gas, 10 in. w.c. propane
- Inspect hot surface igniter for cracks — replace if cracked
- Clean flame sensor rod with fine steel wool

### E6/E7 — High Pressure Lockout
- Wash condenser coil with fin coil cleaner
- Confirm all condenser fans rotate (check capacitors)
- Measure refrigerant subcooling: target 10–15°F for R-410A

### Flash 2 — Low-Pressure Lockout
- Check refrigerant charge with gauges
- Inspect evaporator coil for ice — check airflow
- Check TXV or metering device operation

## Parts Commonly Replaced | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |---|---|
| Hot surface igniter | [Silicon carbide — handle with gloves](https://www.amazon.com/s?k=Silicon%20carbide%20%E2%80%94%20handle%20with%20gloves&tag=errorcodefixe-20) |  | Flame sensor | [Measure µA output; replace below 1.5 µA](https://www.amazon.com/s?k=Measure%20%C2%B5A%20output%3B%20replace%20below%201.5%20%C2%B5A&tag=errorcodefixe-20) |  | Limit switch | [Match temperature rating](https://www.amazon.com/s?k=Match%20temperature%20rating&tag=errorcodefixe-20) |  | Run capacitor | [Check µF before condemning motor](https://www.amazon.com/s?k=Check%20%C2%B5F%20before%20condemning%20motor&tag=errorcodefixe-20) |  | Pressure switch | [High or low side — match setting](https://www.amazon.com/s?k=High%20or%20low%20side%20%E2%80%94%20match%20setting&tag=errorcodefixe-20) |  | IFC board | York part number varies by model year |

> **Note:** York, Luxaire, and Coleman commercial RTUs share the same IFC control boards and fault codes. Parts are fully interchangeable across brands.
