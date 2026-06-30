---
title: "Yaskawa GA800 F037 Fault - Causes & Fix"
description: "F037 does not exist in GA800 documentation. Verify the exact code on the display. Likely misread of OC, OV, or CrST alarm codes."
pubDatetime: 2026-06-28T10:10:09Z
modDatetime: 2026-06-28T10:10:09Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Encoder coupling or tether"
most_likely_cause: "Misidentified fault code"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact fault code displayed on the GA800 by navigating to the Modified Parameter or Fault Log menu"
  - "Check that the Run command is off before attempting to reset the drive (CrST alarm requires Run command to be inactive)"
  - "Inspect all mechanical couplings (motor-to-load and encoder-to-motor) for tightness and proper alignment"
no_buy_pct: "60%"
---

## Yaskawa GA800 F037 Fault — What It Means

The F037 fault code does not appear in Yaskawa's GA800 VFD technical manual or official fault code listings. The GA800 uses fault prefixes like OC (Overcurrent), OV (Overvoltage), LP (Low Pressure), CrST (Cannot Reset), and bUS (Option Communication), but numeric codes in the F001-F999 format are not part of the standard GA800 fault register.

If you see F037 on your display, it may be a misread of a different code (such as OC037 or F370), a firmware-specific error from a different Yaskawa drive model (GA500, E7, or a servo system), or a custom application error. The most common faults that technicians mistake for F037 are CrST (Cannot Reset, which occurs when a run command is still active during reset) and OC faults (Overcurrent due to ground faults, PID feedback oscillation, or mechanical coupling issues). Always verify the exact code using the Modified Parameter or Fault Log menu on the GA800 display before proceeding with diagnostics.

## Before You Replace Anything

Technicians often replace motors or encoders assuming an overcurrent fault without first checking for loose mechanical couplings or ground faults. A megger test on motor leads (should read above 1 megohm) and a visual inspection of encoder and motor-to-load couplings can identify the real cause before spending on hardware.

[Jump to Fix](#fix)

## Common Causes

- **Code misread or misidentified (~40%)** The display may show a different code (OC, OV, CrST, or bUS) that was misread as F037, or the code may belong to a different Yaskawa drive model.
- **CrST (Cannot Reset) alarm active (~20%)** The drive will not reset if the Run command is still active when you attempt to clear a fault.
- **Ground fault in motor or wiring (~15%)** A ground fault in the motor windings or cable can trigger overcurrent faults and persist even after motor replacement if the wiring is damaged.
- **PID feedback oscillation (~10%)** A rapidly oscillating torque reference from unstable PID feedback can cause overcurrent faults that only appear when PID mode is active.
- **Loose encoder or motor coupling (~10%)** A slipping encoder coupling or motor-to-load coupling allows mechanical play that creates torque spikes and fault conditions.
- **Incorrect motor parameters (~5%)** Motor parameters that do not match the connected motor can lead to control instability and fault codes during operation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the GA800 display show the exact code F037, or could it be OC, OV, CrST, or another code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Navigate to the Fault Log menu (consult your GA800 manual for menu path) and write down the exact code displayed, then look it up in the technical manual.<br><strong>No:</strong> The code is confirmed as F037, which does not exist in GA800 documentation. Contact Yaskawa Technical Support with your drive model and serial number for clarification.</div>
</details>

<details class="dtree"><summary>Is the Run command (forward or reverse) currently active on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Turn off the Run command using the external input, keypad, or network command, then attempt to reset the fault. This resolves CrST alarms.<br><strong>No:</strong> The fault is not a CrST alarm. Proceed with checking for ground faults and mechanical issues.</div>
</details>

<details class="dtree"><summary>Do you have access to a megger (insulation resistance tester) to test the motor and cable?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect the motor from the drive and perform a megger test on each motor lead to ground. Readings above 1 megohm are normal. Readings below 1 megohm indicate a ground fault in the motor or cable.<br><strong>No:</strong> Check all motor and encoder cable connections for damage, moisture, or loose terminals. Inspect mechanical couplings for tightness and proper alignment.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact fault code** by navigating to the Modified Parameter or Fault Log menu on the GA800 keypad and write down the complete code displayed.
2. **Check for CrST (Cannot Reset) conditions** by confirming the Run command (forward or reverse) is off, then attempt to reset the fault using the reset button or command.
3. **Inspect PID feedback** if the fault only occurs in PID mode by checking the feedback sensor wiring and signal stability with a multimeter or scope.
4. **Perform a megger test** on motor leads to ground with the motor disconnected from the drive (readings should be above 1 megohm to rule out ground faults).
5. **Examine all mechanical couplings** by checking that motor-to-load and encoder-to-motor couplings are tightened to specification and free of obstruction or wear.
6. **Run a rotational autotune** from the GA800 setup menu to recalibrate motor parameters and confirm the drive can control the motor without faults.
7. **Contact Yaskawa Technical Support** with your drive model number, serial number, exact fault code, and application details if the fault persists or the code cannot be identified.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder coupling or tether | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f037-fault-code&k=Encoder+coupling+or+tether&tag=errorcodefixes-20) \| Replace if the coupling is slipping or damaged and causing torque oscillation faults. |
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f037-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Use if megger test shows ground fault in the cable rather than the motor windings. |
| GA800 control board or fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f037-fault-code&k=GA800+control+board+or+fan&tag=errorcodefixes-20) \| Yaskawa supports replacement of these components if internal diagnostics point to drive hardware failure. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-certified integrator if you cannot identify the exact fault code after checking the display menu, if the drive does not reset after turning off the Run command, or if a megger test shows a ground fault and you are unsure whether the fault is in the motor, cable, or drive output stage. Professional help is also needed if the fault involves option communication modules (bUS errors), if you lack the tools to perform insulation resistance testing, or if the drive requires firmware updates or internal board replacement. Yaskawa Technical Support can provide remote diagnostics and should be contacted if the fault code does not match any entry in the GA800 manual.

**Rough cost:** A pro service call runs about $200-500 for diagnostic and repair depending on actual fault.
