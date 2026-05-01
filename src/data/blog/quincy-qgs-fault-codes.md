---
title: "Quincy QGS Compressor Fault Codes: Complete Guide"
description: "Quincy QGS rotary screw compressor fault codes and diagnostics. Intellizone II fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - compressor
  - quincy
  - industrial
---

# Quincy QGS Compressor Fault Codes

Quincy QGS rotary screw compressors use the Intellizone II controller. Fault codes and messages display on the Intellizone panel LCD. The controller stores fault history with run hours and timestamps.

## QGS Fault Code Table

| Code/Message | Fault Description | Common Cause | Action |
|-------------|------------------|--------------|--------|
| HIGH TEMP | High discharge temperature | Dirty cooler, low oil, high ambient | Clean cooler, check oil |
| HIGH TEMP WARN | Temperature approaching limit | Pre-shutdown warning | Clean cooler immediately |
| MOTOR OVERLOAD | Motor thermal trip | Excessive current or load | Check motor amps and load |
| HIGH PRESSURE | System pressure too high | Excessive demand | Check pressure setting |
| LOW OIL PRESSURE | Oil pressure insufficient | Low oil or failed pump | Check oil level and pump |
| PHASE LOSS | Missing supply phase | Fuse or supply fault | Check input power |
| INLET RESTRICTION | Dirty inlet filter | Restricted air intake | Replace inlet filter |
| EMERGENCY STOP | E-stop active | E-stop circuit open | Check E-stop wiring |
| CHECK SEPARATOR | Separator element pressure drop high | Dirty separator | Replace separator element |
| SERVICE DUE | Maintenance interval reached | Hours elapsed | Perform scheduled PM |
| SENSOR FAULT | Failed temperature sensor | Open or shorted sensor | Replace thermistor |
| AUTO DRAIN FAULT | Condensate drain valve fault | Solenoid valve failure | Check drain valve |

## Most Common QGS Faults

### HIGH TEMP
Quincy QGS compressors have a high-temperature shutdown at typically 228°F (109°C). The most common cause is a dirty oil cooler or air aftercooler. Blow fins clean with low-pressure air. On larger QGS models, the cooler can be removed for power washing with degreaser.

### MOTOR OVERLOAD
Check that the motor overload relay is set correctly: current setting should be 100–105% of motor nameplate FLA. Verify three-phase voltage balance — more than 3% imbalance causes disproportionate current in one phase.

### CHECK SEPARATOR — Separator Element
When separator differential pressure exceeds design maximum (typically 10 PSI), this alarm triggers. The separator element is a wear item — replace at the scheduled interval (typically 4,000 hours). A clogged separator element increases discharge temperature and reduces compressor efficiency.

### AUTO DRAIN FAULT
Quincy QGS has an electronic auto-drain to remove condensate from the separator tank. If the solenoid valve fails (stuck closed = water in oil; stuck open = air loss), this fault triggers. Check solenoid valve coil resistance and verify 24 VAC at coil during drain cycle.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Inlet air filter | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?tag=errorcodefixes-20) \| Model-specific |
| Oil/separator element | [Amazon](https://www.amazon.com/s?k=Oil%2Fseparator+element&tag=errorcodefixes-20) \| Replace per service schedule |
| Quincy QGS oil | [Amazon](https://www.amazon.com/s?k=Quincy+QGS+oil&tag=errorcodefixes-20) \| Synthetic — match model specification |
| Auto-drain solenoid | [Amazon](https://www.amazon.com/s?k=Auto-drain+solenoid&tag=errorcodefixes-20) \| Check coil resistance |
| Temperature thermistor | [Amazon](https://www.amazon.com/s?k=Temperature+thermistor&tag=errorcodefixes-20) \| NTC type — check resistance vs. temp chart |
| Motor overload relay | [Amazon](https://www.amazon.com/s?k=Motor+overload+relay&tag=errorcodefixes-20) \| Match FLA setting |
> **Pro tip:** Quincy QGS Intellizone II logs the last 10 faults with run hours. Access via MENU ΓåÆ HISTORY ΓåÆ FAULT LOG on the panel. If HIGH TEMP faults are increasing in frequency, track the interval between faults — progressive reduction in time between faults indicates a degrading cooler before total failure.
