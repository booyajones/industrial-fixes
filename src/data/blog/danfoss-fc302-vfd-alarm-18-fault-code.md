---
title: "Danfoss FC302 VFD ALARM 18 - Causes & Fix"
description: "ALARM 18 on Danfoss FC302 means motor phase missing. Most common fix: check and tighten all motor output terminals at drive and motor."
pubDatetime: 2026-06-02T10:45:15Z
modDatetime: 2026-06-02T10:45:15Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable"
most_likely_cause: "Loose or open motor lead"
---

## What this code means
ALARM 18 on a Danfoss VLT AutomationDrive FC 302 indicates a motor phase missing condition. The drive has detected that one of the three output phases to the motor is absent or not being measured correctly, so the motor will not be driven normally. This alarm is tied to open-phase or missing-phase conditions on the motor output path. Danfoss instructs technicians to look for wiring, motor, and drive output-stage problems rather than treating it as a generic software fault.

## Common Causes

- **Loose or open motor lead** A conductor has come loose or disconnected at the drive output terminals or motor terminal block.
- **Damaged motor cable** The cable between the drive and motor has an open circuit on one phase due to physical damage or a faulty connector.
- **Motor winding fault** An internal motor winding has failed or an internal motor connection has opened.
- **Incorrect motor connection** A wiring error was introduced during installation or after recent service work.
- **Failed inverter output stage** The drive's internal power stage has failed if all motor and wiring checks are normal.

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive following local lockout/tagout procedures before touching any output wiring or motor terminals.
2. **Inspect and tighten all motor output terminals** at both the drive and motor ends, looking carefully for signs of heat damage, corrosion, or a loose conductor.
3. **Isolate the motor from the drive** by disconnecting the motor cable at the drive output terminals to separate external wiring and motor faults from internal drive faults.
4. **Ohm-check the motor cable phase-to-phase** and phase-to-ground with a multimeter to identify any open phase or clear imbalance that points to the cable or motor rather than the drive.
5. **Test the motor windings** phase-to-phase and phase-to-ground for continuity and balance, looking for an open or shorted winding.
6. **If the fault remains with the motor disconnected** or all wiring and motor checks are verified normal, suspect the drive's output or inverter power stage and proceed with drive-level repair or replacement.
7. **After correction, clear the alarm** from the drive display and run a controlled test with the motor unloaded first, then under normal operating load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-18-fault-code&k=Motor+cable&tag=errorcodefixes-20) \| If an open phase is found in the cable between drive and motor. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-18-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| If a winding or internal terminal fault is confirmed by resistance testing. |
| Danfoss FC302 power/inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-18-fault-code&k=Danfoss+FC302+power%2Finverter+module&tag=errorcodefixes-20) \| If the fault is internal to the VFD output stage after external wiring and motor are ruled out. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in lockout/tagout procedures, if you are uncomfortable working with three-phase power circuits, or if you have verified all motor and cable wiring and the fault persists. Drive output stage repair or replacement requires VFD-specific training and access to manufacturer service support. If the motor winding has failed, a motor shop or technician with winding test equipment should evaluate and repair or replace the motor.
