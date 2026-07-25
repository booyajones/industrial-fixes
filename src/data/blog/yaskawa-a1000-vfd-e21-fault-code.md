---
title: "Yaskawa A1000 VFD E21 Fault - Causes & Fix"
description: "E21 indicates a ground fault or insulation breakdown. Most often caused by damaged motor cable insulation or motor winding fault."
pubDatetime: 2026-07-23T07:21:08Z
modDatetime: 2026-07-23T07:21:08Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated motor cable"
most_likely_cause: "Damaged motor cable insulation or contaminated motor windings"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for pinched, cut, or abraded insulation along the entire run"
  - "Check motor terminal box for moisture, oil contamination, or loose strands touching ground"
  - "Disconnect motor leads at the drive and run the drive unloaded to see if the fault clears"
---

## Yaskawa A1000 VFD E21 Fault — What It Means

The E21 fault code on a Yaskawa A1000 variable frequency drive signals a ground fault detection. The drive has detected current leaking to ground, either in the motor cable or in the motor windings themselves. This protective fault prevents the drive from running to avoid damage to the equipment or electrical hazards. Ground faults typically occur when insulation has broken down, allowing current to flow where it should not.

The drive continuously monitors for imbalance between the outgoing and returning current paths. When the sum of the three phase currents does not equal zero within the drive's tolerance, the drive interprets this as leakage to ground and trips the E21 fault. This fault will not reset until the underlying ground fault is repaired or removed from the circuit.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the fault is actually in the motor cable or motor windings. Always megger-test the motor and cable insulation to ground before replacing the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~40%)** Pinched, abraded, or cut cable jacket allows phase conductors to contact ground or conduit.
- **Motor winding insulation failure (~30%)** Contamination, moisture, age, or thermal stress breaks down winding insulation, creating a path to the motor frame.
- **Moisture or contamination in motor terminal box (~15%)** Water, oil, or conductive dust creates a low-resistance path from motor leads to the grounded frame.
- **Incorrect drive parameter settings (~10%)** Ground fault sensitivity set too high or improper carrier frequency can cause nuisance tripping on long motor cables.
- **Failed ground fault detection circuitry in drive (~5%)** Internal drive board failure causes false ground fault detection even when no actual fault exists.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the E21 fault clear when you disconnect all three motor leads at the drive output terminals and reset the fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor cable or motor itself, not the drive. Proceed with insulation resistance testing of the motor and cable.<br><strong>No:</strong> The fault is likely internal to the drive or a wiring issue between the drive and ground. Inspect drive output terminals and internal components or call a technician.</div>
</details>

<details class="dtree"><summary>When you megger-test the motor windings to ground (with cable disconnected), do you read greater than 1 megohm at 500 VDC?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation is acceptable. Test the motor cable separately for insulation breakdown between conductors and ground or along the cable run.<br><strong>No:</strong> Motor winding insulation has failed. The motor needs cleaning, drying, or rewinding, or replacement depending on contamination and damage.</div>
</details>

<details class="dtree"><summary>Is the motor cable routed through areas with moving machinery, sharp edges, or high heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Inspect the cable very carefully for physical damage. Replace cable if jacket or insulation is compromised, and reroute to prevent future damage.<br><strong>No:</strong> Check the motor terminal box for moisture, dirt, or oil buildup that may be creating a leakage path to ground.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD at the main disconnect and verify zero voltage with a multimeter at input and output terminals.
2. **Disconnect the motor leads** at the drive output terminals (U, V, W) and cap or isolate them safely.
3. **Reset the fault** on the drive keypad and attempt to run the drive without a load connected to verify if the fault is downstream.
4. **Perform insulation resistance testing** using a megohmmeter set to 500 VDC, testing each motor phase to ground and phase-to-phase with the cable disconnected from the motor.
5. **Inspect the motor cable** along its entire length for physical damage, pinch points, abrasion, or entry into conduit with sharp edges.
6. **Open the motor terminal box** and check for moisture, oil, metallic debris, or loose wire strands that could bridge to the frame.
7. **Consult the drive manual** to verify ground fault sensitivity parameters are set appropriately for your motor cable length and application.
8. **Replace damaged cable or repair motor** as indicated by test results, then reconnect and test the system under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e21-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Shielded, stranded copper cable rated for inverter duty; match gauge and length to your motor and application |
| Yaskawa A1000 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e21-fault-code&k=Yaskawa+A1000+control+board&tag=errorcodefixes-20) \| Only if internal drive fault is confirmed by eliminating all external causes and testing by qualified technician |

## When to Call a Pro

Call a qualified electrician or motor technician if you are not trained to work with high-voltage three-phase equipment, do not own a megohmmeter or know how to interpret insulation resistance readings, or if initial free checks do not isolate the fault. Ground fault diagnosis requires systematic electrical testing and safe handling of motor circuits. If the motor winding insulation has failed, repair or replacement involves disassembly and may require a motor shop. If the drive itself has failed internally after confirming no external faults, only a technician familiar with VFD repair should handle board-level diagnostics and replacement.

**Rough cost:** A pro service call runs about $200-800.
