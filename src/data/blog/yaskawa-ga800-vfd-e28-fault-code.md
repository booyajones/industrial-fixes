---
title: "Yaskawa GA800 E28 Fault Code - Causes & Fix"
description: "E28 is not a standard GA800 fault code. Verify the displayed code on your keypad and check your manual for the exact meaning and fix."
pubDatetime: 2026-06-05T09:59:54Z
modDatetime: 2026-06-05T09:59:54Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "GA800 control board (PCB)"
most_likely_cause: "Misread or transposed fault code"
---

## Yaskawa GA800 E28 Fault Code — What It Means

E28 does not appear in verified Yaskawa GA800 documentation as a standard fault or alarm code. The code displayed on your keypad may be misread or may refer to a different fault identifier. Common GA800 codes include Uv3 (Soft Charge Answerback Fault), GF (Ground Fault), and others that use letter-number combinations. Always confirm the exact code shown on the operator panel before diagnosing, as each code has a specific meaning tied to internal circuits, sensors, or protection functions. Consult your GA800 manual or the fault history log (parameter group A1) to identify the true code and its definition for your drive model.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transposed fault code** The displayed fault may actually be Uv3, E2, or another code that looks similar under poor lighting or at an angle.
- **Custom parameter or option-card alarm** Some installations use programmable logic or add-on cards that generate non-standard fault codes not listed in the base manual.
- **Firmware or keypad display error** Corrupted parameter memory or a failing keypad can show garbled or invalid fault codes.
- **Incorrect manual or model mismatch** You may be referencing documentation for a different Yaskawa series (V1000, A1000) that uses E-prefix codes not present on the GA800.

## Step-by-Step Fix {#fix}

1. Power down the drive and wait 5 minutes for capacitors to discharge, then power back up and observe the exact code displayed on the keypad or remote operator.
2. Record the fault code exactly as shown, including all letters, numbers, and any decimal points or prefixes, and compare it against the fault table in your GA800 instruction manual (chapter 6 or appendix).
3. Check parameter A1-01 through A1-04 to review the fault history log and confirm whether the code matches any stored fault events.
4. If the code is confirmed as non-standard, inspect for any option cards (DeviceNet, Modbus, encoder feedback) installed in the drive and consult their supplemental manuals for additional fault definitions.
5. Verify that you are using the correct manual revision for your drive's firmware version by checking the drive nameplate and downloading the matching manual from the Yaskawa website.
6. If the code persists and cannot be identified, contact Yaskawa technical support with the drive model number, serial number, firmware version, and the exact displayed code for official interpretation.
7. If the code is actually Uv3 (Soft Charge Answerback Fault), check parameter U4-06 [PreChargeRelayMainte] and replace the control board or drive if the value exceeds 90 percent or the fault does not clear after a power cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e28-fault-code&k=GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Required if Uv3 soft-charge relay fault is confirmed and does not clear after power cycle. |
| GA800 operator keypad (JVOP) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e28-fault-code&k=GA800+operator+keypad+%28JVOP%29&tag=errorcodefixes-20) \| Replace if the display is garbled, flickering, or shows non-existent codes consistently. |

## When to Call a Pro

Call a qualified drives technician or Yaskawa-certified service provider if you cannot locate the fault code in your manual, if the drive repeatedly displays unrecognized codes after power cycling, or if you lack the tools and training to safely work inside a VFD enclosure. Industrial drives operate at lethal voltages and require proper lockout/tagout, insulated tools, and familiarity with DC bus discharge procedures. A professional can access Yaskawa's internal service bulletins, use DriveWizard software to read detailed fault logs, and perform board-level diagnostics that are not documented in public manuals.

## See Also

- [Yaskawa A1000 HCA Fault Code - Causes & Fix](/posts/yaskawa-a1000-vfd-hca-fault-code/)
- [Yaskawa GA800 F031 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f031-fault-code/)
- [Yaskawa GA800 A.116 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-a-116-fault-code/)
- [Yaskawa GA800 E07 Fault - Causes & Fix](/posts/yaskawa-ga800-e07-fault-code/)
