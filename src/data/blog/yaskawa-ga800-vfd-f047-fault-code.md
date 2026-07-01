---
title: "Yaskawa GA800 LF Fault - Causes & Fix"
description: "LF fault means output phase loss (missing motor connection). Most often a disconnected or broken motor cable. Check wiring first."
pubDatetime: 2026-06-29T10:31:18Z
modDatetime: 2026-06-29T10:31:18Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor main circuit cable (three-conductor, rated for VFD output)"
most_likely_cause: "Disconnected, broken, or improperly wired motor main circuit cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down and visually inspect all connections at the VFD output terminals (U, V, W) and motor terminals for loose or corroded screws"
  - "Check the motor main circuit cable for visible damage, cuts, or wear along its entire length"
part_price: "$50-200 depending on cable gauge and length"
no_buy_pct: "60%"
---

## Yaskawa GA800 LF Fault — What It Means

The LF fault code (sometimes misread as F047 due to display formatting) stands for Output Phase Loss. The drive has detected that one or more of the output phases (U, V, or W) leading to the motor are disconnected or open-circuit. This is a safety shutdown to prevent motor damage or unbalanced operation due to missing output voltage.

The fault is triggered when the VFD cannot sense proper current flow on all three output legs. It does not mean the drive itself has failed. It means the physical connection between the drive output terminals and the motor has been interrupted somewhere along the main circuit cable.

## Before You Replace Anything

Technicians sometimes replace internal VFD boards or capacitors when the LF fault appears. First inspect and test the motor cable for continuity with a multimeter (expect low resistance, typically under 1 ohm per phase). The fault is nearly always a physical wiring problem, not an internal drive failure.

[Jump to Fix](#fix)

## Common Causes

- **Disconnected or broken motor main circuit cable (~50%)** The most common cause is a physical break, disconnection, or loose connection in the cable running from the VFD output (U, V, W) to the motor terminals.
- **Loose terminal connections (~25%)** Output terminal screws at the VFD or motor can vibrate loose over time, creating an open circuit on one or more phases.
- **Damaged or corroded wiring (~15%)** Corrosion, moisture intrusion, or physical wear in the motor cable can create high resistance or open circuits in one or more conductors.
- **Improper wiring during installation (~7%)** Incorrect wiring at the output terminals or at the motor junction box can result in missing phase connections.
- **Internal wiring errors in main circuit input power (~3%)** Less common but possible, incorrect wiring at the drive's input power terminals can sometimes trigger output phase detection faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all terminal screws at the VFD output (U, V, W) and motor tight and secure?</summary>
<div class="dtree-body"><strong>Yes:</strong> The connections are not the issue. Proceed to test the motor cable for continuity.<br><strong>No:</strong> Tighten all terminal screws and restart the drive. If the fault clears, the loose connection was the cause.</div>
</details>

<details class="dtree"><summary>Does a multimeter show continuity (low resistance, typically under 1 ohm) on each of the three motor cable conductors from VFD to motor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is intact. The issue may be internal or require advanced diagnostics. Contact Yaskawa support.<br><strong>No:</strong> One or more conductors are open. Replace or repair the motor main circuit cable.</div>
</details>

<details class="dtree"><summary>Is there visible damage (cuts, abrasion, or corrosion) on the motor cable insulation or conductors?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the damaged cable before attempting further operation.<br><strong>No:</strong> The cable appears intact. Verify wiring is correct per the GA800 wiring diagram and recheck all connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down safely** by disconnecting main power to the GA800 drive and waiting for all internal indicators to go dark.
2. **Inspect the motor cable** from the VFD output terminals (U, V, W) to the motor junction box for any visible damage, cuts, abrasion, or loose connections.
3. **Check all terminal screws** at both the VFD output and motor terminals to confirm they are tight and properly seated.
4. **Test for continuity** using a multimeter set to resistance mode. Measure each of the three output conductors (U, V, W) from VFD to motor. Expect low resistance, typically under 1 ohm per phase depending on cable length.
5. **Verify wiring** against the GA800 wiring diagram to confirm U, V, and W are correctly connected with no crossed or missing phases.
6. **Replace or repair** the motor main circuit cable if you find an open circuit, damaged insulation, or broken conductor.
7. **Reconnect power** and clear the fault from the drive. Run the motor under load and observe for any recurrence of the LF fault. If the fault persists after verified good wiring, contact Yaskawa technical support at 1.800.927.5292 (Option 2, then Option 1).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor main circuit cable (three-conductor, rated for VFD output) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f047-fault-code&k=Motor+main+circuit+cable+%28three-conductor%2C+rated+for+VFD+output%29&tag=errorcodefixes-20) \| Match the wire gauge and length to your original cable and motor nameplate current rating. Consult the GA800 Technical Manual for cable sizing tables. |
| Terminal lugs or ferrules | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f047-fault-code&k=Terminal+lugs+or+ferrules&tag=errorcodefixes-20) \| If replacing the cable, use properly sized crimp lugs or ferrules for the VFD and motor terminal blocks. |

## When to Call a Pro

Call a qualified electrician or industrial automation technician if you are not trained to work with three-phase power or VFD wiring. This repair involves high-voltage motor circuits and requires lockout/tagout procedures, multimeter testing, and proper cable installation. If the motor cable tests good and all wiring is verified correct but the LF fault persists, contact Yaskawa Technical Support at repair@yaskawa.com or 1.800.927.5292 (Option 2 for Technical Support, then Option 1 for Drive Support). They may request your project file and trend recordings to replicate the issue. The GA800 Maintenance & Troubleshooting Manual does not include internal repair information beyond fan and control board replacement, so advanced diagnostics require factory support.

**Rough cost:** A pro service call runs about $150-400 depending on cable length and labor.
