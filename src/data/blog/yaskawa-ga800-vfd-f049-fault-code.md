---
title: "Yaskawa GA800 Er-04 Fault - Causes & Fix"
description: "Er-04 on a Yaskawa GA800 means line-to-line motor resistance is out of range during auto-tuning. Fix wiring and connections first."
pubDatetime: 2026-06-28T10:15:50Z
modDatetime: 2026-06-28T10:15:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Three-phase AC induction motor"
most_likely_cause: "poor or damaged motor wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all motor terminal connections for tightness, corrosion, or visible damage"
  - "Check motor cable for cuts, pinches, or insulation damage along the entire run"
  - "Verify encoder coupling is tight and free of mechanical obstruction or slippage"
---

## Yaskawa GA800 Er-04 Fault — What It Means

The Er-04 (Line-to-Line Resistance Error) fault on a Yaskawa GA800 drive means the auto-tuning process calculated a line-to-line motor resistance value that falls outside the acceptable parameter range defined by the drive firmware. This indicates the drive cannot reliably determine the motor's electrical characteristics for proper torque and speed control.

Note: The GA800 does not use an F049 fault code. F049 is associated with Siemens drives, not Yaskawa. The Er-04 code is the correct Yaskawa GA800 fault for resistance issues during auto-tuning.

## Before You Replace Anything

Technicians sometimes replace the motor when the real problem is loose or corroded connections at the motor terminals. Always perform a megger test on motor windings and check all wiring continuity before condemning the motor.

[Jump to Fix](#fix)

## Common Causes

- **Poor or damaged motor wiring (~40%)** Loose connections, broken conductors, or corroded terminals prevent accurate resistance measurement during auto-tuning.
- **Motor ground fault or insulation breakdown (~25%)** A megger test will reveal if motor windings have developed a ground fault or low insulation resistance.
- **Incorrect motor type or size (~15%)** Using a motor with resistance too high or too low for the drive's expected range causes the auto-tune to fail.
- **Encoder or coupling misalignment (~10%)** Slippage in the encoder coupling or misaligned gearbox creates erratic feedback during the auto-tune process.
- **DC bus interference from other loads (~10%)** Other equipment connected to the DC bus can distort voltage and affect tuning accuracy.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all motor terminal connections tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is likely good. Proceed to megger test the motor windings for insulation integrity.<br><strong>No:</strong> Clean and tighten all terminals, repair any damaged cable, then re-run auto-tuning.</div>
</details>

<details class="dtree"><summary>Does the motor pass a megger test (insulation resistance above 1 megohm)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation is good. Check encoder coupling and mechanical alignment next.<br><strong>No:</strong> Motor has a ground fault or insulation breakdown. Replace the motor.</div>
</details>

<details class="dtree"><summary>Is the encoder coupling tight and does the shaft rotate freely by hand?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical setup is good. Review motor parameter settings and verify correct motor type for the drive.<br><strong>No:</strong> Tighten or replace the encoder coupling, clear any mechanical obstruction, then re-run auto-tuning.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Examine all motor wiring** from drive to motor terminals and check every connection for tightness, continuity, and insulation integrity.
2. **Disconnect the motor from the drive** and isolate it to perform rotational auto-tuning without machine load interference.
3. **Perform a megger test** on motor leads and motor windings to detect ground faults or insulation breakdown (consult your model's table for acceptable resistance values).
4. **Verify encoder and couplings** by ensuring the encoder coupling is tightly secured, shows no slippage, and all mechanical components rotate freely without obstruction.
5. **Check for DC bus interference** by confirming no other loads are connected to the DC bus that could distort the tuning process.
6. **Review motor parameter settings** and compare tuned parameters with those from a known-good identical motor if available.
7. **Re-run rotational auto-tune** with the motor isolated, properly connected, and grounding system configured per Yaskawa specifications.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase AC induction motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f049-fault-code&k=Three-phase+AC+induction+motor&tag=errorcodefixes-20) \| Only if megger test confirms ground fault or insulation breakdown. |
| Rotary encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f049-fault-code&k=Rotary+encoder&tag=errorcodefixes-20) \| Only if coupling slippage or feedback inconsistency is confirmed. |
| Motor coupling or gearbox | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f049-fault-code&k=Motor+coupling+or+gearbox&tag=errorcodefixes-20) \| Only if mechanical misalignment or obstruction is found during inspection. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician for all GA800 fault diagnosis and repair. This work requires understanding of three-phase power systems, motor parameter tuning, and high-voltage safety protocols. If you are not trained in VFD commissioning and motor testing (including megger tests and auto-tuning procedures), do not attempt the repair. Contact Yaskawa Technical Support at repair@yaskawa.com or 1.800.927.5292 for assistance, and consult the GA800 Maintenance & Troubleshooting Manual (TOEPYAIGA8001) for exact firmware limits and parameter ranges.

**Rough cost:** A pro service call runs about $200-500 depending on motor size and labor.
