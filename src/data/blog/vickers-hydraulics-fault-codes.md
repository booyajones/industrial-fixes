---
title: "Vickers Hydraulics Fault Codes - Complete Guide"
description: "Vickers (Eaton) hydraulic system fault codes for proportional valves and hydraulic power units: causes, diagnostic steps, and parts."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vickers
  - eaton
  - hydraulics
  - industrial
---

## Vickers Hydraulics Fault Codes - Quick Reference

Vickers (now Eaton Hydraulics) proportional valve amplifiers and HPU controls display fault conditions via LED indicators and digital outputs. Common systems include the EEA-PAM amplifiers and CVCS valve controls.

| [Fault / Indicator](https://www.amazon.com/s?k=Fault%20%2F%20Indicator&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------------ |---------|-----------|
| Red LED - No Enable | [Enable input not active](https://www.amazon.com/s?k=Enable%20input%20not%20active&tag=errorcodefixe-20) | Check enable wiring from PLC |
| [Red LED - Solenoid Fault](https://www.amazon.com/s?k=Red%20LED%20-%20Solenoid%20Fault&tag=errorcodefixe-20) | Valve coil short or open | Measure coil resistance | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Amber LED - Power Fault | Supply voltage out of range | [Check 24VDC supply](https://www.amazon.com/s?k=Check%2024VDC%20supply&tag=errorcodefixe-20) |  | Ramp Fault | [Ramp generator error](https://www.amazon.com/s?k=Ramp%20generator%20error&tag=errorcodefixe-20) | Check command signal |
| [HPU: Low Oil Level](https://www.amazon.com/s?k=HPU%3A%20Low%20Oil%20Level&tag=errorcodefixe-20) | Reservoir below minimum | Add hydraulic oil | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | HPU: High Temperature | Oil temperature limit exceeded | [Check oil cooler](https://www.amazon.com/s?k=Check%20oil%20cooler&tag=errorcodefixe-20) |  | HPU: Filter Bypass | [Filter DP exceeded bypass pressure](https://www.amazon.com/s?k=Filter%20DP%20exceeded%20bypass%20pressure&tag=errorcodefixe-20) | Replace filter element |
| [HPU: Motor Overload](https://www.amazon.com/s?k=HPU%3A%20Motor%20Overload&tag=errorcodefixe-20) | Pump motor overcurrent | Check motor amps and voltage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure Sensor Fault | Sensor signal out of range | [Check sensor wiring](https://www.amazon.com/s?k=Check%20sensor%20wiring&tag=errorcodefixe-20) |  | System Pressure Low | [HPU not reaching system pressure](https://www.amazon.com/s?k=HPU%20not%20reaching%20system%20pressure&tag=errorcodefixe-20) | Check pump, relief valve |

## Most Common Faults

### Solenoid Fault
Vickers EEA amplifier cards monitor solenoid current in real time. A coil resistance below approximately 4 ohms or above 100 ohms (model dependent) triggers a solenoid fault. Always measure the coil at the amplifier output terminals - this tests both the coil and the wiring harness.

### Enable Fault
Many older Vickers HPUs require a 24VDC signal on the enable input to allow the amplifier to energize outputs. A failed PLC output, blown fuse, or broken wire in the enable circuit causes this. Verify 24V at pin 1 (or as labeled on your specific amplifier card).

### HPU Filter Bypass
Vickers specifies Beta ratios for hydraulic filters - once the element reaches its rated collapse pressure, the bypass opens. Running contaminated oil destroys pump and valve spools rapidly. Pull an oil sample after any bypass event and check for metal particles.

### High Oil Temperature
Verify cooler oil flow - a thermostatic bypass valve that sticks open causes hot oil to bypass the cooler entirely. These valves are often serviceable without draining the system.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Hydraulic filter element](https://www.amazon.com/s?k=Hydraulic%20filter%20element&tag=errorcodefixe-20) | Replace on bypass fault |
| [Proportional solenoid coil](https://www.amazon.com/s?k=Proportional%20solenoid%20coil&tag=errorcodefixe-20) | Replace on coil fault |
| [Vickers EEA amplifier card](https://www.amazon.com/s?k=Vickers%20EEA%20amplifier%20card&tag=errorcodefixe-20) | Replace on electronics failure |
| [Thermostatic bypass valve](https://www.amazon.com/s?k=Thermostatic%20bypass%20valve&tag=errorcodefixe-20) | Common on high-temp faults |
| [Pressure transducer](https://www.amazon.com/s?k=Pressure%20transducer&tag=errorcodefixe-20) | Replace on sensor fault |

## When to Call a Pro
Vickers servo proportional valve null adjustment and amplifier tuning requires factory procedures. Mis-adjusted valves cause cylinder drift and loss of position control.

