---
title: "Yaskawa GA800 F013 Fault - Causes & Fix"
description: "F013 is not a standard GA800 code. Verify the display; common codes are PF (Phase Loss) or OC (Overcurrent). Contact Yaskawa support."
pubDatetime: 2026-06-26T10:08:08Z
modDatetime: 2026-06-26T10:08:08Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Control Board"
diy_or_pro: "pro"
free_checks:
  - "Re-check the fault code display on the keypad to confirm it is not PF, OC, or another standard code"
  - "Inspect input power terminals for loose or corroded connections"
  - "Verify that all three input phases are present and stable at the incoming power supply"
---

## What this code means
The F013 fault code does not appear in the available Yaskawa GA800 documentation or manuals. Standard GA800 fault codes include PF (Phase Loss), OC (Overcurrent), OV (Overvoltage), and UV (Undervoltage). The code displayed may be a misread (such as confusing PF with F013), a typographical error, or a code not listed in publicly accessible service documents. You should carefully re-check the keypad display and consult the drive's technical manual or contact Yaskawa Technical Support directly at repair@yaskawa.com or 1.800.927.5292 for the specific definition.

If the actual fault is PF (Phase Loss), it indicates Input Phase Loss caused by a dropped phase in the drive input power or loose wiring at the input terminals. If the fault is OC (Overcurrent), it points to rapidly oscillating torque reference, mechanical binding, or a ground fault in the motor. Without confirmation of the exact code, proceed by inspecting input power connections, checking for loose terminals, and monitoring output current for abnormal behavior.

## Before You Replace Anything

Technicians sometimes replace the motor after an overcurrent fault without first checking for loose encoder couplings, mechanical binding, or poor grounding. Perform a megger test on the motor leads (not the drive itself) and inspect all mechanical connections before ordering a new motor.

## Common Causes

- **Misread or non-standard fault code (~40%)** The displayed code may be PF (Phase Loss) or another standard code that was misinterpreted as F013, or the code is not documented in public GA800 manuals.
- **Loose input power wiring (if PF) (~25%)** Loose connections at the drive input power terminals or a missing phase in the incoming supply can trigger a Phase Loss fault.
- **Mechanical binding or oscillating torque (if OC) (~15%)** Rapidly changing torque reference, obstructed couplings, or tight encoder tethers can cause overcurrent faults.
- **Motor ground fault (if OC) (~10%)** Insulation breakdown in the motor windings or ground fault in motor leads can trip an overcurrent protection.
- **Damaged control board (~10%)** Internal drive faults or corrupted firmware can display non-standard fault codes or misreport standard codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad clearly show F013, or could it be PF or another two-letter code?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it is actually PF, proceed to check input power wiring and phase presence. If it is another code, consult the GA800 manual for that specific fault.<br><strong>No:</strong> If the code is truly F013 and not documented, contact Yaskawa Technical Support for interpretation before troubleshooting further.</div>
</details>

<details class="dtree"><summary>Are all three input phases present and stable at the drive input terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is likely good. Check for loose terminals, then inspect the motor and mechanical connections for binding or ground faults.<br><strong>No:</strong> Repair the incoming power supply or tighten loose input terminals. Reset the drive and test.</div>
</details>

<details class="dtree"><summary>Is the motor mechanically free, with no binding in couplings or encoder tether?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical system is clear. Perform a megger test on motor leads (not the drive) to check for ground faults or insulation breakdown.<br><strong>No:</strong> Free the obstruction, tighten the encoder coupling, and verify smooth rotation before restarting the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the incoming power supply to make sure safe access to terminals and connections.
2. **Re-check the fault code** displayed on the keypad and write it down exactly. Confirm whether it reads F013, PF, OC, or another standard GA800 code.
3. **Inspect the input power terminals** for loose, corroded, or missing connections. Tighten all three phases and verify continuity back to the main supply.
4. **Measure incoming phase voltages** at the drive input to confirm all three phases are present and stable. Consult your model's table for acceptable voltage ranges.
5. **Examine all mechanical connections** including motor couplings, encoder tethers, and load attachments. make sure the motor shaft spins freely by hand with no binding.
6. **Perform a megger insulation test** on the motor leads only (do not megger the drive itself, as this will damage it). Look for values within the motor manufacturer's acceptable range.
7. **Check grounding** of the motor frame and drive chassis. Verify a low-resistance path to earth ground and inspect for loose or missing ground wires.
8. **Consult the GA800 Technical Manual** (reference SIEPC*********) or contact Yaskawa Technical Support at repair@yaskawa.com or 1.800.927.5292 if the code remains undefined or the fault persists after basic checks.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f013-fault-code&k=Yaskawa+GA800+Control+Board&tag=errorcodefixes-20) \| Only user-replaceable component beyond fan; contact Yaskawa for part number and availability. |
| Motor Coupling or Encoder Tether | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f013-fault-code&k=Motor+Coupling+or+Encoder+Tether&tag=errorcodefixes-20) \| Replace if mechanical inspection reveals damage or wear causing binding. |
| Three-Phase Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f013-fault-code&k=Three-Phase+Motor&tag=errorcodefixes-20) \| Replace only after megger test confirms insulation failure or ground fault; verify all other causes first. |

## When to Call a Pro

Call a qualified electrician or Yaskawa-certified technician if you cannot confirm the exact fault code, if incoming three-phase power is unstable or missing, or if the drive displays the same fault after you have verified input wiring and mechanical connections. Do not attempt to replace the control board or perform high-voltage diagnostics unless you have VFD training and proper test equipment. Do not use a megger on the drive itself, as manufacturer documentation explicitly warns this will cause damage. If the motor megger test shows insulation breakdown or a ground fault, a professional should evaluate whether the motor or drive output stage has failed. Yaskawa supports only fan and control board replacement for end-user service, and any other internal repair requires factory return or authorized service.

**Rough cost:** A pro service call runs about $200-500.
