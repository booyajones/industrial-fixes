---
title: "Carrier WeatherMaker Rooftop Unit Error Codes: Complete Guide"
description: "Carrier WeatherMaker RTU error codes for 48 and 50 Series commercial rooftop units. Flash codes, fault descriptions, and technician-level fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - rooftop-unit
  - commercial-hvac
---

# Carrier WeatherMaker Rooftop Unit Error Codes

Carrier WeatherMaker 48/50 Series RTUs use an LED diagnostic board that flashes fault codes. Count the LED flashes, wait for a 3-second pause, and count again. The total equals the fault code. Some newer units display codes on a 7-segment display.

## WeatherMaker Flash Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 2 | Low-pressure lockout | Low refrigerant, dirty evaporator coil | Check static pressure, inspect filter |
| 3 | High-pressure lockout | Dirty condenser coil, failed condenser fan | Wash coil, check fan rotation |
| 11 | Ignition failure | No gas, weak spark, dirty flame sensor | Check gas pressure (3.5 in. w.c.) |
| 12 | Flame sense fault | Dirty or cracked flame sensor | Clean or replace flame sensor rod |
| 13 | Limit switch open | Restricted airflow, dirty filter | Replace filter, check blower wheel |
| 14 | Ignition lockout | 3 failed ignition attempts | Manual reset required |
| 21 | Gas valve fault | Failed gas valve or wiring issue | Check 24 VAC at gas valve |
| 22 | Low combustion air | Blocked flue, failed inducer | Inspect flue and inducer pressure |
| 23 | Draft safeguard switch | Blocked flue or failed inducer motor | Measure inducer manifold pressure |
| 31 | High-pressure switch open | Refrigerant overcharge, blocked condenser | Check subcooling (10ΓÇô15┬░F target) |
| 33 | Limit switch lockout | Persistent overtemperature | Fix airflow restriction before reset |
| 41 | Blower motor fault | Failed blower motor or run capacitor | Check capacitor ┬╡F, motor amps |
| 42 | Inducer motor fault | Failed inducer motor or blocked flue | Check inducer amp draw |
| 44 | Control board fault | Internal board failure | Replace IFC board |
| 46 | Power failure | Power interruption detected | Check supply voltage and breakers |

## Most Common WeatherMaker Faults

### Code 13 ΓÇö Limit Switch Open
The top commercial RTU call. Work through in order: replace dirty filter, verify all grilles are open, inspect blower wheel for debris, then check limit switch continuity at room temperature.

### Code 23 ΓÇö Draft Safeguard Switch
Measure inducer manifold pressure before condemning the pressure switch. Typical WeatherMaker spec is -0.20 to -0.35 in. w.c. at the pressure switch. A blocked flue screen is a common culprit.

### Code 11 ΓÇö Ignition Failure
Check gas pressure first. Natural gas inlet pressure must be 5ΓÇô7 in. w.c.; manifold pressure 3.5 in. w.c. Clean the flame sensor rod with steel wool ΓÇö measure ┬╡A (must exceed 1.5 ┬╡A).

### Code 3 ΓÇö High Pressure
Verify all condenser fan motors are running and drawing rated amps. Wash the condenser coil. Check refrigerant subcooling with manifold gauges.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) \| Clean first; replace if ┬╡A reading is below 1.5 |
| IFC board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Model-specific ΓÇö cross-reference part number |
| Limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?tag=errorcodefixes-20) \| Match temperature rating exactly |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) \| Test ┬╡F with capacitor tester before condemning motor |
| Inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) \| Check capacitor before replacing motor |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| Verify switch spec matches flue pressure measured |
> **Pro tip:** Carrier WeatherMaker IFC boards store the last 5 fault codes. Hold the diagnostic button 5 seconds to retrieve fault history before clearing codes.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
