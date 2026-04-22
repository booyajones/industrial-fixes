---
title: "Omega Temperature Controller Error Codes — Guide"
description: "Omega Engineering temperature controller error codes: what each means and how to fix it."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - omega
---

## Omega Temperature Controller Error Codes — What They Mean

Omega Engineering temperature controllers (CN series, iSeries, and Platinum series) are widely used in industrial ovens, furnaces, heat treat equipment, and process applications. They display alphanumeric error codes when sensor or system faults occur.

| Code | Meaning |
|------|---------|
| Err 1 / OPNC | Open circuit — sensor or thermocouple is open |
| Err 2 / SHRT | Short circuit — sensor leads shorted |
| Err 3 / OVER | Over-range — temperature exceeds sensor or controller range |
| Err 4 / UNDR | Under-range — temperature below sensor minimum |
| Err 5 | ADC fault (internal) |
| HiLim | High temperature limit alarm |
| LoLim | Low temperature limit alarm |

[Jump to Fix](#fix)

## Most Common Omega Controller Errors and Fixes {#fix}

### Err 1 / OPNC — Open Circuit
Most common error. Test thermocouple or RTD continuity. Broken thermocouple wire = open circuit. Also check terminal connections at the controller — loose screw terminals cause open-circuit readings.

### Err 2 / SHRT — Short Circuit
Thermocouple leads touching (shorted) or a failed RTD. Check for insulation damage on sensor leads, especially near high-temperature zones.

### OVER / UNDR — Range Error
The actual temperature is outside the sensor or controller's range. Verify the correct sensor type is selected in controller parameters (Type K, J, T, RTD, etc.). A type mismatch between sensor and controller causes OVER or UNDR readings at normal temperatures.

### HiLim / LoLim
Temperature crossed the alarm setpoint. Verify the setpoint is configured correctly for the process. If temperature is genuinely out of range, investigate the heating/cooling system.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermocouple (Type K, J, T, etc.) | Match to controller input type — Type K is most common |
| RTD (PT100) | For RTD-input controllers |
| Terminal connector | Omega 1/4" DIN panel terminals if loose |

## When to Call a Pro

Err 5 (ADC fault) indicates internal controller failure. Omega Engineering technical support can determine if the controller needs factory repair or replacement.
