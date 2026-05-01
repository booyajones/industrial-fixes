---
title: "Schneider Altivar 320 Fault Code Guide — Complete Diagnostic Reference"
description: "Complete guide to Schneider Electric Altivar 320 VFD fault codes, causes, and step-by-step repair procedures for industrial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - schneider
  - industrial
---

## Schneider Altivar 320 Fault Codes — What They Mean

The Schneider Electric Altivar 320 (ATV320) is a variable speed drive for simple machine applications — conveyors, compressors, mixers, and hoists. It is the successor to the Altivar 312 and shares its compact format and ease-of-use design. The ATV320 displays fault codes as alphanumeric strings on its integrated display (or on the optional SoMove software via USB or Bluetooth). Fault codes appear in the format of short text strings — different from the F-number format used by Siemens or Danfoss.

[Jump to Fix](#fix)

## Schneider ATV320 Fault Code Reference

| Code | Fault |
|---|---|
| OCF | Overcurrent fault |
| OBF | Overbraking / DC bus overvoltage during deceleration |
| OSF | Overspeed fault — motor running above maximum frequency |
| PHF | Input phase loss |
| SCF1 | Output phase short circuit — motor phases shorted |
| SCF3 | Ground short circuit on motor output |
| OHF | Drive overtemperature |
| OLF | Motor thermal overload |
| ULF | Underload fault — motor current below minimum threshold |
| EEF1 | EEPROM fault — control board memory |
| CFF | Configuration factory reset fault |
| INF | Internal hardware fault |
| SLF1 | Modbus communication loss |
| CAF | CAN bus communication loss |
| LFF1 | Loss of 4–20mA feedback signal (AI1 input) |

## Common Causes by Code

- **OCF — Overcurrent** — Load too heavy for drive sizing, acceleration ramp too short, or output phase fault. Check parameter ACC (acceleration ramp time) and the mechanical load condition.
- **OBF — Overbraking** — Deceleration too fast for the load inertia. Increase the deceleration time (DEC parameter). If quick stops are required, a braking resistor must be added to the ATV320.
- **PHF — Phase loss** — One of the three input supply phases is missing or has fallen below 190V. Check input fuses and contactor contacts upstream of the drive. The ATV320 does not operate on single-phase input — all three phases must be present.
- **OHF — Overtemperature** — The ATV320 has a built-in cooling fan that activates at a set temperature threshold. If the fan fails, or if ambient temperature exceeds 50°C (122°F), OHF triggers. Check that the drive is not mounted near heat sources.
- **LFF1 — 4–20mA loss** — The analog input 1 signal has fallen below the minimum threshold (typically 2mA). Check the PLC output card, the cable, and the connections at the AI1 terminal. Also verify the sensor or transducer powering the signal is operational.
- **ULF — Underload** — The motor is running below the minimum current threshold — indicating the load has disconnected (broken coupling, broken belt, or open damper). Use ULF to detect pump or fan faults.

## Step-by-Step Fix {#fix}

1. **Read the display** — The ATV320 integrated display shows the fault code. Press the ENTER button to see more fault detail. Fault history is stored in parameter F409 (via SoMove or the drive menu).
2. **For OCF (overcurrent)** — Disconnect the motor and test run the drive in no-load mode. If OCF persists without the motor, the fault is internal to the drive. If OCF clears without the motor, the issue is in the motor or load.
3. **For OBF (overbraking)** — Increase the DEC parameter by 50% increments until OBF no longer triggers. If quick deceleration is required by the application, install a Schneider ATV320 braking resistor module.
4. **For PHF (phase loss)** — Measure all three input voltages at the drive terminals (L1, L2, L3) with the drive powered. Unbalanced voltage above 2% between phases causes intermittent PHF faults even when all three phases are present.
5. **For LFF1 (4–20mA loss)** — Verify the analog signal at AI1 using a milliammeter in series. If the signal is present at the field sensor but absent at the drive terminal, check the cable for breaks. If the signal is absent at the sensor, the sensor has failed.

## Parts Often Needed

| Part | Notes |
|---|---|
| Braking resistor | [Amazon](https://www.amazon.com/s?k=Braking+resistor&tag=errorcodefixes-20) \| External; required for fast deceleration on high-inertia loads |
| ATV320 replacement drive | [Amazon](https://www.amazon.com/s?k=ATV320+replacement+drive&tag=errorcodefixes-20) \| For INF or persistent hardware faults |
| SoMove configuration cable | [Amazon](https://www.amazon.com/s?k=SoMove+configuration+cable&tag=errorcodefixes-20) \| USB-to-RJ45 for parameter access and diagnostics |
| Input fuses | [Amazon](https://www.amazon.com/s?k=Input+fuses&tag=errorcodefixes-20) \| Semiconductor fuses rated for the drive input current |
| Analog sensor | [Amazon](https://www.amazon.com/s?k=Analog+sensor&tag=errorcodefixes-20) \| For LFF1; check sensor supply and output |
## When to Call a Pro

Schneider Electric's SoMove software provides remote monitoring and parameter management for ATV320 drives via USB or Bluetooth. For INF (internal hardware fault) or EEF1 faults that recur after power cycling, contact Schneider Electric technical support or a Schneider Service Partner. Many ATV320 faults can be diagnosed remotely using SoMove before dispatching a technician.
