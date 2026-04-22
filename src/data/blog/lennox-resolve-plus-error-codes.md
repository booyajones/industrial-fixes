---
title: "Lennox ResolvePlus Rooftop Unit Error Codes: Complete Guide"
description: "Lennox ResolvePlus RTU error codes and fault diagnostics. Covers flash codes, communicating system faults, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - rooftop-unit
  - commercial-hvac
---

# Lennox ResolvePlus Rooftop Unit Error Codes

Lennox ResolvePlus packaged rooftop units use a flashing LED diagnostic system on the integrated control board. The control stores up to 5 fault codes in memory. For units with Lennox communicating thermostats (iComfort), fault codes display as numeric codes directly.

## ResolvePlus Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 111 | Pressure switch fault | [Blocked inducer, failed switch](https://www.amazon.com/s?k=Blocked%20inducer%2C%20failed%20switch&tag=errorcodefixe-20) | Measure flue pressure |
| [114](https://www.amazon.com/s?k=114&tag=errorcodefixe-20) | Limit switch open | Dirty filter, blocked return | [Replace filter, check airflow](https://www.amazon.com/s?k=Replace%20filter%2C%20check%20airflow&tag=errorcodefixe-20) |  | 125 | [Ignition failure](https://www.amazon.com/s?k=Ignition%20failure&tag=errorcodefixe-20) | Low gas, weak igniter | Check gas pressure and igniter | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 204 | High-pressure switch open | [Dirty condenser coil](https://www.amazon.com/s?k=Dirty%20condenser%20coil&tag=errorcodefixe-20) | Wash coil, check fan operation |
| [223](https://www.amazon.com/s?k=223&tag=errorcodefixe-20) | Low-pressure switch open | Low refrigerant charge | [Check charge, inspect TXV](https://www.amazon.com/s?k=Check%20charge%2C%20inspect%20TXV&tag=errorcodefixe-20) |  | 225 | [Freeze fault](https://www.amazon.com/s?k=Freeze%20fault&tag=errorcodefixe-20) | Low airflow or refrigerant | Check filter and evaporator coil | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 231 | Discharge temperature high | [Refrigerant issue, condenser fan](https://www.amazon.com/s?k=Refrigerant%20issue%2C%20condenser%20fan&tag=errorcodefixe-20) | Inspect condenser fan motors |
| [327](https://www.amazon.com/s?k=327&tag=errorcodefixe-20) | Communication fault | Wiring issue to communicating thermostat | [Check communication wiring](https://www.amazon.com/s?k=Check%20communication%20wiring&tag=errorcodefixe-20) |  | 332 | [Blower motor fault](https://www.amazon.com/s?k=Blower%20motor%20fault&tag=errorcodefixe-20) | Failed ECM motor or VFD | Check motor for proper operation | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 411 | Flame sensor fault | [Dirty or failed flame sensor](https://www.amazon.com/s?k=Dirty%20or%20failed%20flame%20sensor&tag=errorcodefixe-20) | Clean sensor, measure µA |
| [412](https://www.amazon.com/s?k=412&tag=errorcodefixe-20) | Inducer motor fault | Failed inducer motor | [Check inducer amp draw](https://www.amazon.com/s?k=Check%20inducer%20amp%20draw&tag=errorcodefixe-20) |  | 432 | [Gas valve fault](https://www.amazon.com/s?k=Gas%20valve%20fault&tag=errorcodefixe-20) | Failed gas valve | Check 24 VAC at valve | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 540 | Loss of communication | [Communication board or wiring](https://www.amazon.com/s?k=Communication%20board%20or%20wiring&tag=errorcodefixe-20) | Inspect communication connections |

## Most Common ResolvePlus Faults

### Code 114 — Limit Switch Open
Check the air filter first. ResolvePlus units are sensitive to static pressure — a dirty filter or blocked return can trip the limit at low ambient temperatures. Verify blower motor speed matches installed ESP.

### Code 125 — Ignition Failure
Check inducer operation before gas pressure. If the inducer doesn't prove, the gas valve won't open. Verify inducer pressure switch closes (typically -0.30 to -0.45 in. w.c.).

### Code 204 — High-Pressure Switch
On R-410A units, high-side pressure above 590 psi trips the HP switch. Wash the condenser coil, verify condenser fan rotation and amp draw.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| [Integrated control board](https://www.amazon.com/s?k=Integrated%20control%20board&tag=errorcodefixe-20) | Must match unit model |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Measure µA before replacing |
| [Inducer motor](https://www.amazon.com/s?k=Inducer%20motor&tag=errorcodefixe-20) | Check capacitor first |
| [Limit switch](https://www.amazon.com/s?k=Limit%20switch&tag=errorcodefixe-20) | Match temperature rating |
| [ECM blower motor](https://www.amazon.com/s?k=ECM%20blower%20motor&tag=errorcodefixe-20) | Check motor module and control board |

> **Pro tip:** Lennox ResolvePlus fault history is accessible via the field diagnostic tool or iComfort interface. Always retrieve fault history before clearing codes to identify intermittent problems.
