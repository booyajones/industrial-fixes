---
title: "Siemens G120 F01034 - Causes & Fix"
description: "F01034 on Siemens G120 means parameter reference value change failed. Learn causes, diagnostic steps, and when to replace the Control Unit."
pubDatetime: 2026-05-27T10:43:12Z
modDatetime: 2026-05-27T10:43:12Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
most_likely_cause: "Reference parameter changed to incompatible value"
---

## What this code means
F01034 on a Siemens SINAMICS G120 indicates that the drive accepted a parameter change to a reference value, but one or more related parameters could not be recalculated correctly in per-unit format. The drive responds by rejecting the change and restoring the original parameter value. This is a parameterization or engineering fault, not an overcurrent, ground fault, or power-stage failure.

The fault triggers when a reference parameter tied to the drive's internal scaling is changed to an incompatible value that cannot be converted cleanly in the per-unit system. The drive's internal calculations depend on consistent reference values across linked parameters, and when a new value breaks that consistency, the conversion fails and the fault is raised.

## Common Causes

- **Reference parameter changed to incompatible value** A scaling or reference parameter was edited to a value that cannot be recalculated in the drive's internal per-unit representation.
- **Parameter value outside valid conversion range** The entered value falls outside the range that the drive can convert for related drive objects.
- **Inconsistent linked reference parameters** One reference parameter was changed without updating related scaling values, causing a mismatch in the per-unit calculation.
- **Parameter download or import error** A parameter set was downloaded or imported that contains reference values incompatible with the current drive configuration.
- **Manual commissioning edit during setup** A technician manually edited reference or scaling settings during commissioning, introducing a conversion conflict.
- **Control Unit internal calculation fault** The Control Unit itself is unable to perform per-unit conversion correctly, even with valid parameter entries.

## Step-by-Step Fix {#fix}

1. **Identify the last parameter changed** before the fault appeared by reviewing the parameter change log in Startdrive or the drive display, and note the previous working value.
2. **Review all related reference and scaling parameters** in the same parameter group to verify consistency, since the fault is triggered by a change in one reference parameter affecting linked values.
3. **Restore the original parameter value** or enter a new value that remains within the valid conversion range for the affected drive object, using the drive's parameter documentation for acceptable limits.
4. **Acknowledge and reset the fault** using the control panel or Startdrive after correcting the parameter condition.
5. **Re-download the commissioning data set** or manually re-enter the parameter set carefully if the fault repeats, focusing on reference and scaling parameters.
6. **Test the drive** by running a controlled ramp to verify the parameter change is accepted and no fault recurs.
7. **Replace the Control Unit** if the drive continues to reject valid parameter values and the fault persists after re-commissioning.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01034-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Required only if the fault persists after correcting parameters and re-commissioning, indicating an internal calculation failure. |

## When to Call a Pro

Call a qualified Siemens drive technician if you are not familiar with Startdrive or SINAMICS parameter structures, or if the fault repeats after you have restored original reference values and re-downloaded a known-good parameter set. If the Control Unit replacement is indicated and you do not have experience with G120 commissioning and parameter backup, professional service will prevent data loss and configuration errors during the swap.
