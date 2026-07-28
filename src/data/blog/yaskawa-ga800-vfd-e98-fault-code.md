---
title: "Yaskawa GA800 E98 Fault Code - Causes & Fix"
description: "E98 is not a documented fault code for the GA800. Check your drive's actual display code and model nameplate, then consult the manual or Yaskawa."
pubDatetime: 2026-06-07T10:33:07Z
modDatetime: 2026-06-07T10:33:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board (model-specific)"
most_likely_cause: "Misread or corrupted display"
---

## What this code means
Yaskawa's GA800 documentation does not list an E98 fault code in its standard alarm and fault tables. Fault codes on the GA800 are model-specific and displayed on the keypad or HMI as text or numeric codes that correspond to entries in the maintenance and troubleshooting manual. Because E98 does not appear in verified Yaskawa reference material for the GA800 series, it is possible the code is being misread, the display is corrupted, or the drive is from a different series or manufacturer. The GA800 troubleshooting process always begins with reading the exact fault text or number from the display, checking the elementary wiring diagram for that model, and referencing the code in the official manual before attempting any repair. If your drive shows a code that looks like E98, verify the characters on the display, note the full model and spec number from the nameplate, and contact Yaskawa technical support with that information. Attempting repairs without confirming the actual fault can lead to unnecessary parts replacement and extended downtime.

## Before You Replace Anything

Technicians sometimes replace the main control board when the drive will not run, but many GA800 faults are caused by open safety circuits (Safe Torque Off jumper missing or safety chain open) or parameter settings. Always verify the exact fault code in the manual and check the STO terminals before ordering boards.

## Common Causes

- **Misread or corrupted display** The alphanumeric display on the keypad may be showing a partial or corrupted code due to a failing display, loose ribbon cable, or electrical noise.
- **Code from a different drive series** Yaskawa manufactures many VFD families (A1000, V1000, P1000, etc.) and each has its own fault code list, so E98 may be valid on a different model but not the GA800.
- **Open Safe Torque Off circuit** The GA800 includes STO as a standard safety function, and if the STO terminals are not jumpered or the external safety chain is open, the drive will not enable and may show an alarm.
- **Communication or parameter fault** If the drive is configured for fieldbus control or has custom parameter sets, a communication loss or parameter conflict can produce an unfamiliar alarm code.
- **Hardware fault not in standard tables** Rare internal faults (EEPROM corruption, board-level damage) can produce non-standard codes that require factory support to decode.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad display show clear, stable characters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the exact code, including all letters and numbers, and check the maintenance manual index for that code. If it is not listed, note the drive model and serial number and contact Yaskawa support.<br><strong>No:</strong> Power-cycle the drive and inspect the keypad ribbon cable for loose connections. A flickering or garbled display usually means a keypad or control board hardware issue, not a process fault.</div>
</details>

<details class="dtree"><summary>Are the Safe Torque Off (STO) terminals jumpered or connected to a safety relay?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify continuity across the STO circuit with a meter. If the circuit is open, the drive will not enable even if no fault is displayed. Check your wiring diagram for the correct STO configuration.<br><strong>No:</strong> Install the STO jumper per the GA800 installation manual. The drive will not run without a closed STO circuit, and this can appear as an enable fault or safety alarm.</div>
</details>

<details class="dtree"><summary>Is the drive part of a networked or fieldbus system?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check for communication faults (bUS, CF, or similar) on the display. Loss of network communication can prevent the drive from running and may display a code related to the option card or parameter settings.<br><strong>No:</strong> Verify that parameters are set for local (keypad or analog) control. Conflicting control-source settings can lock out the drive and produce parameter-related alarms.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive at the main disconnect, then wait at least five minutes for the DC bus capacitors to discharge before opening any covers.
2. **Photograph the exact fault code** displayed on the keypad, including all characters, and note the drive model number and spec code from the nameplate on the side or bottom of the enclosure.
3. **Locate the maintenance and troubleshooting manual** for your specific GA800 model (available from Yaskawa's website by entering the model number) and search the fault code table for the exact code you photographed.
4. **Check the Safe Torque Off terminals** on the control terminal strip. If no external safety relay is installed, verify that the factory STO jumper is in place and making good contact.
5. **Inspect the keypad and ribbon cable** for physical damage, corrosion, or loose connections. A failing keypad can display corrupted codes that do not match any manual entry.
6. **Review parameter settings** related to control source, communication options, and safety functions. Use the keypad or DriveWizard Plus software to compare current parameters against the default set or a known-good backup.
7. **Contact Yaskawa technical support** with the exact fault code, drive model, spec number, and application details. If the code is not in the manual, factory support can decode internal diagnostic codes and recommend the correct repair procedure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e98-fault-code&k=Yaskawa+GA800+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Order by full drive model and revision. Requires parameter upload/download and may need factory support to configure. |
| Yaskawa keypad or remote operator (JVOP-180 or compatible) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e98-fault-code&k=Yaskawa+keypad+or+remote+operator+%28JVOP-180+or+compatible%29&tag=errorcodefixes-20) \| Replacement keypad for corrupted display. Verify compatibility with your GA800 model and firmware version. |

## When to Call a Pro

Call a qualified industrial electrician or Yaskawa-certified service technician immediately if you cannot find the fault code in your drive's manual, if the display is corrupted or flickering, or if the drive has been exposed to electrical surges or environmental contamination. VFD troubleshooting requires interpreting wiring diagrams, measuring high-voltage DC bus levels, and working safely around lethal voltages that remain present even after input power is removed. A technician with DriveWizard Plus software can read detailed fault logs, compare parameter sets, and contact Yaskawa support with the correct diagnostic data. Attempting to swap boards or adjust parameters without confirmed fault information often leads to extended downtime and additional damage. If your drive is under warranty or covered by a service contract, contact Yaskawa or your distributor before opening the enclosure.

**Rough cost:** A pro service call runs about $200–500 for service call and diagnosis, plus parts if needed.
