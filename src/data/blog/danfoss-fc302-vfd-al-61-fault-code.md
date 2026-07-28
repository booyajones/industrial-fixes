---
title: "Danfoss FC302 AL-61 - Causes & Fix"
description: "AL-61 is a feedback error: speed measured by the encoder does not match calculated speed. Most often caused by loose encoder wiring."
pubDatetime: 2026-06-24T10:00:37Z
modDatetime: 2026-06-24T10:00:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Encoder or feedback sensor"
most_likely_cause: "Loose, corroded, or broken encoder wiring and connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect encoder wiring connections for loose terminals, corrosion, or broken pins"
  - "Review parameters 4-30, 4-31, and 4-32 to see if tolerances are set too tight for the application"
  - "Reset the drive after checking wiring to see if the fault clears"
---

## What this code means
AL-61 is a Feedback Error alarm on the Danfoss FC302 VFD. It triggers when the drive's internal speed calculation (based on output voltage and frequency) does not match the actual motor speed reported by the external feedback device, such as an encoder or sensor. The discrepancy exceeds the tolerable error limit set in the drive parameters. This fault is a safety feature to prevent loss of closed-loop control and protect both the motor and the driven load.

The drive continuously compares its calculated speed against the real-time feedback signal. If the two values diverge beyond the threshold defined in parameter 4-31 (Motor Feedback Speed Error) for longer than the timeout set in parameter 4-32 (Motor Feedback Loss Timeout), the drive trips AL-61. The fault can be configured to trigger a warning or a full trip through parameter 4-30 (Motor Feedback Loss Function).

## Before You Replace Anything

Technicians often replace the encoder or motor first. Check encoder wiring connections, parameter settings (4-30, 4-31, 4-32), and test the encoder signal integrity with a megohmmeter before ordering parts.

## Common Causes

- **Loose or damaged encoder wiring (~40%)** Intermittent signal loss from loose connections, corrosion on feedback terminals, or broken wiring prevents the drive from receiving consistent speed feedback.
- **Parameter settings too strict (~25%)** Parameter 4-31 (tolerable speed error) or 4-32 (feedback loss timeout) set too low for the application causes nuisance trips when speed varies slightly under normal load changes.
- **Failed encoder or sensor (~15%)** The feedback device itself develops internal faults or intermittent signal output, leading to inconsistent speed reporting.
- **Mechanical overload or binding (~10%)** The motor shaft encounters binding, excessive friction, or mechanical overload that causes actual speed to drop below the drive's calculated speed.
- **Motor winding degradation (~5%)** Partial short circuits or insulation breakdown in motor windings cause the motor to run slower than the drive expects, triggering a speed mismatch.
- **Faulty IGBT modules or drive internal components (~5%)** Aging or damaged IGBT modules fail to regulate current properly, or noise on feedback signal lines inside the drive corrupts the speed calculation.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the encoder cable show any loose connections, corrosion, or physical damage at the drive terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean and reseat all encoder connections, then reset the drive and test. If AL-61 clears, the wiring was the issue.<br><strong>No:</strong> Proceed to check parameter settings and encoder signal integrity.</div>
</details>

<details class="dtree"><summary>Are parameters 4-31 and 4-32 set to low values (below 2% error or below 1 second timeout)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Increase parameter 4-31 to a higher tolerable error (3-5%) and parameter 4-32 to a longer timeout (2-3 seconds), then reset and test.<br><strong>No:</strong> The fault is likely hardware related, proceed to encoder and motor testing.</div>
</details>

<details class="dtree"><summary>Does the motor run normally when disconnected and the drive is tested unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or mechanical load is causing the speed mismatch, inspect for binding, overload, or motor winding faults.<br><strong>No:</strong> The drive itself has an internal fault, check IGBT modules and feedback input circuitry.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD** and lock out electrical supply following lockout/tagout procedures.
2. **Inspect encoder wiring and connections** at both the drive feedback terminals and the motor encoder. Look for loose pins, corrosion, broken shield wires, or signs of insulation damage.
3. **Test encoder signal integrity** using a megohmmeter. Measure resistance from each encoder signal wire to ground. Readings should exceed 2 MΩ. Replace the encoder if resistance is low or signal is absent.
4. **Review and adjust parameter settings** on the drive display. Navigate to parameter 4-30 (Motor Feedback Loss Function) and confirm it is set appropriately (Warning or Trip). Check parameter 4-31 (Motor Feedback Speed Error) and increase the tolerable error if load varies (typically 3-5%). Check parameter 4-32 (Motor Feedback Loss Timeout) and increase the timeout if the signal is intermittent (2-3 seconds).
5. **Disconnect the motor** and run the drive unloaded at a low speed. If AL-61 clears, the fault is in the motor or mechanical load. If AL-61 persists, the drive has an internal fault.
6. **Inspect the motor and load** for mechanical binding, overload, or damaged shaft bearings. Perform a megohmmeter test on motor windings to check insulation resistance (should exceed 2 MΩ to ground). Verify that parameter 1-24 (motor current rating) matches the actual motor nameplate rating.
7. **Check drive internal components** if the unloaded drive still trips. Inspect IGBT modules for visible damage or open phase output. Verify cooling fans are operating. Test sensor continuity and resistance on the drive's feedback input circuit. Replace the power module or IGBTs if faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder or feedback sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-61-fault-code&k=Encoder+or+feedback+sensor&tag=errorcodefixes-20) \| Select based on motor shaft size and signal type (incremental or absolute) specified in the original equipment documentation. |
| Encoder cable assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-61-fault-code&k=Encoder+cable+assembly&tag=errorcodefixes-20) \| Use a shielded cable rated for the encoder signal voltage and length, with proper grounding at the drive end only. |
| IGBT power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-61-fault-code&k=IGBT+power+module&tag=errorcodefixes-20) \| Match the module part number exactly to the FC302 model and power rating; consult Danfoss service documentation for replacement procedures. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you lack experience with three-phase electrical systems, closed-loop motor control, or encoder troubleshooting. High-voltage work on the drive's DC bus and IGBT modules carries serious shock and arc-flash hazards. If the fault persists after checking wiring and adjusting parameters, internal drive diagnostics and component-level testing require specialized tools and training. Professional service is also necessary if motor winding insulation has degraded or if mechanical binding cannot be identified and corrected safely. A technician can perform precise signal integrity tests, load current analysis, and determine whether the encoder, motor, or drive itself needs replacement.

**Rough cost:** A pro service call runs about $150-400 depending on whether wiring repair, encoder replacement, or motor testing is required.
