---
title: "Siemens G120 A05000 - Causes & Fix"
description: "Siemens G120 A05000 means power unit heatsink overtemperature. Learn causes like blocked airflow, failed fans, and overload, plus step-by-step repair."
pubDatetime: 2026-05-28T09:03:47Z
modDatetime: 2026-05-28T09:03:47Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Cooling fan assembly"
most_likely_cause: "Blocked airflow or dirty heatsink"
---

## What this code means
A05000 on a Siemens SINAMICS G120 is an alarm indicating that the inverter's heatsink has reached the overtemperature threshold. It is a warning stage, not yet a fault. Siemens describes it as 'Power unit: Heatsink overtemperature' and the drive's response is configurable through parameter p0290. If the heatsink temperature rises another 5 K above this alarm point, the drive will escalate to fault F30004 and shut down to protect itself.

This alarm tells you the power unit is running too hot and the cooling system is not keeping up. The drive is still operational at this stage, but continuing to run without addressing the root cause can lead to a fault trip or damage to the inverter. The most common reasons are environmental (high ambient temperature, poor cabinet ventilation, blocked airflow) or operational (overload, excessive duty cycle, or non-standard pulse frequency settings).

## Common Causes

- **Blocked airflow or dirty heatsink** Dust, debris, or clogged cabinet filters restrict cooling air from reaching the inverter heatsink, causing temperature to climb even under normal load.
- **Failed or slow cooling fan** The inverter's internal or external cooling fan has stopped, is running too slowly, or is not turning on when the drive operates.
- **High ambient or cabinet temperature** The drive is installed in an environment that exceeds Siemens' temperature limits, or cabinet ventilation is inadequate for the heat load.
- **Inverter overload or excessive duty cycle** The connected motor load is too high for the inverter's rating, or the drive is cycling on and off too frequently without enough cool-down time.
- **Pulse frequency set too high** The switching frequency has been increased from default, which raises internal losses and heatsink temperature under the same mechanical load.

## Step-by-Step Fix {#fix}

1. {'lead': 'Check cabinet and ambient temperature', 'text': 'Verify that the enclosure temperature and room ambient are within the installation limits listed in your G120 manual, and confirm cabinet ventilation is working.'}
2. {'lead': 'Inspect airflow and clean the heatsink', 'text': 'Look for dust buildup on the inverter heatsink fins and cabinet filters, remove any blockages, and clean or replace filters to restore full airflow.'}
3. {'lead': 'Verify the cooling fan operation', 'text': 'With the drive powered and running, confirm the fan spins at full speed and listen for unusual noise or vibration that indicates bearing wear or failure.'}
4. {'lead': 'Compare motor power to inverter rating', 'text': "Use parameter p0307 (motor rated power) and read r0206 (inverter rated power) to check that the motor size does not exceed the drive's capacity, and reduce mechanical load if necessary."}
5. {'lead': 'Check pulse frequency setting', 'text': 'Review the pulse frequency parameter and restore it to the factory default if it was raised, since higher switching frequency increases heat generation.'}
6. {'lead': 'Monitor the alarm after corrections', 'text': 'Run the drive under normal load and watch for A05000 to clear or reappear, paying attention to heatsink temperature trends in the drive display or monitoring software.'}
7. {'lead': 'Escalate if overheating persists', 'text': 'If the alarm continues after you have corrected ventilation, loading, and switching settings, the power unit or cooling assembly may be failing and requires deeper service or Siemens support.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05000-fault-code&k=Cooling+fan+assembly&tag=errorcodefixes-20) \| Replace if the fan does not spin, runs slowly, or makes grinding noise during drive operation. |
| Cabinet air filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05000-fault-code&k=Cabinet+air+filter&tag=errorcodefixes-20) \| Clean or replace clogged filters to restore full airflow to the inverter heatsink and enclosure. |

## When to Call a Pro

Call a qualified drive technician or Siemens service if the A05000 alarm persists after you have cleaned the heatsink, verified the fan, improved ventilation, and confirmed the load is within rating. Repeated overtemperature alarms or escalation to fault F30004 can indicate internal power module degradation, a failing thermal sensor, or a cooling system design problem that requires diagnostic tools and factory training to resolve safely. Also reach out for support if you are uncomfortable working inside energized VFD cabinets, because line voltage and DC bus capacitors present serious shock hazards even when the drive appears off.
