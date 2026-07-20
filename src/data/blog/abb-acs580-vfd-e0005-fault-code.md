---
title: "ABB ACS580 VFD E0005 Fault Code - Causes & Fix"
description: "E0005 on an ABB ACS580 VFD signals an overcurrent fault. Most often caused by incorrect motor parameters or a short in the motor."
pubDatetime: 2026-07-18T07:39:13Z
modDatetime: 2026-07-18T07:39:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "VFD-rated motor cable"
most_likely_cause: "Incorrect motor parameter settings or motor cable short"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the motor nameplate and compare rated current, voltage, and frequency to the VFD parameter settings in the control panel"
  - "Disconnect the motor cables from the VFD output terminals and inspect for visible damage, scorching, or pinched insulation"
  - "Reset the fault and observe if it trips immediately on power-up or only when the motor is commanded to run"
---

## ABB ACS580 VFD E0005 Fault Code — What It Means

The E0005 fault code on an ABB ACS580 variable frequency drive indicates an overcurrent condition detected in the motor circuit. This means the drive has measured a current flow exceeding safe limits, either during startup, acceleration, or steady-state operation. The drive shuts down immediately to protect itself and the connected motor from damage.

This fault can be triggered by electrical faults such as shorted motor windings or cables, mechanical problems like a locked rotor or excessive load, or configuration errors where the drive parameters do not match the motor nameplate data. Because the ACS580 monitors current continuously, any sudden spike or sustained overload will trip this protective function.

## Before You Replace Anything

Many users replace the VFD itself when the fault is actually caused by a shorted motor or incorrect parameter programming. Always verify motor parameters match the nameplate and perform a megger test on the motor windings and cable before replacing the drive.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor parameters programmed into the VFD (~35%)** When nominal motor current, voltage, frequency, or power ratings in the drive do not match the actual motor nameplate, the drive may see normal motor current as an overcurrent condition.
- **Shorted or grounded motor windings (~25%)** Insulation breakdown inside the motor creates a low-resistance path that draws excessive current and trips the drive immediately.
- **Damaged or shorted motor cable (~20%)** Pinched, cut, or degraded insulation in the cable between the VFD output and the motor can cause phase-to-phase or phase-to-ground faults.
- **Mechanical overload or locked rotor (~10%)** A jammed pump, seized bearing, or blockage in the driven equipment forces the motor to draw excessive current trying to overcome the load.
- **Acceleration or deceleration ramp time set too short (~7%)** Demanding that a high-inertia load accelerate or decelerate too quickly can cause current spikes that exceed the drive's overcurrent threshold.
- **Faulty current sensors or internal drive fault (~3%)** Failed current transducers inside the VFD or a shorted IGBT module can falsely report or create an actual overcurrent condition.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault trip immediately when you power up the VFD, before issuing a run command?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is electrical, most likely a short in the motor cable or motor windings; disconnect the motor and check cable insulation and motor winding resistance.<br><strong>No:</strong> The fault occurs under load, so check motor parameters in the drive menu and verify the driven equipment is free to rotate without binding.</div>
</details>

<details class="dtree"><summary>Do the motor nameplate amps, voltage, and frequency exactly match the values programmed in the VFD parameter menu?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter mismatch is not the cause; proceed to check for mechanical overload or electrical shorts in the motor and cable.<br><strong>No:</strong> Re-enter the correct motor nameplate data into the drive parameters, reset the fault, and test again before troubleshooting further.</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with the VFD disconnected and the driven load uncoupled?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical binding is not the issue; focus on electrical checks such as insulation resistance testing of the motor and cable.<br><strong>No:</strong> The motor or driven equipment is mechanically seized or overloaded; repair the mechanical fault before re-energizing the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD at the main disconnect or circuit breaker and lock out the supply according to local safety procedures.
2. **Record the current parameter settings** by navigating the VFD control panel menus or using the ABB Drive Composer PC software to save a backup of the configuration.
3. **Compare motor nameplate data** to the VFD parameters for nominal current, voltage, frequency, power, and speed; correct any mismatches and save the new values.
4. **Disconnect the motor cables** from the U, V, and W output terminals of the VFD and inspect each cable for physical damage, burns, or pinched insulation.
5. **Perform an insulation resistance test** on the motor windings and motor cable using a megohmmeter set to the motor's rated voltage; readings below one megohm to ground or between phases indicate insulation failure.
6. **Check for mechanical binding** by manually rotating the motor shaft and driven equipment with the motor uncoupled; repair or clear any obstructions before reconnecting.
7. **Reconnect the motor cables** if all electrical and mechanical checks pass, restore power, reset the fault code from the control panel, and command a test run at low speed to verify normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0005-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use shielded cable rated for inverter duty; match conductor size to motor current per NEC tables |
| Replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0005-fault-code&k=Replacement+motor&tag=errorcodefixes-20) \| Select a motor with the same frame, horsepower, voltage, and mounting as the original if windings are shorted |

## When to Call a Pro

Call a qualified electrician or motor technician if you are not trained to work safely around high-voltage three-phase equipment, if you do not have a megohmmeter to test insulation resistance, or if the fault persists after verifying correct parameters and clearing mechanical issues. Professional diagnosis is necessary when the drive itself may have internal component damage, when programming requires knowledge of application-specific control modes, or when the motor must be disassembled for winding inspection or replacement.

**Rough cost:** A pro service call runs about $200-800 depending on whether the issue is programming, cable replacement, or motor repair.

## See Also

- [ABB ACS580 A5A1 Fault - Causes & Fix](/posts/abb-acs580-vfd-a5a1-fault-code/)
- [ABB ACS580 VFD E0023 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0023-fault-code/)
- [ABB ACS580 VFD E0028 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0028-fault-code/)
- [ABB ACS580 VFD E0001 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0001-fault-code/)
