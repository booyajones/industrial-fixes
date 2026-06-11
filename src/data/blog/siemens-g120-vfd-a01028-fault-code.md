---
title: "Siemens G120 A01028 Fault - Causes & Fix"
description: "A01028 means the drive's saved configuration was made for a different module type. Save parameters with p0971=1 or reload the correct project."
pubDatetime: 2026-05-31T11:16:07Z
modDatetime: 2026-05-31T11:16:07Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU) matching installed MLFB"
---

## Siemens G120 A01028 Fault — What It Means

Fault code A01028 on a Siemens SINAMICS G120 is a configuration error alarm. It appears when the drive detects that the downloaded parameter set was created for a different hardware module than the one physically installed. The drive compares the stored configuration's target module type and order number (MLFB) against the actual Control Unit and Power Module present, and this alarm triggers when they do not match. The alarm reaction is NONE and it requires no acknowledgment, but it signals that your commissioning data is inconsistent with the installed hardware. This is not an electrical failure but a mismatch between the project file and the drive identity.

[Jump to Fix](#fix)

## Common Causes

- **Wrong hardware selected during commissioning** The project in Startdrive or your commissioning software was built for a different G120 module variant or MLFB than the drive you actually installed.
- **Parameter file copied from another drive** A configuration backup from a different power module or control unit family was loaded into this drive without updating the device identity.
- **Parameters not saved non-volatilely** Changes were made but not stored permanently, so the volatile buffer and stored configuration are out of sync when the drive restarts.
- **Hardware replaced without updating the project** The Control Unit or Power Module was swapped during service but the old parameter set still references the original module type.
- **Incorrect module identity after firmware or memory reset** A firmware update, factory reset, or memory issue caused the drive to lose or corrupt its stored module type data.

## Step-by-Step Fix {#fix}

1. **Check the installed drive nameplate** for the exact order number (MLFB) and module type, and write down the Control Unit and Power Module part numbers from the physical G120 unit.
2. **Open your commissioning project** in Startdrive or the Siemens tool you used, navigate to the device configuration, and verify that the selected Control Unit and Power Module types match the installed hardware exactly.
3. **Save parameters non-volatilely** by setting parameter p0971 to 1 and executing the command, which writes the current configuration to the drive's permanent memory.
4. **Power-cycle the drive** completely by removing control power for at least 10 seconds, then restore power so the drive reloads the saved configuration from non-volatile memory.
5. **Verify the alarm clears** by checking the drive display or diagnostic buffer, and confirm that the module type in the drive properties now matches the installed hardware.
6. **Reload the correct project** if the alarm persists: create or download a new project in Startdrive for the exact MLFB of your installed G120 module, then download it to the drive and save with p0971=1.
7. **Inspect for Control Unit or memory faults** if a known-correct project still triggers A01028 after a full power cycle, as the module identity circuitry or stored calibration data may be corrupted and require hardware service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) matching installed MLFB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01028-fault-code&k=Siemens+G120+Control+Unit+%28CU%29+matching+installed+MLFB&tag=errorcodefixes-20) \| Required if the current Control Unit has failed or the stored module identity cannot be corrected by reloading the project. |
| Siemens G120 Power Module (PM) matching installed MLFB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01028-fault-code&k=Siemens+G120+Power+Module+%28PM%29+matching+installed+MLFB&tag=errorcodefixes-20) \| Needed if the Power Module was replaced without updating the project, or if the physical module does not match the commissioned configuration. |
| Siemens Startdrive commissioning software license | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01028-fault-code&k=Siemens+Startdrive+commissioning+software+license&tag=errorcodefixes-20) \| Used to create, edit, and download the correct parameter set for your exact G120 module variant and save it non-volatilely. |

## When to Call a Pro

Call a qualified Siemens drive technician or automation integrator if you cannot identify the installed module MLFB, if you do not have access to the original commissioning project or Startdrive software, or if the alarm returns after correctly matching the project to the hardware and saving with p0971=1. Also contact a professional if the drive was part of a coordinated system (PLC, motion control, or multi-axis setup) where changing parameters could affect other equipment. If the Control Unit or Power Module identity cannot be read or verified through the drive interface, the hardware may have a memory or circuit fault that requires factory-trained service and possible module replacement under warranty.

## See Also

- [Siemens Micromaster F0004 - Causes & Fix](/posts/siemens-micromaster-vfd-f0004-fault-code/)
- [Siemens Sinumerik Alarm 380500 — Causes & Fix](/posts/siemens-sinumerik-alarm-380500/)
- [Siemens Micromaster F0020 - Causes & Fix](/posts/siemens-micromaster-f0020-fault-code/)
- [Siemens Micromaster F0071 - Causes & Fix](/posts/siemens-micromaster-f0071-fault-code/)
