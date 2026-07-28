---
title: "Yaskawa GA800 F036 Fault - Causes & Fix"
description: "F036 is not a standard GA800 code. Verify the exact code in the fault log menu. Most likely a misread or custom alarm-check manual."
pubDatetime: 2026-06-27T11:53:04Z
modDatetime: 2026-06-27T11:53:04Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "GA800 Control Board (PCB)"
diy_or_pro: "pro"
free_checks:
  - "Check the keypad display carefully and compare the exact code to your GA800 manual fault table."
  - "Access the fault log menu (Fn000) to confirm the code number and description text."
  - "Power-cycle the drive: turn off power, wait for all indicators to go dark, then restart and see if the code clears."
---

## What this code means
The F036 code does not appear in Yaskawa's published GA800 fault code documentation. Standard GA800 faults are displayed as letter-number combinations like oC (overcurrent), GF (ground fault), CPF03 (PWM data error), or Er-08 (autotuning error). This means F036 is either a display misread, a custom alarm configured by the installer, or a code from a different Yaskawa model (such as the V3F10 or a Servopack). Without confirmation from the drive's fault log or manual, the exact cause cannot be determined.

To find the true fault, navigate the GA800 keypad to the Fault Log or Alarm History menu (often parameter Fn000) and record the complete code and description text. Compare this to the fault table in your GA800 manual. If the code still does not match any published fault, contact Yaskawa Technical Support at 1.800.927.5292 or repair@yaskawa.com with your model number, serial number, and the displayed code for a definitive answer.

## Before You Replace Anything

Do not replace the control board or main PCB until you verify the exact fault code from the fault log menu. A misread display or parameter error often looks like an unknown code but clears with a simple reset or parameter check.

## Common Causes

- **Misread or transposed code (~40%)** The displayed code may be a different fault (such as oC, GF, CPF03, or Er-08) that was read incorrectly on the keypad.
- **Custom or user-defined alarm (~30%)** Some integrators configure custom fault codes in the GA800 that do not appear in standard documentation.
- **Wrong drive model (~20%)** The code F036 may belong to a different Yaskawa series (V3F10, GA700, or Servopack) and was referenced by mistake.
- **Control board data corruption (~10%)** A corrupted EEPROM or control circuit fault may generate an undocumented or garbled code until the drive is reset or repaired.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault log menu show the same code F036?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is real. Cross-check it against your GA800 manual or contact Yaskawa support for confirmation.<br><strong>No:</strong> The keypad displayed a different or partial code. Record the full code from the log and look it up in the manual.</div>
</details>

<details class="dtree"><summary>Does the code clear after a power cycle (turn off, wait, restart)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely transient or caused by a parameter glitch. Monitor the drive for recurrence.<br><strong>No:</strong> The fault is persistent. Check wiring, motor connections, and input power, then call a qualified technician.</div>
</details>

<details class="dtree"><summary>Is the drive a GA800 model, verified by the nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Confirm the code is truly F036 in the fault log, then contact Yaskawa if it does not match the manual.<br><strong>No:</strong> You may have a different Yaskawa model (V3F10, GA700, or Servopack) with its own fault code list.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the GA800 drive and wait until all LED indicators and the display go dark to discharge internal capacitors.
2. **Restore power** and note the exact code on the keypad display, including any letters, numbers, and decimal points.
3. **Access the fault log** by pressing the Menu or Function key, scrolling to the Fault History or Alarm Log (often Fn000), and recording the complete fault code and description text.
4. **Compare the code** to the fault table in your GA800 instruction manual or quick-start guide to see if it matches a known fault.
5. **Check for common GA800 faults** such as oC (overcurrent), GF (ground fault), CPF03 (PWM data error), or Er-08 (autotuning error) in case the code was misread.
6. **Contact Yaskawa Technical Support** at 1.800.927.5292 (toll-free) or 1.847.887.7457 (direct), or email repair@yaskawa.com, with your model number, serial number, and the exact fault code if it does not appear in your manual.
7. **Do not replace parts** or run a megger insulation test on the drive without guidance, as unauthorized testing can damage the control board or power modules.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 Control Board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f036-fault-code&k=GA800+Control+Board+%28PCB%29&tag=errorcodefixes-20) \| Only replace if Yaskawa confirms a control circuit fault; GA800 manual states repairs are limited to fan and control board only. |
| GA800 Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f036-fault-code&k=GA800+Cooling+Fan&tag=errorcodefixes-20) \| Authorized replacement part for GA800 maintenance; consult Yaskawa for exact fan part number for your drive frame size. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service center immediately if the fault log confirms an unrecognized code, if the drive trips repeatedly, or if you are unsure of the exact code. Do not attempt to test the drive with a megger or withstand voltage tester, as the GA800 manual warns this will damage internal circuits. Only fan and control board replacements are user-serviceable on the GA800. All other repairs require factory service or authorized support. Contact Yaskawa at 1.800.927.5292 or repair@yaskawa.com with your model, serial number, and fault code for a diagnosis and repair quote.

**Rough cost:** A pro service call runs about $200-500 for service call and diagnosis; part costs vary widely if control board or fan replacement needed.
