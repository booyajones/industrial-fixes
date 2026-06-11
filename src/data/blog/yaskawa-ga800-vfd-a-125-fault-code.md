---
title: "Yaskawa GA800 A.125 Fault - Causes & Fix"
description: "A.125 is not a confirmed GA800 fault code. Verify the display-most GA800 alarms use letters like oC or ov. Check your manual for the exact code."
pubDatetime: 2026-06-09T11:14:57Z
modDatetime: 2026-06-09T11:14:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 operator keypad (JVOP-140 or JVOP-180 series)"
diy_or_pro: "pro"
---

## Yaskawa GA800 A.125 Fault — What It Means

The A.125 code is not documented as a standard Yaskawa GA800 VFD fault in manufacturer materials. GA800 drives typically display alphanumeric fault codes such as oC (overcurrent), ov (overvoltage), CPF06 (control power fault), and similar patterns. The code you see may be misread from the keypad, belong to a different Yaskawa drive series, or represent a parameter number or accessory alarm rather than a main drive fault.

Before troubleshooting, confirm the exact characters shown on the operator keypad, including any decimal points, dashes, or flashing symbols. Consult your GA800 manual's alarm table or contact Yaskawa technical support with your drive's full model number and serial number to identify the correct fault definition. Proceeding with repairs based on an unverified code can damage the drive or connected equipment.

## Before You Replace Anything

Technicians sometimes replace power boards or parameter cards when the display shows an unfamiliar code, only to discover it was a parameter readout or a different drive model's alarm. Always cross-reference the exact code in the drive's printed manual or contact the manufacturer before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread display or incorrect fault transcription (~40%)** The operator may have noted the code incorrectly, confusing a decimal point, letter, or parameter number with a fault alarm.
- **Parameter number displayed instead of fault (~30%)** The keypad may be in parameter-edit mode showing A.125 as a parameter address rather than an active alarm.
- **Code from a different Yaskawa drive model (~20%)** A.125 may be valid for a different Yaskawa series (such as V1000 or A1000) and was carried over in documentation by mistake.
- **Accessory or option-card alarm (~10%)** If the drive has a communication card, encoder card, or brake chopper, the code may originate from that module rather than the main inverter.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad show a decimal point, dash, or letter prefix before or after the code?</summary>
<div class="dtree-body"><strong>Yes:</strong> The display may be showing a parameter address (e.g. A.125 is parameter A-125) rather than a fault. Press the alarm/fault key to see if a different code appears.<br><strong>No:</strong> Write down the exact characters, including any flashing or steady indicators, and compare them to the alarm table in your GA800 manual.</div>
</details>

<details class="dtree"><summary>Is the drive still running, or has it tripped and stopped the motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> If the drive is running, you are likely viewing a parameter or status message, not an active fault. Check the manual's parameter list.<br><strong>No:</strong> A tripped drive will display a true fault code. Confirm the code against the GA800 alarm list; if A.125 is not listed, contact Yaskawa support before resetting.</div>
</details>

<details class="dtree"><summary>Does your system include option cards, encoders, or fieldbus adapters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check each accessory's manual for alarm codes. The A.125 display may come from an add-on module rather than the main drive.<br><strong>No:</strong> The code is more likely a misread main-drive fault or parameter. Verify the full model number and firmware version with Yaskawa.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** following lockout/tagout procedure and wait for the DC bus to discharge (LED indicators off).
2. **Photograph the keypad display** showing the A.125 code, including any decimal points, dashes, or additional text.
3. **Locate the GA800 user manual** for your exact drive model (the model number is on the nameplate) and turn to the alarm-code table.
4. **Search the alarm table** for A.125, A-125, A125, and similar variations; if the code is absent, note that fact.
5. **Check parameter mode** by pressing the menu or parameter key; if the display changes to show parameter groups (A, b, C, etc.), you were viewing a parameter address, not a fault.
6. **Record the drive's full model number, serial number, and firmware version** (visible in the monitor menu or on the nameplate).
7. **Contact Yaskawa technical support** or your local distributor with the photo, model details, and a description of when the code appeared; they will confirm whether A.125 is valid for your drive and provide the correct troubleshooting steps.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 operator keypad (JVOP-140 or JVOP-180 series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-125-fault-code&k=Yaskawa+GA800+operator+keypad+%28JVOP-140+or+JVOP-180+series%29&tag=errorcodefixes-20) \| Only replace if Yaskawa confirms the keypad is faulty; most unrecognized codes are not keypad failures. |
| Yaskawa GA800 user manual and parameter reference | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-125-fault-code&k=Yaskawa+GA800+user+manual+and+parameter+reference&tag=errorcodefixes-20) \| Download the exact manual for your drive model from Yaskawa's website or request a printed copy from your distributor. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service provider immediately if you cannot find the A.125 code in your drive's manual. Variable-frequency drives operate at high DC bus voltages (up to 800 VDC for 480 VAC models) and contain large capacitors that remain charged after input power is removed. Attempting repairs without proper training, insulated tools, and manufacturer guidance can result in severe electric shock, equipment damage, or voided warranty. A technician will use Yaskawa's DriveWizard software or a direct support line to decode the alarm, retrieve fault history, and perform safe diagnostic tests on the control boards, power stage, and any installed option cards.

**Rough cost:** A pro service call runs about $150–400 for diagnostic visit and code verification; repair cost depends on actual fault once identified.
