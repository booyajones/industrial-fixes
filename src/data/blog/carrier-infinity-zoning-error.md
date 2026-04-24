---
title: "Carrier Infinity Zoning System Error Codes — Complete Guide"
description: "Carrier Infinity zoning system error codes for SYSTXCCITC01 zone controller: fault messages, causes, and step-by-step troubleshooting."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - carrier
  - infinity
  - zoning
  - hvac
  - thermostat
---

## Carrier Infinity Zoning System Error Codes — Quick Reference

The Carrier Infinity Zone Controller (SYSTXCCITC01) manages multiple zones and communicates over the Infinity system bus. Errors appear on the Infinity thermostat display when the zone controller detects a fault.

| Error Code | Meaning | Quick Fix |
|-----------|---------|-----------|
| 126 | Zone controller communication lost | Check zone controller wiring and power |
| 128 | Zone controller fault | Check zone controller for alarm condition |
| 174 | Damper communication error | Check zone damper wiring and addressing |
| 175 | Damper fault | Inspect damper actuator and wiring |
| 179 | Zone sensor fault | Check zone remote temperature sensor |
| 180 | Zone controller reset | Normal after power cycle |
| 181 | System communication fault | Check Infinity bus wiring |
| 182 | Zone damper open fault | Damper not responding to open command |

## Most Common Errors

### Error 126 — Zone Controller Communication Lost
The Infinity thermostat cannot communicate with the zone controller. Check:
1. Zone controller has 24VAC power (measure at red and common terminals)
2. Infinity bus wiring (2-conductor, polarity matters on some models) is connected
3. Wiring for continuity and shorts
4. Zone controller is not in fault condition (check its LED)

### Error 174 — Damper Communication Error
The zone controller cannot communicate with a specific damper. Each Infinity-compatible zone damper has an address switch. Check:
1. Damper address switch matches the zone number
2. Wiring from zone controller to damper is intact
3. Damper actuator is powered (24VAC)

### Error 175 — Damper Fault
The zone damper actuator has detected a fault condition. This can be: the damper blade is stuck (debris or ice), the actuator motor has failed, or an internal drive fault. Inspect the damper blade physically for obstruction.

### Error 179 — Zone Sensor Fault
The remote temperature sensor for the zone is open or shorted. Check the sensor wiring at both the sensor and zone controller terminal blocks. Measure sensor resistance — a typical 10K NTC thermistor reads approximately 10,000 ohms at 77°F.

## Infinity Zone Controller LED Status

The SYSTXCCITC01 zone controller has status LEDs:
- **Green solid** — Normal operation
- **Green flashing** — Communication active
- **Amber** — Fault condition — check thermostat for error code
- **Red** — System fault

## Zone Damper Addressing

| Zone Number | Damper Address Switch |
|------------|----------------------|
| Zone 1 | Address 1 |
| Zone 2 | Address 2 |
| Zone 3 | Address 3 |
| Zone 4–8 | Addresses 4–8 |

Confirm each damper has a unique address. Duplicate addresses cause communication errors.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Infinity zone controller | [Amazon](https://www.amazon.com/s?k=Infinity+zone+controller&tag=errorcodefixes-20) \| Replace on repeated zone controller faults |
| Zone damper actuator | [Amazon](https://www.amazon.com/s?k=Zone+damper+actuator&tag=errorcodefixes-20) \| Replace on damper fault or stuck blade |
| Zone temperature sensor | [Amazon](https://www.amazon.com/s?k=Zone+temperature+sensor&tag=errorcodefixes-20) \| Replace on sensor fault |
| Infinity bus cable | [Amazon](https://www.amazon.com/s?k=Infinity+bus+cable&tag=errorcodefixes-20) \| Replace on communication errors |
## Jump to Fix

- **Error 126** → Check 24VAC at zone controller → Check bus wiring → Inspect controller LED
- **Error 174/175** → Check damper address switch → Inspect wiring → Test actuator
- **Error 179** → Check sensor resistance → Inspect wiring → Replace sensor

## When to Call a Pro
Carrier Infinity system programming and zoning configuration requires a qualified HVAC technician. Contact a Carrier authorized dealer for system diagnostics.
