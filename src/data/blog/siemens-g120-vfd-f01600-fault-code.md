---
title: "Siemens G120 F01600 - Causes & Fix"
description: "F01600 means Safety Integrated STOP A initiated on your Siemens G120 VFD. Check STO inputs, read fault value r0949, then cycle power."
pubDatetime: 2026-05-31T11:21:51Z
modDatetime: 2026-05-31T11:21:51Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "STO safety relay or contactor"
---

## Siemens G120 F01600 — What It Means

F01600 on a Siemens SINAMICS G120 variable frequency drive means 'STOP A initiated' by the drive's Safety Integrated function. This is a safety stop triggered by the internal safety processor, not a motor overload or power stage fault. The drive has detected a condition in the safety monitoring chain that requires it to halt operation immediately. The fault can appear after a failed forced-checking procedure of the safety shutdown path, a monitoring channel defect, or a state mismatch where pulses are suppressed even though Safe Torque Off (STO) is not selected. In some cases, F01600 follows or accompanies fault F01611, which points to a safety channel error.

[Jump to Fix](#fix)

## Common Causes

- **STO input wiring fault** Loose, open, or miswired Safe Torque Off terminals prevent the safety circuit from closing correctly and trigger STOP A.
- **Failed safety shutdown-path proof test** The drive's internal forced-checking routine detected that the safety shutdown path is not functioning as expected.
- **Safety monitoring channel defect** One of the two redundant safety processors (processor 1 or 2) has registered an internal error and initiated the stop.
- **STO state mismatch** The drive has suppressed pulses even though Safe Torque Off was not commanded, indicating a logic conflict in the safety circuit.
- **Related F01611 fault** F01600 can appear as a follow-up response when the drive has already logged a safety channel fault F01611.

## Step-by-Step Fix {#fix}

1. **Read the fault value** in parameter r0949 on the drive display or via your HMI to identify the exact subtype and trigger for the STOP A event.
2. **Check for fault F01611** in the fault buffer, since F01600 often follows a safety channel error and you may need to address that fault first.
3. **Inspect all STO input wiring and terminals** on the drive, including connections to any external safety relay or e-stop device, and verify continuity and correct voltage levels.
4. **Cycle the STO command** by selecting Safe Torque Off and then de-selecting it if the fault value in r0949 indicates that pulses are suppressed without an STO selection.
5. **Perform a full power cycle** of the drive by removing all control and line power for at least 30 seconds, then restore power and attempt to clear the fault.
6. **Re-test the safety function** by manually triggering and releasing your STO input or safety device to confirm that the drive responds correctly without re-faulting.
7. **Replace the control unit or drive module** if the fault persists after all wiring and external safety devices are verified, as the safety processor circuit path is likely defective.

## Parts Often Needed

| Part | Notes |
|------|-------|
| STO safety relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01600-fault-code&k=STO+safety+relay+or+contactor&tag=errorcodefixes-20) \| If your external safety device feeding the STO terminals is faulty or chattering. |
| G120 control unit (CU) module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01600-fault-code&k=G120+control+unit+%28CU%29+module&tag=errorcodefixes-20) \| Required when the internal Safety Integrated processor path has failed and the fault cannot be cleared by wiring or logic checks. |

## When to Call a Pro

Call a qualified drives technician or Siemens-certified service provider if you cannot locate the fault trigger using r0949, if F01611 appears alongside F01600, or if the fault returns immediately after you have verified all STO wiring and cycled power. Safety Integrated faults involve redundant processor logic and internal forced-checking routines that require specialized diagnostic tools and knowledge of functional-safety standards. If your process is safety-critical or the drive is part of a certified SIL installation, any repair or troubleshooting must be performed by personnel trained in functional safety to maintain compliance.

## See Also

- [Siemens G120 F01040 - Causes & Fix](/posts/siemens-g120-f01040-fault-code/)
- [Siemens G120 F01018 - Causes & Fix](/posts/siemens-g120-f01018-fault-code/)
- [Siemens G120 F01650 - Causes & Fix](/posts/siemens-g120-vfd-f01650-fault-code/)
- [Siemens G120 F01600 - Causes & Fix](/posts/siemens-g120-f01600-fault-code/)
