---
title: "Siemens G120 F0004 - Causes & Fix"
description: "F0004 means inverter overtemperature. Most often caused by blocked airflow or a failed cooling fan. Check filters and fan before replacing the power module."
pubDatetime: 2026-06-01T11:35:50Z
modDatetime: 2026-06-01T11:35:50Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F0004 — What It Means

F0004 on a Siemens G120 VFD signals an inverter or power module overtemperature fault. The drive has detected that the internal inverter temperature has exceeded its safe operating threshold and has shut down to protect the power stage from thermal damage. This fault is the drive's way of telling you that heat is not being removed fast enough from the power electronics, either because cooling has failed or because the drive is working too hard in a hot environment.

[Jump to Fix](#fix)

## Common Causes

- **Blocked or restricted airflow** Dust, debris, or obstructions around the heatsink, cabinet vents, or drive mounting clearances prevent cooling air from reaching the inverter.
- **Cooling fan failure** The internal fan has stopped running, is running too slowly, or is intermittent, so the inverter cannot shed heat during operation.
- **High ambient temperature** The enclosure or room temperature exceeds the G120's rated operating environment, overwhelming the cooling system even when it is functioning normally.
- **Excessive load or overload condition** A stalled motor, repeated high-current cycles, or mechanical overload forces the inverter to dissipate more heat than the cooling system can handle.
- **Clogged air filters or dirty heatsink** Accumulated contamination on filters or heatsink fins reduces thermal transfer and starves the drive of fresh cooling air.
- **Internal temperature sensor or power module fault** A defective temperature sensing circuit or damaged power module incorrectly reports or actually generates excessive heat, triggering the trip.

## Step-by-Step Fix {#fix}

1. **Verify the fault code** by checking the drive display or parameter list and note any associated diagnostic values (such as r0947 or r0949) before clearing the fault.
2. **Inspect all cooling paths** including cabinet intake and exhaust fans, drive internal fan, air filters, and heatsink fins for dust, blockages, or physical obstructions.
3. **Measure the ambient temperature** at the drive location and compare it to the rated operating range in the G120 installation manual for your frame size and module variant.
4. **Check the motor and load** for mechanical binding, repeated overload, or high-current conditions that would force the inverter to work harder and generate excess heat.
5. **Allow the drive to cool completely**, then restart under no-load or light-load conditions to determine if the fault returns immediately or only under full operating current.
6. **Test or replace the cooling fan** if it is not spinning, running intermittently, making unusual noise, or moving air weakly when the drive is powered and calling for cooling.
7. **Clean or replace air filters and heatsink** if contamination is present, then retest the drive to confirm normal thermal performance before returning to full operation.
8. **Contact Siemens service or a qualified drive technician** if the fault persists after all cooling-system checks, as the power module or internal temperature sensing circuit may require factory-level repair or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0004-fault-code&k=Siemens+G120+cooling+fan+assembly&tag=errorcodefixes-20) \| Match to your specific G120 frame size and module variant. |
| Cabinet air filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0004-fault-code&k=Cabinet+air+filter&tag=errorcodefixes-20) \| Replace if airflow restriction is causing elevated enclosure temperature. |
| Siemens G120 power module (inverter section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0004-fault-code&k=Siemens+G120+power+module+%28inverter+section%29&tag=errorcodefixes-20) \| Required only if internal hardware failure is confirmed after cooling-system repairs. |

## When to Call a Pro

Call a qualified VFD technician or Siemens authorized service provider if the F0004 fault returns immediately after the drive has cooled and all visible cooling components (fans, filters, heatsinks) have been cleaned or replaced. Persistent overtemperature trips after environmental and airflow corrections usually indicate a failed power module, defective internal temperature sensor, or other circuit-level fault that requires diagnostic tools, replacement modules, and firmware-level troubleshooting beyond typical field maintenance.

## See Also

- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
- [Siemens Micromaster F0001 - Causes & Fix](/posts/siemens-micromaster-f0001-fault-code/)
- [Siemens G120 A05002 - Causes & Fix](/posts/siemens-g120-a05002-fault-code/)
- [Siemens G120 F0007 Fault Code - Causes & Fix](/posts/siemens-g120-vfd-f0007-fault-code/)
