---
title: "Yaskawa GA800 VFD AL-02 Fault - Causes & Fix"
description: "AL-02 indicates a ground fault or overcurrent. Check input power wiring, motor cable routing, and insulation before replacing boards."
pubDatetime: 2026-07-21T07:27:28Z
modDatetime: 2026-07-21T07:27:28Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "IGBT Power Module"
most_likely_cause: "Motor cable insulation failure or improper grounding"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable routing for sharp bends, pinch points, or contact with metal enclosures"
  - "Check all ground connections at the drive, motor, and panel for tightness and corrosion"
  - "Review the drive's alarm history display for additional fault details or patterns"
---

## Yaskawa GA800 VFD AL-02 Fault — What It Means

The AL-02 fault on a Yaskawa GA800 variable frequency drive typically signals a ground fault or overcurrent condition detected during operation. The drive has shut down to protect itself and the connected motor from damage. This fault can arise from problems in the motor, the motor cable, the input power supply, or internal drive components.

Because the exact definition of AL-02 can vary by firmware version and parameter settings, always consult your drive's user manual and the alarm history screen for additional detail. The fault may be logged with subcodes or time stamps that narrow the root cause.

## Before You Replace Anything

Technicians sometimes replace the IGBT board or control card without first meggering the motor and checking cable routing. A 500 V insulation resistance test on the motor and cable often reveals the true fault and saves the cost of a new drive module.

[Jump to Fix](#fix)

## Common Causes

- **Motor or cable insulation breakdown (~40%)** Damaged insulation on the motor windings or in the output cable allows current to leak to ground, triggering the fault.
- **Improper or missing ground connection (~25%)** A loose, corroded, or inadequate ground path at the motor or drive can cause stray current and false ground-fault detection.
- **Input power transient or phase imbalance (~15%)** Voltage spikes, sags, or unbalanced three-phase supply can push the drive into overcurrent protection.
- **Motor overload or mechanical binding (~10%)** A seized bearing, locked rotor, or overloaded pump forces the drive to draw excess current and trip.
- **Faulty current sensor or control board (~7%)** An internal current transducer or board component may misread or falsely signal a fault condition.
- **Incorrect drive parameters (~3%)** Overcurrent trip thresholds, acceleration ramps, or V/F settings that do not match the motor nameplate can cause nuisance trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on power-up before the motor runs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is likely in the input power supply, ground wiring, or a failed drive component; check incoming voltage and all ground connections before proceeding.<br><strong>No:</strong> The fault occurs under load, so focus on the motor cable insulation, motor condition, and mechanical load first.</div>
</details>

<details class="dtree"><summary>Can you disconnect the motor cable at the drive and clear the fault by running the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is external to the drive; inspect and test the motor cable and motor windings for insulation breakdown or ground faults.<br><strong>No:</strong> The drive itself is likely at fault; internal current sensors, IGBT modules, or control circuitry may need replacement or factory service.</div>
</details>

<details class="dtree"><summary>Is the motor free to rotate by hand and are all three phases of input power balanced within a few volts?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical and supply issues are unlikely; perform an insulation resistance test on the motor and cable, then review drive parameters.<br><strong>No:</strong> Fix the mechanical binding or voltage imbalance before replacing any drive components; these conditions can damage even a healthy drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive at the main disconnect, then wait for the DC bus capacitors to discharge per the manual's safety instructions.
2. **Record all parameter settings** and the alarm history from the keypad or software, noting the exact time and load conditions when AL-02 appeared.
3. **Inspect all ground connections** at the drive PE terminal, motor frame, and panel enclosure; clean any corrosion and torque to the manufacturer's specification.
4. **Check motor cable routing** for damage, sharp bends, or contact with metal edges; make sure shielded cable is grounded at one end only and routed away from power wiring.
5. **Perform an insulation resistance test** on the motor and cable using a 500 V megohmmeter; consult your model's table for minimum acceptable resistance (typically above 10 MΩ for a healthy motor).
6. **Verify input power quality** with a multimeter or power analyzer, checking that all three phases are present, balanced, and free of large transients.
7. **Review drive parameters** for correct motor nameplate data, acceleration times, and overcurrent trip thresholds; reset to factory defaults if uncertain, then re-enter motor data.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IGBT Power Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-02-fault-code&k=IGBT+Power+Module&tag=errorcodefixes-20) \| Only replace if insulation tests pass and the drive faults with no load connected; consult Yaskawa for the exact module part number for your frame size. |
| Control PCB Assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-02-fault-code&k=Control+PCB+Assembly&tag=errorcodefixes-20) \| Required if the drive shows erratic behavior or faults persist after all external checks pass; verify firmware version compatibility. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to work with high-voltage three-phase equipment, if insulation testing or power-quality measurement is beyond your skill set, or if the drive continues to fault after all external checks pass. Ground-fault and overcurrent diagnostics often require specialized test gear and experience interpreting waveform data. Because incorrect wiring or parameter changes can destroy expensive drive components or create a safety hazard, professional service is the best choice when the root cause is not obvious from visual inspection and basic continuity tests.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [Yaskawa VFD Fault OH — Causes & Fix](/posts/yaskawa-vfd-fault-oh/)
- [Yaskawa A1000 oFA34 Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-al-34-fault-code/)
- [Yaskawa GA800 VFD F0021 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-f0021-fault-code/)
- [Yaskawa A1000 CPF13 - Causes & Fix](/posts/yaskawa-a1000-vfd-cpf13-fault-code/)
