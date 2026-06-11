---
title: "Lennox XC21 Error Codes — Diagnostic Guide and Fixes"
description: "Complete guide to Lennox XC21 variable-capacity heat pump error codes displayed on iComfort thermostats, with causes and step-by-step fixes."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - lennox
money_part: "iComfort thermostat (S30 or E30)"
---

## Lennox XC21 Error Codes — What They Mean

The Lennox XC21 is a variable-capacity inverter heat pump that communicates with the iComfort S30 or E30 thermostat over the proprietary iComfort communication bus. Fault codes appear on the thermostat under Menu > Alerts or can be viewed through the Lennox dealer diagnostic app. Unlike older Lennox flash-code units, the XC21 generates text-based alert codes that describe the fault type and which component detected it. The outdoor unit, indoor unit, and thermostat each report independently.

[Jump to Fix](#fix)

## Most Common XC21 Alert Codes

| Alert Code | Meaning |
|-----------|---------|
| 434 | Outdoor unit lost communication |
| 411 | Indoor unit lost communication |
| 327 | High discharge temperature |
| 225 | Low-pressure fault (outdoor) |
| 223 | High-pressure fault (outdoor) |
| 204 | Compressor over-current |
| 125 | Outdoor ambient temperature sensor fault |
| 103 | Discharge temperature sensor fault |

## Common Causes

- **Alerts 434/411 — Communication faults** — Loose or corroded communication wiring at the terminal blocks, failed iComfort thermostat, or failed outdoor/indoor control board. These are the most frequent XC21 field complaints.
- **Alert 327 — High discharge temp** — Low refrigerant charge, restricted liquid line filter drier, dirty condenser coil, or outdoor fan motor failure. Discharge temps above ~270°F trigger this protective lockout.
- **Alert 225 — Low pressure** — Refrigerant leak, liquid line solenoid valve stuck closed, or failed low-pressure switch. Do not operate the unit with low pressure — the compressor will fail without adequate refrigerant oil return.
- **Alert 223 — High pressure** — Dirty condenser coil, failed outdoor fan motor, refrigerant overcharge, or non-condensable gases in the system. Clean the coil before checking charge.
- **Alert 204 — Compressor over-current** — Low supply voltage, failing compressor, or inverter drive fault. Check voltage first — low voltage is the most common cause of compressor overcurrent on variable-speed units.

## Step-by-Step Fix {#fix}

1. **Pull the full alert history from iComfort** — Navigate to Menu > Advanced > Alerts on the iComfort thermostat. Record all alerts with timestamps. The history helps distinguish one-time events from recurring patterns.
2. **For Alerts 434/411** — Inspect communication wiring at both the outdoor unit and the air handler. iComfort uses two wires on the COMM terminals — ensure both are secure, unbroken, and not touching each other or ground. Power cycle the system with a 60-second wait.
3. **For Alert 327 or 225** — Connect refrigerant manifold gauges to evaluate system charge. On the XC21, target subcooling within the range on the unit data plate (typically 10–15°F). If subcooling is low, the system has a refrigerant leak — locate and repair before recharging.
4. **For Alert 223** — Clean the condenser coil thoroughly from the inside out using a low-pressure garden hose. Check that the outdoor fan is spinning at full speed. If coil is clean and fan is good, verify charge level.
5. **For Alert 204** — Measure supply voltage at the outdoor unit disconnect under load. Should be within ±10% of nameplate voltage. If voltage is correct, measure compressor RLA with a clamp meter; compare to nameplate.
6. **Clear alerts and test** — After repairs, clear alerts from the iComfort menu and run a 15-minute heating and cooling cycle. Confirm no alerts recur and the system reaches the target set point.

## Parts Often Needed

| Part | Notes |
|------|-------|
| iComfort thermostat (S30 or E30) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-xc21-error-codes&k=iComfort+thermostat+%28S30+or+E30%29&tag=errorcodefixes-20) \| For persistent 411/434 after wiring confirmed |
| Outdoor unit control board | [Amazon](https://www.amazon.com/s?k=Outdoor+unit+control+board&tag=errorcodefixes-20) \| For persistent 434 — must match XC21 model exactly |
| Condenser fan motor + capacitor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-lennox-xc21-error-codes&tag=errorcodefixes-20) \| For Alert 223 with clean coil; test capacitor before motor |
| Low-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lennox-xc21-error-codes&tag=errorcodefixes-20) \| For persistent Alert 225 after confirming charge |
| Discharge temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-lennox-xc21-error-codes&tag=errorcodefixes-20) \| For Alert 103 or persistent 327 with correct charge |
## When to Call a Pro

The XC21's inverter-driven compressor requires specialized diagnostic tools — the iComfort communicating system gives real-time compressor speed, operating pressures, and temperature data that a Lennox dealer can read remotely via the iComfort Connect portal. All refrigerant work requires EPA 608 certification. If the inverter drive board inside the outdoor unit is suspect, replacement involves high-voltage components and should only be handled by a trained technician.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)

## See Also

- [Lennox Error Code 114 — Causes & Fix](/posts/lennox-error-code-114/)
- [Lennox ResolvePlus Rooftop Unit Error Codes: Complete Guide](/posts/lennox-resolve-plus-error-codes/)
- [Lennox Error Code 125 — Causes & Fix](/posts/lennox-error-code-125/)
- [Lennox Harmony III Zoning System Error Codes — Complete Guide](/posts/lennox-harmony-iii-error-codes/)
