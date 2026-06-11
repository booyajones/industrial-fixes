---
title: "Yaskawa GA800 E13 Fault Code - Causes & Fix"
description: "E13 is not a documented GA800 fault code. Learn how to verify the actual displayed fault on your Yaskawa GA800 drive and troubleshoot correctly."
pubDatetime: 2026-05-30T12:27:51Z
modDatetime: 2026-05-30T12:27:51Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "GA800 operator keypad (JVOP-180)"
---

## Yaskawa GA800 E13 Fault Code — What It Means

E13 does not appear in the Yaskawa GA800 fault or alarm code lists in the manufacturer documentation. If your keypad displays E13, it is likely a misread, a different code (such as E1 or A13), or a custom field-configured label from an option card or communication module. The GA800 uses specific fault and alarm displays that are documented in the manual, and the technician must verify the exact message on the operator keypad before diagnosing.

Yaskawa instructs technicians to remove the cause of any fault and reset the drive, and to check wiring and peripheral ratings after a trip or blown fuse before re-energizing the drive. Because E13 is not a standard GA800 code, you must confirm what the drive is actually showing and then cross-reference that exact code with your GA800 model manual and any installed option cards.

[Jump to Fix](#fix)

## Common Causes

- **Misread display or similar code** The keypad may show E1, E3, A13, or another code that looks like E13 in poor lighting or from an angle.
- **Option card or communication error** Installed option cards (network, encoder, I/O expansion) can generate their own error codes not listed in the base drive fault table.
- **Custom user alarm or parameter message** Some installations configure custom alarms or status messages using parameter programming that do not match factory fault lists.
- **Field-applied label or sticker** A previous technician may have applied a non-standard error label or documentation that does not match Yaskawa's code system.

## Step-by-Step Fix {#fix}

1. **Verify the exact keypad display.** Stand directly in front of the operator panel in good light and write down the complete fault or alarm code, including any prefix letters (A, E, F) and all digits, and note whether it is labeled as a fault, alarm, or status message.
2. **Consult the GA800 manual fault table.** Locate your drive's manual (by model code from the nameplate) and turn to the fault and alarm code section, then find the exact code you recorded in step 1.
3. **Check installed option cards.** Open the drive enclosure and note any option modules installed in the control card slots, then refer to each option's manual for its specific error codes if the base manual does not list your code.
4. **Inspect wiring and peripherals.** Before resetting or re-energizing, check all input power connections, motor leads, control wiring, and fuse condition per Yaskawa's instruction to inspect after any trip.
5. **Clear the fault and test.** Follow the manual procedure to reset the fault (usually a dedicated reset input or keypad command), then run the drive under no-load or reduced-load conditions to see if the fault returns.
6. **Record parameter settings.** If the fault does not return, use the keypad to review recent alarm history and any user-configured alarm parameters in the 100-series and 200-series parameter groups.
7. **Contact Yaskawa support with details.** If you cannot match the code to any manual, provide Yaskawa technical support with the exact keypad message, drive model and serial number, and a photo of the display for identification.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 operator keypad (JVOP-180) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e13-fault-code&k=GA800+operator+keypad+%28JVOP-180%29&tag=errorcodefixes-20) \| Replacement if display is damaged or unreadable |
| GA800 control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e13-fault-code&k=GA800+control+PCB&tag=errorcodefixes-20) \| Required if option slot or main board fault is confirmed after code verification |

## When to Call a Pro

Call a qualified drive technician or Yaskawa-authorized service provider if you cannot locate the displayed code in any of your manuals, if the fault returns immediately after reset, or if you find physical damage to the control board or option cards during inspection. Also call a professional if the drive has blown fuses or shows signs of overcurrent damage, because Yaskawa instructs against re-energizing without a full wiring and component check. A factory-trained technician has access to extended fault logs, parameter backup tools, and direct support channels that can decode non-standard or option-generated codes.

## See Also

- [Yaskawa GA800 E03 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e03-fault-code/)
- [Yaskawa VFD Fault CF — Causes & Fix](/posts/yaskawa-vfd-fault-cf/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/posts/yaskawa-ga800-error-uv1/)
- [Yaskawa GA800 E17 Fault - Causes & Fix](/posts/yaskawa-ga800-e17-fault-code/)
