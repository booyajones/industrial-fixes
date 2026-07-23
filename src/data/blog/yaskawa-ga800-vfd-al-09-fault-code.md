---
title: "Yaskawa GA800 VFD AL-09 Fault - Causes & Fix"
description: "AL-09 signals a VFD undervoltage fault. Most often caused by incoming AC supply voltage sag or an internal DC bus issue."
pubDatetime: 2026-07-21T07:32:28Z
modDatetime: 2026-07-21T07:32:28Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 DC bus capacitor bank"
most_likely_cause: "incoming AC supply voltage sag or dropout"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify all three phases of incoming AC power are present and within rated voltage"
  - "Inspect input power terminals for loose connections or corrosion"
  - "Reset the fault and attempt a no-load run to see if the fault recurs immediately or only under motor load"
---

## Yaskawa GA800 VFD AL-09 Fault — What It Means

The AL-09 fault on a Yaskawa GA800 variable frequency drive indicates an undervoltage condition has been detected on the internal DC bus. The drive monitors the rectified DC voltage that feeds the inverter section and will trip AL-09 if that voltage falls below a safe threshold. This threshold varies by drive model and input voltage rating, so consult your model's manual for the exact trip point. Undervoltage faults protect the drive and the connected motor from operating outside design parameters.

The fault can be triggered by problems with the incoming AC power supply, internal rectifier or capacitor issues, improper parameter settings, or excessive regenerative energy from the load. Because the drive relies on stable three-phase AC input (or single-phase on smaller models), any drop or interruption in that supply will immediately affect the DC bus. Some installations also see AL-09 during deceleration if the motor is regenerating power faster than the drive can dissipate it and no dynamic braking resistor is installed.

## Before You Replace Anything

Technicians sometimes replace the main control board or gate driver when the real problem is worn DC bus capacitors or a loose input power connection. Always measure incoming AC line voltage and DC bus voltage under load before swapping electronics.

[Jump to Fix](#fix)

## Common Causes

- **Incoming AC supply voltage sag or dropout (~40%)** Utility voltage drops, phase loss, or building electrical issues cause the DC bus to collapse below the trip threshold.
- **Aging DC bus capacitors (~25%)** Electrolytic capacitors lose capacitance over time and can no longer maintain stable DC bus voltage under load.
- **Excessive regenerative energy during deceleration (~15%)** High-inertia loads can push energy back into the DC bus faster than the drive can absorb it, especially without a braking resistor.
- **Loose or corroded input power connections (~10%)** Poor contact at the input terminals or internal bus bars creates voltage drop under load.
- **Incorrect drive parameter settings (~5%)** Deceleration time set too short or undervoltage trip level misconfigured can cause nuisance faults.
- **Rectifier diode or bridge failure (~5%)** A failed input rectifier diode reduces the effective DC bus voltage and can trigger undervoltage protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately on power-up, before the motor even starts?</summary>
<div class="dtree-body"><strong>Yes:</strong> Incoming AC voltage is likely low or a phase is missing. Measure line voltage at the drive input terminals with a multimeter.<br><strong>No:</strong> The fault is probably load-related or occurs during run or deceleration. Proceed to check DC bus voltage and deceleration parameters.</div>
</details>

<details class="dtree"><summary>Does the fault only appear during motor deceleration or stopping?</summary>
<div class="dtree-body"><strong>Yes:</strong> Regenerative energy is likely overwhelming the DC bus. Check if a dynamic braking resistor is installed and whether deceleration time is set too aggressively.<br><strong>No:</strong> The fault occurs during acceleration or steady run, pointing to supply voltage sag, capacitor wear, or a rectifier issue.</div>
</details>

<details class="dtree"><summary>When you measure the incoming AC line voltage under load, is each phase within the drive's rated input range?</summary>
<div class="dtree-body"><strong>Yes:</strong> The AC supply is adequate. Focus on the DC bus capacitors, internal connections, and drive parameter settings.<br><strong>No:</strong> The building supply is inadequate or a phase is weak. Work with an electrician to correct the incoming power before troubleshooting the drive further.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** the incoming AC power to the drive and verify zero voltage at the input terminals with a multimeter.
2. **Open the drive enclosure** and visually inspect the DC bus capacitors for swelling, leakage, or venting, which indicates failure.
3. **Check all input power terminations** (L1, L2, L3 or R, S, T) and DC bus bar connections for tightness and signs of arcing or corrosion.
4. **Measure incoming AC voltage** on all three phases under no-load and then again with the motor running to detect voltage sag.
5. **Review drive parameters** related to undervoltage trip level, deceleration time, and braking resistor enable using the keypad or configuration software.
6. **Test the DC bus voltage** by powering up the drive (motor disconnected) and measuring between the positive and negative DC bus terminals with a voltmeter, comparing to the expected value in the manual.
7. **Replace the DC bus capacitors** if they are visibly damaged or if measured DC bus voltage is significantly low compared to the rectified AC input, and reset the fault to test.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 DC bus capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-09-fault-code&k=Yaskawa+GA800+DC+bus+capacitor+bank&tag=errorcodefixes-20) \| Match the capacitance and voltage rating to your drive model and frame size. |
| Dynamic braking resistor for GA800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-al-09-fault-code&k=Dynamic+braking+resistor+for+GA800&tag=errorcodefixes-20) \| Required if the application involves high-inertia loads or frequent deceleration; consult drive manual for ohm and watt ratings. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician whenever you lack experience with high-voltage DC bus circuits or three-phase power systems. The DC bus can remain charged to several hundred volts even after AC power is removed, and improper handling can cause severe shock or arc flash. A professional will safely discharge the bus, perform diode and capacitor testing with specialized meters, review parameter settings, and verify that the building electrical supply meets the drive's requirements. If the drive is under warranty or service contract, contact Yaskawa or an authorized service center before opening the enclosure.

**Rough cost:** A pro service call runs about $200-600.
