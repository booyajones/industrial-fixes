---
title: "Danfoss FC302 AL-101 Fault - Causes & Fix"
description: "AL-101 is not a standard Danfoss code. Check if you see Alarm 13 (overcurrent) or 14 (short circuit). Most often a motor or cable fault."
pubDatetime: 2026-06-23T10:18:29Z
modDatetime: 2026-06-23T10:18:29Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Motor output cable (shielded VFD-rated cable)"
most_likely_cause: "Motor winding insulation failure or damaged output cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect the motor output wires (U, V, W) and reset the drive. If the alarm clears with no motor connected, the drive is healthy and the fault is in the motor or cable."
  - "Check for loose motor terminal connections or visible damage to the output cable jacket."
---

## Danfoss FC302 AL-101 Fault — What It Means

There is no factory fault code named AL-101 in the Danfoss FC302 VFD manual. You likely misread Alarm 13 (Overcurrent), Alarm 14 (Short Circuit), or another numeric alarm. If the display truly shows AL-101 as text, it is a custom alarm string defined by the equipment manufacturer in parameters 15-01 through 15-04, not a universal Danfoss code. Alarm 13 means the drive output current exceeded the safe threshold (typically 150 to 160 percent of rated current) during acceleration or run, pointing to a motor short, mechanical overload, or incorrect motor parameters. Alarm 14 indicates an instantaneous short circuit or severe output fault, often from a failed IGBT module, motor winding short, or cable short to ground.

Because AL-101 is not documented, you must check your specific machine manual or the alarm text parameters to decode it. The repair steps below assume you are dealing with a standard overcurrent or short-circuit alarm, which are the most common drive faults and the most likely explanation for any unfamiliar code.

## Before You Replace Anything

Many users replace the entire drive or power board first. Disconnect the motor and run the drive unloaded. If the fault clears, the drive is healthy and the problem is downstream in the motor, cable, or load.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (~35%)** Moisture, thermal aging, or contamination breaks down motor winding insulation, causing a partial or full short that draws excessive current and trips the drive.
- **Damaged output cable (~25%)** Cable insulation damaged by rodents, sharp conduit edges, or wear creates a short to ground or phase-to-phase fault.
- **Mechanical overload on motor shaft (~15%)** A jammed bearing, seized pump, or blocked fan forces the motor to draw more current than rated, triggering overcurrent protection.
- **Failed IGBT module in the drive (~15%)** Aging or damaged IGBTs lose current regulation ability or short internally, causing the drive to detect an instantaneous overcurrent or short-circuit fault.
- **Incorrect motor parameters (~10%)** Wrong motor nameplate data entered in parameter 1-24 or auto-tune not performed causes the drive to supply inappropriate current, leading to nuisance trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor and power the drive on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive is healthy. The fault is in the motor, cable, or mechanical load. Proceed to motor insulation and cable testing.<br><strong>No:</strong> The drive has an internal component failure (IGBT module, DC bus capacitors, or power board). Call a qualified drive technician or return the unit for repair.</div>
</details>

<details class="dtree"><summary>Can you turn the motor shaft freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is not seized. Focus on motor winding insulation and cable testing.<br><strong>No:</strong> The load is jammed or the bearing is seized. Free the load, replace the bearing, and retest before returning the drive to service.</div>
</details>

<details class="dtree"><summary>Does the output cable jacket show any visible damage or rodent chewing?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the damaged cable section. Even small insulation breaks can cause short-circuit faults.<br><strong>No:</strong> Perform a megohm insulation test on the motor windings to check for hidden insulation breakdown.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off and lock out** the drive at the main disconnect. Wait five minutes for internal DC bus capacitors to discharge before opening any covers or touching terminals.
2. **Disconnect the motor** by removing the output wires (U, V, W) from the drive output terminals. Leave the input power and control wiring connected.
3. **Power the drive on** and reset the fault from the keypad or parameter menu. Attempt to run the drive with no motor connected (the drive will spin internal logic but output no mechanical load).
4. **If the alarm clears** with no motor, the drive is healthy. Proceed to step 5. If the alarm persists, the drive has an internal failure (IGBT, DC capacitor, or power board). Call a qualified technician or return the unit for factory repair.
5. **Perform a megohm insulation test** on the motor. Disconnect all motor leads from the motor terminal box. Use a 500V or 1000V megohm meter to measure resistance from each winding (U, V, W) to the motor frame ground. Readings below 2 megohms indicate insulation failure. Replace or rewind the motor.
6. **Inspect the output cable** for damage. Look for rodent chewing, sharp conduit edges, pinch points, or burned insulation. Replace any damaged cable sections with properly rated motor cable.
7. **Check motor parameters** in the drive. Verify that parameter 1-24 matches the motor nameplate data (voltage, current, frequency, speed). Run auto-tune (parameter 1-29) if the drive supports it to calibrate current control for the connected motor.
8. **Reconnect the motor** and perform a no-load test run at low speed. Monitor the drive display for current draw. If the alarm returns immediately, recheck motor insulation and cable integrity. If the drive runs cleanly at no load but trips under load, inspect the mechanical load for binding or overload.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable (shielded VFD-rated cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-101-fault-code&k=Motor+output+cable+%28shielded+VFD-rated+cable%29&tag=errorcodefixes-20) \| Match the conductor size and length to your motor nameplate current rating and distance. |
| Danfoss FC302 IGBT power module or power board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-101-fault-code&k=Danfoss+FC302+IGBT+power+module+or+power+board&tag=errorcodefixes-20) \| Part number specific to your drive frame size. Consult Danfoss or your distributor for the correct replacement module. |

## When to Call a Pro

Call a qualified technician or drive service center if the alarm persists with the motor disconnected, which points to an internal drive failure (IGBT module, rectifier, or DC bus capacitor). Professional motor insulation testing and cable fault location require a high-voltage megohm meter and experience interpreting readings. If you are not trained in VFD diagnostics or high-voltage lockout procedures, call a pro for any step beyond visual inspection and simple parameter checks. Replacing IGBT modules or power boards requires soldering, torque specs, and thermal compound application that are outside typical homeowner scope.

**Rough cost:** A pro service call runs about $300-800 for motor insulation testing, cable repair, or drive power board replacement.

## See Also

- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC302 VFD Alarm 37 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-37-fault-code/)
- [Danfoss VFD Fault AL 14 — Causes & Fix](/posts/danfoss-vfd-fault-al-14/)
- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-35-fault-code/)
