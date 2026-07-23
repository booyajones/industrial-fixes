---
title: "Yaskawa GA800 VFD AL-15 Fault Code - Causes & Fix"
description: "AL-15 on a Yaskawa GA800 indicates an overload trip. Most often caused by a motor or mechanical jam. Check motor current and free movement."
pubDatetime: 2026-07-21T07:36:57Z
modDatetime: 2026-07-21T07:36:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor overload relay or thermal protector"
most_likely_cause: "mechanical jam or excessive load on the driven equipment"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the driven equipment (pump, fan, conveyor) for mechanical binding or obstruction by hand rotation with power off"
  - "Review the VFD parameter settings and verify that motor nameplate data (current, voltage, Hz) matches the programmed values"
  - "Check the VFD display for real-time output current and compare to motor nameplate rating"
no_buy_pct: "60%"
---

## Yaskawa GA800 VFD AL-15 Fault Code — What It Means

The AL-15 fault code on a Yaskawa GA800 variable frequency drive signals an overload condition. The drive has detected that the motor is drawing excessive current beyond the programmed overload trip threshold. This is a protective shutdown to prevent damage to the motor, driven equipment, or the VFD itself.

The fault can stem from mechanical problems in the driven load, incorrect drive parameter settings, motor issues, or electrical faults. The GA800 continuously monitors output current and compares it to the configured overload curve. When the current exceeds the safe threshold for the programmed duration, the drive trips and displays AL-15. Review the drive's trip history and current reading to narrow down the source.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the real problem is a seized bearing or jammed pump impeller in the driven equipment. Always disconnect the motor from the load and run it unloaded to isolate whether the fault is mechanical or electrical.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical jam or overload (~40%)** A seized bearing, jammed impeller, blocked conveyor, or other mechanical fault in the driven equipment forces the motor to draw excessive current and trip the overload protection.
- **Incorrect motor parameter settings (~25%)** If the VFD is programmed with motor nameplate values that do not match the actual motor, the overload threshold may be set too low and trip prematurely during normal operation.
- **Motor winding fault (~15%)** A shorted turn, phase-to-phase short, or ground fault in the motor windings causes unbalanced or excessive current draw that triggers the overload alarm.
- **Drive output phase loss (~10%)** A loose output terminal, damaged motor cable, or faulty output transistor in the VFD can create a missing phase condition that forces the remaining phases to carry extra current.
- **Rapid acceleration or deceleration settings (~7%)** Overly aggressive ramp times or frequency changes demand high current surges that exceed the overload curve, especially with high-inertia loads.
- **Ambient temperature or cooling failure (~3%)** Blocked cooling fins, failed internal fan, or high ambient temperature reduces the VFD's current capacity and can cause nuisance overload trips even at normal motor load.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor or driven equipment turn freely by hand with power off and disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical system is not jammed. Proceed to check motor and VFD electrical health, wiring, and parameter settings.<br><strong>No:</strong> You have a mechanical problem. Repair the jammed bearing, clear the obstruction, or reduce the load before restarting the drive.</div>
</details>

<details class="dtree"><summary>Do the programmed motor parameters (current, voltage, frequency) match the motor nameplate exactly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Settings are correct. Test the motor windings for shorts or grounds and inspect the VFD output wiring and connections.<br><strong>No:</strong> Reprogram the drive with the correct nameplate values and reset the fault to see if the overload clears.</div>
</details>

<details class="dtree"><summary>When you run the motor unloaded (disconnected from the driven equipment), does the AL-15 fault still appear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor windings, motor cable, or VFD output stage. Test motor insulation resistance and check for output phase balance.<br><strong>No:</strong> The fault is caused by the driven load. Inspect for binding, misalignment, or excessive process demand.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Shut down and lock out** all power to the VFD and motor circuit at the disconnect switch before any inspection.
2. **Record the fault history** from the VFD display or keypad to capture the output current and frequency at the time of the trip.
3. **Verify motor nameplate data** and compare each value (rated current, voltage, frequency, horsepower) to the VFD parameter settings in the motor configuration menu.
4. **Disconnect the motor from the driven load** (uncouple the shaft or remove the belt) and check that the equipment turns freely by hand with no binding or unusual resistance.
5. **Test motor winding resistance and insulation** using a megohmmeter to identify shorts, opens, or ground faults in the stator windings.
6. **Inspect all motor cable connections** at the VFD output terminals and motor terminal box for loose lugs, corrosion, or signs of arcing and verify phase continuity.
7. **Clear the fault** from the VFD display, re-energize the system, and run the motor unloaded at low speed to confirm it operates without tripping before reconnecting the load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor overload relay or thermal protector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-15-fault-code&k=Motor+overload+relay+or+thermal+protector&tag=errorcodefixes-20) \| Only if the motor itself has a separate embedded protector that needs replacement after a winding fault |
| Output contactor or line reactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-15-fault-code&k=Output+contactor+or+line+reactor&tag=errorcodefixes-20) \| May be added to reduce current spikes if drive settings and mechanical issues are ruled out |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not comfortable working with three-phase power, programming VFD parameters, or performing motor insulation testing. High-voltage DC bus capacitors inside the drive remain charged and dangerous even after input power is removed. A professional can perform a full load analysis, measure phase balance with a power analyzer, verify drive output transistor health, and reprogram acceleration curves or overload settings to match your application. If the motor windings are damaged or the VFD output stage has failed, replacement or rewind work requires specialized tools and safety procedures.

**Rough cost:** A pro service call runs about $150-500.
