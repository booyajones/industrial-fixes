---
title: "Danfoss FC302 AL-142 - Causes & Fix"
description: "AL-142 is not a real Danfoss code. The actual fault is Alarm 13 (ground fault) or Alarm 14 (overcurrent). Most common: motor insulation failure."
pubDatetime: 2026-06-25T09:29:09Z
modDatetime: 2026-06-25T09:29:09Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Replacement motor (if insulation fails megohm test)"
most_likely_cause: "motor winding insulation failure"
likelihood: "the most common cause for Alarm 13"
diy_or_pro: "pro"
free_checks:
  - "Power off the drive, wait 5 minutes for capacitors to discharge, then disconnect motor cable from U/V/W output terminals and run the drive unloaded to see if Alarm 13 or 14 clears"
  - "Check for loose motor terminal connections or damaged cable insulation where the cable enters the motor junction box"
---

## Danfoss FC302 AL-142 — What It Means

There is no Danfoss fault code AL-142 for the FC302 VFD. The number 142 refers to parameter 1426 (trip delay at inverter fault), not an alarm. The actual faults protected by parameter 1426 are Alarm 13 (ground fault) and Alarm 14 (overcurrent). Alarm 13 means the drive detects current flowing from a motor phase to ground, indicating a short in the motor winding, cable insulation, or drive power board. Alarm 14 means output current exceeded the drive's rated limit during acceleration, deceleration, or running, typically from motor overload, too-short deceleration ramps on high-inertia loads, or failed IGBTs inside the drive.

Parameter 1426 sets how many seconds the drive waits before tripping when it sees an intermittent inverter fault. Increasing this delay can prevent nuisance trips on high-inertia applications, but it does not fix the underlying ground fault or overcurrent condition that triggered Alarm 13 or 14.

## Before You Replace Anything

Technicians often replace the entire drive or control card before testing the motor and cable. Disconnect the motor cable and run the drive unloaded. If the alarm clears, the fault is external (motor or cable), not the drive itself.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure (Alarm 13) (~35%)** Moisture, contamination, or thermal stress breaks down the insulation between motor windings and ground, causing current to leak to the motor frame.
- **Short deceleration ramp on high-inertia load (Alarm 14) (~25%)** The drive tries to stop a heavy or high-speed load too quickly, forcing excess regenerative current through the output stage and tripping the overcurrent protection.
- **Damaged motor cable insulation (~15%)** Sharp conduit edges, rodent damage, or pinched cable creates a path from a motor phase wire to ground or cable shield.
- **Failed IGBT module or gate driver in the drive (~15%)** A shorted IGBT or failed gate driver circuit inside the VFD output stage causes uncontrolled current flow and triggers Alarm 13 or 14 even with no motor connected.
- **Motor mechanically overloaded or locked (~10%)** Bearings seized, pump jammed, or load friction exceeds motor rating, drawing excessive current during run and tripping Alarm 14.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor cable and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or cable. Perform a megohm test on the motor windings to ground and inspect the cable for damage.<br><strong>No:</strong> The fault is internal to the drive. Test the DC bus voltage and output IGBTs, or consult a VFD technician to check the power board and control card.</div>
</details>

<details class="dtree"><summary>Does the motor megohm test show less than 2 megohms to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation has failed. Replace the motor or have the windings professionally re-insulated.<br><strong>No:</strong> Check the motor cable for pinched insulation, loose connections at the motor junction box, or damage along the conduit run.</div>
</details>

<details class="dtree"><summary>Is the DC bus voltage lower than 300 VDC on a 400 VAC input drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The rectifier diodes or input fuse may have failed. Replace the rectifier module or power board.<br><strong>No:</strong> Test the output IGBTs for shorts or consult the drive manufacturer for control-card diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** and wait at least 5 minutes for the DC bus capacitors to discharge fully before touching any terminals.
2. **Disconnect the motor cable** from the drive output terminals (U, V, W) and leave the drive input power connected.
3. **Run the drive unloaded** by resetting the alarm and starting a low-speed command. If Alarm 13 or 14 clears, the fault is external (motor or cable). If it persists, the fault is internal (drive power board or IGBTs).
4. **Perform a megohm test** on the motor windings to ground using an insulation tester. Readings below 2 megohms indicate motor insulation failure and require motor replacement or rewinding.
5. **Inspect the motor cable** for damaged insulation, sharp bends, pinched points in conduit, or rodent damage. Repair or replace any damaged cable.
6. **Check motor terminal connections** at the junction box for loose or corroded wires that create resistance spikes and false ground readings.
7. **If the fault is internal**, measure the DC bus voltage across the main capacitor terminals (consult a qualified technician). Low DC bus or shorted IGBTs require power-board replacement or drive swap.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement motor (if insulation fails megohm test) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-142-fault-code&k=Replacement+motor+%28if+insulation+fails+megohm+test%29&tag=errorcodefixes-20) \| Match motor frame size, voltage, and HP rating to your application. Confirm mounting and shaft dimensions before ordering. |
| Motor cable (shielded VFD-rated cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-142-fault-code&k=Motor+cable+%28shielded+VFD-rated+cable%29&tag=errorcodefixes-20) \| Use VFD-rated cable with continuous shield bonded at both ends to prevent ground-fault nuisance trips. |
| Danfoss FC302 power board or IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-142-fault-code&k=Danfoss+FC302+power+board+or+IGBT+module&tag=errorcodefixes-20) \| Factory or authorized-distributor part only. Requires serial-number matching and careful installation by a VFD technician. |

## When to Call a Pro

Call a VFD technician or motor specialist if the alarm persists with the motor disconnected, if you measure low DC bus voltage, or if megohm testing shows motor insulation below 2 megohms and you lack rewinding equipment. High-voltage DC bus capacitors inside the drive hold lethal charge for minutes after power-off, and IGBT testing requires specialized equipment and knowledge of gate-driver circuits. If the motor passes insulation tests but the cable is routed through underground conduit or inaccessible chases, a professional can pull new VFD-rated shielded cable and verify proper shield grounding at both ends to prevent ground-fault recurrence.

**Rough cost:** A pro service call runs about $150-500.

## See Also

- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC302 AL-159 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-159-fault-code/)
- [Danfoss FC302 ALARM 15 - Causes & Fix](/posts/danfoss-fc302-alarm-15-fault-code/)
- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/posts/danfoss-fc302-alarm-12/)
