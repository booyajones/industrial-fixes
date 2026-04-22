---
title: "LG Multi V VRF System Error Codes: Complete Guide"
description: "LG Multi V VRF system error codes and fault diagnostics. CH-series codes for outdoor and indoor units, causes, and technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lg
  - vrf
  - commercial-hvac
---

# LG Multi V VRF System Error Codes

LG Multi V VRF systems display fault codes as CH (Check) codes on the remote controller or LGAP controller. CH codes are two-digit numbers. Codes can be read on the outdoor unit LED (flashes) or via LG HVAC Solution (cloud diagnostic tool).

## Multi V Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CH01 | Indoor unit sensor fault | [Intake or pipe sensor failure](https://www.amazon.com/s?k=Intake%20or%20pipe%20sensor%20failure&tag=errorcodefixe-20) | Check sensor resistance |
| [CH02](https://www.amazon.com/s?k=CH02&tag=errorcodefixe-20) | Pipe sensor fault (indoor) | Liquid or gas sensor failure | [Check thermistor](https://www.amazon.com/s?k=Check%20thermistor&tag=errorcodefixe-20) |  | CH03 | [Fan motor fault (indoor)](https://www.amazon.com/s?k=Fan%20motor%20fault%20(indoor)&tag=errorcodefixe-20) | Indoor fan motor failure | Check motor and capacitor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CH05 | Communication error | [Indoor-to-outdoor wiring](https://www.amazon.com/s?k=Indoor-to-outdoor%20wiring&tag=errorcodefixe-20) | Check communication wiring |
| [CH10](https://www.amazon.com/s?k=CH10&tag=errorcodefixe-20) | Indoor PCB fault | Control board failure | [Replace indoor PCB](https://www.amazon.com/s?k=Replace%20indoor%20PCB&tag=errorcodefixe-20) |  | CH21 | [Inverter over-current](https://www.amazon.com/s?k=Inverter%20over-current&tag=errorcodefixe-20) | Compressor or inverter board | Check compressor winding | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CH22 | Inverter fault | [Inverter PCB failure](https://www.amazon.com/s?k=Inverter%20PCB%20failure&tag=errorcodefixe-20) | Check DC bus, replace inverter |
| [CH26](https://www.amazon.com/s?k=CH26&tag=errorcodefixe-20) | High discharge temp | Low refrigerant, blocked EEV | [Check charge and EEV](https://www.amazon.com/s?k=Check%20charge%20and%20EEV&tag=errorcodefixe-20) |  | CH27 | [High pressure](https://www.amazon.com/s?k=High%20pressure&tag=errorcodefixe-20) | Dirty outdoor coil, overcharge | Wash coil, check charge | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CH29 | Low pressure | [Low refrigerant, EEV fault](https://www.amazon.com/s?k=Low%20refrigerant%2C%20EEV%20fault&tag=errorcodefixe-20) | Check charge and EEV |
| [CH34](https://www.amazon.com/s?k=CH34&tag=errorcodefixe-20) | Outdoor PCB fault | Outdoor control board failure | [Replace outdoor PCB](https://www.amazon.com/s?k=Replace%20outdoor%20PCB&tag=errorcodefixe-20) |  | CH38 | [EEV fault](https://www.amazon.com/s?k=EEV%20fault&tag=errorcodefixe-20) | Electronic expansion valve | Check EEV operation | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CH45 | Compressor overload | [Compressor protection trip](https://www.amazon.com/s?k=Compressor%20protection%20trip&tag=errorcodefixe-20) | Check amps, check voltage |
| [CH67](https://www.amazon.com/s?k=CH67&tag=errorcodefixe-20) | Outdoor fan motor fault | Fan motor or PCB driver failure | [Check motor amps](https://www.amazon.com/s?k=Check%20motor%20amps&tag=errorcodefixe-20) | ## Most Common Multi V Faults

### CH05 — Communication Error
LG Multi V uses a 2-wire communication bus between indoor and outdoor units. Check for miswired connectors, damaged cable, or address conflicts. On multi-outdoor configurations, check inter-unit communication as well.

### CH26 — High Discharge Temperature
Discharge temperature above 250°F (121°C) triggers CH26. Check refrigerant charge using LG's DX charging chart. Also check EEV operation — a stuck-closed EEV causes high discharge with low suction pressure.

### CH27 — High Pressure
On Multi V units, HP switch is set at 590 psi (R-410A). Dirty outdoor coil, restricted airflow, or overcharge are typical causes. Verify all outdoor unit fans are operating.

### CH21 — Inverter Overcurrent
Check compressor winding resistance with ohmmeter (all phases should be equal, typically 0.5–2 Ω). Measure DC bus voltage at inverter. Check inverter board LED status for secondary fault indication.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Outdoor PCB | [Match Multi V model exactly](https://www.amazon.com/s?k=Match%20Multi%20V%20model%20exactly&tag=errorcodefixe-20) |  | Indoor PCB | [Match indoor unit model](https://www.amazon.com/s?k=Match%20indoor%20unit%20model&tag=errorcodefixe-20) |  | EEV (electronic expansion valve) | [Match valve size and refrigerant](https://www.amazon.com/s?k=Match%20valve%20size%20and%20refrigerant&tag=errorcodefixe-20) |  | Outdoor fan motor | [DC motor type on most Multi V](https://www.amazon.com/s?k=DC%20motor%20type%20on%20most%20Multi%20V&tag=errorcodefixe-20) |  | Communication cable | 2-wire shielded — check polarity |

> **Pro tip:** LG Multi V systems can be diagnosed remotely via LG HVAC Solution. Register the system with the ACS (Advanced Central System) for real-time monitoring and fault code alerts without site visits.
