---
title: "FLIR T620 Thermal Camera Error Codes: Complete Guide"
description: "FLIR T620 thermal imaging camera error codes and fault messages. Error causes and technician-level troubleshooting for industrial thermography."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - instruments
  - flir
  - thermography
  - test-equipment
---

# FLIR T620 Thermal Camera Error Codes

The FLIR T620 is a professional thermal imaging camera with a 640×480 uncooled microbolometer detector. Error messages display on the camera LCD or in the FLIR Tools software. Most errors relate to calibration, communication, or detector issues.

## FLIR T620 Error Messages Table

| [Message](https://www.amazon.com/s?k=Message&tag=errorcodefixe-20) | Meaning | Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |---------|---------|-------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | NUC in progress | Flat field correction | [Automatic shutter calibration](https://www.amazon.com/s?k=Automatic%20shutter%20calibration&tag=errorcodefixe-20) | Normal — wait for completion |
| [Battery low](https://www.amazon.com/s?k=Battery%20low&tag=errorcodefixe-20) | Low battery | Battery depleted | [Replace or charge battery](https://www.amazon.com/s?k=Replace%20or%20charge%20battery&tag=errorcodefixe-20) |  | SD card error | [Memory card fault](https://www.amazon.com/s?k=Memory%20card%20fault&tag=errorcodefixe-20) | Corrupt or incompatible card | Format or replace SD card | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Overtemp | Camera overtemperature | [High ambient temperature](https://www.amazon.com/s?k=High%20ambient%20temperature&tag=errorcodefixe-20) | Allow camera to cool |
| [USB comm error](https://www.amazon.com/s?k=USB%20comm%20error&tag=errorcodefixe-20) | Communication failure | USB driver or cable issue | [Check USB cable and drivers](https://www.amazon.com/s?k=Check%20USB%20cable%20and%20drivers&tag=errorcodefixe-20) |  | Image corrupt | [File system error](https://www.amazon.com/s?k=File%20system%20error&tag=errorcodefixe-20) | Corrupt image file | Delete file, check SD card | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Focus error | Autofocus fault | [Dirty lens or close range](https://www.amazon.com/s?k=Dirty%20lens%20or%20close%20range&tag=errorcodefixe-20) | Clean lens, check focus mode |
| [Detector fault](https://www.amazon.com/s?k=Detector%20fault&tag=errorcodefixe-20) | Detector initialization | Detector or PCB failure | [Contact FLIR service](https://www.amazon.com/s?k=Contact%20FLIR%20service&tag=errorcodefixe-20) |  | FFC failed | [Flat-field correction fail](https://www.amazon.com/s?k=Flat-field%20correction%20fail&tag=errorcodefixe-20) | Shutter mechanism fault | Return for service | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | GPS error | GPS module fault | [GPS antenna issue](https://www.amazon.com/s?k=GPS%20antenna%20issue&tag=errorcodefixe-20) | Check GPS settings |

## Most Common FLIR T620 Issues

### NUC In Progress
The T620 performs automatic Non-Uniformity Correction (NUC) using an internal shutter mechanism. This is normal operation and takes 1–3 seconds. If the camera performs NUC excessively, it may indicate rapid ambient temperature changes. Allow the camera to reach thermal equilibrium before beginning thermographic surveys.

### Battery Low
The T620 uses a 3.7V Li-ion smart battery (FLIR T197771 or equivalent). The battery charge indicator shows remaining percentage. In cold weather, battery performance decreases significantly — carry a spare battery and keep it warm until needed.

### SD Card Error
The T620 supports SDHC cards up to 32GB (FAT32 format). SDXC cards are not supported. If an SD card error occurs, format the card in-camera via Settings → Storage → Format Card. If errors persist, replace the card.

### Detector Fault
A detector fault indicates a problem with the microbolometer array or its control PCB. This requires factory service. Do not attempt to disassemble the camera — the detector requires a clean room environment.

### FFC Failed — Flat Field Correction
If the internal shutter mechanism fails, the camera cannot perform NUC. Symptoms include persistent fixed-pattern noise on the image. The shutter is a mechanical component that wears with use. Contact FLIR for shutter replacement.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| [Battery pack](https://www.amazon.com/s?k=Battery%20pack&tag=errorcodefixe-20) | FLIR T197771 or compatible |
| [Battery charger](https://www.amazon.com/s?k=Battery%20charger&tag=errorcodefixe-20) | FLIR ACC-T197773 |
| [SD card](https://www.amazon.com/s?k=SD%20card&tag=errorcodefixe-20) | Class 10 SDHC up to 32GB, FAT32 |
| [Lens cleaning kit](https://www.amazon.com/s?k=Lens%20cleaning%20kit&tag=errorcodefixe-20) | Dry optical lens tissue only |
| [USB cable](https://www.amazon.com/s?k=USB%20cable&tag=errorcodefixe-20) | Mini-USB type B |

> **Pro tip:** FLIR T620 calibration is typically factory-verified annually. Keep calibration certificates current for compliance with industrial thermography standards (ISO 18436-7, ASNT TC-1A). Calibration expiry appears in FLIR Tools under camera properties.
