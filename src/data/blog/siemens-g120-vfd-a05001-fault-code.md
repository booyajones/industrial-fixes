---
title: "Siemens G120 A05001 Fault Code - Causes & Fix"
description: "A05001 on a Siemens G120 VFD is a Power Module overtemperature alarm. Most often caused by blocked airflow or a failed cooling fan."
pubDatetime: 2026-06-01T11:31:08Z
modDatetime: 2026-06-01T11:31:08Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Power Module (PM)"
---

## Siemens G120 A05001 Fault Code — What It Means

A05001 is an alarm indicating that the Power Module in your Siemens SINAMICS G120 variable frequency drive has reached or is approaching its thermal limit. This alarm monitors the power semiconductor chip temperature inside the AC converter power unit. It is a warning condition, not an immediate trip fault. The drive is telling you that the internal power electronics are running too hot and cooling or load conditions need correction before thermal shutdown or component damage occurs.

[Jump to Fix](#fix)

## Common Causes

- **Insufficient cooling or blocked airflow** The most common cause is obstructed air inlets or outlets, dirty heatsinks, or inadequate cabinet ventilation that prevents heat from leaving the drive.
- **Failed or underperforming cooling fan** The internal or cabinet cooling fan has stopped or is running too slowly to remove heat from the Power Module.
- **High ambient temperature** The environment around the drive exceeds the manufacturer's thermal design limits, reducing the drive's ability to dissipate heat.
- **Excessive mechanical load or duty cycle** The motor is loaded beyond the drive's thermal capacity or the application duty cycle is too aggressive for the installed Power Module size.
- **High switching frequency settings** Operating the drive at an elevated pulse frequency increases power semiconductor losses and heat generation in the Power Module.
- **Power Module thermal sensor or internal hardware fault** If all environmental and load causes are ruled out, the Power Module itself or its temperature sensing circuit may have degraded or failed.

## Step-by-Step Fix {#fix}

1. **Check the ambient temperature** around the drive and inside the cabinet to confirm it is within the G120's rated operating range and that the installation environment has not changed.
2. **Inspect and clean the heatsink and air paths.** Remove dust, dirt, and debris from the Power Module heatsink fins, air inlets, and cabinet exhaust vents to restore full airflow.
3. **Verify all cooling fans are running** at full speed on both the drive and any cabinet ventilation equipment. Listen for abnormal noise or slow rotation and replace any failed fans immediately.
4. **Review the load and duty cycle.** Compare the motor nameplate current and actual running current against the drive's continuous rating to confirm the application is not overloading the Power Module thermally.
5. **Check the pulse frequency parameter** in the drive settings. If it has been increased from default, consider lowering it to reduce switching losses and heat generation in the power semiconductors.
6. **Allow the drive to cool completely** and then reset the alarm. Monitor the drive under normal load to see if the A05001 alarm returns or if the thermal condition was temporary.
7. **Replace the Power Module assembly** if the alarm persists after all ventilation, load, and environmental corrections have been made. This indicates an internal thermal fault or sensor issue in the power unit hardware.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Power Module (PM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05001-fault-code&k=Siemens+G120+Power+Module+%28PM%29&tag=errorcodefixes-20) \| Match the exact frame size and power rating to your existing drive. Consult the drive nameplate and Siemens documentation for the correct Power Module part number. |
| Cooling fan for G120 Power Module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05001-fault-code&k=Cooling+fan+for+G120+Power+Module&tag=errorcodefixes-20) \| OEM replacement fan assembly for the specific G120 frame size. Verify voltage and connector type before ordering. |

## When to Call a Pro

Call a qualified drive technician or contact Siemens technical support if the A05001 alarm returns immediately after cooling and cleaning, if you measure normal airflow and ambient conditions but the drive still overheats, or if you are not comfortable working with three-phase power and VFD internal components. Persistent thermal alarms after environmental corrections usually mean an internal Power Module fault that requires module-level replacement or factory service. If your process cannot tolerate downtime for troubleshooting, bring in a professional with Siemens-specific diagnostic tools and replacement parts on hand.

## See Also

- [Siemens G120 F01659 - Causes & Fix](/posts/siemens-g120-vfd-f01659-fault-code/)
- [Siemens Micromaster F0015 - Causes & Fix](/posts/siemens-micromaster-f0015-fault-code/)
- [Siemens SINAMICS G120 F30021 Fault — Ground Fault Fix](/posts/siemens-sinamics-f30021-fault/)
- [Siemens G120 A05000 - Causes & Fix](/posts/siemens-g120-a05000-fault-code/)
