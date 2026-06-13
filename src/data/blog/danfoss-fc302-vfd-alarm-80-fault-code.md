---
title: "Danfoss FC302 VFD Alarm 80 - Causes & Fix"
description: "Alarm 80 means the Danfoss FC302 drive has been initialized to default values. Clear the alarm by resetting the unit, then reload your saved parameter set."
pubDatetime: 2026-06-05T09:49:02Z
modDatetime: 2026-06-05T09:49:02Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control card (PCB)"
---

## Danfoss FC302 VFD Alarm 80 — What It Means

Alarm 80 on a Danfoss VLT AutomationDrive FC 302 indicates the drive has been initialized to default values. This is not a hardware fault. The drive's parameter settings have been reset to factory defaults, typically after a manual reset or commissioning procedure. Danfoss documentation describes this as "Drive initialised to default value" and notes that it appears when the drive powers up after a successful initialization. The alarm itself signals that your custom application parameters have been replaced with the factory baseline settings, rather than pointing to a failed power component or motor issue.

[Jump to Fix](#fix)

## Common Causes

- **Manual reset or initialization** A deliberate reset procedure or commissioning process that restores all parameters to factory defaults.
- **Lost parameter set after service** Configuration was overwritten or erased during control board replacement, parameter download, or maintenance work.
- **Interrupted parameter download** A parameter transfer or programming session was stopped partway through, leaving the drive in default state.
- **Control board replacement without parameter restore** A new or swapped control card was installed but the saved application parameters were not reloaded.
- **Unexpected configuration loss** The drive reverted to defaults on its own, suggesting a problem with parameter storage on the control side.

## Step-by-Step Fix {#fix}

1. **Verify whether the reset was intentional.** If you just commissioned the drive or performed a manual reset, confirm that returning to factory defaults was the goal and check whether your application parameters need to be reloaded.
2. **Clear the alarm by resetting the unit.** Danfoss specifies that Alarm 80 is cleared by performing a reset on the drive.
3. **Cycle power to the drive.** Turn off main power, wait 30 seconds, then restore power to see whether Alarm 80 returns on its own.
4. **Reload your saved parameter set from backup.** If the drive has reverted to defaults and you have a backup file or written parameter list, download or re-enter the correct application settings now.
5. **Check commissioning integrity if the alarm recurs.** Confirm that the correct parameters are present, that any replaced control card is programmed properly, and that the drive is not losing settings between power cycles.
6. **Inspect the control card and parameter storage.** If Alarm 80 appears repeatedly without manual resets, suspect a control board or memory retention problem rather than a motor or output-stage fault.
7. **Document your final parameter set.** Once the drive is running with the correct application settings, save a backup file and keep a written copy to simplify future recovery.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control card (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-80-fault-code&k=Danfoss+FC302+control+card+%28PCB%29&tag=errorcodefixes-20) \| Required if the drive cannot retain or restore parameter settings and Alarm 80 recurs after each power cycle. |
| Parameter backup file or commissioning record | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-80-fault-code&k=Parameter+backup+file+or+commissioning+record&tag=errorcodefixes-20) \| Not a physical part but essential for restoring your application settings after a reset to defaults. |

## When to Call a Pro

Call a qualified drives technician or Danfoss service partner if Alarm 80 reappears on its own after you have cleared it and cycled power, especially if you did not perform a manual reset. Recurring initialization to defaults without user intervention points to a control card or parameter storage issue that requires diagnostic tools and familiarity with VFD commissioning. Also seek professional help if you do not have a backup of your application parameters and the drive controls a complex process, because incorrect motor control settings can damage equipment or create unsafe operating conditions.

## See Also

- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
- [Danfoss FC302 VFD Alarm 44 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-44-fault-code/)
- [Danfoss FC302 ALARM 36 - Causes & Fix](/posts/danfoss-fc302-alarm-36-fault-code/)
- [Danfoss FC302 ALARM 30 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-30-fault-code/)
