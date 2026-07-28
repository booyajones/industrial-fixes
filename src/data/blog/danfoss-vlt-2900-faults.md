---
title: "Danfoss VLT 2900 Fault Codes: Complete Guide"
description: "Danfoss VLT 2900 VFD fault codes and diagnostics. AL-series alarm codes, causes, and technician-level troubleshooting for VLT 2900 drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
  - industrial
  - motor-control
---

# Danfoss VLT 2900 Fault Codes

The Danfoss VLT 2900 series is a general-purpose VFD rated 0.37–30 kW. Alarm codes display on the LCP (Local Control Panel) as "AL" followed by a number. Warning codes display as "W" codes. The VLT 2900 is an older series — replacement is the VLT FC301/302 family.

## VLT 2900 Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| AL 1 | 10V supply low | 10V reference output shorted | Check terminal 50 wiring |
| AL 2 | Live zero fault | Reference input below minimum | Check analog input signal |
| AL 4 | Phase loss (motor) | Missing output phase | Check motor connections |
| AL 5 | DC link overvoltage | Regeneration or voltage spike | Extend decel ramp, add brake |
| AL 7 | DC link overvoltage (fault) | Persistent overvoltage | Check input voltage |
| AL 13 | Overcurrent | Motor short or overload | Megger test motor, reduce load |
| AL 14 | Ground fault | Motor winding ground | Megger test motor |
| AL 15 | Drive incompatible | Wrong hardware | Check drive model |
| AL 16 | Short circuit | Output short circuit | Check motor and cables |
| AL 17 | Control word timeout | Serial communication loss | Check network connection |
| AL 25 | Brake resistor short | Brake resistor failure | Check brake resistor resistance |
| AL 29 | Heatsink overtemp | Cooling blocked or high ambient | Clean fins, check fan |
| AL 34 | Communication fault | Fieldbus timeout | Check communication network |
| AL 38 | Motor thermal limit | Motor overtemperature | Reduce load, check motor cooling |
| AL 41 | Analog input 53 low | Signal below minimum | Check signal from sensor/controller |

## Most Common VLT 2900 Faults

### AL 13 — Overcurrent
The VLT 2900 is sensitive to output impedance. Verify motor data in parameters 102–106 (nameplate data). Increase parameter 207 (acceleration time). If the fault is immediate on start, check for a short circuit at output terminals.

### AL 29 — Heatsink Overtemperature
VLT 2900 units installed in enclosures must have adequate ventilation. Heatsink temperature limit is 90°C. Clean fins with compressed air. In enclosed panels, provide fan-forced cooling with adequate airflow through the panel.

### AL 5 — DC Link Overvoltage
Most common on applications with high inertia loads (fans, pumps, centrifuges). The VLT 2900 DC bus charges if motor decelerates faster than the drive absorbs energy. Extend decel time (parameter 208) or add brake chopper/resistor.

### AL 14 — Ground Fault
Use megohmmeter at 1000 VDC on all motor windings and cables. Also check PE (ground) connection integrity at both motor and drive. Long cables act as capacitors and can cause nuisance ground fault trips on older drives.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| LCP control panel | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-2900-faults&k=LCP+control+panel&tag=errorcodefixes-20) \| Available as replacement accessory |
| Brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-2900-faults&k=Brake+resistor&tag=errorcodefixes-20) \| Match resistance and power rating |
| Cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-2900-faults&k=Cooling+fan&tag=errorcodefixes-20) \| Specific to VLT 2900 frame size |
| Fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-2900-faults&k=Fuses&tag=errorcodefixes-20) \| Note: VLT 2900 uses specific semiconductor fuse types |
> **Pro tip:** Danfoss VLT 2900 drives are discontinued. When parts are no longer available, the FC301/FC302 is the recommended migration path. Danfoss provides a parameter migration guide for converting VLT 2900 parameters to FC302 equivalents.
