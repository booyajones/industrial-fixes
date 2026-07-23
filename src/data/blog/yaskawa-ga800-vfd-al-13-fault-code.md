---
title: "Yaskawa GA800 VFD AL-13 Fault - Causes & Fix"
description: "AL-13 signals a ground fault in the VFD output circuit. Check motor cable insulation and motor windings for shorts to ground."
pubDatetime: 2026-07-21T07:35:19Z
modDatetime: 2026-07-21T07:35:19Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "damaged motor cable insulation or moisture in motor junction box"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for cuts, abrasion, or pinch points along the entire run"
  - "Check motor junction box for moisture, corrosion, or loose terminal connections"
  - "Disconnect motor leads at the drive and attempt to run the drive unloaded to see if the fault clears"
---

## Yaskawa GA800 VFD AL-13 Fault — What It Means

The AL-13 fault code on a Yaskawa GA800 variable frequency drive indicates a ground fault has been detected in the output circuit. The drive has sensed an imbalance in current that suggests insulation breakdown or a short circuit path between the motor windings or output cables and ground. This protection feature shuts down the drive to prevent damage to the inverter output stage and connected equipment.

The fault typically occurs when the drive detects current leaking to the equipment grounding conductor rather than flowing through the intended motor circuit. This can happen in the motor cable, at termination points, inside the motor itself, or at any junction where insulation has failed. The drive compares outgoing and return currents and trips when the difference exceeds its internal threshold.

## Before You Replace Anything

Technicians sometimes replace the VFD itself when the fault actually originates in the motor or cable. Always measure insulation resistance of the motor and cable to ground with a megohmmeter before condemning the drive.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~35%)** Physical damage to the VFD output cable from abrasion, crushing, or improper installation allows conductors to contact grounded conduit or metal surfaces.
- **Motor winding insulation failure (~30%)** Internal breakdown of motor winding insulation due to age, overheating, contamination, or moisture creates a path to the motor frame.
- **Moisture in motor junction box (~15%)** Water intrusion into the motor terminal box provides a conductive path between live terminals and the grounded enclosure.
- **Loose or corroded motor connections (~10%)** Poor terminations at the motor or drive allow arcing or tracking that the ground fault detection circuit interprets as a fault condition.
- **Excessive motor cable length or capacitance (~5%)** Very long motor cable runs generate charging current that can be misinterpreted as a ground fault by the drive's protection circuits.
- **Failed VFD output stage (~5%)** Internal failure of the drive's IGBT output transistors or gate drivers can create a fault condition that registers as a ground fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear when you disconnect the motor leads at the drive and attempt to run?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor cable or motor itself. Proceed with insulation testing of the cable and motor windings.<br><strong>No:</strong> The fault is internal to the VFD. Check for damaged output components or a faulty ground fault detection circuit board.</div>
</details>

<details class="dtree"><summary>Does a megohmmeter test show motor winding insulation resistance above 2 megohms to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor windings are likely intact. Focus on the cable, terminations, and connections between the drive and motor.<br><strong>No:</strong> The motor has failed insulation and needs repair or replacement. This is the source of the ground fault.</div>
</details>

<details class="dtree"><summary>Is the motor cable routed through wet or contaminated areas, or does it share conduit with other high-voltage circuits?</summary>
<div class="dtree-body"><strong>Yes:</strong> Moisture or electromagnetic interference may be contributing to the fault. Reroute the cable in dedicated dry conduit and retest.<br><strong>No:</strong> The cable routing is acceptable. Perform point-by-point inspection and insulation testing of the cable itself.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD at the upstream disconnect or breaker and verify zero voltage with a multimeter at the drive input terminals.
2. **Document the fault** by noting the exact fault code displayed and any recent changes to the system, such as motor replacement, cable modifications, or environmental conditions.
3. **Disconnect the motor leads** at the VFD output terminals (U, V, W) and label them for reconnection.
4. **Measure insulation resistance** of the motor cable using a megohmmeter (500 V DC test setting). Test each conductor to ground and conductor-to-conductor. Readings below 2 megohms indicate insulation breakdown.
5. **Test the motor windings** by placing the megohmmeter probes on motor terminals and the motor frame. Again, readings below 2 megohms suggest motor winding failure.
6. **Inspect all termination points** at the drive, any junction boxes, and the motor for loose connections, corrosion, moisture, or tracking marks that indicate arcing.
7. **Replace damaged cable or motor** if testing reveals insulation failure. Use cable rated for VFD service (shielded or armored) and follow manufacturer recommendations for maximum length and conduit fill.
8. **Reconnect the repaired system** and restore power. Clear the fault from the VFD control panel according to the drive manual and test run the motor under no-load conditions before returning to full operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-13-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for inverter duty with appropriate insulation and shielding to minimize ground faults and EMI. |
| Motor terminal lugs and heat-shrink insulation | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-13-fault-code&k=Motor+terminal+lugs+and+heat-shrink+insulation&tag=errorcodefixes-20) \| Replace corroded or damaged terminations with proper compression lugs and insulating sleeves rated for the voltage and environment. |

## When to Call a Pro

Ground fault diagnosis on VFD systems requires specialized test equipment (megohmmeter, clamp-on ground leakage meter) and knowledge of high-voltage DC circuits. If you are not trained in industrial electrical work or do not have access to insulation testing tools, call a qualified electrician or motor technician. Work on energized VFD circuits can be lethal, and improper repairs can damage expensive drive components. A professional will systematically isolate the fault, perform insulation resistance measurements, and make sure all grounding and bonding meets code requirements before returning the system to service.

**Rough cost:** A pro service call runs about $200-800.
