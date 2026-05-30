---
title: "Siemens G120 A03520 - Causes & Fix"
description: "Siemens G120 alarm A03520 signals a temperature sensor fault in the Control Unit. Learn causes, diagnostics, and repair steps."
pubDatetime: 2026-05-28T09:03:07Z
modDatetime: 2026-05-28T09:03:07Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 A03520 — What It Means

A03520 is an alarm (not a trip fault) on the Siemens SINAMICS G120 that indicates a temperature sensor error in the Control Unit (CU). The drive has detected a problem with the CU's internal temperature-sensing circuit, not a motor overload or power-module issue. The alarm is stored in the drive's diagnostic memory and appears as "CU: Temperature sensor fault" or "Temperature Sensor Error" in the fault text.

[Jump to Fix](#fix)

## Common Causes

- **Defective temperature sensor in the Control Unit** The sensor chip or circuit inside the CU has failed and no longer returns a valid temperature reading.
- **Loose or damaged CU wiring or connector** If the sensor path uses an external harness or plug, contamination or a loose connection can interrupt the signal.
- **Internal CU electronics failure** A fault in the temperature measurement circuit on the Control Unit board prevents accurate sensing.
- **Temporary corruption or erratic state** A soft fault or memory glitch can trigger the alarm until a full power-off, power-on cycle clears it.

## Step-by-Step Fix {#fix}

1. Read the active alarm in the drive diagnostics and confirm code A03520 is stored in parameter r2110 (active alarms) or the fault history in r0947, r0948, or r0949.
2. Perform a complete power-off, power-on cycle of the drive and associated components to clear any temporary corruption, as recommended in Siemens remedy documentation.
3. Inspect the Control Unit for signs of overheating, discoloration, contamination, or visible damage to connectors and circuit board components.
4. Check any accessible CU temperature-sensor harness or plug for looseness, corrosion, or physical damage if your hardware version has an external sensor path.
5. Replace the Control Unit if the alarm returns immediately after power cycling and no external wiring faults are found.
6. Verify the new CU by powering up and monitoring r2110 to confirm A03520 does not reappear.
7. Escalate to manufacturer-level service if the alarm persists after CU replacement, as the fault is in the temperature-sensing circuit rather than the power module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens SINAMICS G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a03520-fault-code&k=Siemens+SINAMICS+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Match the exact CU variant (CU240, CU250, etc.) to your G120 order number or MLFB label. |
| CU temperature sensor harness or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a03520-fault-code&k=CU+temperature+sensor+harness+or+connector&tag=errorcodefixes-20) \| Only if your hardware version uses an accessible external sensor path. Consult your drive documentation. |

## When to Call a Pro

Call a qualified Siemens service technician or automation specialist if the alarm persists after a full power cycle and you are not comfortable replacing the Control Unit yourself. If the alarm returns immediately after installing a new CU, or if you are unsure which CU variant matches your drive model, professional diagnosis is required. Escalate to the manufacturer if the fault is intermittent or accompanied by other drive errors, as it may indicate a deeper electronics or environmental issue.

## See Also

- [Siemens Micromaster F0011 - Causes & Fix](/posts/siemens-micromaster-f0011-fault-code/)
- [Siemens Micromaster F0020 - Causes & Fix](/posts/siemens-micromaster-f0020-fault-code/)
- [Siemens G120 A05004 - Causes & Fix](/posts/siemens-g120-a05004-fault-code/)
- [Siemens Micromaster F0001 - Causes & Fix](/posts/siemens-micromaster-f0001-fault-code/)
