---
title: "Danfoss FC302 VFD Alarm 41 - Causes & Fix"
description: "Alarm 41 means overload on digital output terminal 29. Disconnect the load from terminal 29, check for shorts, and verify parameters."
pubDatetime: 2026-06-03T10:49:12Z
modDatetime: 2026-06-03T10:49:12Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 VFD Alarm 41 — What It Means

Alarm 41 on the Danfoss VLT FC 302 indicates an overload of digital output terminal 29. This fault means the terminal is drawing too much current, either from an excessive load, a short circuit in the connected wiring, or incorrect configuration settings. Terminal 29 is a programmable digital output, and the drive's protection circuitry has detected current beyond its safe operating range.

The alarm is specifically tied to terminal 29 and does not indicate a motor or main power issue. Most occurrences trace to external wiring problems or devices connected to that terminal that exceed its capacity. Once the overload condition is removed and the alarm is reset, normal operation typically resumes if no internal drive damage has occurred.

[Jump to Fix](#fix)

## Common Causes

- **Excessive current draw from connected load** The device or relay coil wired to terminal 29 is pulling more current than the output can safely supply.
- **Short circuit in terminal 29 wiring** Damaged wire insulation, pinched cables, or miswiring has created a direct short to ground or another terminal.
- **Incorrect parameter configuration** Parameter 5-00 Digital I/O Mode or parameter 5-02 Terminal 29 Mode is set incorrectly for the intended output function.
- **Defective external load device** A relay, pilot light, or other accessory connected to terminal 29 has failed internally and is drawing fault current.
- **Damaged drive output circuitry** The output stage for terminal 29 on the control board has been weakened or damaged by a previous overload event.

## Step-by-Step Fix {#fix}

1. **Power down the drive safely** and lock out the power source before inspecting any wiring or connections.
2. **Inspect the wiring at terminal 29** for visible damage, loose strands, pinched insulation, or signs of arcing or burning.
3. **Disconnect the load** connected to terminal 29 and isolate the output terminal completely from any external devices.
4. **Power up the drive** and reset Alarm 41 using the control panel or by cycling power, then observe whether the fault returns with no load attached.
5. **If the alarm clears with the load removed**, test or replace the external device and its wiring, then reconnect and verify normal operation.
6. **If the alarm persists with no load**, navigate to parameter 5-00 Digital I/O Mode and parameter 5-02 Terminal 29 Mode and verify they match the intended output function per the manual.
7. **Restore correct parameter values** if they were changed or corrupted, save the settings, reset the alarm, and test again. If the fault still appears with correct wiring and settings, the drive's output circuit for terminal 29 is likely damaged and requires professional repair or control board replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement wiring harness or terminal block connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-41-fault-code&k=Replacement+wiring+harness+or+terminal+block+connector&tag=errorcodefixes-20) \| If wiring to terminal 29 is damaged or burnt beyond field repair. |
| Danfoss FC 302 control card or I/O board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-41-fault-code&k=Danfoss+FC+302+control+card+or+I%2FO+board&tag=errorcodefixes-20) \| Required if the output circuitry for terminal 29 is internally damaged and the alarm persists with correct wiring and parameters. |

## When to Call a Pro

Call a qualified technician or Danfoss service provider if the alarm continues after you have disconnected the load, verified wiring integrity, and confirmed correct parameter settings. Persistent Alarm 41 with no external cause points to internal damage on the drive's control board, which requires specialized diagnostic tools, board-level repair skill, and access to OEM replacement parts. If your application is critical or you are unfamiliar with VFD parameter programming, professional support is recommended from the start to avoid extended downtime or further equipment damage.
