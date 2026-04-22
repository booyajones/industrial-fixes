---
title: "Carel IR33 Controller Fault Codes - Complete Guide"
description: "Carel IR33 refrigeration controller fault codes and alarm codes: causes, reset procedures, and repair guidance."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - carel
  - refrigeration
  - ir33
---

## Carel IR33 Fault Codes - Quick Reference

The Carel IR33 is a widely used microprocessor controller for refrigerated display cases, cold rooms, and condensing units. It displays single-letter or alphanumeric alarm codes on the front LED display.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|-----------|
| E1 | [NTC probe 1 (air) fault - open or short](https://www.amazon.com/s?k=NTC%20probe%201%20(air)%20fault%20-%20open%20or%20short&tag=errorcodefixe-20) | Check probe wiring |
| [E2](https://www.amazon.com/s?k=E2&tag=errorcodefixe-20) | NTC probe 2 (defrost) fault - open or short | Check probe wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | E3 | NTC probe 3 fault - open or short | [Check probe wiring](https://www.amazon.com/s?k=Check%20probe%20wiring&tag=errorcodefixe-20) |  | HA | [High temperature alarm](https://www.amazon.com/s?k=High%20temperature%20alarm&tag=errorcodefixe-20) | Check equipment operation |
| [LA](https://www.amazon.com/s?k=LA&tag=errorcodefixe-20) | Low temperature alarm | Check thermostat settings | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | dA | Defrost still in progress (not fault) | [Wait for defrost to finish](https://www.amazon.com/s?k=Wait%20for%20defrost%20to%20finish&tag=errorcodefixe-20) |  | Hd | [Defrost timeout alarm](https://www.amazon.com/s?k=Defrost%20timeout%20alarm&tag=errorcodefixe-20) | Check heater and termination probe |
| [LO](https://www.amazon.com/s?k=LO&tag=errorcodefixe-20) | Continuous cycle alarm | Check temperature vs. setpoint | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | rEC | Recovering after alarm | [Normal - equipment recovering](https://www.amazon.com/s?k=Normal%20-%20equipment%20recovering&tag=errorcodefixe-20) |  | oFF | [Unit off](https://www.amazon.com/s?k=Unit%20off&tag=errorcodefixe-20) | Check power and set/reset point |

## Most Common Faults

### E1 - Air Probe Fault
The IR33 air probe is an NTC thermistor. E1 means the probe is disconnected (open circuit - reads very high resistance) or shorted (reads near zero resistance). Disconnect the probe from the IR33 terminal block and measure resistance. At room temperature (~25°C), a good NTC should read 10,000 Ohms (10K) for Carel standard NTC sensors.

Replace the probe and reconnect securely. A common failure point is the probe connector - re-crimp or replace the connector if the probe itself measures correctly.

### E2 - Defrost Termination Probe Fault
The defrost termination probe (clipped to the evaporator coil) can fail from repeated heating and cooling cycles. E2 means this probe has opened or shorted. Replace the probe and re-secure it firmly to the evaporator fin - poor contact causes premature defrost termination and temperature problems.

### Hd - Defrost Timeout
When the defrost termination probe doesn't reach the termination setpoint (typically 10–15°C) within the maximum defrost time, Hd activates. The IR33 terminates defrost by time and returns to cooling, but the evaporator may still be frosted. Check the defrost heater ohm reading - an open heater is the most common Hd cause.

### HA - High Temperature Alarm
HA fires when the display case temperature rises above the setpoint plus the high alarm differential. After ensuring the unit is cooling, check door seals, fan operation, and defrost history. If the temperature is genuinely high, confirm the refrigerant system is operating (suction and discharge pressure, compressor running).

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Carel NTC probe (NTC/S)](https://www.amazon.com/s?k=Carel%20NTC%20probe%20(NTC%2FS)&tag=errorcodefixe-20) | Replace on E1/E2/E3 |
| [Defrost heater element](https://www.amazon.com/s?k=Defrost%20heater%20element&tag=errorcodefixe-20) | Replace on Hd alarm |
| [Defrost safety thermostat](https://www.amazon.com/s?k=Defrost%20safety%20thermostat&tag=errorcodefixe-20) | Replace on Hd alarm |
| [Evaporator fan motor](https://www.amazon.com/s?k=Evaporator%20fan%20motor&tag=errorcodefixe-20) | Replace on temperature alarms |
| [IR33 controller](https://www.amazon.com/s?k=IR33%20controller&tag=errorcodefixe-20) | Replace on persistent electronics faults |

## When to Call a Pro
If defrost heating is confirmed working and high temperature persists, the problem is in the refrigeration circuit (low charge, expansion valve, compressor). This requires EPA Section 608 certification for refrigerant handling.

