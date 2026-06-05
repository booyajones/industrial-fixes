---
title: "Siemens G120 A05006 Alarm - Causes & Fix"
description: "A05006 means power module overtemperature on your Siemens G120 drive. Most often caused by blocked airflow or a failed cooling fan."
pubDatetime: 2026-06-01T11:34:01Z
modDatetime: 2026-06-01T11:34:01Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 A05006 Alarm — What It Means

A05006 is an alarm (not a fault) indicating that your Siemens SINAMICS G120 variable frequency drive has detected power module overtemperature. Specifically, the thermal model has calculated that the temperature difference between the semiconductor chip and the heat sink has exceeded the permissible limit on blocksize power units. This is a warning condition. If the temperature continues to rise and the alarm is not addressed, it can escalate to fault F30024, which will trip the drive offline.

[Jump to Fix](#fix)

## Common Causes

- **Blocked air intake or clogged heatsink fins** Dust buildup, debris, or obstruction in the ventilation path restricts cooling airflow and causes heat to accumulate in the power module.
- **Cooling fan failure or degraded performance** The internal or external cooling fan may be stalled, running slowly, or completely failed, preventing adequate heat removal from the heatsink.
- **High ambient temperature or inadequate clearance** The drive may be installed in an enclosure with poor ventilation, insufficient spacing around the unit, or an environment above its rated thermal limits.
- **Sustained overload or high duty cycle** Continuous heavy loading, frequent starts and stops, or excessive current draw forces the thermal model to accumulate heat beyond normal operating conditions.
- **Power module internal thermal issue** If the alarm recurs even with normal cooling and loading, the power module itself may have a thermal sensing fault or internal degradation.

## Step-by-Step Fix {#fix}

1. **Verify the alarm code** in the drive's diagnostics or alarm buffer to confirm it is A05006 and not a different A050xx or F30xxx condition.
2. **Inspect the airflow path** by checking enclosure ventilation openings, air intake ports, and heatsink fins for dust, debris, or physical obstructions that block cooling air.
3. **Check cooling fan operation** by confirming the fan starts, runs at normal speed, and is not noisy, stalled, or intermittent during drive operation.
4. **Verify ambient conditions and clearances** to make sure the drive has adequate space around it and is not installed above its environmental temperature limits or with blocked ventilation zones.
5. **Reduce process loading if needed** by reviewing the application for continuous overload, excessive start-stop cycles, or higher-than-rated current demand that would drive thermal buildup.
6. **Power-cycle after cooling and inspection** by removing power, allowing the unit to cool completely, then reapplying power. If the alarm recurs immediately, an unresolved thermal problem is still present.
7. **Replace the power module** if the alarm persists despite verified airflow, normal fan operation, and reasonable loading, as this points to a failed power module or internal thermal sensor fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05006-fault-code&k=Siemens+G120+cooling+fan+assembly&tag=errorcodefixes-20) \| Replacement fan for your specific G120 frame size. Verify frame and voltage before ordering. |
| Siemens G120 power module (PM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05006-fault-code&k=Siemens+G120+power+module+%28PM%29&tag=errorcodefixes-20) \| Blocksize power unit for your drive frame. Match the exact model and current rating from your drive nameplate. |
| Enclosure air filter kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05006-fault-code&k=Enclosure+air+filter+kit&tag=errorcodefixes-20) \| Replacement intake filters if your installation uses a filtered enclosure or cabinet. |

## When to Call a Pro

If you have cleaned all ventilation paths, confirmed fan operation, and verified normal ambient conditions but the A05006 alarm returns immediately or frequently, call a qualified electrician or Siemens service partner. Persistent thermal alarms despite good cooling conditions usually mean a failing power module or internal thermal sensor fault that requires module-level replacement and diagnostic tools. Also call a professional if you are not comfortable working inside energized industrial control panels or if your facility requires certified personnel for VFD service work.

## See Also

- [Siemens Micromaster F0020 - Causes & Fix](/posts/siemens-micromaster-f0020-fault-code/)
- [Siemens SINAMICS G120 Fault F30021, Ground Fault Causes & Fix](/posts/siemens-sinamics-g120-fault-f30021/)
- [Siemens G120 A05000 Alarm - Causes & Fix](/posts/siemens-g120-vfd-a05000-fault-code/)
- [Siemens SINAMICS G120X Fault Codes: Complete Guide](/posts/siemens-g120x-fault-codes/)
