---
title: "Siemens G120 F01105 - Causes & Fix"
description: "Siemens G120 F01105 means insufficient memory on the Control Unit. Learn the causes, reset steps, and when to replace the CU."
pubDatetime: 2026-05-27T10:44:55Z
modDatetime: 2026-05-27T10:44:55Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
most_likely_cause: "Too many data sets configured"
---

## Siemens G120 F01105 — What It Means

Fault F01105 on a Siemens SINAMICS G120 indicates 'CU: Insufficient memory' on the Control Unit. This is a parameterization or configuration issue where the Control Unit does not have enough internal memory to store the configured data sets or parameter files. The drive will trip to OFF1 and require a full POWER ON reset to clear the fault.

This is not a motor overload, line voltage problem, or power module fault. It is strictly a Control Unit memory or configuration fault caused by too much data being stored or corrupted parameter files in non-volatile memory.

[Jump to Fix](#fix)

## Common Causes

- **Too many data sets configured** The Control Unit has a finite amount of memory, and configuring an excessive number of parameter data sets or application function blocks can exceed the available space.
- **Corrupted parameter file or non-volatile memory** A parameter set stored on the memory card or in the CU's internal memory can become corrupted during upload, download, or a power interruption, triggering the memory fault.
- **Firmware bug or outdated version** Some firmware versions may mismanage memory allocation or fail to properly handle large parameter files, leading to false insufficient-memory faults.
- **Failed or defective Control Unit** Internal hardware failure in the CU's memory chips or data storage circuitry can prevent normal parameter storage and trigger F01105 even with a valid configuration.

## Step-by-Step Fix {#fix}

1. {'lead': 'Read the fault buffer and confirm F01105', 'text': 'using the operator panel or Starter software, and note the fault value in parameter r0949 if displayed.'}
2. {'lead': 'Perform a full POWER ON reset', 'text': 'by turning off the main disconnect or control power supply, waiting 30 seconds, then powering the drive back on to clear the fault from memory.'}
3. {'lead': 'Review recent parameterization changes', 'text': 'and delete or disable any data sets, function blocks, or application profiles that are not required for your application to free up Control Unit memory.'}
4. {'lead': 'Check the memory card and non-volatile data', 'text': 'by removing the memory card (if installed), inspecting it for physical damage, and attempting to reload a known-good parameter backup or factory defaults.'}
5. {'lead': 'Update the Control Unit firmware', 'text': 'to the latest version available from Siemens using Starter software or the service tool, as newer releases often fix memory allocation bugs.'}
6. {'lead': 'Replace the Control Unit if the fault persists', 'text': 'after all configuration and firmware steps, and contact Siemens technical support for warranty evaluation or advanced diagnostics.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01105-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Match the CU part number exactly to your existing unit (CU240E, CU250S, etc.) and confirm firmware compatibility before installation. |
| Siemens memory card for G120 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01105-fault-code&k=Siemens+memory+card+for+G120&tag=errorcodefixes-20) \| Used to store and transfer parameter files. Replace if the existing card is corrupted or physically damaged. |

## When to Call a Pro

Call a qualified electrician or Siemens-certified technician if the fault reappears after a full power cycle and parameter reset, if you are not trained in VFD commissioning software, or if you need to replace the Control Unit and transfer your application parameters. Firmware updates and CU replacements require Starter or SCOUT software and a working knowledge of G120 parameter structures. If the drive is under warranty or part of a critical process line, contact Siemens technical support before performing any hardware replacement to avoid voiding coverage or creating additional configuration issues.

## See Also

- [Siemens Micromaster F0052 - Causes & Fix](/posts/siemens-micromaster-f0052-fault-code/)
- [Siemens Micromaster F0022 - Causes & Fix](/posts/siemens-micromaster-f0022-fault-code/)
- [Siemens G120 A05004 - Causes & Fix](/posts/siemens-g120-a05004-fault-code/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
