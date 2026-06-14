---
title: "Danfoss FC302 VFD Alarm 16 - Causes & Fix"
description: "Alarm 16 on a Danfoss FC302 VFD means a line-to-line short circuit in the motor or motor wiring. Isolate and test cable and windings."
pubDatetime: 2026-06-03T10:36:17Z
modDatetime: 2026-06-03T10:36:17Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (three-phase shielded)"
most_likely_cause: "Shorted motor cable"
---

## Danfoss FC302 VFD Alarm 16 — What It Means

Alarm 16 on the Danfoss VLT FC 302 drive indicates a short circuit fault. The drive has detected a line-to-line short circuit in the motor or motor wiring. This means current is flowing between output phases in an unintended path, either in the motor cable, inside the motor windings, or within the drive's own power section.

The fault protects the drive from damage by shutting down output. It does not point to a specific component until you isolate the motor from the drive and test each part of the circuit. If the alarm clears when the motor is disconnected, the problem is external. If it persists with no load, the drive's inverter or power stage has likely failed internally.

[Jump to Fix](#fix)

## Common Causes

- **Shorted motor cable** Damaged insulation or pinched wiring between drive output terminals and motor causes phase-to-phase shorts in the field cabling.
- **Shorted motor windings** Internal insulation failure inside the motor creates a direct short between winding phases.
- **Failed IGBT or inverter module** A shorted power semiconductor in the drive's output stage triggers Alarm 16 even with the motor disconnected.
- **Damaged motor terminal box** Carbon tracking, moisture, or loose hardware in the terminal box bridges output phases at the motor connection point.
- **Defective drive power board** Component failure on the drive's power section can create an internal short circuit path that mimics a motor fault.

## Step-by-Step Fix {#fix}

1. **Lock out and remove all power** to the drive and motor before touching any terminals or opening enclosures.
2. **Disconnect the motor leads** from the drive output terminals (U, V, W) and visually inspect the cable, connectors, and motor terminal box for char marks, melted insulation, or physical damage.
3. **Power the drive with no motor connected** and observe whether Alarm 16 still appears. If the fault persists with no load, the problem is inside the drive's power section.
4. **Test the motor cable for continuity** between each phase pair (U-V, V-W, U-W) using a multimeter. Any reading below infinite resistance indicates a cable short.
5. **Ohm-test the motor windings** phase-to-phase at the motor terminal box. A zero or very low resistance reading between any two phases confirms an internal motor short.
6. **Replace the faulty component** identified by your tests. If the cable or motor is shorted, replace it. If the drive faulted with no load, the inverter module or power board must be replaced.
7. **Reassemble and verify insulation integrity** on all connections, then perform a controlled startup test at low speed to confirm the fault is cleared before returning to normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (three-phase shielded) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-16-fault-code&k=Motor+cable+%28three-phase+shielded%29&tag=errorcodefixes-20) \| Match original gauge and length if cable insulation is shorted or damaged between drive and motor. |
| IGBT inverter module (FC 302 power section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-16-fault-code&k=IGBT+inverter+module+%28FC+302+power+section%29&tag=errorcodefixes-20) \| Required when drive shows Alarm 16 with motor disconnected. Consult Danfoss or a drive repair house for the correct module for your frame size. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-16-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| Replace if ohm tests confirm a winding-to-winding short inside the motor that cannot be repaired. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage electrical work or VFD troubleshooting. Diagnosing Alarm 16 requires live voltage measurements, isolation testing, and familiarity with three-phase motor circuits. If your tests show the drive's internal power section has failed, replacement of the IGBT module or power board demands specialized tools and knowledge of semiconductor handling. A Danfoss-authorized service center can bench-test and repair the drive power stage, often more cost-effectively than field replacement of entire boards.

## See Also

- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
- [Danfoss FC302 ALARM 20 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-20-fault-code/)
- [Danfoss FC302 Alarm 14 - Causes & Fix](/posts/danfoss-fc302-alarm-14-fault-code/)
- [Danfoss FC302 Alarm 31 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-31-fault-code/)
