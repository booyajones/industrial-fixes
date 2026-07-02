---
title: "Danfoss FC302 Alarm 13 - Causes & Fix"
description: "Alarm 13 (Inverter Fault/Overcurrent) means the drive sees sustained output current above 150-160% of nominal. Most often a jammed motor."
pubDatetime: 2026-06-25T09:25:00Z
modDatetime: 2026-06-25T09:25:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter IGBT module"
most_likely_cause: "Mechanical motor overload (jammed shaft, clogged pump, or stuck conveyor)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect motor cable from drive output terminals, power on, and run the drive unloaded to isolate whether the fault is internal to the drive or downstream in motor/cable"
  - "Inspect motor shaft and coupled load for mechanical binding, seized bearings, or obstructions (pump clogs, conveyor jams)"
  - "Verify Parameter 1-24 (Nominal Motor Current) matches the motor nameplate current rating"
---

## Danfoss FC302 Alarm 13 — What It Means

Alarm 13 (often displayed as AL 13 or Err 13, not AL-137) indicates Inverter Fault (Overcurrent) on the Danfoss FC302 drive. This fault trips when output current gradually builds beyond 150 to 160 percent of the drive's nominal rating for several seconds during acceleration or steady operation. Unlike instantaneous short-circuit faults (Alarm 16), Alarm 13 points to a sustained mechanical or thermal overload rather than a hard wiring failure.

The drive is protecting its IGBT modules from thermal damage caused by prolonged high current. Common triggers include a stuck motor shaft, clogged pump, conveyor jam, or degraded motor windings drawing excessive current. Less often, incorrect motor parameter settings (such as a low nominal-current entry in Parameter 1-24) cause the drive to misread normal current as an overload.

## Before You Replace Anything

Many technicians replace the inverter IGBT module or entire drive before checking whether the motor shaft is jammed or motor windings are shorted. Always perform a megohm test on motor windings and verify the load is free to rotate before replacing any drive components.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical motor overload (~40%)** The motor shaft is jammed, the pump is clogged, or the conveyor is stuck, forcing the motor to draw sustained high current that trips the drive.
- **Incorrect motor parameters (~25%)** Parameter 1-24 (Nominal Motor Current) is set too low, causing the drive to interpret normal current as an overload.
- **Degraded motor winding insulation (~15%)** Moisture, contamination, or thermal aging breaks down winding insulation, causing partial shorts that increase current draw.
- **Cable or connection faults (~10%)** Loose motor terminals, corroded connectors, or damaged cables create resistance spikes and current surges.
- **Failed IGBT modules (~7%)** Aging or damaged inverter IGBTs lose current regulation ability and trip on overcurrent even under normal load.
- **Failing DC bus capacitors (~3%)** Degraded or exploded DC link capacitors cause voltage spikes that manifest as overcurrent faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does Alarm 13 persist when you disconnect the motor cable and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive (IGBT modules, DC capacitors, or rectifier board). Call a qualified technician to test and replace drive components.<br><strong>No:</strong> The fault is downstream in the motor or cable. Proceed to test motor windings and inspect connections.</div>
</details>

<details class="dtree"><summary>Does the motor shaft rotate freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical binding is not the cause. Check motor winding insulation resistance and cable connections.<br><strong>No:</strong> The load is jammed or bearings are seized. Clear obstructions, repair the pump or conveyor, or replace motor bearings before re-energizing.</div>
</details>

<details class="dtree"><summary>Is Parameter 1-24 (Nominal Motor Current) set to match the motor nameplate current?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor parameters are correct. Perform a megohm test on motor windings to ground to rule out insulation failure.<br><strong>No:</strong> Increase Parameter 1-24 to the correct nameplate value and test again. An incorrect low setting will cause false overcurrent trips.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lockout** the drive, then disconnect the motor cable from the drive output terminals (U, V, W).
2. **Power on the drive** and attempt to run it unloaded (no motor connected). If Alarm 13 persists, the drive has an internal fault (IGBTs, DC capacitors, or rectifier). If Alarm 13 clears, the problem is in the motor or cable.
3. **Test motor winding insulation** using a megohm meter. Measure resistance from each motor winding to ground. Readings below 2 megohms indicate insulation failure and the motor requires repair or replacement.
4. **Inspect motor terminals and cables** for loose connections, corrosion, or physical damage (cuts, crimps, rodent chews). Repair or replace damaged cables and clean corroded terminals.
5. **Verify motor parameters** in the drive. Check that Parameter 1-24 (Nominal Motor Current) matches the motor nameplate current, and review Parameters 1-20 through 1-25 for correct motor data entry.
6. **Increase ramp times** if the motor draws high current during acceleration. Raise Parameters 3-41 (Ramp Up Time) and 3-42 (Ramp Down Time) to reduce starting current spikes.
7. **Inspect drive internals** if the isolated test showed internal fault. Check IGBT modules for shorts, DC bus capacitors for bulging or cracks, and cooling fans for proper operation. Replace failed components as needed.
8. **Clear the alarm** by pressing the reset button or cycling power, then run the drive under normal load to confirm the fault is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-137-fault-code&k=Danfoss+FC302+inverter+IGBT+module&tag=errorcodefixes-20) \| Match the exact module part number to your drive frame size and voltage rating |
| Danfoss FC302 DC link capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-137-fault-code&k=Danfoss+FC302+DC+link+capacitor+bank&tag=errorcodefixes-20) \| Replace all capacitors in the bank if one has failed, to prevent cascade failures |
| Shielded motor cable rated for VFD use | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-137-fault-code&k=Shielded+motor+cable+rated+for+VFD+use&tag=errorcodefixes-20) \| Use appropriate gauge and length for your motor current and installation distance |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if the motor-disconnected test shows the fault is internal to the drive, if you lack a megohm tester or cannot safely perform insulation tests, or if the alarm persists after you have verified motor parameters and cleared mechanical obstructions. Replacing IGBT modules, DC bus capacitors, or rectifier boards requires knowledge of high-voltage DC circuits (up to 800 VDC on the bus), proper electrostatic discharge precautions, and the ability to interpret drive diagnostic data. Also call a professional if motor winding insulation tests fail, because motor rewind or replacement often requires crane lifts, alignment, and coupling work beyond typical maintenance scope.

**Rough cost:** A pro service call runs about $200-800 depending on whether the fix is motor repair, cable replacement, or drive board replacement.

## See Also

- [Danfoss FC302 AL-97 - Causes & Fix](/posts/danfoss-fc302-vfd-al-97-fault-code/)
- [Danfoss FC302 AL-165 - Causes & Fix](/posts/danfoss-fc302-vfd-al-165-fault-code/)
- [Danfoss FC302 W66 - Causes & Fix](/posts/danfoss-fc302-vfd-al-66-fault-code/)
- [Danfoss FC302 AL-61 - Causes & Fix](/posts/danfoss-fc302-vfd-al-61-fault-code/)
