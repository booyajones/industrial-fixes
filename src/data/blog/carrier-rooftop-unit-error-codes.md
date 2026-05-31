---
title: "Carrier Rooftop Unit Error Codes: Common Faults Guide"
description: "Complete guide to Carrier RTU error codes. Covers flash codes, fault descriptions, and technician-level fixes for 48 and 50 Series commercial rooftop units."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - rooftop-unit
  - commercial-hvac
---

# Carrier Rooftop Unit Error Codes: Complete Technician Guide

Carrier 48/50 Series rooftop units (RTUs) communicate faults via a diagnostic LED on the integrated furnace control (IFC) board. Each flash count maps to a specific fault code. Newer units with 7-segment displays show codes directly. This guide covers all common Carrier RTU fault codes.

## How to Read Carrier RTU Flash Codes

Count rapid LED flashes, wait for the 3-second pause, then count again. The number equals the fault code. Most boards also store the last 5 fault codes — press and hold the diagnostic button for 5 seconds to retrieve fault history.

## Carrier RTU Flash Code Table

| Flash Code | Fault Description | Common Cause |
|---|---|---|
| 2 | Low-pressure lockout | Low refrigerant, dirty filter, blocked coil |
| 3 | High-pressure lockout | Dirty condenser coil, failed condenser fan, overcharge |
| 4 | Open high-pressure switch | Refrigerant overcharge, blocked condenser |
| 11 | Ignition failure | No gas, weak spark, dirty flame sensor |
| 12 | Flame sense fault | Dirty/cracked flame sensor, grounding issue |
| 13 | Limit switch open | Restricted airflow, dirty filter, failed blower |
| 14 | Ignition lockout | 3 failed ignition attempts — requires manual reset |
| 21 | Gas valve fault | Failed gas valve, wiring issue |
| 22 | Low combustion air | Blocked flue, failed inducer |
| 23 | Draft safeguard switch open | Blocked flue, failed inducer motor |
| 24 | Secondary voltage fuse blown | Short in low-voltage wiring |
| 25 | Control reversing valve fault | Stuck reversing valve (heat pump models) |
| 31 | High-pressure switch open | Refrigerant overcharge, condenser blocked |
| 32 | Low-pressure switch open | Low refrigerant, metering device issue |
| 33 | Limit switch lockout | Persistent overtemperature — check all airflow paths |
| 34 | Ignition proving fault | Flame sensor issue, gas pressure low |
| 41 | Blower motor fault | Failed blower motor or run capacitor |
| 42 | Inducer motor fault | Failed inducer, blocked flue |
| 43 | Low-ambient lockout | Ambient temp below unit minimum rating |
| 44 | Control board fault | Replace integrated control board |
| 45 | Control board memory fault | Replace control board |
| 46 | Power failure | Power interruption logged |
| 48 | Induced draft motor lockout | Failed inducer motor or blocked flue |
| 52 | Defrost fault | Failed defrost board or sensor issue |
| 54 | Defrost thermostat open | Check defrost thermostat and wiring |
| 58 | Compressor fault | Compressor locked out — check contactor and capacitor |

## Most Common Carrier RTU Faults

### Code 13 — Limit Switch Open
The most common commercial RTU service call. Always check in order:
1. Air filter — replace if dirty
2. All supply/return grilles — confirm open
3. Blower wheel — inspect for debris buildup
4. Limit switch continuity — open at room temp means failed switch

### Code 23 — Draft Safeguard Switch
Inducer-related fault. Check inducer motor amp draw and measure flue pressure before condemning the pressure switch.

### Code 33 — Limit Switch Lockout
Three consecutive limit trips trigger a hard lockout. Root cause is almost always restricted airflow. Fix the airflow restriction before resetting.

### Codes 11/14 — Ignition Issues
Check gas pressure first: 3.5 in. w.c. for natural gas, 10 in. w.c. for propane. Clean or replace the flame sensor rod — measure microamp output (must be above 1.5 µA).

### Code 3/31 — High Pressure
Wash condenser coil with coil cleaner. Verify all condenser fans are rotating. Check refrigerant subcooling: target 10–15°F.

## Parts Commonly Needed

| Part | Notes |
|---|---|
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Measure µA before replacing |
| Integrated control board | [Amazon](https://www.amazon.com/s?k=Integrated+control+board&tag=errorcodefixes-20) \| Model-specific — cross-reference by part number |
| Limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-rooftop-unit-error-codes&tag=errorcodefixes-20) \| Match temperature rating exactly |
| Inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-rooftop-unit-error-codes&tag=errorcodefixes-20) \| Check capacitor before condemning motor |
| High-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-rooftop-unit-error-codes&tag=errorcodefixes-20) \| Check setting: 410A = 590 psi, R-22 = 380 psi |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-rooftop-unit-error-codes&tag=errorcodefixes-20) \| Check µF with capacitor tester |
> **Pro tip:** Carrier RTU boards store the last 5 fault codes in memory. Access fault history by pressing and holding the LED diagnostic button for 5 seconds on 48/50 Series controls.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
