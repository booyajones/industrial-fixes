---
title: "Allen-Bradley PowerFlex 525 F041 - Causes & Fix"
description: "F041 means Phase UV Short: excessive current between U and V output terminals. Most often caused by shorted motor leads or windings."
pubDatetime: 2026-06-12T10:14:55Z
modDatetime: 2026-06-12T10:14:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "PowerFlex 525 VFD replacement drive"
most_likely_cause: "Shorted or damaged motor leads between U and V"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Lock out power and visually inspect the drive output terminals and motor junction box for loose connections, contamination, carbon tracking, or pinched wires"
  - "Check for moisture, oil, or metal filings inside the motor junction box that could create a phase-to-phase short"
---

## Allen-Bradley PowerFlex 525 F041 — What It Means

F041 on an Allen-Bradley PowerFlex 525 means Phase UV Short. The drive has detected excessive current between the U and V output terminals going to the motor. Rockwell's manual defines this as a shorted condition on the output path and directs you to check the motor and drive output terminal wiring. This is not a parameter or settings fault. It points to a physical short in the motor circuit: damaged motor leads, failed motor windings, contaminated terminals, or less commonly a failed output stage inside the drive itself.

The fault is specifically tied to the output terminals, so the first suspects are always the motor cable and motor. Only after verifying those should you consider replacing the drive. The manufacturer recommends checking for a shorted condition and states that if the fault cannot be cleared after inspection and correction, replace the drive.

## Before You Replace Anything

Technicians sometimes replace the drive immediately without isolating the motor circuit first. Always disconnect the motor leads and retest the drive before ordering a replacement. A shorted motor or cable will destroy a new drive just as quickly.

[Jump to Fix](#fix)

## Common Causes

- **Shorted motor leads between U and V (~40%)** Damaged insulation in the motor cable from pinching, crushing, moisture ingress, or age allows U and V conductors to touch.
- **Shorted motor windings (~30%)** Internal insulation failure inside the motor creates a winding-to-winding short that the drive sees as excessive current on the U-V path.
- **Loose, contaminated, or incorrectly landed output wiring (~15%)** Debris, carbon tracking, moisture, or loose lugs at the drive or motor terminals create a low-resistance path between U and V.
- **Failed drive output power components (~10%)** A shorted IGBT or other output-stage component inside the drive creates the fault even with the motor disconnected.
- **Crushed or mechanically damaged conduit (~5%)** Physical damage to the raceway or cable tray crushes the motor cable and shorts phases together.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear and stay away when you disconnect all three motor leads from the drive and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive output stage is good and the problem is in the motor or motor cable. Proceed to insulation and resistance testing of the motor circuit.<br><strong>No:</strong> The drive itself has a shorted output stage. The drive will need to be replaced after verifying no external short is back-feeding through control or ground wiring.</div>
</details>

<details class="dtree"><summary>Do you see visible damage, moisture, oil, or carbon tracking at the motor terminals or inside the junction box?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean and dry the terminals thoroughly, inspect for cracked insulators or pinched leads, and repair or replace damaged components before reconnecting.<br><strong>No:</strong> The short is likely internal to the motor windings or hidden in the cable run. Move to phase-to-phase resistance and insulation testing.</div>
</details>

<details class="dtree"><summary>Does a megohm test of the motor and cable show low insulation resistance phase-to-phase or phase-to-ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or cable insulation has failed. Replace the motor cable first if accessible, then retest the motor alone. Replace the motor if the winding insulation is degraded.<br><strong>No:</strong> Recheck all terminations for tightness and correct landing. If everything tests normal and the fault returns immediately, replace the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power to the drive and verify zero voltage at the input and output terminals.
2. **Inspect the drive output terminals** (U, V, W) and motor junction box for loose lugs, damaged wire insulation, moisture, contamination, carbon tracking, or any visible signs of a short.
3. **Disconnect all three motor leads** from the drive output terminals U, V, and W and label them for correct reconnection.
4. **Restore power and attempt to start the drive** (with the motor disconnected). If F041 does not appear, the drive is good and the fault is in the motor circuit. If F041 appears immediately, the drive output stage is faulty and the drive must be replaced.
5. **Perform a phase-to-phase resistance check** on the motor leads (U-V, U-W, V-W) with the motor disconnected from the drive. Compare readings for balance and check for an abnormal short or open circuit.
6. **Megger or insulation-test the motor and cable** phase-to-phase and phase-to-ground to identify insulation breakdown. Consult your motor manufacturer's acceptable insulation-resistance values for your voltage class.
7. **Inspect the motor cable run** for crushed conduit, pinched wires, moisture intrusion, or mechanical damage along the entire path from drive to motor.
8. **Reconnect the motor** if all tests pass, restore power, and monitor. If F041 returns, replace the motor cable first (if suspect) or the motor (if winding insulation is low). If the fault appeared with the motor disconnected, replace the drive.

## Parts Often Needed

| Part | Notes |
|------|-------|
| PowerFlex 525 VFD replacement drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f041-fault-code&k=PowerFlex+525+VFD+replacement+drive&tag=errorcodefixes-20) \| Match the horsepower, voltage, and enclosure rating to your original drive. Only replace after verifying the motor and cable test good. |
| Three-phase motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f041-fault-code&k=Three-phase+motor+cable&tag=errorcodefixes-20) \| Use cable rated for VFD service with the correct gauge for your motor current and run length. Replace if insulation is damaged or megohm test fails. |
| Replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f041-fault-code&k=Replacement+motor&tag=errorcodefixes-20) \| Required if internal winding insulation has failed and phase-to-phase or phase-to-ground resistance is too low to safely operate. |

## When to Call a Pro

Call a qualified electrician or controls technician for F041 troubleshooting and repair. This fault involves high-voltage AC output circuits and requires lock-out/tag-out, insulation testing with a megohmmeter, and the ability to safely work inside the drive and motor junction box. Incorrect diagnosis can lead to repeated drive failures or motor damage. A technician will isolate the motor circuit, perform resistance and insulation tests to the correct standards, verify proper wire sizing and termination torque, and determine whether the fault is in the cable, motor, or drive output stage. If the drive must be replaced, a professional will also verify that all parameters and network settings are correctly transferred to the new unit.

**Rough cost:** A pro service call runs about $200-800 depending on whether the fix is new motor cable, motor rewind, or drive replacement.

## See Also

- [Allen-Bradley PowerFlex 525 F080 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f080-fault-code/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)
- [Allen-Bradley PowerFlex 4M Fault Codes — F2, F4, F5, F7, F12 Fix Guide](/posts/allen-bradley-powerflex-4m-fault-codes/)
- [Allen-Bradley PowerFlex 525 F125 - Causes & Fix](/posts/allen-bradley-powerflex-525-vfd-f125-fault-code/)
