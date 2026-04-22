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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 2 | Pressure switch stuck closed | [Shorted switch or wiring](https://www.amazon.com/s?k=Shorted%20switch%20or%20wiring&tag=errorcodefixe-20) | Check switch and wiring |
| [3](https://www.amazon.com/s?k=3&tag=errorcodefixe-20) | Pressure switch open | Blocked inducer port, failed switch | [Measure inducer flue pressure](https://www.amazon.com/s?k=Measure%20inducer%20flue%20pressure&tag=errorcodefixe-20) |  | 4 | [Open high-limit](https://www.amazon.com/s?k=Open%20high-limit&tag=errorcodefixe-20) | Restricted airflow | Replace filter, check duct | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 5 | Flame sensed with no call | [Leaking gas valve](https://www.amazon.com/s?k=Leaking%20gas%20valve&tag=errorcodefixe-20) | Replace gas valve |
| [6](https://www.amazon.com/s?k=6&tag=errorcodefixe-20) | Ignition failure | Gas, spark, or sensor issue | [Check gas pressure and igniter](https://www.amazon.com/s?k=Check%20gas%20pressure%20and%20igniter&tag=errorcodefixe-20) |  | 7 | [Limit switch lockout](https://www.amazon.com/s?k=Limit%20switch%20lockout&tag=errorcodefixe-20) | Repeated overtemperature | Resolve airflow restriction | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 8 | Low-pressure switch | [Low refrigerant, iced coil](https://www.amazon.com/s?k=Low%20refrigerant%2C%20iced%20coil&tag=errorcodefixe-20) | Check charge and defrost |
| [9](https://www.amazon.com/s?k=9&tag=errorcodefixe-20) | High-pressure switch | Dirty coil, failed condenser fan | [Clean coil, check fans](https://www.amazon.com/s?k=Clean%20coil%2C%20check%20fans&tag=errorcodefixe-20) |  | 10 | [Defrost fault](https://www.amazon.com/s?k=Defrost%20fault&tag=errorcodefixe-20) | Defrost board or sensor | Check sensor clip position | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 11 | Blower fault | [Failed motor or relay](https://www.amazon.com/s?k=Failed%20motor%20or%20relay&tag=errorcodefixe-20) | Check motor amps and relays |

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
| [IFC board](https://www.amazon.com/s?k=IFC%20board&tag=errorcodefixe-20) | Match to unit model |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Measure µA first |
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Match pressure setpoint |
| [Limit switch](https://www.amazon.com/s?k=Limit%20switch&tag=errorcodefixe-20) | Match temperature rating |
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | Test µF with meter |
| [Blower motor](https://www.amazon.com/s?k=Blower%20motor&tag=errorcodefixe-20) | Check for ECM vs. PSC type |

> **Pro tip:** York Affinity units with the communicating system log fault timestamps. Always retrieve fault history via thermostat diagnostics menu before clearing — provides valuable intermittent fault pattern data.
