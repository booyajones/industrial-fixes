---
title: "Danfoss FC302 AL-121 - Causes & Fix"
description: "AL-121 is not a valid Danfoss FC302 code. Check the display again for Alarm 13, 14, 38, or AL 17, which are the actual fault codes."
pubDatetime: 2026-06-24T10:17:38Z
modDatetime: 2026-06-24T10:17:38Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control card (logic board)"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive completely (disconnect input power for 60 seconds, then reconnect)"
  - "Verify the exact code on the LCP display and write down the full alarm number or AL code"
  - "Check Parameter 15-32 for extended internal fault codes if the display shows Alarm 38"
---

## Danfoss FC302 AL-121 — What It Means

The code AL-121 does not exist in official Danfoss FC302 VFD documentation. Danfoss VLT AutomationDrive FC 301/302 drives use numeric alarms (such as Alarm 13, 14, or 38) or two-digit AL codes like AL 17. If your display shows something that looks like 121, verify whether it is Alarm 13 (overcurrent), Alarm 14 (overvoltage), Alarm 38 (internal fault), a parameter error code, or a custom alarm set in parameter groups. Always confirm the exact code on the LCP display before proceeding.

The most common faults on FC302 drives are Alarm 13 (output overcurrent caused by motor overload or winding issues), Alarm 38 (internal hardware or software error), and AL 17 (serial communication timeout with the keypad). Each has specific diagnostic steps. If the display truly shows 121 without the AL prefix, check Parameter 15-32 for extended fault codes or consult your drive's parameter list for custom alarms.

## Before You Replace Anything

Technicians often replace the inverter module or IGBTs when seeing Alarm 13, but a simple megohm test of the motor windings (which must be at least 2 megohms) will reveal if the fault is in the motor instead of the drive.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transposed code (~40%)** The display may show Alarm 13, 31, or 121 in a parameter field rather than an AL-121 fault, and the code was recorded incorrectly.
- **Overcurrent (Alarm 13) (~25%)** Output current exceeds 150 to 160 percent of rated current for several seconds due to mechanical motor overload, incorrect motor current parameter (Par 1-24), partial motor winding short, loose motor cable, or aging IGBTs.
- **Internal fault (Alarm 38) (~15%)** Internal hardware or software error in the gate driver, control board, or memory caused by failed gate driver, corrupted firmware, or control board component failure.
- **Serial communication timeout (AL 17) (~10%)** Serial communication lost with the keypad (LCP) or accessory due to faulty LCP cable, dead keypad, or broken communication board.
- **Overvoltage during deceleration (Alarm 14) (~10%)** DC bus voltage too high during deceleration because ramp time is too short, no brake resistor is installed, or the load has high inertia.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP display show AL-121 exactly, or does it show Alarm 13, 31, 38, or another number?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it shows Alarm 13, 38, or another standard code, follow the diagnostic steps for that specific alarm.<br><strong>No:</strong> If it truly shows AL-121, check Parameter 15-32 for extended codes or consult the parameter list for custom alarms programmed into your drive.</div>
</details>

<details class="dtree"><summary>Does the fault clear after a full power cycle (disconnect input power for 60 seconds)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may be a transient internal error or corrupted memory; monitor the drive and log any recurrence.<br><strong>No:</strong> A persistent fault after power cycling indicates a hardware failure in the control card, gate driver, inverter module, or motor; proceed to load testing and component checks.</div>
</details>

<details class="dtree"><summary>Can you run the drive with the motor disconnected (unloaded)?</summary>
<div class="dtree-body"><strong>Yes:</strong> If the drive runs without fault when unloaded, the problem is in the motor, motor cable, or mechanical load, not the drive itself.<br><strong>No:</strong> If the drive faults even with no motor connected, the inverter module, control board, or internal power supply has failed.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm code** on the LCP display and write it down completely, including any AL prefix or numeric-only format.
2. **Power-cycle the drive** by disconnecting all input power for 60 seconds, then reconnecting and observing whether the fault returns.
3. **Check Parameter 15-32** (Internal Fault Code) if the display shows Alarm 38, or review the parameter list if the code appears only in a parameter field.
4. **Disconnect the motor** from the drive output terminals and attempt to run the drive unloaded; if the fault persists with no motor, the drive has an internal failure.
5. **Perform a megohm test** on the motor windings if Alarm 13 appears; insulation resistance must be at least 2 megohms between each winding and ground.
6. **Verify motor parameters** in Par 1-24 (motor current) and Par 1-20 through 1-25 (motor data) match the motor nameplate; incorrect settings cause false overcurrent faults.
7. **Swap the LCP keypad** with a known-good unit if AL 17 or communication errors appear; if communication resumes, replace the LCP display; if not, replace the communication or control board.
8. **Replace the control card** (logic board) if Alarm 38 persists after power cycling and parameter checks, or replace the inverter module or IGBTs if Alarm 13 continues with a verified good motor.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control card (logic board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-121-fault-code&k=Danfoss+FC302+control+card+%28logic+board%29&tag=errorcodefixes-20) \| Match the part number to your exact drive frame size and firmware revision. |
| Danfoss FC302 inverter module or power board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-121-fault-code&k=Danfoss+FC302+inverter+module+or+power+board&tag=errorcodefixes-20) \| Required for persistent Alarm 13 or DC bus faults; verify frame size and voltage rating. |
| Danfoss LCP display unit (keypad) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-121-fault-code&k=Danfoss+LCP+display+unit+%28keypad%29&tag=errorcodefixes-20) \| Standard replacement for AL 17 communication faults; confirm connector type. |
| Brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-121-fault-code&k=Brake+resistor&tag=errorcodefixes-20) \| Add if Alarm 14 (overvoltage) occurs during deceleration and none is installed; size per Par 2-10. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician for any Danfoss FC302 fault. These drives operate at high voltage (up to 690V AC) and high DC bus voltage, and internal repairs require specialized test equipment, firmware tools, and familiarity with gate-driver circuits and parameter programming. If the exact code cannot be identified from the LCP display or parameter list, a technician with Danfoss MCT software can read extended diagnostic logs and verify whether the code is a custom alarm or a misread standard fault. Professional service also ensures proper motor parameter setup, which prevents repeat overcurrent and overvoltage faults.

**Rough cost:** A pro service call runs about $200-800.
