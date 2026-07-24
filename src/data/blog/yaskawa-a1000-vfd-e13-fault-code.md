---
title: "Yaskawa A1000 VFD E13 Fault - Causes & Fix"
description: "E13 indicates a ground fault or output phase loss on the Yaskawa A1000 VFD. Check motor cable insulation and connections first."
pubDatetime: 2026-07-22T07:40:40Z
modDatetime: 2026-07-22T07:40:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Shielded VFD-rated motor cable"
most_likely_cause: "damaged motor cable insulation or loose output connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all motor cable connections at the drive output terminals and motor terminal box for looseness or corrosion"
  - "Look for visible damage, cuts, or moisture on the motor cable jacket and conduit seals"
---

## Yaskawa A1000 VFD E13 Fault — What It Means

The E13 fault code on a Yaskawa A1000 variable frequency drive typically signals a ground fault condition or an output phase loss between the drive and the motor. This means the drive has detected current leaking to ground through damaged insulation, or one of the three output phases feeding the motor has been interrupted or lost continuity. The drive shuts down to protect itself and the motor from damage.

Because the exact definition can vary slightly between firmware versions and application settings, always consult your drive's manual and the parameter list for your specific model. Ground faults are often caused by moisture, worn cable jackets, or contamination inside the motor. Phase loss can result from loose terminals, broken conductors, or failed contactors in the output circuit.

## Before You Replace Anything

Technicians sometimes replace the output power module or entire drive when the real problem is a damaged motor cable or moisture in a junction box. Use a megohmmeter to test cable insulation to ground and phase-to-phase resistance before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~40%)** Worn, pinched, or moisture-damaged cable insulation allows current to leak to ground and trip the fault.
- **Loose or corroded output terminals (~25%)** Poor contact at the drive output or motor terminal box creates intermittent phase loss or high resistance that the drive reads as a fault.
- **Motor winding insulation failure (~20%)** Internal motor insulation breakdown from age, heat, or moisture creates a path to ground inside the motor frame.
- **Moisture in motor or junction box (~10%)** Water ingress into the motor housing or a conduit junction box provides a conductive path that triggers the ground fault detection.
- **Failed output contactor or relay (~5%)** An external contactor between the drive and motor with burned or welded contacts can drop a phase and cause the fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all three output terminals tight and free of corrosion at both the drive and motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connections are good. Proceed to test cable and motor insulation with a megohmmeter.<br><strong>No:</strong> Clean and retighten all output terminals. Reset the fault and test run the drive.</div>
</details>

<details class="dtree"><summary>Does the motor cable show any visible damage, cuts, or moisture?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the damaged section of cable or the entire run. make sure conduit seals are intact.<br><strong>No:</strong> The cable jacket looks intact. Use an insulation resistance tester to check for internal breakdown.</div>
</details>

<details class="dtree"><summary>Does a megohmmeter test show low insulation resistance (below 1 megohm) from any motor lead to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or cable insulation has failed. Isolate the motor and test the cable alone to determine which component is at fault.<br><strong>No:</strong> Insulation is acceptable. Check for loose connections, failed contactors, or incorrect drive parameter settings.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and lock out the main disconnect. Wait for the DC bus capacitors to discharge (typically five minutes or per the label on the drive).
2. **Inspect all output connections** at the drive U, V, W terminals and at the motor terminal box. Look for loose hardware, burned terminals, or signs of arcing.
3. **Examine the motor cable** along its entire run for cuts, abrasion, tight bends, or moisture. Check conduit seals and junction box covers.
4. **Perform a megohmmeter test** on the motor cable. Disconnect the cable at both ends and test insulation resistance from each conductor to ground and between conductors. Readings below 1 megohm indicate insulation failure.
5. **Test the motor windings** separately by disconnecting the cable at the motor and testing each winding to the motor frame. Low readings point to motor insulation breakdown.
6. **Check any external contactors or relays** in the output circuit. Verify that all three poles close properly and that contacts are not burned or pitted.
7. **Clear the fault** from the drive keypad or by cycling power. Review the drive's fault history and parameter settings to confirm ground fault detection is enabled and set correctly for your application.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e13-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive service with proper grounding and shielding for the distance and voltage of your installation. |
| Three-phase motor (matching frame and horsepower) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e13-fault-code&k=Three-phase+motor+%28matching+frame+and+horsepower%29&tag=errorcodefixes-20) \| Required only if megohmmeter testing confirms internal winding insulation has failed and cannot be repaired. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained to work safely around high-voltage DC bus capacitors or if you lack an insulation resistance tester. Ground fault diagnosis requires megohmmeters and an understanding of drive output circuits. If the motor or cable tests good but the fault persists, the drive's output power module or internal ground fault detection circuit may have failed, and factory-trained service is needed to replace internal components or adjust advanced parameters.

**Rough cost:** A pro service call runs about $200-600.
