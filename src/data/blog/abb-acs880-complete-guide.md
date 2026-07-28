---
title: "ABB ACS880 Complete Fault Code Guide — All Faults and Fixes"
description: "Complete fault code guide for the ABB ACS880 industrial drive, covering common fault codes, causes, and step-by-step troubleshooting for all drive sizes."
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

## ABB ACS880 Complete Fault Code Guide

The ABB ACS880 is a high-performance industrial drive designed for demanding applications including cranes, extruders, winders, and complex motion control. It uses ABB's Direct Torque Control (DTC) algorithm and supports PROFIBUS, PROFINET, EtherNet/IP, and other fieldbus protocols. Faults are displayed on the ACS-AP-I or ACS-AP-S control panel as "Fxxx" codes with description text.

## ABB ACS880 Common Fault Codes

| Fault | Meaning |
|-------|---------|
| 2310 | Overcurrent — motor current exceeded limit |
| 2321 | Earth fault (ground fault) |
| 2330 | Short circuit — output phase-to-phase short |
| 3130 | Input phase loss — one input phase missing |
| 3210 | DC overvoltage |
| 3220 | DC undervoltage |
| 4110 | Control board temperature too high |
| 5010 | Fan fault — cooling fan failed |
| 5090 | Motor connection or cable fault |
| 6100 | FPGA fault — drive logic fault |
| 6310 | Fieldbus communication fault |
| 7010 | Motor stall |
| 7011 | Motor overload (thermal model) |
| 7012 | Motor underload |
| 9300 | External fault (via digital input or fieldbus) |
| FA81 | Safe Torque Off (STO) active |

## ABB ACS880 Alarm Codes (Warnings)

| Alarm | Meaning |
|-------|---------|
| A2310 | Overcurrent warning |
| A3130 | Input phase loss warning |
| A3210 | DC overvoltage warning |
| A4110 | Drive temperature warning |
| A7011 | Motor thermal overload warning |
| A9300 | External fault warning |

## Common Causes by Fault Code

- **2310 — Overcurrent** — Aggressive acceleration, mechanical overload, short circuit in the motor cable, or incorrect motor data entered in parameters. On ACS880, DTC requires accurate motor nameplate data (Group 99 parameters) to properly calculate current limits — incorrect motor data causes overcurrent faults during acceleration.
- **2321 — Earth fault** — Motor winding or cable insulation failure. The ACS880 uses a sensitive earth fault detector — even a partial insulation failure can trigger 2321. Measure insulation resistance with a megohmmeter at 500V or 1000V depending on motor rating.
- **3130 — Input phase loss** — One of the three input supply phases is missing or has low voltage. This is a serious fault — running single-phase can cause DC bus voltage ripple that stresses the drive capacitors. Check all input fuses and the supply contactor.
- **3210 — DC overvoltage** — Braking energy from the load is exceeding the drive's ability to dissipate it. Add a braking resistor and chopper if the load has high inertia (cranes, conveyors). Alternatively, extend the deceleration ramp time.
- **4110 — Board temperature** — The ACS880 control board temperature has exceeded the limit. Check the drive cabinet cooling — the ACS880 requires specific minimum airflow through the cabinet. Confirm the cabinet door is closed and the cooling fans are operating.
- **5010 — Fan fault** — The ACS880 cooling fan has failed. The drive has a diagnostic mode that monitors fan current — check parameter 05.05 for fan speed and current. Fan replacement on ACS880 is a routine maintenance item; average fan life is 50,000–60,000 hours.
- **7010 — Motor stall** — Motor is mechanically stalled. Check the driven equipment for a jam, seized bearing, or mechanical overload. ACS880 stall detection is configurable — adjust parameters 30.11–30.14.
- **FA81 — STO** — Safe Torque Off is active via the STO1 or STO2 terminals. Confirm the STO safety circuit is not open. Check the safety relay, E-stop device, or safety PLC output connected to the STO terminals.

## Step-by-Step Fix {#fix}

1. **Read the fault** — On the ACS-AP-I panel, navigate to the Fault Logger (Main menu > Diagnostics > Fault logger) to see the fault code, timestamp, and drive state at the time of fault.
2. **For 2310 (overcurrent)** — Check Group 99 motor data parameters. Confirm rated current, voltage, frequency, and speed match the motor nameplate. Adjust acceleration time (parameter 23.11). Inspect motor cable for shorts.
3. **For 2321 (earth fault)** — Disconnect motor cables at the drive output. Use a megohmmeter at 500V (or 1000V for medium voltage). Check each phase: Phase-to-Phase should be <10 Ω (winding resistance). Phase-to-ground should be >1 MΩ.
4. **For 3130 (phase loss)** — Measure all three input phases at L1, L2, L3 terminals under load. Check supply fuses and supply contactor contact condition. On cabinet drives, check the input busbar connections.
5. **For 3210 (DC overvoltage)** — Extend deceleration time in parameter 23.12. If frequent occurrence, add braking resistor — calculate resistance value from ABB's selection guide for the ACS880 frame size.
6. **For FA81 (STO)** — Trace the STO circuit. On the ACS880, STO1 and STO2 must both have 24VDC applied for the drive to enable. If either is open (0V), the drive is STO-active. Check E-stops, safety relays, and interlocks.
7. **Reset** — Press RESET on the control panel or issue a reset via fieldbus command. Check Fault Logger for recurrence.

## Key Parameter Groups

| [Group](https://www.amazon.com/s?ascsubtag=ecf-abb-acs880-complete-guide&k=Group&tag=errorcodefixes-20) | Description |
|-------|-------------|
| 04 | Warnings and faults |
| 05 | I/O and hardware diagnostics |
| 23 | Speed ramp |
| 30 | Motor protection |
| 35 | Motor thermal protection |
| 99 | Motor data |

## When to Call a Pro

ABB ACS880 is a high-performance drive used in critical industrial applications. Fault 6100 (FPGA fault) requires factory service. Before condemning a drive for 2310 or 2321, always verify the motor and cable first — replacing a drive into a failed motor or shorted cable will destroy the new drive. ABB has a global service network; contact your local ABB sales office for repair support.
