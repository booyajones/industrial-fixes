---
title: "Honeywell WEBs Building Controller Fault Codes - Complete Guide"
description: "Honeywell WEBs-AX and WEBs-4S building controller fault codes and alarms: communication errors, sensor faults, causes and fixes."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - honeywell
  - webs
  - bms
  - building-automation
money_part: "WEBs-4S controller"
---

## Honeywell WEBs Fault Codes - Quick Reference

Honeywell WEBs-AX and WEBs-4S supervisory controllers and field controllers (XL15B, XL10, Spyder, Sylk devices) use the Niagara Framework and appear in the Honeywell Workbench or WEBs Commissioning Tool.

| Alarm / Status | Device | Meaning | Quick Fix |
|---------------|--------|---------|-----------|
| {disabled} | Any point | Point disabled in Niagara | Re-enable via Workbench |
| {fault} | Sensor/device | Point in fault state | Check driver and wiring |
| {comm} | Field device | Communication to device lost | Check LON/BACnet wiring |
| Temp High/Low Alarm | Zone | Zone temp out of setpoint | Check HVAC equipment |
| Fan Status Fail | AHU | Fan command/status mismatch | Check fan and status input |
| Valve Fault | AHU | Actuator feedback fault | Check actuator |
| Freeze Alarm | AHU | Freezestat condition | Check heating coil |
| Override Active | Any | Point in manual override | Release override |
| Network Unreachable | WEBs | Controller cannot reach host | Check Ethernet settings |
| Database Fault | WEBs | Database corruption | Restore from backup |

## Most Common Faults

### {fault} State on Points
In Niagara/WEBs, a {fault} status means the point has a valid connection to the controller but the controller cannot read the physical input or cannot reach the downstream device. Check the driver connection status in the Workbench point browser - look for the driver's health indicator (green = ok, red = fault).

### Communication Loss to Sylk/XL10 Devices
Honeywell Sylk devices communicate over a proprietary two-wire bus. Communication faults occur when bus polarity is reversed, bus length exceeds limits, or multiple devices share the same address. Use the Honeywell Commissioning Tool to scan for devices and check addressing.

### LON Communication Fault
Older WEBs-AX systems communicate with XL controllers via LonWorks. A LON commission fault means the WEBs cannot route to the XL controller. Check the LON channel, verify the controller is commissioned (not just powered), and confirm the service pin was pressed after controller installation.

### Database Fault
WEBs supervisory controllers store application data in flash memory. A database fault after a power failure or firmware update requires restoring from a backup station (.dist file). Always export a current backup before making configuration changes.

## Parts Often Needed

| Part | Notes |
|------|-------|
| WEBs-4S controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-webs-fault-codes&k=WEBs-4S+controller&tag=errorcodefixes-20) \| Replace on hardware fault |
| XL15B field controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-webs-fault-codes&k=XL15B+field+controller&tag=errorcodefixes-20) \| Replace on hardware failure |
| Spyder controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-webs-fault-codes&k=Spyder+controller&tag=errorcodefixes-20) \| Replace on Sylk bus fault |
| Honeywell actuator (M7415) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-webs-fault-codes&k=Honeywell+actuator+%28M7415%29&tag=errorcodefixes-20) \| Replace on valve fault |
| LON network interface card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-webs-fault-codes&k=LON+network+interface+card&tag=errorcodefixes-20) \| Replace on LON fault |
## When to Call a Pro
Niagara Framework database programming, WEBs licensing issues, and LON commissioning require certified Niagara/Honeywell technicians. Incorrect configuration changes can cause entire floor or building HVAC to misbehave.

