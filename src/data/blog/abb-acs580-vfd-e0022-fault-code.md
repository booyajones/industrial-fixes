---
title: "ABB ACS580 VFD E0022 Fault - Causes & Fix"
description: "E0022 fault signals a motor overcurrent condition on the ABB ACS580 drive. Most often caused by a high load or motor short."
pubDatetime: 2026-07-18T07:53:30Z
modDatetime: 2026-07-18T07:53:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Replacement three-phase AC motor"
most_likely_cause: "Motor overload or mechanical binding"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the motor shaft and driven equipment for binding or mechanical resistance by rotating by hand with power off"
  - "Check all three motor lead connections at the drive output terminals for loose or corroded contacts"
  - "Review drive parameter settings to confirm motor nameplate current and acceleration time are correctly entered"
---

## ABB ACS580 VFD E0022 Fault — What It Means

The E0022 fault code on an ABB ACS580 variable frequency drive indicates that the drive has detected an overcurrent condition in the motor circuit. This means current flow exceeded the safe operating limits programmed into the drive, triggering a protective shutdown to prevent damage to the drive or motor.

The fault typically appears when the motor draws more current than expected during operation. This can happen during startup, acceleration, or steady-state running. The drive monitors current continuously and compares it against internal limits based on your parameter settings and the drive's rated capacity. When those limits are exceeded, the drive trips and logs the E0022 code.

## Before You Replace Anything

Many technicians replace the VFD itself when the fault is actually caused by a shorted motor winding or seized bearing. Always meg-test the motor insulation and check shaft rotation by hand before ordering a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor overload or mechanical binding (~35%)** The driven load is too heavy, a bearing has seized, or the equipment is jammed, forcing the motor to draw excessive current.
- **Incorrect drive parameters (~25%)** Motor nameplate data, acceleration time, or current limit parameters are set incorrectly in the drive, causing nuisance trips.
- **Shorted motor windings (~20%)** Insulation failure inside the motor creates a winding-to-winding or winding-to-ground short circuit that draws excessive current.
- **Loose or corroded motor connections (~10%)** Poor contact at output terminals or motor leads creates high resistance, heat, and localized current spikes that trigger the fault.
- **Drive output stage failure (~7%)** Internal IGBT or current sensor damage in the drive causes false overcurrent detection or actual output short circuits.
- **Undersized drive for application (~3%)** The drive is too small for the motor or load characteristics, causing repeated current limit trips during normal operation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor shaft turn freely by hand with power off and disconnect open?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical binding is unlikely. Proceed to electrical checks on motor windings and drive parameters.<br><strong>No:</strong> The load or motor bearings are binding. Repair the mechanical fault before re-energizing the drive.</div>
</details>

<details class="dtree"><summary>Are the drive parameter settings (motor nameplate current, voltage, frequency) correct per the motor data plate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter mismatch is not the cause. Focus on motor condition and connections.<br><strong>No:</strong> Reprogram the drive with correct motor data and test. Incorrect settings are a common source of nuisance overcurrent faults.</div>
</details>

<details class="dtree"><summary>Does a megohm test of the motor show insulation resistance above 1 megohm to ground on all three phases?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor windings are likely intact. Check output connections and consider drive internal faults.<br><strong>No:</strong> The motor has failed insulation. Replace or rewind the motor before returning the drive to service.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the main supply to the VFD and verify with a meter. Lock out and tag the disconnect.
2. **Inspect motor connections** at the drive output terminals (U, V, W). Tighten all terminals and look for signs of arcing or corrosion.
3. **Rotate the motor shaft by hand** to check for mechanical resistance, seized bearings, or jammed equipment on the driven load.
4. **Perform a megohm test** on the motor. Disconnect motor leads at the drive, then test each winding to ground and phase-to-phase. Consult your model's table for acceptable resistance values.
5. **Review and correct drive parameters**. Enter the motor nameplate full-load current, rated voltage, rated frequency, and motor type into the parameter menu. Verify acceleration and deceleration times are appropriate for the load inertia.
6. **Reset the fault** using the drive keypad or control interface and attempt a test run under no load or reduced load if possible.
7. **Monitor current draw** during startup and running using the drive display. Compare actual current to nameplate current to identify if the fault recurs and under what conditions.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0022-fault-code&k=Replacement+three-phase+AC+motor&tag=errorcodefixes-20) \| Match the horsepower, voltage, and frame size to your driven equipment and VFD rating. |
| ABB ACS580 VFD replacement unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0022-fault-code&k=ABB+ACS580+VFD+replacement+unit&tag=errorcodefixes-20) \| Order the exact frame size and current rating for your application; confirm all internal faults are ruled out first. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working with three-phase power or do not have a megohm tester and clamp meter. High-voltage VFD troubleshooting requires knowledge of motor theory, parameter programming, and safety procedures. A professional can perform insulation testing, verify drive output stages with specialized equipment, and reprogram parameters correctly. If the motor or drive needs replacement, a technician will size and commission the new equipment to match your application and prevent repeat failures.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [ABB ACS880 Fault 3130 — Input Phase Loss Causes & Fix](/posts/abb-acs880-fault-3130/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
- [ABB ACS550 EFB1 Fault Code - Causes & Fix](/posts/abb-acs550-vfd-efb1-fault-code/)
- [ABB ACS580 VFD E0008 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0008-fault-code/)
