---
title: "Danfoss FC302 VFD AL-87 - Causes & Fix"
description: "AL-87 is not a standard Danfoss FC302 code. It may be a misread Alarm 8 (overvoltage) or a custom user alarm. Check the display closely."
pubDatetime: 2026-06-24T10:03:07Z
modDatetime: 2026-06-24T10:03:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control panel / keypad"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm code on the display (look for Alarm 8, Alarm 13, Alarm 17, or Alarm 38 with a sub-code)"
  - "Check parameter 14-20 through 14-29 for any custom alarm limits that may have been set"
  - "Measure incoming line voltage at the drive input terminals to rule out supply issues"
---

## Danfoss FC302 VFD AL-87 — What It Means

The Danfoss FC302 VFD does not list AL-87 as a standard alarm code in its documentation. Standard alarms for this drive series typically range from Alarm 13 to Alarm 80. If your display shows AL-87 it is likely one of three things: a misread code (such as Alarm 8 for overvoltage or Alarm 17 for serial timeout), a custom user-defined parameter alarm configured in parameters 14-20 through 14-29 for external sensors like pressure or temperature limits, or a communication error with an attached accessory. Double-check the display and your parameter setup before troubleshooting.

If the code is actually Alarm 8 (overvoltage), it means the DC bus voltage has exceeded the safe limit, often because the motor is generating power back into the drive during deceleration on a high-inertia load. If it is Alarm 13, the drive cannot detect the motor on its output terminals due to wiring issues or motor insulation failure. If it is a custom alarm, the meaning depends entirely on the parameter configuration set by the installer.

## Before You Replace Anything

Technicians often replace the power board or IGBT module when the fault is actually a misread code or a simple parameter misconfiguration. Always verify the exact alarm number on the display and consult the parameter list in the manual before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread alarm code (~40%)** The display may show Alarm 8 (overvoltage) or Alarm 17 (serial timeout) but appear as AL-87 due to a dim segment or viewing angle.
- **Custom user-defined alarm (~30%)** Parameters 14-20 through 14-29 can be configured to trigger custom alarms for external sensors or process limits, which may display as non-standard codes.
- **Communication accessory error (~15%)** An external module or fieldbus adapter may be reporting an error that does not appear in the standard alarm list.
- **Display module fault (~10%)** The control panel or keypad may have a failing display that is showing corrupted characters or segments.
- **Firmware version mismatch (~5%)** Older or custom firmware may use alarm codes that differ from the published documentation for standard FC302 drives.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show AL-87 with no flickering or missing segments?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is likely a custom user alarm or communication error. Check parameters 14-20 through 14-29 and any connected modules.<br><strong>No:</strong> The display may be failing or the code is misread. Clean the panel and view it straight-on, then compare to the alarm list in the manual.</div>
</details>

<details class="dtree"><summary>Can you find the alarm code in the drive's alarm history (parameter 15-00 or similar)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The history will show the exact numeric code and timestamp. Cross-reference it with the manual's alarm table to identify the real fault.<br><strong>No:</strong> The alarm may be transient or the history is not enabled. Write down the exact characters you see and contact Danfoss support with your drive's serial number.</div>
</details>

<details class="dtree"><summary>Are any external sensors, pressure switches, or fieldbus modules connected to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect them one at a time and cycle power. If the alarm clears, the external device is triggering a custom alarm.<br><strong>No:</strong> The issue is likely a misread standard alarm. Recheck the display and compare each character to the alarm code table in the manual.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and wait two minutes for the DC bus capacitors to discharge before touching any terminals.
2. **Photograph the display** clearly while the alarm is active so you have an exact record of the characters shown.
3. **Access the alarm history** by navigating to parameter 15-00 (or consult your model's parameter map) to see the numeric code and timestamp of recent faults.
4. **Cross-reference the code** with the alarm table in the FC302 manual (typically section 6 or 9) to identify the real alarm number and meaning.
5. **Check custom alarm parameters** 14-20 through 14-29 if the code does not appear in the standard list, as these can be configured for external process limits.
6. **Inspect connected accessories** including any fieldbus adapters, I/O modules, or external sensors, and disconnect them to isolate communication errors.
7. **Contact Danfoss technical support** with your drive's serial number, firmware version, and the exact alarm code if it remains unidentified, as custom firmware or regional variants may use non-standard codes.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control panel / keypad | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-87-fault-code&k=Danfoss+FC302+control+panel+%2F+keypad&tag=errorcodefixes-20) \| Replace only if the display is physically damaged or shows corrupted characters on multiple codes |
| Danfoss FC302 power board / IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-87-fault-code&k=Danfoss+FC302+power+board+%2F+IGBT+module&tag=errorcodefixes-20) \| Order only after confirming a legitimate Alarm 8 (overvoltage) or Alarm 13 (motor not detected) that persists after parameter and wiring checks |

## When to Call a Pro

Call a qualified VFD technician or Danfoss service partner if you cannot identify the alarm code after checking the display and alarm history, if the drive continues to fault after verifying parameters and connections, or if internal hardware repair is needed. VFD troubleshooting requires knowledge of high-voltage DC bus circuits, parameter programming, and motor drive theory. Incorrect changes to parameters or wiring can damage the drive or motor. A technician can use Danfoss MCT software to read detailed fault logs, update firmware, and test the drive under controlled conditions.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Danfoss FC302 Alarm 40 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-40-fault-code/)
- [Danfoss FC302 AL-16 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-162-fault-code/)
- [Danfoss FC302 AL-17 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-117-fault-code/)
- [Danfoss FC302 AL-131 (Overcurrent) - Causes & Fix](/posts/danfoss-fc302-vfd-al-131-fault-code/)
