---
title: "ABB ACS580 A2A4/A2B4 Fault - Causes & Fix"
description: "A2A4/A2B4 fault means short circuit detected in motor cable or motor windings. Most often caused by damaged cable insulation."
pubDatetime: 2026-06-21T10:34:23Z
modDatetime: 2026-06-21T10:34:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "VFD-rated shielded motor cable"
most_likely_cause: "damaged motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for physical damage, abrasion, or rodent chewing along the entire run"
  - "Check motor terminal box and drive output terminals for loose wires touching adjacent contacts or frame"
part_price: "$150-400 for replacement motor cable depending on gauge and length"
---

## ABB ACS580 A2A4/A2B4 Fault — What It Means

The ABB ACS580 variable frequency drive has detected a short circuit in the motor cable or motor itself. The drive's output stage sensed a direct low-resistance path between phases or between a phase and ground, exceeding the safe current limit. This is a critical protection event that immediately shuts down the drive to prevent damage to the internal power transistors (IGBTs). The official ABB fault list shows this code as A2B4 with the description "Short circuit: Short-circuit in motor cable(s) or motor," though it may appear as A2A4 on some displays depending on the specific sub-code or hex digit reading.

The drive will not restart until the short circuit is cleared and the fault is reset. This fault is distinct from ground faults or overload conditions. It indicates a physical failure in the insulation system of either the motor cable or the motor windings, creating a direct connection between conductors that should be isolated.

## Before You Replace Anything

Technicians sometimes replace the drive itself without testing the motor and cables first. Always use a megohmmeter to test cable and motor insulation resistance before condemning the VFD output stage.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation (~45%)** Physical abrasion, rodent damage, water intrusion, or pinched cable causes conductors to touch each other or ground.
- **Shorted motor windings (~30%)** Burnt or damaged windings inside the motor create a short between phases or to the motor frame.
- **Loose or incorrect wiring connections (~15%)** Terminal screws not tightened properly allow wires to touch adjacent phases or ground at the drive or motor terminal box.
- **Ground fault in motor or cable (~8%)** A phase conductor contacting the motor frame or cable conduit creates a ground fault the drive reads as a short circuit.
- **Failed drive output stage (~2%)** Internal IGBT transistors shorted due to prior overvoltage or current event, causing immediate fault even with no motor connected.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately when you power up the drive with the motor cables disconnected from the output terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive's internal output transistors are shorted. The drive needs repair or replacement.<br><strong>No:</strong> The short is in the motor cable or motor. Proceed to test the cable and motor insulation.</div>
</details>

<details class="dtree"><summary>With a megohmmeter, does the motor cable measure greater than 1 MΩ resistance between all phases and between each phase and ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is good. The short is likely in the motor windings. Test the motor next.<br><strong>No:</strong> The cable insulation has failed. Replace the motor cable and retest.</div>
</details>

<details class="dtree"><summary>Does the motor measure greater than 1 MΩ resistance from each phase to ground and show balanced phase-to-phase resistance?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor windings are good. Recheck all terminal connections for loose wires or debris causing intermittent shorts.<br><strong>No:</strong> Motor windings are shorted. The motor needs repair or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lockout** the drive at the main disconnect, wait 5 to 10 minutes for output capacitors to discharge, then verify zero voltage with a multimeter.
2. **Disconnect the motor cables** (U, V, W) from the drive's output terminals and inspect the terminals for loose strands or debris.
3. **Test the drive alone** by powering it up without the motor cables connected. If the A2B4 fault trips immediately with no load, the drive's internal output stage is shorted and the drive needs repair or replacement.
4. **Measure cable insulation** using a megohmmeter set to 500 V or 1000 V. Test resistance between each phase pair (U-V, V-W, W-U) and between each phase and ground (U-G, V-G, W-G). Resistance should be greater than 1 MΩ. If any reading shows less than 0.5 MΩ or continuity (near 0 Ω), replace the motor cable.
5. **Measure motor winding insulation** at the motor terminal box. Check phase-to-phase resistance (should be nearly equal within 1 to 2 percent) and phase-to-ground resistance (should be greater than 1 MΩ). If one phase-to-phase shows near 0 Ω or any phase-to-ground shows continuity, the motor windings are shorted and the motor needs repair or replacement.
6. **Inspect all connections** in the motor terminal box, drive output terminals, and any junction boxes for loose wires, crossed phases, or physical contact between conductors.
7. **Reconnect and test** after replacing the faulty cable or motor. Reset the fault from the drive keypad and perform a no-load test, then gradually increase load to verify the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a4-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Match the wire gauge to your motor's full-load amperage and consult your model's table for maximum cable length to avoid voltage reflection issues. |
| Three-phase induction motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2a4-fault-code&k=Three-phase+induction+motor&tag=errorcodefixes-20) \| Match voltage, horsepower, frame size, and mounting to the original motor nameplate. |

## When to Call a Pro

Call a licensed electrician or motor technician for this repair. The fault involves high-voltage output circuits and requires a megohmmeter (insulation tester) to safely diagnose. Incorrect testing can damage the drive or create a shock hazard. If the motor windings are shorted, rewinding or replacement requires specialized equipment and knowledge of three-phase motor construction. If the drive's internal output stage is shorted, the drive must be sent to an authorized ABB service center or replaced. Do not attempt to bypass safety interlocks or run the drive with a known short circuit, as this will cause catastrophic failure of the power transistors and create a fire risk.

**Rough cost:** A pro service call runs about $300-800 depending on whether cable or motor needs replacement.

## See Also

- [ABB ACH580 HVAC VFD Fault Codes — Full Diagnostic Guide - What It Means and How to Fix It](/posts/abb-ach580-fault-codes/)
- [ABB ACS550 AI1 LOSS - Causes & Fix](/posts/abb-acs550-ai1-loss-fault-code/)
- [ABB ACS550 F0001 Fault — Causes & Fix](/posts/abb-acs550-f0001-overcurrent/)
- [ABB ACS580 A7AB Fault - Causes & Fix](/posts/abb-acs580-a7ab-fault-code/)
