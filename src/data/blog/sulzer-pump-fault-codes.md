---
title: "Sulzer Pump Fault Codes: Complete Guide"
description: "Sulzer pump fault codes and diagnostics. Fault codes for Sulzer centrifugal and submersible pumps, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - pumps
  - sulzer
  - industrial
---

# Sulzer Pump Fault Codes

Sulzer pumps (ABS, MF, MXF, WPK series) with integrated controls or monitoring systems display fault codes on the control panel or relay outputs. Sulzer's Pump Advisor monitoring system provides real-time diagnostics. Most Sulzer pumps are controlled by external PLCs or drives — fault codes depend on the associated control system.

## Sulzer ABS/MF Series Fault Reference

| [Fault/Indication](https://www.amazon.com/s?k=Fault%2FIndication&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |-----------------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overtemp alarm | Motor winding overtemperature | [Overload, blocked cooling, high liquid temp](https://www.amazon.com/s?k=Overload%2C%20blocked%20cooling%2C%20high%20liquid%20temp&tag=errorcodefixe-20) | Check motor current and cooling |
| [Moisture alarm](https://www.amazon.com/s?k=Moisture%20alarm&tag=errorcodefixe-20) | Moisture in motor housing | Seal failure | [Inspect mechanical seal](https://www.amazon.com/s?k=Inspect%20mechanical%20seal&tag=errorcodefixe-20) |  | Vibration alarm | [Excessive vibration](https://www.amazon.com/s?k=Excessive%20vibration&tag=errorcodefixe-20) | Cavitation, imbalance, bearing wear | Check for cavitation and bearings | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overcurrent | Motor overcurrent trip | [Overload or winding fault](https://www.amazon.com/s?k=Overload%20or%20winding%20fault&tag=errorcodefixe-20) | Check motor amps and winding resistance |
| [Undercurrent](https://www.amazon.com/s?k=Undercurrent&tag=errorcodefixe-20) | Motor undercurrent | Pump dry running or cavitation | [Check liquid level and system pressure](https://www.amazon.com/s?k=Check%20liquid%20level%20and%20system%20pressure&tag=errorcodefixe-20) |  | Phase loss | [Missing input phase](https://www.amazon.com/s?k=Missing%20input%20phase&tag=errorcodefixe-20) | Supply fault | Check input fuses and contactor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Seal failure | Seal monitoring triggered | [Mechanical seal failure](https://www.amazon.com/s?k=Mechanical%20seal%20failure&tag=errorcodefixe-20) | Replace mechanical seal |
| [Bearing temp high](https://www.amazon.com/s?k=Bearing%20temp%20high&tag=errorcodefixe-20) | High bearing temperature | Lubrication failure or overload | [Check lubrication and alignment](https://www.amazon.com/s?k=Check%20lubrication%20and%20alignment&tag=errorcodefixe-20) |  | Flow low | [Flow below minimum](https://www.amazon.com/s?k=Flow%20below%20minimum&tag=errorcodefixe-20) | Closed valves, strainer blockage | Check system and strainer | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Start failure | Pump fails to start | [Electrical or mechanical](https://www.amazon.com/s?k=Electrical%20or%20mechanical&tag=errorcodefixe-20) | Check starter and impeller |

## Most Common Sulzer Pump Faults

### Moisture Alarm
Sulzer submersible pumps (ABS series) have moisture detection sensors in the motor housing. A moisture alarm indicates seal failure — liquid is entering the motor. Do not operate the pump — remove from service immediately and inspect the mechanical seal. The seal should be replaced proactively before full seal failure floods the motor.

### Overtemperature
Sulzer pump motors are typically thermistor-protected. If the motor winding temperature exceeds 150°C (class F insulation), the thermistor resistance rises sharply, triggering the alarm. Check motor current against nameplate FLA. Check that the cooling jacket has adequate flow. On wet-pit submersible pumps, verify liquid level covers the motor.

### Vibration Alarm
Excessive vibration indicates cavitation, impeller imbalance, or bearing deterioration. Measure vibration at the pump bearing housings with a vibration meter (velocity RMS, target < 4.5 mm/s for good condition). Cavitation sounds like gravel in the pump — increase inlet pressure or reduce flow.

### Undercurrent / Dry Run
Sulzer pumps with undercurrent monitoring detect when flow drops below expected levels. Dry-run operation damages mechanical seals rapidly. Check liquid level in the wet well or tank. Verify suction piping is submerged and not air-locked.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| [Mechanical seal kit](https://www.amazon.com/s?k=Mechanical%20seal%20kit&tag=errorcodefixe-20) | Match pump model and size |
| [Moisture sensor cable](https://www.amazon.com/s?k=Moisture%20sensor%20cable&tag=errorcodefixe-20) | Sulzer-specific — match pump series |
| [Impeller](https://www.amazon.com/s?k=Impeller&tag=errorcodefixe-20) | Replace if worn or damaged |
| [Bearing kit](https://www.amazon.com/s?k=Bearing%20kit&tag=errorcodefixe-20) | Match pump bearing specification |
| [Thermistor](https://www.amazon.com/s?k=Thermistor&tag=errorcodefixe-20) | Match motor winding type |

> **Pro tip:** Sulzer's Pump Advisor digital service platform enables remote condition monitoring of Sulzer pumps via IIoT sensors. Retrofit kits are available for older pump installations — real-time vibration and temperature data can predict failures weeks before they occur.
