---
title: "Siemens G120 F01033 - Causes & Fix"
description: "Siemens G120 fault F01033 means a reference parameter is set to 0.0 during unit switchover. Fix by setting p0304, p0305, or related parameters to valid nonzero values."
pubDatetime: 2026-05-27T10:42:45Z
modDatetime: 2026-05-27T10:42:45Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F01033 — What It Means

F01033 on a Siemens SINAMICS G120 means the drive detected an invalid value during a unit switchover or scaling conversion. Specifically, one of the required reference parameters for speed or unit display is set to 0.0 when it must contain a valid nonzero value. This fault appears during commissioning, parameter uploads, or after a parameter reset when the drive tries to convert or display units but finds a missing or zeroed reference value. It is a configuration problem, not a hardware failure in the power stage or control board.

[Jump to Fix](#fix)

## Common Causes

- **Reference parameter left at 0.0 during commissioning** One of the key scaling parameters such as p0304, p0305, p0310, p0596, or p2000 through p2003 was never set or was accidentally cleared to zero.
- **Parameter restore or factory reset** A parameter upload, factory reset, or drive replacement restored default values that left reference parameters at 0.0 without re-entering the application-specific scaling values.
- **Inconsistent unit conversion setup** Unit display or reference mode was changed without updating the corresponding reference parameter values to match the new unit system.
- **Corrupted or incomplete parameter download** A partial parameter set was loaded from a backup or commissioning tool, leaving some reference values unpopulated or zeroed.
- **Change to speed reference source without updating scaling** The speed reference or setpoint source was switched but the associated reference parameter for that input was not configured with a valid nonzero value.

## Step-by-Step Fix {#fix}

1. **Access the fault buffer** on the G120 using the BOP-2 keypad or commissioning software to confirm the active fault is F01033 and note the time and any recent parameter changes.
2. **Check parameters p0304, p0305, p0310, p0596, p2000, p2001, p2002, p2003** using the keypad or STARTER software to identify which reference parameter is currently set to 0.0.
3. **Set the relevant reference parameter to a valid nonzero value** that matches your application's speed or unit scaling, consulting the original commissioning sheet or the drive's rated speed and application requirements.
4. **Verify related unit and display parameters** to confirm the scaling and unit conversion settings are consistent with the newly entered reference value.
5. **Acknowledge the fault** and reset the drive, or power-cycle the G120 if the fault does not clear immediately after parameter correction.
6. **Test drive operation** by commanding a speed reference and observing that the drive runs normally and displays the correct speed units without retriggering F01033.
7. **Re-check commissioning data or consult Siemens support** if the fault persists after confirming all reference parameters are nonzero, as this may indicate a deeper parameter conflict or corrupted dataset.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 parameter backup file or commissioning dataset | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01033-fault-code&k=Siemens+G120+parameter+backup+file+or+commissioning+dataset&tag=errorcodefixes-20) \| If your original commissioning values are lost, obtain a known-good parameter set for your application before attempting to re-enter scaling values. |
| Siemens STARTER or SINAMICS G120 Smart Access software license | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01033-fault-code&k=Siemens+STARTER+or+SINAMICS+G120+Smart+Access+software+license&tag=errorcodefixes-20) \| Required for full parameter access and backup if using a PC-based commissioning tool instead of the basic operator panel. |

## When to Call a Pro

Call a Siemens-trained drives technician or automation integrator if you do not have access to the original commissioning parameters, if the fault reappears after setting valid reference values, or if you are unfamiliar with G120 parameter structure and unit scaling. This fault does not indicate a failed component, but incorrect parameterization can prevent proper operation or cause nuisance trips. A qualified technician can compare your current parameter set against the application requirements, verify unit conversion logic, and restore a complete commissioning dataset if needed.

## See Also

- [Siemens G120 F01018 - Causes & Fix](/posts/siemens-g120-f01018-fault-code/)
- [Siemens Micromaster F0052 - Causes & Fix](/posts/siemens-micromaster-f0052-fault-code/)
- [Siemens SINAMICS G120X Fault Codes: Complete Guide](/posts/siemens-g120x-fault-codes/)
- [Siemens G120 F01044 - Causes & Fix](/posts/siemens-g120-f01044-fault-code/)
