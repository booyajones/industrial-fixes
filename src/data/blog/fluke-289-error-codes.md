---
title: "Fluke 289 Multimeter Error Codes: Complete Guide"
description: "Fluke 289 digital multimeter error codes and display messages. Error causes and technician-level troubleshooting for the Fluke 289 industrial multimeter."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - instruments
  - fluke
  - electrical
  - test-equipment
---

# Fluke 289 Multimeter Error Codes

The Fluke 289 is a professional true-RMS multimeter designed for industrial technicians. Error messages and indicators display on the primary and secondary LCD displays. Unlike older Fluke meters, the 289 has an extended error message capability.

## Fluke 289 Error Messages Table

| Display | Meaning | Cause | Action |
|---------|---------|-------|--------|
| OL | Overload | Input exceeds measurement range | Select higher range or check connections |
| FUSED | Fuse blown | Current path fuse blown | Replace 11A or 440mA fuse |
| BATT | Low battery | Battery below minimum voltage | Replace AA batteries |
| CAL ERR | Calibration error | Internal calibration failed | Return for calibration |
| ERR x | Measurement error | Context-dependent error | Check input signal and connections |
| dBm | dB milliwatt | Reference impedance mode active | Normal for dBm measurements |
| OPEN TC | Open thermocouple | TC probe not connected | Check Type K thermocouple connection |
| SHORT | Short circuit detected | Leads shorted in resistance mode | Check measurement leads |
| HOLD | Reading held | Auto-Hold or Touch Hold active | Press HOLD to release |
| SMOOTH | Averaging mode | Noise filter active | Press SMOOTH to toggle off |

## Most Common Fluke 289 Issues

### OL — Overload
OL appears when the input voltage, current, or resistance exceeds the selected range. On voltage: maximum input is 1000 VDC / 1000 VAC. On current through A jacks: maximum is 10A (11A momentary). On the mA/┬╡A jack: maximum is 440mA. If OL appears at low ranges, check that leads are in the correct jacks.

### FUSED — Fuse Blown
The Fluke 289 has two current fuses. The 10A/600V fuse protects the 10A input. The 440mA/1000V fuse protects the mA input. After a fuse blow, the display shows FUSED. Replace with Fluke-specified fuses (Fluke PN 943260 for 11A, 943261 for 440mA). Never substitute with lower-quality fuses — this is a safety-critical component.

### OPEN TC — Open Thermocouple
In temperature mode with a Type K thermocouple, OPEN TC means the thermocouple is not connected or has an open junction. Check the thermocouple lead connection at the Fluke 289 input jack. Verify thermocouple polarity (yellow = positive for Type K).

### CAL ERR — Calibration Error
Indicates the internal calibration reference has failed. This is usually caused by battery depletion during calibration, a dropped meter, or age. Return to a Fluke-authorized calibration center.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Fuse 11A/600V | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fluke-289-error-codes&k=Fuse+11A%2F600V&tag=errorcodefixes-20) \| Fluke PN 943260 — use only Fluke fuses |
| Fuse 440mA/1000V | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fluke-289-error-codes&k=Fuse+440mA%2F1000V&tag=errorcodefixes-20) \| Fluke PN 943261 |
| AA batteries | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fluke-289-error-codes&k=AA+batteries&tag=errorcodefixes-20) \| Alkaline — 6x AA |
| Test leads | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fluke-289-error-codes&k=Test+leads&tag=errorcodefixes-20) \| Fluke TL175 or TL80A |
| Type K thermocouple | [View on Amazon](https://www.amazon.com/dp/B00RJF4PYQ?ascsubtag=ecf-fluke-289-error-codes&tag=errorcodefixes-20) \| 80BK-A for HVAC temperature measurements |
> **Pro tip:** Fluke 289 has memory logging capability — up to 15,000 time-stamped readings. When troubleshooting intermittent faults, set up logging mode (MIN/MAX/AVG or Event Log) before leaving the site to capture conditions that occur after hours.
