---
title: "Yaskawa A1000 VFD E35 Fault - Causes & Fix"
description: "E35 typically signals an overcurrent or ground fault. Check for motor cable damage, load binding, or incorrect parameter settings."
pubDatetime: 2026-07-23T07:31:41Z
modDatetime: 2026-07-23T07:31:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Shielded VFD-rated motor cable"
most_likely_cause: "Damaged or shorted motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable for visible cuts, pinch points, or burned insulation along the entire run"
  - "Check motor shaft rotates freely by hand with no mechanical binding or seized bearings"
  - "Review parameter settings for acceleration time and current limit against the motor nameplate values"
---

## Yaskawa A1000 VFD E35 Fault — What It Means

The E35 fault code on a Yaskawa A1000 variable frequency drive generally indicates an overcurrent condition or ground fault has been detected during motor operation. The drive senses current flow that exceeds safe thresholds, either from a short circuit, insulation breakdown, or excessive mechanical load on the motor. The exact definition can vary slightly between firmware versions, so consult your drive's manual for the precise meaning on your unit.

The drive trips to protect itself and the connected motor from damage. The fault may occur at startup, during acceleration, or under steady-state load. Common underlying problems include damaged motor cables, a bound or overloaded motor shaft, incorrect acceleration or current-limit parameters, or degraded insulation in the motor windings or cable. Addressing the root cause rather than simply resetting the fault is important to prevent recurring trips or equipment damage.

## Before You Replace Anything

Technicians sometimes replace the VFD output modules or main control board before inspecting motor cables and connections. A basic insulation resistance (megger) test on the motor and cable will reveal shorts or weak insulation at a fraction of the cost of a drive repair.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~35%)** Pinched, cut, or deteriorated cable insulation creates a short circuit or ground path, triggering the overcurrent fault.
- **Motor or driven load binding (~25%)** A seized bearing, jammed coupling, or stuck mechanical load forces the motor to draw excessive current under torque.
- **Incorrect acceleration or current-limit parameters (~20%)** Overly aggressive acceleration ramps or current limits set below the motor's requirements cause the drive to trip on normal inrush.
- **Motor winding insulation failure (~15%)** Degraded or shorted windings inside the motor create a ground fault or phase-to-phase short.
- **Loose or corroded motor connections (~5%)** High-resistance joints at the drive output terminals or motor junction box generate heat and erratic current readings.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor shaft spin freely by hand with the drive powered off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is not binding; focus on electrical causes such as cable or motor winding faults.<br><strong>No:</strong> A seized bearing or jammed load is drawing excessive current; repair the mechanical issue before re-energizing the drive.</div>
</details>

<details class="dtree"><summary>Is there visible damage or wear on the motor cable jacket or armor?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the damaged cable section and perform an insulation resistance test before restarting the drive.<br><strong>No:</strong> Proceed to test motor winding insulation and verify drive parameter settings match the motor nameplate.</div>
</details>

<details class="dtree"><summary>Do the drive's acceleration time and current-limit parameters match the motor nameplate ratings?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct; the fault is likely a motor or cable insulation issue requiring electrical testing.<br><strong>No:</strong> Reprogram the drive with the correct values from the motor nameplate and test operation under light load first.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the VFD and disconnect the motor cable at both the drive output terminals and the motor junction box.
2. **Perform a visual inspection** of the entire motor cable run for cuts, pinch points, abraded insulation, or signs of overheating.
3. **Use a megohmmeter** to test insulation resistance between each motor phase and ground, and between phases; readings below one megohm suggest insulation failure.
4. **Check motor bearings and coupling** by rotating the motor shaft by hand; any binding or unusual resistance indicates a mechanical problem.
5. **Review and correct drive parameters** by comparing acceleration time, deceleration time, and current-limit settings to the motor nameplate and application requirements.
6. **Reconnect the motor cable** with clean, tight terminations at both ends, applying anti-oxidant compound to aluminum conductors if present.
7. **Clear the fault** from the drive's display or control interface and perform a no-load test run, gradually increasing speed to verify stable operation before reapplying the full mechanical load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e35-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Replace damaged sections with cable rated for inverter duty and the correct ampacity for your motor. |
| Motor bearing set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e35-fault-code&k=Motor+bearing+set&tag=errorcodefixes-20) \| If mechanical binding is confirmed, replace worn or seized bearings to restore free rotation. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to work with three-phase power, if insulation testing reveals motor winding faults that require motor disassembly, or if the fault persists after cable and parameter corrections. High-voltage VFD troubleshooting involves lethal voltages and stored energy in DC bus capacitors. A technician can perform comprehensive diagnostics with oscilloscopes and current clamps, reprogram advanced parameters safely, and coordinate motor or drive repairs under warranty if applicable.

**Rough cost:** A pro service call runs about $200-600.
