---
title: "Control Techniques Unidrive SP Fault Codes — Complete Guide"
description: "Control Techniques Unidrive SP fault codes: all trip codes for Unidrive SP and M series VFDs with causes and step-by-step fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - control-techniques
  - emerson
  - motor-control
---

## Control Techniques Unidrive SP Fault Codes — Quick Reference

Control Techniques (now part of Nidec) manufactures the Unidrive SP and Unidrive M series variable-speed drives, widely used in industrial applications. The drives display fault codes as text "trip" codes on the keypad display. The trip history is accessible via parameter Pr 10.20–10.29 (last 10 trips).

| [Trip Code](https://www.amazon.com/s?i=industrial&k=Trip+Code&tag=errorcodefixes-20) | Meaning | Common Cause | Quick Fix |
|-----------|---------|-------------|-----------|
| [OI.AC](https://www.amazon.com/s?i=industrial&k=OI.AC&tag=errorcodefixes-20) | Overcurrent — AC output | Short circuit; too fast acceleration | Check motor wiring; increase accel time |
| [OI.DC](https://www.amazon.com/s?i=industrial&k=OI.DC&tag=errorcodefixes-20) | Overcurrent — DC bus | Braking energy; voltage spike | Add brake resistor; check decel |
| OV | DC Bus Overvoltage | Fast deceleration; high supply voltage | Increase decel time; add brake resistor |
| UV | DC Bus Undervoltage | Low input voltage; power interruption | Check supply voltage; check fuses |
| OH | Drive heatsink overtemperature | Blocked fan; high ambient temp | Clean heatsink; improve ventilation |
| OH2 | Control board overtemperature | Ambient too hot | Improve enclosure cooling |
| [t.dEF](https://www.amazon.com/s?i=industrial&k=t.dEF&tag=errorcodefixes-20) | Thermistor fault — motor PTC | PTC resistance out of range | Check PTC wiring; check motor temp |
| Ot | Motor overtemperature — model-based | Motor overloaded | Reduce load; check motor cooling |
| SCL | Serial comms loss | Fieldbus or serial link interrupted | Check comms wiring; check master device |
| EEF | EEPROM fault — parameter error | Parameter corruption | Restore factory defaults and reprogram |
| PSF | Power supply fault — internal | Internal power supply failed | Replace drive |
| [O.SPd](https://www.amazon.com/s?i=industrial&k=O.SPd&tag=errorcodefixes-20) | Overspeed | Speed feedback exceeded limit | Check speed reference; check encoder |
| EnC | Encoder fault | Encoder signal lost or invalid | Check encoder wiring; check speed |
| Ph | Input phase loss | Missing L1, L2, or L3 | Check input wiring; check fuses |
| GF | Ground fault | Motor or cable insulation fault | Megger motor; check cable |

## Most Common Faults

### OI.AC — AC Output Overcurrent
The output current exceeded the instantaneous trip threshold (typically 200–220% of rated current). This is the most common trip on the Unidrive SP in industrial pump and fan applications.

**Diagnosis:**
1. Check if the trip occurs at startup or while running — startup OI.AC often indicates too-short acceleration time or a high-inertia load
2. If running, check for a mechanical jam in the driven load
3. Disconnect the motor and check output wiring for short circuits between phases or phase-to-ground

**Fix:**
- Increase acceleration time (Pr 2.11) by 50% and retry
- If the motor was recently replaced, verify the motor nameplate amps and update the drive's motor rated current parameter (Pr 5.07)

### OV — DC Bus Overvoltage
Occurs when regenerated energy from rapid deceleration raises the DC bus voltage above the trip threshold (typically 830VDC on 400VAC drives, 415VDC on 200VAC drives).

**Fix:**
- Increase deceleration time (Pr 2.21)
- Enable the drive's built-in voltage-dependent deceleration (Pr 2.32 = 1) — this automatically extends decel time to keep DC bus below trip level
- Add an external braking resistor connected to the drive's braking terminals — essential for applications with high inertia (large fans, centrifuges)

### OH — Heatsink Overtemperature
The Unidrive SP uses forced-air cooling via an internal fan. The heatsink trip occurs at approximately 90°C.

**Fix:**
1. Clean the heatsink fins thoroughly — the fins on the back of the drive pack with dust rapidly in industrial environments
2. Verify the internal cooling fan is running — it should be audible when the drive is powered
3. Check ambient temperature in the panel: maximum for Unidrive SP is 40°C
4. Verify minimum clearances: 100mm above, 100mm below, and 30mm on sides (or per installation guide)

### SCL — Serial Communications Loss
The drive lost contact with its Fieldbus master (PROFIBUS, EtherNet/IP, Modbus RTU, etc.) or serial link. Check the communications cable, the module connector on the drive, and the scan rate settings. Verify the master device is polling the drive.

### EEF — EEPROM Fault
Parameter memory has corrupted. This can occur after a power interruption during a parameter save. Reset to factory defaults (Pr 00.09 = 1000 for most models), then reprogram all required parameters. Save all parameters to a computer before this reset if possible using CT's SyPTPro or Connect software.

## Unidrive SP Parameter Menu Access

- Hold the **M** button for 2 seconds to access the full parameter list
- Trip history: navigate to Menu 10 → Pr 10.20 through 10.29
- Trip reset: press the STOP/RESET key after correcting the fault condition

## When to Call a Pro
PSF (internal power supply), GF (ground fault with motor failure), and Ph (input phase loss) on a persistent basis require an industrial drive specialist. Control Techniques service centers offer drive repair and board-level service.
