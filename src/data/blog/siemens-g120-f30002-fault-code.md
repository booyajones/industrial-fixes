---
title: "Siemens G120 F30002 - Causes & Fix"
description: "Siemens G120 F30002 is a DC-link overvoltage fault. Learn the causes, diagnostic steps, and repair procedure for this drive fault."
pubDatetime: 2026-05-28T09:06:45Z
modDatetime: 2026-05-28T09:06:45Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Braking resistor for Siemens G120"
most_likely_cause: "Too-rapid deceleration or aggressive ramp settings"
---

## Siemens G120 F30002 — What It Means

F30002 on a Siemens SINAMICS G120 means DC-link overvoltage. The power unit has detected that the intermediate circuit voltage has exceeded its permitted limit and trips to protect itself. This is a drive hardware protection fault, not a motor overload condition.

The fault is most often associated with regenerative energy returning from the motor back into the DC link, especially during deceleration or braking. When energy flows back faster than the drive can absorb or dissipate it, the DC bus voltage rises above the safe threshold and triggers the fault.

[Jump to Fix](#fix)

## Common Causes

- **Too-rapid deceleration or aggressive ramp settings** The motor is decelerating too quickly and pushing regenerative energy back into the DC link faster than the drive can handle it.
- **Braking resistor missing, open, or undersized** The braking resistor is not present, not wired correctly, open circuit, overheated, or incorrectly sized for the application.
- **Regenerative energy from high-inertia or overhauling loads** The application involves a large inertia load or a load that actively drives the motor (such as lowering a heavy mass) and generates excess energy.
- **Line voltage disturbances or supply fluctuations** The incoming AC supply is experiencing spikes, surges, or other disturbances that raise the DC-link voltage above normal levels.
- **Incorrect drive parameterization for braking** The drive's braking parameters, deceleration ramps, or chopper settings are not configured properly for the application.
- **Control tuning issues causing DC-link oscillation** Poor PID tuning or speed control oscillation repeatedly builds up energy in the DC link during normal operation.

## Step-by-Step Fix {#fix}

1. **Stop the drive safely** and verify there is no mechanical runaway or hazardous motion from the load.
2. **Identify when the fault occurs** by checking whether it trips during deceleration, stopping, lowering a load, or speed changes to narrow down the root cause.
3. **Inspect the braking resistor and wiring** to confirm it is present, correctly connected, not open circuit, and shows no signs of overheating or damage.
4. **Review and lengthen the deceleration ramp time** in the drive parameters to reduce the regenerative energy peak and allow more time for the drive to absorb it.
5. **Check the supply voltage quality** using a multimeter or power analyzer to confirm the incoming mains are stable and within specification.
6. **Review the drive's diagnostic buffer** using the control panel or STARTER software to confirm the DC-link voltage reading at the time of fault.
7. **Test-run the drive after making changes** and monitor the DC-link voltage during braking or load changes to verify the fault does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Braking resistor for Siemens G120 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f30002-fault-code&k=Braking+resistor+for+Siemens+G120&tag=errorcodefixes-20) \| Verify correct ohm and watt rating for your G120 frame size and application inertia. Consult the G120 manual for your model. |
| Brake chopper module (if external) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f30002-fault-code&k=Brake+chopper+module+%28if+external%29&tag=errorcodefixes-20) \| Required if your drive setup uses an external braking chopper and it has failed or is not engaging. |
| G120 power unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f30002-fault-code&k=G120+power+unit&tag=errorcodefixes-20) \| Only replace if internal diagnostics confirm a hardware fault in the DC-link circuit itself rather than an external braking or supply issue. |

## When to Call a Pro

Call a qualified drives technician or Siemens service partner if you have checked the braking resistor and ramp settings but the fault persists, or if you are unfamiliar with drive parameter configuration and DC-link diagnostics. Also call a professional if the fault occurs with no apparent regenerative condition (such as during constant speed) or if the drive's diagnostic buffer shows unusual voltage levels that suggest internal power unit damage. Applications with complex braking requirements or safety-rated motion control should always be serviced by trained personnel.

## See Also

- [Siemens VFD F1 Fault - Causes & Fix](/posts/siemens-vfd-f1-fault/)
- [Siemens G120 F01018 - Causes & Fix](/posts/siemens-g120-f01018-fault-code/)
- [Siemens G120 F01600 - Causes & Fix](/posts/siemens-g120-f01600-fault-code/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
