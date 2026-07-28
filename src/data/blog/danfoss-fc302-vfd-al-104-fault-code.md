---
title: "Danfoss FC302 AL-104 - Causes & Fix"
description: "AL-104 means the internal mixing fan is not spinning. Most often the fan motor has failed. Check for dust blockage first, then replace the fan."
pubDatetime: 2026-06-23T10:20:40Z
modDatetime: 2026-06-23T10:20:40Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 cooling fan (mixing fan)"
most_likely_cause: "Failed fan motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power off the drive, remove the cover, and inspect the fan for dust, debris, or physical obstruction blocking the blades or heatsink"
  - "Check that the drive's air vents are not clogged and that the ambient temperature is within -10°C to +50°C"
  - "Power on the drive and visually observe whether the fan attempts to spin at startup"
part_price: "$40-120"
no_buy_pct: "30%"
---

## What this code means
The AL-104 fault code on a Danfoss FC302 VFD indicates a Mixing Fan Fault. The drive's fan monitor circuit has detected that the internal cooling fan is not spinning at power-up or when commanded to turn on. This is a protective trip to prevent the drive from overheating due to inadequate cooling.

The drive will not operate until the fan fault is cleared. The fault can be caused by a dead fan motor, mechanical blockage from dust or debris, a failed fan drive circuit on the control board, or ambient temperatures exceeding the drive's operating range.

## Before You Replace Anything

Technicians sometimes replace the control board or power board before testing the fan itself. Measure voltage at the fan terminals with a voltmeter while the drive is powered to confirm whether the fan motor is dead or the board circuit has failed.

## Common Causes

- **Failed fan motor (~45%)** The fan motor windings have burned out or opened, preventing the fan from spinning even when voltage is applied.
- **Dust or debris blockage (~25%)** The fan blades, heatsink, or air vents are clogged with dust and debris, creating mechanical resistance that stops the fan from turning.
- **Faulty fan drive circuit on power or control board (~20%)** The wiring or circuit that supplies power to the fan has failed, so the fan receives no voltage even though it is mechanically sound.
- **Excessive ambient temperature (~10%)** The drive is operating in an environment above its rated temperature range, causing the fan to seize or the drive to trip before the fan can cool it.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fan spin freely when you turn it by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan motor or electrical circuit is likely faulty. Measure voltage at the fan terminals when powered on.<br><strong>No:</strong> The fan is blocked by dust, debris, or a damaged bearing. Clean the heatsink and vents thoroughly.</div>
</details>

<details class="dtree"><summary>Is voltage present at the fan terminals when the drive is powered on (typically 24V DC)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan motor is dead and needs replacement. Order a new mixing fan.<br><strong>No:</strong> The fan drive circuit on the control or power board has failed. Replace the board.</div>
</details>

<details class="dtree"><summary>Is the drive installed in a location with poor ventilation or high ambient heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> Relocate the drive to a cooler area or add external cooling to keep ambient temperature within -10°C to +50°C.<br><strong>No:</strong> The fault is mechanical or electrical. Focus on fan replacement or board repair.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off and lock out** the drive. Remove the front cover to access the internal cooling fan and heatsink.
2. **Inspect the fan and heatsink** for dust, debris, or physical obstruction. Clean thoroughly with compressed air or a brush if clogged.
3. **Check the ambient environment** to confirm the drive is operating within -10°C to +50°C and has adequate ventilation around the air vents.
4. **Power on the drive** and immediately observe whether the fan spins at startup. If it does not, proceed to electrical testing.
5. **Measure fan voltage** at the fan terminals using a voltmeter while the drive is powered (typically 24V DC). If voltage is present but the fan does not spin, the fan motor is faulty. If no voltage is present, the control or power board is defective.
6. **Replace the mixing fan** if the motor is dead, or replace the power board if the fan drive circuit has failed.
7. **Reassemble the drive** and power it on to verify the fault clears and the fan operates normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 cooling fan (mixing fan) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-104-fault-code&k=Danfoss+FC302+cooling+fan+%28mixing+fan%29&tag=errorcodefixes-20) \| Verify the voltage rating (typically 24V DC) and mounting configuration for your specific FC302 model. |
| Danfoss FC302 power board (rectifier and inverter assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-104-fault-code&k=Danfoss+FC302+power+board+%28rectifier+and+inverter+assembly%29&tag=errorcodefixes-20) \| Required if the fan drive circuit on the board is defective and no voltage reaches the fan. |
| Danfoss FC302 control PCB (I/O board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-104-fault-code&k=Danfoss+FC302+control+PCB+%28I%2FO+board%29&tag=errorcodefixes-20) \| May be needed if the fan control signal originates here and the circuit is faulty. |

## When to Call a Pro

Call a qualified technician for any VFD repair. The FC302 operates at high voltage and current, and opening the drive enclosure exposes you to lethal electrical hazards even after power is removed due to charged capacitors. A technician has the tools to safely discharge the DC bus, measure fan circuits under power, and replace internal components without damaging the drive or risking electrocution. If you lack electrical training or do not have lockout/tagout procedures in place, do not attempt this repair yourself.

**Rough cost:** A pro service call runs about $200-500.
