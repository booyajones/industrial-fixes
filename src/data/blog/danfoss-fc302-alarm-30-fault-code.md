---
title: "Danfoss FC302 ALARM 30 - Causes & Fix"
description: "ALARM 30 on the Danfoss FC302 means missing motor phase U. Learn the common causes, diagnostic steps, and parts to fix this fault."
pubDatetime: 2026-05-29T09:47:36Z
modDatetime: 2026-05-29T09:47:36Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (U-phase conductor)"
---

## Danfoss FC302 ALARM 30 — What It Means

ALARM 30 on a Danfoss VLT AutomationDrive FC 302 indicates a missing motor phase U. The drive does not detect output current flowing through the U phase to the motor, meaning there is an open circuit or broken connection between the drive's U output terminal and the motor. This alarm appears during normal operation, not at startup, and points to a problem in the physical wiring, motor winding, or the drive's output stage on the U leg.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected U-phase motor lead** A broken wire, unplugged connector, or loose conductor on phase U between the drive and motor is the most common field cause.
- **Bad terminal connection at drive or motor** Corroded, heat-damaged, or partially seated terminals and lugs at either end can create an open circuit on the U phase.
- **Open motor winding on phase U** If the wiring is intact, a failed or open winding inside the motor on the U phase will trigger the alarm.
- **Failed drive inverter output stage** A defective IGBT, power module, or inverter board on the U leg inside the drive can prevent current from reaching the motor even when wiring and motor are good.

## Step-by-Step Fix {#fix}

1. Power down and lock out the drive, then verify zero voltage at all motor terminals before any inspection or testing.
2. Inspect the motor cable from drive to motor, looking specifically for damage, breaks, or disconnection on the U-phase conductor.
3. Tighten and re-seat all motor terminal connections at both the drive output and motor junction box, checking for oxidation, heat damage, or loose ferrules.
4. Use a multimeter to check continuity on the U-phase motor winding and cable; compare readings to the V and W phases to isolate whether the open circuit is in the wire or motor.
5. If wiring and motor check good, swap or test the U-phase output at the drive (if possible) to determine whether the drive's power module or inverter board has failed.
6. Replace the faulty component (cable, motor, or drive power module) based on your test results.
7. Clear the alarm on the drive, power up, and run the motor under load to confirm current is restored on phase U and the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (U-phase conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-30-fault-code&k=Motor+cable+%28U-phase+conductor%29&tag=errorcodefixes-20) \| Replace if the U-phase wire is broken, damaged, or shows an open circuit during continuity tests. |
| Motor terminal hardware (lugs, ferrules, connectors) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-30-fault-code&k=Motor+terminal+hardware+%28lugs%2C+ferrules%2C+connectors%29&tag=errorcodefixes-20) \| Replace corroded, heat-damaged, or loose terminals at the drive or motor junction box. |
| Motor (three-phase) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-30-fault-code&k=Motor+%28three-phase%29&tag=errorcodefixes-20) \| Required if the U-phase winding is open and the motor cannot be repaired. |
| Drive power module or inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-30-fault-code&k=Drive+power+module+or+inverter+board&tag=errorcodefixes-20) \| Replace if diagnostics confirm the drive's U-phase output stage is defective and wiring and motor are good. |

## When to Call a Pro

Call a qualified technician or certified Danfoss service partner if you are not trained in high-voltage AC wiring, if you cannot safely isolate and test the drive and motor, or if your tests point to a failed inverter power module inside the drive. Replacing internal drive components requires experience with VFD electronics and proper ESD handling. If the fault persists after wiring and motor checks, or if multiple phase alarms appear together, professional diagnosis will save time and prevent further damage to the drive or motor.

## See Also

- [Danfoss FC302 ALARM 36 - Causes & Fix](/posts/danfoss-fc302-alarm-36-fault-code/)
- [Danfoss FC302 ALARM 37 - Causes & Fix](/posts/danfoss-fc302-alarm-37-fault-code/)
- [Danfoss FC302 ALARM 27 - Causes & Fix](/posts/danfoss-fc302-alarm-27-fault-code/)
- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-alarm-34-fault-code/)
