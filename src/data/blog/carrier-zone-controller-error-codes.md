---
title: "Carrier Zone Controller Error Codes — Complete Guide"
description: "Carrier zone controller error codes for SYSTXZNSMS01 and compatible zone panels: fault codes, damper faults, thermostat errors, and step-by-step fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - zoning
---

## Carrier Zone Controller Error Codes — Quick Reference

Carrier zone controllers (models SYSTXZNSMS01, SYSTXZNCC1) manage multi-zone HVAC systems by controlling damper actuators and coordinating with zone thermostats. They work with Carrier Infinity and Performance series equipment. Fault codes appear on the Infinity System Control display or on the zone controller's LED indicator.

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| ZN1 FAULT | Zone 1 communication error | Check zone 1 thermostat wiring |
| [ZN2–ZN8 FAULT](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=ZN2%E2%80%93ZN8+FAULT&tag=errorcodefixes-20) | Zone 2–8 communication errors | Check individual zone wiring |
| [DAMP FAULT](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=DAMP+FAULT&tag=errorcodefixes-20) | Damper actuator fault | Test actuator; check wiring |
| [BYPASS FAULT](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=BYPASS+FAULT&tag=errorcodefixes-20) | Bypass damper not responding | Inspect bypass actuator and duct |
| [EQUIP FAULT](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=EQUIP+FAULT&tag=errorcodefixes-20) | Equipment communication fault | Check Infinity system bus wiring |
| [POWER FAULT](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=POWER+FAULT&tag=errorcodefixes-20) | 24VAC power supply issue | Verify transformer size and output |
| [SENSOR FAULT](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=SENSOR+FAULT&tag=errorcodefixes-20) | Zone temperature sensor error | Replace sensor or thermostat |
| [COMM LOSS](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=COMM+LOSS&tag=errorcodefixes-20) | Infinity system bus communication lost | Check data bus wiring; reboot system |
| [CONFIG ERR](https://www.amazon.com/s?ascsubtag=ecf-carrier-zone-controller-error-codes&k=CONFIG+ERR&tag=errorcodefixes-20) | Zone configuration mismatch | Reconfigure zone count in setup menu |
| E4 | System lockout — multiple faults | Cycle power; investigate root faults |

## Most Common Faults

### ZN FAULT — Zone Communication Error
Zone faults occur when the zone controller loses contact with a thermostat on a specific zone. The Carrier Infinity system uses a proprietary three-wire communication bus (in addition to 24VAC power). Check that the communication wires (typically orange and blue in Infinity wiring) are securely connected at both the thermostat and the zone controller terminal block. A broken wire or poor connection will trigger a persistent zone fault.

### DAMP FAULT — Damper Actuator Failure
Zone dampers on Carrier systems use 24VAC spring-return or motorized actuators. When the controller commands a damper to change position and doesn't receive position feedback, it logs a damper fault. Locate the faulted zone's damper in the ductwork, inspect the actuator wiring, and manually verify the damper blade moves freely. Apply 24VAC directly to the actuator to test it independent of the controller.

### BYPASS FAULT — Pressure Relief Damper
The bypass damper protects the equipment from over-pressurization when most zones are closed. A bypass fault requires immediate attention — without a functioning bypass, high static pressure can trip the furnace's limit switch repeatedly. Test the bypass actuator by applying 24VAC directly to its terminals. If the damper blade is stuck, it may be jammed by debris or a failing actuator shaft.

### COMM LOSS — Infinity Bus Communication
The Carrier Infinity system uses a proprietary data bus to allow the thermostat, zone controller, furnace, and air conditioner to communicate. A COMM LOSS fault means the bus has been interrupted. Inspect the bus wiring connections at every device on the bus — furnace, air handler, outdoor unit, and zone controller. The data bus wires must be connected in a continuous daisy-chain, not star-wired.

### EQUIP FAULT — Equipment Communication
The zone controller is not receiving responses from the furnace or air handler. This can occur if the Infinity control board in the furnace has faulted, if the bus wiring to the furnace is broken, or if the furnace is powered off. Check the furnace LED for its own fault codes first before diagnosing the zone controller.

## Wiring and Configuration Notes

- Carrier zone controllers require Infinity-compatible thermostats (HAC-ZT-2) or compatible Infinity T-stats
- Data bus wiring must be low-voltage shielded wire — do not run alongside line-voltage wires
- Maximum zone controller bus length is 500 feet
- Bypass damper size must be correctly sized to handle full system airflow

## When to Call a Pro
Carrier Infinity zone systems are complex communicating systems. COMM LOSS and EQUIP FAULT codes that persist after wiring checks require a Carrier-certified technician with Infinity diagnostic tools.
