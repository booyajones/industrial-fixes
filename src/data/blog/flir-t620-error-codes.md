---
title: "FLIR T620 Thermal Camera Error Codes: Complete Guide"
description: "FLIR T620 thermal imaging camera error codes and fault messages. Error causes and technician-level troubleshooting for industrial thermography."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - instruments
  - flir
  - thermography
  - test-equipment
---

# FLIR T620 Thermal Camera Error Codes

The FLIR T620 is a professional thermal imaging camera with a 640├ù480 uncooled microbolometer detector. Error messages display on the camera LCD or in the FLIR Tools software. Most errors relate to calibration, communication, or detector issues.

## FLIR T620 Error Messages Table

| Message | Meaning | Cause | Action |
|---------|---------|-------|--------|
| NUC in progress | Flat field correction | Automatic shutter calibration | Normal — wait for completion |
| Battery low | Low battery | Battery depleted | Replace or charge battery |
| SD card error | Memory card fault | Corrupt or incompatible card | Format or replace SD card |
| Overtemp | Camera overtemperature | High ambient temperature | Allow camera to cool |
| USB comm error | Communication failure | USB driver or cable issue | Check USB cable and drivers |
| Image corrupt | File system error | Corrupt image file | Delete file, check SD card |
| Focus error | Autofocus fault | Dirty lens or close range | Clean lens, check focus mode |
| Detector fault | Detector initialization | Detector or PCB failure | Contact FLIR service |
| FFC failed | Flat-field correction fail | Shutter mechanism fault | Return for service |
| GPS error | GPS module fault | GPS antenna issue | Check GPS settings |

## Most Common FLIR T620 Issues

### NUC In Progress
The T620 performs automatic Non-Uniformity Correction (NUC) using an internal shutter mechanism. This is normal operation and takes 1–3 seconds. If the camera performs NUC excessively, it may indicate rapid ambient temperature changes. Allow the camera to reach thermal equilibrium before beginning thermographic surveys.

### Battery Low
The T620 uses a 3.7V Li-ion smart battery (FLIR T197771 or equivalent). The battery charge indicator shows remaining percentage. In cold weather, battery performance decreases significantly — carry a spare battery and keep it warm until needed.

### SD Card Error
The T620 supports SDHC cards up to 32GB (FAT32 format). SDXC cards are not supported. If an SD card error occurs, format the card in-camera via Settings ΓåÆ Storage ΓåÆ Format Card. If errors persist, replace the card.

### Detector Fault
A detector fault indicates a problem with the microbolometer array or its control PCB. This requires factory service. Do not attempt to disassemble the camera — the detector requires a clean room environment.

### FFC Failed — Flat Field Correction
If the internal shutter mechanism fails, the camera cannot perform NUC. Symptoms include persistent fixed-pattern noise on the image. The shutter is a mechanical component that wears with use. Contact FLIR for shutter replacement.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Battery pack | [Amazon](https://www.amazon.com/s?k=Battery+pack&tag=errorcodefixes-20) \| FLIR T197771 or compatible |
| Battery charger | [Amazon](https://www.amazon.com/s?k=Battery+charger&tag=errorcodefixes-20) \| FLIR ACC-T197773 |
| SD card | [Amazon](https://www.amazon.com/s?k=SD+card&tag=errorcodefixes-20) \| Class 10 SDHC up to 32GB, FAT32 |
| Lens cleaning kit | [Amazon](https://www.amazon.com/s?k=Lens+cleaning+kit&tag=errorcodefixes-20) \| Dry optical lens tissue only |
| USB cable | [Amazon](https://www.amazon.com/s?k=USB+cable&tag=errorcodefixes-20) \| Mini-USB type B |
> **Pro tip:** FLIR T620 calibration is typically factory-verified annually. Keep calibration certificates current for compliance with industrial thermography standards (ISO 18436-7, ASNT TC-1A). Calibration expiry appears in FLIR Tools under camera properties.
