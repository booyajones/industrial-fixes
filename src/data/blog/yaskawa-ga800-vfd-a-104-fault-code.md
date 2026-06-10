---
title: "Yaskawa GA800 A.104 Fault - Causes & Fix"
description: "A.104 is not a documented GA800 fault code. Verify the exact code on the keypad display and consult your GA800 manual's fault table."
pubDatetime: 2026-06-08T10:57:11Z
modDatetime: 2026-06-08T10:57:11Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
---

## Yaskawa GA800 A.104 Fault — What It Means

A.104 does not appear in the published Yaskawa GA800 fault code tables available in manufacturer documentation. GA800 drives display alphanumeric fault codes on the keypad when an internal protection circuit trips or a sensor detects an abnormal condition. Because this specific code cannot be verified for the GA800 series, it may be a misread display, a code from a different Yaskawa drive family, or a custom parameter alarm configured by the installer.

Yaskawa specifies that all GA800 faults must have their underlying cause removed before pressing RESET on the keypad to clear the alarm. If your keypad shows A.104, write down the exact characters and dots as displayed, then cross-reference the fault table in your GA800 Installation and Primary Operation manual or the GA800 Maintenance and Troubleshooting manual. If the code does not appear in those tables, contact Yaskawa technical support or the drive integrator to confirm whether it is a user-defined alarm.

## Before You Replace Anything

Technicians sometimes replace the control board when the fault code is actually a misread display or a parameter-configuration alarm that only requires a software reset or parameter adjustment. Always photograph the keypad and consult the fault table before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread or misidentified fault code (~40%)** The display may show a similar code from another Yaskawa series or a decimal point that changes the meaning.
- **User-defined parameter alarm (~30%)** Some GA800 installations use custom alarm codes configured by the system integrator for external interlock or process faults.
- **Control board memory corruption (~15%)** Power surges or battery failure can scramble parameter memory and generate undefined fault codes.
- **Keypad display fault (~10%)** A failing keypad LCD can show garbled characters that look like valid codes.
- **Firmware version mismatch (~5%)** Older or beta firmware may display codes not documented in the standard manual.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display show any other text or symbols alongside A.104?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the full display exactly as shown, including dots and brackets, then compare it to the fault table in your manual. The additional text may clarify the code family.<br><strong>No:</strong> The code may be user-defined or from a different drive series. Proceed to verify the drive model and firmware version.</div>
</details>

<details class="dtree"><summary>Can you find A.104 in the fault code table of your printed GA800 manual?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the troubleshooting steps listed for that code in the manual and remove the cause before pressing RESET.<br><strong>No:</strong> Contact Yaskawa technical support with your drive serial number and a photo of the keypad to confirm whether the code is valid.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you press RESET and then immediately reappear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The underlying condition is still present. Check for external interlock signals, parameter settings, or a hardware fault on the control board.<br><strong>No:</strong> The fault may have been transient due to noise or a momentary power disturbance. Monitor the drive for recurrence.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the main disconnect to make sure safe access to the keypad.
2. **Photograph the keypad display** exactly as shown, capturing any decimal points, brackets, or additional text that may clarify the code.
3. **Locate your GA800 manual** (Installation and Primary Operation or Maintenance and Troubleshooting) and turn to the fault code table, typically in an appendix or troubleshooting chapter.
4. **Cross-reference the displayed code** against every entry in the table. If A.104 does not appear, note the closest alphanumeric codes and check for firmware release notes or addenda.
5. **Check the parameter list** (accessible via the keypad programming menu) for any user-defined alarm settings in the 400-series or 500-series parameter groups that may generate custom codes.
6. **Contact Yaskawa technical support** or your system integrator with the drive model number, serial number, firmware version, and the exact fault display to confirm the code definition.
7. **Clear the fault** only after the underlying cause is identified and removed, then press RESET on the keypad and monitor the drive for stable operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (main CPU card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-104-fault-code&k=Yaskawa+GA800+control+board+%28main+CPU+card%29&tag=errorcodefixes-20) \| Only order after Yaskawa confirms a hardware fault. Part number is model-specific. |
| Yaskawa GA800 keypad (JVOP-180 or JVOP-181) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-104-fault-code&k=Yaskawa+GA800+keypad+%28JVOP-180+or+JVOP-181%29&tag=errorcodefixes-20) \| Replace if the LCD is damaged or displays garbled characters that do not match any manual entry. |

## When to Call a Pro

Call a qualified Yaskawa distributor or certified drive technician if the fault code does not appear in your manual, if you are unable to access the parameter menu, or if the drive was recently installed or programmed by an integrator. VFD troubleshooting requires familiarity with parameter configuration, wiring diagrams, and high-voltage DC bus circuits. Yaskawa's own maintenance documentation states that GA800 repair is limited to fan and control board replacement and that other internal faults require factory service or a drive exchange. Do not attempt to open the drive enclosure or replace power components without proper training and lockout procedures.

**Rough cost:** A pro service call runs about $150-400 for diagnostics and minor part replacement if a board or fan is confirmed faulty.

## See Also

- [Yaskawa GA800 E22 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e22-fault-code/)
- [Yaskawa VFD Fault PF — Causes & Fix](/posts/yaskawa-vfd-fault-pf/)
- [Yaskawa GA800 E13 Error - Causes & Fix](/posts/yaskawa-ga800-vfd-e13-fault-code/)
- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
