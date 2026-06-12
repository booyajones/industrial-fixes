---
title: "Yaskawa GA800 A.117 Fault - Causes & Fix"
description: "A.117 is a parameter setup error alarm on the GA800 VFD. The most likely fix is checking motor nameplate data and control mode settings."
pubDatetime: 2026-06-08T11:11:22Z
modDatetime: 2026-06-08T11:11:22Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Incorrect motor nameplate data or control-mode mismatch"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "GA800 control board"
---

## Yaskawa GA800 A.117 Fault — What It Means

The A.117 alarm on a Yaskawa GA800 variable frequency drive is a parameter configuration error, not a hardware failure. The drive has detected that one or more setup values are invalid or inconsistent with the motor and control circuit configuration you have programmed. Unlike a trip fault that shuts down operation immediately due to a power-stage problem, this alarm tells you the drive's internal logic has found a mismatch in the parameters you entered during commissioning or after a recent change.

In practical terms, A.117 appears after initialization, a parameter reset, or when you change the control method or motor data without updating related settings. The drive will not run until you correct the configuration and press RESET on the keypad. Yaskawa's documentation groups A.117 under alarm/error display behavior and directs the technician to remove the cause of the alarm before resetting the drive. This code almost never means you need to replace hardware. Instead, it points to incomplete or conflicting programming in the drive's parameter memory.

## Before You Replace Anything

Technicians sometimes replace the control board or keypad when A.117 appears, but this alarm is almost always a programming issue. Before ordering any parts, review the motor nameplate entries and control wiring against the actual installation and check for recent parameter changes.

[Jump to Fix](#fix)

## Common Causes

- **Motor nameplate data mismatch (~35%)** The horsepower, voltage, current, or frequency values entered in the motor parameters do not match the actual motor on the machine, causing the drive to reject the configuration.
- **Control mode and wiring mismatch (~30%)** The programmed command source (keypad, digital input, or communication card) does not match the physical wiring or the drive expects a feedback signal that is not connected.
- **Incomplete initialization after parameter reset (~20%)** A factory reset or partial parameter change left the drive with an invalid combination of settings that were not fully reconfigured for the application.
- **Invalid parameter combination introduced during programming (~10%)** Changing the application preset, basic setup group, or control method created a conflict between dependent parameters that the drive will not accept.
- **Loose or incorrectly seated option card (~5%)** If an option card is installed and the configuration depends on it, a poor connection or wrong card type can trigger a parameter error alarm.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did the alarm appear immediately after you changed a parameter or performed a reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The new setting likely conflicts with another parameter or the motor data. Review the parameter you changed and any related settings in the same group, then consult the GA800 manual for valid combinations.<br><strong>No:</strong> The alarm may have appeared after a power cycle or installation change. Proceed to verify the motor nameplate data and control wiring match the drive configuration.</div>
</details>

<details class="dtree"><summary>Does the motor nameplate voltage, current, and frequency exactly match the values entered in the drive's motor parameters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor data is correct. Check that the control mode setting matches your actual run/stop wiring and that any required feedback devices (encoder, PTC, etc.) are connected if enabled in parameters.<br><strong>No:</strong> Enter the correct motor nameplate data into the drive, save the parameters, and press RESET. If the alarm clears, the mismatch was the cause.</div>
</details>

<details class="dtree"><summary>Is an option card (communication, I/O expansion, or feedback) installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power down the drive, reseat the option card firmly in its slot, and verify the card type matches the configuration in the drive parameters. A loose or wrong card can cause parameter alarms.<br><strong>No:</strong> The issue is in the base parameter setup. Review the control method, application preset, and any recent changes, or restore a known-good parameter file if available.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the alarm and all displayed conditions** on the keypad before changing anything, including which parameters were recently modified and the current control mode setting.
2. **Power down the drive** and verify the motor nameplate (voltage, current, frequency, horsepower) against the values entered in the motor parameter group in the drive.
3. **Check the elementary diagram and actual wiring** to confirm the run/stop command source, speed reference input, and any feedback devices match the control mode and input configuration programmed in the drive.
4. **Review recent parameter changes** and look for invalid combinations, especially in the basic setup, application preset, and control method groups. Consult the GA800 parameter manual for dependencies.
5. **If an option card is installed**, power down, remove and reseat the card, and verify the card type and parameter settings for that card match the installed hardware.
6. **Correct the conflicting parameter or motor data**, save the changes, then press RESET on the keypad to clear the alarm and attempt to run the drive.
7. **If the alarm returns immediately**, perform a controlled reinitialization to factory defaults and methodically re-enter the correct motor and control parameters, or restore a known-good parameter file if you have a backup.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-117-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Only if the alarm persists after all parameter checks and you confirm a hardware fault (extremely rare for A.117). |
| GA800 keypad | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-117-fault-code&k=GA800+keypad&tag=errorcodefixes-20) \| Only if the display is damaged or unresponsive and you cannot access parameters to correct the configuration. |

## When to Call a Pro

Call a qualified VFD technician or controls integrator if you are not familiar with variable frequency drive programming and parameter structures. A.117 requires understanding the GA800 parameter map, motor data entry, control wiring, and the interaction between application presets and control modes. If you have changed parameters and cannot restore a working configuration, a technician with the full GA800 manual and parameter backup tools can quickly diagnose the conflict and reprogram the drive. Also call a professional if the alarm persists after you have verified all motor data and wiring, because at that point you may need to check the control board seating, option card compatibility, or perform a firmware update. Do not replace hardware until programming is confirmed correct.

**Rough cost:** A pro service call runs about $150–400 for a service call to reprogram and verify the drive, assuming no hardware is damaged.
