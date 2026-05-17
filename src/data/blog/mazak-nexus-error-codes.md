---
title: "Mazak Nexus Series Error Codes: Complete Guide"
description: "Mazak Nexus CNC error codes and alarm diagnostics. Alarm categories, causes, and technician-level troubleshooting for Nexus turning and machining centers."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - mazak
  - industrial
  - machining
---

# Mazak Nexus Series Error Codes

Mazak Nexus series (QTN, QT, VCN, VCS, HCN) machines use the Mazatrol MATRIX CNC or SMOOTHG control. Alarms display on the CNC screen with a number and description. Alarms are grouped by category: 1xx (servo), 2xx (spindle), 3xx (PC/control), 4xx (OT/limit), 5xx (ATC/APC), 6xx (chuck/tailstock).

## Nexus Alarm Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| 50 | Emergency stop | E-stop activated | Release and check cause |
| 100 | Servo alarm — X axis | Servo drive or motor fault | Check servo drive |
| 200 | Spindle alarm | Spindle drive fault | Check spindle drive |
| 201 | Spindle overspeed | Speed above maximum | Check program S code |
| 300 | Control unit alarm | NC/PC communication fault | Check PC board |
| 400 | Overtravel — positive | Axis past positive limit | Move axis, check limits |
| 401 | Overtravel — negative | Axis past negative limit | Move axis, check limits |
| 500 | ATC alarm | Tool changer fault | Check ATC sequence |
| 501 | Magazine alarm | Magazine positioning fault | Check magazine servo |
| 600 | Chuck fault | Chuck not clamped | Check hydraulic pressure |
| 601 | Tailstock fault | Tailstock positioning fault | Check tailstock control |
| 700 | MPC alarm | Machine parameter error | Check machine parameters |
| 800 | ATC carrier alarm | Carrier positioning fault | Check carrier servo |

## Most Common Nexus Faults

### 100/200 — Servo/Spindle Alarms
Nexus servo alarms refer to the Mazak servo pack (FANUC-based). Check servo amplifier LED on cabinet door. Alarm LED codes: 1 = overload, 2 = regeneration, 3 = DC bus, 4 = IGBT, 5 = feedback, 6 = communication. Match LED reading to specific remediation.

### 400/401 — Overtravel
Work offset or tool offset entered incorrectly. In MDI mode with E-stop released, hold SHIFT + override axis in JOG mode to move axis back into travel range. Then review all offsets before resuming production.

### 500 — ATC Alarm
Mazak Nexus ATC sequence is programmable. Check which step in the M6 sequence fails — view ATC sequence diagram in the machine maintenance screen. Common causes: proximity switch failure, servo positioning error, or mechanical jam.

### 600 — Chuck Fault
Check hydraulic pressure (minimum 900 PSI for standard chucks). Verify workpiece is seated correctly. If chuck relay is suspected, check PLC input in the Mazatrol diagnostic screen.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Servo pack | [Amazon](https://www.amazon.com/s?i=industrial&k=Servo+pack&tag=errorcodefixes-20) \| Match axis and current rating |
| Encoder battery | [Amazon](https://www.amazon.com/s?i=industrial&k=Encoder+battery&tag=errorcodefixes-20) \| Absolute encoder backup |
| ATC proximity switches | [Amazon](https://www.amazon.com/s?i=industrial&k=ATC+proximity+switches&tag=errorcodefixes-20) \| Check position in sequence diagram |
| Hydraulic pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| Chuck and tailstock circuits |
| Coolant pump | [Amazon](https://www.amazon.com/s?i=industrial&k=Coolant+pump&tag=errorcodefixes-20) \| Check impeller and motor amps |
> **Pro tip:** Mazak Nexus stores alarm history with timestamps in the ALARM LOG menu. Access via MAINTENANCE ΓåÆ ALARM LOG. Historical data shows if an alarm is intermittent (temperature-related) or consistent (mechanical or electrical failure).

## Related Articles

- [CNC Alarm Reset Guide: How to Clear Alarms Safely](/posts/cnc-alarm-reset-guide/)
- [CNC Machine Error Codes: Complete Troubleshooting Guide](/posts/cnc-error-codes-guide/)
- [Doosan CNC Alarm Codes Guide — Fanuc / Fanuc i Series Controls](/posts/doosan-cnc-fault-codes/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
