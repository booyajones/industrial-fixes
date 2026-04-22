---
title: "Haas EC-400 Horizontal Machining Center Alarm Codes"
description: "Haas EC-400 horizontal machining center alarm codes and diagnostics. Common HMC alarms, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
  - industrial
  - machining
---

# Haas EC-400 Horizontal Machining Center Alarm Codes

The Haas EC-400 is a 40-taper horizontal machining center with B-axis rotary table. It uses the Haas Next Generation Control (NGC) or classic control. Alarms display on the control screen with a number and description. The EC-400 shares many alarms with other Haas mills but has unique alarms for its 4-axis configuration and ATC.

## EC-400 Alarm Code Table

| [Alarm](https://www.amazon.com/s?k=Alarm&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |-------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 101 | E-stop | [Emergency stop active](https://www.amazon.com/s?k=Emergency%20stop%20active&tag=errorcodefixe-20) | Check all E-stop buttons |
| [102](https://www.amazon.com/s?k=102&tag=errorcodefixe-20) | Servo overload | Axis motor overload | [Check motor amps and load](https://www.amazon.com/s?k=Check%20motor%20amps%20and%20load&tag=errorcodefixe-20) |  | 103 | [Servo drive fault](https://www.amazon.com/s?k=Servo%20drive%20fault&tag=errorcodefixe-20) | Drive failure or overtemperature | Check servo drive LEDs | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 110 | X-axis servo error | [Position error (following error)](https://www.amazon.com/s?k=Position%20error%20(following%20error)&tag=errorcodefixe-20) | Check axis motor and encoder |
| [111](https://www.amazon.com/s?k=111&tag=errorcodefixe-20) | Y-axis servo error | Position error | [Check Y motor and encoder](https://www.amazon.com/s?k=Check%20Y%20motor%20and%20encoder&tag=errorcodefixe-20) |  | 112 | [Z-axis servo error](https://www.amazon.com/s?k=Z-axis%20servo%20error&tag=errorcodefixe-20) | Position error | Check Z motor and encoder | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 113 | B-axis servo error | [B-axis rotary position error](https://www.amazon.com/s?k=B-axis%20rotary%20position%20error&tag=errorcodefixe-20) | Check B-axis drive and encoder |
| [120](https://www.amazon.com/s?k=120&tag=errorcodefixe-20) | ATC fault | Tool changer problem | [Check ATC carousel and arm](https://www.amazon.com/s?k=Check%20ATC%20carousel%20and%20arm&tag=errorcodefixe-20) |  | 121 | [ATC magazine fault](https://www.amazon.com/s?k=ATC%20magazine%20fault&tag=errorcodefixe-20) | Magazine positioning error | Check magazine motor and switch | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 125 | Carousel fault | [Carousel servo error](https://www.amazon.com/s?k=Carousel%20servo%20error&tag=errorcodefixe-20) | Check carousel servo drive |
| [130](https://www.amazon.com/s?k=130&tag=errorcodefixe-20) | Spindle drive fault | Spindle drive alarm | [Check spindle drive display](https://www.amazon.com/s?k=Check%20spindle%20drive%20display&tag=errorcodefixe-20) |  | 134 | [Spindle overload](https://www.amazon.com/s?k=Spindle%20overload&tag=errorcodefixe-20) | Spindle motor overload | Reduce cutting conditions | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 138 | Spindle orientation fault | [Spindle M19 failed](https://www.amazon.com/s?k=Spindle%20M19%20failed&tag=errorcodefixe-20) | Check orientation sensor and drive |
| [149](https://www.amazon.com/s?k=149&tag=errorcodefixe-20) | Low lube fault | Lubrication system low | [Check lube oil level and pump](https://www.amazon.com/s?k=Check%20lube%20oil%20level%20and%20pump&tag=errorcodefixe-20) | ## Most Common EC-400 Faults

### Alarm 130 — Spindle Drive Fault
Check the Haas Vector spindle drive (located in cabinet). The drive has an LED display showing an internal fault code. Common EC-400 spindle faults: SPD (spindle drive fault), OC (overcurrent), OT (overtemperature). Check spindle motor air cooling passage for chips and debris.

### Alarm 120 — ATC Fault
The EC-400 has a 30-pocket or 60-pocket side-mount ATC. Check for a jammed tool, broken retention knob, or carousel positioning fault. Manually jog the ATC through its sequence using the Haas diagnostic screens to identify which step fails.

### Alarms 110–113 — Servo Error
Following error exceeds maximum threshold. Causes: mechanical binding (lubrication issue, crashed axis, damaged ball screw), encoder cable fault, or servo drive fault. Check axis by jogging slowly and monitoring servo load on the control screen.

### Alarm 149 — Low Lube
The EC-400 uses a central lubrication system (Rexnord or equivalent). Check the lube oil reservoir level, verify the pump runs on cycle, and check all lube lines for blockage. The lube fault can also be triggered by a failed pressure switch.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Servo motors | [Alpha series — match axis](https://www.amazon.com/s?k=Alpha%20series%20%E2%80%94%20match%20axis&tag=errorcodefixe-20) |  | Encoder cables | [Check at both motor and drive connectors](https://www.amazon.com/s?k=Check%20at%20both%20motor%20and%20drive%20connectors&tag=errorcodefixe-20) |  | ATC solenoid valves | [Check for proper operation](https://www.amazon.com/s?k=Check%20for%20proper%20operation&tag=errorcodefixe-20) |  | Lube pump | [Check for seized impeller](https://www.amazon.com/s?k=Check%20for%20seized%20impeller&tag=errorcodefixe-20) |  | Retention knobs | [Replace damaged/worn 40-taper knobs](https://www.amazon.com/s?k=Replace%20damaged%2Fworn%2040-taper%20knobs&tag=errorcodefixe-20) |  | Way wipers | Inspect and replace if worn |

> **Pro tip:** Haas EC-400 service information is available on the Haas Service Portal (haasspeed.com). The NGC diagnostic screens show real-time servo loads, spindle RPM, and I/O status — use these during troubleshooting to observe behavior without disassembly.
