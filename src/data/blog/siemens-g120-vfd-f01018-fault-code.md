---
title: "Siemens F01018 - Causes & Fix"
description: "F01018 means the G120 drive's power-up was interrupted multiple times and it reverted to factory settings. Fix by checking supply power stability first."
pubDatetime: 2026-05-31T11:15:32Z
modDatetime: 2026-05-31T11:15:32Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens F01018 — What It Means

Fault F01018 on a Siemens SINAMICS G120 indicates that the drive's controller detected repeated interrupted boot attempts during startup. When this happens, the drive automatically reverts to factory settings as a fallback. The fault typically points to an unstable power supply during the power-up sequence, a corrupted parameter set, or an internal CPU issue preventing normal boot completion.

[Jump to Fix](#fix)

## Common Causes

- **Unstable or interrupted control power during startup** Voltage sags, brown-outs, or intermittent supply during the boot sequence prevent the controller from completing initialization.
- **Repeated reboot or reset events** Multiple power cycles in quick succession or intermittent supply connections force the drive to abort startup more than once.
- **Invalid or corrupted parameterization** Startup data stored in the drive is damaged or contains invalid values that prevent the controller from booting normally.
- **Loose or corroded supply terminals** Poor connections at the incoming power or control terminals cause intermittent contact during the critical power-up phase.
- **Failing control-unit module or CPU** Internal electronics in the control unit crash repeatedly during boot, triggering the fault even when external power is stable.

## Step-by-Step Fix {#fix}

1. **Fully power down the drive** and disconnect all supply power, then wait for the DC bus to discharge completely before attempting any further action.
2. **Power the drive back on** once only and observe whether F01018 reappears immediately or if the drive completes a normal boot cycle.
3. **Check incoming power supply stability** by measuring line voltage during startup with a meter to confirm no sags or drops occur, and inspect all power and control terminals for loose, corroded, or intermittent connections.
4. **Read the fault buffer** in the drive's diagnostics menu to review the complete fault history and check for other startup-related errors that preceded F01018.
5. **Inspect and verify drive parameterization** by reviewing commissioning data and startup parameters for invalid or corrupted values, or reload a known-good parameter set from backup.
6. **Test with a clean power cycle** after correcting any supply or parameter issues, and monitor the drive through several full startup sequences to confirm stable operation.
7. **Replace or reprogram the control unit** if F01018 persists after confirming stable supply power and valid parameters, since repeated boot interruption points to a control-side hardware failure rather than an external load problem.

## Parts Often Needed

| Part | Notes |
|------|-------|
| G120 Control Unit Module (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01018-fault-code&k=G120+Control+Unit+Module+%28CU%29&tag=errorcodefixes-20) \| Required if repeated boot failures persist after supply and parameter checks. Confirm your exact G120 model and CU variant before ordering. |
| Siemens parameter backup memory card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01018-fault-code&k=Siemens+parameter+backup+memory+card&tag=errorcodefixes-20) \| Useful for restoring known-good parameter sets if corrupted commissioning data is suspected. |

## When to Call a Pro

Call a qualified Siemens technician or certified drive specialist if F01018 returns immediately after a clean power cycle and you have confirmed stable incoming power and valid parameterization. Repeated boot interruptions that survive basic supply and parameter troubleshooting usually indicate an internal control-unit fault requiring specialized diagnostic tools, firmware updates, or module replacement. If the drive is mission-critical or connected to expensive machinery, professional support will prevent extended downtime and avoid damage from trial-and-error parts swapping.
