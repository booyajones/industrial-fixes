---
title: "Siemens G120 A05004 - Causes & Fix"
description: "Siemens G120 A05004 means rectifier overtemperature alarm. Learn the causes, step-by-step troubleshooting, and parts to fix it."
pubDatetime: 2026-05-28T09:05:30Z
modDatetime: 2026-05-28T09:05:30Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 cooling fan"
most_likely_cause: "Excessive ambient temperature"
---

## What this code means
A05004 on a Siemens SINAMICS G120 is an alarm for rectifier overtemperature. The drive has detected that the input rectifier section has reached the alarm threshold for excessive temperature. If the temperature climbs another 5 K, the alarm escalates to fault F30037 and the drive will trip.

This alarm means the power conversion components at the input of the drive are running too hot. It can be caused by conditions outside the drive or by an internal problem in the rectifier itself. The drive is warning you before it shuts down completely.

## Common Causes

- **Excessive ambient temperature** The room or enclosure temperature exceeds the drive's permitted operating range, preventing the rectifier from cooling properly.
- **Cooling fan failure or blocked airflow** The drive's internal fan has stopped, or dust, debris, or obstructions block the heatsink or ventilation openings.
- **Load or duty cycle beyond drive rating** The application draws more current or runs a heavier duty cycle than the drive is thermally sized to handle.
- **Missing or unbalanced input phase** A lost phase or poor line conditions force the rectifier to work harder, generating excess heat.
- **Defective rectifier arm or power module** An internal component in the incoming rectifier section has failed or degraded, causing localized overheating.

## Step-by-Step Fix {#fix}

1. Confirm the alarm on the drive display or control panel and note whether it has already escalated to a fault state or is still at the warning level.
2. Check ambient temperature in the cabinet and verify it falls within the drive's nameplate specifications, then confirm all ventilation grilles and enclosure doors are unobstructed.
3. Inspect the cooling fan for operation, listen for abnormal noise, and look for dust buildup on the heatsink fins or air intake, cleaning if necessary.
4. Verify all three input phases are present at the drive terminals using a multimeter, and inspect power connections for loose, discolored, or burnt terminals.
5. Review the motor nameplate current and application duty cycle against the drive's continuous and overload ratings to confirm the drive is not undersized for the load.
6. Clear the alarm by cycling power or using the control panel reset function only after correcting the underlying cause.
7. If the alarm returns immediately after cooling and supply checks pass, suspect an internal rectifier defect and prepare to replace the power module or contact a qualified service technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05004-fault-code&k=Siemens+G120+cooling+fan&tag=errorcodefixes-20) \| Match the fan part number to your specific G120 frame size and power rating. |
| Siemens G120 power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05004-fault-code&k=Siemens+G120+power+module&tag=errorcodefixes-20) \| Required if the rectifier section itself is defective after all external causes are ruled out. |

## When to Call a Pro

Call a qualified drive technician if the alarm persists after you have verified ambient temperature, confirmed cooling fan operation, cleaned all air paths, and checked the incoming power supply. Internal rectifier failures require specialized testing and often replacement of the entire power module. If you are not trained to work safely on live industrial power equipment or do not have the tools to measure phase balance and inspect high-voltage connections, stop and call for service. Repeated overtemperature alarms can damage other components in the drive if the root cause is not corrected.
