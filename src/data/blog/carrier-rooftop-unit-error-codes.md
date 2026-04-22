---
title: "Carrier Rooftop Unit Error Codes: Common Faults Guide"
description: "Complete guide to Carrier RTU error codes. Covers flash codes, fault descriptions, and technician-level fixes for 48 and 50 Series commercial rooftop units."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
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

| [Flash Code](https://www.amazon.com/s?k=Flash%20Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| 2 | [Low-pressure lockout](https://www.amazon.com/s?k=Low-pressure%20lockout&tag=errorcodefixe-20) | Low refrigerant, dirty filter, blocked coil |
| [3](https://www.amazon.com/s?k=3&tag=errorcodefixe-20) | High-pressure lockout | Dirty condenser coil, failed condenser fan, overcharge | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 4 | Open high-pressure switch | [Refrigerant overcharge, blocked condenser](https://www.amazon.com/s?k=Refrigerant%20overcharge%2C%20blocked%20condenser&tag=errorcodefixe-20) |  | 11 | [Ignition failure](https://www.amazon.com/s?k=Ignition%20failure&tag=errorcodefixe-20) | No gas, weak spark, dirty flame sensor |
| [12](https://www.amazon.com/s?k=12&tag=errorcodefixe-20) | Flame sense fault | Dirty/cracked flame sensor, grounding issue | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 13 | Limit switch open | [Restricted airflow, dirty filter, failed blower](https://www.amazon.com/s?k=Restricted%20airflow%2C%20dirty%20filter%2C%20failed%20blower&tag=errorcodefixe-20) |  | 14 | [Ignition lockout](https://www.amazon.com/s?k=Ignition%20lockout&tag=errorcodefixe-20) | 3 failed ignition attempts — requires manual reset |
| [21](https://www.amazon.com/s?k=21&tag=errorcodefixe-20) | Gas valve fault | Failed gas valve, wiring issue | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 22 | Low combustion air | [Blocked flue, failed inducer](https://www.amazon.com/s?k=Blocked%20flue%2C%20failed%20inducer&tag=errorcodefixe-20) |  | 23 | [Draft safeguard switch open](https://www.amazon.com/s?k=Draft%20safeguard%20switch%20open&tag=errorcodefixe-20) | Blocked flue, failed inducer motor |
| [24](https://www.amazon.com/s?k=24&tag=errorcodefixe-20) | Secondary voltage fuse blown | Short in low-voltage wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 25 | Control reversing valve fault | [Stuck reversing valve (heat pump models)](https://www.amazon.com/s?k=Stuck%20reversing%20valve%20(heat%20pump%20models)&tag=errorcodefixe-20) |  | 31 | [High-pressure switch open](https://www.amazon.com/s?k=High-pressure%20switch%20open&tag=errorcodefixe-20) | Refrigerant overcharge, condenser blocked |
| [32](https://www.amazon.com/s?k=32&tag=errorcodefixe-20) | Low-pressure switch open | Low refrigerant, metering device issue | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 33 | Limit switch lockout | [Persistent overtemperature — check all airflow paths](https://www.amazon.com/s?k=Persistent%20overtemperature%20%E2%80%94%20check%20all%20airflow%20paths&tag=errorcodefixe-20) |  | 34 | [Ignition proving fault](https://www.amazon.com/s?k=Ignition%20proving%20fault&tag=errorcodefixe-20) | Flame sensor issue, gas pressure low |
| [41](https://www.amazon.com/s?k=41&tag=errorcodefixe-20) | Blower motor fault | Failed blower motor or run capacitor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 42 | Inducer motor fault | [Failed inducer, blocked flue](https://www.amazon.com/s?k=Failed%20inducer%2C%20blocked%20flue&tag=errorcodefixe-20) |  | 43 | [Low-ambient lockout](https://www.amazon.com/s?k=Low-ambient%20lockout&tag=errorcodefixe-20) | Ambient temp below unit minimum rating |
| [44](https://www.amazon.com/s?k=44&tag=errorcodefixe-20) | Control board fault | Replace integrated control board | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 45 | Control board memory fault | [Replace control board](https://www.amazon.com/s?k=Replace%20control%20board&tag=errorcodefixe-20) |  | 46 | [Power failure](https://www.amazon.com/s?k=Power%20failure&tag=errorcodefixe-20) | Power interruption logged |
| [48](https://www.amazon.com/s?k=48&tag=errorcodefixe-20) | Induced draft motor lockout | Failed inducer motor or blocked flue | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 52 | Defrost fault | [Failed defrost board or sensor issue](https://www.amazon.com/s?k=Failed%20defrost%20board%20or%20sensor%20issue&tag=errorcodefixe-20) |  | 54 | [Defrost thermostat open](https://www.amazon.com/s?k=Defrost%20thermostat%20open&tag=errorcodefixe-20) | Check defrost thermostat and wiring |
| [58](https://www.amazon.com/s?k=58&tag=errorcodefixe-20) | Compressor fault | Compressor locked out — check contactor and capacitor | [## Most Common Carrier RTU Faults

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

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Carrier%20RTU%20Faults%0A%0A%23%23%23%20Code%2013%20%E2%80%94%20Limit%20Switch%20Open%0AThe%20most%20common%20commercial%20RTU%20service%20call.%20Always%20check%20in%20order%3A%0A1.%20Air%20filter%20%E2%80%94%20replace%20if%20dirty%0A2.%20All%20supply%2Freturn%20grilles%20%E2%80%94%20confirm%20open%0A3.%20Blower%20wheel%20%E2%80%94%20inspect%20for%20debris%20buildup%0A4.%20Limit%20switch%20continuity%20%E2%80%94%20open%20at%20room%20temp%20means%20failed%20switch%0A%0A%23%23%23%20Code%2023%20%E2%80%94%20Draft%20Safeguard%20Switch%0AInducer-related%20fault.%20Check%20inducer%20motor%20amp%20draw%20and%20measure%20flue%20pressure%20before%20condemning%20the%20pressure%20switch.%0A%0A%23%23%23%20Code%2033%20%E2%80%94%20Limit%20Switch%20Lockout%0AThree%20consecutive%20limit%20trips%20trigger%20a%20hard%20lockout.%20Root%20cause%20is%20almost%20always%20restricted%20airflow.%20Fix%20the%20airflow%20restriction%20before%20resetting.%0A%0A%23%23%23%20Codes%2011%2F14%20%E2%80%94%20Ignition%20Issues%0ACheck%20gas%20pressure%20first%3A%203.5%20in.%20w.c.%20for%20natural%20gas%2C%2010%20in.%20w.c.%20for%20propane.%20Clean%20or%20replace%20the%20flame%20sensor%20rod%20%E2%80%94%20measure%20microamp%20output%20(must%20be%20above%201.5%20%C2%B5A).%0A%0A%23%23%23%20Code%203%2F31%20%E2%80%94%20High%20Pressure%0AWash%20condenser%20coil%20with%20coil%20cleaner.%20Verify%20all%20condenser%20fans%20are%20rotating.%20Check%20refrigerant%20subcooling%3A%20target%2010%E2%80%9315%C2%B0F.%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Flame sensor rod | Measure µA before replacing | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Integrated control board | Model-specific — cross-reference by part number | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Limit switch | Match temperature rating exactly | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Inducer motor | Check capacitor before condemning motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | High-pressure switch | Check setting: 410A = 590 psi, R-22 = 380 psi | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Run capacitor | Check µF with capacitor tester |

> **Pro tip:** Carrier RTU boards store the last 5 fault codes in memory. Access fault history by pressing and holding the LED diagnostic button for 5 seconds on 48/50 Series controls.
