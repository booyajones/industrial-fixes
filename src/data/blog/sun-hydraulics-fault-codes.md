---
title: "Sun Hydraulics Fault Codes - Complete Guide"
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

## Sun Hydraulics Fault Codes - Quick Reference

Sun Hydraulics (now Helios Technologies) manufactures screw-in hydraulic cartridge valves and Enovation Controls (Murphy) electronic systems for mobile and industrial hydraulics. Faults appear on MurphyLink displays or CAN bus diagnostics.

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------- |---------|-----------|
| Supply Voltage Low | [Battery or supply below threshold](https://www.amazon.com/s?k=Battery%20or%20supply%20below%20threshold&tag=errorcodefixe-20) | Check supply voltage at module |
| [Supply Voltage High](https://www.amazon.com/s?k=Supply%20Voltage%20High&tag=errorcodefixe-20) | Over-voltage on power input | Check alternator or power supply | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Solenoid Open Circuit | Valve solenoid disconnected or failed | [Check coil and wiring](https://www.amazon.com/s?k=Check%20coil%20and%20wiring&tag=errorcodefixe-20) |  | Solenoid Short Circuit | [Valve coil shorted](https://www.amazon.com/s?k=Valve%20coil%20shorted&tag=errorcodefixe-20) | Replace coil |
| [Sensor Signal Low](https://www.amazon.com/s?k=Sensor%20Signal%20Low&tag=errorcodefixe-20) | Pressure or position sensor below range | Check sensor supply and wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Sensor Signal High | Sensor above range | [Check sensor and calibration](https://www.amazon.com/s?k=Check%20sensor%20and%20calibration&tag=errorcodefixe-20) |  | CAN Bus Fault | [Communication lost on CAN network](https://www.amazon.com/s?k=Communication%20lost%20on%20CAN%20network&tag=errorcodefixe-20) | Check CAN wiring and termination |
| [Temperature High](https://www.amazon.com/s?k=Temperature%20High&tag=errorcodefixe-20) | Controller or oil temp exceeded | Check cooling, reduce duty cycle | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Calibration Required | Setup procedure needed | [Run calibration routine](https://www.amazon.com/s?k=Run%20calibration%20routine&tag=errorcodefixe-20) |  | Output Overcurrent | [Output channel drawing too much current](https://www.amazon.com/s?k=Output%20channel%20drawing%20too%20much%20current&tag=errorcodefixe-20) | Check load wiring |

## Most Common Faults

### Solenoid Open Circuit
The most common electrohydraulic fault on Sun/Helios systems. Vibration, moisture, and heat cycling cause solenoid connector failures. Check the DT or Deutsch connector pins before replacing the solenoid - bent or pushed-back pins are the leading cause of open circuit faults on mobile equipment.

### CAN Bus Fault
Sun Hydraulics controllers on CAN networks require proper 120-ohm termination resistors at both ends of the CAN bus. A missing or failed terminator causes intermittent or total communication loss. Measure CAN HI to CAN LO - you should read approximately 60 ohms (two 120-ohm resistors in parallel) with power off.

### Sensor Signal Low/High
Sun proportional hydraulic systems often use 0.5–4.5VDC ratiometric pressure sensors. A reference supply failure causes all sensors to read low simultaneously. Check the 5V sensor supply pin at the controller connector first before replacing sensors.

### Temperature High
In mobile equipment, hydraulic oil temperature control relies on adequate fan cooling of the reservoir and cooler. Check for air dam obstructions, bent cooler fins, or a failed thermostat that prevents the cooler from activating.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Deutsch DT connector pins](https://www.amazon.com/s?k=Deutsch%20DT%20connector%20pins&tag=errorcodefixe-20) | Most common fault location |
| [Solenoid coil (12VDC or 24VDC)](https://www.amazon.com/s?k=Solenoid%20coil%20(12VDC%20or%2024VDC)&tag=errorcodefixe-20) | Replace on short/open |
| [Pressure transducer](https://www.amazon.com/s?k=Pressure%20transducer&tag=errorcodefixe-20) | Replace on signal fault |
| [CAN bus termination resistor](https://www.amazon.com/s?k=CAN%20bus%20termination%20resistor&tag=errorcodefixe-20) | 120 ohm |
| [Murphy display module](https://www.amazon.com/s?k=Murphy%20display%20module&tag=errorcodefixe-20) | Replace on screen or power faults |

## When to Call a Pro
Enovation/Murphy controller calibration for load-sensing systems and proportional valve flow tuning requires factory documentation. Incorrect calibration causes erratic machine motion.

