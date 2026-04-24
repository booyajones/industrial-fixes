---
title: "Siemens SENTRON 3WL/3VA Fault Codes — Troubleshooting Guide"
description: "Siemens SENTRON 3WL and 3VA circuit breaker fault codes and ETU trip unit alarms: overload, short circuit, ground fault, and communication errors."
pubDatetime: 2026-04-22T21:00:00Z
modDatetime: 2026-04-22T21:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - circuit-breaker
  - siemens
  - sentron
  - power-distribution
---

## Siemens SENTRON Fault Codes — Quick Reference

Siemens SENTRON 3WL (air circuit breakers) and 3VA (molded case) breakers with ETU (Electronic Trip Unit) display fault information on the integrated or plug-in display module. Common trip categories follow the LSIG protection scheme.

| Trip Type | Meaning | Quick Fix |
|-----------|---------|-----------|
| L — Long Time Delay | Overload trip | Reduce load, verify Ir setpoint |
| S — Short Time Delay | High overcurrent below instantaneous | Check for fault, inspect load |
| I — Instantaneous | Severe short circuit | Find and clear short before reset |
| G — Ground Fault | Ground fault current detected | Megohm test circuit, locate fault |
| N — Neutral Protection | Neutral overcurrent | Check neutral conductor and loads |
| U — Undervoltage | Phase voltage low | Check supply voltage |
| COM Error | Communication module fault | Check ETU-COM module and wiring |
| Device Not Ready | Internal ETU fault | Power cycle and inspect module |

## Most Common Trips

### L Long Time Delay (Overload)
The load current has exceeded the Ir setpoint for longer than the allowable time-current curve allows. Check actual current using the ETU display or a clamp meter. If load is within nameplate ratings, verify the Ir setting on the ETU is appropriate.

### G Ground Fault
The 3WL and higher-specification 3VA breakers with LSIG ETUs detect ground fault current (residual current between phase conductors and neutral/ground). A ground fault trip requires locating and repairing the fault before resetting. With breaker open, use a megohm meter on load-side conductors.

### COM Error
The SENTRON PAC communication module or ETU COM attachment is not communicating. Check the ribbon cable between the ETU and COM module. Verify the PROFIBUS or Modbus address is correctly set.

## Resetting SENTRON Breakers

3WL breakers: Turn the handle to OFF, then back to ON. 3VA molded case: The handle must go fully to the TRIP position and then to OFF before ON.

The ETU display shows the last trip cause — press the "i" or RESET button to read the stored event.

## 3VA ETU Types and Features

| ETU Model | Protection | Notes |
|-----------|-----------|-------|
| ETU10B | L only (basic) | Basic overload protection |
| ETU25B | LSI | Adds short-time and instantaneous |
| ETU45B | LSIG | Full ground fault protection |
| ETU55B | LSIG + Monitoring | Display, energy metering |

## Parts Often Needed

| Part | Notes |
|------|-------|
| ETU module | [Amazon](https://www.amazon.com/s?k=ETU+module&tag=errorcodefixes-20) \| Plug-in replacement without replacing breaker |
| COM module | [Amazon](https://www.amazon.com/s?k=COM+module&tag=errorcodefixes-20) \| Adds Modbus/PROFIBUS for monitoring |
| Shunt trip | [Amazon](https://www.amazon.com/s?k=Shunt+trip&tag=errorcodefixes-20) \| Remote trip coil accessory |
## Jump to Fix

- **L overload trip** → Measure current → Adjust load or Ir setting
- **G ground fault** → Open breaker → Megohm test → Clear fault
- **COM error** → Check ribbon cable → Verify address → Cycle power

## When to Call a Pro
Siemens-authorized electrical contractors and switchgear specialists handle ETU configuration, arc flash coordination, and 3WL maintenance.
