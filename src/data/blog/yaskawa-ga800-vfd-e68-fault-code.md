---
title: "Yaskawa GA800 E68 Fault - Causes & Fix"
description: "E68 is not a standard GA800 code in Yaskawa literature. Double-check the display for Er-11 or another code, then consult the drive manual."
pubDatetime: 2026-06-06T11:51:57Z
modDatetime: 2026-06-06T11:51:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
---

## Yaskawa GA800 E68 Fault — What It Means

E68 does not appear in the Yaskawa GA800 fault and alarm code lists available in manufacturer troubleshooting material. Yaskawa VFD fault codes can be easily misread on the display panel, particularly codes beginning with Er, E, or A. Before attempting any repair, verify the exact code shown on the drive display and consult the fault and alarm list in your GA800 manual. For example, Er-11 is a documented Motor Speed Error code that is visually similar but has completely different causes and corrective actions.

If your drive truly displays E68, it may be a custom alarm programmed for your specific application, or the display may be showing a partial or corrupted code due to control board or communication issues. Yaskawa troubleshooting guidance directs technicians to have the model and specification number, serial number, the exact fault or alarm code, a description of what the drive was doing when the fault occurred, the application type, and the time in service ready when diagnosing unfamiliar codes or contacting technical support.

## Before You Replace Anything

Technicians sometimes replace the control board when they cannot identify a fault code, but many unrecognized codes are actually misread standard codes or application-specific alarms that require only parameter changes. Always photograph the display, cross-reference the exact code in the drive manual, and check for custom alarm programming before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread fault code** The display shows Er-11, E6, E8, or another standard code that was misidentified as E68 due to viewing angle, partial display, or transcription error.
- **Custom application alarm** The integrator or machine builder programmed a user-defined alarm using E68 for a specific machine condition such as process feedback, external interlock, or sensor fault.
- **Control board communication fault** The keypad or display is not communicating correctly with the control board, causing the drive to show an incomplete or corrupted code.
- **Control board failure** Internal control circuitry has failed or corrupted, causing the drive to generate or display non-standard fault codes.
- **Display panel failure** The LCD segments or LED indicators are damaged or malfunctioning, making a valid code appear as E68.
- **Firmware or parameter corruption** Drive parameters or firmware have been corrupted by power loss, electrical noise, or improper upload, resulting in undefined alarm behavior.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show a clear, steady code, or is the display flickering, partial, or changing?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is likely real. Photograph it and compare against every code in the GA800 manual fault list to confirm E68 is truly shown, not a similar code.<br><strong>No:</strong> You have a display or control board communication problem. Power-cycle the drive, check keypad cable connections, and see if a valid code appears.</div>
</details>

<details class="dtree"><summary>Can you find E68 listed anywhere in the fault and alarm tables in your GA800 manual?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the corrective action given in the manual for that code.<br><strong>No:</strong> E68 is not a standard Yaskawa code. Check if your machine builder programmed a custom alarm, or contact Yaskawa technical support with your model, serial number, and application details.</div>
</details>

<details class="dtree"><summary>Did this fault appear immediately after parameter changes, a firmware update, or a power outage?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive parameters or firmware may be corrupted. Try restoring factory defaults (if safe for your application) or reloading a known-good parameter file.<br><strong>No:</strong> The fault is likely hardware-related. Inspect the control board and display for visible damage, check all control wiring and shielding, and prepare to call Yaskawa support or a qualified technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive safely** and follow lockout-tagout procedures. Wait for the DC bus capacitors to discharge (the charge indicator LED will go out).
2. **Photograph the drive display** exactly as shown, capturing the full code and any additional text or indicators. Take multiple photos from different angles to confirm each character.
3. **Locate the fault and alarm code list** in your GA800 manual (usually in the troubleshooting or appendix section) and compare every code on that list to your photo. Look especially for Er-11, E6, E8, A-codes, and codes with similar-looking characters.
4. **Check for custom alarms** by reviewing the parameter list in the drive or in your machine documentation. Custom alarms are often programmed in the H2, H3, or similar parameter groups and may use non-standard code numbers.
5. **Inspect the keypad and control board connections**. Remove and reseat the keypad cable, check for corrosion or damage on the connector pins, and verify that the keypad is firmly seated.
6. **Power the drive back on** and watch the display during startup. Note whether the code appears immediately, after a few seconds, or only when the drive tries to run. Record any additional information shown (frequency, current, DC bus voltage).
7. **Contact Yaskawa technical support** with your drive model and specification number (from the nameplate), serial number, the exact fault code as photographed, a description of when the fault occurs, your application type, and how long the drive has been in service. Have the elementary diagram and parameter list ready if available.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e68-fault-code&k=Yaskawa+GA800+control+board+%28PCB%29&tag=errorcodefixes-20) \| Only if Yaskawa support confirms board failure. Board part number is model-specific. |
| Yaskawa GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e68-fault-code&k=Yaskawa+GA800+cooling+fan&tag=errorcodefixes-20) \| If diagnostics point to thermal shutdown or fan fault. Confirm fan part number from your drive nameplate. |

## When to Call a Pro

Call a qualified industrial electrician or Yaskawa-certified technician immediately if you cannot verify the exact fault code, if the drive will not power up, if you see smoke, burning smells, or physical damage to the control board or power components, or if your application is safety-critical. VFD troubleshooting requires an understanding of three-phase power systems, motor control theory, and the ability to safely measure high DC bus voltages (often 300-800 VDC depending on input voltage). Yaskawa troubleshooting documentation emphasizes having the elementary diagram, fault code definition, and application details ready before beginning diagnostics. If E68 is confirmed as a non-standard code and you do not have machine-builder documentation explaining it, only the OEM or a technician familiar with your specific machine will be able to resolve it.

**Rough cost:** A pro service call runs about $150-400 depending on diagnostic time and whether a control board or fan replacement is needed.
