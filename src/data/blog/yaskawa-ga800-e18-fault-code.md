---
title: "Yaskawa GA800 E18 Error - Causes & Fix"
description: "Yaskawa GA800 E18 (Back EMF Error) occurs when induced-voltage tuning results fall outside range. Fix motor data and rerun auto-tune."
pubDatetime: 2026-05-30T12:30:39Z
modDatetime: 2026-05-30T12:30:39Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Replacement motor"
most_likely_cause: "Incorrect motor nameplate data entered"
---

## Yaskawa GA800 E18 Error — What It Means

E18 or Er-18 on the Yaskawa GA800 is a Back EMF Error. It appears when the drive completes an induced-voltage tuning routine but the result falls outside the acceptable range. In practical terms, the drive attempted to identify motor characteristics during auto-tuning and could not arrive at a valid outcome, so it assumes the motor data or tuning conditions are wrong.

This fault does not indicate a burned component or failed circuit board in most cases. Instead, it tells you the drive could not match what it measured from the motor against what it expected based on the programmed parameters. The tuning process measures back electromotive force to build an accurate motor model, and when those measurements do not align with the nameplate data you entered, the drive throws E18 and halts.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor nameplate data entered** Voltage, current, frequency, power, or pole count programmed into the drive does not match the actual motor nameplate.
- **Motor disconnected or miswired** Loose output terminals, missing phase, or swapped leads prevent the drive from reading correct back EMF during tuning.
- **Auto-tune run with motor under load** Running tuning while the motor is coupled to a machine or under mechanical load skews the induced-voltage measurement.
- **Wrong motor selected for the drive rating** Motor horsepower or current rating exceeds the drive capability or falls far below, making tuning results invalid.
- **Previous tuning data corrupted or incomplete** An interrupted or failed earlier auto-tune left partial data that conflicts with a new attempt.

## Step-by-Step Fix {#fix}

1. **Clear the fault** by pressing the reset button or cycling drive power, then navigate to the alarm history to confirm E18 is the active code.
2. **Verify motor nameplate data** by comparing every parameter (voltage, rated current, frequency, power, poles, speed) on the physical motor plate against what is programmed in the drive's motor data registers.
3. **Inspect motor wiring** at the drive output terminals and at the motor junction box to confirm all three phases are tight, correctly landed, and that no phase is open or shorted to ground.
4. **Decouple the motor** from the driven load if possible, or verify the shaft can spin freely and is not mechanically bound during the tuning routine.
5. **Rerun auto-tuning** using the drive's tuning function menu, ensuring the motor is stationary and unloaded, and allow the routine to complete without interruption.
6. **Check the fault again** after tuning finishes. If E18 reappears, re-enter motor nameplate data from scratch and repeat the tuning sequence.
7. **Document drive model, serial number, and all motor nameplate data** if the fault persists after two clean tuning attempts, then contact Yaskawa technical support with that information and the application details.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e18-fault-code&k=Replacement+motor&tag=errorcodefixes-20) \| Required only if the existing motor nameplate is damaged, unreadable, or if the motor itself fails electrical tests after correct data entry and tuning attempts. |
| Output reactor or line reactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e18-fault-code&k=Output+reactor+or+line+reactor&tag=errorcodefixes-20) \| Consult factory documentation if your application requires one and it is missing, as some installations need reactors for long motor cables or to reduce reflected wave effects during tuning. |

## When to Call a Pro

Call a qualified drive technician or Yaskawa-authorized service provider if the E18 fault returns after you have verified motor nameplate data twice, checked all wiring, and completed two separate auto-tune cycles with the motor uncoupled. Persistent back EMF errors can indicate a failing motor winding, a drive measurement circuit issue, or an application mismatch that requires detailed motor testing and drive configuration beyond basic parameter entry. Also contact support if you do not have the original motor nameplate or documentation, since guessing at motor data will cause repeated tuning failures and may damage the motor or drive.

## See Also

- [Yaskawa GA800 E08 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e08-fault-code/)
- [Yaskawa GA800 E02 Fault - Causes & Fix](/posts/yaskawa-ga800-e02-fault-code/)
- [Yaskawa GA800 E16 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e16-fault-code/)
- [Yaskawa VFD Fault PF — Causes & Fix](/posts/yaskawa-vfd-fault-pf/)
