---
title: "Yaskawa GA800 A.143 Fault - Causes & Fix"
description: "A.143 is not a standard GA800 fault code. Confirm the exact display text and check your fault history menu before diagnosing further."
pubDatetime: 2026-06-09T11:35:48Z
modDatetime: 2026-06-09T11:35:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 control board"
most_likely_cause: "Misread or misrecorded fault code"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.143 Fault — What It Means

A.143 does not appear in Yaskawa GA800 documentation as a standard alarm code. GA800 drives typically display alphanumeric fault names such as oC, ov, GF, or CPFxx rather than decimal-style codes like A.143. This means the code may be misread from the keypad display, or it may belong to a different Yaskawa series or a parameter/monitoring screen rather than the fault list.

Before attempting any repair, confirm the exact text shown on the keypad, including all letters and punctuation. Pull the fault history from the drive's monitor or history menu and compare the alarm name to the GA800 manual specific to your drive model. If the code is actually a control-circuit or overvoltage fault with a similar appearance, follow the applicable Yaskawa diagnostic path for wiring, parameter checks, and power cycling before replacing any hardware.

## Before You Replace Anything

Technicians sometimes replace the control board or entire drive without first verifying the exact alarm code and checking wiring, motor cable length, and deceleration parameters. Always pull the fault history and compare the displayed code to your GA800 manual before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread or misrecorded fault code (~40%)** The keypad display may have been read incorrectly, or the code may belong to a parameter screen rather than a fault alarm.
- **Code from a different Yaskawa series (~25%)** The displayed code may be valid for a different Yaskawa VFD family but not listed in GA800 documentation.
- **Control board communication error (~15%)** A corrupted display or keypad communication fault can show unexpected codes that are not in the alarm table.
- **Option card or expansion module fault (~10%)** An installed option card may generate a code not listed in the base GA800 manual.
- **Firmware or parameter corruption (~10%)** Parameter memory corruption or a firmware mismatch can display non-standard alarm codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad show the exact same code each time you power-cycle the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is persistent and is most likely a real alarm or a hardware communication issue. Pull the fault history from the monitor menu and compare the code to your GA800 manual.<br><strong>No:</strong> The code may be transient noise or a display glitch. Record the code, pull the fault history, and verify wiring connections before cycling power again.</div>
</details>

<details class="dtree"><summary>Do you have any option cards or expansion modules installed?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the option card manual for additional alarm codes specific to that module, as those codes may not appear in the base GA800 documentation.<br><strong>No:</strong> The code should be in the base GA800 alarm list. Confirm the exact display text and compare it character-by-character to the manual.</div>
</details>

<details class="dtree"><summary>Can you pull a fault history log from the drive's monitor menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review the fault history for the actual alarm name and timestamp. Use that name to look up the fault in the GA800 manual and follow the documented troubleshooting steps.<br><strong>No:</strong> Write down the exact keypad display text, power-cycle the drive, and watch for the code to reappear. Take a photo of the display and consult the GA800 manual or a qualified technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Write down the exact display text** including all letters, numbers, and punctuation as shown on the keypad, and take a photo if possible.
2. **Access the fault history menu** on the keypad (consult your GA800 manual for the specific monitor parameter number) and record all stored alarm codes and timestamps.
3. **Compare the recorded code** to the alarm list in your GA800 manual, checking character-by-character for matches or similar codes.
4. **Power-cycle the drive** by removing control and main power, waiting 60 seconds, then restoring power and observing whether the same code reappears.
5. **Inspect all wiring and terminals** at the drive, motor, and control inputs for loose connections, corrosion, or damage, and verify motor cable length and routing meet Yaskawa guidelines.
6. **Check option card documentation** if any expansion modules are installed, as additional alarm codes may be listed in the option card manual rather than the base drive manual.
7. **Contact Yaskawa technical support or a qualified technician** with the exact code, fault history log, and drive model number if the code cannot be verified in the GA800 documentation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-143-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Only if a verified control-circuit fault persists after wiring and power-cycle checks. |
| Yaskawa GA800 keypad/operator interface | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-143-fault-code&k=Yaskawa+GA800+keypad%2Foperator+interface&tag=errorcodefixes-20) \| Replace if the display is corrupted or shows non-standard characters after a power cycle. |

## When to Call a Pro

Call a qualified technician or contact Yaskawa technical support if you cannot verify the displayed code in your GA800 manual, if the fault history menu is inaccessible, or if the code reappears after wiring inspection and power cycling. VFD troubleshooting requires familiarity with motor control parameters, AC drive wiring standards, and manufacturer-specific alarm definitions. A technician with Yaskawa experience can pull diagnostic data, compare the code to the correct manual for your firmware revision, and replace the control board or drive only after confirming the fault through proper testing.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [Yaskawa GA800 E09 Fault Code - Causes & Fix](/posts/yaskawa-ga800-vfd-e09-fault-code/)
- [Yaskawa GA800 E53 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e53-fault-code/)
- [Yaskawa A1000 oP Fault Code - Causes & Fix](/posts/yaskawa-a1000-vfd-op-fault-code/)
- [Yaskawa GA800 E67 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e67-fault-code/)
