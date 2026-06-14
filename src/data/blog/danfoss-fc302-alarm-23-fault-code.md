---
title: "Danfoss FC302 Alarm 23 - Causes & Fix"
description: "Danfoss FC302 Alarm 23 means internal fan fault. Learn what triggers the warning, how to diagnose fan and sensor issues, and repair steps."
pubDatetime: 2026-05-29T09:44:30Z
modDatetime: 2026-05-29T09:44:30Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 internal cooling fan assembly"
most_likely_cause: "Fan not spinning or mechanically failed"
---

## Danfoss FC302 Alarm 23 — What It Means

Alarm 23 on the Danfoss FC 302 drive signals an internal fan fault or warning. The drive monitors whether the internal cooling fan is running and mounted correctly. On units with DC fans, the drive expects a feedback sensor signal from the fan. If the fan is commanded to run but no feedback is received, the alarm appears. On units with AC fans, the drive monitors the fan supply voltage instead of a feedback sensor. The alarm can also appear if the fan is not properly mounted or connected, even if the fan itself is functional.

[Jump to Fix](#fix)

## Common Causes

- **Fan not spinning or mechanically failed** The internal cooling fan has stopped rotating due to bearing wear, motor failure, or debris blocking the blades.
- **Fan not properly mounted or connected** The fan assembly is loose, the connector is unseated, or the mounting is incorrect so the monitor circuit sees a fault.
- **Faulty fan feedback sensor (DC fan units)** On drives with DC fans, the feedback sensor or its wiring has failed so the drive does not detect fan operation even when the fan runs.
- **Fan supply voltage issue (AC fan units)** On drives with AC fans, the supply voltage to the fan is absent or incorrect when the drive commands the fan to run.
- **Control card or fan-sense circuit fault** The control card circuit that monitors the fan has failed or the sensor path from the fan to the control card is broken.
- **Blocked airflow or dirty heatsink** Although not the direct trigger, clogged filters or debris on the heatsink often accompany fan trouble and can cause the fan to struggle or fail.

## Step-by-Step Fix {#fix}

1. Verify the alarm code on the keypad or LCP display and confirm the unit is an FC 301 or FC 302 drive, as Alarm 23 is specific to the fan monitor function on these models.
2. Inspect the internal cooling fan physically for rotation, debris, damage, loose mounting screws, and secure connector attachment. Look for signs of wear or obstruction.
3. Cycle power to the drive and observe the fan at startup. The fan should briefly operate during power-up on both DC and AC fan variants as part of the normal startup sequence.
4. Check parameter 14-53 (Fan Monitor) in the drive programming to confirm the fan monitor function is enabled. If disabled, the drive will not detect fan faults, but disabling is not a repair for a failed cooling system.
5. If the drive uses a DC fan, check the fan feedback sensor and trace the wiring and signal path back to the control card. Look for broken wires, poor connections, or sensor damage.
6. If the drive uses an AC fan, verify that the fan supply voltage is present when the drive commands the fan to run. Use a multimeter to measure voltage at the fan terminals.
7. Replace the fan assembly if it does not run, does not provide the expected feedback signal, or shows mechanical failure. If the fan is good but the alarm persists, inspect the control card connections and consider control card replacement if the sensing circuit is faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 internal cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-23-fault-code&k=Danfoss+FC+302+internal+cooling+fan+assembly&tag=errorcodefixes-20) \| Match to your drive frame size and voltage. DC and AC fan versions differ. |
| Fan feedback sensor (DC fan models) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-23-fault-code&k=Fan+feedback+sensor+%28DC+fan+models%29&tag=errorcodefixes-20) \| Only needed on DC fan units if sensor is proven faulty. |
| FC 302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-23-fault-code&k=FC+302+control+card&tag=errorcodefixes-20) \| Required only if fan and sensor are good but alarm remains due to failed sensing circuit. |

## When to Call a Pro

Call a qualified technician or Danfoss service partner if you are not comfortable working inside the drive enclosure, if the fan and sensor both test good but the alarm persists, or if you suspect a control card fault. Drives operate at dangerous voltages and improper work can damage the unit or void warranties. A technician can trace the fan feedback circuit, verify control card operation, and safely replace internal components. If your drive is under warranty or part of a larger automated system, professional service is the safer choice to avoid unintended downtime or integration issues.

## See Also

- [Danfoss FC302 ALARM 26 - Causes & Fix](/posts/danfoss-fc302-alarm-26-fault-code/)
- [Danfoss VFD Fault E-Trip — Causes & Fix](/posts/danfoss-vfd-fault-e-trip/)
- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/posts/danfoss-fc302-alarm-13/)
- [Danfoss FC302 Alarm 21 - Causes & Fix](/posts/danfoss-fc302-alarm-21-fault-code/)
