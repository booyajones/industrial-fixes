---
title: "York Rooftop Unit Error Codes: Technician Guide"
description: "Complete York RTU error code guide for Predator, Affinity, and ZF series. Flash codes, alphanumeric faults, and field fixes for commercial rooftop units."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
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

| Flash Code | Fault | Common Cause |
|---|---|---|
| 2 | Low-pressure lockout | Low refrigerant charge |
| 3 | High-pressure lockout | Dirty condenser coil, fan failure |
| 4 | Limit switch open | Airflow restriction, dirty filter |
| 5 | Rollout switch open | Cracked heat exchanger, blocked burner |
| 6 | Ignition lockout | No ignition after 3 attempts |
| 7 | Flame signal lost | Dirty or failed flame sensor |
| 8 | Blower motor fault | Motor or capacitor failed |
| 2-2 | Low-pressure switch stuck closed | Replace pressure switch |
| 3-3 | High-pressure switch stuck closed | Replace pressure switch |
| 4-1 | Primary limit fault | Overtemperature — check airflow |
| 4-2 | Secondary limit fault | Overtemperature — check secondary limit |
| 5-1 | Gas valve fault | Check valve and wiring |
| 6-1 | Inducer fault | Check inducer motor and flue |

## York Predator/YSC Alphanumeric Codes

| Code | Description | Action |
|---|---|---|
| E1 | Control board communication fault | Check wiring, replace board |
| E2 | Supply air sensor open/shorted | Check sensor resistance |
| E3 | Return air sensor fault | Check or replace sensor |
| E4 | Outdoor sensor fault | Check or replace outdoor sensor |
| E6 | High-pressure lockout — compressor 1 | Check condenser, coil, charge |
| E7 | High-pressure lockout — compressor 2 | Check condenser, coil, charge |
| E8 | Low-pressure lockout | Check refrigerant charge |
| P1 | Low-ambient compressor lockout | Ambient below min — check lockout settings |
| P2 | Low-ambient heating lockout | Ambient below heating minimum |

## Most Common York RTU Faults

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

## Parts Commonly Replaced

| Part | Notes |
|---|---|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) \| Silicon carbide — handle with gloves |
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) \| Measure µA output; replace below 1.5 µA |
| Limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Match temperature rating |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) \| Check µF before condemning motor |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| High or low side — match setting |
| IFC board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| York part number varies by model year |
> **Note:** York, Luxaire, and Coleman commercial RTUs share the same IFC control boards and fault codes. Parts are fully interchangeable across brands.

## Related Articles

- [York 2 Flashes Error Code — Causes & Fix](/posts/york-2-flashes-error-code/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
- [York 4 Flashes Error Code — Open Limit Device Fix](/posts/york-4-flashes-error-code/)
- [York 5 Flashes Error Code — Causes & Fix](/posts/york-5-flashes-error-code/)
- [York Furnace 6 Flashes Error Code — Pressure Switch Fault Fix](/posts/york-6-flashes-pressure-switch-fault/)
