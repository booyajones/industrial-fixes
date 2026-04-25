---
title: "Carrier Infinity System Communication Error Codes — Complete Guide"
description: "Carrier Infinity communicating system error codes explained. Learn how to diagnose system fault, component faults, and communication bus errors on Infinity HVAC systems."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - carrier
  - infinity-system
  - hvac
  - communicating
  - error-code
---

## Carrier Infinity System Error Codes

The Carrier Infinity system is a fully communicating HVAC platform — the Infinity thermostat, furnace/air handler, and outdoor unit all talk over a proprietary 4-wire bus. Faults appear on the Infinity touch thermostat or wall control with specific codes identifying which component and what failed.

## How the Infinity System Works

All components communicate on the Infinity bus:
- **Infinity thermostat** (SYSTXCCITC01-B, SYSTXCCWIC01-B) — system controller
- **Gas furnace** (58MVC, 58MVP, 59MN7) — indoor heat
- **Air handler** (FV4C, FX4D) — cooling coil + ECM blower
- **Outdoor unit** (24VNA, 24ACC, 25HCC) — compressor and condenser

Any loss of communication between these devices triggers a fault code.

## Common Infinity Error Codes

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Description | Likely Cause |
|---|---|---|
| 10 | System communication error | Wiring fault or device offline |
| 11 | Thermostat communication error | Thermostat board failure |
| 12 | Indoor unit communication error | Furnace/AHU board failure |
| 13 | Outdoor unit communication error | Outdoor board failure or power loss |
| 14 | Accessory communication error | Zone controller, humidifier offline |
| 24 | Secondary voltage fuse | 3A fuse blown on indoor board |
| 31 | High-pressure limit | Outdoor unit overpressure |
| 33 | Open limit device | Indoor high-limit tripped |
| 41 | Blower motor fault | ECM motor fault (Infinity blower) |
| 45 | Control voltage lockout | Low 24V supply |
| 46 | Low outdoor ambient | System in defrost lockout |
| 47 | Low indoor ambient | Heating system fault |
| 175 | Indoor board internal fault | Replace IFC board |
| 178 | Outdoor board internal fault | Replace outdoor control board |

## Code 10/11/12/13 — Communication Faults

These are the most common Infinity codes. They indicate a device on the bus isn't responding.

### Diagnosis Steps

**Step 1 — Check power to all components.** Furnace or air handler powered on? Outdoor unit circuit breaker on? Outdoor disconnect closed?

**Step 2 — Inspect Infinity bus wiring.** The bus uses 4 wires labeled 1, 2, 3, 4 on most Carrier boards. Inspect connections at:
- Thermostat base
- Furnace/AHU control board
- Outdoor unit control board
- Any zone damper boards or accessories

Connections must be secure. Bus wires run at data signal levels — a loose wire will drop the device.

**Step 3 — Power cycle in order.** Turn off the outdoor unit at the disconnect. Turn off the furnace at the power switch. Wait 2 minutes. Restore power: furnace first, then outdoor unit, then verify thermostat shows all devices connected.

**Step 4 — Isolate the failed device.** Disconnect the outdoor unit from the bus at the furnace board. If the thermostat now shows the indoor unit normally, the outdoor unit or its bus wiring is the fault.

**Step 5 — Check for firmware updates.** Infinity systems can have firmware mismatches after component replacement. Carrier's Infinity dealer software (Infinity Dashboard) can check and update firmware for all connected components.

## Code 41 — ECM Blower Motor Fault

The Infinity system uses a variable-speed ECM (Electronically Commutated Motor) blower. Code 41 means the motor reported an internal fault.

Common causes:
- Motor winding failure (requires replacement)
- Communication error between IFC and ECM module
- Voltage spike damage

The ECM is a two-part assembly: the motor and the control module. Replacing just the module (less expensive) fixes some code 41 faults. Full motor replacement costs $400–800+.

## Code 33 — Open Limit (Overheating)

Code 33 on Infinity is the same as code 33 on standard Carrier furnaces — the high-limit switch opened because the heat exchanger overheated. Check:
- Air filter (dirty)
- Blower operation (code 41 causing this)
- Duct system restrictions

## Dealer Required for Some Codes

Codes **175** and **178** (internal board faults) and full system communication resets often require Carrier dealer software and credentials. If you've exhausted basic diagnosis, contact a Carrier Infinity-certified dealer.

## Infinity Thermostat Error Screen Navigation

Press and hold MENU on the Infinity touch thermostat. Navigate to System Info → Active Faults or Fault History. This shows all current and recent codes with timestamps — useful for intermittent faults that clear before a tech arrives.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
