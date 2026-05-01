---
title: "Sulzer Pump Fault Codes: Complete Guide"
description: "Sulzer pump fault codes and diagnostics. Fault codes for Sulzer centrifugal and submersible pumps, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
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

| Fault/Indication | Fault Description | Common Cause | Action |
|-----------------|------------------|--------------|--------|
| Overtemp alarm | Motor winding overtemperature | Overload, blocked cooling, high liquid temp | Check motor current and cooling |
| Moisture alarm | Moisture in motor housing | Seal failure | Inspect mechanical seal |
| Vibration alarm | Excessive vibration | Cavitation, imbalance, bearing wear | Check for cavitation and bearings |
| Overcurrent | Motor overcurrent trip | Overload or winding fault | Check motor amps and winding resistance |
| Undercurrent | Motor undercurrent | Pump dry running or cavitation | Check liquid level and system pressure |
| Phase loss | Missing input phase | Supply fault | Check input fuses and contactor |
| Seal failure | Seal monitoring triggered | Mechanical seal failure | Replace mechanical seal |
| Bearing temp high | High bearing temperature | Lubrication failure or overload | Check lubrication and alignment |
| Flow low | Flow below minimum | Closed valves, strainer blockage | Check system and strainer |
| Start failure | Pump fails to start | Electrical or mechanical | Check starter and impeller |

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
| Mechanical seal kit | [Amazon](https://www.amazon.com/s?k=Mechanical+seal+kit&tag=errorcodefixes-20) \| Match pump model and size |
| Moisture sensor cable | [Amazon](https://www.amazon.com/s?k=Moisture+sensor+cable&tag=errorcodefixes-20) \| Sulzer-specific — match pump series |
| Impeller | [Amazon](https://www.amazon.com/s?k=Impeller&tag=errorcodefixes-20) \| Replace if worn or damaged |
| Bearing kit | [Amazon](https://www.amazon.com/s?k=Bearing+kit&tag=errorcodefixes-20) \| Match pump bearing specification |
| Thermistor | [Amazon](https://www.amazon.com/s?k=Thermistor&tag=errorcodefixes-20) \| Match motor winding type |
> **Pro tip:** Sulzer's Pump Advisor digital service platform enables remote condition monitoring of Sulzer pumps via IIoT sensors. Retrofit kits are available for older pump installations — real-time vibration and temperature data can predict failures weeks before they occur.
