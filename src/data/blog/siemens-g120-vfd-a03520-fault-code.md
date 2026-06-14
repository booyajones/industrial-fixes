---
title: "Siemens G120 A03520 Fault - Causes & Fix"
description: "A03520 is a temperature sensor fault in the G120 Control Unit. Most often caused by poor airflow or a failed CU sensor circuit."
pubDatetime: 2026-06-01T11:29:51Z
modDatetime: 2026-06-01T11:29:51Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
most_likely_cause: "Faulty or disconnected CU temperature sensor circuit"
---

## Siemens G120 A03520 Fault — What It Means

A03520 on a Siemens SINAMICS G120 is a temperature sensor fault in the Control Unit (CU), not a motor overtemperature alarm. The 'A' prefix means this is an alarm rather than a hard trip fault, so the drive may continue to run while the alarm is active. The code indicates the CU's internal temperature sensing circuit has failed, disconnected, or detected an out-of-range condition. In most cases the drive logs the alarm and continues operation, but the condition should be addressed to prevent future issues or progression to a fault that stops the drive.

[Jump to Fix](#fix)

## Common Causes

- **Faulty or disconnected CU temperature sensor circuit** The Control Unit's internal temperature sensor or its wiring has failed or become disconnected, triggering the alarm even when ambient temperature is normal.
- **Blocked air intake or poor ventilation around the Control Unit** Dust, debris, or obstructed cooling vents prevent adequate airflow over the CU, causing elevated temperatures that can trigger the sensor alarm.
- **Failed or stopped Control Unit cooling fan** If your G120 uses a dedicated CU fan, a fan failure will reduce cooling and may cause the temperature sensor to report a fault condition.
- **Internal CU electronics degradation** Age, heat stress, or component wear inside the Control Unit can cause the temperature sensing circuit to malfunction and report false alarms.
- **Firmware or configuration issue** Outdated firmware or corrupted CU configuration can occasionally produce spurious temperature sensor alarms that persist across resets.
- **High ambient temperature in the enclosure** Enclosure temperatures exceeding the Control Unit's rated operating range will cause legitimate temperature sensor alarms even if the sensor itself is functioning correctly.

## Step-by-Step Fix {#fix}

1. **Record the alarm details** from the drive display or parameter buffer (check the fault/alarm history) before clearing or resetting anything, so you have a reference if the alarm recurs.
2. **Power down completely** by switching off all incoming power to the G120 and waiting at least 30 seconds, then power back up. A full power cycle clears transient faults and allows the CU to re-initialize its sensor circuits.
3. **Inspect and clean all cooling paths** around the Control Unit. Remove dust and debris from air intake slots, verify ventilation openings are not blocked, and confirm the CU fan (if fitted) is spinning and free of obstructions.
4. **Allow the drive to cool** for 15 to 30 minutes if the enclosure feels warm, then check whether the alarm clears automatically. Siemens temperature alarms often reset once the CU temperature drops below the threshold.
5. **Check ambient enclosure temperature** with a thermometer. If the enclosure exceeds the G120's rated ambient range, improve ventilation, add external cooling, or relocate the drive to a cooler environment.
6. **Update or reload CU firmware** if the alarm persists after cooling and cleaning. Consult your G120 documentation or Siemens support for the correct firmware version and update procedure for your specific Control Unit model.
7. **Replace the Control Unit** if the A03520 alarm returns immediately after power-up or does not clear with normal airflow and cooling. Match the replacement CU to your G120 Power Module type code and make sure firmware compatibility before installation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a03520-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Match the CU model and firmware version to your existing Power Module. Common CU variants include CU240E-2, CU250S-2, and others specific to your G120 configuration. |
| Control Unit cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a03520-fault-code&k=Control+Unit+cooling+fan&tag=errorcodefixes-20) \| If your G120 CU uses a dedicated fan, verify the part number from the drive nameplate or service manual before ordering a replacement. |

## When to Call a Pro

Call a qualified drive technician or Siemens-certified service provider if the A03520 alarm persists after you have cleaned cooling paths, verified airflow, and performed a full power cycle. Control Unit replacement requires matching the correct CU model to your Power Module and may involve firmware updates or parameter cloning, which are best handled by a technician with Siemens drive experience and access to commissioning tools. Also call a pro if you are unfamiliar with high-voltage industrial equipment, if the drive is part of a critical process, or if your facility requires documented service records for safety and compliance.

## See Also

- [Siemens SINAMICS G120 F30003 Fault — DC Link Undervoltage Fix](/posts/siemens-sinamics-f30003-fault/)
- [Siemens Micromaster F0005 - Causes & Fix](/posts/siemens-micromaster-f0005-fault-code/)
- [Siemens Micromaster F0085 - Causes & Fix](/posts/siemens-micromaster-f0085-fault-code/)
- [Siemens Micromaster F0005 - Causes & Fix](/posts/siemens-micromaster-vfd-f0005-fault-code/)
