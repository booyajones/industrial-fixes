---
title: "Danfoss FC302 AL-86 Fault - Causes & Fix"
description: "AL-86 means motor speed fell below the limit set in parameter 1-86. Most often caused by excessive mechanical load or wrong trip speed setting."
pubDatetime: 2026-06-24T10:02:19Z
modDatetime: 2026-06-24T10:02:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor bearings"
most_likely_cause: "excessive mechanical load on the motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect motor from mechanical load and run at no-load to see if AL-86 clears"
  - "Check parameter 1-86 to verify trip speed setting is realistic for your application speed"
  - "Tighten all motor terminal connections (U, V, W) while power is off"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-86 Fault — What It Means

The AL-86 (Trip Speed Low) fault on a Danfoss FC302 VFD means the drive detected the motor speed dropped below the programmed limit in parameter 1-86 for longer than the trip delay time (parameter 14-26). This is not a generic hardware fault. It is a speed-control logic alarm triggered when the actual RPM falls below the set threshold, indicating the motor either did not start, stalled under load, or lost speed during operation.

The drive calculates speed from output frequency and current feedback. When this calculated speed stays too low for the configured delay period, the drive trips to protect the motor and load. Common scenarios include a mechanically overloaded motor (clogged pump, jammed conveyor, seized bearing), incorrect motor parameters causing false detection, or a trip speed setting that is too high for the actual application speed.

## Before You Replace Anything

Technicians sometimes replace the VFD or motor without first checking mechanical load and parameter settings. Disconnect the motor from its load and run no-load to confirm whether the fault is mechanical or electrical before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Excessive mechanical load (~40%)** Motor is overloaded by a clogged pump, jammed conveyor, seized bearing, or other mechanical fault that prevents it from reaching set speed.
- **Trip speed setting too high (~25%)** Parameter 1-86 is set above the motor's actual operating speed under load, causing a false trip when the motor runs normally but below the threshold.
- **Incorrect motor parameters (~15%)** Motor nominal current (parameter 1-24) or motor data (parameters 1-20 to 1-25) set incorrectly, or AMA (Auto Motor Adaptation) not completed or failed, leading to inaccurate speed detection.
- **Motor wiring problems (~12%)** Loose motor connections, open phase, or shorted windings prevent proper torque generation and cause the motor to stall or run slow.
- **Low input voltage (~8%)** Insufficient supply voltage reduces DC bus voltage and available motor torque, preventing the motor from reaching target speed.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor run at full speed when disconnected from its mechanical load?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical load (pump, conveyor, fan) is the problem. Inspect for clogs, jams, seized bearings, or broken components.<br><strong>No:</strong> The issue is electrical or a parameter setting. Move to the next check.</div>
</details>

<details class="dtree"><summary>Is parameter 1-86 (Trip Speed Low) set higher than your motor's actual operating speed?</summary>
<div class="dtree-body"><strong>Yes:</strong> Lower parameter 1-86 to match your real application speed or increase parameter 14-26 (Trip Delay at Speed Low) to allow more time.<br><strong>No:</strong> Check motor wiring and parameter settings next.</div>
</details>

<details class="dtree"><summary>Are all three motor terminal connections (U, V, W) tight and all phases showing continuity?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is good. Verify motor parameters (1-20 to 1-25 and 1-24) match motor nameplate and re-run AMA (parameter 129).<br><strong>No:</strong> Tighten loose connections or repair open phase. Test motor winding insulation to ground (should be above 2 megohms).</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out the VFD** before any inspection. Confirm zero voltage at motor terminals.
2. **Verify mechanical load** by disconnecting the motor from its driven equipment (pump, fan, conveyor). Run the motor at no-load. If AL-86 clears, the mechanical load is the fault. Inspect for clogs, jams, seized bearings, or broken components and repair as needed.
3. **Check parameter 1-86 (Trip Speed Low)** on the VFD keypad or software. If set higher than the motor's actual operating speed under load (for example 1200 RPM when motor only reaches 1000 RPM), reduce it to a realistic value. Also review parameter 14-26 (Trip Delay at Speed Low) and increase it if speed drops are brief and transient.
4. **Inspect motor wiring and connections**. Tighten all motor terminal screws (U, V, W). Use a multimeter to check continuity between each phase pair (U-V, V-W, W-U). Perform a megohm test on motor windings to ground. Readings below 2 megohms indicate insulation failure and require motor repair or replacement.
5. **Review motor parameters in the VFD**. Confirm parameter 1-24 (Motor Nominal Current) matches the motor nameplate amperage. Verify parameters 1-20 to 1-25 (Motor Data) are correct for motor voltage, frequency, power, and RPM. If AMA (Auto Motor Adaptation) was skipped or failed, run it via parameter 129 to allow the drive to learn motor characteristics.
6. **Check input voltage at the VFD supply terminals**. Low supply voltage reduces DC bus voltage and available torque. Measure line-to-line voltage and compare to VFD nameplate rating. If low, correct upstream electrical issues or use a step-up transformer.
7. **Clear the fault and test run**. After repairs, reset the VFD and gradually increase speed reference while monitoring motor current and frequency. If AL-86 does not return and motor reaches target speed, the issue is resolved. If the fault returns immediately, recheck load and parameters or contact Danfoss support for advanced diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-86-fault-code&k=Motor+bearings&tag=errorcodefixes-20) \| If mechanical overload is due to seized or damaged bearings |
| Motor cable and terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-86-fault-code&k=Motor+cable+and+terminals&tag=errorcodefixes-20) \| If phase wiring is damaged or corroded beyond cleaning |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work with industrial three-phase power and variable frequency drives. Diagnosing AL-86 requires measuring motor parameters, reviewing and adjusting drive parameters (1-86, 14-26, 1-20 to 1-25, 129), and safely working inside the VFD enclosure. If mechanical inspection and basic wiring checks do not resolve the fault, a technician with Danfoss programming tools and motor testing equipment is needed to perform AMA tuning, verify torque output, and rule out drive internal faults or motor winding damage.

**Rough cost:** A pro service call runs about $200-600 depending on root cause.
