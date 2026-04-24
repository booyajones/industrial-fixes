---
title: "Trane Precedent Rooftop Unit Error Codes: Complete Guide"
description: "Trane Precedent RTU error codes and fault diagnostics for commercial technicians. Flash codes, sensor faults, and step-by-step fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
  - rooftop-unit
  - commercial-hvac
---

# Trane Precedent Rooftop Unit Error Codes

Trane Precedent RTUs (3ΓÇô10 ton) use an LED on the unit control module (UCM) to flash fault codes. Count flashes between 3-second pauses. Units with the Integrated Comfort System display codes on a thermostat or controller.

## Precedent Flash Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 2 | Supply air sensor fault | Failed SAT sensor or wiring | Check thermistor resistance |
| 3 | Outdoor air sensor fault | Failed OAT sensor | Replace sensor |
| 4 | Return air sensor fault | Failed RAT sensor | Check wiring to sensor |
| 5 | Compressor trip | Compressor protection open | Check HP/LP switches, contactor |
| 6 | Low charge/low pressure | Low refrigerant or TXV failure | Check subcooling, superheat |
| 7 | High discharge temp | Refrigerant short, failed condenser fan | Check condenser fan, refrigerant charge |
| 8 | Heating lockout | Gas heating fault | Check igniter, gas valve, flame sensor |
| 9 | Economizer fault | Failed actuator or sensor | Check economizer actuator and damper |
| 10 | Supply fan fault | Failed blower motor or VFD | Check motor amps, run capacitor |
| 12 | Ignition failure | No gas, weak spark | Check gas pressure and igniter |
| 13 | Limit switch lockout | Persistent overtemperature | Clear airflow restriction before reset |
| 14 | Flame rollout trip | Cracked heat exchanger or blocked flue | Inspect heat exchanger |

## Most Common Precedent Faults

### Code 5 ΓÇö Compressor Trip
Check HP switch setting (R-410A = 590 psi, R-22 = 380 psi) and LP switch. Verify refrigerant charge with superheat and subcooling measurements before adding refrigerant.

### Code 8 ΓÇö Heating Lockout
Work through ignition sequence: verify 24 VAC to igniter, check spark gap (1/8"), clean flame sensor, and confirm gas pressure at manifold (3.5 in. w.c. natural gas).

### Code 13 ΓÇö Limit Switch Lockout
Three consecutive limit trips lock out the unit. The cause is almost always restricted airflow. Replace the filter, verify all dampers are open, and check blower motor speed.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| UCM control board | [Amazon](https://www.amazon.com/s?k=UCM+control+board&tag=errorcodefixes-20) \| Match to unit model and refrigerant type |
| SAT/OAT/RAT sensors | [Amazon](https://www.amazon.com/s?k=SAT%2FOAT%2FRAT+sensors&tag=errorcodefixes-20) \| Thermistor type ΓÇö check resistance vs. temp chart |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Clean with emery cloth before condemning |
| Run capacitor | [Amazon](https://www.amazon.com/s?k=Run+capacitor&tag=errorcodefixes-20) \| Check ┬╡F value with capacitor meter |
| Limit switch | [Amazon](https://www.amazon.com/s?k=Limit+switch&tag=errorcodefixes-20) \| Match opening temperature rating |
> **Pro tip:** Trane Precedent units require the correct UCM firmware for the refrigerant type (R-22 vs. R-410A). Swapping boards without matching firmware causes erratic fault codes.
