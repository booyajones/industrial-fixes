---
title: "BACnet Protocol Error Codes — Complete Guide"
description: "BACnet protocol error codes, reject reasons, and abort codes for building automation systems: causes and troubleshooting steps."
pubDatetime: 2026-04-22T20:00:00Z
modDatetime: 2026-04-22T20:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - bacnet
  - building-automation
  - protocol
---

## BACnet Error Codes — Quick Reference

BACnet (Building Automation and Control Networks, ASHRAE Standard 135) defines specific error codes returned by devices in response to service requests. These appear in BACnet client software, commissioning tools, and network analyzers.

| Error Code | Class | Meaning | Quick Fix |
|-----------|-------|---------|-----------|
| UNKNOWN-OBJECT | Device | Object does not exist | Check object ID in database |
| UNKNOWN-PROPERTY | Device | Property not supported | Check device documentation |
| VALUE-OUT-OF-RANGE | Device | Write value exceeds limits | Check min/max before writing |
| NO-SPACE-TO-WRITE-PROPERTY | Device | Device memory full | Check device capacity |
| WRITE-ACCESS-DENIED | Device | Property is read-only | Check property write protection |
| DEVICE-NOT-FOUND | Network | Device not responding | Check address and network |
| TIMEOUT | Network | No response received | Check network and device |
| REJECT: UNRECOGNIZED-SERVICE | Device | Service not supported | Use supported service |
| ABORT: BUFFER-OVERFLOW | Network | Response too large | Use pagination or segmentation |
| SEGMENTATION-NOT-SUPPORTED | Device | Large transfers not supported | Read in smaller chunks |

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

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| All devices offline | Bus break or master offline | Trace cable, check master |
| Intermittent comm | Extra termination resistor | Remove extra terminators |
| One device offline | Address conflict | Scan bus, fix duplicate address |
| Slow response | High token rotation time | Reduce Max_Master setting |
| Packet errors | Baud rate mismatch | Verify all devices at same baud |

## When to Call a Pro
BACnet network design, router configuration, and integration between different BACnet implementations often require a certified BACnet professional (CBP) or integration specialist.
