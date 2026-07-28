---
title: "Danfoss FC302 VFD Alarm 16 - Causes & Fix"
description: "Alarm 16 (often misread as AL-161) means instantaneous overcurrent/short circuit. Most common fix: replace failed IGBT power module."
pubDatetime: 2026-06-26T09:53:06Z
modDatetime: 2026-06-26T09:53:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "IGBT Power Module (FC302)"
most_likely_cause: "IGBT module failure (semiconductor junction breakdown)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive and visually inspect the power section and heatsink for scorch marks, burning smells, or visible damage"
  - "Check all motor cable connections and tighten loose terminals at the drive output (U, V, W) and motor terminal box"
part_price: "$250-800"
---

## What this code means
The Danfoss FC302 does not have an 'AL-161' fault code. You are likely seeing Alarm 16, which the drive identifies as 'Overcurrent (Instantaneous)' or catastrophic short circuit. This is the most severe overcurrent condition where the drive detects output current exceeding safe thresholds by a catastrophic margin, typically caused by a phase-to-phase short or direct IGBT module failure creating a short across the DC bus. The drive's internal protection acts within microseconds to prevent damage to surrounding components, but the affected semiconductor junctions have already broken down.

Alarm 16 is an instantaneous trip that happens so fast the drive usually survives, but the root cause is almost always a hard failure inside the power section or a dead short in the motor circuit. Do not attempt to reset and run the drive multiple times, as each attempt risks cascading damage to additional components.

## Before You Replace Anything

Many technicians replace the control board or DC link capacitors first. Always disconnect the motor and run the drive unloaded to isolate whether the fault is internal (IGBT failure) or external (motor/cable short) before ordering parts.

## Common Causes

- **IGBT power module failure (~60%)** The most common cause is internal failure of the drive's IGBT power semiconductors where the junctions have shorted out, creating a direct short across the DC bus.
- **Phase-to-phase short in motor cable or terminal box (~25%)** A hard short between motor wires (phase-to-phase) in the cable or inside the motor terminal box triggers instantaneous overcurrent, though the drive usually survives due to fast protection.
- **Motor winding insulation failure (~10%)** Motor windings with insulation resistance below 2 megohms create intermittent or hard shorts that appear as instantaneous overcurrent to the drive.
- **Incorrect motor nominal current parameter (~3%)** Parameter 1-24 (motor nominal current) set much higher than the actual motor rating can cause false detection, though this is less common for an instantaneous trip.
- **Excessively short ramp times (~2%)** Ramp Up or Ramp Down times (Parameters 3-41 and 3-42) set too short force current spikes during acceleration or deceleration that can appear as instantaneous faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you see scorch marks, smell burning, or see visible damage on the drive's power section or heatsink?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive has sustained internal component damage (likely IGBTs or DC link capacitors). The drive needs component-level repair or replacement by a qualified technician or Danfoss service center.<br><strong>No:</strong> Proceed to isolate whether the fault is internal or external by disconnecting the motor and running the drive unloaded.</div>
</details>

<details class="dtree"><summary>With the motor disconnected from the drive output terminals (U, V, W), does Alarm 16 clear when you power up the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is external (motor or cable). Perform a megohm test on the motor windings to ground and check for phase-to-phase shorts in the cable and terminal box.<br><strong>No:</strong> The fault is internal to the drive. The IGBT module, DC link capacitors, or current sensors have failed and require professional repair or board replacement.</div>
</details>

<details class="dtree"><summary>Does a megohm (insulation) test on the motor windings show resistance of 2 megohms or higher to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor insulation is acceptable. Check for loose connections, corroded terminals, or damaged cable insulation that could cause intermittent phase-to-phase shorts.<br><strong>No:</strong> The motor has insulation failure. The motor needs rewinding or replacement, as readings below 2 megohms indicate a fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Remove mains power immediately.** Do not attempt to reset and run the drive multiple times, as each attempt risks cascading damage to additional components.
2. **Perform a visual inspection** of the drive's power section and heatsink for scorch marks, burning smells, or visible damage. If visible damage exists, component-level repair is required.
3. **Disconnect the motor** by removing all motor wiring from the drive output terminals (U, V, W) to isolate whether the fault is internal or external.
4. **Run the drive unloaded** (no motor connected) and power it up. If Alarm 16 persists, the drive has an internal component failure (likely IGBTs or DC link caps) requiring professional repair or board replacement. If Alarm 16 clears, the fault is external (motor or cable).
5. **Test the motor** using a megohm (insulation) tester on the motor windings to ground. Readings below 2 megohms indicate insulation failure and require motor rewinding or replacement.
6. **Check for phase-to-phase shorts** using a continuity meter from drive output terminals to motor windings. Inspect all motor cable connections and terminal box for loose wires, corrosion, or damaged insulation.
7. **If the drive is faulty**, disassemble the drive to access the heatsink and power section. Test the IGBT modules and current sensors for shorts or open circuits. Replace failed components or send the drive to a Danfoss service center for repair.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IGBT Power Module (FC302) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-161-fault-code&k=IGBT+Power+Module+%28FC302%29&tag=errorcodefixes-20) \| Match to your exact FC302 frame size and voltage rating, consult Danfoss part numbers for your model |
| DC Link Capacitor Bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-161-fault-code&k=DC+Link+Capacitor+Bank&tag=errorcodefixes-20) \| Order capacitors rated for your drive's DC bus voltage, typically paired with IGBT replacement |
| Current Sensor (Hall Effect) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-161-fault-code&k=Current+Sensor+%28Hall+Effect%29&tag=errorcodefixes-20) \| Replace if testing shows open or shorted sensor, verify model compatibility |

## When to Call a Pro

Call a professional immediately if you see visible damage to the drive, if Alarm 16 persists with the motor disconnected, or if you lack experience testing and replacing IGBT modules and high-voltage DC components. VFD repair involves working with DC bus voltages exceeding 600 VDC and requires specialized test equipment (megohm testers, IGBT testers, oscilloscopes) and knowledge of power electronics. If the motor fails the megohm test (below 2 megohms), a motor shop or electrician should rewind or replace the motor. Danfoss service centers can perform board-level repair and component replacement with genuine parts and warranty the work.

**Rough cost:** A pro service call runs about $400-1200.
