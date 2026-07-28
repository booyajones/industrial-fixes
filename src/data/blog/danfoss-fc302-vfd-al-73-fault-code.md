---
title: "Danfoss FC302 WARNING 73 - Causes & Fix"
description: "WARNING 73 means Safe Stop is active but set to auto-restart. Most common: a safety door/guard is open or terminal 37 is shorted."
pubDatetime: 2026-06-22T10:25:14Z
modDatetime: 2026-06-22T10:25:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Safety door interlock switch (magnetic or mechanical)"
most_likely_cause: "Physical safety interlock (door, guard, or emergency stop) is engaged or wiring to terminal 37 is shorted"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check all safety doors, guards, and emergency stops to confirm they are fully closed and interlocks are not stuck"
  - "Measure voltage between terminal 37 and terminal 12 with a volt meter; if you see approximately 24V when the safety device should be open, the circuit is shorted or the device is stuck"
  - "Review parameter 5-12 (Terminal 27 Digital Input) to confirm it is set to 'No function' if that input is not in use"
part_price: "$40-80 for a replacement safety door switch or interlock sensor"
no_buy_pct: "65%"
---

## What this code means
WARNING 73 on the Danfoss FC302 means the drive has detected activation of the Safe Stop (STO) function, typically through terminal 37 or terminal 27. Because parameter 5-10 is configured for 'Auto restart,' the drive does not trip or fault. Instead it waits in a ready state. Once the Safe Stop signal clears (the interlock opens or the terminal is disconnected), the motor will automatically resume running at its previous speed without needing a manual reset.

This is different from an alarm code. The drive remains powered and operational, simply waiting for the Safe Stop condition to be removed. The warning will persist as long as the Safe Stop input sees an active signal, which could be from a physical safety device, a wiring fault, or an incorrect parameter setting.

## Before You Replace Anything

Technicians sometimes replace the control card thinking the input is latched, but a simple voltage measurement at terminal 37 will show whether a physical interlock or wiring short is holding the signal active.

## Common Causes

- **Safety door or guard is open or stuck (~45%)** A physical safety interlock (door switch, guard magnet, or emergency stop button) is engaged, sending a Safe Stop signal to terminal 37 or 27.
- **Shorted or damaged control wiring to terminal 37 (~30%)** A wire connecting terminal 37 to terminal 12 (24V) is shorted or pinched, creating a continuous Safe Stop signal even when the interlock should be open.
- **Jumper wire installed during testing (~10%)** A technician placed a temporary jumper between terminal 37 and terminal 12 to bypass an interlock during troubleshooting and forgot to remove it.
- **Parameter 5-12 misconfigured (~10%)** Terminal 27 Digital Input is set to an active Safe Stop function instead of 'No function,' causing the drive to see a constant Safe Stop signal.
- **Faulty safety switch or sensor (~5%)** The physical interlock switch or magnetic sensor has failed in the closed (active) position, holding the Safe Stop signal even when the door is fully closed.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all safety doors, guards, and emergency stops fully closed and latched?</summary>
<div class="dtree-body"><strong>Yes:</strong> The interlock hardware is positioned correctly. Proceed to check wiring and parameter settings.<br><strong>No:</strong> Close or latch the open safety device. If the warning clears, the interlock was simply engaged. If it persists, the switch or sensor may be faulty.</div>
</details>

<details class="dtree"><summary>Do you measure approximately 24V between terminal 37 and terminal 12 when the safety device is open?</summary>
<div class="dtree-body"><strong>Yes:</strong> The circuit is shorted or the safety switch is stuck closed. Inspect wiring for shorts and test the switch continuity.<br><strong>No:</strong> The wiring and switch are not holding the signal active. Check parameter 5-12 and terminal 27 configuration.</div>
</details>

<details class="dtree"><summary>Is parameter 5-12 (Terminal 27 Digital Input) set to 'Safe Stop' or another active function?</summary>
<div class="dtree-body"><strong>Yes:</strong> If terminal 27 is not in use, change parameter 5-12 to 'No function' and cycle power. If it is in use, verify the input signal is correct.<br><strong>No:</strong> Terminal 27 is not the cause. Recheck terminal 37 wiring, inspect for noise coupling from power cables, or consult the drive manual for advanced diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check the status display or parameters** to confirm WARNING 73 is active and note whether terminal 37 or terminal 27 is shown as the active Safe Stop input.
2. **Inspect all physical safety devices** (doors, guards, emergency stops) to verify they are fully closed, latched, and the interlocks are not physically stuck or damaged.
3. **Measure voltage at terminal 37** using a volt meter between terminal 37 and terminal 12 (24V reference). If you read approximately 24V when the safety device is open, the circuit is shorted or the switch is stuck.
4. **Trace control wiring from terminal 37 and 27** back to the interlock devices. Look for pinched wires, damaged insulation, corrosion at terminals, or any jumper wires left in place from prior testing.
5. **Review parameter 5-12 (Terminal 27 Digital Input)** in the drive menu. If terminal 27 is not used for Safe Stop, set it to 'No function.' If it is used, confirm the input signal matches the expected state.
6. **Cycle power to the drive** if the wiring and parameters are correct but the warning persists. A stuck input latch will sometimes clear after a full power-down for 30 seconds.
7. **Test the safety switch or sensor** by disconnecting it and checking continuity with a multimeter. Replace any switch that remains closed when the interlock should be open.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety door interlock switch (magnetic or mechanical) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-73-fault-code&k=Safety+door+interlock+switch+%28magnetic+or+mechanical%29&tag=errorcodefixes-20) \| Match the voltage rating and mounting type to your existing switch; consult your machine's wiring diagram for the correct part number. |
| Control cable for Safe Stop circuit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-73-fault-code&k=Control+cable+for+Safe+Stop+circuit&tag=errorcodefixes-20) \| Use shielded twisted-pair cable rated for 24V control signals; keep runs separate from motor power cables to prevent noise. |

## When to Call a Pro

Call a qualified technician or controls specialist if you are not comfortable working with 24V control circuits, interpreting VFD parameters, or tracing wiring in an industrial control panel. A professional should handle all troubleshooting if the drive is part of a safety-rated system (SIL-rated Safe Stop) where incorrect configuration could create a hazard. Also call a pro if the warning persists after you have verified the wiring and parameters are correct, as this may indicate a failing control board or a noise issue requiring shielded cable rerouting and grounding work.

**Rough cost:** A pro service call runs about $100-250 depending on whether it is wiring repair or a faulty safety switch.
