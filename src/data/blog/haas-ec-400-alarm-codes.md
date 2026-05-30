---
title: "Haas EC-400 Horizontal Machining Center Alarm Codes"
description: "Haas EC-400 horizontal machining center alarm codes and diagnostics. Common HMC alarms, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
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

| Alarm | Fault Description | Common Cause | Action |
|-------|------------------|--------------|--------|
| 101 | E-stop | Emergency stop active | Check all E-stop buttons |
| 102 | Servo overload | Axis motor overload | Check motor amps and load |
| 103 | Servo drive fault | Drive failure or overtemperature | Check servo drive LEDs |
| 110 | X-axis servo error | Position error (following error) | Check axis motor and encoder |
| 111 | Y-axis servo error | Position error | Check Y motor and encoder |
| 112 | Z-axis servo error | Position error | Check Z motor and encoder |
| 113 | B-axis servo error | B-axis rotary position error | Check B-axis drive and encoder |
| 120 | ATC fault | Tool changer problem | Check ATC carousel and arm |
| 121 | ATC magazine fault | Magazine positioning error | Check magazine motor and switch |
| 125 | Carousel fault | Carousel servo error | Check carousel servo drive |
| 130 | Spindle drive fault | Spindle drive alarm | Check spindle drive display |
| 134 | Spindle overload | Spindle motor overload | Reduce cutting conditions |
| 138 | Spindle orientation fault | Spindle M19 failed | Check orientation sensor and drive |
| 149 | Low lube fault | Lubrication system low | Check lube oil level and pump |

## Most Common EC-400 Faults

### Alarm 130 — Spindle Drive Fault
Check the Haas Vector spindle drive (located in cabinet). The drive has an LED display showing an internal fault code. Common EC-400 spindle faults: SPD (spindle drive fault), OC (overcurrent), OT (overtemperature). Check spindle motor air cooling passage for chips and debris.

### Alarm 120 — ATC Fault
The EC-400 has a 30-pocket or 60-pocket side-mount ATC. Check for a jammed tool, broken retention knob, or carousel positioning fault. Manually jog the ATC through its sequence using the Haas diagnostic screens to identify which step fails.

### Alarms 110–113 — Servo Error
Following error exceeds maximum threshold. Causes: mechanical binding (lubrication issue, crashed axis, damaged ball screw), encoder cable fault, or servo drive fault. Check axis by jogging slowly and monitoring servo load on the control screen.

### Alarm 149 — Low Lube
The EC-400 uses a central lubrication system (Rexnord or equivalent). Check the lube oil reservoir level, verify the pump runs on cycle, and check all lube lines for blockage. The lube fault can also be triggered by a failed pressure switch.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Servo motors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-ec-400-alarm-codes&k=Servo+motors&tag=errorcodefixes-20) \| Alpha series — match axis |
| Encoder cables | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-ec-400-alarm-codes&k=Encoder+cables&tag=errorcodefixes-20) \| Check at both motor and drive connectors |
| ATC solenoid valves | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-ec-400-alarm-codes&k=ATC+solenoid+valves&tag=errorcodefixes-20) \| Check for proper operation |
| Lube pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-ec-400-alarm-codes&k=Lube+pump&tag=errorcodefixes-20) \| Check for seized impeller |
| Retention knobs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-ec-400-alarm-codes&k=Retention+knobs&tag=errorcodefixes-20) \| Replace damaged/worn 40-taper knobs |
| Way wipers | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-ec-400-alarm-codes&k=Way+wipers&tag=errorcodefixes-20) \| Inspect and replace if worn |
> **Pro tip:** Haas EC-400 service information is available on the Haas Service Portal (haasspeed.com). The NGC diagnostic screens show real-time servo loads, spindle RPM, and I/O status — use these during troubleshooting to observe behavior without disassembly.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas Alarm 103 Overheating — CNC Machine Thermal Fault Diagnosis and Fix](/posts/haas-alarm-103-overheating/)
- [Haas Alarm 107 — Causes & Fix](/posts/haas-alarm-107/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas SL-20 Lathe Common Alarms — What They Mean and How to Fix Them](/posts/haas-sl-20-lathe-alarms/)
