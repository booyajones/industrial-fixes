---
title: "Trane Rooftop Unit Error Codes: Common Faults Guide"
description: "Complete guide to Trane RTU fault codes for Precedent, YCD, and YCC series units. Flash codes, alphanumeric faults, and technician fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
  - rooftop-unit
  - commercial-hvac
---

# Trane Rooftop Unit Error Codes: Complete Technician Guide

Trane commercial RTUs — including the Precedent, YCD, YCC, and CGAM series — report faults via LED flash codes on the IFC board and alphanumeric codes on the zone sensor or ComfortLink communicating thermostat. This guide covers all common Trane RTU fault codes.

## How to Read Trane RTU Codes

**LED Flash Method:** Count rapid flashes, wait for the pause, count again. The number equals the fault code.

**Display Method (Tracer ZN / ComfortLink II):** Alphanumeric fault codes appear directly on the zone sensor or thermostat display. Access the diagnostic menu by pressing Menu > Diagnostics.

## Trane RTU Flash Code Table

| [Flash Count](https://www.amazon.com/s?k=Flash+Count&tag=errorcodefixes-20) | Fault | Common Cause |
|---|---|---|
| 1 | Normal — no fault | System operating correctly |
| 2 | Inducer/pressure switch fault | Blocked flue, failed inducer motor |
| 3 | Pressure switch stuck closed | Faulty pressure switch or control board |
| 4 | Open high-temperature limit | Restricted airflow, failed blower motor |
| 5 | Flame sense fault | Dirty flame sensor, sensor position off |
| 6 | Ignition failure | Gas pressure low, spark igniter weak |
| 7 | Gas valve fault | Failed gas valve, wiring |
| 8 | Low flame signal | Weak flame, contaminated sensor |
| 9 | Rollout switch open | Cracked heat exchanger, blocked burner |

## Trane ComfortLink / Tracer Alphanumeric Codes

| [Fault Code](https://www.amazon.com/s?k=Fault+Code&tag=errorcodefixes-20) | Description | Action |
|---|---|---|
| 77 | High-pressure cutout | Check condenser coil, fan motors, charge |
| 79 | Low-pressure cutout | Check refrigerant charge, filter, evap coil |
| 80 | Loss of charge | Refrigerant leak — perform leak check |
| 81 | Compressor protection | Check compressor amps, capacitor |
| 91 | Communication fault | Check wiring between control boards |
| 92 | Zone sensor fault | Check sensor wiring and resistance |
| 93 | Outdoor air sensor fault | Check or replace outdoor sensor |
| 94 | Supply air sensor fault | Check or replace supply sensor |
| 126 | Economizer fault | Check damper actuator and linkage |

## Most Common Trane RTU Faults

### 4 Flashes — Open Limit Switch
Check airflow first: filter, blower motor operation, all registers open. Check limit switch continuity — an open limit at room temperature means the switch has failed.

### Fault 77 — High Pressure Cutout
Most common during summer. Wash the condenser coil with coil cleaner, verify all condenser fans are running, confirm capacitor µF. Check refrigerant charge: target superheat 8–12°F, subcooling 10–15°F.

### 6 Flashes — Ignition Failure
1. Verify gas supply pressure: 3.5 in. w.c. natural gas, 10 in. w.c. LP
2. Inspect hot surface igniter — cracks or discoloration mean replace
3. Clean flame sensor rod with fine steel wool (never sandpaper)

### Fault 79 — Low Pressure Cutout
In cooling mode: refrigerant low. In heat pump heating mode: check for defrost operation.

### 2 Flashes — Inducer/Pressure Switch Fault
Verify inducer motor is running. Check pressure switch hose for blockages. Measure pressure switch trip point with a manometer.

## Trane RTU Parts Reference

| Part | Notes |
|---|---|
| [Hot surface igniter](https://www.amazon.com/dp/B00BTLLJ40?tag=errorcodefixes-20) | Silicon carbide — handle without skin contact |
| [Flame sensor rod](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) | Replace if µA reading below 1.5 µA |
| [High-pressure switch](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) | 410A = 590 psi, check OEM setting |
| [Condenser fan motor](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | Check run capacitor first |
| [IFC control board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Match model number exactly |
| [Inducer motor](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) | Check capacitor before replacing motor |

> **Pro tip:** On Trane Precedent units, the IFC stores the last fault. After a power cycle, the board replays the fault code during startup via the diagnostic LED.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
