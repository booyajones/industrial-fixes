---
title: "Lennox Furnace Error Codes — Complete Reference Guide"
description: "Lennox furnace error codes: all fault codes for G61, ML, EL, and SL series furnaces with causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox Furnace Error Codes — Quick Reference

Lennox furnaces use a combination of flash codes (older models) and numeric fault codes displayed on an iComfort thermostat or the control board's diagnostic port (newer communicating models). On non-communicating furnaces, look for the blinking LED on the IFC board through the lower access panel. Lennox also makes Aire-Flo, Armstrong Air, and Ducane — codes may overlap.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------|---------|-----------|
| 103 | Rollout switch lockout | Inspect heat exchanger; reset switch |
| 111 | No previous fault | Normal after power cycle |
| 114 | Blower on/off delay | Timing fault; check blower |
| 125 | Pressure switch fault | Check inducer, hose, drain trap |
| 204 | Ignition lockout | Check gas, igniter, flame sensor |
| 223 | Limit switch open | Clean/replace filter; check blower |
| 225 | Flame roll-out switch open | Safety fault; inspect heat exchanger |
| 231 | Gas valve fault | Gas valve or wiring issue |
| 327 | Pressure switch stuck closed | Check pressure switch hose |
| 332 | Inducer motor fault | Check inducer motor and wiring |
| 411 | Flame sensed without call | Possible gas valve leak |
| 412 | Flame failure | Clean flame sensor; check gas |
| 414 | Gas valve or roll-out fault | Check gas valve energization |
| 432 | Communication fault | Check thermostat wiring |
| 434 | Blower motor fault | Check motor and capacitor |
| 540 | Board fault | Replace IFC board |
| 292 | Variable-speed blower fault | Check blower motor ECM |

## Most Common Codes

### Code 204: Ignition Lockout
Four ignition attempts failed. On Lennox G61MPV and ML296V models, check the hot-surface igniter — Lennox uses a silicon nitride igniter rated at 40–90 ohms cold resistance. Also verify the gas supply is on and check the main gas valve operator coil for continuity (24V AC signal should reach the valve on a call for heat).

### Code 223: High Limit Open
Limit switch tripped due to overheating. Replace the filter first — Lennox high-efficiency models use thick media filters that clog quickly. Also verify all supply and return registers are open. On variable-speed models (ML/EL/SL series), check that the ECM blower motor ramps up properly; a failing motor running at low speed causes repeated limit trips.

### Code 225: Flame Roll-Out Switch Open
Hot gases backed out of the heat exchanger and melted a fuse link or tripped a manual-reset roll-out switch. This is a serious fault — do not simply reset without finding the cause. Possible causes: blocked flue pipe, cracked heat exchanger, excessive gas pressure, or blocked secondary heat exchanger on 90%+ models.

### Code 412: Flame Failure
Burner lit briefly but flame wasn't confirmed. Clean the flame sensor rod. On Lennox G61 series, the flame sensor is located in the rightmost burner position. Microamp signal should be above 1.5 µA; below 1.0 µA is unreliable.

### Code 432: Communication Fault
On iComfort-equipped systems, the furnace and thermostat have lost the communication bus. Check the 2-wire thermostat cable and connections at both ends. A short in the communication wire is common if rodents have accessed the unit.

### Code 292: Variable-Speed Blower Fault
The ECM blower motor on variable-speed Lennox furnaces has reported a fault. This can mean a failed motor, bad motor controller module, or communication error between the board and ECM. Start by checking all harness connectors to the motor.

## When to Call a Pro
Codes 225 (roll-out) and 411 (flame without call) require professional inspection before the furnace is restarted. A cracked heat exchanger or leaking gas valve are not DIY repairs.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
