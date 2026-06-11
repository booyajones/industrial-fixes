---
title: "Danfoss FC302 Alarm 47 - Causes & Fix"
description: "Alarm 47 on Danfoss FC302 VFD means 24V control supply is low. Most often caused by overloaded or shorted control wiring on terminal 50."
pubDatetime: 2026-06-03T10:52:40Z
modDatetime: 2026-06-03T10:52:40Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control card"
---

## Danfoss FC302 Alarm 47 — What It Means

Alarm 47 on a Danfoss VLT FC302 drive indicates the internal 24 V control supply voltage has dropped out of range. This is a control power fault, not a motor or input power issue. The drive generates three internal supplies through its switch-mode power supply (SMPS), and this alarm means the 24 V rail that powers the control circuits is sagging or failing.

The fault can come from external wiring that overloads the 24 V output or from a failure inside the drive's power card or control card. Danfoss directs technicians to isolate the problem by disconnecting terminal 50 wiring first. If the alarm clears, the issue is in your field wiring. If it stays, the control card or internal SMPS section has failed.

[Jump to Fix](#fix)

## Common Causes

- **Overloaded 24 V control circuit** External devices or incorrect wiring pull too much current from the drive's 24 V control supply, dragging the voltage down.
- **Short circuit on terminal 50 wiring** A short in the field control wiring connected to terminal 50 loads the supply and triggers the alarm.
- **Failed control card** The control card that regulates or monitors the 24 V supply has failed internally and cannot maintain correct voltage.
- **Failed SMPS section on power card** The switch-mode power supply circuit on the power card that generates the 24 V control rail is not working properly.
- **Miswired control circuit** Incorrect wiring connections to the control terminals create a load or short path that the 24 V supply cannot handle.
- **Downstream component fault** A component connected to the control supply inside the drive pulls excessive current or shorts internally, collapsing the 24 V rail.

## Step-by-Step Fix {#fix}

1. **Power down and lockout** the drive following all electrical safety procedures before touching any wiring or components.
2. **Disconnect all wiring from terminal 50** and any other 24 V control circuit terminals, then power the drive back on and check if Alarm 47 clears.
3. **If the alarm clears**, inspect all removed control wiring for shorts, damage, or incorrect connections, and verify that connected external devices do not exceed the 24 V supply current rating.
4. **Reconnect control wiring one circuit at a time** to identify which load or wire causes the alarm to return, then repair or remove that circuit.
5. **If the alarm does not clear** with all terminal 50 wiring removed, power down again and replace the control card per Danfoss instructions.
6. **Verify the 24 V control supply voltage** is stable and within range after repair, using a multimeter on the appropriate test points if accessible.
7. **Return the drive to service** and monitor for the alarm during the first few run cycles to confirm the repair resolved the issue.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-47-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Replace if Alarm 47 does not clear with all terminal 50 wiring disconnected. |
| Danfoss FC302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-47-fault-code&k=Danfoss+FC302+power+card&tag=errorcodefixes-20) \| Required if the SMPS section that generates the 24 V supply has failed internally. |

## When to Call a Pro

Call a qualified drive technician or automation electrician if you are not trained to work safely inside energized VFD cabinets or if the alarm does not clear after removing external control wiring. Replacing control cards and power cards requires knowledge of VFD internal layouts, proper ESD handling, and sometimes firmware transfer or parameter backup. If you cannot isolate the fault using the terminal 50 disconnect test, or if you find the fault comes back intermittently, a technician with a scope and schematics can trace the 24 V supply path and identify failed components on the power card that are not field-replaceable without board-level repair.
