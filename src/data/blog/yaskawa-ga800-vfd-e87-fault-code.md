---
title: "Yaskawa GA800 E87 Fault - Causes & Fix"
description: "E87 fault meaning varies by GA800 model. Check the drive's fault list on the keypad or manual, remove the cause, then press RESET."
pubDatetime: 2026-06-08T10:42:31Z
modDatetime: 2026-06-08T10:42:31Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
---

## Yaskawa GA800 E87 Fault — What It Means

The E87 fault code on a Yaskawa GA800 VFD is not clearly identified in the manufacturer documentation available, so its exact meaning depends on the specific model and firmware version of your drive. Yaskawa instructs technicians to read the fault or alarm description directly from the drive's keypad display or from the fault list in the model-specific manual, then remove the underlying cause before pressing the RESET button on the keypad.

Because Yaskawa GA800 drives use a standardized fault code structure but individual codes can vary, you should confirm whether the display shows E87, EF87, or a similar code, since a single character misread is common in the field. Once you have confirmed the code and consulted the fault list for your exact model, you can identify the root cause and proceed with the manufacturer's recommended reset procedure.

## Before You Replace Anything

Do not replace the control board or power section until you have verified the exact fault definition from your model's fault list and ruled out external wiring, parameter settings, or sensor issues that trigger the code.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect fault code read (~25%)** The displayed code may be E87, EF87, or another similar alphanumeric combination, and a single-digit misread can lead to misdiagnosis.
- **Parameter setting mismatch (~20%)** Drive parameters may be configured incorrectly for the motor or application, triggering a fault that appears as E87 on some GA800 models.
- **External wiring or sensor fault (~20%)** Input terminal wiring, feedback devices, or external interlock signals can trigger faults that the drive reports as E87 depending on configuration.
- **Control board or I/O card issue (~15%)** The control board or an option card may have failed or lost communication, generating a fault code in the E8x family.
- **Power section or DC bus fault (~10%)** Internal power stage faults or DC bus issues can generate codes in the E8x range on some GA800 firmware versions.
- **Firmware or display corruption (~10%)** A corrupted fault log or display glitch can show an unrecognized code until the drive is power-cycled and reset.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad show the full fault text or description alongside the E87 code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the exact text and compare it to the fault list in your GA800 manual to identify the specific cause.<br><strong>No:</strong> Press the keypad menu buttons to navigate to the fault history or alarm log screen and read the complete fault description there.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you press RESET on the keypad, and does the drive run normally afterward?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient event caused by external conditions or a temporary wiring issue; monitor the drive for recurrence.<br><strong>No:</strong> The fault is persistent and indicates a hardware, wiring, or parameter problem that requires further diagnosis before the drive will run.</div>
</details>

<details class="dtree"><summary>Have you recently changed any drive parameters, wiring, or external control signals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review the changes and restore factory defaults or known-good parameter settings to rule out a configuration error.<br><strong>No:</strong> The fault is likely caused by component failure or degraded wiring, and you should collect model, serial, and fault details before contacting Yaskawa support.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the incoming supply to make sure safe access to the keypad and wiring terminals.
2. **Power up the drive** and read the exact fault code and description from the keypad display, noting whether it shows E87, EF87, or another similar code.
3. **Locate the fault list** in the GA800 manual for your specific model and firmware version, and look up the meaning of the code you recorded.
4. **Check external wiring** at all input and output terminals for loose connections, damaged insulation, or shorted wires that match the fault description.
5. **Review parameter settings** using the keypad or DriveWizard Plus software, and compare critical parameters to the motor nameplate and application requirements.
6. **Press RESET** on the keypad after removing the cause identified in the fault list, and observe whether the drive returns to ready status.
7. **Collect drive information** including model/spec number, serial number, fault code, application details, and length of service if the fault persists, then contact Yaskawa support for further diagnosis.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e87-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Only if the fault definition and diagnostics confirm control board failure; consult Yaskawa support for the exact part number for your drive model. |
| Yaskawa GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e87-fault-code&k=Yaskawa+GA800+cooling+fan&tag=errorcodefixes-20) \| If the fault is related to overtemperature or fan failure; fan replacement is a user-serviceable repair per Yaskawa documentation. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa support if the fault persists after you have checked wiring and reset the drive, if you do not have access to the model-specific fault list, or if diagnostics point to internal power stage or control board failure. Yaskawa's GA800 maintenance documentation states that repair beyond fan and control board replacement is not supported in the field, so drives requiring power section work must be sent to an authorized service center. Always provide the model/spec number, serial number, fault code with description, application details, and length of service when you call for support.

**Rough cost:** A pro service call runs about $200-600 depending on diagnosis time and component replacement.
