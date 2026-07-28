---
title: "Mitsubishi FR-D700 VFD Fault Codes — Complete Diagnostic Reference"
description: "Complete guide to Mitsubishi FR-D700 VFD fault codes, causes, and step-by-step repair procedures for industrial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - mitsubishi
  - industrial
money_part: "Cooling fan"
---

## Mitsubishi FR-D700 VFD Fault Codes — What They Mean

The Mitsubishi FR-D700 is a compact inverter drive used on conveyors, small pumps, and packaging equipment. It displays fault codes directly on the built-in keypad in short alphanumeric form. The FR-D700 is reliable, but it is often installed in tight cabinets where heat, poor wiring, and abrupt parameter changes create nuisance trips.

## Mitsubishi FR-D700 Common Fault Code Reference

| Code | Meaning |
|---|---|
| OC1 | Overcurrent during acceleration |
| OC2 | Overcurrent during constant speed |
| OC3 | Overcurrent during deceleration |
| OV1 | Overvoltage during acceleration |
| OV2 | Overvoltage during run |
| OV3 | Overvoltage during deceleration |
| THT | Inverter overtemperature |
| THM | Motor thermal overload |
| UVT | Undervoltage |
| GF | Ground fault |
| OLT | Stall prevention / overload trip |
| CPU | Internal control fault |

## Common Causes by Fault

- **OC1/OC2/OC3** — Mechanical binding, bad motor cable, or acceleration/deceleration set too aggressively.
- **OV3** — Most common on fast stop commands. Extend deceleration time.
- **THT** — Dust-clogged fan path or failed internal fan.
- **THM** — Motor current above rating for too long. Check parameterized motor FLA against nameplate.
- **GF** — Insulation breakdown in motor or cable.

## Step-by-Step Fix {#fix}

1. **Capture the exact code** — Mitsubishi faults are phase-of-operation specific, so OC1 and OC3 point to different root causes.
2. **For OC faults** — Remove the load if possible and test the motor alone. Review acceleration and torque boost parameters.
3. **For OV faults** — Increase decel time. If the application requires rapid stopping, use a braking resistor if supported.
4. **For THT** — Check ambient temperature, clean the drive, and confirm fan movement.
5. **For GF** — Disconnect the motor leads and insulation test each phase to ground.

## Parts Often Needed

| Part | Notes |
|---|---|
| Cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-d700-fault-codes&k=Cooling+fan&tag=errorcodefixes-20) \| Common thermal trip cause |
| Keypad | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-d700-fault-codes&k=Keypad&tag=errorcodefixes-20) \| For damaged display/buttons |
| Replacement FR-D700 drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-d700-fault-codes&k=Replacement+FR-D700+drive&tag=errorcodefixes-20) \| For CPU faults |
| Braking resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-d700-fault-codes&k=Braking+resistor&tag=errorcodefixes-20) \| If fast stop is application-critical |
## When to Call a Pro

Persistent CPU faults or repeated GF trips with the motor disconnected usually mean internal inverter damage. Mitsubishi drive service or a qualified controls technician should evaluate before the drive is put back into production.
