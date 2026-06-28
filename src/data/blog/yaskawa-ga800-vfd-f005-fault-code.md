---
title: "Allen-Bradley PowerFlex F005 - Causes & Fix"
description: "F005 signals DC bus overvoltage from energy regenerating back into the drive. Usually fixed by slowing the deceleration ramp time."
pubDatetime: 2026-06-26T10:01:29Z
modDatetime: 2026-06-26T10:01:29Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - allen-bradley
money_part: "Dynamic braking resistor"
most_likely_cause: "deceleration ramp set too fast for the load inertia"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Reset the fault by pressing and holding the Stop button for 2-3 seconds and observe whether it trips again during the next deceleration cycle."
  - "Check Parameter 2 (Output Voltage) and Parameter 4 (DC Bus Voltage) during deceleration to see if DC bus climbs above 415V (230V-class) or 830V (460V-class)."
  - "Verify incoming line voltage (L1/L2/L3) with a true RMS meter to confirm it is within ±10% of the drive nameplate rating."
part_price: "$150-400"
no_buy_pct: "60%"
---

## Allen-Bradley PowerFlex F005 — What It Means

The F005 fault indicates an overvoltage condition on the DC bus inside your Allen-Bradley PowerFlex VFD (models 525, 750, and similar). The internal DC bus voltage climbed above safe limits, triggering a protective trip to prevent damage to capacitors and power components. This typically happens during deceleration when the motor acts as a generator and pushes energy back into the drive faster than the drive can dissipate it.

Note: F005 is not a Yaskawa GA800 fault code. Yaskawa drives use different fault conventions (such as OV for overvoltage or E.OC1 for overcurrent). If you have a Yaskawa GA800 and see a fault, consult the Yaskawa manual for the correct code definitions.

## Before You Replace Anything

Technicians sometimes replace the DC bus capacitors or power board when F005 appears repeatedly, yet the root cause is often a parameter setting (decel time) or missing braking resistor. Always measure DC bus voltage during deceleration and adjust parameters before swapping boards.

[Jump to Fix](#fix)

## Common Causes

- **Deceleration ramp too fast (~50%)** The motor stops too quickly for the load inertia, causing the motor to regenerate energy back into the drive and spike the DC bus voltage.
- **Overhauling or regenerative load (~25%)** The mechanical load (descending hoist, conveyor with momentum, cyclical press) drives the motor faster than the VFD's commanded speed, forcing the motor into generator mode.
- **Incoming AC voltage too high (~10%)** The line voltage exceeds the drive rating by more than 10%, raising the DC bus baseline and reducing headroom for regeneration.
- **Mismatched conveyor speeds (~8%)** Adjacent VFDs run at different frequencies, so one motor is grabbed and back-driven by the other, acting as a generator.
- **Loose power connections (~5%)** Partially clamped motor or line terminals create intermittent arcing or impedance that disturbs DC bus regulation.
- **Missing or undersized braking resistor (~2%)** High-inertia applications lack a braking resistor to absorb regenerated energy, so the DC bus climbs unchecked.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault appear only during deceleration or stopping?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor is regenerating energy. Increase the deceleration time parameter (P036 or P042) or add a braking resistor.<br><strong>No:</strong> Check incoming line voltage and look for loose wiring or a mechanical overhauling condition.</div>
</details>

<details class="dtree"><summary>Is the incoming line voltage within ±10% of the drive nameplate rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Line voltage is acceptable. Focus on decel ramp and braking resistor.<br><strong>No:</strong> Install a line reactor or step-down transformer to bring voltage into specification.</div>
</details>

<details class="dtree"><summary>Are there multiple drives or motors on the same mechanical system?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check for speed mismatches or back-driving between drives and synchronize commanded frequencies.<br><strong>No:</strong> The issue is isolated to this drive's parameters or load. Adjust decel time or add a braking resistor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Reset the fault** by pressing and holding the Stop button for 2 to 3 seconds until the display returns to Ready. If the keypad is locked, verify Parameter 36 (P1 Node) is set to 0 and Parameter 140 (Access Level) allows basic access. If a button reset fails, disconnect line power, wait 30 seconds, and reapply.
2. **Monitor DC bus voltage** by checking Parameter 4 (DC Bus Voltage) during normal operation and again during deceleration. For 230V-class drives, the bus should stay below 415V. For 460V-class drives, it should stay below 830V. If voltage spikes above these thresholds during decel, you have confirmed regeneration.
3. **Increase the deceleration time** by raising Parameter 36 (Decel Time 1) or Parameter P042 to allow a slower ramp. Start by doubling the current value and test. For very high inertia loads, consider setting the stop action to Coast instead of Ramp.
4. **Verify incoming line voltage** with a true RMS meter at L1, L2, and L3. Voltage must be within ±10% of the drive nameplate. If line voltage is high, install a line reactor or consult your utility to correct the supply.
5. **Inspect all power connections** at the line terminals, DC bus terminals, and motor output. Tighten any loose lugs and look for arcing marks or discolored wire strands. Replace damaged connectors.
6. **Add a braking resistor** if increasing decel time and verifying line voltage does not resolve the fault and DC bus still climbs above the safe threshold. Select a resistor rated for your drive model and install it according to the manufacturer's wiring diagram. Consult the drive manual for resistor ohm and wattage ratings.
7. **Check for mechanical overhauling** by reviewing the application. Hoists, inclines, presses, and conveyors with heavy pallets can push the motor. If the load can drive the motor, a braking resistor or external dynamic brake module is required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Dynamic braking resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f005-fault-code&k=Dynamic+braking+resistor&tag=errorcodefixes-20) \| Match ohm value and wattage to your drive model and load inertia per the manufacturer's selection table. |
| Line reactor (AC choke) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f005-fault-code&k=Line+reactor+%28AC+choke%29&tag=errorcodefixes-20) \| Install on the incoming AC line to reduce harmonic distortion and lower DC bus voltage when line voltage is high. |

## When to Call a Pro

Call a qualified electrician or drives technician if you are uncomfortable working with high-voltage three-phase power, if you need to add a braking resistor and are unsure of the wiring, or if the fault persists after adjusting decel time and verifying line voltage. A pro can measure DC bus ripple with an oscilloscope, calculate braking resistor duty cycle, and confirm that the power section and capacitors are healthy. If you have a Yaskawa GA800 and need help with a fault code, consult a Yaskawa-authorized service center since the F005 code does not apply to that brand.

**Rough cost:** A pro service call runs about $200-500.
