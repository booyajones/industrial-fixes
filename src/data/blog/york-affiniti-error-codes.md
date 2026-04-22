---
title: "York Affinity Series Packaged Unit Error Codes: Complete Guide"
description: "York Affinity packaged unit error codes and fault diagnostics. Flash codes, communicating system faults, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - york
  - packaged-unit
  - commercial-hvac
---

# York Affinity Series Packaged Unit Error Codes

York Affinity packaged units use an LED diagnostic system on the Integrated Furnace Control (IFC) board. Flash codes identify faults. Units with the York Affinity Communicating System display codes on a thermostat. Fault history is stored in the control board.

## Affinity Flash Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 2 | Pressure switch stuck closed | Shorted switch or wiring | Check switch and wiring |
| 3 | Pressure switch open | Blocked inducer port, failed switch | Measure inducer flue pressure |
| 4 | Open high-limit | Restricted airflow | Replace filter, check duct |
| 5 | Flame sensed with no call | Leaking gas valve | Replace gas valve |
| 6 | Ignition failure | Gas, spark, or sensor issue | Check gas pressure and igniter |
| 7 | Limit switch lockout | Repeated overtemperature | Resolve airflow restriction |
| 8 | Low-pressure switch | Low refrigerant, iced coil | Check charge and defrost |
| 9 | High-pressure switch | Dirty coil, failed condenser fan | Clean coil, check fans |
| 10 | Defrost fault | Defrost board or sensor | Check sensor clip position |
| 11 | Blower fault | Failed motor or relay | Check motor amps and relays |

## Most Common Affinity Faults

### Code 4 — Open High-Limit
York Affinity units are available in gas heat versions where limit trips are common with dirty filters. The limit opens at 150–200°F depending on model. Replace the filter, verify all supply registers are open, and check blower RPM.

### Code 6 — Ignition Failure
Check in sequence: induced draft motor running, pressure switch proven, gas valve opens (listen/check inlet pressure), spark at igniter (1/8" gap), and flame sensor signal (µA). Clean flame sensor first.

### Code 9 — High Pressure
R-410A high-side must stay below 590 psi. Wash condenser coil, check condenser fan rotation — it must pull air through the coil. Verify unit is not operating in excessive ambient temperature.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| IFC board | Match to unit model |
| Flame sensor | Measure µA first |
| Pressure switch | Match pressure setpoint |
| Limit switch | Match temperature rating |
| Run capacitor | Test µF with meter |
| Blower motor | Check for ECM vs. PSC type |

> **Pro tip:** York Affinity units with the communicating system log fault timestamps. Always retrieve fault history via thermostat diagnostics menu before clearing — provides valuable intermittent fault pattern data.
