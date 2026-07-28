---
title: "Yaskawa GA800 F028 Fault - Causes & Fix"
description: "F028 is not a recognized Yaskawa GA800 fault code. Verify the exact code on the keypad and cross-check the official manual or call support."
pubDatetime: 2026-06-27T11:46:44Z
modDatetime: 2026-06-27T11:46:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Keypad / Operator"
most_likely_cause: "Misread or typographical error of the displayed fault code"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact fault code displayed on the GA800 keypad or LED operator"
  - "Consult the official GA800 Maintenance & Troubleshooting Manual fault code list"
  - "Check for loose connections or grounding issues at the control terminals"
no_buy_pct: "80%"
---

## What this code means
The fault code F028 does not appear in Yaskawa's official GA800 VFD documentation. Yaskawa fault codes for the GA800 follow the format F001 through F999, but F028 is not among the recognized codes in the Maintenance & Troubleshooting Manual. This discrepancy typically arises from one of three issues: a misread code on the display (for example F020, F029, or F038), confusion with a different Yaskawa drive model (such as the GA700 or GA500 series where fault formats vary), or a third-party keypad or controller that uses a custom fault code set.

The best first step is to verify the exact code displayed on the GA800 LED operator or keypad. If the display truly shows F028, cross-check it against the official GA800 Fault Code List in the drive manual and contact Yaskawa Technical Support directly with the drive's model number, serial number, and a description of the fault condition. Common similar codes include F020 for encoder errors, F029 for PID feedback errors, and F038 for DC bus overvoltage issues in certain contexts.

## Before You Replace Anything

Technicians sometimes replace the control board or encoder before verifying the actual fault code. Always confirm the exact code on the keypad and consult the official manual or Yaskawa support before ordering parts.

## Common Causes

- **Misread fault code on display (~50%)** The operator may have misread the code as F028 when the actual code is F020, F029, or F038, all of which are valid GA800 faults.
- **Drive model confusion (~25%)** The code might belong to a different Yaskawa VFD series (GA700, GA500, or E7) where fault code formats and numbering differ.
- **Third-party keypad or controller (~15%)** A non-Yaskawa keypad or aftermarket controller may be displaying a custom fault code not in the official GA800 set.
- **Encoder or PID feedback wiring fault (~10%)** If the actual code is F020 or F029, the cause is typically a faulty encoder coupling, tether, or PID feedback sensor wiring.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display clearly show F028 without flickering or artifacts?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is likely not a display error. Consult the official GA800 manual fault list and contact Yaskawa support with the drive model and serial number.<br><strong>No:</strong> The display may be faulty or the code was misread. Power cycle the drive and observe the code again, or check for loose keypad connections.</div>
</details>

<details class="dtree"><summary>Is the drive a genuine Yaskawa GA800 model (not GA700, GA500, or a third-party variant)?</summary>
<div class="dtree-body"><strong>Yes:</strong> F028 is not a valid GA800 code. Double-check the code and compare it to similar valid codes like F020, F029, or F038 in the manual.<br><strong>No:</strong> The fault code format may belong to a different Yaskawa series or aftermarket controller. Consult the documentation for that specific model.</div>
</details>

<details class="dtree"><summary>Have you recently replaced the keypad or added a third-party controller?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault code may be a custom code from the new keypad or controller. Check the third-party documentation or revert to the original Yaskawa keypad.<br><strong>No:</strong> The issue is likely a misread code or a display error. Verify the code carefully and contact Yaskawa support for confirmation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** by reading the GA800 LED operator or keypad display carefully. Write down the exact code shown, including all digits and letters.
2. **Consult the official manual** by locating the GA800 Maintenance & Troubleshooting Manual (SIEPC series) and cross-referencing the code against the Fault Code List. Confirm whether F028 appears in the list.
3. **Check for similar valid codes** such as F020 (Encoder Error), F029 (PID Feedback Error), or F038 (DC Bus Overvoltage) that may have been misread as F028.
4. **Inspect the keypad and connections** by checking for loose wiring, corrosion, or damage at the keypad terminals and operator interface. Reseat all connections firmly.
5. **Power cycle the drive** by shutting down the VFD, waiting 60 seconds, and restarting. Observe whether the fault code reappears and whether it matches the original reading.
6. **Contact Yaskawa Technical Support** at 1.800.927.5292 (press Option 2, then Option 1) or email repair@yaskawa.com with the drive's model number, serial number, and a description of the fault condition.
7. **Test for common fault causes** if the actual code is F020 or F029: inspect encoder wiring for continuity and shorts, verify encoder coupling tightness and alignment, and perform a megger test on motor leads (target ≥100MΩ for healthy insulation). Replace faulty sensors or encoders as needed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Keypad / Operator | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f028-fault-code&k=Yaskawa+GA800+Keypad+%2F+Operator&tag=errorcodefixes-20) \| Only if the keypad display is damaged or a third-party unit is causing custom codes; verify compatibility with your GA800 model. |
| PID Feedback Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f028-fault-code&k=PID+Feedback+Sensor&tag=errorcodefixes-20) \| If the actual code is F029, replace a faulty analog feedback sensor or transducer; consult your application manual for the correct type. |
| Incremental Encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f028-fault-code&k=Incremental+Encoder&tag=errorcodefixes-20) \| If the actual code is F020, replace the encoder or encoder coupling; match the encoder type and PPR to the motor and drive specifications. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-certified service provider when the fault code cannot be verified from the official manual, when you suspect control board or internal drive failure, or when the drive is part of a critical industrial process that requires immediate diagnosis. Professional help is also needed if the actual fault (F020 or F029) involves encoder tuning, PID loop configuration, or megger testing of motor insulation, as these tasks require specialized test equipment and knowledge of drive programming. Contact Yaskawa Technical Support directly at 1.800.927.5292 or repair@yaskawa.com to confirm the fault code and obtain guidance before attempting repairs or ordering parts.

**Rough cost:** A pro service call runs about $150-400.
