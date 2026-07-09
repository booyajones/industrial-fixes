---
title: "Danfoss FC302 VFD AL-70 Fault - Causes & Fix"
description: "AL-70 means PTC 1 Safe Stop triggered by motor overheating. Most common fix: let motor cool, check thermistor wiring, then reset."
pubDatetime: 2026-06-22T10:22:57Z
modDatetime: 2026-06-22T10:22:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "VLT PTC Thermistor Card MCB 112"
most_likely_cause: "Motor overheating due to excessive load or poor ventilation"
likelihood: "the most direct cause"
diy_or_pro: "pro"
free_checks:
  - "Let the motor cool completely and verify temperature with an infrared thermometer"
  - "Press the Reset key on the LCP or send a reset command via bus or digital I/O after cooling"
  - "Inspect the wiring between the motor thermistor and MCB 112 card for loose or corroded connections"
part_price: "$150-250 for MCB 112 card"
no_buy_pct: "40%"
---

## Danfoss FC302 VFD AL-70 Fault — What It Means

Alarm 70 on the Danfoss FC302 VFD indicates PTC 1 Safe Stop, meaning the motor has overheated and the VLT PTC Thermistor Card (MCB 112) has activated the Safe Torque Off (STO) function to prevent damage. The alarm triggers when the motor temperature exceeds the safe limit detected by the PTC (Positive Temperature Coefficient) thermistor embedded in the motor windings.

Once the digital input from the MCB 112 card is deactivated (meaning the motor temperature drops to an acceptable level), the drive can be reset via bus, digital I/O, or the Reset key on the LCP. The fault is a protective measure to avoid motor burnout and requires both cooling and troubleshooting before restart.

## Before You Replace Anything

Technicians sometimes replace the MCB 112 card first. Before ordering a new card, measure the motor thermistor resistance when cool (should be under 150 Ω) and inspect wiring for loose connections or shorts.

[Jump to Fix](#fix)

## Common Causes

- **Motor overheating (~35%)** The motor runs too hot due to excessive load, poor ventilation, or high ambient temperature, causing the PTC thermistor to trip the safe stop.
- **Thermistor wiring issues (~25%)** Disconnected, loose, or shorted wiring between the motor thermistor and the MCB 112 card causes the drive to interpret the signal as an overheat condition.
- **Failed PTC thermistor in motor (~20%)** The PTC sensor inside the motor is defective and shows high resistance even when the motor is cool, falsely triggering the alarm.
- **Faulty MCB 112 card (~15%)** The PTC Thermistor Card itself may be faulty or incorrectly configured, causing false detection of high temperature.
- **Environmental factors (~5%)** Blocked motor cooling fans, dirty heat sinks, or high ambient room temperature prevent adequate motor cooling and trigger the overheat alarm.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the motor physically hot to the touch or above normal operating temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor genuinely overheated. Check load conditions, ventilation, and allow cooling before resetting. Investigate why the motor is running hot.<br><strong>No:</strong> The alarm may be false. Check thermistor wiring and measure thermistor resistance to rule out a failed sensor or loose connection.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after the motor cools and you press Reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor overheated but the thermistor and card are working. Address the root cause of overheating (load, ventilation, duty cycle).<br><strong>No:</strong> The thermistor, wiring, or MCB 112 card is likely faulty. Measure thermistor resistance and inspect connections before replacing the card.</div>
</details>

<details class="dtree"><summary>Does the motor thermistor measure under 150 Ω when cool?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermistor is healthy. Check wiring continuity and the MCB 112 card configuration or replace the card if wiring is good.<br><strong>No:</strong> The thermistor is failed or open. Replace the motor thermistor or the motor if the sensor is not serviceable.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify motor temperature** using an infrared thermometer or by carefully touching the motor housing. If the motor is indeed hot, identify the source of overheating (excessive load, blocked ventilation, high ambient temperature).
2. **Allow the motor to cool** completely until the digital input from the MCB 112 card is deactivated. This may take 15-60 minutes depending on motor size and environment.
3. **Reset the drive** by pressing the Reset key on the LCP, sending a reset command via the bus, or using a configured digital I/O reset signal.
4. **Inspect thermistor wiring** between the motor and the MCB 112 card. Look for loose terminals, corroded connections, shorts, or open circuits. Repair or replace damaged wiring.
5. **Test the PTC thermistor** by disconnecting it from the motor and measuring resistance with a multimeter. A healthy PTC thermistor should read less than 150 Ω at 25°C and jump to over 1,000 Ω (often 2-5 kΩ) when heated above the trip point.
6. **Check MCB 112 card configuration** in the drive parameters. Verify that the card is correctly installed and the digital input is mapped to the PTC function. If the card is suspect, swap it with a known-good unit for testing.
7. **Address root cause of overheating** if the motor was genuinely hot. Reduce load, improve ventilation, clean motor fans and heat sinks, or review duty cycle and ambient conditions to prevent recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VLT PTC Thermistor Card MCB 112 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-70-fault-code&k=VLT+PTC+Thermistor+Card+MCB+112&tag=errorcodefixes-20) \| Replace if the card is faulty or incorrectly reading the thermistor signal after wiring and sensor are confirmed good. |
| Motor PTC thermistor sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-70-fault-code&k=Motor+PTC+thermistor+sensor&tag=errorcodefixes-20) \| Replace if the sensor shows high resistance when cool or is open-circuit; consult motor manufacturer for correct replacement part. |
| Motor thermistor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-70-fault-code&k=Motor+thermistor+cable&tag=errorcodefixes-20) \| Replace if wiring is damaged, shorted, or corroded between the motor and the MCB 112 card. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained to work with industrial drives and motor controls. The repair requires interpreting digital inputs, testing thermistor circuits, and configuring drive parameters. If the motor itself is overheating due to mechanical or electrical faults (bearing failure, rotor issues, phase imbalance), a motor specialist should diagnose and repair the root cause. High-voltage work and drive parameter changes should only be performed by personnel familiar with Danfoss VFD operation and safety lockout procedures.

**Rough cost:** A pro service call runs about $200-500 for diagnostics, thermistor replacement, or MCB 112 card swap.

## See Also

- [Danfoss FC302 ALARM 15 - Causes & Fix](/posts/danfoss-fc302-alarm-15-fault-code/)
- [Danfoss FC302 ALARM 45 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-45-fault-code/)
- [Danfoss FC302 Alarm 51 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-51-fault-code/)
- [Danfoss FC302 VFD AL-109 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-109-fault-code/)
