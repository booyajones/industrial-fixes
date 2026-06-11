---
title: "Danfoss FC302 VFD Alarm 44 - Causes & Fix"
description: "Alarm 44 on a Danfoss FC302 VFD means earth (ground) fault. The drive detected leakage current to ground. Usually the motor or cable."
pubDatetime: 2026-06-03T10:50:51Z
modDatetime: 2026-06-03T10:50:51Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Three-phase AC motor"
---

## Danfoss FC302 VFD Alarm 44 — What It Means

Alarm 44 on the Danfoss VLT FC 302 indicates an earth (ground) fault. The drive has detected leakage current flowing from one or more motor output phases to ground and trips to protect the drive, motor, and personnel. This is not a generic overload or phase-loss alarm. It is a specific ground-fault or insulation-leakage condition on the motor circuit. The drive's internal circuitry continuously monitors output current balance and will shut down when it senses current escaping to ground through damaged insulation, moisture, or contamination.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation breakdown** Age, overheating, contamination, or moisture ingress causes the motor windings to leak current to the motor frame.
- **Damaged motor cable or conduit** Abrasion, crushed insulation, or rodent damage in the cable run creates a path to ground.
- **Terminal-to-ground leakage** Water, dirt, or conductive contamination in the motor junction box or drive output terminals creates a leakage path.
- **Drive output stage failure** Internal damage to the drive's IGBT or output power section causes a ground fault even with the motor disconnected.

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive, then wait for the DC bus capacitors to discharge (consult your manual for safe wait time).
2. **Disconnect the motor leads** from the drive output terminals (U, V, W) and attempt to clear and reset the alarm.
3. **Perform a megohm insulation test** on the motor windings to ground with all three phases tied together (consult your insulation tester instructions and compare results to acceptable insulation resistance for your motor voltage).
4. **Test the motor cable separately** by disconnecting it from the motor and megohmming the cable to ground to distinguish cable damage from motor winding failure.
5. **Inspect all output wiring, junction boxes, and terminations** for moisture, carbon tracking, loose wire strands touching grounded enclosures, or physical damage.
6. **If the alarm persists with all output wiring removed**, suspect an internal drive fault in the power section or output IGBTs and prepare for drive repair or module replacement.
7. **After replacing the failed motor, cable, or drive power section**, reassemble all connections, clear faults from the drive, and run a no-load then full-load test to confirm the alarm does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-44-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| If insulation resistance to ground is too low and winding is compromised. |
| Shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-44-fault-code&k=Shielded+motor+cable&tag=errorcodefixes-20) \| Match voltage rating and conductor size to your VFD and motor nameplate. |
| FC 302 power module / inverter section | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-44-fault-code&k=FC+302+power+module+%2F+inverter+section&tag=errorcodefixes-20) \| Required if fault remains with motor disconnected (often a factory or authorized repair). |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage DC bus safety, megohm insulation testing, or VFD output circuits. If the alarm clears when the motor is disconnected but you cannot locate visible damage in the cable or motor junction box, a technician with a megohmmeter and experience interpreting insulation-resistance trends is essential. Internal drive faults in the power section or IGBT module require factory-trained service or an authorized Danfoss repair center, since these repairs involve replacing potted power assemblies and verifying gate-driver circuitry.

## See Also

- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-alarm-32-fault-code/)
- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
- [Danfoss FC302 Alarm 39 - Causes & Fix](/posts/danfoss-fc302-alarm-39-fault-code/)
