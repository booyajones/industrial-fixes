---
title: "Yaskawa A1000 Complete Guide - Fault Codes, Parameters, and Commissioning"
description: "Complete guide to the Yaskawa A1000 AC drive: full fault code reference, key parameters, commissioning procedure, and troubleshooting for all common faults including OC, OV, UV1, and GF."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Yaskawa A1000 is one of the most capable mid-range AC drives available — a full-featured vector-control drive that handles everything from simple V/f applications to full closed-loop flux vector control with encoder feedback. Its fault code system is comprehensive and well-documented, making diagnosis straightforward when you know how to use the drive's built-in diagnostics. This guide covers the complete fault code reference, the key parameters you need to know, and a step-by-step commissioning procedure.

## What Does Yaskawa A1000 Fault Data Mean?

The A1000 displays fault codes on its digital operator (keypad). Navigate to the fault history via **U2-01** (current fault) and **U2-02 through U2-10** (fault history). Each fault entry also logs the output frequency, current, voltage, and drive status at the time of fault.

### Overcurrent and Short Circuit Faults

| Code | Name | Common Cause |
|------|------|-------------|
| OC | Overcurrent | Acceleration too fast, motor short, mechanical jam |
| SCA | Overcurrent (during stop) | Output short circuit, IGBT failure |
| GF | Ground Fault | Motor winding or cable insulation failure |
| SC | Short Circuit | Direct output phase short |
| OCA | Overcurrent (during acceleration) | Ramp time too short |
| OCD | Overcurrent (during deceleration) | Load regeneration exceeding DC bus capacity |
| OCR | Overcurrent (during constant speed) | Sudden load spike, mechanical fault |

### Overvoltage and Undervoltage

| Code | Name | Common Cause |
|------|------|-------------|
| OV | DC Bus Overvoltage | Fast deceleration, regenerative load, high input voltage |
| UV1 | DC Bus Undervoltage | Low input voltage, power dip, blown input fuse |
| UV2 | Control Power Undervoltage | Internal control supply failure |
| UV3 | Soft Charge Circuit Fault | Pre-charge relay not closing |
| PF | Input Phase Loss | Missing input phase, blown fuse |

### Motor and Thermal Faults

| Code | Name | Common Cause |
|------|------|-------------|
| oL1 | Motor Overload (electronic thermal) | Motor running above rated load continuously |
| oL2 | Drive Overload | Drive running above rated current continuously |
| oH1 | Drive Overheat | Insufficient cooling, blocked heatsink |
| oH2 | Motor Overheat (thermistor) | Motor PTC/NTC thermistor tripped |
| OH3 | Motor Overheat (oL1 pre-alarm) | Motor approaching thermal limit |

### Communication and Encoder Faults

| Code | Name | Common Cause |
|------|------|-------------|
| bUS | Communication Error | MEMOBUS/Modbus timeout, loose RS-485 wiring |
| CE | MEMOBUS/Modbus Communication Error | PLC stopped communicating, wiring fault |
| EF0 | External Fault (terminal S1) | External safety circuit opened |
| EF1–EF8 | External Fault (terminals S1–S8) | External fault input activated |
| dEv | Speed Deviation | Encoder fault, mechanical slip in closed-loop mode |
| PGo | Encoder Open Circuit | Encoder cable disconnected or broken |

### Safety and Other Faults

| Code | Name | Common Cause |
|------|------|-------------|
| SEr | EEPROM Write Error | Parameter save failure |
| CPF00 | EEPROM Error | Control board fault |
| CPF02 | A/D Converter Fault | Control board fault |
| Err | EEPROM Error | Corrupted parameter memory |
| STP | Safety Circuit Fault | Safe Torque Off (STO) circuit open |
| LF | Output Phase Loss | Missing motor phase, blown motor lead |

## Key Parameters

Understanding these parameter groups is essential for A1000 commissioning and fault diagnosis.

### Motor Setup (Parameter Group E)

| Parameter | Function | Typical Setting |
|-----------|---------|----------------|
| E1-01 | Input voltage (V) | Match supply voltage |
| E2-01 | Motor rated current (A) | Motor nameplate FLA |
| E2-02 | Motor rated slip (Hz) | Calculate from nameplate |
| E2-03 | Motor no-load current (A) | Typically 30–50% of E2-01 |
| E2-04 | Motor poles | 4 for 1800 RPM, 6 for 1200 RPM |
| E2-05 | Motor rated power factor | Motor nameplate cos φ |

### Acceleration and Deceleration (Parameter Group C)

| Parameter | Function |
|-----------|---------|
| C1-01 | Acceleration Time 1 (seconds) |
| C1-02 | Deceleration Time 1 (seconds) |
| C1-03 | Acceleration Time 2 |
| C1-04 | Deceleration Time 2 |
| C6-01 | Drive duty cycle (Heavy Duty vs. Normal Duty) |

### Protection Parameters (Parameter Group L)

| Parameter | Function |
|-----------|---------|
| L1-01 | Motor protection selection (electronic thermal) |
| L1-02 | Motor overload protection time constant |
| L2-01 | Momentary power loss ride-through enable |
| L3-01 | Acceleration stall prevention enable |
| L3-02 | Deceleration stall prevention enable |
| L5-01 | Number of auto restart attempts |
| L5-02 | Auto restart fault list |

### Reference and Speed Control (Parameter Group d)

| Parameter | Function |
|-----------|---------|
| d1-01 | Frequency reference 1 |
| d1-17 | Jog frequency |
| d2-01 | Frequency reference upper limit |
| d2-02 | Frequency reference lower limit |

## How to Fix It

**Step 1: Pre-Power Inspection**

Before applying power:
- Verify input voltage matches drive nameplate (200V class or 400V class).
- Verify motor voltage matches the selected V/f pattern.
- Verify output cable connections at U, V, W terminals and motor terminal box — check phase rotation if motor direction matters.
- Verify grounding: drive PE terminal to building ground, motor frame to drive PE.
- Check that all terminal screws are torqued to spec (see hardware manual for terminal torque specs).
- Verify no output cable is connected to input terminals.

**Step 2: Initial Power-Up and Parameter Initialization**

- Apply power to the A1000. The digital operator displays "HAND OFF AUTO" or the frequency reference.
- If starting fresh, initialize to factory defaults: **A1-03 = 2220** (2-wire initialization) or **A1-03 = 3330** (3-wire initialization). Press ENTER and confirm.
- Set the control mode: **A1-02** = 0 (V/f), 1 (V/f with encoder), 2 (Open-loop vector), 3 (Closed-loop vector), 5 (Open-loop vector 2).

**Step 3: Enter Motor Nameplate Data**

Navigate to parameter group E2 and enter:
- E2-01: Motor rated current (A) — from nameplate "FLA" or "A"
- E2-04: Number of motor poles — 2 for 3600 RPM, 4 for 1800 RPM, 6 for 1200 RPM
- E2-05: Motor rated power factor
- E1-01: Input voltage
- E1-03: V/f pattern selection (01 = 60 Hz, 00 = 50 Hz, or custom)

**Step 4: Run Auto-Tuning**

For Open-Loop Vector (A1-02 = 2) or Closed-Loop Vector (A1-02 = 3) modes, run rotational auto-tuning:
- **T1-01 = 0** (Rotational Auto-Tuning) — requires motor to be uncoupled from load
- **T1-02** = Motor rated power (kW)
- **T1-03** = Motor rated voltage
- **T1-04** = Motor rated frequency (Hz)
- **T1-05** = Motor rated speed (RPM)
- **T1-06** = Motor rated current (A)
- **T1-07** = Motor poles

Press RUN on the digital operator to start auto-tuning. The motor rotates slowly during this process. Auto-tuning takes 30–90 seconds and writes measured values back to E2 parameters.

For applications where load cannot be disconnected, use **T1-01 = 2** (Stationary Auto-Tuning) which measures resistance and inductance without rotating the motor.

**Step 5: Set Acceleration/Deceleration Times**

- **C1-01:** Acceleration time 1 — start at 10 seconds for general loads, increase for high-inertia loads.
- **C1-02:** Deceleration time 1 — for drives without a braking resistor, set to the minimum time that doesn't trigger OV fault.
- Enable deceleration stall prevention (**L3-04 = 1**) if OV faults occur during deceleration.

**Step 6: Configure Speed Reference**

- **b1-01 = 1:** Frequency reference from analog input (0–10V or 4–20mA at terminal A1 or A2).
- **b1-01 = 0:** Frequency reference from digital operator.
- **b1-02:** Run command source (1 = digital input terminals, 0 = digital operator).

**Step 7: Configure Motor Protection**

- **L1-01 = 1:** Enable electronic thermal protection.
- **L1-02:** Set overload time constant — typically 9 minutes for standard motors, 2 minutes for inverter-duty motors with forced cooling.

**Step 8: Test Run**

- Start with a low frequency reference (10–15 Hz) and verify motor rotation direction.
- If direction is wrong, swap any two output terminals (U↔V or V↔W) at the drive or motor.
- Increase to full speed and monitor output current in monitor U1-03. Compare to motor nameplate FLA.
- Monitor heatsink temperature in U4-06 during extended operation.

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| Yaskawa A1000 Digital Operator (JOG) | Replace failed keypad / display | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-complete-guide&k=Yaskawa+A1000+digital+operator+keypad&tag=errorcodefixes-20) |
| Megohmmeter Insulation Tester | Test motor windings before commissioning | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-complete-guide&k=megohmmeter+motor+winding+tester&tag=errorcodefixes-20) |
| Yaskawa A1000 Braking Resistor | Prevent OV faults on regenerative loads | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-complete-guide&k=Yaskawa+A1000+braking+resistor&tag=errorcodefixes-20) |
| RS-485 to USB Converter Cable | Connect A1000 to PC for DriveWizard | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-complete-guide&k=RS-485+to+USB+converter+cable&tag=errorcodefixes-20) |
| Shielded Control Cable (18 AWG) | Reduce noise on analog reference inputs | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-complete-guide&k=shielded+control+cable+18+awg+VFD&tag=errorcodefixes-20) |

## When to Call a Pro

- **CPF faults (control board errors):** CPF00, CPF02, CPF20 indicate control board hardware failure. Send the drive to a Yaskawa repair center.
- **OC at startup with known good motor:** If insulation tests pass and OC persists, the drive's IGBT module may have failed. Requires power module replacement.
- **Encoder (PGo, dEv) faults in closed-loop mode:** Closed-loop vector commissioning requires careful encoder wiring and parameter tuning. Contact Yaskawa application engineering for complex applications.

## FAQ

**Q: What's the difference between OC and OCA on the Yaskawa A1000?**

A: OCA is "Overcurrent during Acceleration" — the drive detected overcurrent specifically while the output frequency was ramping up. This helps you pinpoint the cause: the acceleration ramp time is too short for the load inertia. Increase C1-01. OC without a suffix means overcurrent occurred during constant speed operation, pointing to a sudden load spike or mechanical fault.

**Q: How do I clear a fault on the Yaskawa A1000?**

A: Press the RESET key on the digital operator after addressing the root cause. Alternatively, close and open a digital input configured as fault reset (H1-xx = 14). Via Modbus, write bit 4 of the command word to clear faults.

**Q: My A1000 shows UV1 on power-up, but the supply voltage is correct. What's wrong?**

A: UV1 that clears after a few seconds is often normal — the DC bus charging through the pre-charge resistors takes a moment to reach operating voltage. If UV1 persists or appears randomly during operation, check: input fuse condition, input line voltage under load (not just at the panel), and pre-charge relay operation (UV3 would indicate pre-charge circuit specifically).

**Q: How long is the Yaskawa A1000 warranty?**

A: Standard Yaskawa A1000 warranty is 2 years from date of manufacture (not date of installation). Extended warranty options are available through Yaskawa distributors. Register your drive at Yaskawa's website to activate and track warranty coverage.

## See Also

- [Yaskawa VFD Fault ER — Causes & Fix](/posts/yaskawa-vfd-fault-er/)
- [Yaskawa VFD Fault PF — Causes & Fix](/posts/yaskawa-vfd-fault-pf/)
- [Yaskawa VFD Fault BB — Causes & Fix](/posts/yaskawa-vfd-fault-bb/)
- [Yaskawa V1000 OC Fault — Overcurrent](/posts/yaskawa-v1000-fault-oc/)
