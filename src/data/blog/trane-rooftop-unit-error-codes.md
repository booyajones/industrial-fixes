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

| [Flash Count](https://www.amazon.com/s?k=Flash%20Count&tag=errorcodefixe-20) | Fault | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| 1 | [Normal — no fault](https://www.amazon.com/s?k=Normal%20%E2%80%94%20no%20fault&tag=errorcodefixe-20) | System operating correctly |
| [2](https://www.amazon.com/s?k=2&tag=errorcodefixe-20) | Inducer/pressure switch fault | Blocked flue, failed inducer motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 3 | Pressure switch stuck closed | [Faulty pressure switch or control board](https://www.amazon.com/s?k=Faulty%20pressure%20switch%20or%20control%20board&tag=errorcodefixe-20) |  | 4 | [Open high-temperature limit](https://www.amazon.com/s?k=Open%20high-temperature%20limit&tag=errorcodefixe-20) | Restricted airflow, failed blower motor |
| [5](https://www.amazon.com/s?k=5&tag=errorcodefixe-20) | Flame sense fault | Dirty flame sensor, sensor position off | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 6 | Ignition failure | [Gas pressure low, spark igniter weak](https://www.amazon.com/s?k=Gas%20pressure%20low%2C%20spark%20igniter%20weak&tag=errorcodefixe-20) |  | 7 | [Gas valve fault](https://www.amazon.com/s?k=Gas%20valve%20fault&tag=errorcodefixe-20) | Failed gas valve, wiring |
| [8](https://www.amazon.com/s?k=8&tag=errorcodefixe-20) | Low flame signal | Weak flame, contaminated sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 9 | Rollout switch open | [Cracked heat exchanger, blocked burner](https://www.amazon.com/s?k=Cracked%20heat%20exchanger%2C%20blocked%20burner&tag=errorcodefixe-20) | ## Trane ComfortLink / Tracer Alphanumeric Codes | Fault Code | [Description](https://www.amazon.com/s?k=Description&tag=errorcodefixe-20) | Action |
|---|---|---| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 77 | High-pressure cutout | [Check condenser coil, fan motors, charge](https://www.amazon.com/s?k=Check%20condenser%20coil%2C%20fan%20motors%2C%20charge&tag=errorcodefixe-20) |  | 79 | [Low-pressure cutout](https://www.amazon.com/s?k=Low-pressure%20cutout&tag=errorcodefixe-20) | Check refrigerant charge, filter, evap coil |
| [80](https://www.amazon.com/s?k=80&tag=errorcodefixe-20) | Loss of charge | Refrigerant leak — perform leak check | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 81 | Compressor protection | [Check compressor amps, capacitor](https://www.amazon.com/s?k=Check%20compressor%20amps%2C%20capacitor&tag=errorcodefixe-20) |  | 91 | [Communication fault](https://www.amazon.com/s?k=Communication%20fault&tag=errorcodefixe-20) | Check wiring between control boards |
| [92](https://www.amazon.com/s?k=92&tag=errorcodefixe-20) | Zone sensor fault | Check sensor wiring and resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 93 | Outdoor air sensor fault | [Check or replace outdoor sensor](https://www.amazon.com/s?k=Check%20or%20replace%20outdoor%20sensor&tag=errorcodefixe-20) |  | 94 | [Supply air sensor fault](https://www.amazon.com/s?k=Supply%20air%20sensor%20fault&tag=errorcodefixe-20) | Check or replace supply sensor |
| [126](https://www.amazon.com/s?k=126&tag=errorcodefixe-20) | Economizer fault | Check damper actuator and linkage | [## Most Common Trane RTU Faults

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

## Trane RTU Parts Reference](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Trane%20RTU%20Faults%0A%0A%23%23%23%204%20Flashes%20%E2%80%94%20Open%20Limit%20Switch%0ACheck%20airflow%20first%3A%20filter%2C%20blower%20motor%20operation%2C%20all%20registers%20open.%20Check%20limit%20switch%20continuity%20%E2%80%94%20an%20open%20limit%20at%20room%20temperature%20means%20the%20switch%20has%20failed.%0A%0A%23%23%23%20Fault%2077%20%E2%80%94%20High%20Pressure%20Cutout%0AMost%20common%20during%20summer.%20Wash%20the%20condenser%20coil%20with%20coil%20cleaner%2C%20verify%20all%20condenser%20fans%20are%20running%2C%20confirm%20capacitor%20%C2%B5F.%20Check%20refrigerant%20charge%3A%20target%20superheat%208%E2%80%9312%C2%B0F%2C%20subcooling%2010%E2%80%9315%C2%B0F.%0A%0A%23%23%23%206%20Flashes%20%E2%80%94%20Ignition%20Failure%0A1.%20Verify%20gas%20supply%20pressure%3A%203.5%20in.%20w.c.%20natural%20gas%2C%2010%20in.%20w.c.%20LP%0A2.%20Inspect%20hot%20surface%20igniter%20%E2%80%94%20cracks%20or%20discoloration%20mean%20replace%0A3.%20Clean%20flame%20sensor%20rod%20with%20fine%20steel%20wool%20(never%20sandpaper)%0A%0A%23%23%23%20Fault%2079%20%E2%80%94%20Low%20Pressure%20Cutout%0AIn%20cooling%20mode%3A%20refrigerant%20low.%20In%20heat%20pump%20heating%20mode%3A%20check%20for%20defrost%20operation.%0A%0A%23%23%23%202%20Flashes%20%E2%80%94%20Inducer%2FPressure%20Switch%20Fault%0AVerify%20inducer%20motor%20is%20running.%20Check%20pressure%20switch%20hose%20for%20blockages.%20Measure%20pressure%20switch%20trip%20point%20with%20a%20manometer.%0A%0A%23%23%20Trane%20RTU%20Parts%20Reference&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hot surface igniter | Silicon carbide — handle without skin contact | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Flame sensor rod | Replace if µA reading below 1.5 µA | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | High-pressure switch | 410A = 590 psi, check OEM setting | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condenser fan motor | Check run capacitor first | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | IFC control board | Match model number exactly | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Inducer motor | Check capacitor before replacing motor |

> **Pro tip:** On Trane Precedent units, the IFC stores the last fault. After a power cycle, the board replays the fault code during startup via the diagnostic LED.
