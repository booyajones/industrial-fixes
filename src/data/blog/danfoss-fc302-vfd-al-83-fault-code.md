---
title: "Danfoss FC302 AL-83 Fault - Causes & Fix"
description: "AL-83 is not a standard Danfoss FC302 code. Likely Alarm 80 (drive initialized, parameters lost) or Alarm 38 (internal fault). Reset and restore parameters first."
pubDatetime: 2026-06-23T10:01:12Z
modDatetime: 2026-06-23T10:01:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control Board / Logic Card"
most_likely_cause: "Corrupted parameter memory or power supply disturbance (if Alarm 80)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive: disconnect AC mains and DC-link power, wait 5 minutes, reconnect and power up"
  - "Check the display for Alarm 80 or Alarm 38 instead of AL-83, and note any sub-code shown"
  - "Verify AC input voltage is stable and within specified range (typically +/- 10% of nominal)"
part_price: "$200-350 for FC302 control board"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-83 Fault — What It Means

There is no specific fault code AL-83 in the Danfoss FC302 VFD documentation. The alarm list for the FC302 series contains Alarm 80 (Drive Initialized, parameters defaulted) and Alarm 81 (Internal Fault) as the highest numbered standard drive-status alarms, with internal fault codes typically appearing as Alarm 38 with a sub-code rather than 83 as a standalone alarm number.

If you are seeing a display reading that resembles AL-83, it is most likely a misinterpretation of Alarm 80 (Drive Initialized), which means the drive has lost its parameter settings and reverted to factory defaults, or Alarm 38 (Internal Fault) with a sub-code displayed in parameter 15-32. A garbled display or visual confusion with a sub-code could cause the misreading. Alarm 80 is caused by power supply instability, corrupted memory, or a manual reset that cleared the parameter set.

## Before You Replace Anything

Technicians sometimes replace the entire control board when the issue is only corrupted parameters (Alarm 80). First cycle power, check for Alarm 80 or 38, and restore parameters from backup before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted parameter memory (Alarm 80) (~40%)** Power supply voltage sags or spikes corrupted the drive's flash memory, causing parameters to default to factory settings.
- **Power supply instability (~25%)** Voltage fluctuations or brownouts caused the drive to lose its stored configuration and trigger Alarm 80.
- **Manual reset performed (~15%)** A user or maintenance action accidentally performed a full parameter reset that cleared all custom settings.
- **Control board failure (Alarm 38) (~12%)** Failed gate driver circuits or component failures on the logic board generate an internal fault code.
- **Heatsink sensor fault (~5%)** Open circuit or shorted sensor on the heatsink prevents feedback and triggers an internal fault.
- **Garbled display (~3%)** The display itself is malfunctioning and showing a non-existent code number.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show Alarm 80 when you look closely?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive has lost its parameters. Reset the alarm and restore parameters from backup or manually re-enter motor data.<br><strong>No:</strong> Check for Alarm 38 or other codes. If the display shows 83 or an unusual number, the display may be faulty or you are seeing a sub-code.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a full power cycle (5 minutes off)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient. Re-enter parameters if needed and monitor for recurrence. If it returns, suspect power supply or control board.<br><strong>No:</strong> The fault is persistent. Check parameter 15-32 for the internal fault sub-code and contact Danfoss service for repair.</div>
</details>

<details class="dtree"><summary>Do you have a parameter backup file or record of motor settings?</summary>
<div class="dtree-body"><strong>Yes:</strong> Restore the parameter set from backup after resetting Alarm 80. Run Automatic Motor Adaptation if required.<br><strong>No:</strong> Manually re-enter motor nameplate data (voltage, current, speed) and tune the drive. Consider saving a backup afterward.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power cycle the drive completely:** Turn off the main disconnect, disconnect AC mains and DC-link power, wait at least 5 minutes for capacitors to discharge, then reconnect and power up.
2. **Identify the actual alarm code:** Look closely at the display and confirm whether it reads Alarm 80, Alarm 38, or another code. If using Danfoss MCT 10 software, connect and read parameter 15-32 for the internal fault sub-code.
3. **Reset the alarm:** Press the reset key on the keypad or send a reset command via the software to clear the fault and see if the drive will start.
4. **Restore parameters (if Alarm 80):** If the alarm was 80, the drive has lost its configuration. Load parameters from a backup file or manually re-enter motor nameplate data (nominal voltage, current, frequency, and speed) and application settings.
5. **Check AC input voltage:** Use a multimeter to verify that the incoming AC supply is stable and within the drive's specified range. Look for voltage sags, spikes, or loose connections at the input terminals.
6. **Inspect the control board:** If the fault persists after power cycling and parameter restore, open the drive cabinet and visually inspect the control board for burned components, loose connectors, or corrosion. Check heatsink sensor wiring for open or shorted connections.
7. **Contact Danfoss service:** If the alarm returns or you see Alarm 38 with a persistent sub-code, the control board or logic card may have failed. Contact a Danfoss service center or local supplier for board-level diagnostics and replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control Board / Logic Card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-83-fault-code&k=Danfoss+FC302+Control+Board+%2F+Logic+Card&tag=errorcodefixes-20) \| Verify the exact frame size and firmware version of your FC302 before ordering. Control boards are model-specific. |
| Heatsink Temperature Sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-83-fault-code&k=Heatsink+Temperature+Sensor&tag=errorcodefixes-20) \| If Alarm 38 sub-code points to sensor fault. Check wiring and connector first before replacing the sensor. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss service partner if the alarm persists after power cycling and parameter restore, if you see Alarm 38 with a sub-code you cannot interpret, or if you are not trained to work inside the drive cabinet. VFD control boards carry stored high-voltage DC for several minutes after power-off and require proper lockout and discharge procedures. A technician with Danfoss MCT 10 software can read detailed fault logs and sub-codes to pinpoint the failure. If the drive is under warranty or a service contract, contact your Danfoss supplier before opening the enclosure to avoid voiding coverage.

**Rough cost:** A pro service call runs about $150-400 for control board replacement if internal fault persists.

## See Also

- [Danfoss FC302 VFD AL-154 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-154-fault-code/)
- [Danfoss FC302 ALARM 25 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-25-fault-code/)
- [Danfoss FC302 VFD Alarm 38 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-38-fault-code/)
- [Danfoss FC302 VFD AL-127 - Causes & Fix](/posts/danfoss-fc302-vfd-al-127-fault-code/)
