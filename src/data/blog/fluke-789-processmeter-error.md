---
title: "Fluke 789 ProcessMeter Error Codes: Complete Guide"
description: "Fluke 789 ProcessMeter error codes and display messages. Error causes and technician-level troubleshooting for loop calibration and process diagnostics."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - instruments
  - fluke
  - process-control
  - test-equipment
---

# Fluke 789 ProcessMeter Error Codes

The Fluke 789 ProcessMeter is a combination meter and process calibrator capable of measuring and sourcing 4–20 mA, mV, and frequency signals. It is widely used for calibrating transmitters, positioners, and I/P converters.

## Fluke 789 Error Messages Table

| [Display](https://www.amazon.com/s?k=Display&tag=errorcodefixe-20) | Meaning | Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |---------|---------|-------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | OL | Overload | [Input exceeds measurement range](https://www.amazon.com/s?k=Input%20exceeds%20measurement%20range&tag=errorcodefixe-20) | Check input signal level |
| [FUSED](https://www.amazon.com/s?k=FUSED&tag=errorcodefixe-20) | Fuse blown | Current input fuse blown | [Replace 440mA fuse](https://www.amazon.com/s?k=Replace%20440mA%20fuse&tag=errorcodefixe-20) |  | BATT | [Low battery](https://www.amazon.com/s?k=Low%20battery&tag=errorcodefixe-20) | Battery below threshold | Replace 9V battery | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ERR | Measurement error | [Signal out of range or connection issue](https://www.amazon.com/s?k=Signal%20out%20of%20range%20or%20connection%20issue&tag=errorcodefixe-20) | Check connections |
| --- | No signal | Input below minimum | [Check signal source](https://www.amazon.com/s?k=Check%20signal%20source&tag=errorcodefixe-20) |  | LOOP PWR ON | [Loop power active](https://www.amazon.com/s?k=Loop%20power%20active&tag=errorcodefixe-20) | 24 VDC loop power enabled | Normal for 2-wire transmitters | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CAL? | Calibration prompt | [Zero/span sequence initiated](https://www.amazon.com/s?k=Zero%2Fspan%20sequence%20initiated&tag=errorcodefixe-20) | Follow calibration procedure |
| [HOLD](https://www.amazon.com/s?k=HOLD&tag=errorcodefixe-20) | Hold active | Reading frozen | [Press HOLD to release](https://www.amazon.com/s?k=Press%20HOLD%20to%20release&tag=errorcodefixe-20) | ## Most Common Fluke 789 Issues

### OL — Overload in mA Mode
Maximum input for the mA measurement function is 22 mA. If a loop is shorted and current spikes, OL appears. Check the loop for short circuits before connecting the 789. Also check that leads are in the correct jacks (mA, not V).

### FUSED — Current Fuse
The 789 uses a 440mA/1000V fuse for the current input circuit. After a fuse failure, the mA measurement will read OL or 0 regardless of actual current. Replace with the specified fuse. Check loop wiring for a short before re-measurement.

### Loop Power Function
The 789 can supply 24 VDC to power a 2-wire transmitter. When LOOP PWR is on, the 789 sources current to the loop. This is normal operation. If the transmitter does not respond, check transmitter wiring and transmitter power requirements (some need 24 VDC minimum).

### MILLIAMP Source Calibration
The 789 sources 4–20 mA for calibrating current inputs on PLCs and controllers. If the sourced current is inaccurate, the 789 may require calibration. Compare the sourced output to a known-accurate reference. Annual calibration is recommended for process calibration work.

## Parts Commonly Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Fuse 440mA/1000V | [Use only Fluke-specified fuse](https://www.amazon.com/s?k=Use%20only%20Fluke-specified%20fuse&tag=errorcodefixe-20) |  | 9V battery | [Alkaline — Duracell or Energizer](https://www.amazon.com/s?k=Alkaline%20%E2%80%94%20Duracell%20or%20Energizer&tag=errorcodefixe-20) |  | Test leads | [Use category-rated leads for process work](https://www.amazon.com/s?k=Use%20category-rated%20leads%20for%20process%20work&tag=errorcodefixe-20) |  | Alligator clips | For hands-free current loop connection |

> **Pro tip:** The Fluke 789 can perform a HART transmitter check when used with the 29 Series signal injectors. When servicing 4–20 mA loops, use the LOOP PWR mode to power isolated transmitters without needing an external power supply.
