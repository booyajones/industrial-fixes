---
title: "Lennox Rooftop Unit Error Codes: Technician Guide"
description: "Complete Lennox RTU error code guide for LGH, LCH, and Strategos series. Flash codes, alphanumeric faults, and technician fixes for commercial rooftop units."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lennox
  - rooftop-unit
  - commercial-hvac
---

# Lennox Rooftop Unit Error Codes: Complete Technician Guide

Lennox commercial RTUs — including the LGH, LCH, LCA, and Strategos series — communicate faults via LED flash codes on the IFC board and, on iComfort-equipped units, alphanumeric codes on the communicating thermostat. This guide covers all common Lennox RTU fault codes.

## How to Read Lennox RTU Flash Codes

The STATUS LED on the furnace control flashes a two-digit code: the first group of flashes is the tens digit, the second group is the units digit. A 3-3 pattern means code 33.

## Lennox RTU Flash Code Table

| [Flash Code](https://www.amazon.com/s?ascsubtag=ecf-lennox-rooftop-unit-error-codes&k=Flash+Code&tag=errorcodefixes-20) | Fault | Common Cause |
|---|---|---|
| 1-1 | System lockout | Manual reset required |
| 1-2 | Blower fault | Blower motor or wiring issue |
| 1-3 | Pressure switch stuck open | Inducer issue, blocked flue |
| 2-1 | Gas heating lockout | 3 failed ignition attempts |
| 2-2 | Limit switch fault | Overtemperature — check airflow |
| 2-3 | Flame sense fault | Dirty sensor, bad ground |
| 2-4 | Ignition failure | No gas, bad igniter |
| 3-2 | Low-pressure switch open | Low refrigerant, dirty filter |
| 3-3 | High-pressure switch open | Dirty condenser, overcharge |
| 4-1 | Rollout switch open | Heat exchanger issue |
| 4-2 | Inducer motor fault | Failed motor or capacitor |
| 5-1 | Control board fault | Replace IFC board |
| 5-2 | EEPROM fault | Replace control board |

## Lennox iComfort Alphanumeric Codes (LCA/LGH with iComfort)

| [Code](https://www.amazon.com/s?ascsubtag=ecf-lennox-rooftop-unit-error-codes&k=Code&tag=errorcodefixes-20) | Description | Action |
|---|---|---|
| 103 | Pressure switch stuck open | Check inducer, flue, pressure switch |
| 111 | Low-pressure lockout | Check refrigerant charge |
| 114 | High-pressure lockout | Check condenser and charge |
| 125 | Defrost fault | Check defrost sensor and board |
| 204 | Blower fault | Check motor and capacitor |
| 223 | Flame sense fault | Clean/replace flame sensor |
| 225 | Ignition failure | Gas, igniter, sensor |
| 231 | Limit switch open | Airflow restriction |
| 327 | Communication fault | Check wiring between boards |
| 332 | Outdoor sensor fault | Replace sensor |
| 411 | Gas valve fault | Check valve and wiring |
| 412 | Rollout switch open | Heat exchanger check required |
| 432 | Inducer fault | Check inducer motor |
| 434 | Pressure switch fault | Check hoses and switch |

## Most Common Lennox RTU Faults

### 2-2 — Limit Switch Fault
Restricted airflow is the cause in most cases:
1. Replace dirty filter
2. Check all supply and return grilles are open
3. Inspect blower wheel for debris
4. Verify limit switch is not defective (check continuity)

### 3-3 — High Pressure
Wash condenser coil. Confirm condenser fan motors are operating. Check refrigerant subcooling: target 10–15°F for R-410A units.

### 2-4 — Ignition Failure
1. Check gas supply pressure at the manifold
2. Inspect hot surface igniter (replace if cracked or over 5 years old)
3. Clean flame sensor with fine steel wool

### 3-2 — Low-Pressure Lockout
Check refrigerant charge with gauges. Inspect evaporator coil for ice formation. Check TXV operation.

## Lennox RTU Parts Reference

| Part | Notes |
|---|---|
| [Hot surface igniter](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-lennox-rooftop-unit-error-codes&tag=errorcodefixes-20) | 18K-ohm type — model-specific |
| [Flame sensor](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-lennox-rooftop-unit-error-codes&tag=errorcodefixes-20) | Check µA output — must exceed 1.5 µA |
| [Run capacitor](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-lennox-rooftop-unit-error-codes&tag=errorcodefixes-20) | Test with capacitor meter before condemning motor |
| [Pressure switch](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-rooftop-unit-error-codes&tag=errorcodefixes-20) | High or low side — match OEM pressure setting |
| [IFC control board](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-lennox-rooftop-unit-error-codes&tag=errorcodefixes-20) | Cross-reference by model and serial |
| [Condenser fan motor](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-lennox-rooftop-unit-error-codes&tag=errorcodefixes-20) | Check RPM and HP spec |

> **Pro tip:** Lennox RTU iComfort-equipped units log fault history accessible via the iComfort thermostat menu under Settings > Advanced > Diagnostics. This gives a timestamp of each fault.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)

## See Also

- [Lennox iComfort Error Code 225 — Communication Fault Fix Guide](/posts/lennox-icomfort-error-code-225/)
- [Lennox Error Code 412 — Limit Switch Fault Fix](/posts/lennox-error-code-412/)
- [Lennox Error Code 434 — Outdoor Unit Communication Fault](/posts/lennox-error-code-434/)
- [Lennox Error Code 411 — Ignition Proving Fault Fix](/posts/lennox-error-code-411/)
