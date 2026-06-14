---
title: "Yaskawa GA800 E35 Fault - Causes & Fix"
description: "E35 on Yaskawa GA800 VFDs indicates an overspeed fault. Most often fixed by adjusting speed-loop tuning or correcting encoder scaling."
pubDatetime: 2026-06-05T10:04:19Z
modDatetime: 2026-06-05T10:04:19Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
money_part: "Encoder or pulse generator"
most_likely_cause: "Aggressive speed-loop tuning"
---

## Yaskawa GA800 E35 Fault — What It Means

The E35 fault on a Yaskawa GA800 variable frequency drive signals that the motor speed has exceeded the configured overspeed detection threshold. This fault can occur during acceleration, deceleration, or steady-state operation. The drive monitors motor speed continuously and trips if the actual speed rises above the allowed limit, protecting the motor and connected equipment from runaway conditions. The fault is typically caused by incorrect tuning, encoder feedback scaling issues, or overspeed detection settings that are too aggressive rather than a physical drive failure.

[Jump to Fix](#fix)

## Common Causes

- **Aggressive speed-loop tuning** High proportional gain or short integral time in the speed controller (ASR) causes overshoot during acceleration or load changes, briefly pushing motor speed above the overspeed threshold.
- **Incorrect encoder or pulse-train scaling** The drive interprets feedback pulses incorrectly if the pulse-per-revolution count or frequency scaling does not match the actual encoder or pulse generator, making the drive think the motor is running faster than it actually is.
- **Overspeed detection level set too low** The overspeed trip threshold or detection delay time is configured too tightly, causing the drive to fault on normal speed variations or transient overshoot.
- **High-frequency injection gain too high in PM motor control** When using permanent-magnet motor control with high-frequency injection for low-speed sensorless operation, excessive HFI proportional gain can destabilize speed estimation and trigger false overspeed faults at startup or low speed.
- **Incomplete or incorrect motor auto-tuning** Permanent-magnet motors require accurate parameter identification, and if auto-tuning was skipped or failed, the drive's internal motor model does not match the real motor, leading to speed-control instability and overspeed trips.

## Step-by-Step Fix {#fix}

1. **Verify the fault code and motor speed** by checking the keypad display to confirm E35 is present, and note whether the fault occurred during startup, acceleration, or running speed to help isolate the cause.
2. **Review speed-loop tuning parameters** and reduce C5-01 (ASR Proportional Gain 1) or increase C5-02 (ASR Integral Time 1) in small increments if overshoot is suspected, starting with a 10-20% adjustment to reduce aggressive response.
3. **Check encoder and pulse-train scaling** by verifying parameters H6-02 through H6-05, setting H6-02 to match the pulse-train frequency at 100% speed reference, and confirming the encoder pulse-per-revolution count matches the installed feedback device.
4. **Adjust overspeed detection settings** by reviewing F1-08 (Overspeed Detection Level) and F1-09 (Overspeed Detection Delay Time), raising the detection level or lengthening the delay if the motor does not actually exceed safe speed and the trips are nuisance faults.
5. **Verify PM motor parameters and auto-tune** if using permanent-magnet motor control, running the drive's auto-tune sequence if not already done, and reducing n8-41 (HFI P Gain) in small steps if faults occur at low speed with n8-57 set to 1.
6. **Clear the fault and reset the drive** by pressing the RESET button on the keypad once all parameter corrections are made and the root cause is addressed, not before.
7. **Test run the drive** under normal load conditions to confirm the overspeed fault does not reappear, monitoring speed feedback and verifying stable operation through the full speed range before returning the system to service.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder or pulse generator | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e35-fault-code&k=Encoder+or+pulse+generator&tag=errorcodefixes-20) \| Replace if feedback scaling is correct but signal integrity is poor or the device is damaged. |
| Encoder feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e35-fault-code&k=Encoder+feedback+cable&tag=errorcodefixes-20) \| Check for shielding breaks, pinched wires, or poor connections that can corrupt speed feedback and cause false overspeed detection. |

## When to Call a Pro

Call a qualified drive technician or controls integrator if you are not familiar with VFD parameter programming, if the overspeed fault persists after tuning and encoder checks, or if the motor or feedback device requires replacement or recalibration. Professional support is also recommended for permanent-magnet motor commissioning, as auto-tuning and high-frequency injection setup require specialized knowledge to avoid instability and protect the motor. If the fault appears alongside other alarms or the drive shows signs of hardware damage, a technician with Yaskawa-specific training and diagnostic tools should inspect the unit.
