---
title: "Danfoss FC302 ALARM 31 - Causes & Fix"
description: "ALARM 31 on the Danfoss FC302 means motor phase V is missing. Troubleshoot loose wiring, open cables, and failed output stages."
pubDatetime: 2026-05-29T09:48:06Z
modDatetime: 2026-05-29T09:48:06Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 ALARM 31 — What It Means

ALARM 31 on a Danfoss VLT AutomationDrive FC 302 indicates that motor phase V is missing between the drive and the motor. The drive has detected that the V output leg is open or absent. This alarm does not appear at startup. It shows up during operation when the drive monitors output current and phase continuity and finds that phase V is not conducting properly.

[Jump to Fix](#fix)

## Common Causes

- **Loose, broken, or disconnected motor wiring on phase V** The V-phase conductor between the drive output terminals and the motor is loose, severed, or completely disconnected.
- **Open or corroded terminals and connectors** Output terminals at the drive or motor have corrosion, burns, or poor contact that interrupts the V-phase path.
- **Motor winding fault** An open winding inside the motor on phase V presents the same symptom as a missing external conductor.
- **Failed drive output stage on the V leg** The inverter or IGBT section for phase V inside the drive has failed, preventing current flow even when wiring is intact.

## Step-by-Step Fix {#fix}

1. Lock out all power to the drive and wait for DC link capacitors to discharge before opening any compartments or touching terminals.
2. Inspect and tighten all motor output terminals, paying close attention to the V phase connection at both the drive output block and the motor terminal box.
3. Check continuity of the V-phase conductor from the drive to the motor with power removed, using a digital multimeter on the resistance or continuity setting.
4. Examine cables, cable glands, and terminals for physical damage, heat discoloration, corrosion, or signs of arcing that could cause an open circuit.
5. Isolate the motor by disconnecting it from the drive and test whether the alarm persists with a known-good motor and cable set to determine if the fault is external or internal to the drive.
6. Measure motor winding resistance if cable continuity is confirmed good, looking for an open winding on phase V that would register infinite resistance.
7. Replace or repair the drive power section or inverter module if both the motor and wiring test good, since a failed V-leg output can mimic a missing phase.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable assembly (phase V conductor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-31-fault-code&k=Motor+cable+assembly+%28phase+V+conductor%29&tag=errorcodefixes-20) \| If the V-phase wire is damaged, severed, or shows signs of overheating or insulation failure. |
| Output terminal blocks or connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-31-fault-code&k=Output+terminal+blocks+or+connectors&tag=errorcodefixes-20) \| Replace if terminals are burned, corroded, or mechanically damaged and cannot be cleaned or tightened. |
| Drive power module or IGBT section | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-31-fault-code&k=Drive+power+module+or+IGBT+section&tag=errorcodefixes-20) \| Required if the V-leg output stage has failed internally and wiring plus motor have been confirmed good. |

## When to Call a Pro

Call a qualified drives technician or authorized Danfoss service provider if you are not trained in high-voltage DC and AC power systems, if lockout and capacitor discharge procedures are unfamiliar, or if initial wiring and terminal checks do not resolve the alarm. Internal drive power-section faults require specialized diagnostic tools and replacement modules that must match your FC 302 frame size and firmware. A professional can also perform load testing and waveform analysis to confirm whether the fault is in the inverter stage or the motor.

## See Also

- [Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix](/posts/danfoss-fc301-fault-al-14/)
- [Danfoss VLT 2900 Fault Codes: Complete Guide](/posts/danfoss-vlt-2900-faults/)
- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/posts/danfoss-fc302-alarm-13/)
- [Danfoss FC302 ALARM 26 - Causes & Fix](/posts/danfoss-fc302-alarm-26-fault-code/)
