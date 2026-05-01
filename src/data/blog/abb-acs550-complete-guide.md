---
title: "ABB ACS550 Complete Fault Code Guide — All Faults and Fixes"
description: "Complete fault code guide for the ABB ACS550 variable frequency drive, covering all fault and alarm codes, causes, and step-by-step troubleshooting."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
  - industrial
---

## ABB ACS550 Complete Fault Code Guide

The ABB ACS550 is a wall-mount general-purpose variable frequency drive rated from 1 to 550 HP (0.75–355 kW). It displays fault and alarm codes on the built-in basic panel (or optional assistant control panel) as an "Fxxx" or "Axxx" code followed by a description. Faults require reset; alarms are warnings that do not stop the drive.

[Jump to Fix](#fix)

## ABB ACS550 Fault Codes (Fxxx)

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixes-20) | Meaning |
|-------|---------|
| [F0001](https://www.amazon.com/s?k=F0001&tag=errorcodefixes-20) | Overcurrent — motor phase current too high |
| [F0002](https://www.amazon.com/s?k=F0002&tag=errorcodefixes-20) | DC overvoltage — DC bus voltage too high |
| [F0003](https://www.amazon.com/s?k=F0003&tag=errorcodefixes-20) | Device temperature — heatsink overtemperature |
| [F0005](https://www.amazon.com/s?k=F0005&tag=errorcodefixes-20) | DC undervoltage — supply voltage too low |
| [F0006](https://www.amazon.com/s?k=F0006&tag=errorcodefixes-20) | DC link fault |
| [F0007](https://www.amazon.com/s?k=F0007&tag=errorcodefixes-20) | AI1 loss — analog input 1 signal lost |
| [F0009](https://www.amazon.com/s?k=F0009&tag=errorcodefixes-20) | Underload — motor drawing less current than expected |
| [F0010](https://www.amazon.com/s?k=F0010&tag=errorcodefixes-20) | Panel loss — control panel communication lost |
| [F0013](https://www.amazon.com/s?k=F0013&tag=errorcodefixes-20) | Ext fault 1 — external fault input active |
| [F0021](https://www.amazon.com/s?k=F0021&tag=errorcodefixes-20) | IGBT fault — drive output bridge fault |
| [F0023](https://www.amazon.com/s?k=F0023&tag=errorcodefixes-20) | Earth fault (ground fault) — motor phase to ground |
| [F0029](https://www.amazon.com/s?k=F0029&tag=errorcodefixes-20) | Motor phase loss — one output phase missing |
| [F0030](https://www.amazon.com/s?k=F0030&tag=errorcodefixes-20) | Motor stall — motor drawing high current at low speed |
| [F0035](https://www.amazon.com/s?k=F0035&tag=errorcodefixes-20) | Safe torque off (STO) — safety input activated |
| [F0041](https://www.amazon.com/s?k=F0041&tag=errorcodefixes-20) | Thermistor fault — motor thermistor overtemp |
| [F0065](https://www.amazon.com/s?k=F0065&tag=errorcodefixes-20) | Motor speed feedback fault |
| [F0070](https://www.amazon.com/s?k=F0070&tag=errorcodefixes-20) | Fieldbus communication fault |
| [F0121](https://www.amazon.com/s?k=F0121&tag=errorcodefixes-20) | Motor overload (I2t) — thermal model overload |
| [F0130](https://www.amazon.com/s?k=F0130&tag=errorcodefixes-20) | Control board fault |

## ABB ACS550 Alarm Codes (Axxx)

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixes-20) | Meaning |
|-------|---------|
| [A2010](https://www.amazon.com/s?k=A2010&tag=errorcodefixes-20) | Overcurrent warning |
| [A2011](https://www.amazon.com/s?k=A2011&tag=errorcodefixes-20) | DC bus overvoltage warning |
| [A2013](https://www.amazon.com/s?k=A2013&tag=errorcodefixes-20) | Device temperature warning (heatsink) |
| [A2023](https://www.amazon.com/s?k=A2023&tag=errorcodefixes-20) | Earth fault warning |
| [A5010](https://www.amazon.com/s?k=A5010&tag=errorcodefixes-20) | AI1 signal lost (warning) |
| [A5030](https://www.amazon.com/s?k=A5030&tag=errorcodefixes-20) | Panel communication lost (warning) |
| [A8110](https://www.amazon.com/s?k=A8110&tag=errorcodefixes-20) | Motor overload warning |

## Common Causes by Fault Code

- **F0001 — Overcurrent** — Acceleration ramp too steep, mechanical overload on the motor, motor cable fault, or short circuit in output wiring. Check motor and cable for shorts (resistance to ground) before resetting. Adjust acceleration time in parameter 22.01.
- **F0002 — DC overvoltage** — Input supply voltage too high, or deceleration ramp too fast (regenerative energy building up DC bus). Add a braking resistor if frequent deceleration overvoltage occurs. Adjust deceleration ramp in parameter 23.01.
- **F0003 — Temperature** — Cooling fan blocked, dirty heatsink, high ambient temperature, or overloaded drive. Check the cooling fan is spinning and the ventilation openings are clear. On wall-mount ACS550, the fan is internal and replaceable.
- **F0005 — DC undervoltage** — Input supply voltage below minimum for drive rating. Caused by a phase loss on the input (check all three input phases at the drive terminal block), blown input fuses, or a weak supply.
- **F0021 — IGBT fault** — A gate drive or output IGBT has failed. This usually requires drive replacement or repair. First check for motor or cable short circuit — a cable fault can destroy an IGBT.
- **F0023 — Earth fault** — One or more motor phases is shorted to ground. Disconnect the motor cables at the drive output terminals and measure each phase to ground with a megohmmeter. Normal reading is >1 MΩ.
- **F0030 — Motor stall** — Motor current is high but speed is low — the motor is stalled mechanically. Check the driven load for a jam or seized bearing. Increase stall protection time in parameter 30.10 if false trips occur at startup.
- **F0041 — Thermistor** — Motor thermistor (PTC) has signaled high motor temperature. Check the motor ventilation and cooling. If the motor is cool but the fault persists, check thermistor continuity and the parameter 30.04 thermistor enable setting.
- **F0070 — Fieldbus** — Communication to the fieldbus module (PROFIBUS, Modbus, etc.) has been lost. Check the fieldbus cable connections and confirm the master device (PLC) is online.

## Step-by-Step Fix {#fix}

1. **Read the fault code** — The ACS550 basic panel displays "FAULT" and the fault code. Use the arrow keys to see the fault description and the fault history (parameter 04.01–04.10).
2. **For F0001 (overcurrent)** — Disconnect motor cables at drive output. Measure resistance between phases and from each phase to ground. Normal phase-to-phase: 0.5–5 Ω (motor winding resistance). Any reading below 1 kΩ to ground indicates a fault.
3. **For F0002 (DC overvoltage)** — Increase the deceleration time (parameter 23.01). If the load has high inertia, consider a braking resistor and brake chopper.
4. **For F0003 (temperature)** — Check the cooling fan — it should spin when the drive is powered on. Blow out heatsink fins with compressed air (from outside in). Verify ambient temperature is below the drive rating.
5. **For F0023 (earth fault)** — Isolate the motor from the drive. Use a 500V megohmmeter on each phase to ground. Replace motor cable if insulation is compromised.
6. **For F0005 (undervoltage)** — Measure all three input phases at the drive L1/L2/L3 terminals under load. If one phase is low, check the supply fuses and contactor.
7. **Reset** — Press RESET on the control panel after correcting the fault. Check fault history (parameter 04.01) for repeat occurrences.

## Parameters Commonly Modified

| [Parameter](https://www.amazon.com/s?k=Parameter&tag=errorcodefixes-20) | Description |
|-----------|-------------|
| [22.01](https://www.amazon.com/s?k=22.01&tag=errorcodefixes-20) | Acceleration time 1 |
| [23.01](https://www.amazon.com/s?k=23.01&tag=errorcodefixes-20) | Deceleration time 1 |
| [30.04](https://www.amazon.com/s?k=30.04&tag=errorcodefixes-20) | Motor thermistor enable |
| [30.10](https://www.amazon.com/s?k=30.10&tag=errorcodefixes-20) | Stall detection time |
| [40.01](https://www.amazon.com/s?k=40.01&tag=errorcodefixes-20) | Fieldbus enable |

## When to Call a Pro

F0021 (IGBT fault) and F0130 (control board fault) typically require factory service or drive replacement. ABB's ACS550 can often be repaired by ABB service centers more cost-effectively than replacement for large HP ratings. For IGBT faults, always inspect the motor and cables first — replacing an IGBT into a shorted motor destroys the new IGBT immediately.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
