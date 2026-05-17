---
title: "Basler Electric Relay Fault Codes — BE1-11g / BE1-CDS Guide"
description: "Basler Electric protective relay fault codes for BE1-11g generator relay and BE1-CDS differential protection: trip indicators, alarms, and troubleshooting."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - protective-relay
  - basler
  - power-distribution
  - generator
---

## Basler Electric Relay Fault Codes — Quick Reference

Basler Electric relays (BE1-11g, BE1-CDS, BE1-GPS, and DECS excitation control) record trip events and generate alarms via front-panel LEDs, the display, and Modbus/DNP3 communications.

| [Element](https://www.amazon.com/s?i=industrial&k=Element&tag=errorcodefixes-20) | Function | Common Cause |
|---------|---------|-------------|
| [51V — Voltage-Restrained OC](https://www.amazon.com/s?i=industrial&k=51V+%E2%80%94+Voltage-Restrained+OC&tag=errorcodefixes-20) | Overcurrent with voltage constraint | Fault during voltage sag |
| [40 — Loss of Excitation](https://www.amazon.com/s?i=industrial&k=40+%E2%80%94+Loss+of+Excitation&tag=errorcodefixes-20) | Generator field loss | AVR failure or field winding open |
| [81O/U — Over/Underfrequency](https://www.amazon.com/s?i=industrial&k=81O%2FU+%E2%80%94+Over%2FUnderfrequency&tag=errorcodefixes-20) | Frequency out of range | Speed governor problem |
| [27 — Undervoltage](https://www.amazon.com/s?i=industrial&k=27+%E2%80%94+Undervoltage&tag=errorcodefixes-20) | Voltage below setpoint | Generator or supply problem |
| [59 — Overvoltage](https://www.amazon.com/s?i=industrial&k=59+%E2%80%94+Overvoltage&tag=errorcodefixes-20) | Voltage above setpoint | AVR or regulator fault |
| [32 — Reverse Power](https://www.amazon.com/s?i=industrial&k=32+%E2%80%94+Reverse+Power&tag=errorcodefixes-20) | Real power flowing backward | Engine failure or backfeed |
| [87G — Generator Differential](https://www.amazon.com/s?i=industrial&k=87G+%E2%80%94+Generator+Differential&tag=errorcodefixes-20) | Internal generator fault | Winding fault |
| [46 — Neg Sequence](https://www.amazon.com/s?i=industrial&k=46+%E2%80%94+Neg+Sequence&tag=errorcodefixes-20) | Phase unbalance | Unbalanced load or open phase |

## Most Common Faults

### Element 40 — Loss of Excitation
The generator's field excitation has been lost or reduced below the pickup threshold. Common causes: AVR (automatic voltage regulator) failure, field rheostat issue, or field winding open circuit. The relay typically trips the generator offline to protect it from absorbing reactive power from the system (motoring).

### Element 32 — Reverse Power
The generator prime mover (engine or turbine) is not producing enough power and the generator begins motoring — taking real power from the bus. This indicates engine or governor failure. The 32 element trips the breaker to prevent damage.

### Element 81 — Over/Underfrequency
The generator speed is outside the acceptable frequency window. Check governor operation and engine/turbine speed control. Underfrequency during load pickup may indicate the engine is overspeeded by load.

## Reading Basler Events

Access via BESTCOMS software (PC to relay via RS-232 or Ethernet):
- Event log shows last 64 events with element, current, voltage, and timestamp
- Oscillography captures last several seconds of waveform data
- Front-panel LED indicators light to indicate which element tripped

## DECS (Digital Excitation Control System) Alarms

Basler DECS-100/200/250 also generate alarms:
- **Generator Overcurrent** — Field current too high
- **Loss of Sensing** — PT fuse blown or sensing circuit open
- **Mode Alarm** — Operating mode changed unexpectedly

## Jump to Fix

- **Loss of excitation (40)** → Check AVR → Check field circuit continuity → Inspect exciter
- **Reverse power (32)** → Check engine/governor → Confirm real power direction
- **Over/underfrequency (81)** → Check governor operation → Verify speed feedback

## When to Call a Pro
Basler provides technical support and application engineers. Generator protection settings require a power systems engineer to coordinate with the system.
