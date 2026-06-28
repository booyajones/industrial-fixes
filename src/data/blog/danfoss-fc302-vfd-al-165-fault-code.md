---
title: "Danfoss FC302 AL-165 - Causes & Fix"
description: "AL-165 is not a standard Danfoss code. Confirm exact code (likely Alarm 16, output phase loss). Check motor connections and parameters first."
pubDatetime: 2026-06-26T09:56:22Z
modDatetime: 2026-06-26T09:56:22Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Power Card (IGBT Module)"
most_likely_cause: "loose or disconnected motor cable at drive or motor terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify exact code on LCP display and check Parameter 15-32 for extended alarm details"
  - "Inspect terminals U, V, W at drive and motor for loose or corroded connections"
  - "Confirm Parameter 1-24 (Motor Nominal Current) matches motor nameplate rating"
---

## Danfoss FC302 AL-165 — What It Means

AL-165 does not appear in official Danfoss FC302 documentation. The closest standard code is Alarm 16 (Output Phase Loss / No Motor Presence), which triggers when the drive cannot detect motor windings during startup. This suggests an open circuit, short, or internal drive failure. If AL-165 appears on your display, verify the exact code on the Local Control Panel (LCP) or check Parameter 15-32 for extended alarm details. The code may also be a custom error from a PLC or HMI overlay rather than a Danfoss drive alarm.

If the code is actually Alarm 16, the drive has detected a missing or faulty motor connection on terminals U, V, or W. This can stem from broken motor windings, damaged cables, loose terminals, incorrect motor parameters, or failed drive output hardware (IGBT modules or power card).

## Before You Replace Anything

Technicians often replace IGBT modules or power cards before checking motor parameters and cable connections. Always verify Parameter 1-24 (Motor Nominal Current) matches the motor nameplate and inspect all terminal connections first.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected motor cable (~35%)** Terminals U, V, or W at the drive or motor end are not tightened, causing intermittent or complete loss of motor detection.
- **Incorrect motor current parameter (~25%)** Parameter 1-24 (Motor Nominal Current) does not match the motor nameplate, preventing the drive from detecting motor presence correctly.
- **Open or shorted motor windings (~20%)** Internal motor damage or cable insulation breakdown creates an open circuit or short that the drive reads as no motor presence.
- **Failed IGBT module or power card (~15%)** Internal drive hardware cannot energize output phases, so the drive never sees motor windings even when connections are correct.
- **Custom PLC or HMI error code (~5%)** AL-165 may be a user-defined fault from an external controller (PLC, SCADA, or HMI) rather than a Danfoss drive alarm, indicating a process timeout or safety interlock.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the exact code on the LCP read Alarm 16 or AL 16 (not AL-165)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow standard Danfoss Alarm 16 troubleshooting below.<br><strong>No:</strong> Check Parameter 15-32 for extended alarm details and consult your system integrator or PLC documentation, as AL-165 is not a standard Danfoss code.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when you disconnect the motor from the drive (terminals U, V, W)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault is in the motor or cable. Test motor winding continuity and cable insulation.<br><strong>No:</strong> Fault is internal to the drive (power card, IGBT, or output sensors). Contact a qualified VFD technician.</div>
</details>

<details class="dtree"><summary>Are all three motor cable phases tightly secured at both drive and motor terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify Parameter 1-24 matches motor nameplate current and run AMA (Auto Motor Adaptation) via Parameter 1-29.<br><strong>No:</strong> Tighten all U, V, W connections and reset the drive. If alarm persists, check motor windings and parameters.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Confirm the exact alarm code** by reading the LCP display carefully and checking Parameter 15-32 (Extended Alarm Code) for additional fault details.
2. **Power down and lock out** the drive using the disconnect switch, then wait for DC bus capacitors to discharge (minimum 5 minutes, consult your model's safety sheet).
3. **Inspect motor cable terminals** at drive outputs U, V, W and motor connection box. Tighten all terminals to manufacturer torque specifications and look for corrosion or damage.
4. **Disconnect the motor** from drive terminals U, V, W and attempt to run the drive unloaded. If the alarm clears, the fault is in the motor or cable. If it persists, the drive power section is faulty.
5. **Test motor windings** with an ohmmeter (all three phases should show similar resistance, within 5 percent) and check cable insulation with a megohmmeter (look for shorts or moisture damage).
6. **Verify motor parameters** in the drive: Parameter 1-24 (Motor Nominal Current) must match motor nameplate, and Parameters 1-20 to 1-25 (voltage, frequency, power, speed) must be correct.
7. **Run Auto Motor Adaptation (AMA)** via Parameter 1-29 to allow the drive to learn motor characteristics and improve detection accuracy.
8. **Check external control circuits** including digital input terminal 50 (if used for start/stop) and any emergency stop or interlock wiring that could prevent motor energization.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Power Card (IGBT Module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-165-fault-code&k=Danfoss+FC302+Power+Card+%28IGBT+Module%29&tag=errorcodefixes-20) \| Only if alarm persists with motor disconnected and all parameters correct. Requires factory-trained technician. |
| Three-phase motor cable (shielded, VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-165-fault-code&k=Three-phase+motor+cable+%28shielded%2C+VFD-rated%29&tag=errorcodefixes-20) \| Match wire gauge and insulation rating to motor current and drive voltage. Consult motor nameplate and drive manual. |

## When to Call a Pro

Call a qualified VFD technician or controls integrator if the alarm persists after you have tightened all connections and verified motor parameters. Internal drive faults (IGBT modules, power cards, or output sensors) require specialized test equipment, factory training, and high-voltage safety protocols. Also contact a professional if AL-165 appears on an HMI or PLC screen rather than the drive LCP, as it may be a custom error code that requires system-level troubleshooting beyond the drive itself. Do not attempt to disassemble the drive or measure DC bus voltages without proper training and PPE.

**Rough cost:** A pro service call runs about $200-800.
