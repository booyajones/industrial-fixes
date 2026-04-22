---
title: "Siemens Sinumerik Alarm 380600 — Encoder Fault"
description: "What Siemens Sinumerik alarm 380600 means, why an encoder fault occurs, and how to diagnose and fix it."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - siemens
---

## Siemens Sinumerik Alarm 380600 — What It Means

Siemens Sinumerik alarm 380600 indicates an encoder fault on a servo axis. The format is typically displayed as "380600 [Axis] Encoder 1 fault: signal level too low." This means the SINAMICS drive detected that the encoder signal amplitude has fallen below the minimum required level, which can occur due to encoder hardware failure, cable damage, contamination of the encoder read head, or loss of power to the encoder.

[Jump to Fix](#fix)

## Common Causes

- **Damaged encoder cable** — The encoder feedback cable has been cut, pinched, or has developed a broken conductor from repeated flexing during axis travel.
- **Encoder read head contamination** — On linear encoders (Heidenhain, Renishaw), coolant, chips, or oil contamination on the scale or read head reduces signal amplitude below the fault threshold.
- **Failed encoder** — The rotary encoder on the servo motor shaft or the linear scale has failed internally. Signal amplitude drops to zero or fluctuates erratically.
- **Encoder power supply fault** — The 5V or 24V supply from the SINAMICS drive to the encoder is low or absent, causing the encoder to output a weak or absent signal.

## Step-by-Step Fix {#fix}

1. **Identify the faulted axis** — The alarm text includes the axis name (X, Y, Z, etc.). Navigate to the Sinumerik diagnostic screen to confirm which axis is reporting alarm 380600.
2. **Inspect the encoder cable** — Trace the encoder feedback cable from the motor to the SINAMICS drive. Look for pinch points at cable carriers, sharp bends, or areas where the cable is exposed to coolant or chips. Flex the cable by hand along its length while observing if the alarm clears momentarily (indicating an intermittent break).
3. **Check the encoder connector at the drive** — At the SINAMICS module, unplug and re-seat the encoder feedback connector (typically an SMC or DRIVE-CLiQ connector). Check for bent or pushed-out pins.
4. **Inspect the linear scale and read head** — For linear encoders, clean the scale with isopropyl alcohol and a lint-free cloth. Inspect the read head mounting for alignment issues or physical damage.
5. **Measure encoder supply voltage** — Use a multimeter at the encoder connector to verify the encoder supply voltage (5V or 24V depending on encoder type) is within specification.
6. **Replace the encoder cable** — If a broken conductor is confirmed or suspected, replace the encoder feedback cable with an equivalent shielded cable of the same type and length.
7. **Replace the encoder** — If the cable and supply voltage are confirmed good but the alarm persists, the encoder itself has failed. Replace with the same model encoder.
8. **Reset the alarm** — After hardware correction, reset alarm 380600 via the Sinumerik control panel Reset button. Verify the axis homes correctly and operates without fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Encoder feedback cable](https://www.amazon.com/s?k=Encoder%20feedback%20cable&tag=errorcodefixe-20) | Must be shielded; match connector type to drive interface |
| [Rotary encoder (motor-mounted)](https://www.amazon.com/s?k=Rotary%20encoder%20(motor-mounted)&tag=errorcodefixe-20) | Match to servo motor model and Sinumerik interface type |
| [Linear scale read head](https://www.amazon.com/s?k=Linear%20scale%20read%20head&tag=errorcodefixe-20) | OEM replacement for Heidenhain/Renishaw scale |
| [DRIVE-CLiQ cable](https://www.amazon.com/s?k=DRIVE-CLiQ%20cable&tag=errorcodefixe-20) | For newer SINAMICS drives with DRIVE-CLiQ encoder interface |

## When to Call a Pro

Encoder replacement on servo motors and linear scale alignment require precision work. A Siemens-authorized service technician should perform encoder replacement and recalibrate the drive parameters (encoder resolution, direction, offset) to avoid positioning errors.
