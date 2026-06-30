---
title: "Yaskawa GA800 LF Fault - Causes & Fix"
description: "LF (Output Phase Loss) means the drive detects a missing motor phase. Most common fix: tighten or replace the motor cable."
pubDatetime: 2026-06-28T10:16:33Z
modDatetime: 2026-06-28T10:16:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor power cable (3-conductor shielded)"
most_likely_cause: "Disconnected or broken motor main circuit cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down and lock out, then check all output terminals (U, V, W) on the drive and motor for loose or corroded connections"
  - "Measure resistance between each pair of motor terminals (U–V, V–W, W–U) with a multimeter to confirm all phases are continuous"
part_price: "$50-150 for typical motor cable"
no_buy_pct: "40%"
---

## Yaskawa GA800 LF Fault — What It Means

The LF fault code on a Yaskawa GA800 VFD stands for Output Phase Loss. The drive's internal monitoring circuit has detected that one or more phases of the three-phase output to the motor are disconnected or open. This is an output-side problem, not an input power issue. The drive will shut down to protect the motor and itself from damage caused by running on unbalanced current.

This fault typically points to a broken motor cable, a loose terminal connection at the drive or motor, or an open winding inside the motor. The drive will not restart until the cause is corrected and the fault is cleared.

## Before You Replace Anything

Technicians sometimes replace the VFD control board thinking the output current sensor is faulty. Always measure motor cable and winding resistance first to confirm the fault is in the field wiring or motor, not the drive electronics.

[Jump to Fix](#fix)

## Common Causes

- **Disconnected or broken motor cable (~45%)** A damaged, cut, or internally broken conductor in the motor power cable is the most frequent cause of LF faults.
- **Loose terminal connections (~30%)** Output terminals (U, V, W) at the drive or motor that are not fully tightened or have corroded contacts will create an open circuit.
- **Open motor winding (~15%)** One phase of the motor's internal windings has failed, showing infinite resistance when measured.
- **Incorrect wiring in main circuit (~8%)** A missing or misconnected phase wire during installation will trigger output phase loss detection.
- **Faulty output current sensor (~2%)** The drive's control board or output current sensor may falsely report phase loss even when wiring is correct.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>When you measure resistance between any two motor terminals (U–V, V–W, or W–U), do you see infinite resistance (∞ Ω or &gt;100 kΩ) on one pair?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor winding is open. The motor needs to be repaired or replaced.<br><strong>No:</strong> The motor windings are intact. Continue checking cable and connections.</div>
</details>

<details class="dtree"><summary>Are all three phase-to-phase resistances within 10% of each other (typically 0.1–2.0 Ω per phase)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor is balanced. Inspect cable integrity and terminal tightness for intermittent breaks.<br><strong>No:</strong> One phase shows higher or infinite resistance. Check for a broken conductor in the motor cable or a loose terminal.</div>
</details>

<details class="dtree"><summary>After tightening all terminals and clearing the fault, does the LF code reappear immediately on restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is persistent. Replace the motor cable or motor if winding is open. If both test good, the drive's output current sensor may be faulty.<br><strong>No:</strong> The problem was a loose connection. Monitor the drive during normal operation to confirm the fix.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive completely. Wait for all internal capacitors to discharge before opening the enclosure.
2. **Inspect motor cables** for visible damage, cuts, or burns. Look for signs of physical stress or environmental damage along the cable run.
3. **Measure resistance** between U, V, and W at both the drive output terminals and the motor terminals using a multimeter. Record all three phase-to-phase readings (U–V, V–W, W–U).
4. **Tighten all output terminals** at the drive and motor. Check that each wire is fully seated and torqued to the manufacturer's specification in the GA800 manual.
5. **Test motor windings** by comparing the three phase-to-phase resistance readings. If one pair shows infinite resistance, the motor winding is open and the motor must be replaced.
6. **Verify wiring diagram** against the Yaskawa GA800 elementary diagram. Confirm that U, V, and W are connected correctly and that no phase is missing.
7. **Clear the fault** via the keypad and restart the drive. Monitor for recurrence during a test run under normal load.
8. **If the fault persists** after confirming all wiring and motor windings are good, contact Yaskawa Technical Support at repair@yaskawa.com or 1.800.927.5292 with your model, serial number, and application details.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor power cable (3-conductor shielded) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f050-fault-code&k=Motor+power+cable+%283-conductor+shielded%29&tag=errorcodefixes-20) \| Choose cable rated for your motor horsepower and ambient temperature; consult the GA800 manual for conductor size. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f050-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Replace if one winding shows infinite resistance; match horsepower, voltage, and frame size to the original. |
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f050-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Only if all field wiring and motor test good and Yaskawa Support confirms output sensor failure; provide full model and serial number. |

## When to Call a Pro

Call a qualified electrician or industrial technician if you are not trained to work safely around high-voltage VFD circuits. Measuring motor resistance and inspecting terminals requires lock-out/tag-out procedures and knowledge of three-phase power systems. If the motor cable or motor itself needs replacement, the job involves terminating high-current conductors and verifying proper grounding. If all field components test good and the fault persists, the drive may need board-level repair or replacement, which requires factory-trained service and proper handling of static-sensitive control electronics.

**Rough cost:** A pro service call runs about $150-400 depending on cable replacement or motor repair.
