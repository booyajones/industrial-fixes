---
title: "Danfoss FC302 AL-132 Fault - Causes & Fix"
description: "AL-132 (Overcurrent) means output current exceeded 150-160% of rated capacity. Most common fix: check for mechanical overload or loose motor wiring."
pubDatetime: 2026-06-25T09:20:52Z
modDatetime: 2026-06-25T09:20:52Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 IGBT power module"
most_likely_cause: "Mechanical overload on the motor shaft"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify Parameter 1-24 (Nominal Motor Current) matches the motor nameplate data"
  - "Inspect and tighten all motor cable connections at both drive and motor terminals"
  - "Check for mechanical binding by manually rotating the motor shaft with power off"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-132 Fault — What It Means

The AL-132 fault (also displayed as AL 13 or Err 13) indicates an overcurrent condition where the drive detected output current exceeding safe operating thresholds, typically reaching 150 to 160% of the nominal current for several seconds. Unlike an instantaneous short circuit, this fault accumulates over time as current gradually builds beyond the drive's rated capacity. This is a thermal and overload protection mechanism designed to prevent damage to the drive's IGBT modules and power components. The drive monitors current continuously and trips when the sustained overload exceeds approximately 1.5 to 1.6 times the drive's nominal rated current.

## Before You Replace Anything

Technicians often replace IGBT modules or the entire drive without first checking motor insulation resistance and mechanical load. A simple megohm test (readings below 2 MΩ indicate motor winding failure) and a manual shaft rotation test can identify the real cause before spending money on drive components.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload (~35%)** Excessive torque required on the motor shaft from jammed pumps, seized bearings, heavy conveyors, or binding equipment forces the drive to draw excessive current trying to maintain speed.
- **Motor winding insulation failure (~25%)** Moisture, contamination, or thermal aging causes partial shorts in motor windings, and megohm readings below 2 MΩ to ground indicate insulation breakdown.
- **Loose motor wiring or connections (~20%)** Loose terminals between drive and motor create resistance and arcing, causing current spikes and false overcurrent readings.
- **Incorrect motor parameters (~10%)** Nominal motor current setting in Parameter 1-24 does not match the actual motor data sheet, causing the drive to misjudge the overload limit.
- **Failing IGBT modules (~7%)** Aging or damaged IGBT transistors in the inverter section lose regulation ability and cannot properly control output current.
- **Faulty current sensor circuit (~3%)** The current shunt or sensor on the power board misreports actual current, triggering false overcurrent faults even under normal load.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is external to the drive. Focus on motor windings, cable connections, and mechanical load. Proceed to motor insulation testing.<br><strong>No:</strong> The fault is internal to the drive. Check IGBT modules, current sensor circuits, rectifier health, and input power balance before replacing the drive.</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical load is not the issue. Test motor winding insulation with a megohm meter and check all cable connections.<br><strong>No:</strong> Mechanical binding or seized bearings are forcing the drive into overcurrent. Inspect the driven equipment and motor bearings for physical obstruction.</div>
</details>

<details class="dtree"><summary>Is the megohm test reading above 2 MΩ from each motor winding to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation is acceptable. Verify drive parameter settings (especially 1-24) and inspect cable connections for corrosion or looseness.<br><strong>No:</strong> Motor windings have insulation failure from moisture or aging. The motor needs drying, rewinding, or replacement depending on severity.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the disconnect switch. Wait for the DC bus capacitors to fully discharge (check the display is completely blank).
2. **Disconnect the motor leads** from the drive's U, V, W output terminals. Label each wire before removal.
3. **Restart the drive unloaded** and attempt to run it without the motor connected. If AL-132 persists, the fault is internal (IGBT failure, current sensor, or rectifier problem). If the fault clears, proceed to motor and load testing.
4. **Perform a megohm test** on the motor windings to ground using an insulation resistance tester. Readings below 2 MΩ indicate insulation failure requiring motor service or replacement.
5. **Inspect all motor cable connections** at both the drive output terminals and the motor terminal box. Tighten all connections and look for corrosion, arcing marks, or damaged insulation.
6. **Verify Parameter 1-24** (Nominal Motor Current) against the motor nameplate. Enter the exact motor current rating. Also check Parameters 1-20 through 1-25 to confirm all motor data is correct.
7. **Check for mechanical overload** by manually rotating the motor shaft with power off. Inspect the driven equipment (pump, fan, conveyor) for jammed components, seized bearings, or excessive resistance.
8. **Test input power balance** using a multimeter. Verify all three phases are within 3% of nominal voltage. Imbalanced mains can cause rectifier stress and false overcurrent trips.
9. **Inspect drive cooling** by checking that all internal and external fans are running. Loss of cooling leads to overheating and can trigger overcurrent protection as a secondary effect.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 IGBT power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-132-fault-code&k=Danfoss+FC302+IGBT+power+module&tag=errorcodefixes-20) \| Required only if internal testing confirms IGBT failure after ruling out motor and load issues. |
| Motor cable assembly with proper shielding | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-132-fault-code&k=Motor+cable+assembly+with+proper+shielding&tag=errorcodefixes-20) \| Use VFD-rated cable with correct gauge for the motor current and cable length to minimize voltage spikes. |

## When to Call a Pro

Call a qualified motor drive technician or electrician for this fault. Diagnosing AL-132 requires high-voltage electrical knowledge, insulation resistance testing equipment, and familiarity with VFD parameter programming. If the fault persists after motor disconnection, internal drive repair demands safe DC bus discharge procedures and component-level troubleshooting of IGBT modules and current sensors. Motor winding failures also require professional evaluation to determine whether drying, rewinding, or replacement is the most cost-effective solution. Input power issues may involve upstream electrical panels and require licensed electrical work.

**Rough cost:** A pro service call runs about $200-600 depending on whether the fix is motor wiring, drive settings, or hardware replacement.
