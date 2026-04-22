---
title: "Lennox XC21 Error Codes — Diagnostic Guide and Fixes"
description: "Complete guide to Lennox XC21 variable-capacity heat pump error codes displayed on iComfort thermostats, with causes and step-by-step fixes."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox XC21 Error Codes — What They Mean

The Lennox XC21 is a variable-capacity inverter heat pump that communicates with the iComfort S30 or E30 thermostat over the proprietary iComfort communication bus. Fault codes appear on the thermostat under Menu > Alerts or can be viewed through the Lennox dealer diagnostic app. Unlike older Lennox flash-code units, the XC21 generates text-based alert codes that describe the fault type and which component detected it. The outdoor unit, indoor unit, and thermostat each report independently.

[Jump to Fix](#fix)

## Most Common XC21 Alert Codes

| [Alert Code](https://www.amazon.com/s?k=Alert%20Code&tag=errorcodefixe-20) | Meaning |
|-----------|---------|
| [434](https://www.amazon.com/s?k=434&tag=errorcodefixe-20) | Outdoor unit lost communication |
| [411](https://www.amazon.com/s?k=411&tag=errorcodefixe-20) | Indoor unit lost communication |
| [327](https://www.amazon.com/s?k=327&tag=errorcodefixe-20) | High discharge temperature |
| [225](https://www.amazon.com/s?k=225&tag=errorcodefixe-20) | Low-pressure fault (outdoor) |
| [223](https://www.amazon.com/s?k=223&tag=errorcodefixe-20) | High-pressure fault (outdoor) |
| [204](https://www.amazon.com/s?k=204&tag=errorcodefixe-20) | Compressor over-current |
| [125](https://www.amazon.com/s?k=125&tag=errorcodefixe-20) | Outdoor ambient temperature sensor fault |
| [103](https://www.amazon.com/s?k=103&tag=errorcodefixe-20) | Discharge temperature sensor fault |

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
| [iComfort thermostat (S30 or E30)](https://www.amazon.com/s?k=iComfort%20thermostat%20(S30%20or%20E30)&tag=errorcodefixe-20) | For persistent 411/434 after wiring confirmed |
| [Outdoor unit control board](https://www.amazon.com/s?k=Outdoor%20unit%20control%20board&tag=errorcodefixe-20) | For persistent 434 — must match XC21 model exactly |
| [Condenser fan motor + capacitor](https://www.amazon.com/s?k=Condenser%20fan%20motor%20%2B%20capacitor&tag=errorcodefixe-20) | For Alert 223 with clean coil; test capacitor before motor |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | For persistent Alert 225 after confirming charge |
| [Discharge temperature sensor](https://www.amazon.com/s?k=Discharge%20temperature%20sensor&tag=errorcodefixe-20) | For Alert 103 or persistent 327 with correct charge |

## When to Call a Pro

The XC21's inverter-driven compressor requires specialized diagnostic tools — the iComfort communicating system gives real-time compressor speed, operating pressures, and temperature data that a Lennox dealer can read remotely via the iComfort Connect portal. All refrigerant work requires EPA 608 certification. If the inverter drive board inside the outdoor unit is suspect, replacement involves high-voltage components and should only be handled by a trained technician.
