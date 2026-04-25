---
title: "Emerson/Alco Controls EEV Fault Codes — Troubleshooting Guide"
description: "Emerson and Alco Controls electronic expansion valve fault codes: controller alarms, superheat problems, stepper valve faults, and repair steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - emerson
  - alco
  - eev
---

## Emerson / Alco Controls EEV Fault Codes — Quick Reference

Emerson and Alco Controls EEV systems pair a controller with a stepper valve to manage evaporator superheat. The controller, not the valve body, usually reports the fault. Common controllers include Emerson E2, Dixell, and OEM rack controllers.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixes-20) | Meaning | Quick Fix |
|------|---------|-----------|
| [Valve Error](https://www.amazon.com/s?k=Valve+Error&tag=errorcodefixes-20) | EEV not moving as commanded | Check wiring, coil, and controller output |
| [Superheat High](https://www.amazon.com/s?k=Superheat+High&tag=errorcodefixes-20) | Evaporator starved | Check charge, drier, and valve movement |
| [Superheat Low](https://www.amazon.com/s?k=Superheat+Low&tag=errorcodefixes-20) | Flooding risk | Check sensors and controller tuning |
| [Sensor Fault](https://www.amazon.com/s?k=Sensor+Fault&tag=errorcodefixes-20) | Pressure or temperature input failed | Check sensor wiring and readings |
| [Communication Fault](https://www.amazon.com/s?k=Communication+Fault&tag=errorcodefixes-20) | Controller lost rack/network communication | Check comm wiring and address |
| [Position Lost](https://www.amazon.com/s?k=Position+Lost&tag=errorcodefixes-20) | Valve position unknown after power loss | Re-home or reinitialize valve |

## Most Common Faults

### Valve Error
Check the EEV motor connector first. Vibration and moisture cause bad connections. If the controller supports manual positioning, step the valve open and watch suction pressure. No change points to a stuck valve, failed motor, or upstream liquid issue.

### Superheat High
A high superheat alarm usually means the evaporator is starved. Check refrigerant charge, liquid line solenoid, plugged filter-drier, and flash gas in the liquid line. Also verify the temperature sensor is tight on the suction line and insulated.

### Position Lost
Some controllers lose track of valve position during a power interruption. The fix is usually to re-home the valve through the controller menu or cycle power so the controller can drive the valve to a known closed position.

## Field Checks

| [Check](https://www.amazon.com/s?k=Check&tag=errorcodefixes-20) | Why it matters |
|------|----------------|
| [Suction line sensor tight and insulated](https://www.amazon.com/s?k=Suction+line+sensor+tight+and+insulated&tag=errorcodefixes-20) | Prevents false superheat readings |
| [Pressure transducer matches gauge reading](https://www.amazon.com/s?k=Pressure+transducer+matches+gauge+reading&tag=errorcodefixes-20) | Confirms controller sees the right pressure |
| [Filter-drier pressure drop](https://www.amazon.com/s?k=Filter-drier+pressure+drop&tag=errorcodefixes-20) | Catches liquid line restriction |
| [Valve responds to manual command](https://www.amazon.com/s?k=Valve+responds+to+manual+command&tag=errorcodefixes-20) | Confirms controller and motor function |

## Jump to Fix

- **Valve error** → Check connector → Command valve manually → Check for suction pressure change
- **Superheat high** → Check charge → Check drier and liquid feed → Verify sensors
- **Position lost** → Re-home valve → Cycle controller power if required

## When to Call a Pro
EEV faults need pressure, temperature, and control data at the same time. If you only swap parts, you will miss the real cause. Call a refrigeration tech who can verify superheat and controller response.
