---
title: "Danfoss FC302 AL-95 Fault - Causes & Fix"
description: "AL-95 (Alarm 95) means motor overload on the Danfoss FC302 VFD. Most often incorrect motor current settings in the drive parameters."
pubDatetime: 2026-06-23T10:13:45Z
modDatetime: 2026-06-23T10:13:45Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss VLT AutomationDrive FC302 replacement drive"
most_likely_cause: "Incorrect motor nominal current parameter setting"
likelihood: "the most frequent electrical cause"
diy_or_pro: "pro"
free_checks:
  - "Verify Parameter 4-02 (Motor Nominal Current) exactly matches the motor nameplate rating"
  - "Check for mechanical binding by rotating the motor shaft by hand with power off"
  - "Review Parameters 3-41 and 3-42 (Ramp Times) and increase them to reduce acceleration current"
no_buy_pct: "65%"
---

## Danfoss FC302 AL-95 Fault — What It Means

Alarm 95 on the Danfoss VLT AutomationDrive FC302 indicates the drive has detected the motor operating at a load that exceeds its rated thermal capacity for a duration that triggers the internal thermal protection model. The drive calculates the motor's thermal load using the current set in parameters (such as motor nominal current) and compares it against the configured overload limit time. This is a thermal trip, not necessarily an instantaneous current short, and the drive is protecting the motor from damage by shutting down before overheating occurs.

The fault can result from either a genuine mechanical overload on the motor or from incorrect parameter settings that cause the drive's thermal model to trip prematurely. Because the drive relies on accurate motor data to build its protection model, even a small error in parameter entry can cause nuisance trips on an otherwise healthy system.

## Before You Replace Anything

Technicians often replace the drive itself when Alarm 95 appears repeatedly, but the real cause is usually incorrect motor data in parameters 4-01 or 4-02, or a mechanical binding in the driven load. Always verify motor nameplate data matches drive settings and perform a no-load test before replacing the VFD.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect Motor Nominal Current (Param 4-02) (~35%)** The motor nominal current parameter is set higher or lower than the motor's actual nameplate rating, causing the drive's thermal model to under-estimate or over-estimate motor stress and trip prematurely.
- **Mechanical Overload on Driven Equipment (~25%)** The motor is physically driving a load heavier than its rating due to jammed conveyors, clogged pumps, binding bearings, or worn mechanical components.
- **Short Ramp Times (Params 3-41 & 3-42) (~15%)** Excessively short ramp-up or ramp-down times cause high current spikes during acceleration and deceleration that trigger the overload alarm even if steady-state load is within limits.
- **Automatic Motor Adaptation (AMA) Not Run (~10%)** Parameter 1-29 (Automatic Motor Adaptation) was not enabled or did not complete successfully, leaving the drive's thermal model inaccurate for the connected motor.
- **Insufficient Cooling or High Ambient Temperature (~10%)** The motor or drive is operating in a hot environment with poor airflow, or the motor's external cooling fan is not running or not configured correctly in Parameter 1-91.
- **Faulty Motor or Internal Short (~5%)** The motor itself has failing windings, insulation breakdown, or internal shorts that draw excessive current even under light load.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does Parameter 4-02 (Motor Nominal Current) exactly match the motor nameplate current rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> The parameter is correct. Move to mechanical and ramp-time checks.<br><strong>No:</strong> Correct Parameter 4-02 to match the motor nameplate, reset the alarm, and test. This fixes many nuisance Alarm 95 trips.</div>
</details>

<details class="dtree"><summary>With power off, can you rotate the motor shaft freely by hand without unusual resistance?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load is not binding. Focus on electrical parameters (ramp times, AMA, motor data).<br><strong>No:</strong> There is mechanical binding in the motor or driven equipment. Inspect bearings, couplings, and the load for jams or wear.</div>
</details>

<details class="dtree"><summary>Does the alarm still trip when the drive runs with the motor cables disconnected (no-load test)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive (control board, current sensor, or IGBT module) and the drive may need replacement or advanced diagnostics.<br><strong>No:</strong> The fault is in the motor or mechanical system. Perform insulation testing on the motor and recheck the load.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and lock out/tag out per facility safety procedures.
2. **Inspect the mechanical system** by rotating the motor shaft by hand to check for binding, jammed loads, worn bearings, or excessive friction in the driven equipment.
3. **Verify motor nameplate data** and compare it to Parameter 4-02 (Motor Nominal Current) and Parameter 4-01 (Motor Nominal Power) in the drive. Correct any mismatches to match the motor's actual ratings.
4. **Check Parameter 1-29** (Automatic Motor Adaptation) and run AMA if it has not been performed, following the drive manual procedure to allow the drive to learn the motor's electrical characteristics.
5. **Increase ramp times** in Parameters 3-41 (Ramp Up Time) and 3-42 (Ramp Down Time) to reduce acceleration current spikes. Try doubling the existing ramp times as a starting point.
6. **Perform a no-load test** by disconnecting the motor output cables from the drive, resetting the alarm, and running the drive with no motor connected. If the alarm still trips, the drive has an internal fault. If it does not trip, the fault is in the motor or load.
7. **Test motor insulation** using a megohmmeter to check for winding-to-ground and phase-to-phase resistance. Values below 1 megohm indicate motor insulation failure and the motor should be replaced or rewound.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss VLT AutomationDrive FC302 replacement drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-95-fault-code&k=Danfoss+VLT+AutomationDrive+FC302+replacement+drive&tag=errorcodefixes-20) \| Only needed if internal drive fault confirmed by no-load testing and all parameters are correct |
| Three-phase AC motor (matching original HP and frame) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-95-fault-code&k=Three-phase+AC+motor+%28matching+original+HP+and+frame%29&tag=errorcodefixes-20) \| Only if motor insulation testing shows winding failure or internal short |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in variable frequency drive commissioning, parameter programming, or high-voltage three-phase systems. Alarm 95 diagnostics require understanding of motor thermal models, accurate parameter entry, and the ability to safely perform no-load testing and insulation testing on motors. If mechanical binding is found, call a millwright or mechanical technician to inspect bearings, couplings, and driven equipment. If the drive itself has failed (alarm trips with no motor connected), replacement and commissioning require a trained VFD specialist to transfer parameters and perform startup checks.

**Rough cost:** A pro service call runs about $150-400 for parameter commissioning and motor testing; $800-2500 if drive replacement is genuinely needed.

## See Also

- [Danfoss FC302 ALARM 16 - Causes & Fix](/posts/danfoss-fc302-alarm-16-fault-code/)
- [Danfoss FC302 Alarm 51 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-51-fault-code/)
- [Danfoss FC302 AL-19 - Causes & Fix](/posts/danfoss-fc302-vfd-al-19-fault-code/)
- [Danfoss FC302 WARNING 77 - Causes & Fix](/posts/danfoss-fc302-vfd-al-77-fault-code/)
