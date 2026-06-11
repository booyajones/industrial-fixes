---
title: "Siemens G120 F01650 - Causes & Fix"
description: "Siemens G120 F01650 fault indicates a safety parameterization error. Learn how to diagnose and clear this Safety Integrated fault."
pubDatetime: 2026-05-27T10:49:22Z
modDatetime: 2026-05-27T10:49:22Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Memory Card"
---

## Siemens G120 F01650 — What It Means

F01650 on a Siemens SINAMICS G120 is a fault in the drive's Safety Integrated parameterization. The drive has detected an inconsistency or invalid configuration in the stored safety parameters and will not allow normal operation until the fault is corrected. This code triggers an OFF2 or OFF3 safe stop reaction, which brings the motor to a controlled halt and blocks further commands.

The fault typically appears during safety commissioning, after changes to safety functions like STO (Safe Torque Off), or when the drive cannot validate its safety configuration after a power cycle. It is part of the Safety Integrated fault family and is tied to the integrity of the drive's safety system rather than a motor or power-stage problem.

[Jump to Fix](#fix)

## Common Causes

- **Safety acceptance test not completed** The drive-integrated Safety Integrated function requires a forced-checking or acceptance test procedure after commissioning, and the fault appears if this step was skipped or did not finish correctly.
- **Mismatch in safety parameter data** The safety settings stored in the drive do not match what the safety system expects, often after manual parameter changes or an incomplete download.
- **Incomplete safety commissioning after parameter changes** Changes to STO or other safety functions were made but the required recommissioning and forced-checking procedure was not run afterward.
- **Memory card or Control Unit failure** The safety parameter data cannot be read, stored, or validated correctly due to a faulty memory card or Control Unit, preventing the drive from confirming safety integrity.

## Step-by-Step Fix {#fix}

1. Read the fault buffer and active diagnostics on the drive using the operator panel or Starter software to confirm F01650 and check for any additional fault values or timestamps.
2. Verify the safety function state and review when the fault first appeared (during commissioning, after a parameter change, or after a power cycle) to narrow the root cause.
3. Check the safety commissioning sequence in your project and confirm that the acceptance test or forced-checking procedure was completed after the last safety parameter change or STO configuration.
4. Inspect the safety parameter set for inconsistencies, especially if safety functions were recently modified, and compare the stored parameters against your safety specification.
5. Acknowledge and reset the fault using the operator panel, digital input, control word, or a power cycle after correcting the parameter issue, then monitor the drive to see if the fault returns.
6. If the fault reappears after reset, replace the memory card or Control Unit (starting with the memory card as it is the simpler swap) and then recommission the safety function.
7. Run the full safety acceptance test and forced-checking procedure after any hardware replacement or parameter correction to validate the Safety Integrated function and clear the fault permanently.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Memory Card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01650-fault-code&k=Siemens+G120+Memory+Card&tag=errorcodefixes-20) \| Replace if the fault persists after parameter corrections and the card cannot store or validate safety data. |
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01650-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Required if the memory card replacement does not resolve the fault or if the Control Unit shows signs of failure during diagnostics. |

## When to Call a Pro

Call a qualified Siemens technician or safety-certified integrator if you are not trained in Safety Integrated commissioning, if the fault returns after you have completed the acceptance test and replaced the memory card or Control Unit, or if your facility's safety approval process requires third-party validation of all safety-function changes. Safety-related faults on VFDs often have regulatory and insurance implications, so professional documentation and sign-off are recommended any time hardware is replaced or safety parameters are altered.

## See Also

- [Siemens G120 F03505 - Causes & Fix](/posts/siemens-g120-f03505-fault-code/)
- [Siemens G120 F01044 - Causes & Fix](/posts/siemens-g120-vfd-f01044-fault-code/)
- [Siemens G120 A01590 Fault Code - Causes & Fix](/posts/siemens-g120-a01590-fault-code/)
- [Siemens G120 F30002 - Causes & Fix](/posts/siemens-g120-f30002-fault-code/)
