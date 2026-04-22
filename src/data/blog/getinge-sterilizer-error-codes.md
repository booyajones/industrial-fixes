---
title: "Getinge Sterilizer Error Codes - Complete Guide"
description: "Getinge autoclave and sterilizer error codes for 88-series and GSS-series: fault codes, causes, and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - getinge
  - sterilizer
  - autoclave
  - medical
---

## Getinge Sterilizer Error Codes - Quick Reference

Getinge steam sterilizers (88-series, GS-series, GSS-series, and Integrity series) display fault codes on the touchscreen controller. Access the full error history via the Getinge service menu or CSAM (Central Service Access Module).

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| E001 | Temperature sensor fault | Check sensor wiring and resistance |
| E002 | Pressure sensor fault | Check transducer and wiring |
| E003 | Steam supply fault | Check steam pressure and supply valve |
| E004 | Door fault - not fully closed | Check door mechanism and gasket |
| E005 | Drain fault | Check drain trap and temperature |
| E006 | Cooling water fault | Check cooling water supply |
| E007 | Air detector fault | Check air detector valve |
| E008 | Cycle abort - temp deviation | Check steam quality and sensors |
| E009 | Communication fault | Check controller wiring |
| E010 | Power fault | Check power supply |

## Most Common Faults

### E003 - Steam Supply Fault
Getinge sterilizers require clean, saturated steam typically at 3–4 bar (45–60 psi). Supply faults occur from: closed isolation valve, steam pressure drop, or failed supply solenoid. Check the inlet pressure at the sterilizer service port. Getinge specifies steam quality per EN 285 - dryness fraction must exceed 0.95.

### E004 - Door Fault
Getinge sliding and hinged doors require full closure and locking before a cycle starts. Door faults occur from: worn door gasket, misaligned door mechanism, or a failed door interlock microswitch. Inspect the door gasket for compression set - a flat or cracked gasket won't seal and will abort cycles.

### E001 - Temperature Sensor Fault
Getinge uses PT100 or PT1000 RTD temperature sensors in the chamber and drain. A failed sensor typically reads -999 or +999 on the display. Disconnect the sensor leads and measure resistance - PT100 reads 100 ohms at 0°C; PT1000 reads 1000 ohms at 0°C. An open or shorted sensor needs replacement.

### E007 - Air Detector Fault
Getinge steam sterilizers with air detectors test for air pockets in the chamber using a porous load test. An air detector fault means the air detector valve didn't sequence correctly or the air removal test failed. Check the air detector valve solenoid and inspect for condensate blockage.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Door gasket (Getinge OEM) | Replace on E004 |
| PT100/PT1000 sensor | Replace on E001 |
| Pressure transducer | Replace on E002 |
| Steam trap | Replace on drain fault |
| Door interlock microswitch | Replace on E004 |

## When to Call a Pro
Getinge sterilizer qualification (IQ/OQ/PQ) and Bowie-Dick test interpretation require biomedical service or Getinge-certified technicians. Do not return a sterilizer to service after a critical fault without proper validation.

