---
title: "Danfoss FC302 AL-103 Fault - Causes & Fix"
description: "AL-103 does not exist in FC302 alarm lists. Likely a typo for AL 13 (overcurrent) or AL 38 (internal fault). Check display and parameter 15-32."
pubDatetime: 2026-06-23T10:20:01Z
modDatetime: 2026-06-23T10:20:01Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 Power Board Assembly"
most_likely_cause: "Misread display or typo for AL 13 (overcurrent)"
likelihood: "the most common explanation"
diy_or_pro: "pro"
free_checks:
  - "Press the Status button and write down the exact alarm number and any sub-code shown in parameter 15-32."
  - "Check that all motor cable connections at U, V, W terminals are tight and that no insulation is damaged."
  - "Inspect the motor shaft by hand (power off) to confirm it turns freely without binding or unusual noise."
---

## Danfoss FC302 AL-103 Fault — What It Means

The alarm code AL-103 is not documented in the official Danfoss VLT AutomationDrive FC 302 fault list. FC 302 alarms range from AL 1 to AL 49. If your display shows '103' or similar, you are likely seeing AL 13 (overcurrent, where output current exceeds 150–160% of rated motor current), AL 38 (internal fault with a sub-code visible in parameter 15-32), a parameter number such as 1-03, or a display error. Some installers confuse this drive with other brands (Siemens, Schneider) that do use three-digit codes.

If the code is actually AL 13, the drive has detected excessive current to the motor, usually from a mechanical jam, shorted motor winding, or failed IGBT module inside the drive. If it is AL 38, an internal control board, gate driver, or heatsink sensor has failed and you must check parameter 15-32 for the specific sub-code. Before ordering parts, confirm the exact alarm by pressing the Status button and reading both the main display and parameter 15-32.

## Before You Replace Anything

Technicians sometimes replace the entire power board when only the motor or cable is faulty. Always disconnect the motor and run the drive unloaded first to isolate whether the fault is in the drive or downstream.

[Jump to Fix](#fix)

## Common Causes

- **Misread alarm or typo (~40%)** The display may show a parameter number (1-03) or the code may be from a different drive model, since AL-103 does not exist in FC 302 documentation.
- **Mechanical overload (if AL 13) (~25%)** The motor shaft is jammed, seized bearings, or the load torque is too high, forcing current above the drive's trip threshold.
- **Motor winding fault (if AL 13) (~15%)** A partial short or phase-to-phase short inside the motor windings draws excessive current and trips the drive.
- **Drive IGBT failure (if AL 13) (~10%)** Aging or damaged insulated-gate bipolar transistor modules inside the power board cannot regulate current properly.
- **Internal control board fault (if AL 38) (~10%)** Memory errors, firmware corruption, failed gate driver circuits, or heatsink sensor failure trigger an internal alarm with a sub-code in parameter 15-32.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show 'AL 13' or 'AL 38' when you press Status?</summary>
<div class="dtree-body"><strong>Yes:</strong> Proceed with the diagnostic steps below for that specific alarm.<br><strong>No:</strong> Write down exactly what the display shows and consult the FC 302 operating instructions or contact Danfoss support to confirm the code.</div>
</details>

<details class="dtree"><summary>With power off, does the motor shaft spin freely by hand?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is not jammed. Check motor windings for shorts and inspect cable insulation.<br><strong>No:</strong> The load or motor bearings are seized. Repair or replace the motor and driven equipment before restarting the drive.</div>
</details>

<details class="dtree"><summary>With the motor disconnected, does the drive run without tripping?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or cable, not the drive. Measure motor winding resistance and inspect cables.<br><strong>No:</strong> The drive has an internal component failure (IGBT, gate driver, or control board) and requires professional repair or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the drive at the main disconnect. Wait at least five minutes for DC bus capacitors to discharge before touching any terminals.
2. **Press the Status button** on the keypad and write down the exact alarm number displayed. Navigate to parameter 15-32 (Extended Alarm Parameter) to see any sub-code if the alarm is AL 38.
3. **Verify the alarm code** against the FC 302 operating instructions. If the code is not AL 13 or AL 38, confirm the drive model and contact Danfoss or your distributor for clarification.
4. **Disconnect the motor** from the drive output terminals U, V, and W. Restore power and attempt to run the drive at low speed with no load.
5. **If the alarm clears** with the motor disconnected, measure motor winding resistance between each pair of phases (U-V, V-W, W-U) using a multimeter. Values should be balanced within 5 percent. Inspect motor cable for cuts, pinches, or missing insulation.
6. **If the alarm persists** with the motor disconnected, the drive has an internal failure in the IGBT modules, DC bus, gate drivers, or control board. Replace the affected board or send the drive for factory repair.
7. **If the alarm was AL 38**, look up the sub-code in parameter 15-32 in the FC 302 alarm list. Common sub-codes point to heatsink sensor faults, gate driver errors, or memory corruption requiring control board replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 Power Board Assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-103-fault-code&k=Danfoss+FC+302+Power+Board+Assembly&tag=errorcodefixes-20) \| Required only if the drive trips with no motor connected and the IGBT or rectifier modules have failed. Match the frame size and voltage rating. |
| Danfoss FC 302 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-103-fault-code&k=Danfoss+FC+302+Control+Board&tag=errorcodefixes-20) \| Required if parameter 15-32 shows a sub-code indicating gate driver failure, memory error, or heatsink sensor fault. |

## When to Call a Pro

Call a qualified VFD technician or motor repair shop if the drive continues to trip with the motor disconnected, if parameter 15-32 shows an internal sub-code you cannot resolve by reseating the control board, or if you lack a multimeter and the training to safely work inside the drive enclosure. High-voltage DC bus capacitors remain charged for minutes after power-off and can cause lethal shock. Professional repair typically involves oscilloscope testing of gate drive signals, thermal imaging of IGBT modules, and access to Danfoss service software for firmware updates or board-level diagnostics. If the motor is the culprit, a motor shop can rewind or replace it and verify insulation resistance before reconnection.

**Rough cost:** A pro service call runs about $200-800 depending on whether repair is a parameter change, cable fix, motor replacement, or drive board swap.

## See Also

- [Danfoss VLT AL 4 Fault - Causes & Fix](/posts/danfoss-vlt-vfd-al-4-fault-code/)
- [Danfoss FC302 VFD Alarm 38 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-38-fault-code/)
- [Danfoss FC302 AL-69 - Causes & Fix](/posts/danfoss-fc302-vfd-al-69-fault-code/)
- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
