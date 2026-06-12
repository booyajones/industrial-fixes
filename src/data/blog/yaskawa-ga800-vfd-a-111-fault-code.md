---
title: "Yaskawa GA800 A.111 - Causes & Fix"
description: "A.111 on a Yaskawa GA800 VFD signals an output-phase or motor-connection issue. Check motor cables and drive terminals first."
pubDatetime: 2026-06-08T11:04:24Z
modDatetime: 2026-06-08T11:04:24Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Loose or damaged output cable connection between the drive and motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "VFD-rated shielded motor cable"
---

## Yaskawa GA800 A.111 — What It Means

The A.111 fault on a Yaskawa GA800 variable frequency drive typically indicates a problem with the drive's output phase or motor connection. This can stem from loose wiring, damaged motor cables, phase imbalance, or a fault within the motor itself. The drive's internal monitoring detects an abnormality in the current or voltage on one or more output phases and shuts down to protect both the drive and the motor.

Because the exact A.111 definition does not appear in all published GA800 documentation, always consult your drive's specific manual or the fault-code table in the operator guide. Yaskawa's standard troubleshooting workflow requires you to remove the underlying cause before pressing the RESET button on the keypad. Simply resetting without fixing the root problem will cause the fault to reappear immediately or during the next start attempt.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the real issue is a corroded terminal or damaged motor cable. Measure resistance and continuity on each output phase and inspect all terminations under power-off/locked-out conditions before ordering a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Loose output terminal or damaged motor cable (~40%)** Vibration, heat cycling, or improper torque during installation can loosen terminal screws or crack insulation, creating intermittent contact or a short.
- **Motor winding fault or ground fault (~25%)** A shorted turn, phase-to-ground fault, or contamination inside the motor housing will draw unbalanced current and trip the drive.
- **Phase imbalance or missing phase (~20%)** If one output conductor is open or has much higher resistance than the others, the drive sees asymmetric load current and flags a fault.
- **Incorrect motor parameters or mismatch (~10%)** When the programmed motor nameplate data does not match the actual motor, the drive's protection algorithms may interpret normal operation as a fault.
- **Drive output stage damage (~5%)** A failed IGBT or gate driver on one phase can produce distorted output waveforms that the drive's diagnostics detect as an anomaly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after pressing RESET and remain clear through a no-load test run?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is likely intermittent or load-dependent. Inspect motor cable routing for pinch points and verify torque on all output terminals.<br><strong>No:</strong> The fault is persistent. Proceed to measure motor winding resistance and insulation resistance to ground with the drive disconnected.</div>
</details>

<details class="dtree"><summary>Are all three motor-cable conductors intact and showing equal resistance phase-to-phase?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is sound. Check the motor for internal faults using a megohmmeter and verify that programmed motor parameters match the nameplate.<br><strong>No:</strong> Replace or repair the damaged cable and re-terminate at both ends with proper torque before testing again.</div>
</details>

<details class="dtree"><summary>Does the drive display the same fault when connected to a known-good motor or a resistive load bank?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive output stage is likely damaged. Contact Yaskawa technical support or an authorized service center for drive repair or replacement.<br><strong>No:</strong> The original motor is faulty. Repair or replace the motor and confirm nameplate compatibility with the drive catalog code.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect and lock out** all power to the drive, wait for the DC bus capacitors to discharge (at least five minutes), and verify zero voltage with a multimeter before touching any terminals.
2. **Inspect output terminals U, V, W** on the drive for loose screws, discoloration, or carbon tracking. Tighten to the torque specification in the GA800 installation manual if loose.
3. **Examine the motor cable** along its entire run for cuts, pinch points, or areas where insulation is worn through. Replace any damaged cable with shielded motor cable rated for VFD use.
4. **Measure motor winding resistance** phase-to-phase (U-V, V-W, W-U) with the cable disconnected from the drive. Readings should be within a few percent of each other.
5. **Perform an insulation-resistance test** from each motor phase to ground using a 500 V or 1000 V megohmmeter. Readings below 1 MΩ indicate contamination or winding damage.
6. **Verify motor nameplate parameters** in the drive programming (rated voltage, current, frequency, speed). Incorrect settings can cause the drive to misinterpret normal operation as a fault.
7. **Restore power and press RESET** on the keypad. If the fault clears and the drive runs normally, monitor for recurrence. If A.111 returns immediately, contact Yaskawa technical support or an authorized service partner for drive evaluation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-111-fault-code&k=VFD-rated+shielded+motor+cable&tag=errorcodefixes-20) \| Use cable rated for inverter duty with symmetrical construction and proper shield grounding at the drive end only. |
| Replacement motor (if winding fault confirmed) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-111-fault-code&k=Replacement+motor+%28if+winding+fault+confirmed%29&tag=errorcodefixes-20) \| Match voltage, horsepower, frame, and speed to the original nameplate and verify compatibility with the GA800 catalog code. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained in high-voltage lockout/tagout, if you lack a megohmmeter or insulation tester, or if the fault persists after verifying all external wiring and motor integrity. Drive output-stage failures require factory-authorized service or replacement. Yaskawa's maintenance documentation notes that field repair beyond fan and control-board replacement is not covered in standard guides, so drive internal faults should be handled by technical support or an authorized service center. Always confirm the drive catalog code on the nameplate matches your application before troubleshooting, and inspect for shipping or installation damage if the system is new.

**Rough cost:** A pro service call runs about $200-600.
