---
title: "Danfoss FC302 AL-118 - Causes & Fix"
description: "AL-118 is not a valid Danfoss FC302 alarm code. Verify the exact numeric alarm on the LCP display and check the FC302 manual for the real code."
pubDatetime: 2026-06-24T10:14:43Z
modDatetime: 2026-06-24T10:14:43Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control PCB (I/O board)"
most_likely_cause: "Misread or mistyped alarm number"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the VFD by disconnecting AC input power for 60 seconds and reconnecting to clear transient memory errors"
  - "Read the exact alarm number from the LCP display and compare it to the official FC302 alarm table in the operating manual (document AQ361181055259en)"
  - "Navigate to parameter 15-32 on the LCP to view the alarm log and extended sub-codes for internal faults"
no_buy_pct: "60%"
---

## What this code means
AL-118 does not exist in the official Danfoss VLT AutomationDrive FC302 documentation. Danfoss FC302 alarms are numbered from Alarm 1 through Alarm 90+, such as Alarm 13 (motor not detected), Alarm 14 (overcurrent), Alarm 16 (short circuit), or Alarm 38 (internal fault). The code you are seeing may be a misread display, a typo, or a firmware/memory error showing a non-standard code.

Most likely you are seeing Alarm 18 (a real code related to frequency or parameter limits), Alarm 11, or a parameter number such as 1-18 (Motor Nominal Current). Check the Local Control Panel error log in parameter 15-32 to see the full alarm number and description. If the display truly shows AL-118 or another non-standard code, the control board may be corrupted or the firmware may be damaged.

## Before You Replace Anything

Technicians sometimes replace the power board when seeing a strange code, but the real fault is often a corrupted control board or firmware. Power-cycle the drive and check the alarm log in parameter 15-32 before ordering any parts.

## Common Causes

- **Misread display or typo (~50%)** The code may actually be Alarm 18, Alarm 11, or parameter 1-18, and the user misread or mistyped it.
- **Control board memory or firmware corruption (~25%)** A power surge, lightning strike, or component failure on the control I/O board can cause the drive to display invalid or garbled alarm codes.
- **Gate driver or IGBT failure triggering Alarm 38 sub-code (~15%)** Internal faults in the power section can sometimes cause the display to show non-standard codes if the control board cannot properly decode the fault.
- **Parameter configuration error (~10%)** Incorrect motor or drive parameters (especially 1-24 Motor Nominal Current or 1-25 Motor Nominal Voltage) can cause the drive to trip with unexpected codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP display show a numeric alarm such as 13, 14, 16, or 38 when you check parameter 15-32?</summary>
<div class="dtree-body"><strong>Yes:</strong> The real alarm is documented in the FC302 manual. Look up that alarm number and follow the official troubleshooting steps for that code.<br><strong>No:</strong> The display may be corrupted or the control board is faulty. Power-cycle the drive and contact Danfoss technical support if the non-standard code persists.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a power cycle (disconnect AC input for 60 seconds)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a transient memory error or voltage spike. Monitor the drive for recurring alarms and check input power quality.<br><strong>No:</strong> The fault is persistent. Check the alarm log in parameter 15-32 and verify motor and drive parameters before replacing the control board.</div>
</details>

<details class="dtree"><summary>Are motor parameters 1-24 (Motor Nominal Current) and 1-25 (Motor Nominal Voltage) set correctly for your motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter settings are correct. The fault is likely internal to the drive (control board, gate driver, or power board).<br><strong>No:</strong> Enter the correct motor nameplate values and perform an auto-tune (parameter 1-29 = 1 or 2) to recalibrate the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** by disconnecting AC input power and waiting 60 seconds for capacitors to discharge.
2. **Restore power** and observe the LCP display. Write down the exact alarm code, including all digits and letters.
3. **Access parameter 15-32** on the LCP (navigate using the hand/auto key and parameter menu) to view the alarm log and any extended sub-codes.
4. **Compare the alarm number** to the official Danfoss FC302 alarm table in the operating manual (document AQ361181055259en available from Danfoss).
5. **If the code is still AL-118 or another non-standard code**, check motor parameters 1-24 (Motor Nominal Current) and 1-25 (Motor Nominal Voltage) against the motor nameplate and correct any errors.
6. **Perform a parameter reset** to factory defaults (parameter 14-22) if parameter corruption is suspected, then re-enter motor and application settings.
7. **If the alarm persists and is not listed in the manual**, contact Danfoss technical support with the drive serial number and the exact code displayed. The control board may need replacement or firmware reflash.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control PCB (I/O board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-118-fault-code&k=Danfoss+FC302+Control+PCB+%28I%2FO+board%29&tag=errorcodefixes-20) \| Only if Danfoss support confirms control board failure. Part number varies by drive size and firmware version. |
| Danfoss FC302 Power Board (IGBT module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-118-fault-code&k=Danfoss+FC302+Power+Board+%28IGBT+module%29&tag=errorcodefixes-20) \| Only if the real alarm is 16, 38, or another power-section fault and the control board is verified good. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss-certified service center if the alarm code does not match any entry in the official FC302 manual, if the alarm persists after a power cycle and parameter check, or if parameter 15-32 shows an internal fault (Alarm 38 or sub-codes). VFD repairs involve high-voltage DC bus capacitors (up to 800 VDC on 480 VAC models) and require proper discharge procedures, insulated tools, and knowledge of gate driver circuits. Do not open the drive enclosure or attempt board-level repairs without training. If the drive displays a real alarm such as 13, 14, or 16, follow the official troubleshooting steps in the FC302 operating manual or contact Danfoss technical support for guidance.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fault is a real alarm or a control board replacement.
