---
title: "Industrial Equipment Troubleshooting by Symptom"
description: "Industrial equipment problems by symptom — find the error code and fix for your specific situation."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
---

## Industrial Equipment Troubleshooting by Symptom

Sometimes you know what's wrong with the equipment but don't know the error code. This guide maps symptoms to the most likely error codes and fixes across all equipment types.

## HVAC / Furnace Symptoms

| Symptom | Most Likely Code | Fix |
|---------|-----------------|-----|
| Furnace runs but no heat | Code 3-4 (pressure/limit) | Check filter, verify gas |
| Furnace short cycling | Code 4 (limit) | Dirty filter, blocked airflow |
| AC runs, no cold air | E3 (low pressure) | Low refrigerant — call tech |
| Furnace flashing red light | Any flash code | Count flashes — see brand guide |
| Pilot won't stay lit | E002/E003 (ignition) | Clean flame sensor rod |
| Mini-split blinking | E or CH code | Check drain, filter, sensor |
| Heat pump not defrosting | E5 (defrost fault) | Check defrost thermostat |

## VFD / Motor Control Symptoms

| Symptom | Most Likely Code | Fix |
|---------|-----------------|-----|
| Motor won't start | F3/F4 (power loss/UV) | Check input voltage, fuses |
| Motor runs hot | OL, F7 (overload) | Verify motor FLA parameter |
| Drive trips on every start | OC during acceleration | Extend acceleration ramp time |
| Drive trips during decel | OV (overvoltage) | Extend deceleration time |
| Drive trips under load | F6/F7 (motor stall/OL) | Mechanical overload or wrong parameter |
| Ground fault | GF, F13 | Megohm test motor |

## CNC Machine Symptoms

| Symptom | Most Likely Code | Fix |
|---------|-----------------|-----|
| Machine won't move after startup | 102/105 (E-stop/servos off) | Release E-stop, home machine |
| Tool change stops mid-cycle | 121-128 (ATC fault) | Manual ATC recovery procedure |
| Axis stops during cutting | 414/435/436 (following error) | Check for binding, encoder cable |
| Spindle won't come to speed | 116/117 (spindle fault) | Check drive, encoder cable |
| Machine position is wrong | 600 (APC/battery alarm) | Replace backup battery |
| Program won't run | 500 (overtravel) | Re-home machine, check coordinates |

## Commercial Refrigeration Symptoms

| Symptom | Most Likely Code | Fix |
|---------|-----------------|-----|
| Walk-in warm | High temp alarm | Check fans, condenser, door seal |
| Ice machine not making ice | E1-E3, Code 1-3 | Clean condenser, check water |
| Reach-in running but warm | E2 / high temp | Check condenser, door gasket |
| Ice machine error light | Multiple codes | See brand-specific guide |
| Walk-in frozen solid | Defrost fault | Check heater + thermostat |

## Boiler / Water Heater Symptoms

| Symptom | Most Likely Code | Fix |
|---------|-----------------|-----|
| No hot water | E002/E003 (Navien), Code 11 (Rinnai) | Check gas, igniter |
| Water heater in lockout | Various lockout codes | Check gas supply, reset |
| Boiler makes noise | Not typically coded | Expansion tank, bleed air |
| Tankless water lukewarm | E302 (Navien low pressure) | Check water pressure |

## When the Symptom Has No Error Code

Some equipment problems don't generate error codes:
- Dirty air filters (HVAC)
- Loose electrical connections
- Mechanical wear and vibration
- Low refrigerant before the pressure switch trips

When there's no code, use the symptom tables above combined with physical inspection.
