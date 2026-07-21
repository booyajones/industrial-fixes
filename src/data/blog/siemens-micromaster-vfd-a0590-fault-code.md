---
title: "Siemens Micromaster VFD A0590 Fault - Causes & Fix"
description: "A0590 on a Siemens Micromaster VFD signals a drive fault. Check your manual for the exact meaning, then inspect connections and parameters."
pubDatetime: 2026-07-19T07:43:39Z
modDatetime: 2026-07-19T07:43:39Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Siemens Micromaster control board"
most_likely_cause: "Parameter configuration mismatch or communication error"
likelihood: "often"
diy_or_pro: "pro"
free_checks:
  - "Check the drive display for additional fault codes or warnings and record them"
  - "Inspect all control and power wiring for loose connections, damaged insulation, or corrosion"
  - "Review the parameter settings against the motor nameplate and application requirements"
---

## Siemens Micromaster VFD A0590 Fault — What It Means

The A0590 fault code on a Siemens Micromaster variable frequency drive indicates the drive has detected an abnormal condition and shut down to protect itself or the connected motor. The exact meaning of A0590 can vary by Micromaster model and firmware version, so you should consult your specific drive's manual or parameter list to decode the precise fault. In general, this family of faults relates to internal drive errors, parameter conflicts, communication issues, or sensor problems. The drive will not restart until the fault is cleared and the underlying cause is resolved.

## Before You Replace Anything

Technicians sometimes replace the entire VFD when the real problem is a wrong parameter setting or a loose communication cable. Always review the fault history and parameter settings in the drive menu before ordering a replacement unit.

[Jump to Fix](#fix)

## Common Causes

- **Parameter setting error (~35%)** Incorrect motor parameters, ramp times, or control mode settings can trigger internal faults when the drive attempts to operate outside safe limits.
- **Communication fault (~25%)** A broken or improperly terminated fieldbus cable, wrong baud rate, or missing communication module can generate alarm codes.
- **Internal sensor or hardware fault (~20%)** Temperature sensors, current sensors, or internal circuitry may fail or drift out of calibration over time, especially in harsh environments.
- **Control board failure (~15%)** Power surges, humidity, or component aging can damage the microprocessor or associated circuits that monitor drive status.
- **Firmware or memory corruption (~5%)** Power interruptions during operation or end-of-life EEPROM wear can corrupt stored parameters or code, leading to unexplained faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show any additional fault codes or warnings in the fault history menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down all codes and cross-reference them in the manual to narrow the root cause, then address the earliest or most frequent fault first.<br><strong>No:</strong> The A0590 may be the only logged fault, so proceed to check wiring and parameter settings systematically.</div>
</details>

<details class="dtree"><summary>Are all control wiring terminals tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is sound, so focus on parameter review and communication settings next.<br><strong>No:</strong> Clean and retighten all terminals, check for broken strands, and retest the drive after securing connections.</div>
</details>

<details class="dtree"><summary>Can you clear the fault and does it return immediately on power-up without running the motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely internal to the drive hardware or firmware, pointing to a control board or sensor issue that needs professional diagnosis.<br><strong>No:</strong> The fault appears only during operation, so verify motor parameters, load conditions, and external control signals before replacing parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** and lock out the disconnect switch, then wait for the DC bus capacitors to discharge fully before opening the enclosure.
2. **Record the fault history** by navigating the drive keypad menu to view all stored alarms and note the sequence and timestamps.
3. **Consult the user manual** for your specific Micromaster model to decode A0590 and identify which parameters or signals are involved.
4. **Inspect all wiring** at the power, motor, and control terminals for tightness, damage, and correct gauge, and check that shielded cables are grounded at one end only.
5. **Review parameter settings** against the motor nameplate data, verifying rated voltage, current, frequency, and motor type (induction or synchronous).
6. **Check communication connections** if the drive uses Profibus, Modbus, or another fieldbus, confirming termination resistors, baud rate, and node address match the network configuration.
7. **Clear the fault** using the reset button or menu command, then test run the drive unloaded or with reduced speed to see if the code reappears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-a0590-fault-code&k=Siemens+Micromaster+control+board&tag=errorcodefixes-20) \| Match the exact model and firmware revision printed on the existing board |
| Communication module or option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-a0590-fault-code&k=Communication+module+or+option+card&tag=errorcodefixes-20) \| Required only if the fault is traced to a specific fieldbus or I/O expansion card |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in three-phase power systems, if the fault persists after checking wiring and parameters, or if internal board-level diagnosis and firmware updates are needed. Variable frequency drives store lethal DC bus voltage even after mains power is removed, and incorrect parameter changes can damage the motor or driven equipment. A technician with the manufacturer's diagnostic software can read detailed fault logs, perform hardware tests, and update firmware safely.

**Rough cost:** A pro service call runs about $200-500.
