---
title: "Daikin RXQ VRV System Error Codes (Outdoor Unit): Complete Guide"
description: "Daikin RXQ VRV outdoor unit error codes and fault diagnostics. U-series fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - daikin
  - vrf
  - commercial-hvac
---

# Daikin RXQ VRV System Error Codes (Outdoor Unit)

Daikin RXQ series VRV outdoor units display fault codes on the unit service panel LED. Codes use an alphanumeric format (e.g., U0, E1, C4). Codes can be retrieved remotely via Daikin Intelligent Touch Controller (ITC) or DIII-NET interface. The LED flashes a letter-number code ΓÇö observe both the letter (flashes) and number (quick flashes).

## RXQ Outdoor Unit Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| U0 | Refrigerant shortage | Low charge or leak | Check pressures, leak test |
| U2 | Power supply fault | Low voltage or phase loss | Check power supply |
| U4 | Communication error | Indoor/outdoor wiring fault | Check communication wiring |
| U7 | System address conflict | Address duplication | Verify unit addresses |
| U9 | Indoor/outdoor mismatch | Incompatible units | Check compatibility |
| E1 | PCB fault | Outdoor control board failure | Replace PCB |
| E3 | High-pressure switch | High discharge pressure | Check coil and refrigerant |
| E4 | Low-pressure switch | Low suction pressure | Check charge and TXV |
| E7 | Fan motor fault | Fan motor or PCB driver | Check motor amps and PCB |
| E9 | Electronic expansion valve | EEV driver or valve fault | Check EEV operation |
| F3 | Discharge temp high | Refrigerant shortage, blockage | Check charge, EEV position |
| L4 | Radiation fin overtemp | Inverter overheating | Check inverter fins and fan |
| L5 | Inverter overcurrent | Inverter or compressor fault | Check compressor amps |
| L8 | Compressor overcurrent | Compressor protection | Check compressor winding |

## Most Common RXQ Faults

### U4 ΓÇö Communication Error
The most common VRV installation fault. Communication between indoor and outdoor units uses a shielded 3-wire bus (F1, F2, shield). Check all terminal connections, verify wire polarity, and check for damaged insulation. Communication errors often appear as multiple indoor unit faults simultaneously.

### E3 ΓÇö High-Pressure Switch
Daikin VRV systems use R-410A (some older RXQ use R-22). HP switch opens at approximately 590 psi (R-410A). Check outdoor heat exchanger for dirt and debris. On heat mode, check indoor coil airflow.

### U0 ΓÇö Refrigerant Shortage
VRV systems require precise refrigerant charge based on total indoor unit capacity and piping length. Use Daikin's charging calculator ΓÇö adding by pressure alone is incorrect on inverter systems.

### L5 ΓÇö Inverter Overcurrent
Check compressor winding resistance (typically 0.5ΓÇô2 ╬⌐ per phase). Check inverter board for burned components. Measure DC bus voltage at inverter.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Outdoor PCB | [Amazon](https://www.amazon.com/s?k=Outdoor+PCB&tag=errorcodefixes-20) \| Match exact RXQ model number |
| Electronic expansion valve (EEV) | [Amazon](https://www.amazon.com/s?k=Electronic+expansion+valve+%28EEV%29&tag=errorcodefixes-20) \| Match refrigerant and valve size |
| Fan motor | [Amazon](https://www.amazon.com/s?k=Fan+motor&tag=errorcodefixes-20) \| VRV units often use DC motors |
| High-pressure switch | [Amazon](https://www.amazon.com/s?k=High-pressure+switch&tag=errorcodefixes-20) \| Match refrigerant type |
| Communication cable | [Amazon](https://www.amazon.com/s?k=Communication+cable&tag=errorcodefixes-20) \| F1/F2 ΓÇö shielded type required |
> **Pro tip:** Daikin VRV systems allow fault code retrieval via the intelligent touch controller without visiting the outdoor unit. Press the Mode/Fan button combination to enter service mode and retrieve all connected unit faults.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E1 Error Code Fix — Indoor Sensor Fault](/posts/daikin-e1-error-code/)
