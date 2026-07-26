---
title: "Yaskawa A1000 VFD E68 Fault - Causes & Fix"
description: "E68 indicates a ground fault detected in the motor circuit. Most often caused by damaged motor cable insulation or a grounded motor."
pubDatetime: 2026-07-24T07:38:51Z
modDatetime: 2026-07-24T07:38:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 VFD output module or drive assembly"
most_likely_cause: "damaged motor cable insulation or moisture in the motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for cuts, pinches, or worn insulation"
  - "Check for moisture or condensation inside the motor junction box"
  - "Verify all terminations are tight and free of carbon tracking or burn marks"
---

## Yaskawa A1000 VFD E68 Fault — What It Means

The E68 fault on a Yaskawa A1000 variable frequency drive signals that the VFD has detected a ground fault in the motor circuit. This means current is leaking to earth ground somewhere between the drive output and the motor, typically through damaged insulation. The drive shuts down to protect itself and the motor from further damage.

Ground faults can occur in the motor windings, in the motor cable, at termination points, or inside the drive itself. The A1000 monitors leakage current and trips when it exceeds the threshold set in the drive parameters. Moisture, contamination, physical damage, or age-related insulation breakdown are common contributors.

## Before You Replace Anything

Many technicians replace the VFD or motor without first testing cable insulation. Use a megohmmeter to test cable and motor winding resistance to ground before replacing expensive components.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~35%)** Physical damage, abrasion, or age-related deterioration allows current to leak from conductors to the cable shield or conduit.
- **Motor winding insulation failure (~30%)** Moisture ingress, thermal cycling, or contamination breaks down winding insulation and creates a path to the motor frame.
- **Moisture in the motor or junction box (~15%)** Condensation or water intrusion provides a conductive path from windings or terminals to ground.
- **Loose or corroded terminations (~10%)** Poor connections at the motor or drive can cause arcing and carbon tracking that creates a ground path.
- **Incorrect drive ground-fault sensitivity setting (~5%)** The drive parameter for ground-fault detection may be set too low for the application, causing nuisance trips.
- **Failed drive output transistors or internal fault (~5%)** A shorted IGBT or internal ground fault inside the VFD itself triggers the ground-fault protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear when you disconnect the motor cable from the drive output terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor cable or motor. Megger-test the cable and motor separately to find the grounded component.<br><strong>No:</strong> The fault is likely inside the drive or at the drive output stage. Inspect the drive output terminals and consider a drive output module failure.</div>
</details>

<details class="dtree"><summary>Is the motor located in a wet, humid, or outdoor environment?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check for moisture in the motor and junction box. Dry thoroughly and retest. Consider installing a space heater or drain to prevent future moisture buildup.<br><strong>No:</strong> Focus on mechanical damage to the cable or motor windings. Inspect the cable route for pinch points or sharp edges.</div>
</details>

<details class="dtree"><summary>Does a megohmmeter test show low resistance (under 1 megohm) from any motor lead to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor winding insulation has failed. Replace the motor or rewind it if economical.<br><strong>No:</strong> Check the motor cable insulation and all termination points. Look for carbon tracking or intermittent faults that appear under load.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive and motor circuit following all electrical safety procedures.
2. **Disconnect the motor cable** from the drive output terminals (U, V, W) to isolate the motor circuit from the drive.
3. **Clear the fault** on the drive and attempt to reset. If the E68 persists with the motor disconnected, the fault is inside the drive and requires factory service or replacement.
4. **Megger-test the motor cable** by measuring insulation resistance between each conductor and ground, and between conductors. A reading below 1 megohm suggests damaged insulation.
5. **Test motor winding insulation** with a megohmmeter from each winding lead to the motor frame. Disconnect any accessories (brakes, encoders) that may provide alternate ground paths.
6. **Inspect all termination points** at the motor junction box and drive output for signs of arcing, carbon tracking, moisture, or loose hardware. Clean and tighten as needed.
7. **Dry the motor** if moisture is present. Use low heat or compressed air, and allow adequate time before re-energizing. Consider sealing entry points or adding a drain plug.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 VFD output module or drive assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e68-fault-code&k=Yaskawa+A1000+VFD+output+module+or+drive+assembly&tag=errorcodefixes-20) \| Required only if internal fault confirmed; consult factory service for exact module number matching your drive horsepower and voltage. |
| Three-phase motor cable (VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e68-fault-code&k=Three-phase+motor+cable+%28VFD-rated%29&tag=errorcodefixes-20) \| Use cable rated for inverter duty with proper shielding; length and gauge depend on motor size and distance. |
| Replacement motor matching original specifications | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e68-fault-code&k=Replacement+motor+matching+original+specifications&tag=errorcodefixes-20) \| If winding insulation has failed beyond repair; verify voltage, horsepower, frame size, and mounting before ordering. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage electrical work or do not have access to a megohmmeter. Ground-fault troubleshooting requires de-energizing circuits, lockout-tagout procedures, and insulation resistance testing that can damage equipment if performed incorrectly. If the fault persists after you have confirmed good motor and cable insulation, the drive may have an internal failure that requires factory-trained service or return to Yaskawa. Do not attempt to open or repair the drive power section without manufacturer authorization, as high-voltage capacitors remain charged even after power is removed.

**Rough cost:** A pro service call runs about $200-800.
