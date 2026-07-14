---
title: "Danfoss FC302 AL-94 - Causes & Fix"
description: "AL-94 is not a valid Danfoss FC302 code. You likely see AL 14 (output overcurrent). Check motor cable for shorts and test windings."
pubDatetime: 2026-06-23T10:12:55Z
modDatetime: 2026-06-23T10:12:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor winding insulation repair or rewind"
most_likely_cause: "Motor winding insulation failure or damaged motor cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Reset the fault by pressing the Reset key and verify the exact alarm code displayed"
  - "Disconnect the motor and run the VFD unloaded to see if the fault clears"
---

## Danfoss FC302 AL-94 — What It Means

AL-94 does not exist in the Danfoss FC302 (VLT AutomationDrive) alarm list. Danfoss FC302 alarms run from AL 1 through AL 84. The most likely explanation is a misread display. If the display shows two digits that look like 94, you are probably seeing AL 14 (Output Overcurrent), which means the drive output current exceeded the peak current limit and the drive shut down to protect the IGBT output stage. This fault typically trips when a motor winding shorts, a cable is damaged, or the mechanical load spikes suddenly.

If you are certain the display reads 94, verify the exact model number and firmware version of your drive and consult the printed alarm list in the drive's manual. Some older firmware or regional variants may use different numbering, but no standard FC302 documentation lists an AL 94 code.

## Before You Replace Anything

Many technicians replace the drive power board or IGBT module without testing the motor and cable first. Always perform a megohm test on the motor windings to ground and check cable continuity before ordering drive components.

[Jump to Fix](#fix)

## Common Causes

- **Misread display (~50%)** The display is dim, dirty, or viewed at an angle, causing you to misread AL 14 or another valid code as 94.
- **Motor winding insulation failure (~25%)** Moisture, contamination, or thermal aging has broken down the motor winding insulation, causing a phase-to-ground or phase-to-phase short that triggers overcurrent protection.
- **Damaged motor cable (~15%)** The cable between the drive and motor has been cut, abraded, or pinched by conduit or mechanical equipment, creating a short circuit.
- **Sudden mechanical load spike (~5%)** The driven equipment (pump, fan, conveyor) jammed or locked up, causing the motor to draw excessive current and trip the drive.
- **Failed IGBT output stage (~5%)** One or more IGBTs on the drive's inverter board have shorted internally, causing uncontrolled output current.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show 94, or could it be 14 or another two-digit number?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the display, view it straight-on in good light, and photograph it. Compare the photo to the alarm list in your manual to confirm the exact code.<br><strong>No:</strong> Proceed with diagnostics for the confirmed code (most likely AL 14 Output Overcurrent).</div>
</details>

<details class="dtree"><summary>Does the fault clear when you disconnect the motor and run the VFD unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is downstream in the motor or cable. Perform a megohm test on the motor windings and inspect the cable for damage.<br><strong>No:</strong> The problem is internal to the drive. Check the DC bus voltage, inspect the power board for burn marks, and test the IGBT module.</div>
</details>

<details class="dtree"><summary>Is the mechanical load free to move, or is something jammed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor and cable are the likely culprits. Test motor winding resistance and insulation.<br><strong>No:</strong> Free the jam, reset the fault, and test again. A locked rotor will trip overcurrent protection immediately.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and disconnect the AC supply at the main disconnect. Wait for the DC bus capacitors to discharge (at least five minutes) and verify zero voltage with a meter.
2. **Photograph the display** in good light to confirm the exact alarm code. Compare the image to the alarm list in the FC302 manual. If the code is not listed, note the firmware version (visible in parameter 0-03) and contact Danfoss support.
3. **Reset the fault** by pressing the Reset key on the keypad. If the drive does not reset, the fault is still active or the drive has a hardware failure.
4. **Disconnect the motor** at the drive output terminals (U, V, W). Power the drive back on and attempt to run it at a low speed setpoint with no load. If the fault does not reappear, the problem is external (motor or cable).
5. **Perform a megohm test** on the motor windings. Disconnect all three motor leads and measure insulation resistance from each winding to ground and between phases. Readings below 2 megohms indicate insulation failure and require motor repair or replacement.
6. **Inspect the motor cable** for physical damage along its entire length. Check for cuts, abrasion, pinch points, and water ingress. Test continuity and insulation on each conductor.
7. **If the fault persists with the motor disconnected**, measure the DC bus voltage at the drive power board (consult your model's schematic for test points). Low or unbalanced DC voltage indicates a failed rectifier or input fuse. Inspect the IGBT module and gate driver board for burn marks, swollen capacitors, or cracked solder joints.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor winding insulation repair or rewind | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-94-fault-code&k=Motor+winding+insulation+repair+or+rewind&tag=errorcodefixes-20) \| Required if the megohm test shows insulation breakdown below 2 megohms. |
| Motor cable (armored or in conduit, sized per drive output) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-94-fault-code&k=Motor+cable+%28armored+or+in+conduit%2C+sized+per+drive+output%29&tag=errorcodefixes-20) \| Replace if physical damage or insulation failure is found during inspection and testing. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician immediately if you are not trained to work with high-voltage three-phase equipment. VFDs store lethal DC bus voltage even after AC power is removed, and incorrect testing can destroy the drive or cause electrocution. A pro will have a megohm tester, oscilloscope, and IGBT tester to diagnose the fault safely. If the drive power board or IGBT module has failed, repair typically requires factory parts and specialized soldering or board-level work. If the motor windings have failed, a motor shop can rewind or replace the stator, which is often more economical than buying a new motor for large frames.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Danfoss FC302 AL-92 - Causes & Fix](/posts/danfoss-fc302-vfd-al-92-fault-code/)
- [Danfoss FC302 AL-124 - Causes & Fix](/posts/danfoss-fc302-vfd-al-124-fault-code/)
- [Danfoss FC302 Alarm 47 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-47-fault-code/)
- [Danfoss FC302 Alarm 55 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-55-fault-code/)
