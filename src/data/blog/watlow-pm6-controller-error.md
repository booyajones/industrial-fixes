---
title: "Watlow PM6 Temperature Controller Error Codes: Complete Guide"
description: "Watlow PM6 temperature controller error codes and fault messages. Error causes and technician-level troubleshooting for industrial thermal systems."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - instruments
  - watlow
  - process-control
  - temperature-control
---

# Watlow PM6 Temperature Controller Error Codes

The Watlow PM6 is a 1/16 DIN PID temperature controller with dual display (process value and set point). It supports thermocouple, RTD, and process voltage/current inputs. Error messages appear on the upper (process) display.

## PM6 Error Code Table

| Display | Meaning | Cause | Action |
|---------|---------|-------|--------|
| OPEN | Open sensor | Open thermocouple or RTD | Check sensor continuity |
| SHRT | Shorted sensor | Shorted thermocouple or RTD | Check sensor insulation |
| OvEr | Over-range input | Temperature above sensor max | Check sensor type and range |
| Undr | Under-range input | Temperature below sensor min | Check input type and polarity |
| Err | General error | Hardware or input fault | Check input signal |
| InEr | Input error | Signal out of specification | Verify input type matches sensor |
| tUnE | Auto-tune in progress | PID auto-tune active | Wait for completion |
| ALo | Low alarm | Process below low alarm setpoint | Check process condition |
| AHi | High alarm | Process above high alarm setpoint | Check process condition |

## Most Common PM6 Faults

### OPEN — Open Sensor
Check the thermocouple or RTD connection at both the PM6 terminals and the sensor head. On thermocouple circuits, open connections may be at extension wire joints. Measure sensor resistance: TC should be < 100 ╬⌐, Pt100 RTD should be 100 ╬⌐ at 0°C, 138.5 ╬⌐ at 100°C.

### SHRT — Shorted Sensor
A short circuit in the thermocouple or RTD wiring. Common causes: pinched extension wire in machinery, damaged insulation from heat, or a shorted sensor element. Disconnect sensor at PM6 terminals and check resistance from each lead to ground.

### OvEr/Undr — Range Errors
If the process temperature is within expected range but the display shows OvEr or Undr, the input type is misconfigured. Verify input type (Inp parameter in menu) matches the connected sensor. A Type K sensor configured as Type J will read incorrectly.

### Auto-Tune (tUnE)
PM6 auto-tune uses relay output switching to identify process dynamics. During auto-tune, the output cycles on/off — this is normal. Auto-tune requires the process to be near operating temperature. If auto-tune fails, the PM6 reverts to previous PID values.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Thermocouple (Type K/J/T) | [Amazon](https://www.amazon.com/dp/B00RJF4PYQ?ascsubtag=ecf-watlow-pm6-controller-error&tag=errorcodefixes-20) \| Match existing sensor type |
| RTD sensor (Pt100) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-watlow-pm6-controller-error&k=RTD+sensor+%28Pt100%29&tag=errorcodefixes-20) \| For RTD input PM6 versions |
| Solid-state relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-watlow-pm6-controller-error&k=Solid-state+relay&tag=errorcodefixes-20) \| Match output type (SSR for current output) |
| Mechanical relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-watlow-pm6-controller-error&k=Mechanical+relay&tag=errorcodefixes-20) \| For relay output versions |
| Replacement PM6 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-watlow-pm6-controller-error&k=Replacement+PM6&tag=errorcodefixes-20) \| Document all parameter values before replacing |
> **Pro tip:** Watlow PM6 parameters can be locked with a password to prevent unauthorized changes. If locked, consult the PM6 installation manual for the default unlock code (1234). Document all parameter values before any PM6 replacement — there is no backup-and-restore function.
