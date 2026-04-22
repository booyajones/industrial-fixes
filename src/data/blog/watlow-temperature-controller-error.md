---
title: "Watlow Temperature Controller Error Codes — Guide"
description: "Watlow temperature controller error codes: what each means and how to fix it."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - watlow
---

## Watlow Temperature Controller Error Codes — What They Mean

Watlow temperature controllers (F4T, EZ-ZONE, Series 96, and PM series) are industrial-grade controllers used in heat treat, plastic processing, packaging, and laboratory equipment. They display fault codes when sensor or process problems occur.

| Code | Meaning |
|------|---------|
| OPn | Open input — sensor is open circuit |
| Shrt | Short input — sensor leads are shorted |
| Err 1 | A/D conversion error (internal) |
| OvRng | Over range — temperature exceeds sensor maximum |
| UnRng | Under range — temperature below sensor minimum |
| HI | High temperature process alarm |
| Lo | Low temperature process alarm |
| OuT | Output alarm |

[Jump to Fix](#fix)

## Most Common Watlow Controller Errors and Fixes {#fix}

### OPn — Open Input
The thermocouple or RTD is disconnected or has broken wire. Test sensor continuity. Check all screw terminal connections — Watlow terminals must be properly torqued. A loose terminal causes OPn intermittently.

### Shrt — Short Input
Sensor leads are touching (shorted together or to thermocouple sheath). Inspect the sensor lead insulation for damage near hot zones.

### OvRng / UnRng — Range Error
Most common cause: wrong sensor type selected in controller setup. If the controller is configured for Type K but a Type J thermocouple is connected, readings appear in OvRng or UnRng at normal temperatures. Verify sensor type in the controller's input menu.

### HI / Lo Alarms
Verify process is within expected temperature range. Check that alarm setpoints are configured correctly for the application. A HI alarm on startup usually means the setpoint was set below ambient.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermocouple | Match type to controller input (Type K, J, N, T, etc.) |
| RTD (PT100 or PT1000) | Match controller configuration |
| Watlow replacement controller | If Err 1 indicates internal ADC failure |

## When to Call a Pro

Err 1 internal errors and EtherNet/IP or DeviceNet communication faults require Watlow technical support for firmware and hardware diagnosis.
