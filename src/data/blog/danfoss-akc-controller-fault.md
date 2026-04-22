---
title: "Danfoss AKC Controller Fault Codes - Complete Guide"
description: "Danfoss AKC refrigeration controller fault codes for supermarket showcase and cold storage: causes and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - danfoss
  - refrigeration
  - akc-controller
---

## Danfoss AKC Controller Fault Codes - Quick Reference

Danfoss AKC controllers (AKC 15, 22, 24, 55, 114, and the newer AK-CC series) manage refrigerated display cases, walk-in coolers, and rack systems. Alarms appear on the controller display and via the Danfoss AKM or ADAP-KOOL network.

| [Alarm / Code](https://www.amazon.com/s?k=Alarm%20%2F%20Code&tag=errorcodefixe-20) | Meaning | Quick Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------------- |---------|-----------|
| A1 - Temperature High | [Case temperature above alarm setpoint](https://www.amazon.com/s?k=Case%20temperature%20above%20alarm%20setpoint&tag=errorcodefixe-20) | Check defrost, door seals, fans |
| [A2 - Temperature Low](https://www.amazon.com/s?k=A2%20-%20Temperature%20Low&tag=errorcodefixe-20) | Case temp below low alarm setpoint | Check thermostat/thermistor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | A3 - Defrost Timeout | Defrost exceeded maximum time | [Check defrost heater and termination](https://www.amazon.com/s?k=Check%20defrost%20heater%20and%20termination&tag=errorcodefixe-20) |  | A4 - Sensor Fault | [Temperature sensor open or shorted](https://www.amazon.com/s?k=Temperature%20sensor%20open%20or%20shorted&tag=errorcodefixe-20) | Check sensor wiring |
| [A5 - Defrost Sensor Fault](https://www.amazon.com/s?k=A5%20-%20Defrost%20Sensor%20Fault&tag=errorcodefixe-20) | Defrost termination sensor fault | Check termination sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | A6 - Door Switch Alarm | Door open too long | [Check door and switch](https://www.amazon.com/s?k=Check%20door%20and%20switch&tag=errorcodefixe-20) |  | A7 - Communication Fault | [Network communication lost](https://www.amazon.com/s?k=Network%20communication%20lost&tag=errorcodefixe-20) | Check LonWorks/RS-485 wiring |
| [A8 - Air Sensor Fault](https://www.amazon.com/s?k=A8%20-%20Air%20Sensor%20Fault&tag=errorcodefixe-20) | Air inlet or outlet sensor fault | Check sensor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | A9 - Power Fail | Supply power was interrupted | [Normal after power outage](https://www.amazon.com/s?k=Normal%20after%20power%20outage&tag=errorcodefixe-20) |  | A10 - Controller Fault | [Internal controller error](https://www.amazon.com/s?k=Internal%20controller%20error&tag=errorcodefixe-20) | Replace controller |

## Most Common Faults

### A1 - Temperature High
Most common alarm on AKC controllers. First check if a recent defrost cycle completed normally. Ice buildup from a failed defrost blocks evaporator airflow and causes temperature rise within hours. Also check door gaskets and night curtains. If defrost is fine, suspect evaporator fan motor failure.

### A3 - Defrost Timeout
AKC controllers terminate defrost on either temperature (termination sensor reaches setpoint) or time (maximum defrost duration). A timeout means the coil didn't reach the termination setpoint within the time limit. Check the defrost heater with an ohmmeter - open heater elements are common on aging equipment. Also check the safety thermostat.

### A4 - Sensor Fault
Danfoss uses NTC (10K or 20K at 25°C depending on model) temperature sensors. A disconnected or failed sensor causes A4. Test the sensor resistance at the controller terminal. Danfoss AK sensors have a standard curve - any value below 200 Ohms or above 500K Ohms indicates failure.

### A7 - Communication Fault
AKC controllers on LonWorks or RS-485 networks alarm on communication loss. Check LonWorks cable polarity and termination - LonWorks requires twisted-pair with proper termination at each end. RS-485 requires a 120-ohm terminator at each trunk end and correct addressing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [AKC temperature sensor (NTC)](https://www.amazon.com/s?k=AKC%20temperature%20sensor%20(NTC)&tag=errorcodefixe-20) | Replace on A4/A5 fault |
| [Defrost heater element](https://www.amazon.com/s?k=Defrost%20heater%20element&tag=errorcodefixe-20) | Replace on A3 timeout |
| [Defrost safety thermostat](https://www.amazon.com/s?k=Defrost%20safety%20thermostat&tag=errorcodefixe-20) | Replace on A3 timeout |
| [Evaporator fan motor](https://www.amazon.com/s?k=Evaporator%20fan%20motor&tag=errorcodefixe-20) | Replace on temperature alarm |
| [AKC controller](https://www.amazon.com/s?k=AKC%20controller&tag=errorcodefixe-20) | Replace on A10 fault |

## When to Call a Pro
Danfoss ADAP-KOOL network configuration and AKM system management require Danfoss-trained refrigeration controls technicians. A misconfigured AKC defrost schedule can cause food safety violations.

