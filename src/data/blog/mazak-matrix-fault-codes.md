---
title: "Mazak Matrix/Matrix 2 Fault Code Guide — Complete Reference"
description: "Mazak Matrix and Matrix 2 CNC control fault codes: alarm descriptions, servo, spindle, and system alarms with diagnostic steps and troubleshooting."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - mazak
  - cnc
  - matrix
  - fault-codes
---

## Mazak Matrix/Matrix 2 Fault Code Guide

The Mazak Matrix and Matrix 2 CNC controls are used on Nexus, Integrex, and Quick Turn machines. The Matrix control uses a Windows-based touchscreen interface with detailed alarm messages.

## Alarm Categories

| Alarm Range | Category |
|------------|----------|
| 001–099 | Machine/PLC alarms |
| 100–199 | Servo and axis alarms |
| 200–299 | Spindle alarms |
| 300–399 | Hydraulic and system |
| 400–499 | ATC and turret |
| 500–599 | General NC alarms |

## Common Alarm Quick Reference

| Alarm | Meaning | Quick Fix |
|-------|---------|-----------|
| 101 Servo Alarm — X | X-axis servo fault | Check drive and motor |
| 200 Spindle Alarm | Spindle drive fault | Check spindle drive and motor |
| 300 Hydraulic Pressure Low | Hydraulic system below setpoint | Check hydraulic pump and oil level |
| 401 ATC Fault | Tool changer problem | Inspect ATC mechanism and position |
| 501 Memory Error | NC memory fault | Backup and re-initialize memory |

## Matrix Alarm Detail Screen

The Mazak Matrix displays alarms in the ALARM screen with:
- Alarm number and description
- Sub-code for drives (often shown as amplifier code)
- Timestamp and machine mode at time of fault

Access: **ALARM** softkey on the Matrix main screen. Scroll to view alarm history.

## Most Common Matrix Alarms

### Servo Alarm (100-series)
A 100-series servo alarm on the Matrix indicates the servo drive (Mazatrol amplifier) for the named axis has detected a fault. Check the amplifier LED status on the drive unit inside the cabinet. Sub-codes indicate: overcurrent, overvoltage, regeneration fault, or encoder error.

### Spindle Alarm (200-series)
The spindle drive has faulted. Note the sub-code on the spindle drive display. Common causes: spindle overload (heavy cut or dull tool), encoder issue, drive board failure.

### Hydraulic Pressure Alarm (300-series)
The hydraulic system pressure dropped below the minimum required for clamp/unclamp operations. Check hydraulic oil level, pump operation, and hydraulic pressure switch.

### ATC Fault (400-series)
The automatic tool changer did not complete its cycle within the allowed time or position error exceeded tolerance. Inspect the ATC mechanism for mechanical obstruction, worn cams, or hydraulic issues on hydraulically actuated ATCs.

## Matrix 2 Differences from Matrix

Matrix 2 added:
- Dual-channel spindle management
- Enhanced tool life management
- Improved servo communication diagnostics
- Additional machine parameter access

Alarm behavior is similar but sub-codes may differ — always reference the machine-specific alarm guide.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Servo amplifier (Mazatrol) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-matrix-fault-codes&k=Servo+amplifier+%28Mazatrol%29&tag=errorcodefixes-20) \| Replace on persistent servo alarms |
| Spindle encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-matrix-fault-codes&k=Spindle+encoder&tag=errorcodefixes-20) \| Replace on spindle speed/comm alarms |
| Hydraulic filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-matrix-fault-codes&k=Hydraulic+filter&tag=errorcodefixes-20) \| Replace on low pressure alarms |
| ATC cam follower | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mazak-matrix-fault-codes&k=ATC+cam+follower&tag=errorcodefixes-20) \| Inspect on ATC mechanical faults |
## Jump to Fix

- **Servo alarm** → Note drive sub-code → Check motor and encoder → Replace drive if needed
- **Spindle alarm** → Note spindle drive code → Check spindle motor → Inspect encoder
- **Hydraulic alarm** → Check oil level → Inspect pump → Check pressure switch

## When to Call a Pro
Mazak has a service team accessible via 1-859-342-1700. The Mazak SmartBox remote diagnostics system can also assist in diagnosing complex faults.

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)

## See Also

- [Mazak Servo Parameter Error Fix (Matrix, M-Plus, Smooth)](/posts/mazak-servo-parameter-error/)
- [Mazak Alarm 900 Tool Magazine Index Fault - Causes & Fix](/posts/mazak-alarm-900-magazine/)
- [Mazak Alarm 218 — Spindle Motor Overheat Fix](/posts/mazak-alarm-218/)
- [Mazak Alarm 1 Servo Alarm — Causes & Fix](/posts/mazak-alarm-1-servo/)
