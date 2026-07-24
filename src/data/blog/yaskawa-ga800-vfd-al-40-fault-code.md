---
title: "Yaskawa GA800 VFD AL-40 Fault - Causes & Fix"
description: "AL-40 indicates an output phase loss or imbalance. Most often caused by loose motor terminal connections. Check all three output wires."
pubDatetime: 2026-07-22T07:31:43Z
modDatetime: 2026-07-22T07:31:43Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Motor cable assembly (shielded, three-conductor plus ground)"
most_likely_cause: "Loose or corroded motor terminal connections"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down and visually inspect all three output terminals on the drive for tightness and corrosion"
  - "Check motor terminal box connections for loose or burned lugs"
  - "Look for physical damage to the motor cable jacket or conduit"
no_buy_pct: "60%"
---

## Yaskawa GA800 VFD AL-40 Fault — What It Means

The AL-40 fault on a Yaskawa GA800 variable frequency drive signals an output phase loss or imbalance. The drive has detected that one or more of the three motor output phases is not delivering current as expected, either due to an open circuit, a poor connection, or an unbalanced load. This protection stops the drive to prevent motor damage from single-phasing.

The fault typically appears during operation or immediately after a start command. The drive monitors output current on all three legs (U, V, W) and triggers AL-40 when it sees asymmetry beyond its threshold. Common triggers include loose terminals, damaged motor cables, or a fault inside the motor windings themselves.

## Before You Replace Anything

Technicians sometimes replace the drive itself when the real problem is a loose wire or corroded terminal at the motor. Always measure resistance phase-to-phase at the motor before ordering a new VFD.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded motor terminal connections (~40%)** Vibration or heat can loosen terminal screws at the drive output or motor, creating intermittent contact and phase imbalance.
- **Damaged motor cable (~25%)** A broken conductor inside the cable jacket or a crushed conduit can open one phase without visible exterior damage.
- **Motor winding fault (~20%)** An open or shorted winding inside the motor creates an imbalance that the drive detects as a lost phase.
- **Drive output stage failure (~10%)** A failed IGBT or gate driver on one output leg inside the VFD can stop current flow on that phase.
- **Incorrect drive parameter setting (~5%)** Motor nameplate data entered incorrectly or a phase-loss detection threshold set too sensitive can cause nuisance trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you see scorch marks, melted insulation, or smell burning at the motor terminal box?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or cable has failed and needs professional inspection; do not re-energize.<br><strong>No:</strong> Proceed to check terminal tightness and cable continuity.</div>
</details>

<details class="dtree"><summary>Does a continuity test show infinite resistance on any output phase (U-V, V-W, W-U) with the motor disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor has an open winding and requires rewinding or replacement.<br><strong>No:</strong> The motor windings are intact; inspect cable and connections.</div>
</details>

<details class="dtree"><summary>After re-torquing all terminals to specification, does the fault clear on restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a loose connection; monitor the drive over the next few cycles to confirm.<br><strong>No:</strong> The cable or drive output stage may be faulty; call a technician with a megohmmeter and oscilloscope.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power sources feeding the VFD, then verify zero voltage at the input and output terminals with a multimeter.
2. **Remove the motor cable** from the drive output terminals (U, V, W) and inspect each lug for corrosion, heat discoloration, or loose strands.
3. **Measure resistance** between each pair of motor leads (U-V, V-W, W-U) at the motor end with the cable disconnected; all three readings should be within a few tenths of an ohm of each other.
4. **Inspect the motor terminal box** for loose screws, burned terminals, or moisture; clean any corrosion with a wire brush and apply contact cleaner.
5. **Re-torque all output terminals** on both the drive and motor to the values given in the installation manual, using a calibrated torque screwdriver or wrench.
6. **Reconnect the motor cable** and restore power, then clear the fault using the keypad reset function and attempt a slow-speed test run.
7. **Monitor output current** on all three phases during the test run using the drive display or a clamp meter; any imbalance greater than 10% suggests a remaining cable or motor issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable assembly (shielded, three-conductor plus ground) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-40-fault-code&k=Motor+cable+assembly+%28shielded%2C+three-conductor+plus+ground%29&tag=errorcodefixes-20) \| Match gauge and length to the original; use VFD-rated cable to minimize EMI. |
| Terminal lugs and heat-shrink tubing | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-40-fault-code&k=Terminal+lugs+and+heat-shrink+tubing&tag=errorcodefixes-20) \| Replace any corroded or burned crimp lugs with new compression-style connectors rated for the motor current. |

## When to Call a Pro

Call a qualified electrician or drive technician if you lack a lockout/tagout procedure, if the fault persists after re-torquing all terminals, or if you measure open or shorted windings in the motor. High-voltage VFD output can exceed 480 volts and requires proper PPE and test equipment. A technician will use a megohmmeter to test insulation resistance, an oscilloscope to verify balanced output waveforms, and thermal imaging to find hidden hot spots. If the drive itself has failed, factory-authorized repair or board-level replacement is the safest path.

**Rough cost:** A pro service call runs about $150-400.
