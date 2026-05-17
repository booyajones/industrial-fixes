---
title: "Goodman GPH Series Packaged Unit Error Codes: Complete Guide"
description: "Goodman GPH packaged heat pump error codes and fault diagnostics. Flash codes, fault descriptions, and technician-level troubleshooting steps."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - packaged-unit
  - heat-pump
---

# Goodman GPH Series Packaged Unit Error Codes

Goodman GPH packaged heat pump units communicate faults via an LED on the control board. Count LED flashes between 3-second pauses. The board stores the last 5 fault codes — press the diagnostic button once to scroll through stored faults.

## GPH Flash Code Table

| Flashes | Fault Description | Common Cause | Action |
|---------|------------------|--------------|--------|
| 1 | Normal operation | No fault | N/A |
| 2 | Low-pressure lockout | Low refrigerant, frozen coil | Check charge, defrost coil |
| 3 | High-pressure lockout | Dirty coil, failed condenser fan | Wash coil, check fan |
| 4 | Open high-pressure switch | Refrigerant overcharge | Check subcooling |
| 5 | Open low-pressure switch | Low charge or refrigerant leak | Find leak, check TXV |
| 6 | Compressor overload | High amperage, failed capacitor | Check cap, contactor, voltage |
| 7 | Defrost lockout | Defrost board failure or sensor fault | Check defrost sensor |
| 8 | Reversing valve fault | Stuck reversing valve | Check 24 VAC to RV solenoid |
| 9 | Control board fault | Internal board failure | Replace control board |

## Most Common GPH Faults

### 2 Flashes — Low-Pressure Lockout
Common in cold weather when outdoor coil ices over. Check airflow across the outdoor coil. Low refrigerant charge also triggers this — measure superheat and compare to charging chart.

### 3 Flashes — High-Pressure Lockout
Dirty condenser coil is the most frequent cause. On packaged heat pumps, the coil is exposed year-round. Wash thoroughly with coil cleaner and verify condenser fan is running.

### 7 Flashes — Defrost Lockout
If the unit fails to defrost, ice accumulates on the outdoor coil, eventually tripping the low-pressure switch. Check defrost sensor clip placement (must contact refrigerant tubing) and defrost termination thermostat continuity.

### 8 Flashes — Reversing Valve Fault
Check for 24 VAC at the reversing valve solenoid in heating mode. A stuck valve may be freed by cycling power. If the valve body is iced or temperature differential is absent, replace the valve.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Defrost control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-goodman-gph-error-codes&tag=errorcodefixes-20) \| Match to unit model number |
| Defrost sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-goodman-gph-error-codes&tag=errorcodefixes-20) \| Clip-on type — confirm placement on tube |
| Reversing valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-gph-error-codes&k=Reversing+valve&tag=errorcodefixes-20) \| Match refrigerant and tonnage |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-goodman-gph-error-codes&tag=errorcodefixes-20) \| Dual-capacitor — check both sections |
| Contactor | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-goodman-gph-error-codes&tag=errorcodefixes-20) \| Check for pitted contacts |
| Low-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-goodman-gph-error-codes&tag=errorcodefixes-20) \| Match pressure setpoint |
> **Pro tip:** Goodman GPH packaged units have the reversing valve energized in cooling mode. If you're testing in heating mode and the valve is de-energized, confirm the solenoid is not stuck energized from a previous short.

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix](/posts/goodman-3-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)
