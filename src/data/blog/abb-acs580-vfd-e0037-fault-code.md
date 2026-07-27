---
title: "ABB ACS580 VFD E0037 Fault Code - Causes & Fix"
description: "E0037 indicates an output-phase error on the ACS580 drive. Check motor connections, cable routing, and load balance first."
pubDatetime: 2026-07-19T07:26:44Z
modDatetime: 2026-07-19T07:26:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Three-phase motor cable (shielded, rated for VFD duty)"
most_likely_cause: "Loose or corroded motor cable connection"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect motor cable terminations at both the drive and motor ends for tightness and corrosion"
  - "Check for visible damage or abraded insulation on the output cable run"
  - "Review drive parameter settings for output-phase loss sensitivity and motor nameplate match"
---

## ABB ACS580 VFD E0037 Fault Code — What It Means

The E0037 fault on an ABB ACS580 variable frequency drive typically signals an output-phase issue detected by the drive's monitoring system. The drive has sensed an imbalance or problem on one or more of the three output phases feeding the motor, which can mean a missing phase, excessive imbalance between phases, or a grounding fault in the output circuit.

This fault protects the drive and motor from damage due to single-phasing or asymmetric loading. The drive will shut down motor operation when the fault triggers. Because the exact threshold and detection logic vary by firmware and parameter settings, consult your model's manual for the precise definition and reset procedure.

## Before You Replace Anything

Technicians sometimes replace the drive's output module or IGBTs before checking basics. Measure cable continuity and insulation resistance at the motor terminal box and cable glands first; many E0037 faults trace to a corroded termination or damaged cable rather than a failed semiconductor.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded motor cable connection (~40%)** A high-resistance or intermittent contact at the drive output terminals or motor terminal box creates phase imbalance that the drive reads as an output fault.
- **Damaged output cable (~25%)** Physical damage, moisture intrusion, or insulation breakdown in one conductor causes a ground fault or opens a phase path.
- **Motor winding fault (~15%)** A shorted turn, winding-to-ground fault, or open winding inside the motor presents as an output imbalance to the drive.
- **Incorrect parameter configuration (~10%)** Mismatched motor nameplate data or overly sensitive phase-loss detection parameters can trigger nuisance faults under normal conditions.
- **Failed drive output stage (~7%)** A defective IGBT or gate driver in one phase of the inverter bridge prevents that phase from switching properly.
- **Mechanical overload or binding (~3%)** A jammed load or seized bearing causes excessive current draw on the motor, which may register as phase imbalance if one winding heats faster than the others.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear immediately on every start, or only after running for a while?</summary>
<div class="dtree-body"><strong>Yes:</strong> An immediate fault points to a wiring issue, parameter mismatch, or failed drive component; check terminations and parameter settings first.<br><strong>No:</strong> A delayed fault suggests thermal issues, intermittent connections, or a developing motor fault; monitor current balance and check for loose hardware.</div>
</details>

<details class="dtree"><summary>Are all three output phases present and balanced at the drive terminals with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive output stage is likely good; focus on the cable and motor for faults or imbalance.<br><strong>No:</strong> The drive itself may have a failed output module or gate driver; professional inverter diagnostics and repair are required.</div>
</details>

<details class="dtree"><summary>Does the motor spin freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is not the issue; concentrate on electrical connections and insulation tests.<br><strong>No:</strong> A binding load or seized bearing creates excessive current that can trigger phase-loss protection; address the mechanical fault first.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power sources to the drive and verify zero voltage at the input and output terminals with a meter.
2. **Inspect all motor cable terminations** at the drive output block and motor terminal box for tightness, corrosion, and signs of arcing or overheating.
3. **Perform insulation-resistance tests** on each motor cable conductor to ground and phase-to-phase using a megohmmeter rated for the system voltage.
4. **Check motor winding resistance** phase-to-phase at the motor terminal box; readings should be within a few percent of each other and match the motor's rated impedance.
5. **Review drive parameters** for motor nameplate data entries (voltage, current, frequency, power factor) and phase-loss sensitivity thresholds.
6. **Clear the fault** from the drive panel or keypad and attempt a slow-speed test run while monitoring output current on all three phases with a clamp meter.
7. **Replace damaged cable or repair motor windings** as indicated by test results, then retest under load and verify balanced current draw before returning to service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase motor cable (shielded, rated for VFD duty) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0037-fault-code&k=Three-phase+motor+cable+%28shielded%2C+rated+for+VFD+duty%29&tag=errorcodefixes-20) \| Match gauge and insulation rating to drive output voltage and motor nameplate current |
| Motor terminal-block assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0037-fault-code&k=Motor+terminal-block+assembly&tag=errorcodefixes-20) \| Needed if corrosion or arcing has damaged the existing terminals inside the motor junction box |

## When to Call a Pro

Call a qualified electrician or drive technician if you lack test equipment (megohmmeter, phase-rotation tester, oscilloscope), if insulation tests reveal a motor winding fault that requires rewind or replacement, or if the drive continues to fault after confirming all external wiring and parameters are correct. Drive output-stage repair involves high-voltage DC bus capacitors and static-sensitive power semiconductors that require factory training and specialized tools. Professional diagnosis can also distinguish between a nuisance fault caused by parameter tuning and a genuine hardware failure, saving time and avoiding unnecessary parts replacement.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [ABB ACS880 Fault 2310 - Overcurrent Diagnosis and Fix](/posts/abb-acs880-fault-2310/)
- [ABB ACS580 Fault 2330 Earth Leakage, Causes & Fix](/posts/abb-acs580-fault-2330/)
- [ABB ACS580 VFD E0018 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0018-fault-code/)
- [ABB ACS580 B1 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-b1-fault-code/)
