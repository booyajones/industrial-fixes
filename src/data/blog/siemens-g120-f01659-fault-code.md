---
title: "Siemens G120 F01659 - Causes & Fix"
description: "Siemens G120 F01659 means Safety Integrated denied your parameter write. Learn why the drive rejects safety changes and how to clear it."
pubDatetime: 2026-05-28T09:01:15Z
modDatetime: 2026-05-28T09:01:15Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F01659 — What It Means

F01659 on a Siemens SINAMICS G120 means the drive has rejected a write request to one or more Safety Integrated parameters on processor 1. This is a configuration and access control fault, not a motor or power stage failure. The drive is protecting the safety system by refusing a change that it cannot allow in the current state.

The exact reason for the rejection is stored in the fault value (r0949), which you must look up in the Siemens List Manual or safety documentation for your specific drive model. This fault does not by itself create a safety stop response. It simply tells you that the safety logic has blocked your parameter modification attempt.

[Jump to Fix](#fix)

## Common Causes

- **Safety password not entered** The drive requires the Safety Integrated password (p9761) before it will accept changes to safety parameters, and the write was attempted without entering it.
- **Safety parameters locked or inhibited** The drive is in an incompatible safety state or the safety function is active, so the safety logic has inhibited writes to those parameters.
- **Parameter reset attempted with Safety Integrated enabled** A drive parameter restore or reset was requested while Safety Integrated was still active, causing the safety system to reject the write.
- **Simulation mode active on safety input** The digital input used by the safety logic is currently in simulation mode, which prevents certain safety parameter changes.
- **Hardware incompatibility** The Control Unit does not support the requested safety function, or the Power Module does not support Safety Integrated at all.
- **Related safety fault active** Another safety fault (such as F01655 or F30655) exists in the chain and is preventing the safety parameter write from completing.

## Step-by-Step Fix {#fix}

1. Read the fault value in r0949 and check the fault buffer to identify the exact sub-cause listed in the Siemens List Manual for your drive model.
2. Check whether the safety password is required. If the fault value indicates this, enter the Safety Integrated password using parameter p9761 before retrying the write.
3. Verify the safety state and inhibit conditions. If Safety Integrated is actively blocking the change, inhibit Safety Integrated using the appropriate safety parameters or reset the safety configuration and then reapply your settings.
4. End any simulation mode on the relevant digital input if that mode is the active cause of the rejection.
5. Look for related safety faults (F01655, F30655) in the fault buffer and resolve those first if they are present, as they may be the root cause blocking the write.
6. Confirm hardware compatibility. Check that your Control Unit supports the safety function you are requesting and that your Power Module supports Safety Integrated.
7. Clear the fault condition, acknowledge or reset the fault, and retry the parameter write. If necessary, cycle STO selection and deselection as part of the safety recovery procedure for your specific configuration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (Safety Integrated compatible) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01659-fault-code&k=Siemens+G120+Control+Unit+%28Safety+Integrated+compatible%29&tag=errorcodefixes-20) \| Required only if your current Control Unit does not support the safety function you need. |
| Siemens G120 Power Module (Safety Integrated compatible) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01659-fault-code&k=Siemens+G120+Power+Module+%28Safety+Integrated+compatible%29&tag=errorcodefixes-20) \| Required only if your current Power Module does not support Safety Integrated and you need that capability. |

## When to Call a Pro

Call a qualified Siemens drive technician or certified safety integrator if you are unfamiliar with Safety Integrated programming, if the fault value in r0949 points to a hardware compatibility issue you cannot resolve, or if related safety faults continue to appear after you clear F01659. Safety parameter configuration requires understanding of the functional safety chain and the specific safety standards (such as SIL or Performance Level) your application must meet. If your facility does not have personnel trained in Siemens Safety Integrated commissioning, professional support is the correct choice to avoid creating unsafe conditions or violating safety certifications.

## See Also

- [Siemens Micromaster F0221 - Causes & Fix](/posts/siemens-micromaster-f0221-fault-code/)
- [Siemens Sinumerik 840D Alarm 25000 — Causes & Fix](/posts/siemens-sinumerik-840d-alarm-25000/)
- [Siemens SINAMICS G120 F30021 Fault — Ground Fault Fix](/posts/siemens-sinamics-f30021-fault/)
- [Siemens Micromaster F0002 - Causes & Fix](/posts/siemens-micromaster-f0002-fault-code/)
