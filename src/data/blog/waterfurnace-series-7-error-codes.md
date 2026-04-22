---
title: "WaterFurnace Series 7 Geothermal Error Codes: Complete Guide"
description: "WaterFurnace Series 7 geothermal heat pump error codes and fault diagnostics. IntelliZone2 fault codes, causes, and technician-level fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - waterfurnace
  - geothermal
  - heat-pump
---

# WaterFurnace Series 7 Geothermal Error Codes

WaterFurnace Series 7 units use the Aurora Base Control (ABC) board with IntelliZone2 for monitoring and diagnostics. Fault codes display on the IntelliZone2 thermostat or Aurora Web Link. Faults are categorized as warnings (unit continues) or lockouts (unit shuts down).

## Series 7 Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Fault Description | Common Cause | [Severity](https://www.amazon.com/s?k=Severity&tag=errorcodefixe-20) |  |------|------------------|--------------|---------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | LO | Low-pressure lockout | [Low refrigerant, low loop flow](https://www.amazon.com/s?k=Low%20refrigerant%2C%20low%20loop%20flow&tag=errorcodefixe-20) | Lockout |
| [HI](https://www.amazon.com/s?k=HI&tag=errorcodefixe-20) | High-pressure lockout | Dirty coil, high loop temp, overcharge | [Lockout](https://www.amazon.com/s?k=Lockout&tag=errorcodefixe-20) |  | FP1 | [Freeze protection 1](https://www.amazon.com/s?k=Freeze%20protection%201&tag=errorcodefixe-20) | Low loop EWT, low refrigerant | Lockout | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | FP2 | Freeze protection 2 | [Low air coil temp](https://www.amazon.com/s?k=Low%20air%20coil%20temp&tag=errorcodefixe-20) | Lockout |
| [HA](https://www.amazon.com/s?k=HA&tag=errorcodefixe-20) | High amperage | Compressor overloading | [Lockout](https://www.amazon.com/s?k=Lockout&tag=errorcodefixe-20) |  | EE | [EEPROM error](https://www.amazon.com/s?k=EEPROM%20error&tag=errorcodefixe-20) | Control board fault | Lockout | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CO | Communication fault | [Wiring to IntelliZone2](https://www.amazon.com/s?k=Wiring%20to%20IntelliZone2&tag=errorcodefixe-20) | Warning |
| [FT](https://www.amazon.com/s?k=FT&tag=errorcodefixe-20) | Flow fault | Low loop GPM | [Warning](https://www.amazon.com/s?k=Warning&tag=errorcodefixe-20) |  | RV | [Reversing valve fault](https://www.amazon.com/s?k=Reversing%20valve%20fault&tag=errorcodefixe-20) | Valve or solenoid issue | Lockout | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | LT | Low loop temp warning | [EWT approaching freeze protection](https://www.amazon.com/s?k=EWT%20approaching%20freeze%20protection&tag=errorcodefixe-20) | Warning |
| [HT](https://www.amazon.com/s?k=HT&tag=errorcodefixe-20) | High discharge temp | Refrigerant issue | [Lockout](https://www.amazon.com/s?k=Lockout&tag=errorcodefixe-20) |  | CC | [Compressor contactor fault](https://www.amazon.com/s?k=Compressor%20contactor%20fault&tag=errorcodefixe-20) | Contactor or wiring | Lockout | [## Most Common Series 7 Faults

### FP1 — Freeze Protection Loop
Triggered when entering water temperature (EWT) drops near 32°F. Check loop pump operation, loop pressure, and antifreeze concentration (should be 15–20% methanol or propylene glycol for protection to 15°F).

### LO — Low-Pressure Lockout
Series 7 operates on R-410A. Low-side pressure below 40 psi triggers LO. Check loop flow rate (minimum 1.5 GPM/ton for closed loop), refrigerant charge, and TXV operation.

### HI — High-Pressure Lockout
High loop entering water temperature or refrigerant overcharge causes HI. Measure EWT — should not exceed 90°F for typical cooling season operation. Check water coil for scale buildup.

### FT — Flow Fault
The Series 7 monitors loop flow via a differential pressure switch. Check loop pump rotation, purge air from loop, and verify loop pressure (15–30 psi static).

## Parts Commonly Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Series%207%20Faults%0A%0A%23%23%23%20FP1%20%E2%80%94%20Freeze%20Protection%20Loop%0ATriggered%20when%20entering%20water%20temperature%20(EWT)%20drops%20near%2032%C2%B0F.%20Check%20loop%20pump%20operation%2C%20loop%20pressure%2C%20and%20antifreeze%20concentration%20(should%20be%2015%E2%80%9320%25%20methanol%20or%20propylene%20glycol%20for%20protection%20to%2015%C2%B0F).%0A%0A%23%23%23%20LO%20%E2%80%94%20Low-Pressure%20Lockout%0ASeries%207%20operates%20on%20R-410A.%20Low-side%20pressure%20below%2040%20psi%20triggers%20LO.%20Check%20loop%20flow%20rate%20(minimum%201.5%20GPM%2Fton%20for%20closed%20loop)%2C%20refrigerant%20charge%2C%20and%20TXV%20operation.%0A%0A%23%23%23%20HI%20%E2%80%94%20High-Pressure%20Lockout%0AHigh%20loop%20entering%20water%20temperature%20or%20refrigerant%20overcharge%20causes%20HI.%20Measure%20EWT%20%E2%80%94%20should%20not%20exceed%2090%C2%B0F%20for%20typical%20cooling%20season%20operation.%20Check%20water%20coil%20for%20scale%20buildup.%0A%0A%23%23%23%20FT%20%E2%80%94%20Flow%20Fault%0AThe%20Series%207%20monitors%20loop%20flow%20via%20a%20differential%20pressure%20switch.%20Check%20loop%20pump%20rotation%2C%20purge%20air%20from%20loop%2C%20and%20verify%20loop%20pressure%20(15%E2%80%9330%20psi%20static).%0A%0A%23%23%20Parts%20Commonly%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Aurora Base Control board | ABC — match to unit model and software version | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | IntelliZone2 thermostat | Communication interface for fault codes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Loop pump | Verify GPM meets unit minimum | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | TXV | Match refrigerant and tonnage | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Reversing valve | Match unit model | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure transducer | Check calibration before replacing |

> **Pro tip:** WaterFurnace Series 7 has variable speed compressor (0–100% capacity). Always view IntelliZone2 diagnostics screen for current operating pressures and EWT/LWT before diagnosing refrigerant issues.
