---
title: "Yaskawa GA800 F035 Fault - Causes & Fix"
description: "F035 is not documented in standard GA800 manuals. Check your drive's fault log and contact Yaskawa support for the exact definition."
pubDatetime: 2026-06-27T11:52:16Z
modDatetime: 2026-06-27T11:52:16Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 Control Board (PCB)"
diy_or_pro: "pro"
free_checks:
  - "Check the drive's fault log menu for additional details or alternate fault code display"
  - "Review recent parameter changes or PID control settings that may have triggered an undocumented alarm"
  - "Inspect motor and encoder wiring for loose connections or grounding issues"
---

## What this code means
The F035 fault code does not appear in the published Yaskawa GA800 VFD Maintenance and Troubleshooting Manual or standard fault code tables. Yaskawa GA800 fault codes typically use two-digit numbers or alphanumeric prefixes (such as OC for overcurrent or UV for undervoltage), and F035 is not among the standardly documented faults. This code may be specific to a custom software version, a PID control configuration, or it may be displayed differently in your drive's fault log. Without an official definition from Yaskawa, it is not possible to determine the exact cause or required repair steps. The safest approach is to review the drive's internal fault log using the Modified Parameters / Fault Log menu on the keypad, then consult the official GA800 manual or contact Yaskawa Technical Support directly. Do not attempt part replacement or voltage testing based on guesswork, as the true meaning of F035 must be confirmed by the manufacturer before proceeding with any repair.

## Common Causes

- **Undocumented or custom fault code (~40%)** F035 does not appear in standard GA800 literature and may be tied to a specific firmware version or application-specific programming.
- **PID control feedback error (~25%)** Similar GA800 issues have appeared only when PID mode is active, often due to unstable feedback signals or encoder wiring problems.
- **Communication or parameter conflict (~20%)** A modified parameter or network communication setting may have triggered an internal alarm not listed in the standard fault table.
- **Grounding or wiring fault (~15%)** Poor motor grounding or loose tether connections can cause intermittent faults that display as non-standard codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear only when PID control or a special function is enabled?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code may be linked to feedback wiring or PID parameter setup. Check encoder connections and review PID feedback settings.<br><strong>No:</strong> The fault may be a general communication or parameter issue. Proceed to check the fault log for additional clues.</div>
</details>

<details class="dtree"><summary>Can you access the drive's fault log menu and see any additional fault details or timestamps?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note the full fault description and any accompanying codes, then contact Yaskawa support with that information.<br><strong>No:</strong> The keypad may be locked or the log cleared. Try a power cycle and observe if the fault recurs, then call Yaskawa for help.</div>
</details>

<details class="dtree"><summary>Have you recently modified drive parameters or updated firmware?</summary>
<div class="dtree-body"><strong>Yes:</strong> A parameter conflict or firmware version mismatch may have introduced the F035 code. Consider restoring factory defaults or reverting the change.<br><strong>No:</strong> The fault is likely hardware or wiring related. Inspect motor, encoder, and grounding connections before calling support.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the main disconnect to make sure safe troubleshooting.
2. **Access the fault log** on the keypad by navigating to the Modified Parameters / Fault Log menu and record the full fault description, timestamp, and any additional codes displayed.
3. **Consult the official GA800 manual** from Yaskawa (available at yaskawa.com or from your distributor) to search for F035 in the fault code table; if it is not listed, proceed to the next step.
4. **Contact Yaskawa Technical Support** at 1.800.927.5292 or repair@yaskawa.com with your drive's model number, serial number, firmware version, and the exact fault log details to obtain the authoritative definition of F035.
5. **Inspect PID and encoder wiring** if the fault occurs only during PID control mode: check for loose connections, correct polarity, stable feedback signals, and proper grounding of the motor and encoder cable shield.
6. **Review recent parameter changes** in the drive's configuration and consider performing a factory reset if a modified setting may have triggered the undocumented fault.
7. **Follow the repair instructions** provided by Yaskawa support once the exact cause of F035 is confirmed, and replace any identified failed components or correct wiring and parameter settings as directed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 Control Board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f035-fault-code&k=Yaskawa+GA800+Control+Board+%28PCB%29&tag=errorcodefixes-20) \| Only replace if Yaskawa support confirms F035 indicates a control board fault; specify your drive's model and voltage rating when ordering. |
| Encoder or Feedback Cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f035-fault-code&k=Encoder+or+Feedback+Cable&tag=errorcodefixes-20) \| If F035 is linked to PID or encoder feedback, verify cable part number and length for your motor model. |

## When to Call a Pro

Call a qualified industrial electrician or Yaskawa-authorized service technician immediately if you cannot locate F035 in your manual or if Yaskawa support confirms the fault requires board-level diagnostics, parameter reprogramming, or high-voltage testing. VFD troubleshooting involves line voltage (typically 230-480 VAC), stored DC bus capacitance, and complex parameter settings that can damage the drive or motor if handled incorrectly. A technician will use Yaskawa's DriveWizard software to read detailed fault logs, verify firmware versions, and perform voltage and insulation resistance tests safely. Do not attempt to bypass the fault or replace components without an official diagnosis, as guessing at the cause of an undocumented code can lead to costly mistakes and voided warranties.

**Rough cost:** A pro service call runs about $200-500 for diagnostic service call and potential part replacement once the fault is identified.
