---
title: "Siemens G120 A05000 Alarm - Causes & Fix"
description: "A05000 means the heatsink is nearing overtemperature. Most often caused by blocked airflow or a failed fan. Check cooling next."
pubDatetime: 2026-06-01T11:30:30Z
modDatetime: 2026-06-01T11:30:30Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 cooling fan assembly"
most_likely_cause: "Blocked or restricted airflow"
---

## What this code means
A05000 is an alarm, not a fault that trips the drive. It means the inverter heatsink temperature has reached the warning threshold and is approaching the point where the drive will shut down to protect itself. The drive continues running when this alarm appears, but you need to address the heat problem before it escalates to a full fault condition. The alarm response behavior is controlled by parameter p0290.

## Common Causes

- **Blocked or restricted airflow** Intake vents, exhaust paths, or heatsink fins are obstructed, preventing cool air from reaching the drive and hot air from escaping.
- **Failed or slow cooling fan** The internal cooling fan has stopped, runs too slowly, or cycles incorrectly, so the heatsink cannot dissipate heat effectively.
- **Ambient temperature too high** The enclosure or room temperature exceeds the drive's rated operating range, or the drive is installed in direct sunlight or near other heat sources.
- **Excessive load or duty cycle** The motor load or the frequency of start/stop cycles exceeds the thermal capacity of the drive, causing higher than normal inverter dissipation.
- **Dust buildup on heatsink** Dirt, dust, or debris has accumulated on the heatsink fins or inside the enclosure, reducing heat transfer and blocking airflow.
- **Incorrect thermal parameter settings** Parameter p0290 or other thermal protection settings are misconfigured, triggering the alarm prematurely or masking a real thermal issue.

## Step-by-Step Fix {#fix}

1. **Check the cooling fan operation** by observing the drive while it runs. Confirm the fan spins at normal speed and does not sound weak or intermittent. If the fan is not running or runs slowly, plan to replace it.
2. **Inspect the heatsink and airflow path** for obstructions, dust, or debris. Remove the drive cover (after isolating power and following lockout procedures) and use compressed air or a soft brush to clean heatsink fins and ventilation openings.
3. **Measure the ambient temperature** inside the enclosure with a thermometer and compare it to the drive's specification sheet. If the ambient exceeds the rated limit, improve cabinet ventilation, add forced cooling, or relocate the drive.
4. **Review the motor load and duty cycle** by checking the output current on the drive display or through parameter monitoring. Compare actual load to the drive nameplate rating. If the drive is consistently loaded near or above rating, reduce load or upsize the drive.
5. **Clear the alarm** and monitor the drive under normal operating conditions. Watch for the alarm to reappear and note the heatsink temperature trend using the drive's internal diagnostics or parameter readouts.
6. **Check parameter p0290** to confirm the alarm response is set correctly for your application. Consult the Siemens G120 parameter manual to understand the configured behavior and adjust if needed.
7. **Contact Siemens support or a qualified technician** if the alarm persists after verifying airflow, fan operation, ambient conditions, and load. A persistent alarm with correct cooling may indicate a heatsink temperature sensor fault or internal drive damage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05000-fault-code&k=Siemens+G120+cooling+fan+assembly&tag=errorcodefixes-20) \| Replacement fan matched to your G120 frame size and power rating. Verify part number from the drive nameplate or Siemens documentation before ordering. |
| Enclosure filter kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05000-fault-code&k=Enclosure+filter+kit&tag=errorcodefixes-20) \| Replacement intake filter for the cabinet if the existing filter is clogged or torn. Clean or replace filters regularly to maintain airflow. |
| Auxiliary cooling fan (cabinet mount) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05000-fault-code&k=Auxiliary+cooling+fan+%28cabinet+mount%29&tag=errorcodefixes-20) \| External fan to improve enclosure ventilation if ambient temperature remains too high after cleaning and the existing cooling is insufficient. |

## When to Call a Pro

Call a qualified electrician or drive technician if the alarm persists after you have cleaned the heatsink, confirmed fan operation, and verified ambient temperature and load conditions are within spec. Also call for help if you are uncomfortable working inside energized electrical enclosures, if the drive shows other simultaneous alarms or faults, or if you need to adjust parameters and are unfamiliar with Siemens drive programming. A technician can perform deeper diagnostics, check the temperature sensor circuit, verify parameter settings, and determine if the drive itself has internal damage requiring repair or replacement.
