---
title: "Danfoss FC302 Alarm 26 - Causes & Fix"
description: "Alarm 26 on Danfoss FC302 VFD means inverter/power stage fault. Most common fix: check motor cable for shorts, then replace IGBT."
pubDatetime: 2026-06-03T10:38:22Z
modDatetime: 2026-06-03T10:38:22Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 26 — What It Means

Alarm 26 on a Danfoss VLT AutomationDrive FC302 is a trip at inverter fault. The drive has detected a problem in its inverter or power stage section and has shut down to protect itself and the motor. This is not a simple overload. The fault is internal to the drive's power electronics or caused by a short circuit in the motor or motor cable. The inverter section contains the IGBTs (power transistors) that switch DC power into variable AC for the motor. When this alarm appears, the drive will not run until the fault is cleared and the alarm is reset.

[Jump to Fix](#fix)

## Common Causes

- **Failed IGBT or power module** The inverter section's power transistors or full power module have failed due to heat, electrical stress, or component aging.
- **Shorted motor cable or damaged output wiring** A phase-to-phase or phase-to-ground short in the output wiring or at the motor terminals triggers inverter protection.
- **Motor winding insulation breakdown** Low insulation resistance in the motor windings creates a fault path that the inverter detects as a power stage problem.
- **Contamination or moisture in the drive** Dirt, dust, or humidity on the inverter board or power stage can create tracking paths and fault conditions.
- **Loose or burned output terminals** Poor connections at the drive's motor output terminals cause arcing and heat that damage the inverter section.
- **DC link or rectifier failure** A fault in the DC bus capacitors or rectifier stage can cascade into an inverter fault alarm.

## Step-by-Step Fix {#fix}

1. **Lock out and tag out all power** to the drive and wait for internal capacitors to discharge (consult your manual for safe wait time, typically 5-15 minutes after power removal).
2. **Record the alarm history** in the drive's display or parameter menu to check for any related faults or patterns that appeared before Alarm 26.
3. **Disconnect the motor leads** from the drive's output terminals (U, V, W) and inspect all output wiring and terminal connections for signs of burning, arcing, loose screws, or physical damage.
4. **Test motor and cable insulation** using a megohmmeter (typically 500V or 1000V DC test) between each phase and ground, and phase-to-phase, to confirm no short or low insulation resistance (check your motor specs for acceptable values, usually >1 megohm for 480V motors).
5. **Attempt a no-load start** with the motor disconnected. Reset the alarm per your manual and command the drive to run unloaded. If Alarm 26 returns with no motor connected, the fault is internal to the drive's inverter power stage.
6. **Inspect the drive interior** (after verifying zero energy) for signs of component damage, burned traces on the inverter board, swollen capacitors, or contamination on the power module and heatsink.
7. **Replace the failed inverter power module or IGBT module** if internal fault is confirmed, or arrange for factory-authorized repair. If the motor or cable tested faulty, repair or replace that component and retest the drive.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IGBT power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-26-fault-code&k=IGBT+power+module&tag=errorcodefixes-20) \| Match the exact part number for your FC302 frame size and voltage rating. |
| Inverter power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-26-fault-code&k=Inverter+power+board+assembly&tag=errorcodefixes-20) \| Full inverter section replacement if individual IGBTs are not serviceable on your model. |
| Motor output cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-26-fault-code&k=Motor+output+cable&tag=errorcodefixes-20) \| Use VFD-rated cable with proper shielding if cable insulation tested low. |
| DC link capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-26-fault-code&k=DC+link+capacitor+bank&tag=errorcodefixes-20) \| If DC bus fault contributed to the inverter trip, consult your drive's schematic. |

## When to Call a Pro

Call a qualified drive technician or authorized Danfoss service provider if you lack the tools or training to perform high-voltage lockout, insulation testing, or internal drive inspection. Component-level repair of inverter power stages requires specialized test equipment and knowledge of high-power electronics. If the motor and cable test good but the drive still trips with no load, the repair typically involves replacing or rebuilding the inverter power module. This is not a DIY repair for most facilities. Danfoss drives contain hazardous voltage even after mains disconnection. Always follow the manufacturer's safety procedures.

## See Also

- [Danfoss FC302 VFD Alarm 46 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-46-fault-code/)
- [Danfoss FC302 ALARM 27 - Causes & Fix](/posts/danfoss-fc302-alarm-27-fault-code/)
- [Danfoss FC302 ALARM 37 - Causes & Fix](/posts/danfoss-fc302-alarm-37-fault-code/)
- [Danfoss FC302 VFD Alarm 41 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-41-fault-code/)
