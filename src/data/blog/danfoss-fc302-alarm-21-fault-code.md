---
title: "Danfoss FC302 Alarm 21 - Causes & Fix"
description: "Danfoss FC302 Alarm 21 means a parameter is out of range or invalid. Learn the real causes, step-by-step fix, and when to call a tech."
pubDatetime: 2026-05-29T09:43:24Z
modDatetime: 2026-05-29T09:43:24Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 21 — What It Means

Alarm 21 on the Danfoss FC302 is a Parameter Error. The drive has detected that a parameter value is out of its permitted range, or the parameter number itself is being displayed as an error condition. The Danfoss manual states this clearly: the parameter is out of range. This is not a motor or power fault. It is a configuration problem, usually triggered by an incorrect value during setup, commissioning, or after a parameter transfer.

[Jump to Fix](#fix)

## Common Causes

- **Parameter value outside allowed range** You entered or changed a parameter to a value that exceeds the minimum or maximum limit defined for that specific parameter.
- **Parameter mismatch after copy or download** A parameter set was transferred from another drive or file, and one or more values do not fit the motor, application, or drive configuration.
- **Corrupted parameter data** The drive's stored parameter data became inconsistent or corrupted after an interrupted load, improper reset, or incomplete initialization sequence.
- **Displayed parameter number error** The LCP keypad is showing a parameter reference instead of normal fault text, which can appear as Alarm 21 in some support documentation.
- **Incorrect startup sequence** A parameter was changed or initialized in the wrong order, leaving the drive in an inconsistent state that triggers the out-of-range alarm.

## Step-by-Step Fix {#fix}

1. **Read the exact parameter number and value** displayed on the LCP when Alarm 21 appears, because this fault is always tied to a specific parameter.
2. **Identify the last parameter you changed** before the alarm occurred and look it up in the FC302 programming guide to confirm the allowed range.
3. **Correct the parameter value** so it falls within the permitted min/max range, then press the Off/Reset button on the keypad to clear the alarm.
4. **Review the full parameter set** if the alarm appeared after a parameter transfer or commissioning change, paying close attention to motor data and control configuration for compatibility.
5. **Perform an initialization to default settings** if multiple parameters appear inconsistent or the alarm persists, then carefully re-enter the correct application data step by step.
6. **Verify the control panel and parameter storage process** if the alarm returns even with valid parameter values, checking for keypad or control card data issues before replacing hardware.
7. **Document the faulty parameter number and value** for future reference, especially if you need to contact Danfoss support or if the drive shows signs of configuration corruption.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 LCP (Local Control Panel) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-21-fault-code&k=Danfoss+FC302+LCP+%28Local+Control+Panel%29&tag=errorcodefixes-20) \| Only needed if the keypad itself is displaying corrupted parameter data or fails to store valid values after reinitialization. |
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-21-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Consider only if parameter corruption persists after default reset and you have ruled out all configuration errors. |

## When to Call a Pro

Call a qualified VFD technician if you cannot identify which parameter is out of range, if the alarm returns immediately after correction, or if the drive will not accept valid parameter values even after a default initialization. Also call for help if you are unfamiliar with the FC302 programming structure or if the alarm appeared without any recent parameter changes, as this may indicate a deeper control card or storage issue that requires diagnostic tools and Danfoss support access.
