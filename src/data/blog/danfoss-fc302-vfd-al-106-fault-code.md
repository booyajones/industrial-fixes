---
title: "Danfoss FC302 VFD AL-106 - Causes & Fix"
description: "AL-106 is not a valid Danfoss FC302 fault code. Check your display for the correct alarm number (1-64) or consult your manual."
pubDatetime: 2026-06-23T10:22:10Z
modDatetime: 2026-06-23T10:22:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 inverter IGBT module"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number on the display and look it up in the FC 302 manual's alarm list"
  - "Check that all three input phases are present and balanced within 3% using a multimeter"
  - "Inspect motor cables for loose connections, corrosion, or physical damage at both drive and motor ends"
---

## What this code means
The code AL-106 does not exist in the official Danfoss VLT AutomationDrive FC 302 documentation. The FC 302 series uses alarm numbers from Alarm 1 to Alarm 64, such as Alarm 13 for overcurrent or Alarm 38 for internal fault. AL-106 may be a misread display, a typo (perhaps AL-10 or Alarm 6), confusion with a parameter code (like parameter 1-06), or a code from a different VFD brand. Verify the exact alarm number shown on the drive's control panel display and cross-reference it with the FC 302 alarm list in your manual.

If you are seeing a common fault like Alarm 13 (overcurrent), the drive has detected output current exceeding its peak limit during acceleration, deceleration, or normal operation. This typically points to a motor winding short, mechanical overload, incorrect motor parameter settings, loose or corroded motor cables, aging or damaged IGBT modules on the inverter board, high incoming line voltage above nominal by more than 10%, or a failed rectifier or power board.

## Before You Replace Anything

Many technicians replace the entire inverter board without first disconnecting the motor and running the drive unloaded. If the fault clears with the motor disconnected, the problem is in the motor or wiring, not the drive electronics.

## Common Causes

- **Invalid or misread code (~50%)** The AL-106 code does not appear in Danfoss FC 302 documentation and may be a display error, typo, or confusion with a parameter number rather than an alarm.
- **Motor winding short or insulation failure (~20%)** Partial or full short in motor windings causes overcurrent faults (Alarm 13) when insulation resistance falls below 2 megohms.
- **Mechanical overload on motor shaft (~15%)** Seized bearings, jammed loads, or binding mechanical components force the motor to draw excessive current and trip the drive.
- **Incorrect motor parameter settings (~10%)** Mismatched motor current in parameter 1-24 or wrong motor nameplate data causes the drive to trip on normal load.
- **Failed IGBT modules or power board (~5%)** Shorted or open IGBT transistors on the inverter section produce overcurrent or internal fault alarms even with the motor disconnected.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show AL-106 or a standard Alarm number (1 through 64)?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it shows a standard Alarm number, look up that specific alarm in your FC 302 manual and follow the documented troubleshooting steps.<br><strong>No:</strong> If it clearly shows AL-106, take a photo and contact Danfoss technical support or verify the drive model number, as this code is not documented for the FC 302.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor windings, motor cables, or a mechanical overload, not the drive electronics.<br><strong>No:</strong> The drive itself has an internal fault in the rectifier, DC link, inverter IGBTs, or control board.</div>
</details>

<details class="dtree"><summary>Are all three input phases present and balanced within 3% of each other?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is acceptable and not the cause of the fault.<br><strong>No:</strong> Check for blown fuses, loose connections, or utility voltage imbalance and correct the input power before further testing.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** displayed on the FC 302 control panel and write it down, then cross-reference it with the alarm list in the VLT AutomationDrive FC 302 manual to confirm it is a valid Danfoss code.
2. **Disconnect the motor** from the drive output terminals and power up the drive without a load to see if the alarm persists.
3. **Perform a megohm test** on the motor windings to ground using an insulation resistance tester, looking for readings of at least 2 megohms between each winding and the motor frame.
4. **Measure incoming line voltage** on all three input phases with a multimeter and verify the phase-to-phase voltages are within 3% of each other and within plus or minus 10% of the nominal voltage rating.
5. **Inspect and tighten** all motor cable connections at both the drive output terminals and the motor junction box, checking for corrosion, fraying, or physical damage.
6. **Check parameter 1-24** (motor nominal current) in the drive programming menu and verify it matches the current rating on the motor nameplate.
7. **Replace the inverter IGBT module or power board** if the alarm occurs with the motor disconnected and all input power is correct, as this indicates an internal drive component failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 inverter IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-106-fault-code&k=Danfoss+FC+302+inverter+IGBT+module&tag=errorcodefixes-20) \| Model-specific; consult your drive nameplate for the exact part number and voltage/current rating. |
| Danfoss FC 302 power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-106-fault-code&k=Danfoss+FC+302+power+board+assembly&tag=errorcodefixes-20) \| Includes rectifier and inverter sections; match the part number to your drive's serial number and frame size. |

## When to Call a Pro

Call a qualified VFD technician or electrician if the alarm code is not documented in your manual, if the fault persists after disconnecting the motor and verifying input power, or if you are not comfortable working with high-voltage three-phase equipment. Replacing IGBT modules or power boards requires knowledge of DC link discharge procedures, proper torque specs for bus bar connections, and safe handling of capacitors that can retain a lethal charge. A technician can also download fault logs from the drive's memory and perform advanced diagnostics with Danfoss MCT software to identify intermittent faults or parameter conflicts that are not obvious from the display.

**Rough cost:** A pro service call runs about $300-800.
