---
title: "Siemens G120 F01018 - Causes & Fix"
description: "Siemens G120 F01018 means the drive's booting was interrupted repeatedly. Learn the causes and step-by-step repair to clear this fault."
pubDatetime: 2026-05-27T10:41:39Z
modDatetime: 2026-05-27T10:41:39Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F01018 — What It Means

F01018 on a Siemens SINAMICS G120 indicates that the drive's booting process was interrupted multiple times. When this happens, the module automatically boots using factory settings instead of your saved configuration. Siemens documents this as a startup recovery behavior triggered by repeated incomplete boot cycles.

The fault is cleared by performing a full POWER ON cycle (powering down completely, then restarting). The drive is trying to protect itself after detecting that it could not complete a normal startup sequence. Once power is stable and the boot completes cleanly, the drive should restore normal operation from user data if available.

[Jump to Fix](#fix)

## Common Causes

- **Power interruption during startup** The drive loses supply voltage or experiences voltage sags while the control unit is initializing, preventing the boot sequence from finishing.
- **Control unit CPU crash** An internal processor fault or boot failure stops the control unit from completing its startup routine.
- **Invalid or corrupted user data** Stored parameter settings are damaged or contain invalid values that prevent the drive from booting normally.
- **Incomplete boot after firmware update** A recent firmware flash or component replacement was not followed by the required full power cycle, leaving the drive in an incomplete startup state.
- **Unstable control power supply** Loose terminals, faulty contactors, or upstream disconnects cause the control electronics to drop out during the boot window.
- **Repeated power cycles without discharge time** Rapidly cycling power on and off does not allow the drive to complete initialization or fully discharge before restart.

## Step-by-Step Fix {#fix}

1. **Check the supply voltage stability** at the drive terminals and upstream disconnect. Verify that the drive is receiving clean, uninterrupted power during startup with no voltage sags or contactor dropouts.
2. **Perform a full POWER ON reset** by shutting down the drive completely, waiting at least 30 seconds for internal capacitors to discharge, then powering it back up. This is the Siemens-specified remedy for F01018.
3. **Monitor the boot sequence** during restart. Watch for any interruptions, flickering indicators, or error messages that would indicate the drive is still losing power or failing to initialize.
4. **Verify parameter integrity** if the fault repeats after a clean reboot. Review recent commissioning changes or parameter uploads for invalid values or corruption, particularly if the drive boots to factory settings each time.
5. **Inspect control wiring and terminals** for loose connections, oxidation, or intermittent contact that could interrupt the control unit during its boot cycle. Tighten all connections and clean any corroded terminals.
6. **Review recent maintenance activity** if the fault appeared after a firmware update or module swap. Repeat the power cycle procedure for all drive components to allow full initialization.
7. **Replace the control unit** if the fault persists after verifying stable power, clean wiring, and valid user data. Recurring boot interruption after these checks points to an internal control module failure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens SINAMICS G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01018-fault-code&k=Siemens+SINAMICS+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| If the fault repeats after verified stable power and data, the control unit itself may have a failed boot processor. |
| G120 parameter backup module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01018-fault-code&k=G120+parameter+backup+module&tag=errorcodefixes-20) \| To restore corrupted user data if the drive continues resetting to factory defaults after each startup. |

## When to Call a Pro

Call a qualified technician or Siemens service if the fault returns after you have verified stable supply voltage, performed a complete power cycle, and checked for parameter corruption. Persistent F01018 after these steps usually means an internal control unit failure or a complex commissioning issue that requires diagnostic software and replacement parts. Also contact support if the drive boots to factory settings every time despite having valid user data loaded, or if you are unfamiliar with VFD parameter management and firmware procedures.
