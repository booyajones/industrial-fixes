---
title: "Yaskawa GA800 VFD F0004 Fault - Causes & Fix"
description: "F0004 on a Yaskawa GA800 means an overcurrent trip. Most often caused by a ground fault or short in motor winding or cable."
pubDatetime: 2026-07-20T07:30:16Z
modDatetime: 2026-07-20T07:30:16Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Three-phase AC motor"
most_likely_cause: "Ground fault or short in motor winding or cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for cuts, abrasion, or pinch points"
  - "Check that the motor shaft turns freely by hand with power off"
  - "Reset the fault and attempt a restart to see if the fault is latched or intermittent"
---

## Yaskawa GA800 VFD F0004 Fault — What It Means

F0004 on a Yaskawa GA800 variable frequency drive indicates an overcurrent fault. The drive has detected current flow that exceeds safe operating limits and has shut down to protect itself and the connected motor. This can occur during acceleration, deceleration, or steady-state operation.

Overcurrent trips are commonly triggered by short circuits, ground faults in the motor or cabling, mechanical binding in the driven load, incorrect drive parameters, or a failing output stage inside the drive itself. Because the GA800 monitors phase currents continuously, this fault usually appears immediately when the condition develops.

## Before You Replace Anything

Technicians sometimes replace the drive when the real problem is a failed motor winding or a damaged cable. Use a megohm meter to test motor insulation resistance and cable integrity before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Ground fault or short in motor winding (~35%)** Insulation breakdown inside the motor allows current to flow to ground or between phases, triggering the overcurrent protection.
- **Damaged or undersized motor cable (~25%)** Nicked insulation, pinched conductors, or cable gauge too small for the run length creates resistance or intermittent shorts.
- **Mechanical binding or overload (~20%)** The driven load is seized, jammed, or requires more torque than the motor and drive combination can deliver.
- **Incorrect acceleration or V/F settings (~10%)** Ramp times too short or voltage-to-frequency curve mismatched to the motor can cause current spikes during startup.
- **Failed IGBT or gate driver in the drive (~10%)** An internal power semiconductor or its control circuit has shorted, causing uncontrolled current flow in one or more output phases.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on power-up before you command a run?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive output stage or DC bus may be shorted internally. Disconnect the motor cables and power up again; if the fault persists, the drive needs repair or replacement.<br><strong>No:</strong> The fault is likely in the motor circuit or load. Proceed to test the motor and cable.</div>
</details>

<details class="dtree"><summary>Does the motor spin freely by hand with the drive disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical binding is unlikely. Test motor winding insulation and cable continuity with a megohm meter.<br><strong>No:</strong> The load is jammed or the motor bearings are seized. Free the load and inspect bearings before restarting.</div>
</details>

<details class="dtree"><summary>Does a megohm test show good insulation resistance on all three motor phases to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor windings are likely intact. Inspect the cable run for damage and verify drive parameter settings match motor nameplate data.<br><strong>No:</strong> The motor winding insulation has failed. Replace or rewind the motor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the main supply and lock out the circuit feeding the VFD.
2. **Record fault history** in the drive's diagnostic menu to see if the fault is consistent or intermittent.
3. **Disconnect the motor cables** from the drive output terminals (U, V, W).
4. **Measure insulation resistance** from each motor lead to ground and between phases using a megohm meter at the voltage rating recommended by the motor manufacturer.
5. **Inspect the motor cable** for physical damage, proper routing away from sharp edges, and correct wire gauge for the cable length and motor current.
6. **Check mechanical freedom** by rotating the motor shaft by hand to confirm the load is not binding or seized.
7. **Review drive parameters** to verify acceleration time, deceleration time, motor nameplate voltage, frequency, and current match the connected motor and application.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f0004-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Match frame size, voltage, frequency, and horsepower to the original nameplate and application requirements. |
| Shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f0004-fault-code&k=Shielded+motor+cable&tag=errorcodefixes-20) \| Use VFD-rated cable with the correct gauge for cable length and motor full-load current; consult your model's table for wire sizing. |

## When to Call a Pro

Call a qualified electrician or motor technician if you are not trained to work with three-phase power, high-voltage DC bus circuits, or megohm testing. VFDs store lethal voltage in internal capacitors even after input power is removed. Incorrect wiring or parameter changes can destroy the drive or create a shock hazard. A technician can safely perform insulation tests, trace ground faults, verify drive programming, and repair or replace output modules if the drive itself has failed.

**Rough cost:** A pro service call runs about $200-800.
