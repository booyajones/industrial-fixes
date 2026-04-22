---
title: "Mazak Matrix/Matrix 2 Fault Code Guide — Complete Reference"
description: "Mazak Matrix and Matrix 2 CNC control fault codes: alarm descriptions, servo, spindle, and system alarms with diagnostic steps and troubleshooting."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
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

| [Alarm Range](https://www.amazon.com/s?k=Alarm%20Range&tag=errorcodefixe-20) | Category |
|------------|----------|
| [001–099](https://www.amazon.com/s?k=001%E2%80%93099&tag=errorcodefixe-20) | Machine/PLC alarms |
| [100–199](https://www.amazon.com/s?k=100%E2%80%93199&tag=errorcodefixe-20) | Servo and axis alarms |
| [200–299](https://www.amazon.com/s?k=200%E2%80%93299&tag=errorcodefixe-20) | Spindle alarms |
| [300–399](https://www.amazon.com/s?k=300%E2%80%93399&tag=errorcodefixe-20) | Hydraulic and system |
| [400–499](https://www.amazon.com/s?k=400%E2%80%93499&tag=errorcodefixe-20) | ATC and turret |
| [500–599](https://www.amazon.com/s?k=500%E2%80%93599&tag=errorcodefixe-20) | General NC alarms |

## Common Alarm Quick Reference

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------- |---------|-----------|
| 101 Servo Alarm — X | [X-axis servo fault](https://www.amazon.com/s?k=X-axis%20servo%20fault&tag=errorcodefixe-20) | Check drive and motor |
| [200 Spindle Alarm](https://www.amazon.com/s?k=200%20Spindle%20Alarm&tag=errorcodefixe-20) | Spindle drive fault | Check spindle drive and motor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 300 Hydraulic Pressure Low | Hydraulic system below setpoint | [Check hydraulic pump and oil level](https://www.amazon.com/s?k=Check%20hydraulic%20pump%20and%20oil%20level&tag=errorcodefixe-20) |  | 401 ATC Fault | [Tool changer problem](https://www.amazon.com/s?k=Tool%20changer%20problem&tag=errorcodefixe-20) | Inspect ATC mechanism and position |
| [501 Memory Error](https://www.amazon.com/s?k=501%20Memory%20Error&tag=errorcodefixe-20) | NC memory fault | Backup and re-initialize memory | [## Matrix Alarm Detail Screen

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

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Matrix%20Alarm%20Detail%20Screen%0A%0AThe%20Mazak%20Matrix%20displays%20alarms%20in%20the%20ALARM%20screen%20with%3A%0A-%20Alarm%20number%20and%20description%0A-%20Sub-code%20for%20drives%20(often%20shown%20as%20amplifier%20code)%0A-%20Timestamp%20and%20machine%20mode%20at%20time%20of%20fault%0A%0AAccess%3A%20**ALARM**%20softkey%20on%20the%20Matrix%20main%20screen.%20Scroll%20to%20view%20alarm%20history.%0A%0A%23%23%20Most%20Common%20Matrix%20Alarms%0A%0A%23%23%23%20Servo%20Alarm%20(100-series)%0AA%20100-series%20servo%20alarm%20on%20the%20Matrix%20indicates%20the%20servo%20drive%20(Mazatrol%20amplifier)%20for%20the%20named%20axis%20has%20detected%20a%20fault.%20Check%20the%20amplifier%20LED%20status%20on%20the%20drive%20unit%20inside%20the%20cabinet.%20Sub-codes%20indicate%3A%20overcurrent%2C%20overvoltage%2C%20regeneration%20fault%2C%20or%20encoder%20error.%0A%0A%23%23%23%20Spindle%20Alarm%20(200-series)%0AThe%20spindle%20drive%20has%20faulted.%20Note%20the%20sub-code%20on%20the%20spindle%20drive%20display.%20Common%20causes%3A%20spindle%20overload%20(heavy%20cut%20or%20dull%20tool)%2C%20encoder%20issue%2C%20drive%20board%20failure.%0A%0A%23%23%23%20Hydraulic%20Pressure%20Alarm%20(300-series)%0AThe%20hydraulic%20system%20pressure%20dropped%20below%20the%20minimum%20required%20for%20clamp%2Funclamp%20operations.%20Check%20hydraulic%20oil%20level%2C%20pump%20operation%2C%20and%20hydraulic%20pressure%20switch.%0A%0A%23%23%23%20ATC%20Fault%20(400-series)%0AThe%20automatic%20tool%20changer%20did%20not%20complete%20its%20cycle%20within%20the%20allowed%20time%20or%20position%20error%20exceeded%20tolerance.%20Inspect%20the%20ATC%20mechanism%20for%20mechanical%20obstruction%2C%20worn%20cams%2C%20or%20hydraulic%20issues%20on%20hydraulically%20actuated%20ATCs.%0A%0A%23%23%20Matrix%202%20Differences%20from%20Matrix%0A%0AMatrix%202%20added%3A%0A-%20Dual-channel%20spindle%20management%0A-%20Enhanced%20tool%20life%20management%0A-%20Improved%20servo%20communication%20diagnostics%0A-%20Additional%20machine%20parameter%20access%0A%0AAlarm%20behavior%20is%20similar%20but%20sub-codes%20may%20differ%20%E2%80%94%20always%20reference%20the%20machine-specific%20alarm%20guide.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Servo amplifier (Mazatrol) | Replace on persistent servo alarms | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Spindle encoder | Replace on spindle speed/comm alarms | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hydraulic filter | Replace on low pressure alarms | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ATC cam follower | Inspect on ATC mechanical faults |

## Jump to Fix

- **Servo alarm** → Note drive sub-code → Check motor and encoder → Replace drive if needed
- **Spindle alarm** → Note spindle drive code → Check spindle motor → Inspect encoder
- **Hydraulic alarm** → Check oil level → Inspect pump → Check pressure switch

## When to Call a Pro
Mazak has a service team accessible via 1-859-342-1700. The Mazak SmartBox remote diagnostics system can also assist in diagnosing complex faults.
