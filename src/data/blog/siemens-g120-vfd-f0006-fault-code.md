---
title: "Siemens G120 F0006 Fault - Causes & Fix"
description: "F0006 means chip temperature is critically high. Check motor sizing, verify thermal parameters, and inspect load cycle before replacing power module."
pubDatetime: 2026-06-01T11:37:01Z
modDatetime: 2026-06-01T11:37:01Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F0006 Fault — What It Means

F0006 on a Siemens SINAMICS G120 means the drive has detected a critical chip-temperature rise in the power electronics and has tripped with an OFF2 shutdown. This is not a simple overtemp alarm you can reset and ignore. The drive is protecting itself from thermal damage. Siemens fault documentation points to both application-level causes (overload, incorrect motor sizing, excessive switching frequency) and hardware failure in the inverter power stage when the fault persists.

[Jump to Fix](#fix)

## Common Causes

- **Overload or excessive duty cycle** The drive is being asked to deliver more torque or current than its thermal capacity allows, especially in applications with continuous high load.
- **Motor power mismatch** Motor power (p0307) does not align with inverter power (r0206), causing the drive to work harder than it was sized for.
- **Excessive switching frequency** High PWM switching frequency creates thermal stress in the power stage, and Siemens specifically mentions parameter P0290 = 0 or 2 as a preventive setting for F0006.
- **Incorrect motor thermal parameters** Motor nominal overtemperature values in p0626–p0628 are not set correctly, confusing the drive's thermal model.
- **Failed inverter power module** When thermal conditions are correct but the fault persists, the internal power electronics have failed and require replacement.

## Step-by-Step Fix {#fix}

1. **Verify the load profile and duty cycle.** Confirm the application is not demanding more continuous torque or current than the drive's thermal rating allows.
2. **Check motor and drive sizing.** Compare motor power in parameter p0307 against inverter power shown in r0206 to confirm they match.
3. **Inspect motor thermal data.** Review parameters p0626 through p0628 to verify motor nominal overtemperature values are correctly entered for your motor.
4. **Review switching frequency setting.** If your application has triggered this fault before, check parameter P0290 and try setting it to 0 or 2 as Siemens recommends to reduce thermal stress.
5. **Inspect cooling conditions.** Check airflow around the drive, clean any blocked vents, and confirm cabinet ventilation is adequate for the installed load.
6. **Clear the fault and test.** After correcting parameters or improving cooling, acknowledge the fault and run a controlled test cycle to see if F0006 returns.
7. **Replace the inverter power module if fault persists.** When thermal settings and load conditions are correct but the drive still trips, contact Siemens service for power module replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 inverter power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0006-fault-code&k=Siemens+G120+inverter+power+module&tag=errorcodefixes-20) \| Required when hardware failure is confirmed. Contact Siemens or an authorized distributor for the correct module for your frame size. |

## When to Call a Pro

Call a qualified technician or Siemens service immediately if the fault returns after you have verified motor sizing, corrected thermal parameters, and confirmed adequate cooling. Persistent F0006 after parameter corrections indicates a hardware failure in the power stage that requires factory-authorized replacement of the inverter power module. Do not attempt repeated resets without addressing the root cause, because continued operation with a real thermal fault can damage the drive permanently.
