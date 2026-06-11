---
title: "Siemens G120 F01033 - Causes & Fix"
description: "F01033 means a reference parameter for unit conversion is invalid (often 0.0). Fix by correcting the scaling parameter in your drive setup."
pubDatetime: 2026-05-31T11:16:41Z
modDatetime: 2026-05-31T11:16:41Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens Startdrive commissioning software"
---

## Siemens G120 F01033 — What It Means

F01033 on a Siemens SINAMICS G120 drive means "Unit switchover: Reference parameter value invalid." The drive has detected that a reference parameter used for unit conversion or scaling is invalid or improperly set. This is a configuration fault, not a hardware overcurrent or thermal fault. The most common trigger is that one of the required reference parameters is set to 0.0, which is not permitted for the conversion calculation. The fault typically appears after commissioning changes, parameter downloads, or when a unit changeover is made without updating all related reference values consistently.

[Jump to Fix](#fix)

## Common Causes

- **Reference parameter set to zero** A scaling or reference value required for unit conversion was entered as 0.0 or left blank, which the drive cannot accept for the calculation.
- **Incomplete unit changeover** A unit conversion was made in Startdrive or the parameter tool, but the associated reference values were not updated to match the new unit selection.
- **Inconsistent parameter set after download** The drive received an incomplete or inconsistent parameter file during commissioning, leaving reference data invalid or missing.
- **Commissioning data lost or corrupted** A memory card load, parameter reset, or incomplete save operation caused the drive to lose or corrupt its reference parameter values.
- **Parameter mismatch after control-unit swap** The control unit was replaced or reset and the restored parameter set does not match the original reference configuration for unit conversion.
- **Manual parameter entry error** A technician entered a reference or scaling parameter incorrectly during setup or troubleshooting, leaving the value out of range or invalid.

## Step-by-Step Fix {#fix}

1. **Access the fault buffer** in the drive using the operator panel (BOP-2 or IOP) or your PC with Startdrive to read fault F01033 and note any additional diagnostic data stored with the fault.
2. **Identify the reference parameter** involved in the fault by reviewing the unit conversion and scaling settings in your parameter set, typically found in the technology or reference parameter group.
3. **Check for zero or invalid values** in all reference parameters related to unit switchover, scaling, or engineering-unit conversion, and compare them to your commissioning documentation or machine specification.
4. **Correct the invalid parameter** by entering the proper reference value from your commissioning data or machine manual, then save the corrected parameter set to the drive's nonvolatile memory.
5. **Verify parameter consistency** by reviewing the full parameter set for any other unit-conversion or scaling parameters that may have been affected by the same download or change event.
6. **Clear the fault** using the operator panel, a digital input configured for fault reset, the control word from your controller, or by cycling power to the drive, depending on your system setup.
7. **Re-test the drive** by running the motor under normal operating conditions and confirming that F01033 does not reappear, then monitor the fault buffer for any new diagnostic entries.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Startdrive commissioning software | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01033-fault-code&k=Siemens+Startdrive+commissioning+software&tag=errorcodefixes-20) \| Required for advanced parameter editing and backup if your operator panel access is limited. |
| Siemens BOP-2 or IOP operator panel | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01033-fault-code&k=Siemens+BOP-2+or+IOP+operator+panel&tag=errorcodefixes-20) \| Allows on-site fault reading and parameter adjustment if your existing panel is damaged or missing. |

## When to Call a Pro

Call a qualified Siemens drive technician or automation engineer if you do not have access to the original commissioning parameter file, if the fault persists after verifying and correcting all reference values, or if you are unfamiliar with navigating the G120 parameter structure. A professional with Startdrive experience can compare your current parameter set to a known-good baseline and identify hidden inconsistencies in the reference or unit-conversion configuration. Also seek expert help if the drive was part of a larger system integration and you do not have documentation for the scaling or engineering-unit setup.

## See Also

- [Siemens SINAMICS G120 F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault/)
- [Siemens Micromaster F0222 - Causes & Fix](/posts/siemens-micromaster-f0222-fault-code/)
- [Siemens F01018 - Causes & Fix](/posts/siemens-g120-vfd-f01018-fault-code/)
- [Siemens G120 A05001 Current Limit - Causes & Fix](/posts/siemens-g120-a05001-fault-code/)
