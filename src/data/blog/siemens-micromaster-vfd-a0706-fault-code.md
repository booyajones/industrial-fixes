---
title: "Siemens Micromaster VFD A0706 Fault - Causes & Fix"
description: "A0706 fault on Siemens Micromaster VFD signals an overcurrent condition. Most common fix: check motor cable and insulation."
pubDatetime: 2026-07-19T07:45:05Z
modDatetime: 2026-07-19T07:45:05Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Siemens Micromaster VFD output cable (shielded motor cable)"
most_likely_cause: "damaged or shorted motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable for visible damage, pinch points, or abraded insulation along its entire run"
  - "Check all power connections at the drive output terminals and motor terminal box for looseness or corrosion"
  - "Review drive parameter settings for correct motor nameplate data and acceleration/deceleration ramp times"
---

## Siemens Micromaster VFD A0706 Fault — What It Means

The A0706 fault code on a Siemens Micromaster variable frequency drive indicates an overcurrent trip during motor operation. This fault occurs when the drive detects current flow exceeding its safe operating limits, which can happen during acceleration, deceleration, or steady-state running. The drive shuts down to protect itself and the connected motor from damage.

Because VFD fault codes can have slightly different meanings across model families, always cross-reference your specific Micromaster model's manual. However, overcurrent faults in this family generally point to issues in the motor circuit, cable integrity, drive parameter settings, or the drive's output stage itself.

## Before You Replace Anything

Technicians often replace the drive's output stage or power module first, but a simple insulation resistance test on the motor and cable with a megohmmeter usually identifies cable faults or motor winding shorts at a fraction of the cost.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable or poor insulation (~35%)** Frayed, pinched, or aged cable insulation allows phase-to-phase or phase-to-ground shorts that trip the overcurrent protection.
- **Incorrect drive parameter settings (~25%)** Motor nameplate data entered wrongly or acceleration ramps set too fast can cause current spikes beyond the drive's rating.
- **Motor winding fault or ground fault (~20%)** Shorted or grounded motor windings draw excessive current and trigger the fault during startup or running.
- **Mechanical overload on the driven equipment (~10%)** A jammed pump, seized bearing, or obstructed fan forces the motor to draw high current to maintain speed.
- **Failed drive output stage or IGBT module (~7%)** Internal semiconductor failure in the drive's power section can cause erratic current sensing and false or real overcurrent trips.
- **Loose or corroded power connections (~3%)** High-resistance connections at the drive output or motor terminals create voltage drop and current imbalance that appears as overcurrent.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on startup, before the motor begins to turn?</summary>
<div class="dtree-body"><strong>Yes:</strong> This points to a short circuit in the motor cable or motor windings. Perform an insulation resistance test with a megohmmeter on the motor and cable.<br><strong>No:</strong> The fault likely occurs under load, suggesting mechanical overload, incorrect parameters, or intermittent cable damage. Proceed to check load and parameter settings.</div>
</details>

<details class="dtree"><summary>Can you spin the motor shaft freely by hand when disconnected from the load?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor bearings are fine. Focus on cable insulation, drive parameters, and the driven equipment for binding or obstruction.<br><strong>No:</strong> Seized motor bearings or a locked rotor will cause immediate overcurrent. Replace bearings or repair the motor before restarting the drive.</div>
</details>

<details class="dtree"><summary>Have you verified that motor nameplate voltage, current, and frequency match the drive parameter settings?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter mismatch is ruled out. Test cable and motor insulation and inspect for mechanical faults in the driven load.<br><strong>No:</strong> Re-enter correct motor data into the drive parameters and adjust acceleration and deceleration ramp times to match the application, then reset and test.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD at the main circuit breaker or disconnect switch and follow lockout/tagout procedures to prevent accidental energization.
2. **Record all drive parameters** by writing down or photographing the current settings, especially motor nameplate data, ramp times, and current limits, so you can restore them if needed.
3. **Inspect the motor cable** from the drive output terminals to the motor terminal box for visible damage, sharp bends, cable ties that pinch insulation, or areas where the cable contacts metal edges.
4. **Disconnect the motor cable** at both the drive output terminals and the motor terminal box, then use a megohmmeter (insulation resistance tester) to measure phase-to-phase and phase-to-ground resistance on the cable and motor separately. Readings below one megohm indicate insulation breakdown.
5. **Check motor shaft rotation** by hand with the load decoupled if possible. The shaft should turn smoothly without binding. Listen and feel for rough bearings or mechanical interference.
6. **Review and correct drive parameters** by comparing the settings in the VFD to the motor nameplate voltage, full-load current, frequency, and power rating. Extend acceleration and deceleration ramp times if the application allows, to reduce current spikes.
7. **Reconnect and test** by restoring power, clearing the fault code per the manual, and running the motor unloaded at low speed first. Monitor drive display for current readings and listen for unusual motor noise before applying full load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster VFD output cable (shielded motor cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-a0706-fault-code&k=Siemens+Micromaster+VFD+output+cable+%28shielded+motor+cable%29&tag=errorcodefixes-20) \| Use VFD-rated shielded cable sized to your motor current rating and cable length. |
| Motor bearings (matching motor frame size) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-a0706-fault-code&k=Motor+bearings+%28matching+motor+frame+size%29&tag=errorcodefixes-20) \| Required only if shaft binding or bearing noise is confirmed during hand rotation. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work on high-voltage industrial equipment, if insulation testing reveals a fault but you cannot locate the damaged section, or if the fault persists after cable and parameter corrections. VFD troubleshooting requires familiarity with three-phase power, proper metering tools, and an understanding of motor control theory. A technician will perform insulation resistance tests, verify drive output waveforms with an oscilloscope, and check the internal power module if external causes are ruled out. Do not attempt to open the drive enclosure or test internal components without proper training and safety equipment.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Siemens G120 F01001 - Causes & Fix](/posts/siemens-g120-f01001-fault-code/)
- [Siemens Micromaster F0222 - Causes & Fix](/posts/siemens-micromaster-vfd-f0222-fault-code/)
- [Siemens Micromaster VFD A0711 Fault - Causes & Fix](/posts/siemens-micromaster-vfd-a0711-fault-code/)
- [Siemens Micromaster F0003 - Causes & Fix](/posts/siemens-micromaster-vfd-f0003-fault-code/)
