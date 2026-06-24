---
title: "Danfoss FC302 AL-64 - Causes & Fix"
description: "AL-64 (Voltage Limit) means the drive cannot supply enough voltage for the motor's speed and load demand. Most often caused by mechanical overload."
pubDatetime: 2026-06-22T10:17:55Z
modDatetime: 2026-06-22T10:17:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Replacement motor"
most_likely_cause: "Mechanical overload on the motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check for mechanical binding or overload by inspecting the pump, fan, or conveyor attached to the motor"
  - "Verify motor nominal current (parameter 124) matches the motor nameplate rating"
  - "Measure input voltage on all three phases and check for imbalance greater than 3%"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-64 — What It Means

Warning 64 (Voltage Limit) on the Danfoss FC302 means the drive cannot supply the voltage required to meet the motor's speed and load demand, causing the output voltage to hit its maximum limit. The drive detects that the motor's speed and load combination demands a voltage higher than the drive can provide. This is not a hard fault (the drive may not trip immediately), but it indicates the motor is under-volted, which can lead to stalled torque or overheating.

## Before You Replace Anything

Technicians often replace the drive power module when the real issue is mechanical overload or incorrect motor parameter settings. Remove the motor load temporarily and verify motor data in parameters 120-125 before swapping components.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload (~35%)** Motor is mechanically overloaded due to a jammed pump, stuck conveyor, binding fan blade, or other mechanical issue creating excessive load.
- **Incorrect motor parameters (~25%)** Motor nominal current (parameter 124) set too low, or motor power, frequency, or voltage data mismatched in parameters 120-125.
- **Low or imbalanced input voltage (~20%)** Input voltage is low or phase imbalance exceeds 3%, reducing the available DC bus voltage and limiting output voltage.
- **Ramp time too short (~10%)** Acceleration ramp time is set too fast, causing sudden high-current demand that pushes the drive to its voltage limit.
- **Motor winding degradation (~7%)** Motor winding insulation has deteriorated, moisture contamination has occurred, or thermal aging has increased resistance.
- **Faulty drive power section (~3%)** Drive inverter module has failed IGBTs, degraded DC link capacitors, or damaged heat sinks reducing available output voltage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the warning clear when you disconnect the motor load (uncouple the motor from the pump or fan)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is mechanical overload. Inspect and repair the driven equipment (pump, conveyor, fan) for jams, binding, or excessive load.<br><strong>No:</strong> The problem is in the drive, motor, or electrical supply. Move to the next check.</div>
</details>

<details class="dtree"><summary>Is the input voltage on all three phases within 3% of each other when measured with a voltmeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is balanced. Check motor parameters (especially parameter 124 nominal current) and motor winding insulation.<br><strong>No:</strong> Input voltage imbalance is the likely cause. Check for loose input connections, blown fuses, or voltage sags from other equipment.</div>
</details>

<details class="dtree"><summary>Does the motor megohm test show insulation resistance of 2 megohms or higher to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor windings are good. Verify drive parameters and ramp settings, or suspect a drive power section fault.<br><strong>No:</strong> Motor insulation has failed. The motor needs repair or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove the mechanical load** from the motor by disconnecting the coupling or belt. Run the drive with no load and observe if the warning clears. If it does, the problem is mechanical overload in the pump, fan, or conveyor.
2. **Verify motor parameters** in the drive. Check parameter 124 (motor nominal current) against the motor nameplate and confirm parameters 120-125 (motor power, voltage, frequency, speed, power factor) are set correctly.
3. **Measure input voltage** on all three phases at the drive input terminals using a multimeter. Calculate phase imbalance: if any phase differs by more than 3% from the average, check for loose input connections, blown fuses, or upstream voltage sags.
4. **Extend the ramp time** in Group 3-xx parameters to reduce sudden voltage demand during acceleration. Increase the ramp-up time gradually and test the drive under load to see if the warning clears.
5. **Perform a megohm test** on the motor windings to ground with the motor disconnected from the drive. Readings below 2 megohms indicate insulation failure. If the motor fails the test, repair or replace the motor.
6. **Inspect drive wiring and connections.** Tighten all motor cable connections at the drive output terminals and motor junction box. Check for corrosion, loose strands, or damaged insulation.
7. **Check the drive power section** if the warning persists with a known-good motor and correct parameters. Inspect cooling fans, heat sinks, and listen for unusual noises. If the drive has failed IGBTs or DC link capacitors, the power module will need replacement or professional repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-64-fault-code&k=Replacement+motor&tag=errorcodefixes-20) \| Only if megohm test shows insulation failure below 2 megohms; match horsepower, voltage, and frame size to the original. |
| Danfoss FC302 power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-64-fault-code&k=Danfoss+FC302+power+module&tag=errorcodefixes-20) \| Required if the drive power section has failed IGBTs or capacitors; consult Danfoss for the correct module for your drive frame size. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained to work with three-phase power, measure high-voltage DC bus levels, or program VFD parameters. Professional help is needed if the drive power module or inverter section has failed, if you cannot safely isolate and test the motor, or if input voltage imbalance points to an upstream electrical issue requiring a licensed electrician. A tech with a megohm tester and parameter programming tools can diagnose the fault in 30-60 minutes and avoid replacing expensive components unnecessarily.

**Rough cost:** A pro service call runs about $150-400 depending on whether the fix is a parameter adjustment, motor repair, or drive component replacement.

## See Also

- [Danfoss FC302 Alarm 39 - Causes & Fix](/posts/danfoss-fc302-alarm-39-fault-code/)
- [Danfoss FC302 AL-78 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-78-fault-code/)
- [Danfoss FC302 AL-68 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-68-fault-code/)
- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
