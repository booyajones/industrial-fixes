---
title: "Yaskawa A1000 VFD E31 Fault - Causes & Fix"
description: "E31 signals a ground fault or earth leak detected by the VFD. Check motor cables for damage and measure insulation resistance."
pubDatetime: 2026-07-23T07:27:49Z
modDatetime: 2026-07-23T07:27:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated motor cable"
most_likely_cause: "damaged or degraded motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect all motor cables for cuts, pinches, or abraded insulation"
  - "Check that the motor frame and drive chassis are properly grounded to earth"
  - "Disconnect the motor from the VFD output and see if the fault clears with no load"
part_price: "$150-600"
---

## Yaskawa A1000 VFD E31 Fault — What It Means

The E31 fault on a Yaskawa A1000 variable frequency drive indicates the drive has detected a ground fault or earth leakage current. This means current is flowing to ground somewhere in the motor circuit, motor windings, or output cabling, rather than staying within the intended power path. The drive protects itself and downstream equipment by shutting down when it senses this condition.

Ground faults can develop gradually as insulation deteriorates over time or appear suddenly after physical damage to cables or the motor. The fault may trigger immediately on startup or appear intermittently under load. The A1000's internal ground fault detection circuit monitors for imbalanced current flow and trips when the leakage exceeds the drive's threshold. Resolving this fault requires methodical inspection and testing of the entire motor circuit from the drive output terminals to the motor frame.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the fault actually originates in damaged motor cables or a failing motor. Always measure insulation resistance of the motor and cables with a megohmmeter before replacing the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~40%)** Physical damage, rodent chewing, pinching at conduit entry points, or UV degradation allows conductors to contact grounded surfaces or each other.
- **Motor winding insulation breakdown (~30%)** Heat, moisture, contamination, or age deteriorates the insulation between motor windings and the frame, allowing leakage current to ground.
- **Moisture or condensation in motor or cable (~15%)** Water ingress through damaged seals or condensation in a cold motor creates conductive paths to ground that trigger the fault.
- **Incorrect or missing grounding (~10%)** Improper grounding of the motor, drive, or shielded cable can create ground loops or stray current paths that the drive interprets as a fault.
- **Failed output transistor in the VFD (~5%)** A shorted IGBT or output stage component in the drive itself can create a false ground fault signal or actual leakage current.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the E31 fault clear when you disconnect the motor from the VFD output terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor or motor cables, not the drive. Proceed with cable and motor insulation testing.<br><strong>No:</strong> The fault is likely internal to the VFD or in the output stage. Professional drive repair or replacement is needed.</div>
</details>

<details class="dtree"><summary>Do you see any visible damage, oil, water, or worn insulation on the motor cables?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace or reroute the damaged cable section and retest. Even small nicks can cause ground faults at VFD voltage levels.<br><strong>No:</strong> The fault is likely in the motor windings or an intermittent cable issue. Proceed with megohmmeter testing.</div>
</details>

<details class="dtree"><summary>Does a megohmmeter show less than 1 megohm resistance from any motor lead to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor insulation has failed and the motor typically requires rewinding or replacement.<br><strong>No:</strong> Check for loose ground connections, shield grounding issues, or drive parameter settings related to ground fault sensitivity.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the VFD and motor circuit following all electrical safety procedures and wait for the drive's DC bus capacitors to discharge fully.
2. **Disconnect the motor cables** at the VFD output terminals (U, V, W) and tape or cap the loose motor leads so they cannot contact anything.
3. **Clear the fault** and attempt to power the drive without the motor connected to determine if the fault is in the drive or downstream.
4. **Inspect all motor cables** along their entire run for physical damage, tight bends, pinch points, moisture, oil contamination, or worn insulation.
5. **Measure insulation resistance** using a megohmmeter set to 500V or 1000V from each motor lead (U, V, W) to the motor frame and from lead to lead, recording all readings.
6. **Check motor and drive grounding** to verify the motor frame, drive chassis, and any cable shields are properly bonded to earth ground per code and the drive manual.
7. **Review drive parameters** related to ground fault detection sensitivity and trip threshold to make sure they match your motor and cable length per the manufacturer's recommendations.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e31-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use shielded, VFD-rated cable with the correct AWG for your motor and run length |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e31-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Match frame size, voltage, horsepower, and RPM to your application and the VFD rating |

## When to Call a Pro

Call a qualified electrician or VFD technician if you lack the test equipment to measure insulation resistance, if the fault persists with the motor disconnected (indicating an internal drive problem), or if you are uncomfortable working with three-phase power. Ground fault diagnosis requires a megohmmeter and knowledge of safe high-voltage testing procedures. Professionals can also analyze drive event logs, adjust ground fault parameters correctly, and determine whether a motor needs rewinding or replacement. If the motor or cables are in a hazardous location or the system is critical to production, professional diagnosis minimizes downtime and ensures code-compliant repairs.

**Rough cost:** A pro service call runs about $200-800.
