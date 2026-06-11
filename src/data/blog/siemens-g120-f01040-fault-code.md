---
title: "Siemens G120 F01040 - Causes & Fix"
description: "Siemens G120 F01040 is an internal software or parameterization fault. Learn how to clear it with a power cycle and parameter save."
pubDatetime: 2026-05-27T10:43:44Z
modDatetime: 2026-05-27T10:43:44Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens SINAMICS G120 Control Unit (CU)"
---

## Siemens G120 F01040 — What It Means

F01040 is a fault code on the Siemens SINAMICS G120 drive that trips the unit and requires a full power cycle after saving parameters. The drive reports an internal software or parameterization error in the Control Unit. Siemens manuals describe the remedy as saving your parameter settings and performing a POWER ON restart. This class of fault relates to inconsistent or corrupted data on the drive's non-volatile memory or to internal software problems that prevent normal operation. Unlike an alarm, F01040 stops the drive completely until you clear the fault and address the underlying cause.

[Jump to Fix](#fix)

## Common Causes

- **Parameter change not committed** A new parameter setting was written but the drive was not powered off and on to load the changes into non-volatile memory.
- **Corrupted non-volatile memory** The Control Unit's internal memory or memory card holds inconsistent or damaged configuration data that the software cannot interpret correctly.
- **Firmware incompatibility or bug** The current firmware version contains a known issue or is mismatched with recent commissioning changes or hardware swaps.
- **Failing Control Unit** The Control Unit itself is degraded or faulty and cannot reliably store or execute parameter data even after power cycling.

## Step-by-Step Fix {#fix}

1. **Record the fault buffer** by connecting via Startdrive or the BOP-2 panel and reading the fault history to confirm F01040 and note the time and context of the trip.
2. **Save the current parameter set** to the drive's non-volatile memory or to an external memory card if communication is still available.
3. **Perform a complete POWER ON cycle** by switching off mains power to the drive, waiting at least 10 seconds, then switching it back on (do not simply press the fault-acknowledge button).
4. **Check the fault buffer again** after restart. If F01040 does not return, restore normal operation and monitor for recurrence.
5. **Inspect the memory card and non-volatile storage** for corruption or mismatched configuration files if the fault reappears. Replace or reformat the card and reload a known-good parameter set.
6. **Update the firmware** to the latest approved version for your G120 model if Siemens support notes or service bulletins document a fix for internal software faults.
7. **Replace the Control Unit** if F01040 persists after power cycling, memory verification, and firmware update. Transfer your saved parameter set to the new CU and commission the drive.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens SINAMICS G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01040-fault-code&k=Siemens+SINAMICS+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Required if the fault persists after power cycling, memory checks, and firmware update. Match the CU model to your Power Module. |
| Siemens SINAMICS memory card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01040-fault-code&k=Siemens+SINAMICS+memory+card&tag=errorcodefixes-20) \| Replace if the installed card shows corruption or read/write errors. Format and load a verified parameter set before installation. |

## When to Call a Pro

Call a qualified drives technician or Siemens service partner if F01040 returns after you have saved parameters, performed a full power cycle, and verified the memory card. If you are not familiar with Startdrive software, fault-buffer diagnostics, or firmware update procedures, get professional help before replacing the Control Unit. Persistent internal software faults can indicate deeper hardware problems that require bench testing and factory repair. Always contact support if the drive is under warranty or if your process cannot tolerate trial replacements.

## See Also

- [Siemens G120 F01034 - Causes & Fix](/posts/siemens-g120-f01034-fault-code/)
- [Siemens G120 A01028 - Causes & Fix](/posts/siemens-g120-a01028-fault-code/)
- [Siemens SINAMICS G120 F30011 Fault — Phase Loss Fix](/posts/siemens-sinamics-f30011-fault/)
- [Siemens Micromaster F0005 - Causes & Fix](/posts/siemens-micromaster-f0005-fault-code/)
