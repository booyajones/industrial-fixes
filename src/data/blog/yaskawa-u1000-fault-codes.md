---
title: "Yaskawa U1000 Fault Codes: Complete Guide"
description: "Yaskawa U1000 matrix drive fault codes and diagnostics. Fault codes, causes, and technician-level troubleshooting for U1000 industrial drives."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
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

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OC | Overcurrent | [Motor winding, short circuit, accel](https://www.amazon.com/s?k=Motor%20winding%2C%20short%20circuit%2C%20accel&tag=errorcodefixe-20) | Check motor and increase ramp |
| [OV](https://www.amazon.com/s?k=OV&tag=errorcodefixe-20) | Overvoltage | Excess regenerative energy | [Check matrix converter operation](https://www.amazon.com/s?k=Check%20matrix%20converter%20operation&tag=errorcodefixe-20) |  | UV1 | [DC bus undervoltage](https://www.amazon.com/s?k=DC%20bus%20undervoltage&tag=errorcodefixe-20) | Low supply voltage | Check supply voltage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | UV2 | Control power undervoltage | [Control board fault](https://www.amazon.com/s?k=Control%20board%20fault&tag=errorcodefixe-20) | Check control power supply |
| [OH](https://www.amazon.com/s?k=OH&tag=errorcodefixe-20) | Heatsink overtemperature | High ambient, cooling blocked | [Clean heatsink, check fan](https://www.amazon.com/s?k=Clean%20heatsink%2C%20check%20fan&tag=errorcodefixe-20) |  | OL1 | [Motor overload](https://www.amazon.com/s?k=Motor%20overload&tag=errorcodefixe-20) | Motor running above FLA | Reduce load, check cooling | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OL2 | Drive overload | [Drive oversized load](https://www.amazon.com/s?k=Drive%20oversized%20load&tag=errorcodefixe-20) | Check drive current rating |
| [GF](https://www.amazon.com/s?k=GF&tag=errorcodefixe-20) | Ground fault | Motor winding ground | [Megger test motor](https://www.amazon.com/s?k=Megger%20test%20motor&tag=errorcodefixe-20) |  | SC | [Short circuit output](https://www.amazon.com/s?k=Short%20circuit%20output&tag=errorcodefixe-20) | Output short circuit | Check motor cable | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CF | Control fault | [Control board error](https://www.amazon.com/s?k=Control%20board%20error&tag=errorcodefixe-20) | Check control power and connections |
| [BB](https://www.amazon.com/s?k=BB&tag=errorcodefixe-20) | Base block | External fault triggered | [Check external fault contact](https://www.amazon.com/s?k=Check%20external%20fault%20contact&tag=errorcodefixe-20) |  | EF0 | [External fault](https://www.amazon.com/s?k=External%20fault&tag=errorcodefixe-20) | Fault input active | Check input terminal wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | LF | Output phase loss | [Missing output phase](https://www.amazon.com/s?k=Missing%20output%20phase&tag=errorcodefixe-20) | Check motor cable connections |
| [PF](https://www.amazon.com/s?k=PF&tag=errorcodefixe-20) | Input power fault | Input phase loss | [Check input fuses and supply](https://www.amazon.com/s?k=Check%20input%20fuses%20and%20supply&tag=errorcodefixe-20) | ## Most Common U1000 Faults

### OC — Overcurrent
The U1000 matrix topology is sensitive to output impedance changes. Perform motor auto-tuning (T1-01 = 2, stationary tuning). Increase acceleration time (C1-01). Check motor connection for loose terminals.

### OH — Heatsink Overtemperature
The U1000 uses active cooling. Check heatsink fan operation on both the matrix converter and output stage. Measure ambient temperature — rated to 45°C without derating. U1000 can be installed in vertical orientation only.

### UV1 — DC Bus Undervoltage
The U1000 matrix drive does not have a traditional DC bus capacitor. UV1 triggers when input voltage drops below minimum. Check all three input phases — a single phase loss causes immediate UV1 on the U1000.

### GF — Ground Fault
Matrix drives are sensitive to ground faults due to the direct AC-to-AC conversion. Megger test all motor windings at 500 VDC. Check cable shielding termination.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Cooling fan | [Match U1000 frame size](https://www.amazon.com/s?k=Match%20U1000%20frame%20size&tag=errorcodefixe-20) |  | Control board | [Contact Yaskawa before ordering](https://www.amazon.com/s?k=Contact%20Yaskawa%20before%20ordering&tag=errorcodefixe-20) |  | Input filter | [Required for matrix drive installations](https://www.amazon.com/s?k=Required%20for%20matrix%20drive%20installations&tag=errorcodefixe-20) |  | Bypass contactor | For maintenance bypass configurations |

> **Pro tip:** Yaskawa U1000 drive data can be monitored via DriveWizard Industrial software. Connect via USB or DeviceNet to log operating parameters and fault data. Always perform a motor auto-tune after any parameter reset.
