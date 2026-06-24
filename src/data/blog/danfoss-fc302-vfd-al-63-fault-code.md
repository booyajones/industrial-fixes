---
title: "Danfoss FC302 AL-63 Fault - Causes & Fix"
description: "AL-63 (Mechanical brake low) means motor current did not reach brake-release threshold. Most common fix: adjust brake current setting."
pubDatetime: 2026-06-22T10:17:13Z
modDatetime: 2026-06-22T10:17:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor mechanical brake assembly"
most_likely_cause: "Brake release current parameter set too high"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify terminal 37 to terminal 12 wiring is intact and brake coil is receiving 24V DC"
  - "Review parameter 1-20 and reduce brake-release current to 10-15% of motor rated current"
  - "Power cycle the drive by disconnecting AC mains until display turns off, then reconnect"
part_price: "$80-180 for a typical motor brake assembly"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-63 Fault — What It Means

Alarm 63 on the Danfoss FC302 VFD is labeled "Mechanical brake low." It occurs when the drive sends a command to release the mechanical brake (typically through terminal 37), but the actual motor current stays below the programmed brake-release current threshold set in parameter 1-20 or parameters 2-11/2-12. This indicates the brake did not open, the motor cannot move, or the load is too light to build enough current when the brake is supposed to release.

The fault does not indicate a DC bus problem or general IGBT failure. It specifically relates to the interaction between the brake release circuit and the motor load. The drive expects to see a current rise when the brake opens and the motor tries to turn. When that current never appears, AL-63 triggers.

## Before You Replace Anything

Technicians sometimes replace the power module thinking an IGBT has failed, when the real problem is a stuck brake or incorrect parameter setting. Check brake wiring continuity and parameter 1-20 before ordering inverter parts.

[Jump to Fix](#fix)

## Common Causes

- **Brake current threshold too high (~35%)** Parameter 1-20 or 2-11/2-12 is set above the current the motor actually draws, so the drive never detects brake release.
- **Mechanical brake stuck or failed (~30%)** Brake solenoid coil is open, brake shoes are seized, or no 24V DC reaches the brake coil to energize it.
- **Brake control wiring fault (~20%)** Terminal 37 is not connected to terminal 12 (24V supply), or there is an open circuit in the wiring to the brake.
- **Motor winding or connection problem (~10%)** Motor has an open phase, damaged windings, or is not connected, preventing normal current draw.
- **Drive output phase missing (~5%)** One IGBT leg has failed, so the drive cannot deliver balanced three-phase current and the motor never reaches brake-release current.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the brake coil measure correct resistance (typically 100-500 ohms) and is 24V DC present at the brake terminals when the drive runs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The brake coil is intact and powered. Check parameter 1-20 and reduce the brake-release current setting to 10-15% of motor rated current, then test again.<br><strong>No:</strong> The brake is not being energized. Trace wiring from terminal 37 to terminal 12 and repair any open circuit, or replace the brake assembly if the coil is open.</div>
</details>

<details class="dtree"><summary>With the motor disconnected from the load, does the alarm clear when you run the drive at low speed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The load is too light or mechanically stuck. Inspect the load for binding or adjust the brake-release current parameter lower.<br><strong>No:</strong> The motor or drive output is faulty. Measure motor phase resistance (should be balanced and typically under 10 ohms for a 4kW motor) and check three-phase output current balance with a clamp meter.</div>
</details>

<details class="dtree"><summary>Are all three motor phase currents balanced within a few percent of each other when the drive runs unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive output is healthy. Focus on the brake circuit wiring and parameter settings.<br><strong>No:</strong> One phase is missing or low, indicating a failed IGBT in that leg. Replace the inverter power module.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the drive** and lock out AC mains before touching any wiring.
2. **Check brake control wiring** by verifying continuity between terminal 37 and terminal 12 (24V supply). Measure brake coil resistance (typically 100-500 ohms) and confirm no open circuit.
3. **Review parameter 1-20** (Brake release current) and reduce it to approximately 10-15% of the motor's rated current if it is set too high.
4. **Disconnect the motor from the load** and run the drive unloaded at low speed. If AL-63 clears, the load is too light or mechanically stuck. Inspect the mechanical system.
5. **Measure motor phase resistance** between all three terminals. Resistance should be balanced and typically under 10 ohms for a 4kW motor. An open or very high reading indicates damaged motor windings.
6. **Use a clamp meter** to check three-phase output current balance while the drive runs. All phases should be within 3% of each other. A missing or low phase points to a failed IGBT in the inverter module.
7. **Power cycle the drive** by disconnecting AC mains, waiting until the display turns off, then reconnecting and resetting the alarm to test your repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor mechanical brake assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-63-fault-code&k=Motor+mechanical+brake+assembly&tag=errorcodefixes-20) \| Match voltage (typically 24V DC) and mounting flange to your motor model. |
| Danfoss FC302 inverter power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-63-fault-code&k=Danfoss+FC302+inverter+power+module&tag=errorcodefixes-20) \| Required only if IGBT output tests show a failed leg. Confirm module part number from drive nameplate. |

## When to Call a Pro

Call a qualified drives technician if you are not trained to work on high-voltage equipment or to interpret VFD parameters. The FC302 operates at DC link voltages around 325V (on 230V input) or 650V (on 480V input), and incorrect testing can destroy the drive or cause electric shock. A pro should also handle inverter module replacement, motor winding tests, and any repair that requires opening the drive enclosure. If basic wiring checks and parameter adjustments do not clear the alarm, a technician with a clamp meter and insulation tester can isolate whether the fault is in the brake, the motor, or the drive output stage.

**Rough cost:** A pro service call runs about $150-400 depending on whether it is a wiring repair, brake replacement, or inverter module.

## See Also

- [Danfoss FC302 Alarm 48 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-48-fault-code/)
- [Danfoss FC302 ALARM 26 - Causes & Fix](/posts/danfoss-fc302-alarm-26-fault-code/)
- [Danfoss FC302 Alarm 25 - Causes & Fix](/posts/danfoss-fc302-alarm-25-fault-code/)
- [Danfoss FC302 VFD Alarm 44 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-44-fault-code/)
