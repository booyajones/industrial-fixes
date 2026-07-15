---
title: "Danfoss FC302 AL-97 - Causes & Fix"
description: "AL-97 is not a valid Danfoss FC302 fault code. You likely saw ALARM 13 (overcurrent) or ALARM 38 (internal fault). Check the display again."
pubDatetime: 2026-06-23T10:15:17Z
modDatetime: 2026-06-23T10:15:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter board / power stack"
most_likely_cause: "motor winding partial short or insulation breakdown"
likelihood: "the most common cause when the actual code is ALARM 13"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm code on the drive display (not AL-97)"
  - "Check all motor cable connections at the drive output terminals and motor for looseness or corrosion"
  - "Review parameter 1-24 (Motor Nominal Current) to confirm it matches the motor nameplate rating"
part_price: "$400-1200 for inverter board or power stack"
---

## Danfoss FC302 AL-97 — What It Means

The code AL-97 does not exist in any official Danfoss FC302 documentation. Danfoss FC302 VFDs use alarm codes numbered AL 1 through AL 99, but AL-97 is not listed. The most commonly misreported codes that might be confused with AL-97 are ALARM 13 (overcurrent, which means output current exceeded the peak limit), ALARM 38 (internal fault with a sub-code), ALARM 39 (heat sink sensor fault), or ALARM 72 (control board failure). If you see a fault on your drive, verify the exact alarm number on the display panel. ALARM 13 is the most frequent real fault and indicates the drive output current went beyond its rated peak (typically 200% of nominal current for more than one second), pointing to a motor winding short, mechanical overload, loose connections, or damaged IGBT modules in the drive itself.

## Before You Replace Anything

Technicians often replace the entire inverter board or power stack before testing the motor windings. Disconnect the motor and run the drive unloaded first to isolate whether the fault is in the drive or the motor.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding partial short or insulation failure (~35%)** The insulation between motor windings breaks down (especially in older or overheated motors), causing phase-to-phase or phase-to-ground faults that trigger overcurrent protection.
- **Mechanical overload on the motor shaft (~25%)** A jammed pump, seized fan bearing, or blocked conveyor forces the motor to draw excessive current under load.
- **Loose or high-resistance connections (~15%)** Corroded, loose, or burned connections between the drive output terminals and motor create arcing or intermittent shorts that spike current.
- **Damaged IGBT modules on the inverter board (~15%)** Failed or partially shorted insulated-gate bipolar transistors in the drive power section cause internal faults and false overcurrent trips.
- **Incorrect motor parameter settings (~10%)** Parameter 1-24 (Motor Nominal Current) set higher than the actual motor rating causes the drive to deliver excess current before tripping.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show AL-97 or a different alarm number?</summary>
<div class="dtree-body"><strong>Yes:</strong> If the display clearly shows AL-97, power-cycle the drive and check again; if it persists, consult Danfoss technical support because AL-97 is not a documented code.<br><strong>No:</strong> Write down the exact alarm number (for example ALARM 13, ALARM 38) and proceed with the troubleshooting for that specific code.</div>
</details>

<details class="dtree"><summary>With the motor disconnected, does the drive run without faulting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor, motor cable, or mechanical load; proceed to megohm-test the motor windings and check for mechanical binding.<br><strong>No:</strong> The fault is inside the drive (IGBT modules, DC link, or control board); call a VFD technician to test the inverter section.</div>
</details>

<details class="dtree"><summary>Does a megohm test show motor winding insulation above 2 megohms phase-to-ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation is acceptable; check for loose connections, incorrect parameters, or mechanical overload.<br><strong>No:</strong> Motor insulation has failed; replace or rewind the motor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the main disconnect, then wait at least five minutes for capacitors to discharge before opening any panels.
2. **Verify the exact alarm code** on the VFD display panel; write down the alarm number and any sub-code (for example ALARM 38-XX).
3. **Disconnect the motor cables** from the drive output terminals (U, V, W) and attempt to run the drive unloaded; if the alarm clears, the fault is in the motor or cable.
4. **Perform a megohm test** on the motor windings using a 500 V or 1000 V insulation tester; measure resistance from each phase (U, V, W) to the motor frame ground (acceptable is 2 megohms or higher).
5. **Inspect all connections** at the drive output terminals and motor terminal box for looseness, corrosion, burned contacts, or damaged wire insulation.
6. **Check parameter 1-24** (Motor Nominal Current) in the drive menu and confirm it matches the motor nameplate rating; adjust if incorrect.
7. **Test the mechanical load** by rotating the motor shaft by hand (with power off) to verify it spins freely without binding or excessive resistance.
8. **If the drive still faults with no motor connected**, call a qualified VFD technician to test the IGBT modules and inverter board; internal drive faults require oscilloscope or specialized test equipment.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter board / power stack | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-97-fault-code&k=Danfoss+FC302+inverter+board+%2F+power+stack&tag=errorcodefixes-20) \| Order by exact drive frame size and voltage rating; includes IGBT modules and gate drivers. |
| Three-phase AC motor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-97-fault-code&k=Three-phase+AC+motor+%28replacement%29&tag=errorcodefixes-20) \| Match horsepower, voltage, frame size, and shaft configuration to the original motor nameplate. |

## When to Call a Pro

Call a VFD technician or industrial electrician if the drive faults with the motor disconnected, if you lack a megohmmeter or insulation tester, or if the alarm code is ALARM 38 or ALARM 72 (internal faults that require firmware diagnostics and component-level testing). Also call a pro if you find failed motor insulation but do not have the tools to safely replace or rewind the motor. High-voltage drive work (especially testing IGBT modules and DC bus capacitors) requires specialized training and equipment.

**Rough cost:** A pro service call runs about $300-800 for motor testing, winding repair, or inverter board replacement.

## See Also

- [Danfoss FC302 AL-141 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-141-fault-code/)
- [Danfoss FC302 Alarm 38 - Causes & Fix](/posts/danfoss-fc302-alarm-38-fault-code/)
- [Danfoss FC302 AL-148 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-148-fault-code/)
- [Danfoss FC302 AL-60 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-60-fault-code/)
