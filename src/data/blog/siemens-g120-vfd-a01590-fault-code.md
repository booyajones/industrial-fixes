---
title: "Siemens G120 A01590 Alarm - Causes & Fix"
description: "A01590 means your motor maintenance interval has expired on the G120 VFD. Reset parameter p0651 after performing scheduled motor service."
pubDatetime: 2026-05-31T11:21:17Z
modDatetime: 2026-05-31T11:21:17Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 A01590 Alarm — What It Means

A01590 is an alarm on the Siemens SINAMICS G120 that indicates your configured motor maintenance interval has expired. This is a service reminder, not a fault that trips the drive. The VFD continues to run while displaying the alarm. The drive is simply telling you that the maintenance counter has reached the interval you set during commissioning. Unlike overcurrent or communication faults, A01590 does not point to a failed power component in the drive itself. It is cleared by performing the scheduled maintenance on your motor or driven equipment and then resetting parameter p0651.

[Jump to Fix](#fix)

## Common Causes

- **Maintenance interval elapsed** The drive's internal counter has reached the motor service interval configured in your commissioning parameters.
- **Interval set too short** The maintenance parameter was programmed with a shorter interval than your application actually requires, causing premature alarms.
- **High runtime accumulation** The motor has genuinely accumulated enough operating hours or cycles to warrant the scheduled service.
- **Incorrect motor profile** The wrong motor or service profile was selected during setup, triggering an alarm at an inappropriate time.

## Step-by-Step Fix {#fix}

1. **Verify the alarm** in the drive's diagnostic buffer or display to confirm it is A01590 and not a different code stored in the history.
2. **Inspect the motor** for the maintenance items tied to this interval, including bearings, lubrication points, cooling fans, couplings, contamination, and abnormal vibration or noise.
3. **Perform the required service** on the motor and driven system according to your plant's maintenance schedule or the manufacturer's motor manual.
4. **Reset the maintenance counter** by accessing parameter p0651 in the drive's commissioning software or control panel and clearing or reloading the interval.
5. **Test run the drive** to confirm the alarm does not return immediately, which would indicate an incorrect interval setting or commissioning error.
6. **Review the interval setting** in your commissioning parameters if the alarm reappears without sufficient runtime, and adjust p0651 to match your actual maintenance schedule.
7. **Document the service** date and reset in your maintenance log so future alarms align with actual service intervals.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01590-fault-code&k=Motor+bearings&tag=errorcodefixes-20) \| Replace if worn or noisy during the maintenance inspection triggered by this alarm. |
| Motor cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01590-fault-code&k=Motor+cooling+fan&tag=errorcodefixes-20) \| Service or replace if contaminated or damaged, common maintenance item for interval-based service. |
| Lubrication supplies | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01590-fault-code&k=Lubrication+supplies&tag=errorcodefixes-20) \| Grease or oil for motor bearings and couplings, per your motor manufacturer's specification. |

## When to Call a Pro

Call a technician or controls engineer if you are not familiar with Siemens commissioning software and cannot locate or reset parameter p0651, or if the alarm returns immediately after reset despite correct service. Also call for help if you discover actual motor damage during inspection (bearing failure, winding damage, or abnormal temperature) that requires troubleshooting beyond routine maintenance. If your facility does not have documentation of the original maintenance interval settings, a Siemens-trained technician can review the commissioning file and verify that p0651 matches your application's service needs.
