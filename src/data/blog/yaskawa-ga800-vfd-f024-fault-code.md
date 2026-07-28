---
title: "Yaskawa GA800 CPF24 - Causes & Fix"
description: "CPF24 means control circuit hardware failure. Most common fix: replace the control board assembly after ruling out transient power issues."
pubDatetime: 2026-06-27T11:43:09Z
modDatetime: 2026-06-27T11:43:09Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "GA800 Control Board Assembly"
most_likely_cause: "control board failure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power off the drive, wait at least five minutes for capacitors to discharge, then power on and check if the fault clears on its own."
  - "Inspect control board connectors for looseness or corrosion and reseat them."
part_price: "$300-600 for control board assembly"
---

## What this code means
The CPF24 fault code (Control Circuit Error) on a Yaskawa GA800 VFD signals a hardware problem inside the drive's control electronics. This is not a user-programmable fault or a parameter setting issue. The drive has detected an internal malfunction in its logic board, microprocessor, or associated control circuitry. Unlike faults triggered by external wiring or load conditions, CPF24 points to a physical failure within the VFD itself.

Note: Yaskawa GA800 fault codes use the format CPFxx (Control Panel Fault), not F0xx. If your display shows F024, verify the exact code in the fault history menu. The GA800 troubleshooting manual explicitly states the drive does not support component-level repair beyond fan and control board replacement.

## Before You Replace Anything

Technicians sometimes replace the entire VFD when only the control board has failed. Before ordering a new drive, power-cycle the unit after a five-minute discharge wait and measure control circuit DC voltage to confirm the fault persists and is not a transient power glitch.

## Common Causes

- **Control board failure (~60%)** Damaged microcontroller, degraded capacitors, or cracked solder joints on the logic board trigger the CPF24 code.
- **Power supply instability (~15%)** Insufficient or noisy DC voltage to the control circuit causes intermittent or persistent control errors.
- **Firmware corruption (~10%)** Abrupt power loss or improper firmware updates can corrupt the drive's internal software and flag a control circuit fault.
- **Environmental stress (~10%)** Excessive heat, moisture, or vibration damages sensitive control components over time.
- **Age-related degradation (~5%)** GA800 drives in service longer than five to seven years often show control board wear from thermal cycling and component aging.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a five-minute power-off and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may be transient due to a power glitch. Monitor the drive closely for recurrence and check input power quality.<br><strong>No:</strong> The control board or its power supply is likely faulty. Proceed with voltage measurements and board inspection.</div>
</details>

<details class="dtree"><summary>Is the control circuit DC voltage within 12.0 to 14.5 volts at the board terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power supply is delivering correct voltage. The control board itself has failed and needs replacement.<br><strong>No:</strong> The main power supply or input capacitors are degraded. Inspect the power supply section before replacing the control board.</div>
</details>

<details class="dtree"><summary>Do you see any burned components, cracked solder, or discolored capacitors on the control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> Physical damage confirms board failure. Replace the control board assembly.<br><strong>No:</strong> The fault is likely internal to the microprocessor or firmware. Replace the control board assembly and test.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the VFD** and disconnect all input power. Wait at least five minutes for internal capacitors to discharge completely before touching any terminals.
2. **Re-energize the drive** and observe the display. If CPF24 persists immediately, proceed with diagnostics. If the fault clears, monitor for recurrence over several cycles.
3. **Measure DC voltage at control board terminals** using a multimeter. The expected range is 12.0 to 14.5 volts DC. If voltage is below 11 volts or above 16 volts, inspect the main power supply or input capacitors.
4. **Inspect the control board physically** with power off. Look for burned components, cracked solder joints, discolored capacitors, moisture, or corrosion on board traces. Check all connectors to the control board for tightness.
5. **Replace the control board assembly** if the fault persists and voltage is correct. Yaskawa does not support component-level repair. Use the model-specific control board part number from the drive nameplate catalog code.
6. **Reset the fault** using the keypad RESET button after board replacement. Run the drive at low speed with no load and verify no alarms appear.
7. **Test at full load** and monitor for stability over several minutes. Check that all parameter settings transferred correctly to the new board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 Control Board Assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f024-fault-code&k=GA800+Control+Board+Assembly&tag=errorcodefixes-20) \| Model-specific part. Match catalog code from drive nameplate. Only fan and control board replacements are supported by Yaskawa. |
| Input Power Supply Capacitors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f024-fault-code&k=Input+Power+Supply+Capacitors&tag=errorcodefixes-20) \| If control circuit voltage is out of range, replace main power supply capacitors rather than the control board. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work inside high-voltage equipment. The GA800 contains lethal DC bus voltages that remain present for several minutes after power-off. Control board replacement requires proper ESD handling, parameter backup and restore, and load testing under full operating conditions. If you lack a multimeter, ESD wrist strap, or experience with VFD internals, professional service is the safest choice. Also call a pro if voltage measurements are abnormal, if the drive shows multiple simultaneous fault codes, or if the replacement board does not clear the CPF24 fault.

**Rough cost:** A pro service call runs about $400-900 for control board replacement and testing.
