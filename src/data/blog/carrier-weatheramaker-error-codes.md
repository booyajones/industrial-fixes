---
title: "Carrier WeatherMaker Rooftop Unit Error Codes: Complete Guide"
description: "Carrier WeatherMaker RTU error codes for 48 and 50 Series commercial rooftop units. Flash codes, fault descriptions, and technician-level fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 2 | Low-pressure lockout | [Low refrigerant, dirty evaporator coil](https://www.amazon.com/s?k=Low%20refrigerant%2C%20dirty%20evaporator%20coil&tag=errorcodefixe-20) | Check static pressure, inspect filter |
| [3](https://www.amazon.com/s?k=3&tag=errorcodefixe-20) | High-pressure lockout | Dirty condenser coil, failed condenser fan | [Wash coil, check fan rotation](https://www.amazon.com/s?k=Wash%20coil%2C%20check%20fan%20rotation&tag=errorcodefixe-20) |  | 11 | [Ignition failure](https://www.amazon.com/s?k=Ignition%20failure&tag=errorcodefixe-20) | No gas, weak spark, dirty flame sensor | Check gas pressure (3.5 in. w.c.) | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 12 | Flame sense fault | [Dirty or cracked flame sensor](https://www.amazon.com/s?k=Dirty%20or%20cracked%20flame%20sensor&tag=errorcodefixe-20) | Clean or replace flame sensor rod |
| [13](https://www.amazon.com/s?k=13&tag=errorcodefixe-20) | Limit switch open | Restricted airflow, dirty filter | [Replace filter, check blower wheel](https://www.amazon.com/s?k=Replace%20filter%2C%20check%20blower%20wheel&tag=errorcodefixe-20) |  | 14 | [Ignition lockout](https://www.amazon.com/s?k=Ignition%20lockout&tag=errorcodefixe-20) | 3 failed ignition attempts | Manual reset required | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 21 | Gas valve fault | [Failed gas valve or wiring issue](https://www.amazon.com/s?k=Failed%20gas%20valve%20or%20wiring%20issue&tag=errorcodefixe-20) | Check 24 VAC at gas valve |
| [22](https://www.amazon.com/s?k=22&tag=errorcodefixe-20) | Low combustion air | Blocked flue, failed inducer | [Inspect flue and inducer pressure](https://www.amazon.com/s?k=Inspect%20flue%20and%20inducer%20pressure&tag=errorcodefixe-20) |  | 23 | [Draft safeguard switch](https://www.amazon.com/s?k=Draft%20safeguard%20switch&tag=errorcodefixe-20) | Blocked flue or failed inducer motor | Measure inducer manifold pressure | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 31 | High-pressure switch open | [Refrigerant overcharge, blocked condenser](https://www.amazon.com/s?k=Refrigerant%20overcharge%2C%20blocked%20condenser&tag=errorcodefixe-20) | Check subcooling (10–15°F target) |
| [33](https://www.amazon.com/s?k=33&tag=errorcodefixe-20) | Limit switch lockout | Persistent overtemperature | [Fix airflow restriction before reset](https://www.amazon.com/s?k=Fix%20airflow%20restriction%20before%20reset&tag=errorcodefixe-20) |  | 41 | [Blower motor fault](https://www.amazon.com/s?k=Blower%20motor%20fault&tag=errorcodefixe-20) | Failed blower motor or run capacitor | Check capacitor µF, motor amps | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 42 | Inducer motor fault | [Failed inducer motor or blocked flue](https://www.amazon.com/s?k=Failed%20inducer%20motor%20or%20blocked%20flue&tag=errorcodefixe-20) | Check inducer amp draw |
| [44](https://www.amazon.com/s?k=44&tag=errorcodefixe-20) | Control board fault | Internal board failure | [Replace IFC board](https://www.amazon.com/s?k=Replace%20IFC%20board&tag=errorcodefixe-20) |  | 46 | [Power failure](https://www.amazon.com/s?k=Power%20failure&tag=errorcodefixe-20) | Power interruption detected | Check supply voltage and breakers | [## Most Common WeatherMaker Faults

### Code 13 — Limit Switch Open
The top commercial RTU call. Work through in order: replace dirty filter, verify all grilles are open, inspect blower wheel for debris, then check limit switch continuity at room temperature.

### Code 23 — Draft Safeguard Switch
Measure inducer manifold pressure before condemning the pressure switch. Typical WeatherMaker spec is -0.20 to -0.35 in. w.c. at the pressure switch. A blocked flue screen is a common culprit.

### Code 11 — Ignition Failure
Check gas pressure first. Natural gas inlet pressure must be 5–7 in. w.c.; manifold pressure 3.5 in. w.c. Clean the flame sensor rod with steel wool — measure µA (must exceed 1.5 µA).

### Code 3 — High Pressure
Verify all condenser fan motors are running and drawing rated amps. Wash the condenser coil. Check refrigerant subcooling with manifold gauges.

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20WeatherMaker%20Faults%0A%0A%23%23%23%20Code%2013%20%E2%80%94%20Limit%20Switch%20Open%0AThe%20top%20commercial%20RTU%20call.%20Work%20through%20in%20order%3A%20replace%20dirty%20filter%2C%20verify%20all%20grilles%20are%20open%2C%20inspect%20blower%20wheel%20for%20debris%2C%20then%20check%20limit%20switch%20continuity%20at%20room%20temperature.%0A%0A%23%23%23%20Code%2023%20%E2%80%94%20Draft%20Safeguard%20Switch%0AMeasure%20inducer%20manifold%20pressure%20before%20condemning%20the%20pressure%20switch.%20Typical%20WeatherMaker%20spec%20is%20-0.20%20to%20-0.35%20in.%20w.c.%20at%20the%20pressure%20switch.%20A%20blocked%20flue%20screen%20is%20a%20common%20culprit.%0A%0A%23%23%23%20Code%2011%20%E2%80%94%20Ignition%20Failure%0ACheck%20gas%20pressure%20first.%20Natural%20gas%20inlet%20pressure%20must%20be%205%E2%80%937%20in.%20w.c.%3B%20manifold%20pressure%203.5%20in.%20w.c.%20Clean%20the%20flame%20sensor%20rod%20with%20steel%20wool%20%E2%80%94%20measure%20%C2%B5A%20(must%20exceed%201.5%20%C2%B5A).%0A%0A%23%23%23%20Code%203%20%E2%80%94%20High%20Pressure%0AVerify%20all%20condenser%20fan%20motors%20are%20running%20and%20drawing%20rated%20amps.%20Wash%20the%20condenser%20coil.%20Check%20refrigerant%20subcooling%20with%20manifold%20gauges.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Flame sensor rod | Clean first; replace if µA reading is below 1.5 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | IFC board | Model-specific — cross-reference part number | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Limit switch | Match temperature rating exactly | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Run capacitor | Test µF with capacitor tester before condemning motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Inducer motor | Check capacitor before replacing motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure switch | Verify switch spec matches flue pressure measured |

> **Pro tip:** Carrier WeatherMaker IFC boards store the last 5 fault codes. Hold the diagnostic button 5 seconds to retrieve fault history before clearing codes.
