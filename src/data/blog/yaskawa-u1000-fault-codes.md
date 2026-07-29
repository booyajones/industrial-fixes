---
title: "Yaskawa U1000 Fault Codes: Complete Guide"
description: "Yaskawa U1000 matrix drive fault codes and diagnostics. Fault codes, causes, and technician-level troubleshooting for U1000 industrial drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
  - industrial
  - motor-control
---

# Yaskawa U1000 Fault Codes

The Yaskawa U1000 is a matrix drive (no DC bus capacitors) designed for energy recovery and ultra-low harmonics in pump and fan applications. It shares some fault codes with the A1000 family but has unique faults related to its matrix converter topology.

## U1000 Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| OC | Overcurrent | Motor winding, short circuit, accel | Check motor and increase ramp |
| OV | Overvoltage | Excess regenerative energy | Check matrix converter operation |
| UV1 | DC bus undervoltage | Low supply voltage | Check supply voltage |
| UV2 | Control power undervoltage | Control board fault | Check control power supply |
| OH | Heatsink overtemperature | High ambient, cooling blocked | Clean heatsink, check fan |
| OL1 | Motor overload | Motor running above FLA | Reduce load, check cooling |
| OL2 | Drive overload | Drive oversized load | Check drive current rating |
| GF | Ground fault | Motor winding ground | Megger test motor |
| SC | Short circuit output | Output short circuit | Check motor cable |
| CF | Control fault | Control board error | Check control power and connections |
| BB | Base block | External fault triggered | Check external fault contact |
| EF0 | External fault | Fault input active | Check input terminal wiring |
| LF | Output phase loss | Missing output phase | Check motor cable connections |
| PF | Input power fault | Input phase loss | Check input fuses and supply |

## Most Common U1000 Faults

### OC — Overcurrent
The U1000 matrix topology is sensitive to output impedance changes. Perform motor auto-tuning (T1-01 = 2, stationary tuning). Increase acceleration time (C1-01). Check motor connection for loose terminals.

### OH — Heatsink Overtemperature
The U1000 uses active cooling. Check heatsink fan operation on both the matrix converter and output stage. Measure ambient temperature — rated to 45°C without derating. U1000 can be installed in vertical orientation only.

### UV1 — DC Bus Undervoltage
The U1000 matrix drive does not have a traditional DC bus capacitor. UV1 triggers when input voltage drops below minimum. Check all three input phases — a single phase loss causes immediate UV1 on the U1000.

### GF — Ground Fault
Matrix drives are sensitive to ground faults due to the direct AC-to-AC conversion. Megger test all motor windings at 500 VDC. Check cable shielding termination.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-u1000-fault-codes&k=Cooling+fan&tag=errorcodefixes-20) \| Match U1000 frame size |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Contact Yaskawa before ordering |
| Input filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-u1000-fault-codes&k=Input+filter&tag=errorcodefixes-20) \| Required for matrix drive installations |
| Bypass contactor | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-u1000-fault-codes&k=Yaskawa+Bypass+contactor&tag=errorcodefixes-20) \| For maintenance bypass configurations |
> **Pro tip:** Yaskawa U1000 drive data can be monitored via DriveWizard Industrial software. Connect via USB or DeviceNet to log operating parameters and fault data. Always perform a motor auto-tune after any parameter reset.
