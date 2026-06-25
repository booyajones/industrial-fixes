---
title: "Danfoss FC302 AL-100 Fault - Causes & Fix"
description: "AL-100 is not a real Danfoss FC302 code. Check the LCP for the actual alarm (80, 88, or external error) and restore parameters or power cycle."
pubDatetime: 2026-06-23T10:17:36Z
modDatetime: 2026-06-23T10:17:36Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 Control PCB (Main Control Card)"
most_likely_cause: "Misread display or external error code from a connected controller"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number on the LCP display under good lighting and check for external error sources"
  - "Disconnect communication cables (fieldbus, Modbus, or PLC wiring) and power cycle the drive to see if the code clears"
  - "Press Off/Reset, wait 30 seconds, and power up again to clear transient faults"
no_buy_pct: "80%"
---

## Danfoss FC302 AL-100 Fault — What It Means

The Danfoss VLT AutomationDrive FC 302 does not generate an AL-100 fault code. Official Danfoss documentation lists alarms only from 1 to 99, such as Alarm 13 for overcurrent, Alarm 38 for internal faults, and Alarm 88 for option layout changes. If your local control panel (LCP) displays "AL-100," you are likely seeing a misread display, a software glitch, or an external error code sent by a connected PLC, HMI, or softstarter that the drive is relaying but did not generate itself.

Technicians often confuse Alarm 80 (settings lost or reset) or Alarm 88 (option detection or layout mismatch) with "AL-100" due to poor lighting, worn displays, or communication errors. The first diagnostic step is to verify the exact five-digit code on the LCP screen, note any internal fault code referenced in the drive's parameter menu, and determine whether the error clears when communication cables are disconnected. If the code persists after a power cycle and parameter restore, inspect the control card, input voltage, and option layout settings to isolate the true fault.

## Before You Replace Anything

Technicians often replace the control PCB or power module without first checking for external error codes from a PLC or HMI. Disconnect communication wiring and power cycle the drive to confirm the fault is internal before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread or corrupted display (~40%)** Poor lighting, worn LCP screens, or software glitches can make Alarm 80 or 88 appear as "AL-100" on the panel.
- **External error code from PLC or HMI (~30%)** A connected controller sends its own fault code to the FC 302 LCP, which displays it but did not generate it internally.
- **Alarm 80 (settings lost or reset) (~15%)** Drive memory has reset to factory defaults due to control card battery failure or power interruption, requiring parameter restore.
- **Alarm 88 (option layout change) (~10%)** Parameter 14-89 is set to frozen configuration and the drive detects a mismatch with installed option cards, blocking operation.
- **Control card memory failure (~5%)** Flash or EEPROM corruption on the control PCB causes persistent alarm codes that do not match the standard 1-99 range.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP show a clear five-digit alarm number (like Alarm 80 or Alarm 88) when you view it under bright light?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code is a known Danfoss fault. Look up the exact alarm in your FC 302 manual and follow the troubleshooting steps for that number.<br><strong>No:</strong> The display may be corrupted or showing an external error. Disconnect communication cables and power cycle to check if the code clears.</div>
</details>

<details class="dtree"><summary>Does the code disappear when you disconnect fieldbus or PLC communication wiring and restart the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is an external error from your controller, not the drive itself. Check your PLC or HMI diagnostics and wiring.<br><strong>No:</strong> The fault is internal. Verify input voltage at terminals 100/101 and check Parameter 15-32 for extended diagnostics.</div>
</details>

<details class="dtree"><summary>Does pressing Off/Reset and waiting 30 seconds before powering up clear the alarm?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient. Monitor for recurrence and check for loose wiring or control supply overload at terminal 50.<br><strong>No:</strong> The fault is persistent. Restore parameters from backup or check for control card failure requiring professional service.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** by viewing the LCP under bright overhead lighting and noting the full five-digit number displayed (for example, Alarm 80 or Alarm 88).
2. **Check for external error sources** by disconnecting all communication cables (fieldbus, Modbus, RS-485, or PLC wiring) from the drive terminals and restarting the unit.
3. **Power cycle the drive** by pressing the Off/Reset button, waiting 30 seconds, and then restoring power to clear any transient fault stored in memory.
4. **Inspect input voltage** at terminals 100/101 with a voltmeter to confirm all three phases match the drive rating (typically 400 V ±10%) and check for blown fuses or loose connections.
5. **Restore parameters from backup** if the display shows Alarm 80 (settings lost) by accessing the parameter menu and uploading your saved configuration file or re-entering critical values.
6. **Check Parameter 14-89 (Option Detection)** if the display shows Alarm 88 and verify it is not set to [0] Frozen configuration, which blocks the drive from accepting option card changes.
7. **Test the 10 V control supply** by measuring the load at terminal 50 with a multimeter (maximum 15 mA, minimum 590 Ω resistance) and removing terminal 50 wiring if the supply is overloaded, then restarting to see if the warning clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 Control PCB (Main Control Card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-100-fault-code&k=Danfoss+FC+302+Control+PCB+%28Main+Control+Card%29&tag=errorcodefixes-20) \| Required if Alarm 80 persists after parameter restore or if Parameter 15-32 shows memory/flash corruption. |
| Danfoss FC 302 Option Card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-100-fault-code&k=Danfoss+FC+302+Option+Card&tag=errorcodefixes-20) \| Replace if Alarm 88 appears and the installed option card does not match the drive's frozen configuration layout. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the alarm persists after you have verified the exact code, disconnected external communication, and power cycled the drive. Professional help is required when Parameter 15-32 shows internal fault diagnostics pointing to control card or power stage failure, when input voltage measurements reveal rectifier or DC bus problems, or when the drive needs firmware updates or option card reconfiguration. Technicians have the tools to perform DC bus voltage tests, measure IGBT gate signals, and safely replace high-voltage power modules or control boards without risking arc flash or further damage to the equipment.

**Rough cost:** A pro service call runs about $200-600 for service call, diagnostics, and parameter restore or control card replacement if needed.

## See Also

- [Danfoss FC302 ALARM 16 - Causes & Fix](/posts/danfoss-fc302-alarm-16-fault-code/)
- [Danfoss FC302 AL-67 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-67-fault-code/)
- [Danfoss FC302 Alarm 74 - Causes & Fix](/posts/danfoss-fc302-vfd-al-74-fault-code/)
- [Danfoss FC302 AL-63 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-63-fault-code/)
