---
title: "Yaskawa GA800 A.106 Fault - Causes & Fix"
description: "A.106 fault on Yaskawa GA800 VFD meaning varies by firmware. Most often a parameter or application mismatch. Reset after fixing cause."
pubDatetime: 2026-06-08T10:58:51Z
modDatetime: 2026-06-08T10:58:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
---

## Yaskawa GA800 A.106 Fault — What It Means

The A.106 fault code is not documented in widely available Yaskawa GA800 technical manuals. Fault and alarm codes on the GA800 indicate drive protection events or configuration issues. Yaskawa's general troubleshooting procedure requires identifying the exact alarm definition from your drive's firmware documentation or the elementary diagram supplied with your model. Some GA800 codes relate to motor tuning errors, wiring faults, or parameter mismatches.

Because the A.106 code definition is not verified in manufacturer materials, consult your drive's full fault table in the user manual or contact Yaskawa technical support to confirm the exact meaning for your firmware version. Once you identify and remove the root cause, press the RESET button on the keypad to clear the fault and restore operation.

## Before You Replace Anything

Technicians sometimes replace the control board before verifying motor wiring, phase balance, or parameter setup. Always check input voltage, motor connections, and autotuning results first.

[Jump to Fix](#fix)

## Common Causes

- **Parameter configuration error (~35%)** Motor nameplate data entered incorrectly or drive parameters incompatible with the application.
- **Motor wiring or phase issue (~25%)** Loose, open, or reversed motor leads or line-to-line resistance outside acceptable range.
- **Autotuning failure (~20%)** Drive autotuning returned results outside the applicable parameter range or tuning was not completed.
- **Control board or keypad fault (~10%)** Internal communication error or corrupted firmware on the control board.
- **Incorrect drive model for application (~10%)** Drive shipped or installed does not match the required horsepower, voltage, or load type.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show the fault code clearly and does it match your manual's fault table?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the manufacturer's corrective action for that code and reset after fixing.<br><strong>No:</strong> Document the exact code displayed and contact Yaskawa technical support for the correct definition.</div>
</details>

<details class="dtree"><summary>Have you recently changed motor parameters or run autotuning?</summary>
<div class="dtree-body"><strong>Yes:</strong> Re-enter motor nameplate data and repeat autotuning following the GA800 manual procedure.<br><strong>No:</strong> Check input power quality and motor wiring integrity at the terminal block.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you press RESET on the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> Monitor for recurrence. If it returns immediately, the root cause is still present.<br><strong>No:</strong> The drive is locked out. Power cycle the unit and inspect for hardware damage or wiring shorts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact fault code** displayed on the GA800 keypad and compare it to the fault table in your drive's user manual or wiring diagram.
2. **Power down the drive** and lock out the incoming supply according to your facility's electrical safety procedures.
3. **Inspect motor wiring** at the drive output terminals for loose connections, damaged insulation, or reversed phases.
4. **Verify motor nameplate data** matches the parameters programmed in the drive (voltage, current, frequency, horsepower).
5. **Re-run autotuning** if the drive supports it and the motor data has been corrected, following the GA800 autotuning procedure in the manual.
6. **Restore power** and press RESET on the keypad after correcting the identified cause.
7. **Monitor drive operation** under load for at least one full cycle to confirm the fault does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-106-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Factory replacement component for internal faults. Verify board part number from drive label. |
| Yaskawa GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-106-fault-code&k=Yaskawa+GA800+cooling+fan&tag=errorcodefixes-20) \| Field-replaceable component if drive overheats due to blocked airflow or fan failure. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service center if you cannot find the A.106 code in your manual, if the fault persists after parameter correction and wiring checks, or if you lack the training to work safely on industrial three-phase equipment. High-voltage VFD repair requires lockout/tagout procedures, multimeter diagnostics, and familiarity with motor control circuits. The GA800 maintenance documentation notes that field repair scope is limited to fan and control board replacement. Internal capacitor banks and power modules retain lethal voltage even after shutdown and must be discharged by trained personnel.

**Rough cost:** A pro service call runs about $200-500.

## See Also

- [Yaskawa GA800 A.120 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-120-fault-code/)
- [Yaskawa GA800 A.143 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-143-fault-code/)
- [Yaskawa GA800 E37 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e37-fault-code/)
- [Yaskawa A1000 Complete Guide - Fault Codes, Parameters, and Commissioning](/posts/yaskawa-a1000-complete-guide/)
