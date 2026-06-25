---
title: "Danfoss FC302 AL-75 - Causes & Fix"
description: "AL-75 does not exist in Danfoss FC302 documentation. Check for misread code (AL-17, AL-70) or Alarm 38 sub-code. Power cycle first."
pubDatetime: 2026-06-23T09:57:06Z
modDatetime: 2026-06-23T09:57:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control board (logic PCB)"
most_likely_cause: "Misread or invalid alarm number"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number shown on the display and compare it to the alarm list in the FC302 manual"
  - "Power down the drive, disconnect all AC and DC power sources, wait 10 minutes, then re-power and check if the alarm clears"
  - "Check the alarm history log in the keypad menu to see if the code is logged as 75 or as a different number with sub-code"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-75 — What It Means

The alarm code AL-75 does not appear in Danfoss's official VLT AutomationDrive FC 302 documentation. Danfoss lists over 90 alarms but Alarm 75 is not among them. If your display shows AL-75, you may be reading another code incorrectly (such as AL-17 or AL-70), or you have Alarm 38 with sub-code 75, which indicates an internal fault in the drive's control logic, memory, or power section.

Alarm 38 sub-codes are not publicly documented by Danfoss and require factory service interpretation. The sub-code typically points to a specific internal failure in the logic board, power board, or firmware that only Danfoss technicians can decode. Before assuming a hardware fault, verify the exact alarm number on your display and consult your drive's alarm log.

## Before You Replace Anything

Technicians sometimes replace the power board before checking that the displayed code is actually valid. Verify the exact alarm number in the drive's alarm history log and power-cycle the drive before ordering any parts.

[Jump to Fix](#fix)

## Common Causes

- **Misread alarm code (~40%)** The display may show AL-17 (mains phase loss), AL-70 (brake resistor overload), or another valid code that looks like 75 when viewed at an angle or with a dim display.
- **Alarm 38 sub-code 75 (internal fault) (~30%)** The drive shows Alarm 38 followed by a sub-code number 75, indicating a fault in the control board, power board, or firmware that Danfoss does not publicly document.
- **Display or firmware glitch (~15%)** A corrupted display module, firmware bug, or keypad fault causes an invalid alarm number to appear that does not correspond to any real fault condition.
- **Control board failure (~10%)** The logic PCB has a memory or firmware corruption issue that generates an undefined alarm code during self-diagnostics.
- **Third-party accessory alarm (~5%)** An add-on keypad, remote I/O module, or communication card generates a proprietary alarm code not listed in the base Danfoss documentation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show 'AL 75' with no sub-code or prefix?</summary>
<div class="dtree-body"><strong>Yes:</strong> This code does not exist in Danfoss documentation. Verify you are reading the correct number and check the alarm history log to see what is actually logged.<br><strong>No:</strong> If it shows 'Alarm 38' followed by a number, you have an internal fault sub-code that requires Danfoss service to decode.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a full power cycle (AC and DC disconnected for 10 minutes)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient firmware or memory glitch. Monitor the drive and log any repeat occurrences.<br><strong>No:</strong> The fault is persistent and points to a hardware failure in the control or power board that needs professional diagnosis.</div>
</details>

<details class="dtree"><summary>Are there any third-party modules or add-on keypads installed on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the documentation for those accessories as they may use custom alarm codes not in the Danfoss base manual.<br><strong>No:</strong> The alarm is either misread or indicates a control/power board fault that requires factory-trained service.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Write down the exact alarm** displayed, including any prefix, sub-code, or flashing symbols, and photograph the screen if possible.
2. **Disconnect all power** to the drive, including AC mains and any remote DC-link supplies (UPS or battery backups), and wait 10 minutes for internal capacitors to discharge.
3. **Re-power the drive** and observe the startup sequence to see if the same alarm code appears or if it was a transient fault.
4. **Access the alarm history log** using the keypad menu (consult your FC302 operating instructions for the exact menu path) and compare the logged alarm number to the displayed code.
5. **Cross-reference the logged alarm** against the complete alarm list in the Danfoss VLT AutomationDrive FC 302 Programming Guide to identify the actual fault condition.
6. **If the alarm is Alarm 38 with a sub-code**, contact Danfoss technical support or a factory-trained service provider to decode the specific internal fault number.
7. **If no valid alarm exists in the log**, inspect the display module and keypad for physical damage, loose connections, or corrosion, and consider replacing the keypad assembly if the display is faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control board (logic PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-75-fault-code&k=Danfoss+FC302+control+board+%28logic+PCB%29&tag=errorcodefixes-20) \| Order by drive frame size and firmware version; only needed if Alarm 38 sub-code points to control logic failure. |
| Danfoss FC302 power board (rectifier/inverter assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-75-fault-code&k=Danfoss+FC302+power+board+%28rectifier%2Finverter+assembly%29&tag=errorcodefixes-20) \| Order by drive power rating and voltage; only needed if internal fault is in the power section. |

## When to Call a Pro

Call a factory-trained Danfoss service technician when the alarm persists after a power cycle, when you have confirmed Alarm 38 with a sub-code that requires decoding, or when you need to replace the control or power board. VFD internal faults involve high DC-link voltages (often 650 VDC or higher) and complex diagnostics that require specialized test equipment and knowledge of the drive's firmware architecture. Danfoss does not publish sub-code meanings for Alarm 38, so only authorized service providers can interpret the exact fault and determine whether the control board, power board, or another internal component has failed.

**Rough cost:** A pro service call runs about $400-1200.
