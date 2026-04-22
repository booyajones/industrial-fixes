---
title: "Trane ComfortLink II Error Codes — Common Faults and Fixes"
description: "Guide to Trane ComfortLink II communicating system error codes, what each fault means, and how to diagnose and fix the most common problems."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane ComfortLink II Error Codes — What They Mean

Trane's ComfortLink II is a proprietary communicating system that links the thermostat, indoor unit, and outdoor unit over a two-wire communication bus. Error codes appear on the ComfortLink II thermostat display under the Service menu. Unlike older flash-code Trane furnaces, the ComfortLink II provides descriptive alphanumeric codes that pinpoint which component reported the fault and what type of failure occurred. The indoor and outdoor units each log their own codes.

[Jump to Fix](#fix)

## Most Common ComfortLink II Error Codes

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Component | Meaning | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-----------|---------|
| 79 | [Outdoor unit](https://www.amazon.com/s?k=Outdoor%20unit&tag=errorcodefixe-20) | Communication loss between outdoor and indoor units |
| [126](https://www.amazon.com/s?k=126&tag=errorcodefixe-20) | Indoor unit | Pressure switch open — inducer fault | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 127 | Indoor unit | [Pressure switch stuck closed](https://www.amazon.com/s?k=Pressure%20switch%20stuck%20closed&tag=errorcodefixe-20) |  | 128 | [Indoor unit](https://www.amazon.com/s?k=Indoor%20unit&tag=errorcodefixe-20) | Ignition failure |
| [174](https://www.amazon.com/s?k=174&tag=errorcodefixe-20) | Outdoor unit | High discharge temperature | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 178 | Outdoor unit | [Low pressure lockout](https://www.amazon.com/s?k=Low%20pressure%20lockout&tag=errorcodefixe-20) |  | 179 | [Outdoor unit](https://www.amazon.com/s?k=Outdoor%20unit&tag=errorcodefixe-20) | High pressure lockout |
| [551](https://www.amazon.com/s?k=551&tag=errorcodefixe-20) | System | ComfortLink thermostat communication fault | [## Common Causes

- **Code 79 — Communication loss** — The most frequent ComfortLink II complaint. Caused by loose wiring at the bus terminals (usually at the air handler or outdoor unit), a failed outdoor control board, or a failed thermostat.
- **Code 126 — Pressure switch open** — Same root causes as any inducer fault: blocked condensate drain, cracked pressure switch hose, failed inducer motor capacitor, or blocked flue.
- **Code 128 — Ignition failure** — Cracked hot surface ignitor, dirty flame sensor, low gas pressure, or failed gas valve.
- **Code 178/179 — Pressure lockouts** — Low or high refrigerant charge, dirty coil, failed fan, or refrigerant flow restriction. Requires gauges to distinguish the root cause.
- **Code 551 — Thermostat fault** — ComfortLink II thermostat has lost communication with the system equipment. Usually a wiring issue or a failed thermostat display unit.

## Step-by-Step Fix {#fix}

1. **Access the fault log** — On the ComfortLink II thermostat, press Menu > Service > Equipment Faults. Record all active and historical codes with timestamps. Intermittent codes (appearing only in cold or hot weather) point to refrigerant or pressure issues; persistent codes point to wiring or board failures.
2. **For Code 79** — Inspect both wires of the communication bus at the outdoor unit, the air handler/furnace, and the thermostat subbase. All connections must be tight and corrosion-free. Power cycle both units (30-second wait) after confirming wiring.
3. **For Code 126** — Check the condensate trap and drain for blockage first (pour water in, confirm flow). Then trace pressure switch hoses for cracks. Test the inducer motor for correct speed and the capacitor for correct µF value.
4. **For Code 128** — Inspect the hot surface ignitor for cracks; test resistance (40–75 ohms when cold). Clean the flame sensor rod with fine steel wool. Verify gas pressure at the manifold (natural gas: 3.5" W.C. minimum outlet pressure).
5. **For Codes 178/179** — Connect manifold gauges and compare suction/discharge pressures to the unit's pressure-temperature chart. Dirty condenser coil is the first thing to address for high pressure codes; check refrigerant charge last.
6. **Clear the fault and retest** — After repairs, clear faults from the Service menu and run a full heating or cooling cycle. Confirm the code does not return.

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Common%20Causes%0A%0A-%20**Code%2079%20%E2%80%94%20Communication%20loss**%20%E2%80%94%20The%20most%20frequent%20ComfortLink%20II%20complaint.%20Caused%20by%20loose%20wiring%20at%20the%20bus%20terminals%20(usually%20at%20the%20air%20handler%20or%20outdoor%20unit)%2C%20a%20failed%20outdoor%20control%20board%2C%20or%20a%20failed%20thermostat.%0A-%20**Code%20126%20%E2%80%94%20Pressure%20switch%20open**%20%E2%80%94%20Same%20root%20causes%20as%20any%20inducer%20fault%3A%20blocked%20condensate%20drain%2C%20cracked%20pressure%20switch%20hose%2C%20failed%20inducer%20motor%20capacitor%2C%20or%20blocked%20flue.%0A-%20**Code%20128%20%E2%80%94%20Ignition%20failure**%20%E2%80%94%20Cracked%20hot%20surface%20ignitor%2C%20dirty%20flame%20sensor%2C%20low%20gas%20pressure%2C%20or%20failed%20gas%20valve.%0A-%20**Code%20178%2F179%20%E2%80%94%20Pressure%20lockouts**%20%E2%80%94%20Low%20or%20high%20refrigerant%20charge%2C%20dirty%20coil%2C%20failed%20fan%2C%20or%20refrigerant%20flow%20restriction.%20Requires%20gauges%20to%20distinguish%20the%20root%20cause.%0A-%20**Code%20551%20%E2%80%94%20Thermostat%20fault**%20%E2%80%94%20ComfortLink%20II%20thermostat%20has%20lost%20communication%20with%20the%20system%20equipment.%20Usually%20a%20wiring%20issue%20or%20a%20failed%20thermostat%20display%20unit.%0A%0A%23%23%20Step-by-Step%20Fix%20%7B%23fix%7D%0A%0A1.%20**Access%20the%20fault%20log**%20%E2%80%94%20On%20the%20ComfortLink%20II%20thermostat%2C%20press%20Menu%20%3E%20Service%20%3E%20Equipment%20Faults.%20Record%20all%20active%20and%20historical%20codes%20with%20timestamps.%20Intermittent%20codes%20(appearing%20only%20in%20cold%20or%20hot%20weather)%20point%20to%20refrigerant%20or%20pressure%20issues%3B%20persistent%20codes%20point%20to%20wiring%20or%20board%20failures.%0A2.%20**For%20Code%2079**%20%E2%80%94%20Inspect%20both%20wires%20of%20the%20communication%20bus%20at%20the%20outdoor%20unit%2C%20the%20air%20handler%2Ffurnace%2C%20and%20the%20thermostat%20subbase.%20All%20connections%20must%20be%20tight%20and%20corrosion-free.%20Power%20cycle%20both%20units%20(30-second%20wait)%20after%20confirming%20wiring.%0A3.%20**For%20Code%20126**%20%E2%80%94%20Check%20the%20condensate%20trap%20and%20drain%20for%20blockage%20first%20(pour%20water%20in%2C%20confirm%20flow).%20Then%20trace%20pressure%20switch%20hoses%20for%20cracks.%20Test%20the%20inducer%20motor%20for%20correct%20speed%20and%20the%20capacitor%20for%20correct%20%C2%B5F%20value.%0A4.%20**For%20Code%20128**%20%E2%80%94%20Inspect%20the%20hot%20surface%20ignitor%20for%20cracks%3B%20test%20resistance%20(40%E2%80%9375%20ohms%20when%20cold).%20Clean%20the%20flame%20sensor%20rod%20with%20fine%20steel%20wool.%20Verify%20gas%20pressure%20at%20the%20manifold%20(natural%20gas%3A%203.5%22%20W.C.%20minimum%20outlet%20pressure).%0A5.%20**For%20Codes%20178%2F179**%20%E2%80%94%20Connect%20manifold%20gauges%20and%20compare%20suction%2Fdischarge%20pressures%20to%20the%20unit's%20pressure-temperature%20chart.%20Dirty%20condenser%20coil%20is%20the%20first%20thing%20to%20address%20for%20high%20pressure%20codes%3B%20check%20refrigerant%20charge%20last.%0A6.%20**Clear%20the%20fault%20and%20retest**%20%E2%80%94%20After%20repairs%2C%20clear%20faults%20from%20the%20Service%20menu%20and%20run%20a%20full%20heating%20or%20cooling%20cycle.%20Confirm%20the%20code%20does%20not%20return.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ComfortLink II thermostat | For persistent Code 551 after wiring confirmed | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Outdoor communicating control board | For persistent Code 79 with good wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hot surface ignitor | Most common Code 128 fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Pressure switch | For Code 126 that returns after drain and hose check | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Condenser fan motor / capacitor | For Code 179 with clean coil |

## When to Call a Pro

ComfortLink II refrigerant work (Codes 178/179) requires EPA 608 certification and access to Trane's HVAC Pro app for system commissioning. Trane's variable-speed outdoor units also use inverter-driven compressors that require specialized diagnostics — standard clamp meters and multimeters don't give valid readings on the variable-frequency output side of the drive.
