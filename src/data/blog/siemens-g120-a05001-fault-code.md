---
title: "Siemens G120 A05001 Current Limit - Causes & Fix"
description: "Siemens G120 A05001 alarm means current limit reached. Learn causes like motor mismatch, long leads, earth faults, and fix steps."
pubDatetime: 2026-05-28T09:04:23Z
modDatetime: 2026-05-28T09:04:23Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Shielded motor cable"
most_likely_cause: "Motor power does not match inverter power"
---

## Siemens G120 A05001 Current Limit — What It Means

The A05001 code on a Siemens SINAMICS G120 drive is an alarm, not a fault trip. It indicates the drive has reached its current limit while attempting to accelerate, hold torque, or run under load. The drive continues to operate but is signaling that it is working at maximum current capacity. No acknowledgment is required, but the alarm warns you that the system is under stress and may not deliver full performance or could transition to a fault if the condition worsens.

This alarm typically appears when the motor is demanding more current than the inverter can safely supply. Common scenarios include starting a heavy load, a motor that is too large for the drive, excessively long motor cables causing voltage drop, or a ground fault in the motor circuit. If the alarm is displayed permanently, the drive input voltage and motor circuit should be checked immediately.

[Jump to Fix](#fix)

## Common Causes

- **Motor power does not match inverter power** A motor rated higher than the drive's output capacity will pull more current than the inverter can deliver, triggering the current limit alarm during acceleration or under load.
- **Motor leads are too long** Excessive cable length between the drive and motor causes voltage drop and requires the drive to compensate with higher current, pushing it to the limit.
- **Earth fault in motor or cable** A ground fault in the motor windings or cable insulation creates a current leakage path that increases total current draw and trips the limit.
- **Input voltage too low or unstable** Low or fluctuating supply voltage forces the drive to draw higher current to maintain motor performance, reaching the current limit threshold.
- **Motor overload or mechanical binding** A jammed load, bearing failure, or other mechanical obstruction forces the motor to draw excessive current to maintain rotation.

## Step-by-Step Fix {#fix}

1. **Verify whether the alarm is persistent or intermittent.** Note if it appears only during startup, acceleration, or under full load, or if it is displayed continuously.
2. **Check that the motor nameplate rating matches the drive output rating.** Confirm the motor horsepower and current rating are within the drive's specified capacity, and consult your model's power table if needed.
3. **Measure the motor cable length and inspect routing.** If the cable run exceeds manufacturer recommendations for your drive model, consider installing a reactor or reducing cable length.
4. **Perform an insulation resistance test on the motor and cable.** Use a megohmmeter to check for earth faults between motor windings and ground, and repair or replace any damaged cable or motor.
5. **Measure the drive input voltage at the power terminals.** Confirm it is within the rated range and stable during operation, and correct any supply issues before continuing.
6. **Inspect the motor and driven load for mechanical issues.** Rotate the motor shaft by hand with power off to check for binding, bearing noise, or excessive drag, and repair any mechanical faults.
7. **Review drive parameter settings for current limits and acceleration ramps.** Adjust p1080 (maximum motor current) and p1120 (ramp-up time) if factory defaults are too aggressive for your application, and reset the alarm after changes.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Shielded motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05001-fault-code&k=Shielded+motor+cable&tag=errorcodefixes-20) \| Replace if length is excessive or insulation is damaged, use manufacturer-approved cable for VFD applications. |
| Line reactor or choke | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05001-fault-code&k=Line+reactor+or+choke&tag=errorcodefixes-20) \| Install on input or output side if cable length or voltage drop is unavoidable, consult drive manual for sizing. |
| Motor bearings | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a05001-fault-code&k=Motor+bearings&tag=errorcodefixes-20) \| Replace if mechanical binding or noise is detected during manual rotation or operation. |

## When to Call a Pro

Call a qualified electrician or drive technician if the alarm persists after verifying motor and cable match, correcting input voltage, and eliminating mechanical faults. If insulation testing reveals a ground fault you cannot trace, or if adjusting parameters does not resolve the alarm, professional diagnostic tools and experience are needed. Also contact Siemens support or a certified service center if you suspect the drive itself is mis-rated for your application or if internal current sensing hardware may be damaged.

## See Also

- [Siemens G120 A01028 - Causes & Fix](/posts/siemens-g120-a01028-fault-code/)
- [Siemens G120 F01611 - Causes & Fix](/posts/siemens-g120-f01611-fault-code/)
- [Siemens Sinumerik Alarm 380600 — Encoder Fault](/posts/siemens-sinumerik-alarm-380600/)
- [Siemens G120 F30002 - Causes & Fix](/posts/siemens-g120-f30002-fault-code/)
