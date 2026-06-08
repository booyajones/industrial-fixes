---
title: "Danfoss FC302 Alarm 32 - Causes & Fix"
description: "Alarm 32 on the Danfoss FC302 VFD means motor phase W is missing. Check wiring and connections on the W output phase first."
pubDatetime: 2026-06-04T09:11:13Z
modDatetime: 2026-06-04T09:11:13Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 32 — What It Means

Alarm 32 on the Danfoss FC302 variable frequency drive indicates that motor phase W is missing. The drive is not detecting current flow on the W output phase between the VFD and the motor. This fault does not appear at startup and is grouped with alarms 30 and 31, which flag missing phases U and V respectively. The issue is on the drive output side, not the incoming mains supply.

The most common cause is a loose, broken, or open motor lead on phase W. Bad terminal connections, damaged cable insulation, or corrosion in one output leg can also trigger this alarm. If wiring and motor checks pass, the problem may be a failed inverter output stage or IGBT in that phase.

[Jump to Fix](#fix)

## Common Causes

- **Loose or broken motor lead on phase W** The W output wire from the drive to the motor has come loose, broken internally, or disconnected at a terminal.
- **Bad terminal connection or connector** Corroded, burned, or improperly tightened connections at the drive output terminals or motor junction box prevent current flow.
- **Cable damage or open circuit in W leg** Physical damage to the motor cable, such as a cut jacket, crushed conductor, or internal break, creates an open circuit on phase W.
- **Failed drive output stage or IGBT** The inverter module or power section IGBT for phase W has failed and no longer switches current to the motor.
- **Motor internal winding or lead fault** An open winding or internal connection failure inside the motor stops current on phase W even when external wiring is intact.

## Step-by-Step Fix {#fix}

1. Lock out power to the VFD and wait for the DC bus capacitors to discharge fully before opening any covers or touching conductors.
2. Inspect the motor output wiring at both the drive output terminals and the motor junction box, paying close attention to phase W for loose lugs, corrosion, or burned connections.
3. Check for continuity from the drive W output terminal through the cable to the motor W lead using a multimeter, looking for any open circuit, damaged cable section, or loose connector.
4. Tighten all motor output connections on phases U, V, and W to manufacturer torque specifications and re-seat any plug-in connectors firmly.
5. Inspect the motor mechanically for internal damage or winding faults, and if needed isolate the motor and test with a known-good replacement or perform insulation-resistance checks.
6. If wiring and motor are confirmed good but the alarm persists, suspect the inverter power module and test or replace the output stage or power board for phase W.
7. Clear the alarm through the drive keypad or control interface, restore power, and run the drive under load to verify all three output phases are present and current is balanced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable (3-phase power cable) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-32-fault-code&k=Motor+output+cable+%283-phase+power+cable%29&tag=errorcodefixes-20) \| Match wire gauge and insulation rating to your drive and motor nameplate specifications. |
| Terminal lugs and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-32-fault-code&k=Terminal+lugs+and+connectors&tag=errorcodefixes-20) \| Use crimp or compression lugs rated for the current and torque at drive and motor terminals. |
| Danfoss FC302 power board or inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-32-fault-code&k=Danfoss+FC302+power+board+or+inverter+module&tag=errorcodefixes-20) \| Consult your drive model and frame size to order the correct replacement output stage assembly. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in high-voltage DC bus safety, if you cannot locate an open circuit in the motor wiring, or if the alarm returns after tightening connections and testing the motor. Inverter output stage repairs require specialized tools, replacement parts matched to your drive frame size, and knowledge of power electronics. If the drive has suffered secondary damage to fuses or the power section, a professional can diagnose the full scope of repairs and prevent further equipment damage.

## See Also

- [Danfoss VLT 2900 Fault Codes: Complete Guide](/posts/danfoss-vlt-2900-faults/)
- [Danfoss RX Controller Fault Codes — Troubleshooting Guide](/posts/danfoss-rx-controller-fault/)
- [Danfoss FC302 Alarm 20 - Causes & Fix](/posts/danfoss-fc302-alarm-20-fault-code/)
- [Danfoss FC302 Alarm 40 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-40-fault-code/)
