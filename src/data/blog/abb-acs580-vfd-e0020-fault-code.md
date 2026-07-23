---
title: "ABB ACS580 VFD E0020 Fault Code - Causes & Fix"
description: "E0020 signals an overcurrent trip on your ABB ACS580 drive. Most often caused by motor overload or incorrect parameters."
pubDatetime: 2026-07-18T07:52:05Z
modDatetime: 2026-07-18T07:52:05Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 replacement drive"
most_likely_cause: "motor overload or mechanical binding in the driven equipment"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the motor shaft turns freely by hand with power off and motor disconnected from the load"
  - "Check all three motor cable connections at both the drive output terminals and the motor terminal box for loose or corroded contacts"
  - "Review the drive parameter settings against the motor nameplate to confirm voltage, frequency, and current match"
---

## ABB ACS580 VFD E0020 Fault Code — What It Means

The E0020 fault code on an ABB ACS580 variable frequency drive indicates an overcurrent condition has been detected. The drive has shut down to protect itself and the connected motor from damage caused by excessive current flow beyond safe operating limits.

Overcurrent faults can stem from mechanical problems in the driven load, electrical issues in the motor or cabling, or incorrect drive parameter settings that do not match the motor nameplate data. The drive continuously monitors phase currents and will trip when current exceeds programmed thresholds for protection.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the actual problem is a seized bearing or jammed load on the motor. Always disconnect the motor from its load and check that the motor shaft spins freely before condemning the VFD.

[Jump to Fix](#fix)

## Common Causes

- **Motor overload or mechanical binding (~40%)** A jammed pump, seized bearing, or blocked fan forces the motor to draw excessive current trying to overcome the mechanical resistance.
- **Incorrect motor parameters programmed in the drive (~25%)** When the rated current or motor nameplate values entered in the drive do not match the actual motor, the overcurrent threshold may be set too low or the drive may apply incorrect V/Hz curves.
- **Damaged or undersized motor cable (~15%)** A cable with broken strands, insulation damage, or inadequate gauge can create high resistance or phase imbalance that spikes current on one or more legs.
- **Motor winding fault or ground fault (~10%)** Shorted turns, phase-to-phase shorts, or insulation breakdown inside the motor will draw excessive current and may trip the drive immediately on start.
- **Drive output stage failure (~7%)** A faulty IGBT or gate driver in the inverter section can produce unbalanced output or fail to regulate current properly, triggering an overcurrent trip.
- **Excessive acceleration or deceleration ramp rate (~3%)** Ramp times set too short force the motor to accelerate or decelerate faster than the inertia of the load allows, causing current spikes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor spin freely by hand when disconnected from the driven load with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor bearings and rotor are likely okay. Focus on cable connections, parameter settings, and motor winding tests.<br><strong>No:</strong> The mechanical load or motor bearings are binding. Inspect the driven equipment for jams, blockages, or seized bearings before restarting.</div>
</details>

<details class="dtree"><summary>Do the programmed motor parameters in the drive match every value on the motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameters are correct. Check motor cable integrity and perform a motor insulation resistance test to rule out winding faults.<br><strong>No:</strong> Re-enter the correct nameplate voltage, current, frequency, speed, and power factor. Run the drive's auto-tune or motor identification routine if available.</div>
</details>

<details class="dtree"><summary>Does the fault occur immediately on start, or only after the motor runs for a while?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate trips point to a short circuit, severe parameter mismatch, or drive hardware fault. Disconnect the motor and test the drive with no load if possible.<br><strong>No:</strong> Delayed trips suggest thermal overload, gradual mechanical binding, or marginal cable issues that worsen under load. Monitor current readings during operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out all power** to the VFD and motor circuit at the main disconnect or breaker.
2. **Disconnect the motor from the driven load** by uncoupling the shaft or removing the belt so the motor can spin freely.
3. **Inspect motor cable connections** at the drive output terminals and the motor terminal box for tightness, corrosion, or signs of arcing.
4. **Verify motor parameters** by comparing every value programmed in the drive (rated voltage, current, frequency, speed, power factor) against the motor nameplate.
5. **Perform a motor insulation resistance test** using a megohmmeter set to 500 V or 1000 V, testing each winding phase to ground and phase to phase; readings below one megohm suggest winding damage.
6. **Check the motor shaft** by rotating it by hand to confirm smooth rotation with no binding, grinding, or excessive drag from bearings.
7. **Reset the fault** on the drive keypad or through the control panel and attempt a no-load motor start to see if the fault recurs without mechanical load.
8. **Monitor real-time current** on the drive display during a test run; compare the readings to the motor nameplate full-load current to identify imbalance or overload conditions.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 replacement drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0020-fault-code&k=ABB+ACS580+replacement+drive&tag=errorcodefixes-20) \| Only if internal diagnostics confirm drive hardware failure after all external causes are ruled out. |
| Three-phase shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0020-fault-code&k=Three-phase+shielded+motor+cable&tag=errorcodefixes-20) \| Select cable gauge and type per drive and motor specifications if existing cable is damaged or undersized. |

## When to Call a Pro

Call a qualified electrician or drive technician if you lack experience with three-phase power, VFD programming, or motor testing equipment. High-voltage DC bus capacitors inside the drive remain charged and dangerous even after input power is removed. A technician can perform megohm testing, current signature analysis, and drive component-level diagnostics that require specialized tools and safety training. If the fault persists after correcting parameters and verifying mechanical freedom, the drive may need factory repair or replacement, which should be handled by an authorized service center to preserve warranty coverage.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [ABB ACS580 VFD E0038 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0038-fault-code/)
- [ABB ACS550 EFB3 Fault - Causes & Fix](/posts/abb-acs550-efb3-fault-code/)
- [ABB VFD Fault 3130 — Input Phase Loss Fix](/posts/abb-vfd-fault-3130/)
- [ABB ACS580 VFD E0039 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0039-fault-code/)
