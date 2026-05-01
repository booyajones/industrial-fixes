---
title: "Carrier Geothermal Heat Pump Error Codes Guide"
description: "Complete guide to Carrier geothermal heat pump error codes. Covers Infinity and Performance series fault codes, diagnostic steps, and technician fixes."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - geothermal
  - heat-pump
---

# Carrier Geothermal Heat Pump Error Codes: Complete Guide

Carrier geothermal heat pumps (Infinity GHP and Performance series) communicate faults via the Infinity system control or the on-board diagnostic LED. This guide covers all common Carrier geothermal fault codes.

## Carrier Geothermal Fault Code Table

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| 1 | Low-pressure lockout | Low refrigerant, low airflow, low loop flow |
| 2 | High-pressure lockout | High loop temp, dirty coil, overcharge |
| 3 | Freeze protection trip | Low loop temp, low water flow |
| 4 | Condensate overflow | Clogged condensate drain |
| 5 | High discharge temperature | Low refrigerant, restricted TXV |
| 6 | Compressor protection — high amp | Locked rotor, low voltage |
| 7 | Compressor protection — low voltage | Check supply voltage |
| 11 | Freeze stat fault | Loop antifreeze concentration low |
| 12 | Low ambient lockout | Ambient below unit minimum |
| 13 | Coax (water coil) freeze protection | Low loop water flow or temperature |
| 21 | ECM blower fault | Failed ECM motor or module |
| 22 | Communication fault | Wiring between Infinity control and unit |
| 24 | Control board fault | Replace control board |
| 31 | Refrigerant circuit fault | Pressure switch or refrigerant issue |
| 33 | Lockout — manual reset required | Multiple faults — identify root cause |
| 41 | Leaving water temperature fault | Water sensor issue |
| 42 | Entering water temperature fault | Water sensor issue |

## Most Common Carrier Geothermal Faults

### Code 1 — Low-Pressure Lockout
1. Check air filter and blower operation
2. Check loop pump operation and flow rate (minimum 1.5 GPM/ton)
3. Check entering water temperature
4. Check refrigerant charge with gauges

### Code 2 — High-Pressure Lockout
In cooling: high loop water temperature is the primary cause. Check EWT — should be below 85°F for most Carrier geothermal units.

In heating: dirty air coil, failed blower, or airflow restriction.

### Code 3 — Freeze Protection
Loop water temperature is too low, or antifreeze concentration is insufficient. Check:
- Propylene glycol concentration (should be 20–25% for most climates)
- Loop pump operation
- EWT — below 25°F triggers freeze protection on most models

### Code 22 — Communication Fault
Carrier Infinity geothermal units communicate via the Infinity bus. Check:
- All control wire connections at the unit and thermostat
- Infinity control for error messages
- Polarity of the communication wires

### Code 21 — ECM Blower Fault
ECM (variable-speed) motors fail as a module or the motor itself. Test:
- Supply voltage to the ECM module
- Control signal from the control board
- Replace ECM module first (lower cost) before replacing full motor

## Carrier Geothermal Parts Reference

| Part | Notes |
|---|---|
| [Low/high pressure switch](https://www.amazon.com/dp/B013IHQ8CU?tag=errorcodefixes-20) | Match refrigerant type and trip pressure |
| [TXV assembly](https://www.amazon.com/s?k=TXV+assembly&tag=errorcodefixes-20) | Model-specific — match refrigerant and capacity |
| [ECM blower motor](https://www.amazon.com/s?k=ECM+blower+motor&tag=errorcodefixes-20) | Match HP and model — Carrier GHP specific |
| [Loop pump](https://www.amazon.com/s?k=Loop+pump&tag=errorcodefixes-20) | Grundfos or Bell & Gossett — match GPM |
| [Freeze stat](https://www.amazon.com/s?k=Freeze+stat&tag=errorcodefixes-20) | Check setpoint — typically 30°F |
| [Water temperature sensor](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) | 10K thermistor — check resistance curve |

> **Pro tip:** Carrier Infinity geothermal units store fault history in the Infinity control. Navigate to System > Advanced > Fault History to view timestamped fault records.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
