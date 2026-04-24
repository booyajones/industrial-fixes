---
title: "Industrial Control Panel Fault Troubleshooting Guide"
description: "How to troubleshoot industrial control panel faults: what common faults mean and how to diagnose and fix them."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
---

## Industrial Control Panel Faults ΓÇö How to Diagnose Them

Industrial control panels house PLCs, VFDs, relays, motor starters, and power distribution components. When a fault occurs, the panel's indicator lights, fault displays, and alarm outputs tell you what failed. This guide covers systematic diagnosis of the most common panel faults.

## Control Panel Fault Indicators

| Indicator | Meaning |
|-----------|---------|
| Power ON lamp off | No input power to panel ΓÇö check supply breaker |
| Run lamp off (should be on) | Motor or drive not running ΓÇö check fault log |
| Fault lamp on | Active fault ΓÇö check fault display or PLC fault log |
| E-stop lamp on | Emergency stop activated ΓÇö find and release |
| Overload lamp on | Motor thermal overload tripped ΓÇö check motor |
| Comm fault lamp on | Communication error ΓÇö check fieldbus cables |

## Most Common Control Panel Faults

### Power Supply Faults
**Symptom:** Panel dead, no indicator lights.
**Check:** Main supply breaker, incoming voltage (all phases), panel main disconnect. Measure voltage at the panel main terminals with a multimeter.

### VFD Faults
See brand-specific VFD fault guides. Common: OC (overcurrent), OV (overvoltage), OT (overtemp), GF (ground fault).

### Motor Starter / Contactor Faults
**Symptom:** Motor doesn't start, contactor doesn't pull in.
**Check:** Coil voltage (should match rated coil voltage when energized), contact condition, overload relay setting.

### PLC Faults
**Symptom:** Panel powered but no outputs energizing.
**Check:** PLC run LED (should be on), PLC fault LED (should be off), I/O module LEDs. Use programming software to read fault buffer.

### E-Stop Circuit Faults
**Symptom:** E-stop active but all buttons released.
**Check:** Safety relay input status, all E-stop buttons (twist and release), safety door switches, light curtain status.

## Systematic Fault Isolation

1. **Is there power?** Measure at the main terminals
2. **Is the E-stop clear?** Release all E-stops, verify safety relay is reset
3. **Is the PLC in RUN mode?** Check PLC status LED and fault buffer
4. **Is the drive/starter faulted?** Check drive display or fault output
5. **Is the motor overloaded?** Check overload relay trip indicator

## When to Call a Pro

High-voltage panel work (above 600V), arc flash hazard zones, and live panel troubleshooting require qualified electrical workers with proper PPE and training. Never open a live panel without appropriate arc flash protection.
