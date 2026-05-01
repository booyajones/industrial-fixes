---
title: "Eaton Power Meter Fault Codes: Complete Guide"
description: "Eaton power meter fault codes and error diagnostics. IQ series and EMon-D meter faults, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Marcus Webb"
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

| Error/Code | Fault Description | Common Cause | Action |
|-----------|------------------|--------------|--------|
| CT open | Current transformer open | CT secondary disconnected | Check CT wiring immediately |
| PT fault | Potential transformer fault | PT secondary voltage absent | Check PT and wiring |
| Memory err | Data memory error | EEPROM or flash fault | Cycle power; contact Eaton |
| Comm err | Communication fault | Modbus/BACnet comm loss | Check wiring and baud rate |
| RTC fault | Real-time clock fault | Clock battery failure | Replace internal battery |
| Overrange | Input over-range | Signal above meter rating | Check CT/PT ratios |
| Setup err | Configuration error | Invalid parameter entries | Verify CT/PT ratio settings |
| Cal err | Calibration error | Internal calibration fault | Return for recalibration |
| Temp err | Temperature out of range | Meter too hot or cold | Check installation environment |
| LOG FULL | Data log full | Memory full | Download and clear log data |

## Most Common Eaton Meter Faults

### CT Open — Critical Safety Issue
An open CT secondary is dangerous — CT secondaries must never be open-circuited with the primary energized. A CT open error means the CT circuit has become disconnected. Shut down equipment before opening CT circuit. Check CT secondary wiring at the meter terminal block. Verify CT shorting blocks are not in place.

### Comm Error — Modbus/BACnet Fault
Eaton IQ meters support Modbus RTU (RS-485) and Modbus TCP/IP. Check baud rate setting matches BMS (typically 9600 or 19200 baud). Verify RS-485 wiring polarity (A+ and B-). On long runs, verify 120╬⌐ termination resistor is installed at the last device on the RS-485 bus.

### Memory Error
Power quality data logs and configuration are stored in non-volatile memory. A memory error can corrupt historical data. Download all data before cycling power. If error persists after power cycle, the meter requires factory service or replacement.

### RTC Fault
The real-time clock battery (typically a CR2032) powers the internal clock during power outages. When the battery fails, timestamps on energy data are incorrect. Replace the battery and set the clock. Note: some meters require a firmware programmer to access the RTC battery compartment.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| CT shorting blocks | [Amazon](https://www.amazon.com/s?k=CT+shorting+blocks&tag=errorcodefixes-20) \| Safety-critical — keep available for maintenance |
| RS-485 termination resistors | [Amazon](https://www.amazon.com/s?k=RS-485+termination+resistors&tag=errorcodefixes-20) \| 120╬⌐ — for Modbus network |
| CR2032 battery | [Amazon](https://www.amazon.com/s?k=CR2032+battery&tag=errorcodefixes-20) \| Internal RTC backup |
| USB-to-RS485 adapter | [Amazon](https://www.amazon.com/s?k=USB-to-RS485+adapter&tag=errorcodefixes-20) \| For meter configuration and data download |
| Replacement meter | [Amazon](https://www.amazon.com/s?k=Replacement+meter&tag=errorcodefixes-20) \| Compare meter to existing when replacing — verify register mapping |
> **Pro tip:** Eaton Power Xpert Meters support energy data export to PowerNet, EnergyAware, and third-party SCADA platforms. Always download historical demand data before replacing a meter — billing data may be required for utility reconciliation.
