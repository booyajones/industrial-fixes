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

| [Error Code](https://www.amazon.com/s?k=Error%20Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|-----------|
| 126 | [Zone controller communication lost](https://www.amazon.com/s?k=Zone%20controller%20communication%20lost&tag=errorcodefixe-20) | Check zone controller wiring and power |
| [128](https://www.amazon.com/s?k=128&tag=errorcodefixe-20) | Zone controller fault | Check zone controller for alarm condition | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 174 | Damper communication error | [Check zone damper wiring and addressing](https://www.amazon.com/s?k=Check%20zone%20damper%20wiring%20and%20addressing&tag=errorcodefixe-20) |  | 175 | [Damper fault](https://www.amazon.com/s?k=Damper%20fault&tag=errorcodefixe-20) | Inspect damper actuator and wiring |
| [179](https://www.amazon.com/s?k=179&tag=errorcodefixe-20) | Zone sensor fault | Check zone remote temperature sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 180 | Zone controller reset | [Normal after power cycle](https://www.amazon.com/s?k=Normal%20after%20power%20cycle&tag=errorcodefixe-20) |  | 181 | [System communication fault](https://www.amazon.com/s?k=System%20communication%20fault&tag=errorcodefixe-20) | Check Infinity bus wiring |
| [182](https://www.amazon.com/s?k=182&tag=errorcodefixe-20) | Zone damper open fault | Damper not responding to open command | [## Most Common Errors

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

## Zone Damper Addressing](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Errors%0A%0A%23%23%23%20Error%20126%20%E2%80%94%20Zone%20Controller%20Communication%20Lost%0AThe%20Infinity%20thermostat%20cannot%20communicate%20with%20the%20zone%20controller.%20Check%3A%0A1.%20Zone%20controller%20has%2024VAC%20power%20(measure%20at%20red%20and%20common%20terminals)%0A2.%20Infinity%20bus%20wiring%20(2-conductor%2C%20polarity%20matters%20on%20some%20models)%20is%20connected%0A3.%20Wiring%20for%20continuity%20and%20shorts%0A4.%20Zone%20controller%20is%20not%20in%20fault%20condition%20(check%20its%20LED)%0A%0A%23%23%23%20Error%20174%20%E2%80%94%20Damper%20Communication%20Error%0AThe%20zone%20controller%20cannot%20communicate%20with%20a%20specific%20damper.%20Each%20Infinity-compatible%20zone%20damper%20has%20an%20address%20switch.%20Check%3A%0A1.%20Damper%20address%20switch%20matches%20the%20zone%20number%0A2.%20Wiring%20from%20zone%20controller%20to%20damper%20is%20intact%0A3.%20Damper%20actuator%20is%20powered%20(24VAC)%0A%0A%23%23%23%20Error%20175%20%E2%80%94%20Damper%20Fault%0AThe%20zone%20damper%20actuator%20has%20detected%20a%20fault%20condition.%20This%20can%20be%3A%20the%20damper%20blade%20is%20stuck%20(debris%20or%20ice)%2C%20the%20actuator%20motor%20has%20failed%2C%20or%20an%20internal%20drive%20fault.%20Inspect%20the%20damper%20blade%20physically%20for%20obstruction.%0A%0A%23%23%23%20Error%20179%20%E2%80%94%20Zone%20Sensor%20Fault%0AThe%20remote%20temperature%20sensor%20for%20the%20zone%20is%20open%20or%20shorted.%20Check%20the%20sensor%20wiring%20at%20both%20the%20sensor%20and%20zone%20controller%20terminal%20blocks.%20Measure%20sensor%20resistance%20%E2%80%94%20a%20typical%2010K%20NTC%20thermistor%20reads%20approximately%2010%2C000%20ohms%20at%2077%C2%B0F.%0A%0A%23%23%20Infinity%20Zone%20Controller%20LED%20Status%0A%0AThe%20SYSTXCCITC01%20zone%20controller%20has%20status%20LEDs%3A%0A-%20**Green%20solid**%20%E2%80%94%20Normal%20operation%0A-%20**Green%20flashing**%20%E2%80%94%20Communication%20active%0A-%20**Amber**%20%E2%80%94%20Fault%20condition%20%E2%80%94%20check%20thermostat%20for%20error%20code%0A-%20**Red**%20%E2%80%94%20System%20fault%0A%0A%23%23%20Zone%20Damper%20Addressing&tag=errorcodefixe-20) | Zone Number | Damper Address Switch | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------ |----------------------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Zone 1 | Address 1 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Zone 2 | Address 2 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Zone 3 | Address 3 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Zone 4–8 | Addresses 4–8 | [Confirm each damper has a unique address. Duplicate addresses cause communication errors.

## Parts Often Needed](https://www.amazon.com/s?k=Confirm%20each%20damper%20has%20a%20unique%20address.%20Duplicate%20addresses%20cause%20communication%20errors.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Infinity zone controller | Replace on repeated zone controller faults | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Zone damper actuator | Replace on damper fault or stuck blade | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Zone temperature sensor | Replace on sensor fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Infinity bus cable | Replace on communication errors |

## Jump to Fix

- **Error 126** → Check 24VAC at zone controller → Check bus wiring → Inspect controller LED
- **Error 174/175** → Check damper address switch → Inspect wiring → Test actuator
- **Error 179** → Check sensor resistance → Inspect wiring → Replace sensor

## When to Call a Pro
Carrier Infinity system programming and zoning configuration requires a qualified HVAC technician. Contact a Carrier authorized dealer for system diagnostics.
