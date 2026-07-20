---
title: "ABB ACS580 VFD E0027 Fault Code - Causes & Fix"
description: "E0027 on an ABB ACS580 drive signals an overcurrent trip. Most often caused by a short in motor or output cables; check wiring first."
pubDatetime: 2026-07-18T07:57:14Z
modDatetime: 2026-07-18T07:57:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 output cable (shielded VFD-rated)"
most_likely_cause: "Short circuit or ground fault in motor cables or motor windings"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor and output cables for visible damage, pinched insulation, or scorch marks"
  - "Check for loose or corroded connections at drive output terminals and motor junction box"
  - "Review drive parameter settings for acceleration time and current limit values that may be too aggressive"
---

## ABB ACS580 VFD E0027 Fault Code — What It Means

The E0027 fault code on an ABB ACS580 variable frequency drive indicates an overcurrent condition has been detected. The drive has shut down to protect itself and the connected motor from damage caused by current exceeding safe operating limits.

This fault typically appears when the drive measures instantaneous current levels that exceed the programmed trip threshold. The condition may occur during acceleration, deceleration, steady-state operation, or at startup depending on the root cause. The drive will remain in a faulted state until the underlying issue is corrected and the fault is manually reset.

## Before You Replace Anything

Technicians sometimes replace the drive power module when the actual problem is a failing motor or damaged output cable. Always megger-test the motor and cables for insulation resistance and check for shorted windings before ordering drive components.

[Jump to Fix](#fix)

## Common Causes

- **Shorted or grounded motor cable (~35%)** Damaged insulation on output cables between drive and motor creates a path to ground or phase-to-phase short that draws excessive current.
- **Motor winding failure (~30%)** Shorted turns or a ground fault inside the motor windings cause the drive to see an overcurrent condition when energized.
- **Mechanical overload or jam (~15%)** A seized bearing, jammed load, or mechanical bind forces the motor to draw excessive current trying to turn the shaft.
- **Incorrect acceleration or deceleration ramp (~10%)** Ramp times set too short for the load inertia cause current spikes during speed changes that exceed the trip threshold.
- **Drive output stage failure (~7%)** A faulty IGBT or gate driver circuit inside the drive power module produces unbalanced output that triggers overcurrent protection.
- **Incorrect motor or drive parameters (~3%)** Motor nameplate data entered incorrectly or current limit set too low causes nuisance trips under normal load.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately when you attempt to start, before the motor begins turning?</summary>
<div class="dtree-body"><strong>Yes:</strong> This points to a short in the cables or motor windings rather than a mechanical or parameter issue; proceed to insulation testing.<br><strong>No:</strong> The motor is able to start, suggesting the overcurrent happens under load; check for mechanical binding or incorrect ramp settings.</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with power off and the load disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical system is not jammed; focus on electrical causes like cable damage, motor winding faults, or parameter settings.<br><strong>No:</strong> A mechanical jam or seized bearing is forcing the motor to draw high current; repair or replace the motor or driven equipment before re-energizing.</div>
</details>

<details class="dtree"><summary>Have you recently changed the motor, cables, or drive parameters?</summary>
<div class="dtree-body"><strong>Yes:</strong> Recent changes are a likely source; verify motor nameplate data matches drive parameters and check new cable routing for damage or incorrect connections.<br><strong>No:</strong> An existing component has likely failed or degraded; perform insulation resistance tests on motor and cables to find the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the upstream disconnect or circuit breaker and verify zero voltage at the drive input terminals using a multimeter; lock out and tag the disconnect.
2. **Inspect all output cables** from drive to motor for physical damage, cuts, pinched insulation, or areas where the cable jacket is melted or discolored; check inside conduit and junction boxes.
3. **Disconnect motor cables** at both the drive output terminals and the motor junction box; label each phase wire for correct reconnection.
4. **Megger-test the motor windings** with an insulation resistance tester set to 500 or 1000 volts; measure from each phase to ground and phase to phase; readings below one megohm indicate a winding or cable fault.
5. **Megger-test the output cables separately** by disconnecting them at both ends; measure insulation resistance from each conductor to ground and conductor to conductor; replace any cable that shows low resistance.
6. **Check motor shaft rotation** by hand with the load uncoupled if possible; resistance or grinding indicates a bearing or mechanical problem that must be repaired before applying power.
7. **Review drive parameter settings** using the keypad or PC software; verify motor nameplate voltage, current, frequency, and power match the values programmed; confirm acceleration and deceleration times are appropriate for the load inertia (consult your model's parameter manual).
8. **Reconnect cables** if all insulation tests pass and mechanical checks are clear; make sure phase connections match original configuration and all terminals are tight.
9. **Restore power and reset the fault** using the drive keypad; attempt a slow-speed no-load test run; if the fault recurs immediately, the drive power module may be damaged and requires manufacturer service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 output cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0027-fault-code&k=ABB+ACS580+output+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Match cable gauge and length to your motor nameplate current and distance; must be shielded and rated for VFD use. |
| Three-phase AC induction motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0027-fault-code&k=Three-phase+AC+induction+motor&tag=errorcodefixes-20) \| Must match original motor voltage, horsepower, and frame size; verify nameplate data before ordering. |

## When to Call a Pro

Call a qualified electrician or motor technician if you do not have an insulation resistance tester or the training to interpret megger readings safely. Professional service is also needed if the motor windings test faulty and the motor must be rewound or replaced, or if the drive itself shows internal faults after all external causes have been ruled out. High-voltage work on VFDs and three-phase motors requires proper safety equipment and knowledge of arc flash hazards. If the fault persists after all external wiring and mechanical issues have been corrected, the drive may need factory repair or replacement of internal power modules, which is beyond typical field service capability.

**Rough cost:** A pro service call runs about $200-800.
