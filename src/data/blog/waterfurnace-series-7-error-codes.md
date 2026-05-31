---
title: "WaterFurnace Series 7 Geothermal Error Codes: Complete Guide"
description: "WaterFurnace Series 7 geothermal heat pump error codes and fault diagnostics. IntelliZone2 fault codes, causes, and technician-level fixes."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "James Rutherford"
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

| Code | Fault Description | Common Cause | Severity |
|------|------------------|--------------|---------|
| LO | Low-pressure lockout | Low refrigerant, low loop flow | Lockout |
| HI | High-pressure lockout | Dirty coil, high loop temp, overcharge | Lockout |
| FP1 | Freeze protection 1 | Low loop EWT, low refrigerant | Lockout |
| FP2 | Freeze protection 2 | Low air coil temp | Lockout |
| HA | High amperage | Compressor overloading | Lockout |
| EE | EEPROM error | Control board fault | Lockout |
| CO | Communication fault | Wiring to IntelliZone2 | Warning |
| FT | Flow fault | Low loop GPM | Warning |
| RV | Reversing valve fault | Valve or solenoid issue | Lockout |
| LT | Low loop temp warning | EWT approaching freeze protection | Warning |
| HT | High discharge temp | Refrigerant issue | Lockout |
| CC | Compressor contactor fault | Contactor or wiring | Lockout |

## Most Common Series 7 Faults

### FP1 — Freeze Protection Loop
Triggered when entering water temperature (EWT) drops near 32°F. Check loop pump operation, loop pressure, and antifreeze concentration (should be 15–20% methanol or propylene glycol for protection to 15°F).

### LO — Low-Pressure Lockout
Series 7 operates on R-410A. Low-side pressure below 40 psi triggers LO. Check loop flow rate (minimum 1.5 GPM/ton for closed loop), refrigerant charge, and TXV operation.

### HI — High-Pressure Lockout
High loop entering water temperature or refrigerant overcharge causes HI. Measure EWT — should not exceed 90°F for typical cooling season operation. Check water coil for scale buildup.

### FT — Flow Fault
The Series 7 monitors loop flow via a differential pressure switch. Check loop pump rotation, purge air from loop, and verify loop pressure (15–30 psi static).

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Aurora Base Control board | [Amazon](https://www.amazon.com/s?k=Aurora+Base+Control+board&tag=errorcodefixes-20) \| ABC — match to unit model and software version |
| IntelliZone2 thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-waterfurnace-series-7-error-codes&k=IntelliZone2+thermostat&tag=errorcodefixes-20) \| Communication interface for fault codes |
| Loop pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-waterfurnace-series-7-error-codes&k=Loop+pump&tag=errorcodefixes-20) \| Verify GPM meets unit minimum |
| TXV | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-waterfurnace-series-7-error-codes&k=TXV&tag=errorcodefixes-20) \| Match refrigerant and tonnage |
| Reversing valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-waterfurnace-series-7-error-codes&k=Reversing+valve&tag=errorcodefixes-20) \| Match unit model |
| Pressure transducer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-waterfurnace-series-7-error-codes&k=Pressure+transducer&tag=errorcodefixes-20) \| Check calibration before replacing |
> **Pro tip:** WaterFurnace Series 7 has variable speed compressor (0–100% capacity). Always view IntelliZone2 diagnostics screen for current operating pressures and EWT/LWT before diagnosing refrigerant issues.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
