---
title: "Siemens G120C VFD Fault Code Guide — Complete Diagnostic Reference"
description: "Complete guide to Siemens SINAMICS G120C compact VFD fault codes, causes, and step-by-step repair procedures for industrial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - siemens
  - industrial
---

## Siemens G120C VFD Fault Codes — What They Mean

The Siemens SINAMICS G120C is a compact variable frequency drive in the G120 product family. The G120C integrates the Control Unit and Power Module into a single compact housing, making it ideal for space-constrained panel installations in pumps, fans, and simple conveyor applications. It uses the same SINAMICS fault code structure as the G120 modular series — faults are prefixed with "F" and alarms with "A." Codes are displayed on the Basic Operator Panel (BOP-2) or the Intelligent Operator Panel (IOP).

[Jump to Fix](#fix)

## Siemens G120C Common Fault Code Reference

| [Fault Code](https://www.amazon.com/s?k=Fault%20Code&tag=errorcodefixe-20) | Description |
|---|---|
| [F00001](https://www.amazon.com/s?k=F00001&tag=errorcodefixe-20) | Overcurrent — drive output current exceeded limit |
| [F00002](https://www.amazon.com/s?k=F00002&tag=errorcodefixe-20) | Overvoltage — DC link voltage too high |
| [F00003](https://www.amazon.com/s?k=F00003&tag=errorcodefixe-20) | Undervoltage — DC link voltage too low |
| [F00004](https://www.amazon.com/s?k=F00004&tag=errorcodefixe-20) | Drive overtemperature — heatsink temp exceeded |
| [F00005](https://www.amazon.com/s?k=F00005&tag=errorcodefixe-20) | Drive I²t overload |
| [F00011](https://www.amazon.com/s?k=F00011&tag=errorcodefixe-20) | Motor overtemperature — PTC/NTC sensor |
| [F00021](https://www.amazon.com/s?k=F00021&tag=errorcodefixe-20) | Ground fault detected |
| [F00030](https://www.amazon.com/s?k=F00030&tag=errorcodefixe-20) | Drive hardware fault |
| [F00051](https://www.amazon.com/s?k=F00051&tag=errorcodefixe-20) | EEPROM fault — parameter storage error |
| [F00052](https://www.amazon.com/s?k=F00052&tag=errorcodefixe-20) | Power stack fault |
| [F00070](https://www.amazon.com/s?k=F00070&tag=errorcodefixe-20) | CB30B communication board fault |
| [F00071](https://www.amazon.com/s?k=F00071&tag=errorcodefixe-20) | PROFIBUS/PROFINET communication fault |
| [F00076](https://www.amazon.com/s?k=F00076&tag=errorcodefixe-20) | PID feedback sensor fault |
| [F00090](https://www.amazon.com/s?k=F00090&tag=errorcodefixe-20) | Encoder fault (where encoder is fitted) |
| [F01003](https://www.amazon.com/s?k=F01003&tag=errorcodefixe-20) | Motor phase loss |

## Common Causes by Fault

- **F00001 — Overcurrent** — Mechanical overload on the driven machine (motor stall, jammed pump, conveyor jam), undersized drive for motor, acceleration ramp too short, or motor cable fault. Check the acceleration time parameter (P1120) — too short a ramp causes overcurrent on heavy loads.
- **F00002 — Overvoltage** — Deceleration ramp too short for the inertia of the load, or regenerative energy from a large flywheel load. Increase deceleration time (P1121) or enable the dynamic braking chopper (if equipped).
- **F00003 — Undervoltage** — Supply voltage below 380V (3-phase) or input fuse failure. Check all three input phases — a single blown fuse on one phase causes the DC bus to drop.
- **F00004 — Drive overtemperature** — Blocked or failed cooling fan on the G120C, ambient temperature too high, drive mounted in a sealed enclosure without ventilation. G120C requires minimum 50mm clearance above and below for airflow.
- **F00021 — Ground fault** — A motor winding or cable insulation fault to ground. Disconnect the motor and run the drive without a motor — if F00021 clears, the fault is in the motor or cable. If it persists, the fault is internal to the drive.
- **F00071 — PROFIBUS/PROFINET** — Communication loss between the PLC and the G120C. Check the PROFIBUS address (P0918) matches the PLC configuration. Verify cable connections at the drive's PROFIBUS connector and at the PLC DP port.

## Step-by-Step Fix {#fix}

1. **Read the fault** — The BOP-2 or IOP displays the fault code (e.g., "F00001") and a brief text description. Use the navigation buttons to display more detail. The fault buffer (parameter r0945) stores up to 8 fault codes with timestamps.
2. **For F00001 (overcurrent)** — Check the driven load — try turning it manually. If it won't turn freely, the mechanical issue must be resolved first. Review acceleration time parameter P1120 — increase it by 50% and retry. Also check motor cable for any shorts between conductors.
3. **For F00004 (overtemperature)** — Check the G120C cooling fan (audible when drive is powered). Confirm ambient temperature at the drive location is below 40°C (104°F). Check panel ventilation — drives mounted in sealed panels frequently overheat.
4. **For F00021 (ground fault)** — Disconnect motor cable at the drive terminals. Measure insulation resistance from each motor lead to ground with a 500V megohmmeter — should be greater than 1 MΩ. A reading below 1 MΩ indicates a cable or motor winding fault.
5. **Clear and restart** — After resolving the fault cause, press the FAULT RESET button on the BOP-2 (or use the reset command via PROFIBUS). The G120C does not auto-restart — a reset must be commanded.

## Parts Often Needed

| Part | Notes |
|---|---|
| [G120C internal cooling fan](https://www.amazon.com/s?k=G120C%20internal%20cooling%20fan&tag=errorcodefixe-20) | Replacement fan for thermal fault prevention |
| [BOP-2 operator panel](https://www.amazon.com/s?k=BOP-2%20operator%20panel&tag=errorcodefixe-20) | For local diagnostics and parameter access |
| [PROFIBUS connector](https://www.amazon.com/s?k=PROFIBUS%20connector&tag=errorcodefixe-20) | 9-pin D-sub with built-in EOL resistor |
| [Motor PTC thermistor](https://www.amazon.com/s?k=Motor%20PTC%20thermistor&tag=errorcodefixe-20) | For F00011; check PTC resistance (normal: 100–1000 Ω) |
| [Complete G120C drive](https://www.amazon.com/s?k=Complete%20G120C%20drive&tag=errorcodefixe-20) | For F00030 or F00052 hardware faults |

## When to Call a Pro

Siemens G120C drives can be remotely diagnosed via PROFINET using Siemens STARTER or TIA Portal. If the drive is integrated into a PROFINET network, a Siemens-trained automation technician can view the full fault buffer, drive telemetry, and parameter settings without being physically at the drive. For F00030 (hardware fault), contact Siemens technical support or a Siemens Service Partner.
