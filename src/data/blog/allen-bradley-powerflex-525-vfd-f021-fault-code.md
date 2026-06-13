---
title: "Allen-Bradley PowerFlex 525 F021 - Causes & Fix"
description: "F021 means Output Phase Loss on the PowerFlex 525 VFD. Most often caused by a loose or damaged motor lead between drive and motor."
pubDatetime: 2026-06-11T10:20:03Z
modDatetime: 2026-06-11T10:20:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor output cable"
most_likely_cause: "loose, open, or damaged motor lead between the drive and motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## Allen-Bradley PowerFlex 525 F021 — What It Means

F021 on an Allen-Bradley PowerFlex 525 means Output Phase Loss. The drive has detected loss of one output phase to the motor. This fault only appears when output phase-loss protection is enabled in parameter A557 (Output Phas Loss En). The drive is telling you it cannot see all three phases at the motor terminals, which points to a break or open circuit somewhere between the drive output and the motor windings.

The fault protects the motor from running unbalanced, which would overheat and damage the windings. When F021 trips, the drive shuts down to prevent harm. The problem lies in the physical connection path or the motor itself, not in the drive logic or programming.

## Before You Replace Anything

Technicians sometimes replace the PowerFlex 525 drive before checking all motor wiring terminations and testing motor winding continuity with a meter. A simple resistance check across all three motor leads usually finds the open phase and saves the cost of a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Loose, open, or damaged motor lead (~50%)** A broken conductor, loose termination, or physically damaged cable between the drive output terminals and the motor creates an open phase that triggers F021.
- **Bad output connection at drive or motor terminals (~25%)** Heat damage, corrosion, or vibration can loosen a terminal screw at the PowerFlex 525 output or at the motor junction box, opening one phase.
- **Motor winding failure (~15%)** An open winding inside the motor from thermal overload, insulation breakdown, or mechanical stress makes one phase appear missing to the drive.
- **Intermittent wiring under vibration (~10%)** A wire that makes contact when still but opens under machine vibration or thermal cycling will cause F021 to appear and disappear unpredictably.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>With power off and locked out, do all three motor leads show continuity from drive output terminals to motor terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is intact so the motor windings are suspect. Measure resistance across each pair of motor leads at the motor junction box to find an open or high-resistance winding.<br><strong>No:</strong> You have an open or damaged cable. Inspect the entire run for physical damage, broken strands, or loose terminations and repair or replace the cable.</div>
</details>

<details class="dtree"><summary>Are all terminal screws at the drive output and motor junction box tight and free of burn marks?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connections are good so check the cable itself for internal breaks or the motor for a winding fault.<br><strong>No:</strong> Tighten loose terminals or replace burned terminal hardware and retest. Heat damage means the connection has been arcing and must be remade.</div>
</details>

<details class="dtree"><summary>Does the fault appear in the drive's fault history repeatedly or only once?</summary>
<div class="dtree-body"><strong>Yes:</strong> A recurring fault points to an intermittent connection under vibration or thermal cycling. Inspect flex conduit, cable entry points, and any terminal that moves during operation.<br><strong>No:</strong> A one-time fault may have been a transient event. Clear the fault and monitor the drive under normal load before replacing parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Stop and lock out power** at the main disconnect before touching any wiring, then wait for the drive DC bus to discharge per the PowerFlex 525 manual.
2. **Inspect all motor cable terminations** at the drive output terminals (T1, T2, T3) and at the motor junction box for loose screws, heat discoloration, or physical damage.
3. **Check motor cable continuity** from the drive output to the motor with a multimeter in resistance mode to confirm all three phases are electrically continuous.
4. **Measure motor winding resistance** across each pair of motor leads (T1-T2, T2-T3, T3-T1) at the motor junction box to verify balanced windings and no open phase.
5. **Verify parameter A557 (Output Phas Loss En)** is enabled in the drive, since F021 only triggers when this protection is active.
6. **Clear the fault** using the drive keypad and run the motor under no load, then under normal load, watching for the fault to return.
7. **Replace the drive** if wiring and motor test good, all connections are tight, and F021 persists after clearing, because the drive output stage may be faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f021-fault-code&k=Motor+output+cable&tag=errorcodefixes-20) \| Use shielded 3-conductor cable rated for VFD service if the original is damaged or shows broken strands. |
| Motor terminal hardware | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f021-fault-code&k=Motor+terminal+hardware&tag=errorcodefixes-20) \| Replace burned or corroded terminal lugs and screws at the motor junction box if heat damage is present. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f021-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| Only if winding resistance tests show an open or severely unbalanced phase. |
| PowerFlex 525 drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f021-fault-code&k=PowerFlex+525+drive&tag=errorcodefixes-20) \| Replace only after confirming wiring and motor are good and the fault cannot be cleared. |

## When to Call a Pro

Call a qualified electrician or industrial technician for F021. The repair requires working on three-phase VFD output wiring, which carries high voltage and high-frequency switching transients that can cause shock or arc flash. The technician will need a multimeter to verify continuity and balance across motor windings, knowledge of VFD parameter settings to check A557, and the ability to safely lock out and test under load. If the motor or drive must be replaced, a professional ensures proper grounding, cable routing, and parameter re-entry so the new equipment runs reliably without nuisance faults.

**Rough cost:** A pro service call runs about $150-500.
