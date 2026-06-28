---
title: "Danfoss FC302 AL-116 Fault - Causes & Fix"
description: "AL-116 is not a standard Danfoss code. It likely means Alarm 16 (short circuit on output). Most common: failed IGBT power module."
pubDatetime: 2026-06-25T09:16:14Z
modDatetime: 2026-06-25T09:16:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT power module or inverter board assembly"
most_likely_cause: "Failed IGBT power module inside the VFD"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect mains power and wait 10 minutes for DC bus discharge, then disconnect motor cables from drive output terminals (U, V, W) and inspect for charred insulation or loose strands shorting between phases"
  - "With motor disconnected, reconnect mains and attempt to run drive unloaded to see if Alarm 16 clears (indicating external fault) or persists (indicating internal VFD fault)"
part_price: "$300-800"
---

## Danfoss FC302 AL-116 Fault — What It Means

There is no official Danfoss FC302 fault code labeled AL-116. If your display shows AL 16, that is Alarm 16, which means the drive detected a catastrophic short circuit current flowing between two output phases or from phase to ground on the motor output side. This typically signals a failed IGBT module inside the drive (where the semiconductor junctions have shorted internally) or a phase-to-phase short in the motor cable or motor windings. If your display shows AL 13, that is Alarm 13 for DC undervoltage (DC bus voltage dropped below the threshold, usually under 200V). Confirm the exact code from your drive's display before troubleshooting.

Assuming Alarm 16 (short circuit), the drive has shut down to protect itself from destructive current. The short can be internal (within the VFD power electronics) or external (in the motor cable or motor). Isolation testing will determine which side is at fault.

## Before You Replace Anything

Technicians sometimes replace the entire motor when the actual fault is a shorted IGBT module in the drive or a damaged motor cable. Always isolate the motor from the drive and test each side independently with a megohmmeter before committing to an expensive motor replacement.

[Jump to Fix](#fix)

## Common Causes

- **Failed IGBT module (~50%)** Semiconductor junctions in the inverter power module break down and short internally, creating a direct path across the DC bus.
- **Phase-to-phase short in motor cable (~25%)** Damaged cable insulation, loose splices, or water ingress causes two output phases to contact each other.
- **Shorted motor windings (~15%)** Internal motor fault where windings short phase-to-phase or phase-to-ground due to insulation breakdown.
- **Overlong motor cable without LC filter (~5%)** Excessive cable length generates voltage spikes that stress IGBTs and can trigger or cause shorts over time.
- **Blocked ventilation or overheating (~5%)** Dirty cooling fans or high ambient temperature degrade IGBT junctions and increase risk of short-circuit failure.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does Alarm 16 clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The short is external (motor cable or motor windings). Inspect cable for damage and test motor windings with a megohmmeter.<br><strong>No:</strong> The short is internal to the VFD. Inspect the power board for burnt IGBTs, charred traces, or exploded capacitors and prepare to replace the IGBT module or power board.</div>
</details>

<details class="dtree"><summary>Do you see visible burn marks, melted plastic, or smell burnt electronics on the VFD power board?</summary>
<div class="dtree-body"><strong>Yes:</strong> The IGBT module or rectifier has failed catastrophically. Replace the damaged power assembly and inspect for root causes (overheating, overload, cable length).<br><strong>No:</strong> The short may be intermittent or the damage is not visible. Test IGBT junctions with a multimeter in diode mode or replace the IGBT module as a unit.</div>
</details>

<details class="dtree"><summary>Does the motor cable pass a 500V megohmmeter test with &gt;10 MΩ phase-to-phase and phase-to-ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The cable is intact. The fault is in the motor windings or the VFD itself. Test motor windings next.<br><strong>No:</strong> The cable insulation has failed. Replace the motor cable and retest before reconnecting to the drive.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect mains power** and lock out the circuit breaker. Wait at least 10 minutes for the DC bus capacitors to discharge fully before opening the VFD enclosure or touching any terminals.
2. **Disconnect motor cables** from drive output terminals U, V, and W. Inspect cable ends for charred insulation, stray wire strands, or signs of arcing between phases.
3. **Reconnect mains power** (with motor still disconnected) and attempt to run the drive unloaded. If Alarm 16 persists, the fault is internal to the VFD. If Alarm 16 clears, the fault is external (motor or cable).
4. **Test motor cable and motor windings** using a 500V to 1000V megohmmeter. Measure phase-to-phase and phase-to-ground resistance. Readings should exceed 10 MΩ. Measure phase-to-phase winding resistance with a low-ohm meter and confirm all three readings are balanced within 5 percent.
5. **If external fault is confirmed**, replace the damaged motor cable or motor. If internal fault is confirmed, remove the VFD cover and inspect the power board for burnt IGBTs, charred circuit traces, or exploded DC link capacitors.
6. **Replace the IGBT power module or inverter board** as a complete assembly if internal damage is found. Consult your drive's service manual for part numbers and torque specifications for bus bar connections.
7. **After repair**, verify cooling airflow paths are clear, clean any dust from heat sinks and fans, and confirm ambient temperature is within the drive's rating before returning to service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT power module or inverter board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-116-fault-code&k=Danfoss+FC302+IGBT+power+module+or+inverter+board+assembly&tag=errorcodefixes-20) \| Match part number to your drive's frame size and voltage rating. Often sold as a complete power card. |
| Shielded motor cable (VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-116-fault-code&k=Shielded+motor+cable+%28VFD-rated%29&tag=errorcodefixes-20) \| Use cable rated for VFD output with symmetrical construction to reduce common-mode noise and voltage spikes. |

## When to Call a Pro

Call a qualified industrial electrician or drive service technician if you see Alarm 16. This fault involves high-voltage DC bus circuits (up to 650V or more) and requires specialized test equipment (megohmmeters, diode-mode multimeters, and oscilloscopes) to isolate the fault safely. Replacing IGBT modules demands correct torque on bus bar connections, thermal compound application, and verification of gate driver circuits. Mishandling can destroy a new power module instantly or create a fire hazard. A technician will also check for root causes such as overload conditions, incorrect parameter settings, or inadequate cooling that led to the original failure.

**Rough cost:** A pro service call runs about $400-1200.

## See Also

- [Danfoss FC302 Alarm 38 - Causes & Fix](/posts/danfoss-fc302-alarm-38-fault-code/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-32-fault-code/)
- [Danfoss FC302 Alarm 74 - Causes & Fix](/posts/danfoss-fc302-vfd-al-74-fault-code/)
- [Danfoss FC302 ALARM 28 - Causes & Fix](/posts/danfoss-fc302-alarm-28-fault-code/)
