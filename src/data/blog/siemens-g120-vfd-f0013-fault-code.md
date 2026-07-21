---
title: "Siemens G120 VFD F0013 Fault - Causes & Fix"
description: "F0013 on a Siemens G120 VFD signals an overcurrent trip. Most often the motor or cable insulation has failed. Check connections first."
pubDatetime: 2026-07-19T07:33:07Z
modDatetime: 2026-07-19T07:33:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Motor cable (shielded, VFD-rated)"
most_likely_cause: "Motor insulation failure or phase-to-phase short"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for damage, pinch points, or exposed conductor"
  - "Check all power terminal connections at the drive output and motor junction box for tightness"
  - "Review drive parameter P0307 (motor rated current) to confirm it matches the motor nameplate"
---

## Siemens G120 VFD F0013 Fault — What It Means

The F0013 fault on a Siemens G120 variable frequency drive indicates the drive has detected an overcurrent condition and shut down to protect itself and the motor. This code typically appears when the current flowing to the motor exceeds safe limits, either instantaneously or over a short period.

The G120 monitors output current continuously and compares it against internal thresholds. When current spikes beyond those limits, the drive trips F0013 to prevent damage to the power electronics, motor windings, and connected equipment. The fault can result from problems in the motor, the motor cable, the driven load, or the drive's own parameter settings.

## Before You Replace Anything

Many technicians replace the drive power module when the real problem is degraded motor winding insulation or a shorted cable. Always megger-test the motor and cable to ground and phase-to-phase before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding or cable insulation failure (~40%)** A breakdown in motor winding insulation or a damaged output cable creates a low-resistance path that draws excessive current and trips the drive immediately.
- **Mechanical overload or seized bearing (~25%)** A jammed load, seized motor bearing, or obstruction forces the motor to draw high current as it struggles to turn under excessive torque.
- **Incorrect drive parameter settings (~15%)** Motor-rated current, acceleration ramp time, or V/Hz curve parameters set too aggressively can cause the drive to trip on overcurrent during startup or load changes.
- **Loose or corroded output terminal connection (~10%)** A poor connection at the drive output terminals or motor junction box increases resistance, generates heat, and can cause arcing that mimics an overcurrent fault.
- **Drive power module failure (~7%)** A shorted IGBT or diode in the drive's output stage will create an internal fault path that registers as overcurrent, though this is less common than external issues.
- **Ground fault in motor or cable (~3%)** Insulation degradation allows current to leak to ground through the motor frame or cable shield, which the drive may read as an overcurrent condition depending on sensor placement.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately when you enable the drive, before the motor even begins to turn?</summary>
<div class="dtree-body"><strong>Yes:</strong> This suggests a short circuit in the motor windings, cable, or drive output stage. Disconnect the motor cable from the drive and attempt to run the drive unloaded (consult your manual for safe no-load operation). If the fault clears, the problem is external to the drive.<br><strong>No:</strong> The fault likely occurs under load or during acceleration, pointing to mechanical overload, parameter mismatch, or intermittent connection issues. Proceed to insulation and load checks.</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with power off and the drive disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical binding is not the issue. Focus on electrical tests: megger the motor and cable, verify parameter settings, and inspect connections.<br><strong>No:</strong> The load or motor bearings are seized or obstructed. Clear the obstruction, replace worn bearings, or reduce the mechanical load before returning the drive to service.</div>
</details>

<details class="dtree"><summary>Does the drive parameter P0307 (motor rated current) match the current shown on the motor nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter settings are likely correct. The fault is probably due to a real overcurrent from a motor, cable, or mechanical fault.<br><strong>No:</strong> Set P0307 to match the motor nameplate current. An incorrect value can cause nuisance trips or allow real overcurrent conditions to go undetected.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** from the drive at the upstream disconnect or breaker and follow lockout-tagout procedures. Wait at least five minutes for the DC bus capacitors to discharge before opening covers.
2. **Inspect the motor cable** for cuts, abrasion, crush damage, or any exposed conductor. Pay special attention to areas where the cable passes through conduit, cable trays, or moving machine parts.
3. **Check all power connections** at the drive output terminals (U, V, W) and at the motor junction box. Tighten any loose terminals to the torque specified in the drive and motor installation manuals.
4. **Perform an insulation resistance test** using a 500 V or 1000 V megohmmeter. Test motor windings to ground and phase-to-phase with the motor cable disconnected from the drive. Readings below 1 MΩ indicate insulation failure. Also test the cable separately.
5. **Verify drive parameter settings** using the BOP-2 keypad or commissioning software. Confirm P0307 (motor rated current) matches the motor nameplate, P1120 (ramp-up time) is not too short for the load inertia, and P1300 (control mode) is appropriate for your application.
6. **Inspect the driven load** for mechanical binding, worn bearings, or obstructions. Rotate the motor shaft by hand with power off to feel for tight spots or rough rotation.
7. **Clear the fault** from the drive by cycling power or pressing the reset button. Restart the drive and observe the output current on the display during acceleration and at steady state. Compare the running current to the motor nameplate value.
8. **If the fault persists** after confirming good insulation, correct parameters, and free mechanical rotation, suspect a failed drive output stage and consult a qualified VFD technician or the drive manufacturer for further diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded, VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0013-fault-code&k=Motor+cable+%28shielded%2C+VFD-rated%29&tag=errorcodefixes-20) \| Use cable rated for inverter duty with adequate insulation and continuous shield for the cable length and voltage class of your drive. |
| Motor bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0013-fault-code&k=Motor+bearings&tag=errorcodefixes-20) \| Match the bearing type and size to your motor frame. Insulated bearings may be required for VFD applications to prevent shaft-voltage damage. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work safely with three-phase power, if insulation testing reveals a motor winding failure that requires motor repair or replacement, or if the fault persists after all external checks and you suspect a failed drive power module. VFD troubleshooting involves high DC bus voltages (typically 650 V or more on 480 V systems) that remain present for several minutes after input power is removed. Incorrect parameter changes can damage the drive or motor, and improper motor cable installation can create ground faults or EMI issues. A technician with oscilloscope and current-clamp tools can measure output waveforms and identify intermittent faults that simple checks miss.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [Siemens Micromaster VFD A0706 Fault - Causes & Fix](/posts/siemens-micromaster-vfd-a0706-fault-code/)
- [Siemens G120 F03505 - Causes & Fix](/posts/siemens-g120-f03505-fault-code/)
- [Siemens Micromaster VFD A0542 Fault - Causes & Fix](/posts/siemens-micromaster-vfd-a0542-fault-code/)
- [Siemens Micromaster F0071 - Causes & Fix](/posts/siemens-micromaster-vfd-f0071-fault-code/)
