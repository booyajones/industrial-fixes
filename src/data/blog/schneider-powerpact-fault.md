---
title: "Schneider PowerPact Breaker Fault Codes — Troubleshooting Guide"
description: "Schneider Electric PowerPact circuit breaker fault codes and trip indicators for H, J, L, and M-frame breakers: causes, reset procedures, and fix steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - circuit-breaker
  - schneider
  - powerpact
  - power-distribution
---

## Schneider PowerPact Fault Codes — Quick Reference

Schneider PowerPact breakers with Micrologic trip units display fault trip codes on the LCD display or trip indicator LEDs. The Micrologic 5.x, 6.x, and 7.x trip units provide detailed fault information.

| [Fault / Trip Code](https://www.amazon.com/s?k=Fault%20%2F%20Trip%20Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------------ |---------|-----------|
| Ir — Long Time Overload | [Sustained overcurrent](https://www.amazon.com/s?k=Sustained%20overcurrent&tag=errorcodefixe-20) | Reduce load or increase Ir setting |
| [Isd — Short Time Delay](https://www.amazon.com/s?k=Isd%20%E2%80%94%20Short%20Time%20Delay&tag=errorcodefixe-20) | Short circuit detected | Check for fault on load side | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Ii — Instantaneous Trip | Severe overcurrent or short circuit | [Check for dead short on load](https://www.amazon.com/s?k=Check%20for%20dead%20short%20on%20load&tag=errorcodefixe-20) |  | Ig — Ground Fault | [Ground fault current detected](https://www.amazon.com/s?k=Ground%20fault%20current%20detected&tag=errorcodefixe-20) | Locate ground fault with megohm meter |
| [Zone — ZSI Trip](https://www.amazon.com/s?k=Zone%20%E2%80%94%20ZSI%20Trip&tag=errorcodefixe-20) | Zone-selective interlock trip | Check upstream/downstream ZSI wiring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | U — Undervoltage | Voltage dropped below threshold | [Check supply voltage and connections](https://www.amazon.com/s?k=Check%20supply%20voltage%20and%20connections&tag=errorcodefixe-20) |  | OV — Overvoltage | [Voltage exceeded threshold](https://www.amazon.com/s?k=Voltage%20exceeded%20threshold&tag=errorcodefixe-20) | Check supply voltage |
| [THD — Harmonic Distortion](https://www.amazon.com/s?k=THD%20%E2%80%94%20Harmonic%20Distortion&tag=errorcodefixe-20) | Harmonics above limit (Micrologic 7) | Check loads for harmonic sources | [## Most Common Trips

### Ir Long Time Overload
The load current has exceeded the Long Time pickup (Ir) for longer than the time delay allows. This is the thermal-magnetic equivalent of a sustained overload. Check actual current with a clamp meter. If load is normal, verify the Ir setpoint is correctly configured for the load.

### Isd Short Time Delay
A high-magnitude overcurrent (but below instantaneous) caused a short-time delay trip. This is typical when a large motor starts across-the-line or when a fault develops over time. Check downstream equipment for incipient faults.

### Ig Ground Fault Trip
Micrologic 5.x and higher units have ground fault protection (LSIG). A ground fault trip requires finding and clearing the ground fault before resetting. Use a megohm meter on the load-side circuit with the breaker open and load disconnected.

## Resetting After a Trip

1. Turn the handle fully to OFF position — the breaker must click to OFF before it can be reset.
2. Hold for 2 seconds.
3. Turn to ON position.
4. If the breaker trips immediately, do NOT retry — a fault is still present.

## Micrologic Display Navigation

The Micrologic trip unit stores the last trip cause in memory. Press the MEASURE button after the trip to view the trip cause, current level, and time on the LCD display.

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Trips%0A%0A%23%23%23%20Ir%20Long%20Time%20Overload%0AThe%20load%20current%20has%20exceeded%20the%20Long%20Time%20pickup%20(Ir)%20for%20longer%20than%20the%20time%20delay%20allows.%20This%20is%20the%20thermal-magnetic%20equivalent%20of%20a%20sustained%20overload.%20Check%20actual%20current%20with%20a%20clamp%20meter.%20If%20load%20is%20normal%2C%20verify%20the%20Ir%20setpoint%20is%20correctly%20configured%20for%20the%20load.%0A%0A%23%23%23%20Isd%20Short%20Time%20Delay%0AA%20high-magnitude%20overcurrent%20(but%20below%20instantaneous)%20caused%20a%20short-time%20delay%20trip.%20This%20is%20typical%20when%20a%20large%20motor%20starts%20across-the-line%20or%20when%20a%20fault%20develops%20over%20time.%20Check%20downstream%20equipment%20for%20incipient%20faults.%0A%0A%23%23%23%20Ig%20Ground%20Fault%20Trip%0AMicrologic%205.x%20and%20higher%20units%20have%20ground%20fault%20protection%20(LSIG).%20A%20ground%20fault%20trip%20requires%20finding%20and%20clearing%20the%20ground%20fault%20before%20resetting.%20Use%20a%20megohm%20meter%20on%20the%20load-side%20circuit%20with%20the%20breaker%20open%20and%20load%20disconnected.%0A%0A%23%23%20Resetting%20After%20a%20Trip%0A%0A1.%20Turn%20the%20handle%20fully%20to%20OFF%20position%20%E2%80%94%20the%20breaker%20must%20click%20to%20OFF%20before%20it%20can%20be%20reset.%0A2.%20Hold%20for%202%20seconds.%0A3.%20Turn%20to%20ON%20position.%0A4.%20If%20the%20breaker%20trips%20immediately%2C%20do%20NOT%20retry%20%E2%80%94%20a%20fault%20is%20still%20present.%0A%0A%23%23%20Micrologic%20Display%20Navigation%0A%0AThe%20Micrologic%20trip%20unit%20stores%20the%20last%20trip%20cause%20in%20memory.%20Press%20the%20MEASURE%20button%20after%20the%20trip%20to%20view%20the%20trip%20cause%2C%20current%20level%2C%20and%20time%20on%20the%20LCD%20display.%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Micrologic trip unit | Replaceable without replacing breaker | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Auxiliary contact | Adds trip signal to SCADA | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Shunt trip coil | Remote trip capability |

## Jump to Fix

- **Ir overload** → Measure current → Reduce load or adjust setting
- **Ig ground fault** → Megohm test circuit → Locate fault → Clear before reset
- **Ii instantaneous** → Check for short circuit → Inspect load-side equipment

## When to Call a Pro
Persistent trips or damaged breaker mechanisms require a qualified electrician. Never defeat or bypass a protective trip device.
