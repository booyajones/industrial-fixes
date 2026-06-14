---
title: "Siemens G120 VFD F01040 - Causes & Fix"
description: "F01040 means the G120 drive changed a parameter and needs you to save settings (p0971) then power-cycle the Control Unit to clear."
pubDatetime: 2026-05-31T11:17:44Z
modDatetime: 2026-05-31T11:17:44Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens BOP-2 Basic Operator Panel"
most_likely_cause: "Commissioning or service parameter edited without saving"
---

## Siemens G120 VFD F01040 — What It Means

F01040 on a Siemens SINAMICS G120 means the drive detected a parameter change that requires the parameters to be saved and the Control Unit to be power-cycled. This is not a hardware failure. It is an indication that a parameter set has changed and the drive expects a save and restart sequence. The fault reaction is OFF2 and acknowledgment requires a full POWER ON restart of the Control Unit.

[Jump to Fix](#fix)

## Common Causes

- **Commissioning or service parameter edited without saving** A parameter was changed using Startdrive, the operator panel, or another tool but was not written to nonvolatile memory.
- **Control Unit configuration parameter modified** A parameter that affects the Control Unit configuration was changed, so the drive requires a full power cycle after saving.
- **Backup or restore activity** Parameter backup or restore operations often trigger this fault when the drive detects the new values need to be committed and the unit restarted.
- **Local operator interface edits** Changes made directly on the drive's keypad or BOP-2 panel without completing the save and power-cycle sequence.

## Step-by-Step Fix {#fix}

1. **Read the active fault and fault buffer** to confirm F01040 is the only active issue and note any recent parameter activity.
2. **Identify the recent parameter change** and verify whether it was intentional by reviewing the edit log or consulting with commissioning personnel.
3. **Save the parameters using p0971** as directed by the Siemens fault remedy. Navigate to p0971 in your parameter list and execute the save command.
4. **Perform a complete POWER ON cycle** of the Control Unit by removing mains power, waiting for capacitor discharge (at least 30 seconds), then re-energizing the drive.
5. **Recheck operation after restart** and confirm the fault clears from the fault buffer and the drive returns to normal run state.
6. **If the fault returns immediately**, re-check for additional parameter edits or configuration issues in the drive object and verify the save operation completed successfully.
7. **Review the parameter change history** in the drive diagnostics to make sure no unintended edits are pending and that the Control Unit firmware supports the parameters you changed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens BOP-2 Basic Operator Panel | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01040-fault-code&k=Siemens+BOP-2+Basic+Operator+Panel&tag=errorcodefixes-20) \| Replacement keypad if the local panel is faulty and preventing parameter save operations. |
| Siemens G120 Control Unit (CU240 or CU250 series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01040-fault-code&k=Siemens+G120+Control+Unit+%28CU240+or+CU250+series%29&tag=errorcodefixes-20) \| Only needed if the Control Unit fails to retain saved parameters after multiple save and power-cycle attempts. |

## When to Call a Pro

Call a qualified drive technician or controls integrator if the fault does not clear after you save parameters with p0971 and perform a full POWER ON cycle, or if the drive fails to retain parameter settings across power cycles. Also seek professional help if you are unsure which parameter was changed or if F01040 appears repeatedly without any known edits. Because this fault is configuration-related rather than a component failure, a technician with Siemens Startdrive or SINAMICS experience can verify parameter integrity, check firmware compatibility, and inspect the Control Unit memory system.

## See Also

- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Micromaster F0012 - Causes & Fix](/posts/siemens-micromaster-vfd-f0012-fault-code/)
- [Siemens Micromaster F0024 - Causes & Fix](/posts/siemens-micromaster-vfd-f0024-fault-code/)
- [Siemens G120 F01250 Fault - Causes & Fix](/posts/siemens-g120-vfd-f01250-fault-code/)
