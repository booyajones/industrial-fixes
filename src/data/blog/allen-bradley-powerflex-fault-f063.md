---
title: "Allen-Bradley PowerFlex Fault F063 — Causes & Fix"
description: "What Allen-Bradley PowerFlex fault code F063 means, why SW OverCurrent trips, and how to diagnose and fix it."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
---

## Allen-Bradley PowerFlex Fault F063 — What It Means

Fault F063 (SW OverCurrent) on an Allen-Bradley PowerFlex drive indicates that the software-based overcurrent protection has tripped. Unlike the hardware overcurrent faults (F002, F004) which respond to instantaneous current peaks, F063 is a software-calculated overcurrent based on the drive's current limit monitoring over time. The drive detected that motor current exceeded the programmed current limit threshold and shut down to protect the motor and drive.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the driven equipment** — A pump, fan, or conveyor with a seized bearing, jammed mechanism, or higher than normal process load demands more current than the drive's software limit allows.
- **Current limit parameter set too low** — Parameter settings for current limit (typically P033 or equivalent) may be configured below the actual motor full-load amps, causing premature F063 trips under normal load.
- **Motor undersized for application** — If the motor was recently changed or the load increased, the motor may not be large enough and draws excessive current under normal conditions.
- **Excessive acceleration rate** — An acceleration time that is too short causes the drive to demand very high current to bring the load up to speed, tripping F063 before the motor reaches operating speed.

## Step-by-Step Fix {#fix}

1. **Check the fault queue** — Access the PowerFlex fault queue (parameter F-Que) to see the output current at the time of the F063 trip. Compare this to the motor nameplate full-load amps (FLA).
2. **Inspect the driven equipment for mechanical issues** — With the drive faulted, manually rotate the driven shaft or check the equipment for jammed components, seized bearings, or unusual resistance to rotation.
3. **Review current limit parameter settings** — Check P033 (Current Limit) and compare it to the motor nameplate FLA. The current limit should be set to 110–150% of motor FLA for most applications. Adjust if it was set too conservatively.
4. **Increase the acceleration time** — If the fault occurs only during startup, increase the accel time (P041 or equivalent) to allow more time for the load to reach speed. A longer ramp reduces peak current demand.
5. **Check drive output current vs. motor nameplate** — If the motor is genuinely overloaded during normal operation, the load must be reduced or the motor replaced with a larger frame.
6. **Verify motor connections** — Check for a phase-to-phase or phase-to-ground fault in the motor winding or output cable that could cause abnormally high current on one phase.
7. **Reset the fault** — Clear F063 via the keypad or a digital input configured as Fault Reset. Restart the drive and monitor output current during the acceleration and run phases.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-fault-f063&k=Motor+bearings&tag=errorcodefixes-20) \| Replace if driven equipment has a seized bearing causing overload |
| Motor (larger frame) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-fault-f063&k=Motor+%28larger+frame%29&tag=errorcodefixes-20) \| Required if motor is confirmed undersized for the application |
| PowerFlex control board | [Amazon](https://www.amazon.com/s?k=PowerFlex+control+board&tag=errorcodefixes-20) \| Only if fault persists with correct parameters and no mechanical cause |
## When to Call a Pro

If F063 persists after parameter correction and mechanical inspection, an Allen-Bradley-authorized technician should perform a full load study and drive sizing review to determine if the application is within the drive's rated capacity.

## Related Articles

- [Allen-Bradley MicroLogix 1400 Common Fault Codes](/posts/allen-bradley-micrologix-fault/)
- [Allen-Bradley PowerFlex 40 Complete Fault Code Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen Bradley PowerFlex 40 F2 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f2-fault/)
- [Allen-Bradley PowerFlex 40 F3 Fault — Power Loss](/posts/allen-bradley-powerflex-40-f3/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)

## See Also

- [Allen-Bradley PowerFlex F122 Fault — I/O Board Failure Fix](/posts/allen-bradley-powerflex-f122-fault/)
- [Allen-Bradley PowerFlex Fault F025 — Causes & Fix](/posts/allen-bradley-powerflex-fault-f025/)
- [Allen Bradley PowerFlex 753 F12 Fault — Causes & Fix](/posts/allen-bradley-powerflex-753-f12-fault/)
- [Allen Bradley PowerFlex 700 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-700-fault-7/)
