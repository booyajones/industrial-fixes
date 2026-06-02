---
title: "Siemens G120 F01611 - Causes & Fix"
description: "Siemens G120 F01611 means a defect in a safety monitoring channel. Learn how to diagnose r0949, check safety wiring, and clear the fault."
pubDatetime: 2026-05-28T09:09:47Z
modDatetime: 2026-05-28T09:09:47Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F01611 — What It Means

F01611 on a Siemens SINAMICS G120 indicates a defect in a monitoring channel or a safety-related discrepancy fault. The drive has detected a mismatch or failure in one of its internal safety monitoring paths. This is not a simple motor overload or power stage trip. Instead, the inverter's safety functions have flagged an inconsistency between redundant monitoring channels or a fault in the safety-integrated circuitry.

Siemens documentation ties this fault to discrepancies in the safety chain and notes that the exact subtype is stored in parameter r0949. The fault value in r0949 tells you which monitoring channel or safety function is affected. You must identify and eliminate the discrepancy before the drive will acknowledge the fault and allow a restart.

[Jump to Fix](#fix)

## Common Causes

- **Mismatch in the safety monitoring chain** The drive detected a discrepancy between redundant safety channels or between expected and actual states in the Safety Integrated circuit.
- **Faulty internal monitoring channel or hardware** A defect in one of the drive's internal monitoring channels can trigger F01611, often pointing to a Control Unit or Power Module problem.
- **Incorrect or inconsistent Safety Integrated wiring** Wiring errors or loose connections in the failsafe digital inputs (F-DI) or Safe Torque Off (STO) circuit create inconsistent signals that the drive flags as a discrepancy.
- **Processor communication or data exchange error** Internal communication faults between the drive's safety processor and main control processor can appear as a monitoring-channel defect.
- **Uncorrected previous safety fault condition** If an earlier safety fault was not properly acknowledged through the failsafe acknowledge sequence, the discrepancy remains latched and reappears as F01611.

## Step-by-Step Fix {#fix}

1. {'lead': 'Read the fault value in parameter r0949', 'text': 'Connect your commissioning software (STARTER or the BOP-2) and record the value in r0949. Siemens says the remedy depends on this fault value, which identifies the specific monitoring channel or safety function involved.'}
2. {'lead': 'Inspect and verify all Safety Integrated wiring', 'text': 'Check the failsafe digital input (F-DI) terminals, STO circuit connections, and any safety relay or external device wiring against your commissioning documentation. Look for loose terminals, crossed wires, or incorrect signal states.'}
3. {'lead': 'Remove the discrepancy in the safety circuit', 'text': 'Correct any wiring fault, reset any external safety relays, and confirm that the safety function configuration in the drive matches the actual field wiring. The drive will not allow reset until the discrepancy is gone.'}
4. {'lead': 'Acknowledge the fault using the failsafe acknowledge sequence', 'text': 'Execute the failsafe acknowledge by cycling the failsafe digital input: F-DI = 0, then 1, then 0. Siemens describes this sequence as the correct method to clear discrepancy messages in the safety path.'}
5. {'lead': 'Perform a power cycle (POWER ON)', 'text': 'If the fault does not clear after acknowledging, remove all power from the drive for at least 30 seconds, then restore power. Many internal safety faults require a full power cycle to reset.'}
6. {'lead': 'Replace the defective Control Unit or Power Module if the fault persists', 'text': 'When F01611 reappears immediately after power-on and r0949 points to an internal channel, replace the Control Unit first. If the fault value indicates a power-stage monitoring issue, replace the Power Module.'}
7. {'lead': 'Re-run safety commissioning checks and acceptance tests', 'text': 'After any repair or configuration change in the safety circuit, verify all Safety Integrated functions (STO, safe stop, etc.) operate correctly and document the test results per Siemens commissioning procedures.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01611-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Replace if r0949 fault value points to internal control or monitoring-channel hardware. Match your current CU model and firmware. |
| Siemens G120 Power Module (PM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01611-fault-code&k=Siemens+G120+Power+Module+%28PM%29&tag=errorcodefixes-20) \| Replace if the discrepancy is in the power-stage monitoring path and cannot be cleared. Verify frame size and power rating before ordering. |
| Safety relay or failsafe digital input components | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01611-fault-code&k=Safety+relay+or+failsafe+digital+input+components&tag=errorcodefixes-20) \| External safety devices feeding F-DI or STO circuits may need replacement if field wiring checks reveal defective contacts or logic. |

## When to Call a Pro

Call a qualified Siemens integrator or automation technician if you are not trained in Safety Integrated commissioning or if r0949 shows a fault value you cannot interpret from the Siemens list manual. Safety-related faults require knowledge of failsafe wiring standards, safety-function configuration, and acceptance testing. If you have replaced the Control Unit or Power Module and F01611 returns immediately, the problem may involve firmware mismatch, incorrect safety-parameter cloning, or a more complex internal communication fault that needs factory support or an authorized service center.

## See Also

- [Siemens SINAMICS G120 F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault/)
- [Siemens G120 F01650 - Causes & Fix](/posts/siemens-g120-f01650-fault-code/)
- [Siemens SINAMICS G120 VFD Complete Setup and Fault Code Guide](/posts/siemens-sinamics-g120-complete-guide/)
- [Siemens G120 A05006 - IGBT Overtemperature Warning & Fix](/posts/siemens-g120-a05006-fault-code/)
