---
title: "Siemens G120 F01015 - Causes & Fix"
description: "Siemens G120 F01015 signals an internal software error in the drive control unit. Learn causes, power-on reset steps, and when to replace the Control Unit."
pubDatetime: 2026-05-27T10:41:03Z
modDatetime: 2026-05-27T10:41:03Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
---

## Siemens G120 F01015 — What It Means

F01015 on a Siemens SINAMICS G120 indicates an internal software error within the drive's control electronics. This fault triggers an OFF2 reaction, shutting down the drive safely, and requires a full power-on reset to acknowledge. The fault value stored in parameter r0949 is intended for internal Siemens troubleshooting only and does not provide actionable field data. The fault buffer in r0945 will record the event and help confirm the nature of the error.

This code points to corruption or instability in the drive's firmware, memory, or boot process rather than a problem with external wiring or motor parameters. Because the fault originates inside the Control Unit's software layer, standard field adjustments will not resolve it. If the fault persists after a clean power cycle and memory check, the Control Unit itself is the most likely component requiring replacement.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted firmware or software mismatch** The drive's internal firmware may be corrupted or running an unstable version, causing the control software to fail during operation or startup.
- **Non-volatile memory or memory card data issues** Siemens documentation explicitly flags memory card or non-volatile memory problems as a source of F01015, especially if parameter data is incomplete or corrupted.
- **Repeated interrupted boot cycles** Power instability or interrupted startup sequences can prevent the drive software from initializing correctly, triggering the internal error flag.
- **Control Unit hardware failure** Internal hardware degradation in the Control Unit can cause the software layer to malfunction even when firmware and memory are intact.
- **Power-up instability or supply voltage transients** Voltage spikes or dips during startup can disrupt the control processor's boot sequence and corrupt runtime software states.

## Step-by-Step Fix {#fix}

1. **Read the fault buffer** by navigating to parameter r0945 on the control panel or via STARTER software, and note the fault value in r0949 for reference.
2. **Perform a full power-off reset** by switching off all power to the drive, waiting 30 seconds, then powering back on. A POWER ON reset is the only acknowledgment method Siemens specifies for F01015.
3. **Check the memory card or non-volatile memory** if your G120 has removable media installed. Remove and reseat the card, inspect for physical damage, and verify parameter data integrity.
4. **Review and upgrade the firmware** to the latest stable version available from Siemens, especially if your current version is known to have software bugs or if corruption is suspected.
5. **Monitor the drive through several start cycles** after the power reset to confirm the fault does not reappear. Log any repeat occurrences with timestamps and operating conditions.
6. **Contact Siemens Technical Support** with the fault buffer data and r0949 value if the fault persists. Prepare for Control Unit replacement, as this is the field-replaceable component Siemens identifies for recurring F01015 faults.
7. **Replace the Control Unit** if Siemens support confirms the diagnosis and the drive is outside warranty or repair turnaround time is too long for your application.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01015-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| The Control Unit is the component Siemens specifies for replacement when F01015 persists. Verify your exact G120 model and CU variant before ordering. |
| Siemens MMC (Multi Media Card) for G120 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01015-fault-code&k=Siemens+MMC+%28Multi+Media+Card%29+for+G120&tag=errorcodefixes-20) \| If memory card data is corrupted, a replacement MMC with clean parameter storage may resolve the fault. make sure card capacity and type match your Control Unit. |

## When to Call a Pro

Call a qualified Siemens service technician or contact Siemens Technical Support if the fault reappears after a full power cycle and memory check. F01015 is an internal software fault that requires factory-level diagnostics when basic resets fail. Replacing the Control Unit involves parameter backup, firmware version matching, and commissioning steps that require familiarity with STARTER software and drive configuration. If your process cannot tolerate extended downtime or if the drive is under warranty, professional support will minimize risk and make sure proper replacement part selection.

## See Also

- [Siemens Micromaster Fault F001 — Causes & Fix](/posts/siemens-micromaster-fault-f001/)
- [Siemens VFD Fault Codes — SINAMICS G120, V20, S120 Guide](/posts/siemens-vfd-fault-codes/)
- [Siemens SINAMICS G120 VFD Complete Setup and Fault Code Guide](/posts/siemens-sinamics-g120-complete-guide/)
- [Siemens SINAMICS G120 F00001 Fault — Causes & Fix](/posts/siemens-sinamics-g120-fault-f00001/)
