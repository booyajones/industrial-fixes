---
title: "Siemens G120 A05006 - IGBT Overtemperature Warning & Fix"
description: "Siemens G120 A05006 signals IGBT junction temperature rise. Learn the real causes, diagnostic steps, and cooling fixes."
pubDatetime: 2026-05-28T09:06:11Z
modDatetime: 2026-05-28T09:06:11Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 A05006 — What It Means

A05006 on a Siemens SINAMICS G120 is a warning, not a trip fault. It means the power unit has detected an IGBT junction temperature rise warning, also called an overtemperature thermal model warning. Siemens describes the cause as the difference between the heat sink and IGBT junction temperature exceeding the warning limit. This alarm appears on blocksize power units and does not stop the drive, but it tells you the thermal margin is shrinking and action is needed to prevent a fault.

The drive monitors the IGBT junction temperature using a thermal model. When the calculated junction temperature climbs too far above the measured heatsink temperature, the drive raises A05006. The alarm reaction is NONE, so the drive continues running, but if the condition worsens the warning may escalate to a trip fault such as F30024. Address the root cause before that happens.

[Jump to Fix](#fix)

## Common Causes

- **Sustained overload or high load cycle** The motor or application is drawing more current than the thermal model can safely absorb over time, pushing junction temperature toward its limit.
- **Blocked or restricted airflow** Dust, debris, or obstruction around the power unit prevents cooling air from reaching the heatsink and raises the temperature difference.
- **Failed or underperforming cooling fan** The internal or external cooling fan has stopped, slowed down, or lost efficiency, reducing forced air circulation through the heatsink.
- **High ambient temperature** The cabinet or installation environment exceeds the rated ambient temperature, limiting the drive's ability to reject heat.
- **Drive undersized for the application** The G120 power unit is too small for the continuous duty cycle or torque demand, causing chronic thermal stress.
- **Dirty or clogged heatsink** Accumulated dust, oil, or lint on the heatsink fins insulates the surface and prevents efficient heat transfer to the air.

## Step-by-Step Fix {#fix}

1. **Verify the alarm and record context** by checking the drive display or r2110 for stored alarm data, noting when the alarm appeared and under what load conditions.
2. **Check the load profile** by reviewing motor nameplate current, measured operating current, and duty cycle to confirm the application is not exceeding the drive's thermal rating.
3. **Inspect the cooling fan** by listening for fan operation, checking fan speed if monitored, and replacing the fan if it has stopped or runs intermittently.
4. **Clean the heatsink and verify airflow** by removing dust and debris from the heatsink fins, checking intake and exhaust paths, and confirming cabinet ventilation is unobstructed.
5. **Measure ambient temperature** inside the cabinet and compare it to the G120 rated ambient limit, improving ventilation or adding cabinet cooling if necessary.
6. **Review thermal parameters** such as P0604 motor temperature warning threshold and other temperature-related settings to confirm correct configuration for your motor and application.
7. **Clear the alarm and monitor** by resetting via the operator panel, power cycle, or control word after correcting the cause, then observe whether the alarm returns under the same load conditions.

## Parts Often Needed

| Part | Notes |
|------|-------|
| G120 power unit cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05006-fault-code&k=G120+power+unit+cooling+fan&tag=errorcodefixes-20) \| Replace if fan has failed or runs at reduced speed, match to your power unit frame size. |
| Cabinet ventilation fan or filter kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05006-fault-code&k=Cabinet+ventilation+fan+or+filter+kit&tag=errorcodefixes-20) \| Improve cabinet airflow if ambient temperature or circulation is insufficient. |
| G120 power module or blocksize unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05006-fault-code&k=G120+power+module+or+blocksize+unit&tag=errorcodefixes-20) \| Consider if thermal warning persists after all cooling and load corrections, consult Siemens for sizing and part number. |

## When to Call a Pro

Call a qualified drive technician or Siemens service partner if the A05006 alarm returns repeatedly after you have corrected load, cleaned cooling paths, and verified the fan. If the warning escalates to a trip fault like F30024, or if you discover the drive is chronically undersized for the application, professional analysis of the thermal model, load profile, and possible power unit replacement is the safest path. Also reach out for help if you lack the tools to measure current accurately or if the installation requires cabinet redesign to meet thermal specifications.
