---
title: "Vickers Hydraulics Fault Codes - Complete Guide"
description: "Vickers (Eaton) hydraulic system fault codes for proportional valves and hydraulic power units: causes, diagnostic steps, and parts."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Dana Kowalski"
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

| Fault / Indicator | Meaning | Quick Fix |
|------------------|---------|-----------|
| Red LED - No Enable | Enable input not active | Check enable wiring from PLC |
| Red LED - Solenoid Fault | Valve coil short or open | Measure coil resistance |
| Amber LED - Power Fault | Supply voltage out of range | Check 24VDC supply |
| Ramp Fault | Ramp generator error | Check command signal |
| HPU: Low Oil Level | Reservoir below minimum | Add hydraulic oil |
| HPU: High Temperature | Oil temperature limit exceeded | Check oil cooler |
| HPU: Filter Bypass | Filter DP exceeded bypass pressure | Replace filter element |
| HPU: Motor Overload | Pump motor overcurrent | Check motor amps and voltage |
| Pressure Sensor Fault | Sensor signal out of range | Check sensor wiring |
| System Pressure Low | HPU not reaching system pressure | Check pump, relief valve |

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
| Hydraulic filter element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vickers-hydraulics-fault-codes&k=Hydraulic+filter+element&tag=errorcodefixes-20) \| Replace on bypass fault |
| Proportional solenoid coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vickers-hydraulics-fault-codes&k=Proportional+solenoid+coil&tag=errorcodefixes-20) \| Replace on coil fault |
| Vickers EEA amplifier card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vickers-hydraulics-fault-codes&k=Vickers+EEA+amplifier+card&tag=errorcodefixes-20) \| Replace on electronics failure |
| Thermostatic bypass valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vickers-hydraulics-fault-codes&k=Thermostatic+bypass+valve&tag=errorcodefixes-20) \| Common on high-temp faults |
| Pressure transducer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-vickers-hydraulics-fault-codes&k=Pressure+transducer&tag=errorcodefixes-20) \| Replace on sensor fault |
## When to Call a Pro
Vickers servo proportional valve null adjustment and amplifier tuning requires factory procedures. Mis-adjusted valves cause cylinder drift and loss of position control.

