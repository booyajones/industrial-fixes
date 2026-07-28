---
title: "Siemens G120 F01650 - Causes & Fix"
description: "F01650 means a safety parameter fault. Most often the Safety Integrated acceptance test is incomplete or safety wiring has a problem."
pubDatetime: 2026-05-31T11:23:02Z
modDatetime: 2026-05-31T11:23:02Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit"
most_likely_cause: "Safety acceptance test not completed"
---

## What this code means
Fault code F01650 on the Siemens SINAMICS G120 drive means there is a fault in the safety parameterization. The drive's Safety Integrated functions have detected that safety parameters are not accepted or not valid for operation. The drive will react with an OFF2 (or OFF3) shutdown to protect the system. This fault typically appears during safety commissioning or acceptance testing, and it indicates that the required safety workflow has not been completed or that there is a problem with the safety signal path or wiring.

## Common Causes

- **Safety acceptance test not completed** The Safety Integrated commissioning or forced-checking procedure has not been finished, leaving the drive in a state that prevents normal operation.
- **Safety reset timeout on processor path** The drive reports r0949 = 100 or 200, indicating a reset timeout condition on safety processor path P1 or P2 that prevents the safety system from validating.
- **Safety input wiring or contact fault** Loose connections, open circuits, or contact problems on the F-DI (fail-safe digital input) terminals disrupt the safety signal path.
- **Safety parameter inconsistency after configuration change** An incomplete or corrupted safety parameter set exists after replacing the control unit, memory card, or modifying the safety-related configuration.
- **Safety chain or interlock signal incorrect** The safety chain, external interlocks, or master controller signals are not in the expected state for the configured safety function.

## Step-by-Step Fix {#fix}

1. {'lead': 'Record the fault and diagnostic values first', 'text': 'Use parameter r0947 to view the fault message storage and check r0949 for the associated cause value (100 or 200 for reset timeout on P1 or P2).'}
2. {'lead': 'Verify safety commissioning status', 'text': 'Confirm whether the drive is still waiting for the acceptance test or forced-checking procedure to be completed, which is the primary condition that triggers F01650.'}
3. {'lead': 'Inspect all safety input wiring and terminals', 'text': 'Check every F-DI wire, terminal block, and connection for loose contacts, breaks, or corrosion, and verify continuity through the entire safety circuit.'}
4. {'lead': 'Complete or retrigger the safety acceptance procedure', 'text': 'Follow the Siemens Safety Integrated commissioning steps exactly, including the forced-checking workflow, then power-cycle or restart the drive as instructed to clear the fault.'}
5. {'lead': 'Repeat the safety reset if timeout is reported', 'text': 'If r0949 shows a reset timeout (100 or 200), execute the safety reset sequence again and make sure the safety signal path remains stable throughout the timeout window.'}
6. {'lead': 'Compare hardware and safety parameter set against the intended configuration', 'text': 'Verify that the installed control unit, memory card, and downloaded safety project match the system design, then re-download or recommission the safety parameters if a mismatch is found.'}
7. {'lead': 'Escalate to Siemens support if the fault persists', 'text': 'If all wiring, commissioning steps, and configuration checks are correct and the fault remains, contact the Siemens hotline for internal diagnostic support.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01650-fault-code&k=Siemens+G120+Control+Unit&tag=errorcodefixes-20) \| Required if the existing unit has corrupted safety parameters or hardware failure after all other diagnostics are ruled out. |
| Siemens G120 Memory Card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01650-fault-code&k=Siemens+G120+Memory+Card&tag=errorcodefixes-20) \| Use if the safety parameter set is corrupted on the existing card and cannot be recommissioned successfully. |

## When to Call a Pro

Call a qualified Siemens-trained technician or system integrator if you are not familiar with Safety Integrated commissioning procedures or if the fault persists after completing the acceptance test and verifying all wiring. Safety functions are critical for personnel protection and require precise configuration. If the drive shows an unresolved internal safety fault after all standard diagnostics, or if you see fault values in r0949 that are not documented in your manual, contact Siemens technical support immediately. Any work on safety circuits should be performed by personnel trained in functional safety standards.
