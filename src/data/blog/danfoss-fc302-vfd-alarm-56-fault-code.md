---
title: "Danfoss FC302 VFD ALARM 56 - Causes & Fix"
description: "ALARM 56 on Danfoss FC302 means 'AMA interrupted by user.' The fix is to restart Automatic Motor Adaptation and let it finish uninterrupted."
pubDatetime: 2026-06-05T09:47:50Z
modDatetime: 2026-06-05T09:47:50Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 VFD ALARM 56 — What It Means

ALARM 56 on a Danfoss VLT AutomationDrive FC 302 means 'AMA interrupted by user.' The Automatic Motor Adaptation procedure was manually stopped before it could complete. This is not a component failure or drive fault. The alarm appears because someone pressed stop, reset, or otherwise exited the AMA sequence. Danfoss documentation shows the correct action is to restart the AMA routine and allow it to run to completion without interruption.

[Jump to Fix](#fix)

## Common Causes

- **Operator pressed stop during AMA** A technician or operator manually aborted the Automatic Motor Adaptation sequence from the keypad or HMI before it finished.
- **Control logic interrupted the routine** An external control signal, PLC command, or programmed interlock stopped the AMA process mid-cycle.
- **Drive reset or power cycle during AMA** The drive was reset or powered off while AMA was running, terminating the procedure before completion.
- **User exited setup menu prematurely** The operator navigated away from the AMA screen or exited commissioning mode before the adaptation routine concluded.
- **Repeated alarm despite no manual stop** If the alarm returns even when you do not interrupt AMA, the drive or motor setup may have an issue preventing successful completion, though ALARM 56 itself still indicates user interruption.

## Step-by-Step Fix {#fix}

1. {'lead': 'Verify the drive state', 'text': 'Confirm the FC 302 is in an AMA routine and not another diagnostic or parameter-change mode by checking the display or HMI status.'}
2. {'lead': 'Check for manual abort', 'text': 'Review whether the procedure was stopped by pressing a button, issuing a reset command, or an external control signal from a PLC or operator panel.'}
3. {'lead': 'Clear the alarm', 'text': 'Press the reset button on the keypad or send a reset command from the control interface to clear ALARM 56 from the display.'}
4. {'lead': 'Restart the AMA procedure', 'text': 'Navigate to the AMA start menu on the FC 302 keypad (consult your manual for the exact parameter path) and initiate the Automatic Motor Adaptation routine again.'}
5. {'lead': 'Let the routine complete uninterrupted', 'text': 'Do not press stop, reset, or change parameters while AMA is running, and make sure no external control signals will halt the process.'}
6. {'lead': 'Repeat if the alarm returns', 'text': 'If ALARM 56 appears again, restart AMA once more and verify the motor is connected correctly and the drive parameters match the motor nameplate (voltage, frequency, power).'}
7. {'lead': 'Review installation if AMA fails repeatedly', 'text': 'If the drive will not complete AMA after multiple attempts, check motor wiring, cable shielding, and drive configuration settings, because the alarm itself does not point to a specific failed component.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 control keypad (LCP) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-56-fault-code&k=Danfoss+FC+302+control+keypad+%28LCP%29&tag=errorcodefixes-20) \| Only if the existing keypad is damaged or unresponsive and preventing you from restarting AMA. |

## When to Call a Pro

Call a qualified VFD technician or controls specialist if the AMA routine fails to complete after three or four attempts, if you are unfamiliar with the FC 302 commissioning menus, or if other alarms appear alongside ALARM 56. A professional can verify motor parameters, cable installation, and drive configuration to determine why AMA cannot finish. Because ALARM 56 is procedural rather than a component fault, most issues resolve by simply restarting the adaptation and allowing it to run, but persistent failures may indicate deeper setup or wiring problems that require systematic troubleshooting.
