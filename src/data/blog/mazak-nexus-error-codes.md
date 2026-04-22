---
title: "Mazak Nexus Series Error Codes: Complete Guide"
description: "Mazak Nexus CNC error codes and alarm diagnostics. Alarm categories, causes, and technician-level troubleshooting for Nexus turning and machining centers."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 50 | Emergency stop | [E-stop activated](https://www.amazon.com/s?k=E-stop%20activated&tag=errorcodefixe-20) | Release and check cause |
| [100](https://www.amazon.com/s?k=100&tag=errorcodefixe-20) | Servo alarm — X axis | Servo drive or motor fault | [Check servo drive](https://www.amazon.com/s?k=Check%20servo%20drive&tag=errorcodefixe-20) |  | 200 | [Spindle alarm](https://www.amazon.com/s?k=Spindle%20alarm&tag=errorcodefixe-20) | Spindle drive fault | Check spindle drive | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 201 | Spindle overspeed | [Speed above maximum](https://www.amazon.com/s?k=Speed%20above%20maximum&tag=errorcodefixe-20) | Check program S code |
| [300](https://www.amazon.com/s?k=300&tag=errorcodefixe-20) | Control unit alarm | NC/PC communication fault | [Check PC board](https://www.amazon.com/s?k=Check%20PC%20board&tag=errorcodefixe-20) |  | 400 | [Overtravel — positive](https://www.amazon.com/s?k=Overtravel%20%E2%80%94%20positive&tag=errorcodefixe-20) | Axis past positive limit | Move axis, check limits | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 401 | Overtravel — negative | [Axis past negative limit](https://www.amazon.com/s?k=Axis%20past%20negative%20limit&tag=errorcodefixe-20) | Move axis, check limits |
| [500](https://www.amazon.com/s?k=500&tag=errorcodefixe-20) | ATC alarm | Tool changer fault | [Check ATC sequence](https://www.amazon.com/s?k=Check%20ATC%20sequence&tag=errorcodefixe-20) |  | 501 | [Magazine alarm](https://www.amazon.com/s?k=Magazine%20alarm&tag=errorcodefixe-20) | Magazine positioning fault | Check magazine servo | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 600 | Chuck fault | [Chuck not clamped](https://www.amazon.com/s?k=Chuck%20not%20clamped&tag=errorcodefixe-20) | Check hydraulic pressure |
| [601](https://www.amazon.com/s?k=601&tag=errorcodefixe-20) | Tailstock fault | Tailstock positioning fault | [Check tailstock control](https://www.amazon.com/s?k=Check%20tailstock%20control&tag=errorcodefixe-20) |  | 700 | [MPC alarm](https://www.amazon.com/s?k=MPC%20alarm&tag=errorcodefixe-20) | Machine parameter error | Check machine parameters | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 800 | ATC carrier alarm | [Carrier positioning fault](https://www.amazon.com/s?k=Carrier%20positioning%20fault&tag=errorcodefixe-20) | Check carrier servo |

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
| [Servo pack](https://www.amazon.com/s?k=Servo%20pack&tag=errorcodefixe-20) | Match axis and current rating |
| [Encoder battery](https://www.amazon.com/s?k=Encoder%20battery&tag=errorcodefixe-20) | Absolute encoder backup |
| [ATC proximity switches](https://www.amazon.com/s?k=ATC%20proximity%20switches&tag=errorcodefixe-20) | Check position in sequence diagram |
| [Hydraulic pressure switch](https://www.amazon.com/s?k=Hydraulic%20pressure%20switch&tag=errorcodefixe-20) | Chuck and tailstock circuits |
| [Coolant pump](https://www.amazon.com/s?k=Coolant%20pump&tag=errorcodefixe-20) | Check impeller and motor amps |

> **Pro tip:** Mazak Nexus stores alarm history with timestamps in the ALARM LOG menu. Access via MAINTENANCE → ALARM LOG. Historical data shows if an alarm is intermittent (temperature-related) or consistent (mechanical or electrical failure).
