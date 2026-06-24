---
title: "Danfoss FC302 Alarm 81 - Causes & Fix"
description: "Alarm 81 means hardware protection triggered by motor overcurrent or DC-link overvoltage. Most often caused by motor overload or jam."
pubDatetime: 2026-06-22T10:31:26Z
modDatetime: 2026-06-22T10:31:26Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT Power Board"
most_likely_cause: "motor overload or mechanical jam"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (turn off mains, wait 5 minutes for DC-link discharge, power back on) and press Reset to see if fault clears"
  - "Inspect motor shaft and driven load for mechanical binding or jam that would stall the motor"
---

## Danfoss FC302 Alarm 81 — What It Means

Alarm 81 (Protection Mode) activates when the Danfoss FC302 detects that motor current or DC-link voltage has exceeded a predefined hardware safety limit. This is a hardware-initiated protection, not a parameter-based warning. The drive's internal circuitry (gate driver or DC-link monitor) detects an unsafe condition and forces a shutdown to protect components. Motor current typically triggers this alarm when it exceeds 150 to 200% of rated current, depending on model and settings. DC-link overvoltage typically trips at around 850V for 400V-class drives. The drive will not restart until the fault condition is cleared and power is cycled.

## Before You Replace Anything

Many technicians replace the IGBT power board without testing the motor and cable first. Disconnect the motor and run the drive unloaded to isolate whether the fault is internal or external before ordering expensive inverter components.

[Jump to Fix](#fix)

## Common Causes

- **Motor overload or mechanical jam (~35%)** Motor is stalled, shaft is jammed, or pump/fan is clogged, causing excessive current draw that trips the hardware protection.
- **Shorted motor winding or cable fault (~25%)** Partial short in motor windings or insulation failure in motor cable creates current spikes that exceed the hardware limit.
- **Incorrect motor data in parameters (~15%)** Nominal motor current (parameter 1-24) set too high causes the drive to misinterpret normal current as an overload condition.
- **DC-link overvoltage from input transients (~15%)** Voltage spikes from utility transients, or DC-link capacitor failure causing voltage imbalance, push DC-link above the hardware threshold.
- **Failed IGBTs or power board (~10%)** Internal short in inverter IGBTs or rectifier diodes causes current surge or DC-link spike that triggers hardware protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm return immediately after power cycle and reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault is persistent, likely internal to the drive or a continuous external fault (shorted cable or motor).<br><strong>No:</strong> Fault was transient, investigate load conditions and motor for intermittent binding or electrical issues.</div>
</details>

<details class="dtree"><summary>Does the motor shaft spin freely by hand when disconnected from the load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor bearings are okay, check the driven load (pump, fan, conveyor) for binding or obstruction.<br><strong>No:</strong> Motor bearings are seized or windings are shorted, remove motor for bench testing or replacement.</div>
</details>

<details class="dtree"><summary>Does Alarm 81 still occur when motor cable is disconnected and drive runs unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fault is internal to the VFD (power board, IGBTs, or DC-link), requires component-level diagnosis or board replacement.<br><strong>No:</strong> Fault is in the motor or motor cable, proceed with megohm insulation test and cable inspection.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off mains power** to the drive and wait 5 minutes for the DC-link capacitors to discharge completely before working on any connections.
2. **Press Reset** on the drive control panel to clear Alarm 81, then observe whether the fault returns immediately or only under load.
3. **Disconnect the motor cable** from the drive output terminals (U, V, W) and run the drive with no load to isolate whether the fault is internal or external.
4. **Perform a megohm insulation test** on the motor windings to ground using a 500V megohmmeter, insulation resistance must be 2 megohms or higher (below this indicates insulation failure).
5. **Measure input voltage** on all three phases at the drive input terminals, phase imbalance must be 3% or less (for example 400V plus or minus 12V).
6. **Inspect the motor cable** for physical damage, moisture ingress, or loose connections at both the drive and motor terminals, and check continuity between all three motor phases for balanced resistance.
7. **Check parameter 1-24** (nominal motor current) to confirm it matches the actual motor nameplate current, incorrect settings cause false protection trips.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT Power Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-81-fault-code&k=Danfoss+FC302+IGBT+Power+Board&tag=errorcodefixes-20) \| Only replace after confirming internal fault by running drive unloaded with motor disconnected, consult your model's manual for exact part number |
| Shielded Motor Cable (VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-81-fault-code&k=Shielded+Motor+Cable+%28VFD-rated%29&tag=errorcodefixes-20) \| Use proper VFD-rated cable with symmetrical shielding if insulation test fails or cable shows physical damage |

## When to Call a Pro

Call a qualified electrical technician or VFD specialist if you are not trained to work on high-voltage industrial drives. Diagnosis requires live voltage measurements on three-phase power, DC-link voltages above 500V, and component-level testing of power electronics. If the drive continues to trip Alarm 81 with the motor disconnected, internal repair or board replacement must be performed by someone with proper training in VFD power circuits and access to OEM diagnostic tools. Motor insulation testing and cable fault location also require specialized megohm testers and current-clamp instrumentation.

**Rough cost:** A pro service call runs about $300-800 depending on whether repair is motor cable, motor rebuild, or VFD power board replacement.
