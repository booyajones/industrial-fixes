---
title: "Siemens G120 F0005 Fault - Causes & Fix"
description: "F0005 on a Siemens G120 VFD means motor overtemperature from thermal overload (I²t trip). Most often fixed by correcting load or motor data."
pubDatetime: 2026-06-02T10:27:48Z
modDatetime: 2026-06-02T10:27:48Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Motor with correct horsepower and frame size"
most_likely_cause: "Mechanical overload on the driven machine"
---

## What this code means
F0005 on the Siemens G120 VFD indicates that the drive's thermal model has detected motor overtemperature through I²t monitoring. This means the accumulated thermal stress in the motor has exceeded the safe threshold, usually from sustained high current draw. The drive calculates heat buildup based on the motor parameters you programmed and the actual load current it measures. When the calculated temperature crosses the limit, the drive trips to protect the motor from damage.

This fault is not a supply voltage problem or a momentary overload spike. It reflects a true thermal accumulation over time, so the root cause is almost always either a real mechanical overload on the driven equipment or incorrect motor nameplate data entered in the drive parameters. Correcting the underlying issue and verifying motor parameters will resolve the fault.

## Common Causes

- **Mechanical overload on the driven machine** Jammed load, binding bearings, misaligned coupling, excessive friction, or higher-than-expected process demand forces the motor to draw sustained high current and overheat.
- **Incorrect motor nameplate data in drive parameters** Wrong rated current, voltage, power, speed, or frequency programmed into the VFD causes the thermal model to calculate incorrectly and trip prematurely.
- **Repeated starts and stops or long acceleration under load** Frequent cycling or slow ramp-up while fighting load keeps motor current high for extended periods, building up I²t thermal accumulation faster than the motor can cool.
- **Poor motor cooling or high ambient temperature** Blocked motor fan, clogged ventilation, obstructed cabinet airflow, or elevated ambient conditions prevent heat dissipation and push the motor into overtemperature even under normal load.
- **Motor or output cable damage** Shorted turns in the motor windings, damaged cable insulation, partial phase faults, or loose connections increase current draw and trigger the thermal protection.

## Step-by-Step Fix {#fix}

1. **Record the fault details** from the G120 operator panel (BOP/IOP) or commissioning tool before resetting, noting the exact fault text, motor current, and operating state at the time of trip.
2. **Verify motor nameplate parameters** in the drive's motor data settings (P0304–P0311) and confirm they exactly match the actual motor's rated current, voltage, frequency, speed, and power rating.
3. **Inspect the driven load mechanically** by disconnecting the machine if possible and checking for jammed bearings, misaligned couplings, tight belts, binding gearbox, seized pump, or any other excessive mechanical resistance.
4. **Measure three-phase motor current** during normal operation using a clamp meter and compare the values to the motor's full-load amperage (FLA) on the nameplate and the drive's rated output current to identify sustained overload.
5. **Check motor and output cable condition** by testing insulation resistance (megohm test) on each phase to ground and phase-to-phase, inspecting terminals for loose or corroded connections, and looking for visible cable damage or shorts.
6. **Verify motor cooling and ambient conditions** by confirming the motor cooling fan is running, air vents are clear, cabinet ventilation is adequate, and ambient temperature is within the motor and drive operating range.
7. **Clear the fault** in the drive menu (Fault Reset), restart the motor under normal load, and monitor running current and thermal accumulation over several cycles to confirm the issue is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor with correct horsepower and frame size | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0005-fault-code&k=Motor+with+correct+horsepower+and+frame+size&tag=errorcodefixes-20) \| Replace if undersized for the load or if winding insulation has failed and cannot be economically repaired. |
| Shielded VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0005-fault-code&k=Shielded+VFD-rated+motor+cable&tag=errorcodefixes-20) \| Replace if insulation is damaged, cable is undersized for actual motor FLA, or if shield continuity is broken. |

## When to Call a Pro

Call a qualified drives technician or electrical contractor if the fault returns immediately after clearing even with correct motor parameters and no obvious mechanical load problem, if you measure significantly unbalanced motor currents across the three phases, or if you suspect internal drive hardware failure. Also call a professional if you are not trained to perform insulation resistance testing on motor windings, work inside energized VFD cabinets, or safely lock-out and inspect industrial machinery. Persistent F0005 faults despite correct data and normal mechanical conditions may indicate a failing motor, damaged output stage in the drive, or a sensor fault that requires factory-trained service.
