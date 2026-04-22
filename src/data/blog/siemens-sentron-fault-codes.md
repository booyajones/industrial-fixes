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

| [Trip Type](https://www.amazon.com/s?k=Trip%20Type&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ----------- |---------|-----------|
| L — Long Time Delay | [Overload trip](https://www.amazon.com/s?k=Overload%20trip&tag=errorcodefixe-20) | Reduce load, verify Ir setpoint |
| [S — Short Time Delay](https://www.amazon.com/s?k=S%20%E2%80%94%20Short%20Time%20Delay&tag=errorcodefixe-20) | High overcurrent below instantaneous | Check for fault, inspect load | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | I — Instantaneous | Severe short circuit | [Find and clear short before reset](https://www.amazon.com/s?k=Find%20and%20clear%20short%20before%20reset&tag=errorcodefixe-20) |  | G — Ground Fault | [Ground fault current detected](https://www.amazon.com/s?k=Ground%20fault%20current%20detected&tag=errorcodefixe-20) | Megohm test circuit, locate fault |
| [N — Neutral Protection](https://www.amazon.com/s?k=N%20%E2%80%94%20Neutral%20Protection&tag=errorcodefixe-20) | Neutral overcurrent | Check neutral conductor and loads | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | U — Undervoltage | Phase voltage low | [Check supply voltage](https://www.amazon.com/s?k=Check%20supply%20voltage&tag=errorcodefixe-20) |  | COM Error | [Communication module fault](https://www.amazon.com/s?k=Communication%20module%20fault&tag=errorcodefixe-20) | Check ETU-COM module and wiring |
| [Device Not Ready](https://www.amazon.com/s?k=Device%20Not%20Ready&tag=errorcodefixe-20) | Internal ETU fault | Power cycle and inspect module | [## Most Common Trips

### L Long Time Delay (Overload)
The load current has exceeded the Ir setpoint for longer than the allowable time-current curve allows. Check actual current using the ETU display or a clamp meter. If load is within nameplate ratings, verify the Ir setting on the ETU is appropriate.

### G Ground Fault
The 3WL and higher-specification 3VA breakers with LSIG ETUs detect ground fault current (residual current between phase conductors and neutral/ground). A ground fault trip requires locating and repairing the fault before resetting. With breaker open, use a megohm meter on load-side conductors.

### COM Error
The SENTRON PAC communication module or ETU COM attachment is not communicating. Check the ribbon cable between the ETU and COM module. Verify the PROFIBUS or Modbus address is correctly set.

## Resetting SENTRON Breakers

3WL breakers: Turn the handle to OFF, then back to ON. 3VA molded case: The handle must go fully to the TRIP position and then to OFF before ON.

The ETU display shows the last trip cause — press the "i" or RESET button to read the stored event.

## 3VA ETU Types and Features](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Trips%0A%0A%23%23%23%20L%20Long%20Time%20Delay%20(Overload)%0AThe%20load%20current%20has%20exceeded%20the%20Ir%20setpoint%20for%20longer%20than%20the%20allowable%20time-current%20curve%20allows.%20Check%20actual%20current%20using%20the%20ETU%20display%20or%20a%20clamp%20meter.%20If%20load%20is%20within%20nameplate%20ratings%2C%20verify%20the%20Ir%20setting%20on%20the%20ETU%20is%20appropriate.%0A%0A%23%23%23%20G%20Ground%20Fault%0AThe%203WL%20and%20higher-specification%203VA%20breakers%20with%20LSIG%20ETUs%20detect%20ground%20fault%20current%20(residual%20current%20between%20phase%20conductors%20and%20neutral%2Fground).%20A%20ground%20fault%20trip%20requires%20locating%20and%20repairing%20the%20fault%20before%20resetting.%20With%20breaker%20open%2C%20use%20a%20megohm%20meter%20on%20load-side%20conductors.%0A%0A%23%23%23%20COM%20Error%0AThe%20SENTRON%20PAC%20communication%20module%20or%20ETU%20COM%20attachment%20is%20not%20communicating.%20Check%20the%20ribbon%20cable%20between%20the%20ETU%20and%20COM%20module.%20Verify%20the%20PROFIBUS%20or%20Modbus%20address%20is%20correctly%20set.%0A%0A%23%23%20Resetting%20SENTRON%20Breakers%0A%0A3WL%20breakers%3A%20Turn%20the%20handle%20to%20OFF%2C%20then%20back%20to%20ON.%203VA%20molded%20case%3A%20The%20handle%20must%20go%20fully%20to%20the%20TRIP%20position%20and%20then%20to%20OFF%20before%20ON.%0A%0AThe%20ETU%20display%20shows%20the%20last%20trip%20cause%20%E2%80%94%20press%20the%20%22i%22%20or%20RESET%20button%20to%20read%20the%20stored%20event.%0A%0A%23%23%203VA%20ETU%20Types%20and%20Features&tag=errorcodefixe-20) | ETU Model | Protection | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |-----------|-----------|-------|
| [ETU10B](https://www.amazon.com/s?k=ETU10B&tag=errorcodefixe-20) | L only (basic) | Basic overload protection | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ETU25B | LSI | [Adds short-time and instantaneous](https://www.amazon.com/s?k=Adds%20short-time%20and%20instantaneous&tag=errorcodefixe-20) |  | ETU45B | [LSIG](https://www.amazon.com/s?k=LSIG&tag=errorcodefixe-20) | Full ground fault protection |
| [ETU55B](https://www.amazon.com/s?k=ETU55B&tag=errorcodefixe-20) | LSIG + Monitoring | Display, energy metering | [## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ETU module | Plug-in replacement without replacing breaker | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | COM module | Adds Modbus/PROFIBUS for monitoring | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Shunt trip | Remote trip coil accessory |

## Jump to Fix

- **L overload trip** → Measure current → Adjust load or Ir setting
- **G ground fault** → Open breaker → Megohm test → Clear fault
- **COM error** → Check ribbon cable → Verify address → Cycle power

## When to Call a Pro
Siemens-authorized electrical contractors and switchgear specialists handle ETU configuration, arc flash coordination, and 3WL maintenance.
