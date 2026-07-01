---
title: "Danfoss FC302 AL-130 Fault - Causes & Fix"
description: "AL-130 on a Danfoss FC302 VFD means DC bus undervoltage (below 200V). Most often caused by blown input fuse or failed rectifier diode."
pubDatetime: 2026-06-25T09:19:03Z
modDatetime: 2026-06-25T09:19:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Power Board (Rectifier + Inverter Assembly)"
most_likely_cause: "Blown input fuse or failed rectifier diode on the power board"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure all three incoming AC phases at the drive input terminals to confirm voltage is balanced within 3% and within the drive's rated range"
  - "Check facility breakers and disconnect switches for tripped or open circuits feeding the drive"
  - "Inspect input terminal connections for loose, corroded, or burned wiring that creates high resistance"
---

## Danfoss FC302 AL-130 Fault — What It Means

The AL-13 fault (also displayed as AL-130 or Err 13) on a Danfoss FC302 variable frequency drive indicates a DC undervoltage condition. The drive's internal DC bus voltage has dropped below the minimum operating threshold, typically less than 200V for 400V-class drives. This voltage collapse prevents the inverter from safely controlling the motor, so the drive shuts down to prevent damage.

The fault is triggered when the rectifier section (which converts incoming AC power to DC for the inverter) fails to maintain the required DC link voltage. This can result from insufficient incoming AC power, a failed rectifier component such as a diode or input fuse, an open circuit in the input wiring, or a shorted DC link capacitor. Unlike output overcurrent faults that build gradually, AL-13 represents an immediate voltage collapse in the DC bus.

## Before You Replace Anything

Technicians sometimes replace the entire inverter IGBT module when the real cause is a blown input fuse or single failed rectifier diode. Always test the input fuses and rectifier diodes with a multimeter before ordering expensive power boards.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuse or failed rectifier diode (~40%)** A blown fuse or open/shorted rectifier diode on the power board prevents the rectifier from converting incoming AC to DC, collapsing the bus voltage.
- **Loose or corroded input wiring connections (~25%)** High resistance at input terminals or internal connections starves the rectifier of AC power and causes voltage sags under load.
- **Incoming AC voltage sag or imbalance (~15%)** Voltage imbalance greater than 3% or momentary sags from other equipment starting up can drop the DC bus below threshold.
- **Failed DC link capacitor (~10%)** A shorted or leaking capacitor in the DC bus circuit drains voltage or creates instability that triggers the undervoltage fault.
- **Tripped breaker or open disconnect (~7%)** An open circuit upstream in the facility's distribution panel cuts power to one or more phases feeding the drive.
- **Failed inverter IGBT module (~3%)** A shorted IGBT can pull down the DC bus voltage, though this typically triggers an overcurrent fault before undervoltage appears.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Do you measure balanced voltage (within 3% on all three phases) at the drive input terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The incoming power is good. The fault is internal to the drive. Proceed to open the drive and test input fuses and rectifier diodes.<br><strong>No:</strong> The problem is upstream. Check facility breakers, disconnects, and wiring from the distribution panel to the drive for open circuits or loose connections.</div>
</details>

<details class="dtree"><summary>When you swap input wires at the drive terminals, does the low-current phase move with the wire?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue is external power supply (facility wiring or breaker). Trace the circuit back to find the weak phase or open connection.<br><strong>No:</strong> The drive's rectifier section is faulty. Replace the input fuse or rectifier board depending on which component tests bad.</div>
</details>

<details class="dtree"><summary>Do you see any bulging, leaking, or exploded capacitors inside the drive enclosure?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the DC link capacitors. A failed capacitor can cause voltage instability and trigger the AL-13 fault.<br><strong>No:</strong> Focus on the rectifier diodes and input fuses. Test each diode for open or shorted condition and replace the power board if defective.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Measure input voltage** at the drive terminals (L1, L2, L3) with a voltmeter to confirm all three phases are balanced within 3% and within the drive's rated voltage range (typically 400V ±10% for this model).
2. **Check current imbalance** using a clamp-on ammeter on each input phase. If one phase shows significantly lower current, swap the input wires at the drive and re-test to determine if the problem is external power or an internal rectifier fault.
3. **Inspect facility breakers and fuses** in the distribution panel and any disconnects feeding the drive to verify all contacts are closed and fuses are intact.
4. **Open the drive enclosure** and visually inspect the power board for blown input fuses, burned components, or bulging/leaking DC link capacitors.
5. **Test the input fuses** on the power board with a multimeter in continuity mode. Replace any blown fuses and re-energize to see if the fault clears.
6. **Measure rectifier diodes** using a multimeter in diode-test mode. Each diode should show forward voltage drop in one direction and open in the other. If a diode is open or shorted, replace the rectifier board or entire power assembly.
7. **Inspect DC link capacitors** for physical damage (swelling, leaking electrolyte, or explosion residue). Replace the capacitor bank if any capacitor shows signs of failure, and verify bus voltage returns to normal after replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Power Board (Rectifier + Inverter Assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-130-fault-code&k=Danfoss+FC302+Power+Board+%28Rectifier+%2B+Inverter+Assembly%29&tag=errorcodefixes-20) \| Consult your drive's model suffix and voltage rating to order the correct replacement board. |
| DC Link Capacitor Bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-130-fault-code&k=DC+Link+Capacitor+Bank&tag=errorcodefixes-20) \| Match the voltage and capacitance rating stamped on the original capacitors; typically used in 400V-class drives. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician for this repair. The fault involves diagnosing and replacing components on the high-voltage DC bus and rectifier section, which can store lethal voltage even after the drive is de-energized. Testing rectifier diodes and IGBTs requires specialized knowledge of power electronics and proper discharge procedures for the DC link capacitors. If you lack experience with VFD internals, multimeter testing of power semiconductors, or lockout/tagout procedures, hire a professional to avoid electric shock, arc flash, or incorrect part replacement that can damage the drive further.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Danfoss FC302 VFD AL-85 - Causes & Fix](/posts/danfoss-fc302-vfd-al-85-fault-code/)
- [Danfoss FC302 Alarm 24 - Causes & Fix](/posts/danfoss-fc302-alarm-24-fault-code/)
- [Danfoss FC302 AL-63 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-63-fault-code/)
- [Danfoss VFD Fault AL 14 — Causes & Fix](/posts/danfoss-vfd-fault-al-14/)
