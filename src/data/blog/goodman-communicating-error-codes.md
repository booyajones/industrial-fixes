---
title: "Goodman ComfortNet Communicating System Error Codes — Complete Guide"
description: "Goodman ComfortNet communicating system error codes: fault codes for ComfortNet-enabled furnaces, heat pumps, and air handlers with causes and fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - communicating
---

## Goodman ComfortNet Communicating System Error Codes — Quick Reference

Goodman's ComfortNet communicating system allows compatible furnaces, heat pumps, air conditioners, and air handlers to share data over a two-wire communication bus. Fault codes appear on the ComfortNet-compatible thermostat (such as the ComfortNet CTK04 or CTK06) and on the individual equipment's LED control board. The same underlying codes are used in Amana ComfortNet systems.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------|---------|-----------|
| E1 | Indoor temperature sensor fault | Check thermostat sensor |
| E2 | Outdoor temperature sensor fault | Inspect outdoor unit sensor wiring |
| E3 | Discharge air sensor fault | Check sensor at air handler/furnace |
| E4 | Communication fault — indoor unit | Check ComfortNet bus wiring at AHU |
| E5 | Communication fault — outdoor unit | Check bus wiring at outdoor unit |
| E6 | Communication fault — thermostat | Inspect thermostat wiring; replace T-stat |
| E7 | Communication bus fault — all devices | Check entire bus wiring; verify termination |
| F1 | Pressure switch fault | Check inducer, hose, pressure switch |
| F2 | High-limit switch fault | Check filter, airflow, heat exchanger |
| F3 | Flame sensor fault | Clean flame sensor rod |
| F4 | Ignition lockout | Check gas supply, igniter, sensor |
| F5 | Rollout switch open | Do not reset — call technician |
| F6 | Inducer motor fault | Test inducer motor |
| F7 | Blower motor fault | Test blower motor/ECM |

## Most Common Faults

### E4–E7 — ComfortNet Communication Bus Faults
The ComfortNet two-wire data bus is the most common source of faults in communicating Goodman systems. The bus requires proper polarity (terminals are labeled COM+ and COM-), and the wiring must be continuous — not star-wired. Inspect all four connection points: furnace/air handler, outdoor unit, thermostat, and any accessories. A single corroded terminal or reversed polarity anywhere on the bus will cause communication faults throughout the system.

### F4 — Ignition Lockout
The furnace attempted to light the burners the maximum number of times without detecting a flame. Start with the simple checks: verify the gas supply valve is fully open, check that other gas appliances in the home are working (rules out a supply issue), then inspect the hot-surface igniter for cracks. A cracked igniter will glow but not get hot enough to light the burners. Clean the flame sensor rod with fine steel wool — even a thin oxide coating can prevent proper flame sensing.

### F2 — High-Limit Switch Fault
The high-temperature limit switch tripped during operation. The most common cause is restricted airflow — check the air filter immediately. If the filter is clean, check that all supply and return registers are open. On high-efficiency furnaces, also check the secondary heat exchanger for blockages. If the limit continues to trip with a clean filter and open registers, the furnace heat exchanger may have a crack causing recirculation of flue gases.

### F5 — Rollout Switch Open
The flame rollout switch is a critical safety device that detects burner flame rolling out of the burner compartment — a sign of severe problems including a cracked heat exchanger or blocked flue. **Do not reset this switch and continue operating the furnace.** Call an HVAC technician immediately to inspect the heat exchanger and flue system.

### F7 — Blower Motor Fault
On ComfortNet systems, the blower motor is typically a variable-speed ECM. A fault means the motor failed to start, stalled, or exceeded temperature limits. Check that the motor plug is fully connected to the control board. If the motor is hot to the touch and won't spin, allow it to cool for 30 minutes — if it starts after cooling and then fails again, the ECM module is failing.

## ComfortNet System Setup Notes

- ComfortNet bus wiring polarity must be maintained throughout the system
- Maximum total bus length: 500 feet
- Only ComfortNet-compatible thermostats can access the full fault code list
- Non-communicating thermostats will still work but won't display detailed codes

## When to Call a Pro
F5 (rollout) is a mandatory technician call — this is a safety fault, not a normal operating fault. Refrigerant-related outdoor unit faults also require licensed HVAC/R service.
