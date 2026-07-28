---
title: "Siemens G120 F01105 - Causes & Fix"
description: "F01105 means the Control Unit has insufficient memory. Most often fixed by reloading parameters or replacing the CU if hardware fails."
pubDatetime: 2026-05-31T11:18:44Z
modDatetime: 2026-05-31T11:18:44Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens SINAMICS G120 Control Unit (CU240E-2, CU250S-2, or matching variant)"
most_likely_cause: "Oversized or complex parameter set"
---

## What this code means
F01105 on a Siemens SINAMICS G120 indicates that the Control Unit (CU) does not have enough available memory to complete a task. This can happen during parameter handling, project loading, firmware downloads, or internal processing operations. The fault is logged as 'CU: Insufficient memory' in the drive's fault buffer. Unlike motor or power-stage faults, this code points directly to a problem with the Control Unit's ability to manage data, either because the parameter set is too complex, the project file is corrupted, or the CU hardware itself has failed.

## Common Causes

- **Oversized or complex parameter set** A project with too many parameters or advanced features can exceed the CU's memory capacity during loading or runtime.
- **Corrupted parameter data** Incomplete or inconsistent parameter uploads, downloads, or copies can create memory allocation problems inside the Control Unit.
- **Failed firmware or project download** An interrupted or mismatched firmware update or Startdrive/TIA project transfer can leave the CU in a state where memory is not properly managed.
- **Firmware and hardware mismatch** Installing a project configured for a different CU model or firmware version can cause memory handling errors during commissioning.
- **Control Unit hardware failure** If the fault returns immediately after a clean parameter reset and power cycle, the CU's internal memory or electronics may be damaged.

## Step-by-Step Fix {#fix}

1. **Read the fault buffer** using the drive's diagnostic parameters or HMI to confirm the exact fault code, time stamp, and any additional context stored in the CU's fault memory.
2. **Identify recent changes** by reviewing what was done before the fault appeared, including parameter uploads, project downloads, firmware updates, or Control Unit or Power Module replacements.
3. **Back up the current parameter set** if possible, then perform a controlled parameter reset or reload a known-good commissioning project to rule out corrupted data as the cause.
4. **Power-cycle the drive completely** by disconnecting control and line power for at least 30 seconds, then re-energize and check if the fault clears with a minimal or default configuration.
5. **Verify hardware and firmware compatibility** by comparing the installed Control Unit model and firmware version against the configured project and Siemens support package to make sure no mismatch exists.
6. **Test with a simplified project** by loading only the essential parameters needed for basic motor control, avoiding advanced functions or custom macros that may strain memory.
7. **Replace the Control Unit** if the fault persists after a clean reload and verified configuration, as a recurring F01105 indicates memory corruption or CU electronics failure that cannot be repaired in the field.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens SINAMICS G120 Control Unit (CU240E-2, CU250S-2, or matching variant) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01105-fault-code&k=Siemens+SINAMICS+G120+Control+Unit+%28CU240E-2%2C+CU250S-2%2C+or+matching+variant%29&tag=errorcodefixes-20) \| Required if memory fault persists after parameter reload and power cycle, verify exact CU model for your frame size. |
| Parameter backup file or clean commissioning project | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01105-fault-code&k=Parameter+backup+file+or+clean+commissioning+project&tag=errorcodefixes-20) \| A verified project reload can resolve data-corruption faults without hardware replacement. |

## When to Call a Pro

Call a qualified drive technician or Siemens-certified service provider if the fault returns after you have reloaded a clean parameter set and power-cycled the drive, or if you are not familiar with Startdrive, TIA Portal, or G120 commissioning procedures. Replacing a Control Unit requires proper configuration transfer, firmware matching, and sometimes module coding or slot assignment depending on your system. A technician will also verify that the fault is not related to a larger system integration issue, network overload, or power-supply problem affecting the CU.
