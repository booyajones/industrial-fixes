---
title: "Yaskawa GA800 A.115 Fault - Causes & Fix"
description: "A.115 is an alarm history code on the GA800 VFD. Check the keypad display and manual code table for the exact fault, then clear the root cause and reset."
pubDatetime: 2026-06-08T11:09:22Z
modDatetime: 2026-06-08T11:09:22Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "GA800 control board"
---

## Yaskawa GA800 A.115 Fault — What It Means

A.115 is a fault or alarm history code displayed on the GA800 VFD keypad. The GA800 records faults and alarms in a history list, and the exact meaning of A.115 must be cross-referenced in the full Yaskawa GA800 alarm and fault code table in the drive manual or on the keypad legend. The code indicates that the drive has detected an alarm condition that was logged, but the specific failure type is not defined in general documentation. According to Yaskawa, faults and alarms are shown on the keypad and can only be cleared after the underlying cause is removed and the drive is reset. The A.115 designation alone does not tell you what failed, only that an alarm was recorded in that history position.

## Before You Replace Anything

Technicians sometimes replace the control board or option cards without first checking the elementary diagram and verifying the exact alarm definition, wasting time and parts. Always record the full fault description from the keypad and check the control wiring and safety circuits before ordering components.

[Jump to Fix](#fix)

## Common Causes

- **Incoming power disturbance or phase loss (~25%)** Power-quality issues such as voltage sag, phase imbalance, or transient spikes can trip the drive and log an alarm code.
- **Loose or miswired control terminals (~20%)** Control signal wiring, terminal blocks, or jumpers that are loose, damaged, or incorrectly configured can generate alarm conditions.
- **Interrupted Safe Torque Off circuit (~20%)** An open or missing STO jumper or safety-circuit wiring prevents run enable and logs an alarm on GA800 systems with safety functions.
- **Incorrect parameter setup or factory reset (~15%)** Drive parameters that do not match the motor, application, or option cards can cause the drive to fault and record an alarm.
- **Failed or unseated option card (~12%)** Communication or I/O option cards that are damaged, unseated, or incompatible with the firmware version can generate alarms.
- **Control board component failure (~8%)** Internal control board faults, including damaged logic circuits or failed relays, can trigger alarm logging.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display show a full fault description in addition to A.115?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the full description and cross-check it in the GA800 manual alarm table to identify the exact condition.<br><strong>No:</strong> Scroll through the fault history menu on the keypad to see if other codes or descriptions are logged, then consult the manual code table.</div>
</details>

<details class="dtree"><summary>Is the Safe Torque Off circuit wired and are all jumpers in place?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify that the STO terminals are properly connected or jumpered per the wiring diagram and that no safety-circuit interlock is open.<br><strong>No:</strong> Install or restore the required STO jumpers or safety wiring as shown in the GA800 installation manual, then reset the drive.</div>
</details>

<details class="dtree"><summary>Are all option cards and terminal connectors firmly seated with no visible damage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the parameter setup for conflicts or incorrect configuration, especially motor parameters and option-card settings.<br><strong>No:</strong> Remove power, wait for discharge, reseat or replace the option card or damaged connector, then power up and reset the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault details** from the keypad display, including any full fault description, date, time, and operating context before attempting a reset.
2. **Remove power safely** by opening the disconnect or circuit breaker, then wait until all keypad indicators and LEDs are off to confirm the drive capacitors have discharged.
3. **Inspect the drive and wiring** for obvious damage, loose terminals, unseated option cards, missing STO jumpers, incorrect catalog number, or signs of shipping damage.
4. **Check the elementary diagram** and control wiring to verify the signal path and any external interlocks or safety circuits that could generate the alarm.
5. **Verify the Safe Torque Off circuit** by confirming that STO terminals are jumpered or correctly wired per the installation manual, as an open STO circuit will prevent run enable.
6. **Correct the underlying cause** identified in the fault history or elementary diagram, whether it is a wiring error, parameter mismatch, power issue, or failed component.
7. **Restore power and reset the drive** from the keypad once the condition is cleared, then test operation and monitor for any recurring alarms or faults.
8. **Contact Yaskawa technical support** with the model number, serial number, spec code, and complete fault history if the alarm persists or the cause is not clear from the manual code table.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-115-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Replace only if the board shows physical damage or if Yaskawa support confirms internal fault after all wiring and parameters are verified. |
| GA800 option card (communications or I/O) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-115-fault-code&k=GA800+option+card+%28communications+or+I%2FO%29&tag=errorcodefixes-20) \| Order the exact catalog number for your drive series and firmware version; verify card is seated and parameters are configured before replacing. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service provider if you cannot locate the exact alarm definition in the GA800 manual code table, if the fault recurs after wiring and parameter checks, or if you lack the training to safely work on industrial motor-drive systems. High-voltage DC bus capacitors, control logic troubleshooting, and firmware or parameter configuration require specialized knowledge and test equipment. Always contact Yaskawa technical support with the drive model, spec number, serial number, and complete fault history if the alarm cause is not obvious or if the drive shows physical damage or component failure.

**Rough cost:** A pro service call runs about $200-500.
