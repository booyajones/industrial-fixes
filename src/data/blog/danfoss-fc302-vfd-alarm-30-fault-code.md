---
title: "Danfoss FC302 ALARM 30 - Causes & Fix"
description: "ALARM 30 on Danfoss FC302 means motor phase U is missing. Most likely fix: check and tighten U-phase motor cable connections."
pubDatetime: 2026-06-03T10:41:06Z
modDatetime: 2026-06-03T10:41:06Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 ALARM 30 — What It Means

ALARM 30 on a Danfoss VLT AutomationDrive FC 302 means motor phase U missing. The drive does not detect continuity on the U phase between the frequency converter and the motor, so it trips to protect the power stage and motor. The FC 302 has detected that the U output phase is open or disconnected between the drive and the motor. This alarm is part of the missing motor phase U/V/W fault family and is not expected to appear during normal start-up. It is a running or output-phase fault that indicates a break in the circuit path.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected motor lead on U phase** A loose, broken, or disconnected motor cable on the U phase between the drive output and motor is the most common cause of this alarm.
- **Bad terminal connection or corroded connector** Corroded, damaged, or overheated terminals and connectors in the U phase path can create an open circuit that triggers the fault.
- **Damaged motor cable conductor** The U-phase motor cable itself may have a broken conductor or internal damage that interrupts continuity.
- **Motor winding open circuit on U phase** An open or failed winding inside the motor on the U phase will make the drive see a missing phase and trip.
- **Internal drive power stage fault** If the inverter output section or IGBT for the U phase is damaged inside the drive, it can produce the same missing-phase symptom even with good external wiring.

## Step-by-Step Fix {#fix}

1. **Remove power and verify safety** before any inspection. The Danfoss FC 302 contains high voltage when connected to mains, DC supply, or load sharing, so lock out and tag out the disconnect and wait for internal capacitors to discharge.
2. **Inspect the U-phase motor wiring** from the drive output terminals to the motor terminal box for visible damage, looseness, broken conductors, or contamination. Look for signs of overheating, corrosion, or physical damage along the entire cable run.
3. **Check and tighten all U-phase output terminals** on both the drive and the motor. Verify that connectors are seated fully and that terminal screws are torqued to the manufacturer's specification. Look for any corrosion, discoloration, or heat damage at each connection point.
4. **Measure continuity of the U-phase circuit** end-to-end from the drive output terminal to the motor terminal using a multimeter. If continuity is lost, repair or replace the cable or termination as needed.
5. **Test with a known-good motor and cable** if continuity checks pass but the alarm persists. If the drive trips with verified good external wiring and a good motor, the fault is likely internal to the drive power stage.
6. **Clear the fault and test under load** after any repair. Restore power, reset the alarm, and run the drive through its operating cycle to confirm the U phase is stable and the drive does not re-trip.
7. **Arrange for drive service or replacement** if the alarm continues with good external wiring. Danfoss indicates that persistent missing-phase alarms with verified wiring point to an internal power section or control assembly fault that requires factory repair or module replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (U-phase conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-30-fault-code&k=Motor+cable+%28U-phase+conductor%29&tag=errorcodefixes-20) \| Replace if continuity is open or conductor is damaged or overheated. |
| Motor terminal connector hardware | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-30-fault-code&k=Motor+terminal+connector+hardware&tag=errorcodefixes-20) \| Replace terminals, lugs, or connectors if corroded, melted, or mechanically damaged. |
| Danfoss FC302 power section or IGBT output stage | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-30-fault-code&k=Danfoss+FC302+power+section+or+IGBT+output+stage&tag=errorcodefixes-20) \| Required if internal drive fault is confirmed after external wiring and motor are verified good. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained to work safely on live or recently live high-voltage equipment. If you have verified that all external motor connections are tight and the U-phase cable has continuity, but the alarm persists, the fault is likely inside the drive and requires an experienced technician or factory-authorized service center to diagnose and replace the power stage or control card. Do not continue to run the drive with a recurring missing-phase alarm, as it can damage the motor or the remaining drive components.

## See Also

- [Danfoss FC302 VFD ALARM 57 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-57-fault-code/)
- [Danfoss FC302 ALARM 20 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-20-fault-code/)
- [Danfoss FC302 ALARM 25 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-25-fault-code/)
- [Danfoss FC302 ALARM 18 - Causes & Fix](/posts/danfoss-fc302-alarm-18-fault-code/)
