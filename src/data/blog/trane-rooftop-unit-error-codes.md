---
title: "Trane Rooftop Unit Error Codes: Common Faults Guide"
description: "Complete guide to Trane RTU fault codes for Precedent, YCD, and YCC series units. Flash codes, alphanumeric faults, and technician fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
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

| Flash Count | Fault | Common Cause |
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

| Fault Code | Description | Action |
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
| Hot surface igniter | Silicon carbide — handle without skin contact |
| Flame sensor rod | Replace if µA reading below 1.5 µA |
| High-pressure switch | 410A = 590 psi, check OEM setting |
| Condenser fan motor | Check run capacitor first |
| IFC control board | Match model number exactly |
| Inducer motor | Check capacitor before replacing motor |

> **Pro tip:** On Trane Precedent units, the IFC stores the last fault. After a power cycle, the board replays the fault code during startup via the diagnostic LED.
