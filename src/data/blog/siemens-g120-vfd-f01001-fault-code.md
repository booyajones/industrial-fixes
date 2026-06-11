---
title: "Siemens G120 F01001 - Causes & Fix"
description: "F01001 means a floating-point software exception in the G120 drive. Power-cycle completely, then check firmware and control-unit health."
pubDatetime: 2026-05-31T11:14:28Z
modDatetime: 2026-05-31T11:14:28Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
---

## Siemens G120 F01001 — What It Means

F01001 is a FloatingPoint exception fault on the Siemens SINAMICS G120. It signals that an error occurred during a floating-point calculation inside the drive's internal software or control logic. This is not a motor, wiring, or power-stage issue. The fault comes from the drive's basic system or an OA application such as FBLOCKS or DCC. The drive reacts by shutting down (OFF2) and requires a full power-off/power-on cycle (POWER ON) to acknowledge and clear the fault.

Because F01001 is a software-level fault, the typical causes are corrupted configuration data, a firmware bug, or a failing Control Unit. The drive's diagnostic buffer (parameter r0945) will record the event. You will not find motor resistance values or voltage thresholds tied to this code. Instead, focus on resetting the controller, verifying parameter settings, updating firmware if available, and replacing the Control Unit if the fault persists after a clean reboot.

[Jump to Fix](#fix)

## Common Causes

- **Transient processor exception** A temporary error in the drive's CPU during a floating-point math operation triggers the fault without indicating permanent damage.
- **Corrupted or incompatible FBLOCKS configuration** Custom function blocks or DCC chart data can produce invalid signals that crash the floating-point engine in the control software.
- **Firmware bug or outdated software version** Known software defects in older firmware revisions can cause repeated floating-point exceptions under specific operating conditions.
- **Failing Control Unit hardware** Memory errors or processing glitches in the CU board generate invalid floating-point operations that cannot be recovered by a simple reset.
- **Incorrect parameterization or recent drive changes** Uploading new parameters or changing scaling factors without validating the configuration can introduce calculation errors in the drive's logic.

## Step-by-Step Fix {#fix}

1. **Read the fault buffer** using parameter r0945 on the keypad (BOP-2 or IOP) or via Starter/Startdrive to confirm the fault timestamp and any repeated occurrences.
2. **Power down the entire system** by switching off the incoming supply and waiting at least 30 seconds for all capacitors to discharge fully.
3. **Power the drive back on** (POWER ON reset) and monitor whether F01001 reappears immediately or only under load.
4. **Review FBLOCKS and DCC configuration** if you use custom applications or function blocks, verifying that all signals and data types are valid and compatible with the current firmware.
5. **Check for firmware updates** on the Siemens support portal or through your distributor, and install the latest approved version if a service bulletin lists F01001 as a known issue.
6. **Examine the Control Unit for physical damage** such as corrosion, burned traces, or loose connections, then reseat the CU in its slot and retry operation.
7. **Replace the Control Unit** if the fault returns after a clean power cycle and firmware update, then contact Siemens technical support or your local hotline for escalation and diagnostics parameter r9999 review.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01001-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Order the CU model that matches your frame size and communication interface (CU240, CU250, etc.). |
| Firmware upgrade kit or SD card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01001-fault-code&k=Firmware+upgrade+kit+or+SD+card&tag=errorcodefixes-20) \| Check the Siemens download portal for the latest software version compatible with your hardware revision. |

## When to Call a Pro

Call a Siemens-certified technician or your distributor's hotline if F01001 persists after a full power cycle and firmware update. The fault may require in-depth diagnostics using service tools, access to parameter r9999, and analysis of the fault buffer history. If your process depends on custom FBLOCKS or DCC charts, an applications engineer will need to validate the logic and data types. A recurring floating-point exception often means a hardware fault in the Control Unit that only a trained professional with OEM replacement parts and calibration equipment can address safely.

## See Also

- [Siemens VFD Fault Codes — SINAMICS G120, V20, S120 Guide](/posts/siemens-vfd-fault-codes/)
- [Siemens SINAMICS V20 F1 Fault — Causes & Fix](/posts/siemens-sinamics-v20-f1-fault/)
- [Siemens Micromaster F0023 - Causes & Fix](/posts/siemens-micromaster-vfd-f0023-fault-code/)
- [Siemens G120 F01662 - Causes & Fix](/posts/siemens-g120-vfd-f01662-fault-code/)
