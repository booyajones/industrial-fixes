---
title: "Siemens G120 A05002 - Causes & Fix"
description: "Siemens G120 A05002 alarm means air intake overtemperature. Learn the common causes and step-by-step repair for restoring airflow."
pubDatetime: 2026-05-28T09:04:59Z
modDatetime: 2026-05-28T09:04:59Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 cooling fan assembly"
most_likely_cause: "High ambient temperature"
---

## What this code means
A05002 is an alarm, not a fault, indicating that the air intake temperature of your Siemens SINAMICS G120 power unit has reached its threshold. For air-cooled power units, this alarm typically triggers at 42 °C with a 2 K hysteresis. If the intake temperature continues to rise by an additional 13 K without correction, the drive will escalate to fault F30035 and shut down. The alarm warns you to address cooling or airflow problems before the drive trips completely.

## Common Causes

- **High ambient temperature** The room or enclosure around the drive is too hot, pushing intake air above the 42 °C threshold.
- **Failed or slow cooling fan** The internal fan is not running, is rotating too slowly, or is making unusual noise and not moving enough air.
- **Blocked or dirty air path** Clogged filters, obstructed vents, or poor cabinet ventilation restrict airflow through the drive.
- **Hot exhaust recirculation** Cabinet or enclosure layout allows hot exhaust air to loop back into the drive intake.
- **High load cycle or power dissipation** Operating the drive near its thermal limit increases internal heat, contributing to elevated intake temperatures.

## Step-by-Step Fix {#fix}

1. {'lead': 'Check ambient temperature at the drive intake', 'text': 'using a thermometer or infrared gun and compare it to the installation limits in your G120 manual.'}
2. {'lead': 'Inspect the cooling fan', 'text': 'for proper operation, correct rotation, and unusual noise, and replace it if it is not running or is failing.'}
3. {'lead': 'Clean or replace air filters', 'text': 'and remove any obstructions from vents, louvers, or cabinet fans to restore full airflow.'}
4. {'lead': 'Check for hot-air recirculation', 'text': 'in the enclosure and adjust cabinet layout, spacing, or ducting to separate intake and exhaust paths.'}
5. {'lead': 'Reduce thermal load if necessary', 'text': 'by reviewing load cycle, motor duty, or power dissipation and confirming the drive is sized correctly for the application.'}
6. {'lead': 'Clear the alarm', 'text': 'only after correcting the root cause and verifying that intake temperature has dropped below the threshold.'}
7. {'lead': 'Monitor the drive', 'text': 'after clearing to confirm the alarm does not return and that ambient conditions remain within specification.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05002-fault-code&k=Siemens+G120+cooling+fan+assembly&tag=errorcodefixes-20) \| Replace if the internal fan is not running or airflow is insufficient. |
| Cabinet air filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05002-fault-code&k=Cabinet+air+filter&tag=errorcodefixes-20) \| Clean or replace if clogged or restricting airflow to the drive. |
| G120 power unit module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05002-fault-code&k=G120+power+unit+module&tag=errorcodefixes-20) \| Only if repeated thermal alarms are caused by internal cooling-path defects after all other causes are ruled out. |

## When to Call a Pro

Call a qualified technician if you are uncomfortable working inside the drive enclosure or if the alarm persists after cleaning filters and verifying fan operation. A technician can measure airflow, check thermal sensors, review cabinet cooling design, and determine whether the power unit or fan assembly needs replacement. Professional help is also recommended if the drive escalates to fault F30035 or if you need to verify load-cycle calculations and drive sizing for your application.
