---
title: "Yaskawa A1000 VFD E08 Fault - Causes & Fix"
description: "E08 on a Yaskawa A1000 VFD signals an undervoltage condition on the DC bus. Most often caused by low incoming AC supply voltage."
pubDatetime: 2026-07-22T07:37:05Z
modDatetime: 2026-07-22T07:37:05Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 rectifier module or power board"
most_likely_cause: "Low incoming AC supply voltage"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming AC line voltage at the drive input terminals with a multimeter while the drive is running and check that it stays within the drive's rated input range"
  - "Inspect all input power terminal connections for tightness and signs of arcing or overheating"
  - "Check for other large loads on the same circuit that might cause voltage sag when they start"
---

## Yaskawa A1000 VFD E08 Fault — What It Means

The E08 fault code on a Yaskawa A1000 variable frequency drive indicates an undervoltage condition detected on the internal DC bus. The drive monitors the rectified DC voltage that powers its inverter section, and when this voltage drops below the programmed threshold for a certain duration, the drive trips to protect itself and the connected motor. This fault typically points to problems with the incoming AC power supply, wiring issues, or internal drive components.

Unlike overcurrent or overload faults that relate to motor load, E08 focuses on the power feeding the drive itself. The drive needs stable AC voltage within its rated range to maintain proper DC bus voltage. When the incoming voltage sags, brown-out conditions occur, or connections loosen, the DC bus cannot sustain the level needed for operation. Consult your model's manual for the exact voltage threshold values, as these vary by drive frame size and input voltage rating.

## Before You Replace Anything

Technicians sometimes replace the main control board or rectifier section without first measuring the incoming AC voltage at the drive input terminals under load. A simple voltage measurement during fault occurrence often reveals utility brown-out or wiring voltage drop as the real problem.

[Jump to Fix](#fix)

## Common Causes

- **Low incoming AC supply voltage (~45%)** Utility brown-out, undersized wiring, or high impedance in the feeder circuit causes the AC input to sag below the drive's minimum requirement, dropping the DC bus voltage.
- **Loose or corroded input terminals (~25%)** Poor contact at the R, S, T input terminals creates high resistance that causes voltage drop under load, triggering the undervoltage trip.
- **Faulty rectifier diodes (~15%)** One or more diodes in the input bridge rectifier fail open or develop high forward resistance, reducing the DC bus charging current and voltage.
- **Incorrect parameter settings (~10%)** The undervoltage trip threshold or detection time parameters are set too high or too sensitive for the actual supply conditions.
- **Failing DC bus capacitors (~5%)** Electrolytic capacitors on the DC bus lose capacitance over time, reducing their ability to buffer voltage dips and causing false undervoltage trips.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the incoming AC voltage at the drive terminals measure within the drive's rated input range (typically ±10% of nameplate voltage) during the fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply voltage is acceptable, so check input terminal tightness, inspect for damaged wiring, and review drive parameter settings for the undervoltage trip level.<br><strong>No:</strong> The supply voltage is low, so investigate the utility feed, check for undersized wiring or long cable runs, verify breaker and disconnect ratings, and look for other loads causing voltage sag.</div>
</details>

<details class="dtree"><summary>Does the fault occur immediately on power-up or only after the drive has been running for some time?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate faults point to supply issues or parameter settings, while delayed faults suggest thermal problems, capacitor degradation, or intermittent connections that worsen with heat.<br><strong>No:</strong> Random or load-dependent faults often trace to loose terminals, voltage sag under load, or a failing rectifier component that behaves erratically.</div>
</details>

<details class="dtree"><summary>Are there other drives or large motors on the same electrical branch circuit?</summary>
<div class="dtree-body"><strong>Yes:</strong> Simultaneous starting or heavy loads can cause momentary voltage sag that triggers undervoltage trips, so consider dedicated circuits or line reactors to buffer transients.<br><strong>No:</strong> The issue is likely isolated to this drive's supply path or internal components, so focus on wiring integrity and drive internal diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** and lock out the drive following all electrical safety procedures, then wait for the DC bus capacitors to discharge (consult your manual for safe discharge time).
2. **Measure incoming AC voltage** at the drive input terminals using a multimeter, checking all three phases (R-S, S-T, T-R) to verify balanced voltage within the drive's rated input range.
3. **Inspect and tighten** all input power terminal connections at the drive, the disconnect switch, and any junction boxes, looking for discoloration, corrosion, or loose hardware.
4. **Review drive parameters** using the keypad or software interface, checking the undervoltage trip threshold setting (often parameter L3-04 or similar, consult your manual) and comparing it to your measured supply voltage.
5. **Test under load** by restoring power and running the drive through its normal duty cycle while monitoring AC input voltage with a recording multimeter or power quality analyzer to capture any transient sags.
6. **Check the DC bus voltage** using the drive's internal monitoring function (often displayed as a parameter or diagnostic value) and compare it to the expected DC level for your AC input (roughly 1.35 times the AC line-to-line voltage for three-phase).
7. **Replace the rectifier section or capacitor bank** if voltage measurements confirm adequate AC supply but the DC bus remains low, or if the drive manual's troubleshooting flowchart directs you to these components after other checks pass.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 rectifier module or power board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e08-fault-code&k=Yaskawa+A1000+rectifier+module+or+power+board&tag=errorcodefixes-20) \| Frame-size and voltage-specific; verify exact model suffix before ordering |
| DC bus electrolytic capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-e08-fault-code&k=DC+bus+electrolytic+capacitor+bank&tag=errorcodefixes-20) \| High-voltage component requiring proper discharge and handling procedures |

## When to Call a Pro

Call a qualified electrician or drive service technician if you are not trained in high-voltage DC and AC power systems. VFD troubleshooting involves working near live bus bars with voltages often exceeding 300 VDC even after AC power is removed. A professional can safely measure DC bus ripple, perform rectifier diode testing with specialized equipment, and interpret drive diagnostic logs to pinpoint internal faults. If the fault persists after verifying supply voltage and tightening connections, internal components such as the rectifier bridge or capacitor bank likely need replacement, which requires drive disassembly, proper discharge procedures, and knowledge of the internal layout.

**Rough cost:** A pro service call runs about $200-600.
