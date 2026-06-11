---
title: "Danfoss FC302 ALARM 45 - Causes & Fix"
description: "ALARM 45 on Danfoss FC302 VFD means Earth fault 2/Ground fault detected. Most often caused by motor cable insulation breakdown."
pubDatetime: 2026-06-03T10:51:29Z
modDatetime: 2026-06-03T10:51:29Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (shielded VFD-rated)"
---

## Danfoss FC302 ALARM 45 — What It Means

ALARM 45 on a Danfoss VLT AutomationDrive FC302 is labeled "Earth fault 2" or "Ground fault" in the drive's documentation. The drive has detected leakage current to ground using its internal ground-fault monitoring circuitry. This is a trip condition, meaning the drive stops the motor immediately to protect the equipment from damage. It is not an overcurrent, overvoltage, or overheating fault. The detection system identifies imbalance or leakage in the motor circuit grounding path.

The fault points to a problem in the motor, motor cables, grounding connections, or less commonly the drive's internal hardware. Danfoss directs troubleshooting toward the motor circuit first, then toward control or option cards if the fault persists after the motor and cables are ruled out.

[Jump to Fix](#fix)

## Common Causes

- **Motor cable insulation breakdown or leakage current** Damaged, aged, or moisture-infiltrated motor cable insulation allows current to leak to ground and trigger the fault.
- **Loose or improper grounding connections** Loose ground wires, corroded terminals, or incorrect shield termination create imbalance that the drive reads as a ground fault.
- **Short circuit in motor cables** A direct short between a motor phase conductor and ground or the cable shield causes immediate fault detection.
- **Defective motor winding insulation** Internal motor insulation failure allows winding current to leak to the motor frame and trigger the ground-fault monitor.
- **Defective control card or option card in the drive** If the motor circuit checks out clean, a failing control or option card can produce false ground-fault signals.
- **Incorrect wire size or wiring practices** Undersized or improperly routed cables increase leakage and imbalance that the drive interprets as a ground fault.

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the VFD and motor using the disconnect switch and verify zero voltage with a meter before touching any connections.
2. **Inspect motor circuit grounding and terminations** for loose connections, corrosion, damaged insulation, or visible cable wear at the drive output terminals, cable runs, and motor junction box.
3. **Disconnect the motor cables** from the drive output terminals to isolate the motor and cable from the drive, then reset and power the drive without the motor connected to see if the fault clears.
4. **Perform an insulation resistance test** (megger test) on the motor and motor cables following your standard procedure and the motor manufacturer's acceptable resistance limits to identify leakage or shorts to ground.
5. **Repair or replace faulty motor cables** if insulation testing shows low resistance, and tighten or replace any loose or corroded ground connections and cable terminations.
6. **Check the drive's 24 V DC supply** if your installation uses an external 24 V supply, and verify correct voltage and clean connections per the drive manual.
7. **Inspect and replace the control card or option card** if the fault persists after the motor circuit is confirmed good, and check the heatsink fan for proper operation as part of broader drive health diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-45-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation testing shows leakage or visible damage. |
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-45-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Order by your exact drive model suffix if motor circuit checks good but fault persists. |
| Danfoss FC302 option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-45-fault-code&k=Danfoss+FC302+option+card&tag=errorcodefixes-20) \| Replace if you have an installed option and fault isolation points to the card. |
| Heatsink fan for FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-45-fault-code&k=Heatsink+fan+for+FC302&tag=errorcodefixes-20) \| Check and replace if drive thermal stress is contributing to intermittent faults. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage VFD work, if insulation testing and motor-circuit inspection do not isolate the fault, or if you suspect internal drive component failure. Ground-fault troubleshooting requires safe isolation procedures, megger testing, and familiarity with three-phase motor circuits. If the fault returns after cable and motor replacement, the drive's control or option card may need factory-level diagnosis or replacement, which requires knowledge of the FC302 hardware architecture and proper handling of static-sensitive electronics.

## See Also

- [Danfoss FC302 ALARM 24 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-24-fault-code/)
- [Danfoss FC302 ALARM 25 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-25-fault-code/)
- [Danfoss FC302 Alarm 40 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-40-fault-code/)
- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
