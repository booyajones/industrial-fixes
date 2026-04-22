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

Daikin RXQ series VRV outdoor units display fault codes on the unit service panel LED. Codes use an alphanumeric format (e.g., U0, E1, C4). Codes can be retrieved remotely via Daikin Intelligent Touch Controller (ITC) or DIII-NET interface. The LED flashes a letter-number code — observe both the letter (flashes) and number (quick flashes).

## RXQ Outdoor Unit Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | U0 | Refrigerant shortage | [Low charge or leak](https://www.amazon.com/s?k=Low%20charge%20or%20leak&tag=errorcodefixe-20) | Check pressures, leak test |
| [U2](https://www.amazon.com/s?k=U2&tag=errorcodefixe-20) | Power supply fault | Low voltage or phase loss | [Check power supply](https://www.amazon.com/s?k=Check%20power%20supply&tag=errorcodefixe-20) |  | U4 | [Communication error](https://www.amazon.com/s?k=Communication%20error&tag=errorcodefixe-20) | Indoor/outdoor wiring fault | Check communication wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | U7 | System address conflict | [Address duplication](https://www.amazon.com/s?k=Address%20duplication&tag=errorcodefixe-20) | Verify unit addresses |
| [U9](https://www.amazon.com/s?k=U9&tag=errorcodefixe-20) | Indoor/outdoor mismatch | Incompatible units | [Check compatibility](https://www.amazon.com/s?k=Check%20compatibility&tag=errorcodefixe-20) |  | E1 | [PCB fault](https://www.amazon.com/s?k=PCB%20fault&tag=errorcodefixe-20) | Outdoor control board failure | Replace PCB | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E3 | High-pressure switch | [High discharge pressure](https://www.amazon.com/s?k=High%20discharge%20pressure&tag=errorcodefixe-20) | Check coil and refrigerant |
| [E4](https://www.amazon.com/s?k=E4&tag=errorcodefixe-20) | Low-pressure switch | Low suction pressure | [Check charge and TXV](https://www.amazon.com/s?k=Check%20charge%20and%20TXV&tag=errorcodefixe-20) |  | E7 | [Fan motor fault](https://www.amazon.com/s?k=Fan%20motor%20fault&tag=errorcodefixe-20) | Fan motor or PCB driver | Check motor amps and PCB | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E9 | Electronic expansion valve | [EEV driver or valve fault](https://www.amazon.com/s?k=EEV%20driver%20or%20valve%20fault&tag=errorcodefixe-20) | Check EEV operation |
| [F3](https://www.amazon.com/s?k=F3&tag=errorcodefixe-20) | Discharge temp high | Refrigerant shortage, blockage | [Check charge, EEV position](https://www.amazon.com/s?k=Check%20charge%2C%20EEV%20position&tag=errorcodefixe-20) |  | L4 | [Radiation fin overtemp](https://www.amazon.com/s?k=Radiation%20fin%20overtemp&tag=errorcodefixe-20) | Inverter overheating | Check inverter fins and fan | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | L5 | Inverter overcurrent | [Inverter or compressor fault](https://www.amazon.com/s?k=Inverter%20or%20compressor%20fault&tag=errorcodefixe-20) | Check compressor amps |
| [L8](https://www.amazon.com/s?k=L8&tag=errorcodefixe-20) | Compressor overcurrent | Compressor protection | [Check compressor winding](https://www.amazon.com/s?k=Check%20compressor%20winding&tag=errorcodefixe-20) | ## Most Common RXQ Faults

### U4 — Communication Error
The most common VRV installation fault. Communication between indoor and outdoor units uses a shielded 3-wire bus (F1, F2, shield). Check all terminal connections, verify wire polarity, and check for damaged insulation. Communication errors often appear as multiple indoor unit faults simultaneously.

### E3 — High-Pressure Switch
Daikin VRV systems use R-410A (some older RXQ use R-22). HP switch opens at approximately 590 psi (R-410A). Check outdoor heat exchanger for dirt and debris. On heat mode, check indoor coil airflow.

### U0 — Refrigerant Shortage
VRV systems require precise refrigerant charge based on total indoor unit capacity and piping length. Use Daikin's charging calculator — adding by pressure alone is incorrect on inverter systems.

### L5 — Inverter Overcurrent
Check compressor winding resistance (typically 0.5–2 Ω per phase). Check inverter board for burned components. Measure DC bus voltage at inverter.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Outdoor PCB | [Match exact RXQ model number](https://www.amazon.com/s?k=Match%20exact%20RXQ%20model%20number&tag=errorcodefixe-20) |  | Electronic expansion valve (EEV) | [Match refrigerant and valve size](https://www.amazon.com/s?k=Match%20refrigerant%20and%20valve%20size&tag=errorcodefixe-20) |  | Fan motor | [VRV units often use DC motors](https://www.amazon.com/s?k=VRV%20units%20often%20use%20DC%20motors&tag=errorcodefixe-20) |  | High-pressure switch | [Match refrigerant type](https://www.amazon.com/s?k=Match%20refrigerant%20type&tag=errorcodefixe-20) |  | Communication cable | F1/F2 — shielded type required |

> **Pro tip:** Daikin VRV systems allow fault code retrieval via the intelligent touch controller without visiting the outdoor unit. Press the Mode/Fan button combination to enter service mode and retrieve all connected unit faults.
