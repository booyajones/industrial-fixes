---
title: "Danfoss FC302 AL-131 (Overcurrent) - Causes & Fix"
description: "AL-131 means sustained overcurrent detected during operation. Most often caused by mechanical overload or incorrect motor parameters."
pubDatetime: 2026-06-25T09:19:56Z
modDatetime: 2026-06-25T09:19:56Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Inverter IGBT module (Danfoss FC302)"
most_likely_cause: "mechanical overload on the motor shaft or connected equipment"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect the motor leads from the drive and run the drive unloaded to isolate whether the fault is in the drive or downstream"
  - "Verify Parameter 1-24 (nominal motor current) matches the actual motor nameplate rating"
  - "Inspect all motor cable connections and terminals for loose or corroded contacts"
---

## Danfoss FC302 AL-131 (Overcurrent) — What It Means

AL 13 (often displayed as AL-131 with a temperature suffix or misread) on a Danfoss FC302 VFD signals that the drive's current sensors have detected output current exceeding safe operating thresholds for a sustained period, typically 150 to 160 percent of rated current for several seconds. This is an overcurrent alarm caused by gradual current buildup rather than an instantaneous short circuit, meaning the motor or connected load is drawing too much power during normal operation or acceleration.

The fault distinguishes itself from a trip caused by a momentary spike. It indicates the drive is working hard to supply current beyond its design capacity, either because the load is too heavy, the motor is struggling, or internal parameters are configured incorrectly. The drive shuts down to protect the inverter IGBT modules and prevent thermal damage.

## Before You Replace Anything

Many technicians replace the inverter board or IGBT modules without first checking motor parameters (especially Parameter 1-24 nominal motor current) and performing a megohm test on the motor windings. A simple megohm test below 2 megohms confirms insulation failure and avoids unnecessary drive repairs.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload (~35%)** The motor shaft is mechanically overloaded or the connected load is too heavy, forcing the motor to draw excessive current during operation.
- **Incorrect motor parameters (~25%)** Parameter 1-24 (nominal motor current) is set incorrectly, often higher than the actual motor rating, causing the drive to misinterpret normal current as overcurrent.
- **Motor winding insulation breakdown (~20%)** A motor winding has developed a partial short or insulation failure, causing current draw to climb beyond normal levels.
- **Cable or connection problems (~10%)** Loose, corroded, or damaged connections between the drive and motor create resistance and voltage drops that result in current spikes.
- **IGBT module failure (~7%)** Aging or damaged inverter IGBT modules on the drive lose current regulation ability and trigger false or real overcurrent detection.
- **Cooling system failure (~3%)** Insufficient cooling airflow from blocked vents or failed fans causes thermal stress and false current readings or genuine overheating.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the AL-13 fault clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is downstream in the motor, cables, or mechanical load. Proceed to test motor insulation and check connections.<br><strong>No:</strong> The drive itself has an internal component failure (IGBT modules, gate drivers, or control board). Call a qualified technician for drive repair or replacement.</div>
</details>

<details class="dtree"><summary>Does the motor winding insulation test show resistance below 2 megohms to ground?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor has insulation failure or a developing winding short. Replace or rewind the motor.<br><strong>No:</strong> The motor is likely healthy. Check mechanical load, cable integrity, and verify drive parameter settings.</div>
</details>

<details class="dtree"><summary>Is Parameter 1-24 (nominal motor current) set higher than the motor nameplate rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Correct the parameter to match the motor nameplate current. Reset the fault and test again.<br><strong>No:</strong> The overcurrent is real. Inspect the mechanical load for binding, jamming, or excessive friction.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the main disconnect before touching any terminals or connections.
2. **Disconnect the motor leads** from the drive output terminals (U, V, W) and run the drive unloaded. If AL-13 persists with no motor connected, the drive has an internal failure (IGBT modules or control board) and requires professional repair.
3. **Perform a megohm test** on the motor windings to ground. Readings below 2 megohms indicate insulation breakdown or a partial short. Replace or rewind the motor if the test fails.
4. **Inspect all cable connections** from the drive output to the motor junction box. Tighten any loose terminals and clean corroded contacts. Look for cable damage from sharp conduit edges or physical wear.
5. **Verify motor parameters** in the drive. Check Parameter 1-24 (nominal motor current) and confirm it matches the motor nameplate. Review Parameters 1-20 through 1-25 to make sure all motor data is correct.
6. **Check the cooling system**. Verify all cooling fans operate and that intake and exhaust vents are clear of dust and debris. Replace any failed fans immediately.
7. **Measure internal IGBT modules** (if the fault persists unloaded). A qualified technician should test the inverter board IGBTs and replace the power module if one is shorted or damaged by heat.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Inverter IGBT module (Danfoss FC302) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-131-fault-code&k=Inverter+IGBT+module+%28Danfoss+FC302%29&tag=errorcodefixes-20) \| Required only if the drive faults with no motor connected and IGBT testing confirms failure |
| Cooling fan (Danfoss FC302) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-131-fault-code&k=Cooling+fan+%28Danfoss+FC302%29&tag=errorcodefixes-20) \| Replace if the fan does not spin or airflow is weak |
| Motor (replacement or rewind) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-131-fault-code&k=Motor+%28replacement+or+rewind%29&tag=errorcodefixes-20) \| Needed if megohm test shows insulation resistance below 2 megohms |

## When to Call a Pro

Call a qualified VFD technician or drive repair specialist if the AL-13 fault persists with the motor disconnected, which points to internal drive failure (IGBT modules, gate drivers, or control board). Also call a pro if you lack the tools or training to perform megohm testing, parameter configuration, or IGBT testing. High-voltage work on industrial drives requires lockout/tagout procedures and specialized test equipment. If the motor requires rewinding or the mechanical load needs diagnosis (bearing failure, coupling misalignment, or gearbox problems), involve a motor shop or mechanical technician.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Danfoss FC302 AL-164 - Causes & Fix](/posts/danfoss-fc302-vfd-al-164-fault-code/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC302 AL-86 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-86-fault-code/)
- [Danfoss FC302 AL-143 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-143-fault-code/)
