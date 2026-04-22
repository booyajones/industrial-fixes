---
title: "Sun Hydraulics Fault Codes — Complete Guide"
description: "Sun Hydraulics (Helios) electrohydraulic manifold and controller fault codes: causes, diagnostic steps, and repair guidance."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - sun-hydraulics
  - hydraulics
  - industrial
---

## Sun Hydraulics Fault Codes — Quick Reference

Sun Hydraulics (now Helios Technologies) manufactures screw-in hydraulic cartridge valves and Enovation Controls (Murphy) electronic systems for mobile and industrial hydraulics. Faults appear on MurphyLink displays or CAN bus diagnostics.

| Fault | Meaning | Quick Fix |
|-------|---------|-----------|
| Supply Voltage Low | Battery or supply below threshold | Check supply voltage at module |
| Supply Voltage High | Over-voltage on power input | Check alternator or power supply |
| Solenoid Open Circuit | Valve solenoid disconnected or failed | Check coil and wiring |
| Solenoid Short Circuit | Valve coil shorted | Replace coil |
| Sensor Signal Low | Pressure or position sensor below range | Check sensor supply and wiring |
| Sensor Signal High | Sensor above range | Check sensor and calibration |
| CAN Bus Fault | Communication lost on CAN network | Check CAN wiring and termination |
| Temperature High | Controller or oil temp exceeded | Check cooling, reduce duty cycle |
| Calibration Required | Setup procedure needed | Run calibration routine |
| Output Overcurrent | Output channel drawing too much current | Check load wiring |

## Most Common Faults

### Solenoid Open Circuit
The most common electrohydraulic fault on Sun/Helios systems. Vibration, moisture, and heat cycling cause solenoid connector failures. Check the DT or Deutsch connector pins before replacing the solenoid — bent or pushed-back pins are the leading cause of open circuit faults on mobile equipment.

### CAN Bus Fault
Sun Hydraulics controllers on CAN networks require proper 120-ohm termination resistors at both ends of the CAN bus. A missing or failed terminator causes intermittent or total communication loss. Measure CAN HI to CAN LO — you should read approximately 60 ohms (two 120-ohm resistors in parallel) with power off.

### Sensor Signal Low/High
Sun proportional hydraulic systems often use 0.5–4.5VDC ratiometric pressure sensors. A reference supply failure causes all sensors to read low simultaneously. Check the 5V sensor supply pin at the controller connector first before replacing sensors.

### Temperature High
In mobile equipment, hydraulic oil temperature control relies on adequate fan cooling of the reservoir and cooler. Check for air dam obstructions, bent cooler fins, or a failed thermostat that prevents the cooler from activating.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Deutsch DT connector pins | Most common fault location |
| Solenoid coil (12VDC or 24VDC) | Replace on short/open |
| Pressure transducer | Replace on signal fault |
| CAN bus termination resistor | 120 ohm |
| Murphy display module | Replace on screen or power faults |

## When to Call a Pro
Enovation/Murphy controller calibration for load-sensing systems and proportional valve flow tuning requires factory documentation. Incorrect calibration causes erratic machine motion.
