---
title: "Mazak Alarm 100 Spindle Alarm — Causes & Fix"
description: "What Mazak alarm 100 means, why a spindle alarm occurs, and how to diagnose and fix the spindle drive system."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - mazak
---

## Mazak Alarm 100 — What It Means

Alarm 100 on a Mazak CNC (Mazatrol T-, M-, or Fusion series) indicates a spindle alarm. The spindle drive detected a fault condition — this can encompass spindle drive overcurrent, overtemperature, encoder feedback loss, or a drive internal fault depending on the specific spindle drive model (Fanuc, Mitsubishi, or Mazak proprietary). Alarm 100 is always accompanied by a sub-alarm or spindle drive LED/code that identifies the specific spindle fault type.

[Jump to Fix](#fix)

## Common Causes

- **Spindle drive overtemperature** — The spindle drive or spindle motor has overheated due to inadequate cooling, high duty cycle, or blocked cooling fans.
- **Spindle motor overload** — Heavy cuts, a dull tool, or an incorrect cutting speed causes the spindle motor to draw excessive current and trip the drive overcurrent protection.
- **Spindle encoder fault** — The encoder on the spindle motor shaft has developed a fault (dirty, damaged, or loose), causing feedback errors that the drive interprets as a spindle alarm.
- **Spindle drive hardware failure** — An internal power module or control circuit fault in the spindle drive.

## Step-by-Step Fix {#fix}

1. **Record all active alarms** — On the Mazatrol display, navigate to the alarm screen and record alarm 100 along with any secondary alarms. The secondary alarm number identifies the specific spindle fault type.
2. **Check the spindle drive fault display** — Open the electrical cabinet and locate the spindle drive (Fanuc red or Mitsubishi drive, or Mazak proprietary). The drive will have a LED display or indicator showing a sub-fault code. Record this code and look it up in the drive service manual.
3. **Power cycle the machine** — Turn the machine off completely (main disconnect), wait 2 minutes, and power back on. Many transient spindle alarms caused by brief overloads or power glitches will clear on restart.
4. **Allow cooling time if overtemperature** — If the spindle drive or motor is hot to the touch, allow 20–30 minutes of cooling before restarting. Check that the spindle drive cooling fan and motor cooling fan are running.
5. **Inspect the cutting conditions** — If the alarm occurred during a cut, review the program for excessive spindle load: very high feed rates, incorrect speed for material, or a tool that is dull or broken.
6. **Check the spindle encoder** — With power off, inspect the encoder connector at the spindle motor for loose or corroded pins. If the drive shows an encoder-related sub-fault, measure the encoder cable for continuity.
7. **Contact Mazak service** — For alarm 100 with a spindle drive hardware sub-fault that does not clear after cooling and power cycling, contact Mazak service or a Mazak-authorized service center.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle drive cooling fan | [Amazon](https://www.amazon.com/s?k=Spindle+drive+cooling+fan&tag=errorcodefixes-20) \| Replace if fan is seized or running slowly |
| Spindle motor encoder | [Amazon](https://www.amazon.com/s?k=Spindle+motor+encoder&tag=errorcodefixes-20) \| Replace if encoder feedback is confirmed faulty |
| Spindle drive module | [Amazon](https://www.amazon.com/s?k=Spindle+drive+module&tag=errorcodefixes-20) \| Contact Mazak service for correct replacement part |
| Spindle motor | [Amazon](https://www.amazon.com/s?k=Spindle+motor&tag=errorcodefixes-20) \| Replace if windings are confirmed damaged |
## When to Call a Pro

Spindle drive replacement, spindle motor testing, and encoder calibration require specialized equipment and Mazak machine knowledge. Contact a Mazak Factory Service Representative or authorized service center for hardware faults that do not resolve with cooling and power cycling.
