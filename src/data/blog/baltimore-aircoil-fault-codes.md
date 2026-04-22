---
title: "Baltimore Aircoil Cooling Tower Fault Codes — VXT / VTL Series Guide"
description: "Baltimore Aircoil (BAC) cooling tower fault codes and alarm conditions for VXT, VTL, and Series V towers: causes and troubleshooting steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cooling-tower
  - baltimore-aircoil
  - hvac
  - industrial
---

## Baltimore Aircoil Cooling Tower Fault Codes — Quick Reference

Baltimore Aircoil (BAC) cooling towers with electronic fan control panels or variable-frequency drives generate fault conditions based on motor, temperature, and water system monitoring.

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| Fan Motor Overload | Fan motor current too high | Check motor current, bearings, and fan blades |
| High Water Temperature | Leaving water temperature above setpoint | Check fan operation and heat load |
| Low Water Level | Basin water level low | Check makeup water valve and float |
| High Water Level | Basin water level too high | Check overflow and makeup valve |
| Vibration Fault | Vibration sensor triggered | Inspect fan, drive shaft, and bearings |
| Motor Phase Loss | Phase missing to fan motor | Check electrical supply and fuses |
| VFD Fault | Variable frequency drive fault | Check VFD fault code display |
| Freeze Protection | Basin temperature near freezing | Activate basin heater, verify controls |

## Most Common Faults

### Fan Motor Overload
Fan motor overcurrent is the most common BAC cooling tower fault. Common causes: worn fan bearings increasing drag, ice buildup on fan blades in cold weather, belt wear or tension issues (belt-drive models), and motor winding failure. Check current with a clamp meter and compare to nameplate amps.

### High Leaving Water Temperature
If the cooling tower cannot maintain the setpoint, check: all fans running at correct speed, drift eliminator not blocked, distribution basin not scaled, and heat load not exceeding tower capacity. In summer, approach temperature limits may be reached on very hot days.

### Low Water Level
Makeup water valve not opening, float valve stuck, or city water pressure low. Check the float valve operation. Also inspect for basin leaks — a cracked basin or failed seal can drain faster than makeup can supply.

### Freeze Protection
Cold weather operation requires freeze protection. The basin heater must be operational. Check basin heater element continuity and thermostat setpoint. Some BAC towers use electric basin heaters; others rely on water circulation to prevent freezing.

## VFD-Controlled Towers

BAC VXT and VTL towers often use ABB, Danfoss, or Yaskawa VFDs to vary fan speed. If the VFD displays a fault:
1. Note the fault code on the VFD display
2. Refer to the VFD manufacturer fault code guide (see related VFD posts on this site)
3. Common VFD faults: F7 (motor stall), F3 (overcurrent), undervoltage

## Preventive Maintenance Schedule

| Interval | Task |
|----------|------|
| Monthly | Check basin water level and quality |
| Quarterly | Inspect fan blades, motor, and bearings |
| Annually | Clean fill media, inspect basin, lubricate bearings |

## Jump to Fix

- **Fan overload** → Check motor current → Inspect bearings → Check fan blades for ice or damage
- **High leaving water temp** → Verify fan operation → Check for scale on fill → Verify heat load
- **Low water level** → Check makeup valve → Inspect float → Look for basin leak

## When to Call a Pro
BAC authorized service providers handle tower inspections, water treatment, and component replacement. Contact BAC at 1-410-799-6200.
