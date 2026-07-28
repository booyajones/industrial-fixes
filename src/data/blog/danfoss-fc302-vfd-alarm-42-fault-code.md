---
title: "Danfoss FC302 Alarm 42 - Causes & Fix"
description: "Alarm 42 on Danfoss FC302 VFD means overload on digital output terminal X30/6 or X30/7. Check wiring and load on these terminals."
pubDatetime: 2026-06-03T10:49:44Z
modDatetime: 2026-06-03T10:49:44Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Relay coil or contactor coil"
most_likely_cause: "Excessive current draw from connected load"
---

## What this code means
Alarm 42 on the Danfoss VLT AutomationDrive FC 302 indicates an overload condition on digital output terminal X30/6 or X30/7. The drive has detected that one of these output terminals is drawing excessive current, either from an overloaded external device or a short circuit in the wiring. This is not a motor overload or input power fault. It is specifically related to the control outputs on those two terminals.

The drive will trigger this alarm to protect the output stage from damage. The problem lies either in the external load connected to the terminal (such as a relay coil, contactor, or solenoid drawing too much current), a wiring fault creating a short circuit, or in rare cases a defective control card if the alarm persists with all external loads disconnected.

## Common Causes

- **Excessive current draw from connected load** A relay coil, contactor, solenoid, or other device wired to X30/6 or X30/7 is drawing more current than the output can supply.
- **Short circuit in output wiring** Damaged insulation, pinched conductors, loose strands, or terminal damage is creating a short at the X30/6 or X30/7 wiring or terminal strip.
- **Defective external device** The field device connected to the output (such as a failed relay or solenoid) has developed an internal short or overload condition.
- **Incorrect terminal parameterization** The drive's programming for the X30 output terminals does not match the intended load or output function, causing an incompatible configuration.
- **Faulty control card or output stage** If the alarm does not clear with external loads removed, the control card or I/O board output stage may be defective.

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and lockout the supply before performing any inspection or wiring work.
2. **Inspect wiring** on terminals X30/6 and X30/7 for pinched conductors, shorts to adjacent terminals, loose strands, and signs of terminal damage.
3. **Disconnect the external load** from the suspect output terminal (X30/6 or X30/7) and reapply power to see if the alarm clears.
4. **Test the disconnected load device** separately using a multimeter to check for excessive current draw, a shorted coil, or a failed component, and replace the defective device if confirmed.
5. **Review the drive's I/O programming** for the X30 terminals in the parameter menu and confirm the terminal mode and output function match the intended application.
6. **Reconnect the load** and reapply power, then verify the alarm does not return under normal operation.
7. **Replace the control card or I/O board** if the alarm persists with the external load removed, indicating a defective output stage on the drive itself.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Relay coil or contactor coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-42-fault-code&k=Relay+coil+or+contactor+coil&tag=errorcodefixes-20) \| Replacement for external load device connected to X30/6 or X30/7 if found shorted or drawing excessive current. |
| Control card (FC 302 compatible) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-42-fault-code&k=Control+card+%28FC+302+compatible%29&tag=errorcodefixes-20) \| Replacement for defective I/O board or output stage if alarm does not clear with external loads disconnected. |
| Terminal block connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-42-fault-code&k=Terminal+block+connectors&tag=errorcodefixes-20) \| Replacement for damaged X30 terminal strip or connectors if physical damage is found. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working with VFD wiring and control circuits, or if the alarm persists after disconnecting all external loads and verifying wiring integrity. Replacing the control card or I/O board requires familiarity with the drive's internal components and proper handling of static-sensitive electronics. Professional diagnostics can isolate whether the fault is in the field wiring, the external load, or the drive's internal output stage, and make sure safe repair of industrial control equipment.
