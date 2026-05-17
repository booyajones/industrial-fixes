---
title: "Schneider PowerPact Breaker Fault Codes — Troubleshooting Guide"
description: "Schneider Electric PowerPact circuit breaker fault codes and trip indicators for H, J, L, and M-frame breakers: causes, reset procedures, and fix steps."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "Dana Kowalski"
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

| Fault / Trip Code | Meaning | Quick Fix |
|------------------|---------|-----------|
| Ir — Long Time Overload | Sustained overcurrent | Reduce load or increase Ir setting |
| Isd — Short Time Delay | Short circuit detected | Check for fault on load side |
| Ii — Instantaneous Trip | Severe overcurrent or short circuit | Check for dead short on load |
| Ig — Ground Fault | Ground fault current detected | Locate ground fault with megohm meter |
| Zone — ZSI Trip | Zone-selective interlock trip | Check upstream/downstream ZSI wiring |
| U — Undervoltage | Voltage dropped below threshold | Check supply voltage and connections |
| OV — Overvoltage | Voltage exceeded threshold | Check supply voltage |
| THD — Harmonic Distortion | Harmonics above limit (Micrologic 7) | Check loads for harmonic sources |

## Most Common Trips

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

## Parts Often Needed

| Part | Notes |
|------|-------|
| Micrologic trip unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-powerpact-fault&k=Micrologic+trip+unit&tag=errorcodefixes-20) \| Replaceable without replacing breaker |
| Auxiliary contact | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-powerpact-fault&k=Auxiliary+contact&tag=errorcodefixes-20) \| Adds trip signal to SCADA |
| Shunt trip coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-schneider-powerpact-fault&k=Shunt+trip+coil&tag=errorcodefixes-20) \| Remote trip capability |
## Jump to Fix

- **Ir overload** → Measure current → Reduce load or adjust setting
- **Ig ground fault** → Megohm test circuit → Locate fault → Clear before reset
- **Ii instantaneous** → Check for short circuit → Inspect load-side equipment

## When to Call a Pro
Persistent trips or damaged breaker mechanisms require a qualified electrician. Never defeat or bypass a protective trip device.
