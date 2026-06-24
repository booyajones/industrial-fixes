---
title: "Danfoss FC302 AL-71 Fault - Causes & Fix"
description: "AL-71 (PTC 1 safe stop) means the drive's Safe Torque Off input triggered via a PTC sensor or safety circuit. Most often loose STO wiring."
pubDatetime: 2026-06-22T10:23:36Z
modDatetime: 2026-06-22T10:23:36Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control Card (I/O PCB)"
most_likely_cause: "Loose or broken STO wiring at terminals 19/20"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check that all emergency stops and selector switches in the STO loop are in the closed (normal) position"
  - "Verify continuity between terminals 19 and 20 with power off"
  - "Cycle power to the drive after clearing any external interlock condition"
no_buy_pct: "65%"
---

## Danfoss FC302 AL-71 Fault — What It Means

Alarm 71 (PTC 1 safe stop) on a Danfoss FC302 VFD indicates that the drive has received a Safe Torque Off (STO) signal from an external PTC (Positive Temperature Coefficient) temperature sensor or a safety circuit connected to the drive's STO input. The drive immediately stops and locks out motor output to prevent unsafe operation. This is a protection logic stop, not a thermal overload or damage fault. The drive will not restart until the STO condition is cleared and power is reset or the input is re-enabled.

The STO input is typically connected to terminals 19 and 20 or configured in parameter group 16-xx for safety interlocks. The fault is distinct from overtemperature alarms and is designed to enforce a safe, non-restartable stop when the PTC sensor detects motor winding overheating or when an external safety circuit (emergency stop, selector switch, or interlock) opens the STO loop.

## Before You Replace Anything

Technicians sometimes replace the control card first, but most AL-71 faults are caused by loose wiring, tripped PTC sensors, or open safety interlocks. Check all external wiring and interlocks before ordering a new I/O PCB.

[Jump to Fix](#fix)

## Common Causes

- **Loose or broken STO wiring (~35%)** A disconnected, corroded, or broken wire at terminals 19/20 (or configured STO terminals) breaks the Safe Torque Off loop and triggers the alarm.
- **External PTC sensor activated (~30%)** A motor winding temperature sensor (PTC type) detected overheating and opened the circuit, signaling STO to the drive.
- **Safety interlock or emergency stop open (~20%)** A safety interlock, emergency stop, or selector switch in the STO loop is not closed, triggering the safe stop.
- **Incorrect parameter configuration (~10%)** Safety interlock or STO input not properly enabled or mapped in parameters (group 16-xx) causes false activation.
- **Faulty control card or STO input circuit (~5%)** Internal failure of the control PCB's STO detection circuit, even when external wiring is intact.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all emergency stops and selector switches in the closed (normal) position?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety interlocks are not the issue. Proceed to check wiring at terminals 19 and 20.<br><strong>No:</strong> Close all safety switches and reset the drive. If the alarm clears, the interlock was the cause. If it remains, check wiring.</div>
</details>

<details class="dtree"><summary>With power off, does a continuity test show a closed circuit between terminals 19 and 20?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is intact. Check motor temperature and PTC sensor, or test the control card.<br><strong>No:</strong> Open circuit detected. Inspect and repair wiring, tighten connections, or replace corroded wires.</div>
</details>

<details class="dtree"><summary>Is the motor temperature above its rated limit or are motor winding readings below 2 megohms?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor overheating or insulation failure triggered the PTC sensor. Allow cooling, reduce load, or inspect motor windings.<br><strong>No:</strong> Motor is fine. The fault is likely incorrect parameter settings or a faulty control card.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** and lock out the disconnect to work safely.
2. **Check all emergency stops and selector switches** in the STO loop to confirm they are in the closed (normal) position.
3. **Inspect STO wiring** at terminals 19 and 20 (or configured STO terminals). Use a multimeter to verify continuity. Tighten all connections and replace corroded or broken wires.
4. **Test motor temperature and PTC sensor** if present. Perform a megohm test on motor windings: readings below 2 megohms indicate insulation failure or overheating. Allow motor to cool if above rated temperature.
5. **Verify parameters in group 16-xx** (such as 16-70 STO function) to confirm the STO input is correctly enabled and mapped. Check motor data in parameters 1-20 through 1-25, especially nominal motor current (1-24).
6. **Place a jumper between terminal 12 (24 VDC)** and the digital input programmed as STO to test if the alarm clears. If it does, the external circuit is the issue.
7. **Cycle power to the drive** after making corrections. If Alarm 71 persists despite correct wiring, interlocks, and parameters, replace the control card (I/O PCB).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control Card (I/O PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-71-fault-code&k=Danfoss+FC302+Control+Card+%28I%2FO+PCB%29&tag=errorcodefixes-20) \| Only if wiring, interlocks, and parameters are verified correct and the STO input circuit has failed internally. |
| PTC Temperature Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-71-fault-code&k=PTC+Temperature+Sensor&tag=errorcodefixes-20) \| If motor winding sensor is confirmed faulty or damaged. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in variable frequency drive troubleshooting, motor thermal testing, or high-voltage DC bus work. This fault involves safety interlocks and Safe Torque Off circuits that are part of machinery safety systems. Incorrect diagnosis can lead to unsafe restarts or machinery damage. A pro has the proper test equipment (megohm testers, programming software like Danfoss MCT) and experience with parameter configuration in group 16-xx. If the control card needs replacement or motor insulation has failed, a technician should perform the repair and validate the drive operates safely under load.

**Rough cost:** A pro service call runs about $150-400.
