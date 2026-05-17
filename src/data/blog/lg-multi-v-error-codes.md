---
title: "LG Multi V VRF System Error Codes: Complete Guide"
description: "LG Multi V VRF system error codes and fault diagnostics. CH-series codes for outdoor and indoor units, causes, and technician fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
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

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| CH01 | Indoor unit sensor fault | Intake or pipe sensor failure | Check sensor resistance |
| CH02 | Pipe sensor fault (indoor) | Liquid or gas sensor failure | Check thermistor |
| CH03 | Fan motor fault (indoor) | Indoor fan motor failure | Check motor and capacitor |
| CH05 | Communication error | Indoor-to-outdoor wiring | Check communication wiring |
| CH10 | Indoor PCB fault | Control board failure | Replace indoor PCB |
| CH21 | Inverter over-current | Compressor or inverter board | Check compressor winding |
| CH22 | Inverter fault | Inverter PCB failure | Check DC bus, replace inverter |
| CH26 | High discharge temp | Low refrigerant, blocked EEV | Check charge and EEV |
| CH27 | High pressure | Dirty outdoor coil, overcharge | Wash coil, check charge |
| CH29 | Low pressure | Low refrigerant, EEV fault | Check charge and EEV |
| CH34 | Outdoor PCB fault | Outdoor control board failure | Replace outdoor PCB |
| CH38 | EEV fault | Electronic expansion valve | Check EEV operation |
| CH45 | Compressor overload | Compressor protection trip | Check amps, check voltage |
| CH67 | Outdoor fan motor fault | Fan motor or PCB driver failure | Check motor amps |

## Most Common Multi V Faults

### CH05 — Communication Error
LG Multi V uses a 2-wire communication bus between indoor and outdoor units. Check for miswired connectors, damaged cable, or address conflicts. On multi-outdoor configurations, check inter-unit communication as well.

### CH26 — High Discharge Temperature
Discharge temperature above 250°F (121°C) triggers CH26. Check refrigerant charge using LG's DX charging chart. Also check EEV operation — a stuck-closed EEV causes high discharge with low suction pressure.

### CH27 — High Pressure
On Multi V units, HP switch is set at 590 psi (R-410A). Dirty outdoor coil, restricted airflow, or overcharge are typical causes. Verify all outdoor unit fans are operating.

### CH21 — Inverter Overcurrent
Check compressor winding resistance with ohmmeter (all phases should be equal, typically 0.5–2 ╬⌐). Measure DC bus voltage at inverter. Check inverter board LED status for secondary fault indication.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Match Multi V model exactly |
| Indoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Match indoor unit model |
| EEV (electronic expansion valve) | [Amazon](https://www.amazon.com/s?i=industrial&k=EEV+%28electronic+expansion+valve%29&tag=errorcodefixes-20) \| Match valve size and refrigerant |
| Outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| DC motor type on most Multi V |
| Communication cable | [Amazon](https://www.amazon.com/s?i=industrial&k=Communication+cable&tag=errorcodefixes-20) \| 2-wire shielded — check polarity |
> **Pro tip:** LG Multi V systems can be diagnosed remotely via LG HVAC Solution. Register the system with the ACS (Advanced Central System) for real-time monitoring and fault code alerts without site visits.
