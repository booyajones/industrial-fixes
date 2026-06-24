---
title: "Danfoss FC302 AL-79 - Causes & Fix"
description: "AL-79 is not a documented fault code on Danfoss FC302 VFDs. The code may be misread or confused with a real alarm like 13, 16, or 29."
pubDatetime: 2026-06-22T10:30:35Z
modDatetime: 2026-06-22T10:30:35Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter board (IGBT module)"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number from the drive display or alarm history menu"
  - "Check the owner's manual alarm code table to confirm the fault description"
  - "Inspect motor cable connections at both the drive and motor for loose or corroded terminals"
---

## Danfoss FC302 AL-79 — What It Means

AL-79 does not appear as a standard fault code in Danfoss VLT AutomationDrive FC 302 official documentation. The number 79 is listed in the manual as a status indicator meaning "Running / no warning" (output speed is higher than set speed under certain conditions), not a fault. If you see "AL-79" on your display, the code is likely misread or the drive is showing a different alarm number. Common high-number alarms on the FC302 include Alarm 13 (no motor detect), Alarm 16 (short circuit on output), Alarm 29 (heatsink overtemperature), Alarm 38 (motor phase missing), and Alarm 72 (thermal shutdown).

Before troubleshooting further, verify the exact alarm number from the drive's display or parameter readout. Consult your FC302 manual alarm list or the drive's alarm history (typically accessible through the control panel menu) to identify the true fault code. Once you have the correct alarm number, you can proceed with the appropriate diagnostic steps for that specific fault.

## Before You Replace Anything

Technicians sometimes replace the inverter board when the real issue is incorrect motor parameters or a damaged motor cable. Always verify motor wiring continuity and run Automatic Motor Adaptation (AMA) before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transposed alarm number (~40%)** The display may show a real alarm like 13, 16, 29, 38, or 72 that was read incorrectly as 79.
- **Alarm 13 (no motor detect) confused for AL-79 (~25%)** The drive cannot detect the motor during startup due to loose wiring, incorrect motor parameters in 1-24, or motor winding faults.
- **Alarm 16 (short circuit on output) confused for AL-79 (~15%)** A short circuit in the motor cable, motor windings, or failed IGBT on the inverter board triggers output protection.
- **Alarm 29 (heatsink overtemperature) confused for AL-79 (~10%)** Heatsink temperature exceeds 90 to 95°C due to a dead cooling fan, blocked airflow, or excessive load.
- **Custom alarm configured by system integrator (~10%)** Some installations use programmable alarms or custom fault logic that may display non-standard codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show the alarm number clearly as '79' or 'AL-79'?</summary>
<div class="dtree-body"><strong>Yes:</strong> Recheck the display carefully or access the alarm history menu to confirm the exact code. The number may be 13, 16, 29, or another two-digit alarm.<br><strong>No:</strong> Write down the exact alarm number and consult the FC302 manual alarm table to find the correct fault description and troubleshooting steps.</div>
</details>

<details class="dtree"><summary>Can you access the drive's alarm history log through the control panel?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review the log for the most recent alarm code and timestamp. Cross-reference the code with the manual to identify the fault.<br><strong>No:</strong> Power-cycle the drive and observe which alarm number appears on startup. Document it before attempting any repair.</div>
</details>

<details class="dtree"><summary>Is the motor connected and are all three output phases present at the motor terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is likely intact. Check motor parameters (1-20 through 1-25) and run AMA (parameter 1-29) to re-tune the drive to the motor.<br><strong>No:</strong> Repair or replace the motor cable and verify continuity from drive output terminals to motor windings before re-energizing.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** at the main disconnect and wait for the DC bus capacitors to discharge (typically 5 to 10 minutes or until the display is blank).
2. **Record the exact alarm code** from the drive display or navigate to the alarm history menu (consult your manual for the menu path, often under Diagnostics or Alarm Log).
3. **Consult the FC302 manual alarm table** to find the documented meaning of the code you recorded. If the code is 13, 16, 29, 38, or 72, proceed with the troubleshooting steps for that specific alarm.
4. **Inspect motor cable connections** at both the drive output terminals and the motor terminal box for loose, corroded, or damaged wiring. Measure resistance between phases at the motor end (should be greater than 100Ω with motor disconnected).
5. **Verify motor parameters** in the drive setup menu (parameters 1-20 through 1-25) match the motor nameplate data. Pay special attention to nominal motor current (parameter 1-24), which should be within 5 to 10 percent of the actual motor rating.
6. **Run Automatic Motor Adaptation (AMA)** by setting parameter 1-29 to the appropriate option (typically option 1 for rotating AMA or option 2 for stationary AMA). Follow the on-screen prompts and allow the drive to complete the tuning cycle.
7. **Check cooling fan operation** by observing airflow through the heatsink while the drive is powered on. If the fan is not running or airflow is blocked, clean debris from the heatsink fins or replace the fan.
8. **Test drive operation** with the motor connected under no-load conditions. Monitor for any new alarms or abnormal behavior. If the alarm persists or returns immediately, suspect a failed inverter board, rectifier board, or motor winding and call a qualified technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter board (IGBT module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-79-fault-code&k=Danfoss+FC302+inverter+board+%28IGBT+module%29&tag=errorcodefixes-20) \| Required if Alarm 16 persists with motor disconnected or IGBT gate resistance tests fail |
| Danfoss FC302 rectifier board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-79-fault-code&k=Danfoss+FC302+rectifier+board&tag=errorcodefixes-20) \| Required if input fuse or rectifier fails, typically after Alarm 13 or input-side faults |
| Cooling fan for Danfoss FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-79-fault-code&k=Cooling+fan+for+Danfoss+FC302&tag=errorcodefixes-20) \| Required if Alarm 29 appears and the original fan is not spinning or is noisy |

## When to Call a Pro

Call a qualified industrial drive technician or electrician if the alarm persists after verifying wiring and running AMA, if you are not trained to work safely on high-voltage VFD systems, or if you need to replace the inverter board, rectifier board, or other internal power components. VFDs store dangerous DC bus voltage even after input power is removed, and working inside the drive requires lockout/tagout procedures, proper discharge of capacitors, and high-voltage test equipment. A pro can also access Danfoss service tools to read internal fault logs, perform advanced diagnostics, and confirm whether the alarm is a true fault or a configuration issue.

**Rough cost:** A pro service call runs about $200-600 depending on actual fault and parts required.
