---
title: "Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide"
description: "Mitsubishi PEX City Multi indoor unit error codes and fault diagnostics. P-series codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mitsubishi
  - vrf
  - commercial-hvac
---

# Mitsubishi PEX City Multi Error Codes (Indoor Unit)

Mitsubishi City Multi PEX series indoor units display fault codes via LED on the unit PCB or on the system controller (MA Remote, G-50A, or AE-200). Codes are two-digit numbers: the first digit indicates the fault category, the second identifies the specific component.

## PEX Indoor Unit Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| P1 | Intake air temp sensor fault | Open or short in sensor | Check sensor resistance (10k╬⌐ at 77┬░F) |
| P2 | Pipe (liquid) sensor fault | Sensor failure | Check refrigerant pipe sensor |
| P4 | Drain pump fault | Drain pump failure or float switch | Check pump operation and float switch |
| P5 | Drain float switch open | High condensate level | Clear drain pan, check drain pump |
| P6 | Fan motor fault | Indoor fan motor failure | Check motor amps and operation |
| P8 | Pipe temp protection | Excessively high or low pipe temp | Check refrigerant charge and flow |
| P9 | Indoor unit error (communication) | Branch controller address | Check BC controller addressing |
| E1 | Outdoor unit error | Fault from outdoor unit | Check outdoor unit PCB |
| E6 | No communication with outdoor | Communication wiring | Check transmission wiring |
| E7 | Fan lock | Fan motor locked | Check fan blade and motor |

## Most Common PEX Indoor Faults

### P4/P5 ΓÇö Drain Issues
Commercial fan coil units accumulate condensate during cooling. P4 (drain pump fault) means the pump is not running or running dry. P5 means the float switch has lifted ΓÇö the pan is full. Clear the drain line, clean the condensate pan, and verify the pump lifts to discharge height.

### P6 ΓÇö Fan Motor Fault
Check that the fan blade turns freely. PEX units use multi-speed motors. Verify the correct speed tap is selected. Measure motor amp draw and check run capacitor where applicable.

### E6 ΓÇö No Communication
City Multi uses a 2-wire transmission network (M-NET). Check that all indoor units have unique addresses on the branch controller. Verify cable polarity and maximum network length limits.

### P8 ΓÇö Pipe Temperature Protection
If pipe temperature is too high or too low, the unit shuts down to protect the refrigerant system. On PEX branch controller systems, check EEV position at the branch controller and verify refrigerant distribution to this branch.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Intake or pipe sensor | [Amazon](https://www.amazon.com/s?k=Intake+or+pipe+sensor&tag=errorcodefixes-20) \| Mitsubishi-specific thermistors |
| Drain pump | [Amazon](https://www.amazon.com/s?k=Drain+pump&tag=errorcodefixes-20) \| Match voltage and lift height |
| Indoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Match PEX model and revision |
| Fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| Match speed, HP, and frame |
| Float switch | [Amazon](https://www.amazon.com/dp/B005D4RFEM?tag=errorcodefixes-20) \| Universal float switch fits most pans |
> **Pro tip:** Mitsubishi City Multi systems allow all indoor unit faults to be read from the G-50A or AE-200 centralized controller. Use the controller's "Monitor" screen to see all unit statuses simultaneously without checking each indoor unit individually.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
- [Mitsubishi E3 Error Code — Indoor Fan Motor Fault Fix](/posts/mitsubishi-e3-error-code/)
