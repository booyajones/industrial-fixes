---
title: "Eaton Power Meter Fault Codes: Complete Guide"
description: "Eaton power meter fault codes and error diagnostics. IQ series and EMon-D meter faults, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-04-22T23:45:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - electrical
  - eaton
  - power-quality
  - industrial
---

# Eaton Power Meter Fault Codes

Eaton power meters (IQ 300, IQ 260, Power Xpert Meter, EMon-D) are used for energy monitoring, power quality measurement, and billing. Error messages display on the meter front panel or are accessible via Modbus/BACnet registers. Error conditions affect data logging and metering accuracy.

## Eaton Power Meter Error Reference

| [Error/Code](https://www.amazon.com/s?k=Error%2FCode&tag=errorcodefixe-20) | Fault Description | Common Cause | [Action](https://www.amazon.com/s?k=Action&tag=errorcodefixe-20) |  |-----------|------------------|--------------|--------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | CT open | Current transformer open | [CT secondary disconnected](https://www.amazon.com/s?k=CT%20secondary%20disconnected&tag=errorcodefixe-20) | Check CT wiring immediately |
| [PT fault](https://www.amazon.com/s?k=PT%20fault&tag=errorcodefixe-20) | Potential transformer fault | PT secondary voltage absent | [Check PT and wiring](https://www.amazon.com/s?k=Check%20PT%20and%20wiring&tag=errorcodefixe-20) |  | Memory err | [Data memory error](https://www.amazon.com/s?k=Data%20memory%20error&tag=errorcodefixe-20) | EEPROM or flash fault | Cycle power; contact Eaton | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Comm err | Communication fault | [Modbus/BACnet comm loss](https://www.amazon.com/s?k=Modbus%2FBACnet%20comm%20loss&tag=errorcodefixe-20) | Check wiring and baud rate |
| [RTC fault](https://www.amazon.com/s?k=RTC%20fault&tag=errorcodefixe-20) | Real-time clock fault | Clock battery failure | [Replace internal battery](https://www.amazon.com/s?k=Replace%20internal%20battery&tag=errorcodefixe-20) |  | Overrange | [Input over-range](https://www.amazon.com/s?k=Input%20over-range&tag=errorcodefixe-20) | Signal above meter rating | Check CT/PT ratios | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Setup err | Configuration error | [Invalid parameter entries](https://www.amazon.com/s?k=Invalid%20parameter%20entries&tag=errorcodefixe-20) | Verify CT/PT ratio settings |
| [Cal err](https://www.amazon.com/s?k=Cal%20err&tag=errorcodefixe-20) | Calibration error | Internal calibration fault | [Return for recalibration](https://www.amazon.com/s?k=Return%20for%20recalibration&tag=errorcodefixe-20) |  | Temp err | [Temperature out of range](https://www.amazon.com/s?k=Temperature%20out%20of%20range&tag=errorcodefixe-20) | Meter too hot or cold | Check installation environment | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | LOG FULL | Data log full | [Memory full](https://www.amazon.com/s?k=Memory%20full&tag=errorcodefixe-20) | Download and clear log data |

## Most Common Eaton Meter Faults

### CT Open — Critical Safety Issue
An open CT secondary is dangerous — CT secondaries must never be open-circuited with the primary energized. A CT open error means the CT circuit has become disconnected. Shut down equipment before opening CT circuit. Check CT secondary wiring at the meter terminal block. Verify CT shorting blocks are not in place.

### Comm Error — Modbus/BACnet Fault
Eaton IQ meters support Modbus RTU (RS-485) and Modbus TCP/IP. Check baud rate setting matches BMS (typically 9600 or 19200 baud). Verify RS-485 wiring polarity (A+ and B-). On long runs, verify 120Ω termination resistor is installed at the last device on the RS-485 bus.

### Memory Error
Power quality data logs and configuration are stored in non-volatile memory. A memory error can corrupt historical data. Download all data before cycling power. If error persists after power cycle, the meter requires factory service or replacement.

### RTC Fault
The real-time clock battery (typically a CR2032) powers the internal clock during power outages. When the battery fails, timestamps on energy data are incorrect. Replace the battery and set the clock. Note: some meters require a firmware programmer to access the RTC battery compartment.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| [CT shorting blocks](https://www.amazon.com/s?k=CT%20shorting%20blocks&tag=errorcodefixe-20) | Safety-critical — keep available for maintenance |
| [RS-485 termination resistors](https://www.amazon.com/s?k=RS-485%20termination%20resistors&tag=errorcodefixe-20) | 120Ω — for Modbus network |
| [CR2032 battery](https://www.amazon.com/s?k=CR2032%20battery&tag=errorcodefixe-20) | Internal RTC backup |
| [USB-to-RS485 adapter](https://www.amazon.com/s?k=USB-to-RS485%20adapter&tag=errorcodefixe-20) | For meter configuration and data download |
| [Replacement meter](https://www.amazon.com/s?k=Replacement%20meter&tag=errorcodefixe-20) | Compare meter to existing when replacing — verify register mapping |

> **Pro tip:** Eaton Power Xpert Meters support energy data export to PowerNet, EnergyAware, and third-party SCADA platforms. Always download historical demand data before replacing a meter — billing data may be required for utility reconciliation.
