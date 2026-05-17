---
title: "BACnet Protocol Error Codes - Complete Guide"
description: "BACnet protocol error codes, reject reasons, and abort codes for building automation systems: causes and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - bacnet
  - building-automation
  - protocol
---

## BACnet Error Codes - Quick Reference

BACnet (Building Automation and Control Networks, ASHRAE Standard 135) defines specific error codes returned by devices in response to service requests. These appear in BACnet client software, commissioning tools, and network analyzers.

| [Error Code](https://www.amazon.com/s?i=industrial&k=Error+Code&tag=errorcodefixes-20) | Class | Meaning | Quick Fix |
|-----------|-------|---------|-----------|
| [UNKNOWN-OBJECT](https://www.amazon.com/s?i=industrial&k=UNKNOWN-OBJECT&tag=errorcodefixes-20) | Device | Object does not exist | Check object ID in database |
| [UNKNOWN-PROPERTY](https://www.amazon.com/s?i=industrial&k=UNKNOWN-PROPERTY&tag=errorcodefixes-20) | Device | Property not supported | Check device documentation |
| [VALUE-OUT-OF-RANGE](https://www.amazon.com/s?i=industrial&k=VALUE-OUT-OF-RANGE&tag=errorcodefixes-20) | Device | Write value exceeds limits | Check min/max before writing |
| [NO-SPACE-TO-WRITE-PROPERTY](https://www.amazon.com/s?i=industrial&k=NO-SPACE-TO-WRITE-PROPERTY&tag=errorcodefixes-20) | Device | Device memory full | Check device capacity |
| [WRITE-ACCESS-DENIED](https://www.amazon.com/s?i=industrial&k=WRITE-ACCESS-DENIED&tag=errorcodefixes-20) | Device | Property is read-only | Check property write protection |
| [DEVICE-NOT-FOUND](https://www.amazon.com/s?i=industrial&k=DEVICE-NOT-FOUND&tag=errorcodefixes-20) | Network | Device not responding | Check address and network |
| [TIMEOUT](https://www.amazon.com/s?i=industrial&k=TIMEOUT&tag=errorcodefixes-20) | Network | No response received | Check network and device |
| [REJECT: UNRECOGNIZED-SERVICE](https://www.amazon.com/s?i=industrial&k=REJECT%3A+UNRECOGNIZED-SERVICE&tag=errorcodefixes-20) | Device | Service not supported | Use supported service |
| [ABORT: BUFFER-OVERFLOW](https://www.amazon.com/s?i=industrial&k=ABORT%3A+BUFFER-OVERFLOW&tag=errorcodefixes-20) | Network | Response too large | Use pagination or segmentation |
| [SEGMENTATION-NOT-SUPPORTED](https://www.amazon.com/s?i=industrial&k=SEGMENTATION-NOT-SUPPORTED&tag=errorcodefixes-20) | Device | Large transfers not supported | Read in smaller chunks |

## Most Common BACnet Errors

### UNKNOWN-OBJECT
The requesting device sent a service (ReadProperty, WriteProperty) referencing an object instance that doesn't exist in the target device. In BAS commissioning, this usually means the controller database and the supervisory controller database are out of sync. Re-commission the device to export the current object list.

### DEVICE-NOT-FOUND / Timeout
When a BACnet device stops responding, the controller logs a communication timeout. On BACnet MS/TP (RS-485), check: bus termination (120 ohm at each end only), address conflicts (two devices at same address), broken cable, and baud rate match. On BACnet IP, verify the device IP, port (UDP 47808 default), and subnet mask.

### WRITE-ACCESS-DENIED
Many BACnet properties are read-only by default. Commandable properties (like Present_Value of binary and analog outputs) require a priority array write with an appropriate priority level (1–16). Level 8 is manual override; level 16 is the default schedule. Writing to a non-commandable property returns WRITE-ACCESS-DENIED.

### ABORT: BUFFER-OVERFLOW
Large BACnet read requests (like reading an entire object list from a device with many objects) can exceed the device's buffer. Use ReadPropertyMultiple in smaller batches, or enable BACnet segmented transfers if the device supports it (check the Segmentation_Supported property).

### VALUE-OUT-OF-RANGE
BACnet devices enforce their own limits on writable properties. A setpoint controller may reject values outside 10–40°C range. Check the property's minPresValue and maxPresValue before writing.

## MS/TP Bus Troubleshooting

| [Issue](https://www.amazon.com/s?i=industrial&k=Issue&tag=errorcodefixes-20) | Likely Cause | Fix |
|-------|-------------|-----|
| [All devices offline](https://www.amazon.com/s?i=industrial&k=All+devices+offline&tag=errorcodefixes-20) | Bus break or master offline | Trace cable, check master |
| [Intermittent comm](https://www.amazon.com/s?i=industrial&k=Intermittent+comm&tag=errorcodefixes-20) | Extra termination resistor | Remove extra terminators |
| [One device offline](https://www.amazon.com/s?i=industrial&k=One+device+offline&tag=errorcodefixes-20) | Address conflict | Scan bus, fix duplicate address |
| [Slow response](https://www.amazon.com/s?i=industrial&k=Slow+response&tag=errorcodefixes-20) | High token rotation time | Reduce Max_Master setting |
| [Packet errors](https://www.amazon.com/s?i=industrial&k=Packet+errors&tag=errorcodefixes-20) | Baud rate mismatch | Verify all devices at same baud |

## When to Call a Pro
BACnet network design, router configuration, and integration between different BACnet implementations often require a certified BACnet professional (CBP) or integration specialist.

