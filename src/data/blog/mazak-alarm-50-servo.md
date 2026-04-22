---
title: "Mazak Alarm 50 Servo — Causes & Fix"
description: "What Mazak CNC alarm 50 servo drive fault means, how to diagnose it, and how to fix it."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - mazak
---

## Mazak Alarm 50 Servo — What It Means

Alarm 50 on a Mazak CNC (Mazatrol T32, M32, Fusion 640, Matrix, Smooth controls) indicates a servo drive fault. Mazak machines use Mitsubishi MDS series servo amplifiers on older models and Mazak/Mitsubishi integrated amplifiers on newer Smooth-series machines. Alarm 50 is generated when the servo amplifier for one or more axes reports an internal fault — the specific axis and sub-fault code are displayed in the alarm detail page or on the servo amplifier's LED display.

[Jump to Fix](#fix)

## Common Causes

- **Axis overcurrent** — A mechanical load event (crash, seized bearing, tight way cover) caused the servo motor to draw current above the drive's overcurrent limit.
- **Servo amplifier overtemperature** — Inadequate cabinet cooling or a failed cooling fan causes the amplifier heatsink to exceed the thermal trip point.
- **Encoder fault** — A failed pulse encoder on the servo motor causes the amplifier to lose position feedback, triggering the alarm. Mazak systems typically use Mitsubishi OSA series absolute encoders.
- **DC bus overvoltage** — Rapid deceleration of a high-inertia axis (rotary table, large spindle) without an adequate regenerative resistor causes the DC bus to rise above the overvoltage trip threshold.

## Step-by-Step Fix {#fix}

1. **Read the alarm detail** — On the Mazatrol control, navigate to the alarm list and note the axis identifier and any sub-alarm codes. On the servo amplifier LED display (visible through the cabinet window or with cabinet open), read the 2-character fault code.
2. **Power cycle with E-stop** — For transient faults (temporary overcurrent from chip-in-way, vibration), a full power-off/power-on cycle (main power, not just NC power) may clear the alarm.
3. **Inspect the faulted axis for mechanical issues** — If the alarm occurred during a cut, inspect the axis for crashed tooling, chips under way covers, or tight way wipers. Clear any obstruction.
4. **Check cabinet cooling** — Confirm the servo drive cooling fans are running and heatsinks are clean. Mazak electrical cabinets have door-mounted fans — check filter mats for blockage.
5. **Check encoder battery (absolute systems)** — Mazak machines with absolute encoders use a backup battery. A low battery causes position errors that can appear as servo faults. Check the battery voltage at the encoder connector (should be 3.6V lithium).

## Parts Often Needed

| Part | Notes |
|------|-------|
| [MDS servo amplifier](https://www.amazon.com/s?k=MDS%20servo%20amplifier&tag=errorcodefixe-20) | Mitsubishi MDS-B, MDS-C1, or MDS-D series depending on control vintage |
| [OSA absolute encoder](https://www.amazon.com/s?k=OSA%20absolute%20encoder&tag=errorcodefixe-20) | Mitsubishi OEM; requires reference point recovery after replacement |
| [Encoder backup battery](https://www.amazon.com/s?k=Encoder%20backup%20battery&tag=errorcodefixe-20) | 3.6V lithium; replace every 3–5 years |
| [Cabinet cooling fan](https://www.amazon.com/s?k=Cabinet%20cooling%20fan&tag=errorcodefixe-20) | Match electrical cabinet specifications |

## When to Call a Pro

Mazak servo system repair — especially on Smooth-series machines — requires Mazak-authorized service. Incorrect amplifier parameters or encoder setup after component replacement causes axis runaway or positioning errors that scrap parts and can damage the machine.
