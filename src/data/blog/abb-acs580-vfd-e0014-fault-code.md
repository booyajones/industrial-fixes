---
title: "ABB ACS580 VFD E0014 Fault - Causes & Fix"
description: "E0014 signals an inverter overload or current limit on the ACS580. Most often caused by motor overload or parameter mismatch."
pubDatetime: 2026-07-18T07:48:05Z
modDatetime: 2026-07-18T07:48:05Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Motor cable replacement"
most_likely_cause: "Motor mechanical overload or jammed load"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the motor and driven load for binding or mechanical jams by spinning the shaft by hand"
  - "Review drive parameter settings against the motor nameplate to confirm current and voltage match"
  - "Reset the fault and observe if it recurs immediately or only under load"
no_buy_pct: "60%"
---

## ABB ACS580 VFD E0014 Fault — What It Means

The E0014 fault on an ABB ACS580 variable frequency drive indicates that the inverter has detected an overload condition or exceeded current limits during operation. This protection feature shuts down the drive to prevent damage to the power electronics and connected motor.

The fault typically appears when the drive attempts to deliver more current than its rating allows, when the motor is mechanically overloaded, or when drive parameters do not match the connected motor. The drive will not restart until the fault is cleared and the underlying condition is resolved.

## Before You Replace Anything

Many technicians replace the VFD when the actual problem is a mechanically bound motor or incorrect parameter settings. Always verify the motor spins freely and check parameter configuration against the motor nameplate before ordering a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the motor (~35%)** The driven equipment (pump, fan, conveyor, compressor) is jammed, seized, or has excessive friction causing the motor to draw overcurrent.
- **Motor parameter mismatch (~25%)** The VFD is programmed with incorrect motor current, voltage, or power ratings that do not match the actual connected motor nameplate.
- **Worn or failing motor bearings (~15%)** Degraded motor bearings create drag and increase current demand beyond the drive's limit.
- **Acceleration or deceleration ramp too fast (~10%)** The drive attempts to spin up or brake the load too quickly, exceeding current limits during the transition.
- **Motor cable fault or ground fault (~10%)** Damaged insulation in the motor cable or a phase-to-ground short causes excessive current draw.
- **Faulty current sensor or drive hardware (~5%)** The drive's current measurement circuit or inverter module has failed and reports false overload conditions.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor and load spin freely by hand when disconnected from power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical system is not jammed. Focus on electrical checks: verify motor parameters in the drive, inspect motor cable insulation, and check for ground faults.<br><strong>No:</strong> The load is mechanically bound. Inspect bearings, couplings, and the driven equipment for jams, misalignment, or seized components before restarting the drive.</div>
</details>

<details class="dtree"><summary>Do the drive's motor parameter settings (voltage, current, frequency) match the motor nameplate exactly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct. Check for mechanical load issues, motor cable faults, or a failing drive component. Run an autotune procedure if available.<br><strong>No:</strong> Reprogram the drive with the correct motor nameplate data. Incorrect current limits are a common cause of nuisance E0014 faults.</div>
</details>

<details class="dtree"><summary>Does the fault occur immediately on start, or only after the motor runs under load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault at startup suggests parameter mismatch, a motor cable fault, or a drive hardware problem. Perform an insulation resistance test on the motor and cable.<br><strong>No:</strong> Fault under load points to mechanical overload, insufficient ramp time, or worn motor components. Reduce load or extend acceleration ramp settings.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD and motor. Follow lockout/tagout procedures and verify zero voltage with a meter before touching any connections.
2. **Inspect the mechanical system** by manually rotating the motor shaft and driven load. Check for binding, seized bearings, jammed belts, or foreign objects in fans or pumps.
3. **Record the motor nameplate** data: voltage, current, frequency, power, and speed. Compare these values to the VFD parameter settings in the motor configuration menu.
4. **Correct any parameter mismatches** in the drive. Use the motor nameplate values to set rated voltage, current, frequency, and power. Run an autotune or motor identification routine if the drive offers one.
5. **Test motor cable insulation** with a megohmmeter. Measure phase-to-phase and phase-to-ground resistance. Replace any cable showing low insulation resistance or visible damage.
6. **Extend acceleration and deceleration ramps** if the fault occurs during speed changes. Increase ramp time settings to reduce peak current demand during transitions.
7. **Reset the fault** and restart the drive under no-load or light-load conditions. Monitor current draw on the drive display and watch for abnormal spikes or immediate faults.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable replacement | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0014-fault-code&k=Motor+cable+replacement&tag=errorcodefixes-20) \| Use shielded VFD-rated cable of the correct gauge for the motor current and run length. Ground the shield at the drive end only. |
| Motor bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0014-fault-code&k=Motor+bearings&tag=errorcodefixes-20) \| Match bearing type and size to the motor model. Use insulated bearings if the motor is VFD-driven to prevent bearing currents. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in VFD commissioning, high-voltage troubleshooting, or motor systems. Incorrect parameter settings or wiring mistakes can destroy the drive or motor. A professional should handle insulation testing, motor cable replacement, drive reprogramming, and any work inside the VFD cabinet. If the fault persists after mechanical and parameter checks, the drive may need factory repair or replacement, which requires proper disconnection and safe handling of the power electronics.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [ABB ACS580 A7A5 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-a7a5-fault-code/)
- [ABB ACS580 A4A2 - Causes & Fix](/posts/abb-acs580-vfd-a4a2-fault-code/)
- [ABB ACS550 AI1 LOSS - Causes & Fix](/posts/abb-acs550-ai1-loss-fault-code/)
- [ABB ACS580 A5A0 Fault - Causes & Fix](/posts/abb-acs580-a5a0-fault-code/)
