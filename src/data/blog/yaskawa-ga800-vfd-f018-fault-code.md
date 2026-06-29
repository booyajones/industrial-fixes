---
title: "Yaskawa GA800 F018 Fault - Causes & Fix"
description: "F018 means motor short circuit detected. Most often caused by shorted motor windings or damaged cable insulation between drive and motor."
pubDatetime: 2026-06-27T11:38:17Z
modDatetime: 2026-06-27T11:38:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor cable (flexible THHN or SOOW rated for VFD use)"
most_likely_cause: "Shorted motor windings or damaged motor cable insulation"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect motor cable for cuts, burns, or moisture damage along its entire run"
  - "Check motor terminal box for loose connections, moisture, or carbon tracking between phases"
---

## Yaskawa GA800 F018 Fault — What It Means

F018 is a motor short circuit fault. The GA800 has detected an unintended electrical connection between the motor's terminals or between a terminal and ground, causing excessive current flow at the drive output. This protection code trips when the drive sees abnormal current that exceeds safe thresholds, pointing to shorted windings, damaged insulation, or a grounded phase. The fault can originate in the motor itself, the cable between drive and motor, or rarely inside the drive's output stage. In systems with multiple motors running in parallel, cumulative leakage to ground can also trigger F018.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the actual fault is in the motor or cable. Always megger-test the motor and cable insulation before replacing the VFD, a 10-minute test can save hundreds of dollars.

[Jump to Fix](#fix)

## Common Causes

- **Shorted motor windings (~40%)** Internal insulation breakdown inside the motor causes phase-to-phase or phase-to-ground short, detected by the drive as excessive current.
- **Damaged motor cable insulation (~35%)** Cuts, abrasion, moisture ingress, or age-related cracking in the cable between drive and motor creates a short circuit path.
- **Motor ground fault under load (~15%)** One phase shorts to the motor frame or conduit when the motor is running, especially common with older motors in wet environments.
- **Multiple motors with cumulative leakage (~5%)** When several motors run in parallel on one drive, their combined leakage current to ground can exceed the drive's fault threshold.
- **Failed drive output IGBT (~5%)** A shorted IGBT in the drive's output stage mimics a motor short circuit, though this is much less common than motor-side faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on power-up before the motor spins?</summary>
<div class="dtree-body"><strong>Yes:</strong> The short is likely in the cable or motor windings themselves. Disconnect the motor and megger-test both.<br><strong>No:</strong> The fault may be load-dependent or intermittent. Test insulation resistance both cold and after a brief run.</div>
</details>

<details class="dtree"><summary>When you disconnect the motor cable from the drive, does the fault clear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor or cable, not the drive. Proceed with insulation testing.<br><strong>No:</strong> The drive itself may have an internal short. Consult a qualified VFD technician or contact Yaskawa support.</div>
</details>

<details class="dtree"><summary>Does a megger test show insulation resistance below 1 MΩ to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have confirmed insulation failure. Identify whether it is in the cable (test each end separately) or the motor windings.<br><strong>No:</strong> Insulation is intact. Check for loose connections, moisture in the terminal box, or an intermittent fault that appears only under load.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Isolate and lock out power** to the GA800 drive and wait for DC bus capacitors to discharge per the manual's safety procedures.
2. **Disconnect the motor cable** from the drive's output terminals U, V, and W to separate the motor circuit from the drive.
3. **Visually inspect** the motor cable for cuts, abrasion, burns, or moisture along its entire length and check the motor terminal box for damage or contamination.
4. **Perform a megger test** on the motor and cable using a megohmmeter. Test insulation resistance between each phase pair and between each phase and ground. Readings below 1 MΩ indicate insulation failure.
5. **Measure winding resistance** with a multimeter between each pair of motor terminals. Values should be balanced within about 5 percent of each other. Large deviations point to a winding short.
6. **Reconnect the motor** and restart the drive. If the fault reappears with the motor connected but cleared when disconnected, the fault is in the motor or cable. If the fault persists with the motor disconnected, suspect an internal drive issue.
7. **Test the motor on line power** (if practical and safe) to confirm it draws rated current. If the motor trips a breaker or shows excessive current draw, the motor windings are shorted and the motor needs repair or replacement.
8. **Contact Yaskawa Technical Support** at 1.800.927.5292 or repair@yaskawa.com if diagnostic steps point to an internal drive fault or if you need guidance on IGBT testing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (flexible THHN or SOOW rated for VFD use) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f018-fault-code&k=Motor+cable+%28flexible+THHN+or+SOOW+rated+for+VFD+use%29&tag=errorcodefixes-20) \| Replace if megger test shows cable insulation failure. Match or exceed original wire gauge and VFD-rated insulation. |
| AC induction motor (matching frame and rated voltage) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f018-fault-code&k=AC+induction+motor+%28matching+frame+and+rated+voltage%29&tag=errorcodefixes-20) \| Required if motor windings are shorted. Consider a motor rewind shop if the motor is large or specialty. |

## When to Call a Pro

Call a qualified electrician or VFD technician for F018 faults. Diagnosis requires a megohmmeter and knowledge of high-voltage AC circuits. If the fault is traced to the motor, a motor shop can perform insulation testing and rewind services. If the drive itself has failed IGBTs, contact Yaskawa or an authorized service center. Do not attempt to repair the drive's internal power electronics without factory training. Yaskawa offers technical support at 1.800.927.5292 and repair services via repair@yaskawa.com.

**Rough cost:** A pro service call runs about $150-500 depending on whether repair involves cable replacement, motor rewind, or drive IGBT replacement.
