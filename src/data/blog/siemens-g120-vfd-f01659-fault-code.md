---
title: "Siemens G120 F01659 - Causes & Fix"
description: "F01659 means the drive rejected a safety parameter write. Most likely fix: enter the correct Safety Integrated password or reset the safety state."
pubDatetime: 2026-05-31T11:23:36Z
modDatetime: 2026-05-31T11:23:36Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "G120 Control Unit"
---

## Siemens G120 F01659 — What It Means

F01659 on a Siemens SINAMICS G120 means the drive rejected a request to write one or more safety-related parameters in the Safety Integrated area. This is not a motor overload or power stage trip. Instead, the drive is blocking your change because a safety condition, password, configuration state, or hardware requirement was not met. The fault does not indicate a safety stop response itself, but rather that the system will not allow the parameter modification you attempted.

Siemens ties the exact cause to the fault value stored in parameter r0949. Common reasons include a missing or incorrect Safety Integrated password, an active safety function like STO preventing the write, a reset attempt while Safety Integrated is parameterized, simulation mode active on a digital input, or hardware that does not support the safety feature you are trying to configure. Related safety faults such as F01655 or F30655 may also be present and need resolution first.

[Jump to Fix](#fix)

## Common Causes

- **Missing or incorrect Safety Integrated password** The drive requires the correct password in p9761 to modify protected safety parameters, and the write is rejected if the password is wrong or not entered.
- **Safety function active or inhibiting writes** An active safety state such as STO or another Safety Integrated condition is preventing parameter changes, and Siemens notes this is a common rejection scenario.
- **Reset attempt while Safety Integrated is parameterized** If Safety Integrated is enabled and you try to reset certain parameters, the drive rejects the request and triggers F01659 with fault value 2.
- **Simulation mode active on a digital input** Siemens lists simulation mode on a digital input as a specific cause for certain fault values, and the write is blocked until simulation is ended.
- **Hardware does not support the safety function** The Control Unit or Power Module may not be compatible with the safety feature being configured, and the drive rejects the parameter write accordingly.
- **Related safety faults already present** Siemens indicates that faults like F01655 or F30655 should be checked and resolved first, as they can block subsequent safety parameter writes.

## Step-by-Step Fix {#fix}

1. {'lead': 'Read the fault value in r0949', 'text': 'and confirm that F01659 is the active fault, since Siemens uses this value to narrow the cause of the rejection.'}
2. {'lead': 'Check whether Safety Integrated is enabled', 'text': 'and verify if a safety state such as STO or another active safety logic is inhibiting parameter writes.'}
3. {'lead': 'Enter the correct Safety Integrated password', 'text': 'in parameter p9761 if the fault is password-related, as the drive will reject changes without proper authorization.'}
4. {'lead': 'Perform a safety reset or inhibit Safety Integrated', 'text': 'if the drive is in a safety-locked or reset state, using p0970 = 5 for the reset procedure Siemens specifies in the reset-related case.'}
5. {'lead': 'End simulation mode', 'text': "on the relevant digital input if Siemens' fault value indicates simulation is active and blocking the write."}
6. {'lead': 'Check for related safety faults', 'text': 'such as F01655 or F30655 in the fault buffer and troubleshoot those first if they are present, as they can prevent parameter changes.'}
7. {'lead': 'Confirm hardware compatibility', 'text': 'by verifying that both the Control Unit and Power Module support the Safety Integrated function you are configuring, and power cycle the complete system if the fault persists after all configuration checks.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| G120 Control Unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01659-fault-code&k=G120+Control+Unit&tag=errorcodefixes-20) \| Required replacement if the existing unit does not support the safety function or if Siemens' internal fault guidance applies and the fault is unresolved. |
| G120 Power Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01659-fault-code&k=G120+Power+Module&tag=errorcodefixes-20) \| Must be Safety Integrated compatible for the function being configured, and replacement is needed if the current module does not support the feature. |

## When to Call a Pro

Call a qualified technician or Siemens support if you cannot resolve the fault after verifying the password, resetting the safety state, and confirming hardware compatibility. Safety Integrated configuration requires knowledge of both the drive's safety architecture and the machine's safety logic, and incorrect changes can compromise personnel protection. If the fault persists after a power cycle and firmware update, or if you see repeated rejections with no clear cause in r0949, professional diagnostic support is needed to interpret the fault value and check for internal Control Unit issues that require replacement.

## See Also

- [Siemens Micromaster F0023 - Causes & Fix](/posts/siemens-micromaster-f0023-fault-code/)
- [Siemens G120 VFD F01040 - Causes & Fix](/posts/siemens-g120-vfd-f01040-fault-code/)
- [Siemens Micromaster F0020 - Causes & Fix](/posts/siemens-micromaster-f0020-fault-code/)
- [Siemens G120 A03520 - Causes & Fix](/posts/siemens-g120-a03520-fault-code/)
