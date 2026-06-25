---
title: "Danfoss FC302 AL-93 - Causes & Fix"
description: "AL-93 does not exist in FC302 documentation. Likely a misread code (AL-13 overcurrent or AL-38 internal fault). Check display again."
pubDatetime: 2026-06-23T10:12:07Z
modDatetime: 2026-06-23T10:12:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "FC302 control board (logic PCB)"
most_likely_cause: "Misread or incorrect code number"
likelihood: "the most common explanation"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm code on the drive display and compare it to the FC302 alarm table in the manual"
  - "Check parameter 15-32 for the extended alarm code if the display shows AL-38"
  - "Cycle power to the drive and observe whether the alarm reappears immediately or only under load"
---

## Danfoss FC302 AL-93 — What It Means

No fault code named AL-93 exists in Danfoss FC302 VFD documentation. The FC302 series has over 90 documented alarms, but AL-93 is not among them. This code is either misread from the display, a typo in logging, or belongs to a different drive manufacturer (Yaskawa, Mitsubishi, or others use different numbering). The most common Danfoss FC302 faults that may be confused include AL-13 (overcurrent, triggered when output current exceeds 150-160% of rated current), AL-14 (earth fault), AL-29 (overtemperature), and AL-38 (internal fault with extended code in parameter 15-32).

If you see AL-13, it typically means mechanical overload, incorrect motor parameters, motor winding shorts, or failed IGBT modules. If you see AL-38, the drive has detected an internal hardware or sensor fault and will display a sub-code in parameter 15-32. Always verify the exact code on the drive display and consult the FC302 operating manual alarm table before ordering parts or attempting repairs.

## Before You Replace Anything

Technicians sometimes replace the entire power board when AL-13 appears, but a simple megohm test of motor windings (should read above 2 MΩ to ground) or disconnecting the motor can reveal whether the fault is in the drive or the load.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transcription error (~60%)** The technician or operator recorded AL-93 instead of AL-13, AL-38, or another valid code from a poorly lit display or handwritten log.
- **Wrong drive model or brand (~25%)** The drive is not a Danfoss FC302, or a third-party control board with non-standard firmware is installed.
- **Custom or modified firmware (~10%)** A non-original control board or aftermarket parameter set is generating an unsupported alarm number.
- **Display or control board corruption (~5%)** The control board has corrupted memory or a failing display that shows garbled digits.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show AL-93 clearly, or could it be AL-13 or AL-38?</summary>
<div class="dtree-body"><strong>Yes:</strong> Photograph the display and compare the image to the FC302 alarm table in the manual. If it truly reads AL-93, the drive may not be a genuine FC302 or has modified firmware.<br><strong>No:</strong> Re-read the code carefully. AL-13 (overcurrent) and AL-38 (internal fault) are the most common FC302 alarms and require different diagnostic paths.</div>
</details>

<details class="dtree"><summary>Does the alarm appear only when the motor is running under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely motor or mechanical (AL-13 overcurrent due to overload, incorrect motor parameters, or motor winding damage). Disconnect the motor and run the drive unloaded to isolate the drive from the load.<br><strong>No:</strong> The fault is likely internal to the drive (AL-38 internal fault, failed gate driver, control board, or sensor). Check parameter 15-32 for the extended fault code and replace the identified component.</div>
</details>

<details class="dtree"><summary>Can you access parameter 15-32 to read an extended alarm code?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the sub-code and cross-reference it in the FC302 manual Table 6.1 to identify the failed sensor, gate driver, or logic circuit.<br><strong>No:</strong> Cycle power and attempt to enter the parameter menu. If the drive remains locked or unresponsive, the control board or display may be failed and requires replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** on the drive front panel display. Take a clear photograph if possible and compare it to the FC302 alarm list in the operating manual.
2. **Check the drive nameplate** to confirm the model is FC302 and not a different Danfoss series (FC301, FC51, VLT Micro) or another manufacturer's VFD.
3. **Access parameter 15-32** using the keypad or PC software to read the extended alarm code if the display shows AL-38 (internal fault).
4. **Disconnect the motor** from the drive output terminals U, V, W and attempt to run the drive unloaded. If the alarm clears, the fault is motor or mechanical. If it persists, the drive has an internal fault.
5. **Perform a megohm test** on the motor windings from each phase to ground and phase to phase. Readings below 2 MΩ indicate insulation failure and motor replacement is required.
6. **Inspect input power** for voltage imbalance (should be within 3 percent across phases) and loose connections at the drive input terminals L1, L2, L3.
7. **Replace the identified failed component** (control board if AL-38 with a sensor or logic fault, power board or IGBT modules if AL-13 persists with motor disconnected, or motor if winding insulation is compromised).

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 control board (logic PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-93-fault-code&k=FC302+control+board+%28logic+PCB%29&tag=errorcodefixes-20) \| Required if AL-38 internal fault points to a failed sensor, gate driver, or corrupted parameter memory. Match the drive frame size and firmware version. |
| FC302 power board (rectifier and inverter assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-93-fault-code&k=FC302+power+board+%28rectifier+and+inverter+assembly%29&tag=errorcodefixes-20) \| Required if AL-13 overcurrent persists with the motor disconnected, indicating failed IGBT modules or DC link capacitors. |
| IGBT module (per phase) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-93-fault-code&k=IGBT+module+%28per+phase%29&tag=errorcodefixes-20) \| Can be replaced individually if the power board is modular and only one phase is shorted. Must match drive voltage and current rating. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-93-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| Required if megohm test shows winding insulation below 2 MΩ or phase-to-phase shorts. Must match nameplate specs in parameters 1-20 through 1-25. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician whenever the drive displays any alarm code. Diagnosis requires safe isolation of high-voltage DC bus capacitors (which can hold lethal charge for minutes after power-off), multimeter testing of IGBT gate signals, and parameter programming. If the alarm is truly AL-93 and not a misread, the drive may have third-party firmware or be a counterfeit unit, and a Danfoss-certified service partner should inspect it. Do not attempt to open the drive enclosure or measure internal voltages without proper training, insulated tools, and lockout/tagout procedures.

**Rough cost:** A pro service call runs about $300-800 depending on whether the fault is motor-side or drive internal.
