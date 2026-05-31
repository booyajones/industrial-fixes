---
title: "Danfoss FC302 Alarm 32 - Causes & Fix"
description: "Danfoss FC302 Alarm 32 means motor phase W is missing. Learn what causes it and how to diagnose wiring, motor windings, and drive output."
pubDatetime: 2026-05-29T09:48:42Z
modDatetime: 2026-05-29T09:48:42Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 32 — What It Means

Alarm 32 on the Danfoss FC302 indicates that the drive does not detect continuity or expected current on the W output phase between the frequency converter and the motor. Danfoss groups Alarm 30, 31, and 32 as the missing motor phase family, with 32 tied specifically to phase W. The drive has detected that the W phase output is open, disconnected, or otherwise not being recognized as a valid motor phase. This alarm does not appear when the drive is starting.

The fault points to an interruption somewhere in the W phase circuit, from the drive output terminal through the motor cable to the motor winding itself. The drive expects to see balanced current on all three phases during operation, and the absence of current on W triggers the protective alarm.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected motor lead on phase W** A loose terminal, poor crimp, or disconnected wire between the drive output and motor is the most common cause of this alarm.
- **Open motor winding on phase W** An open winding inside the motor or a bad termination in the motor junction box will prevent current flow on that phase.
- **Connector or terminal issue at the drive output** Poor clamp pressure, corrosion, or a damaged cable lug at the W output terminal can create an open circuit.
- **Damaged motor cable** A pinched, cut, or broken conductor in the motor cable will interrupt the W phase even if both ends appear connected.
- **Failed inverter power stage on W leg** If the drive's output power device for the W phase has failed, the drive may not supply or detect current even when wiring and motor are good.

## Step-by-Step Fix {#fix}

1. Lock out power and wait for DC bus discharge. Stop the motor, disconnect AC mains and any DC-link sources, and use an appropriate voltage measuring device to verify capacitors are fully discharged before touching any terminals.
2. Inspect the W motor phase wiring from drive output to motor terminal box. Look for loose connections, pinched cable, visible damage, or a broken conductor.
3. Tighten and re-terminate the drive output terminals and motor terminals. Remove and reseat the W phase connection at both ends if any corrosion or poor contact is visible.
4. Measure continuity of the W phase from drive to motor. Compare the resistance against U and V phases. An open circuit on only W confirms a wiring or winding fault.
5. Swap or ohm-check the motor leads at the motor junction box if accessible. If the fault follows the cable when you move it to a different motor terminal, the cable is bad. If the fault stays with the motor terminal, the winding is open.
6. Isolate the motor from the drive and re-test if needed. If you connect a known-good motor and the alarm clears, the original motor is faulty. If the alarm persists with a good motor and verified wiring, suspect the drive's W-phase output stage.
7. Check the drive's output power stage if wiring and motor test good. If Alarm 32 continues after all external connections are verified, the inverter power module on the W leg may have failed and requires drive-level diagnostics or module replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (3-phase shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-32-fault-code&k=Motor+cable+%283-phase+shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if continuity test shows open conductor on W phase or visible damage. |
| Motor terminal connections or junction-box hardware | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-32-fault-code&k=Motor+terminal+connections+or+junction-box+hardware&tag=errorcodefixes-20) \| Replace corroded or damaged terminal lugs, bus bars, or mounting hardware in the motor junction box. |
| Motor winding (or complete motor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-32-fault-code&k=Motor+winding+%28or+complete+motor%29&tag=errorcodefixes-20) \| If the W phase is open inside the motor and cannot be accessed, the motor requires rewind or replacement. |
| Drive inverter power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-32-fault-code&k=Drive+inverter+power+module&tag=errorcodefixes-20) \| Contact Danfoss or your distributor for the correct module part number for your FC302 frame size if the W-phase output stage is faulty. |

## When to Call a Pro

Call a qualified technician if you are not trained to work on high-voltage DC bus circuits or if you cannot safely verify that the drive's capacitors are discharged. If continuity tests and wiring inspections do not locate the fault, or if the alarm persists after verifying all external connections and substituting a known-good motor, the drive's internal power stage likely requires module-level repair or replacement that should be performed by a drive specialist or Danfoss-certified service provider.
