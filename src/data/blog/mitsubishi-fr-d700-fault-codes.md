---
title: "Mitsubishi FR-D700 VFD Fault Codes — Complete Diagnostic Reference"
description: "Complete guide to Mitsubishi FR-D700 VFD fault codes, causes, and step-by-step repair procedures for industrial technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - mitsubishi
  - industrial
---

## Mitsubishi FR-D700 VFD Fault Codes — What They Mean

The Mitsubishi FR-D700 is a compact inverter drive used on conveyors, small pumps, and packaging equipment. It displays fault codes directly on the built-in keypad in short alphanumeric form. The FR-D700 is reliable, but it is often installed in tight cabinets where heat, poor wiring, and abrupt parameter changes create nuisance trips.

[Jump to Fix](#fix)

## Mitsubishi FR-D700 Common Fault Code Reference

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning |
|---|---|
| [OC1](https://www.amazon.com/s?k=OC1&tag=errorcodefixe-20) | Overcurrent during acceleration |
| [OC2](https://www.amazon.com/s?k=OC2&tag=errorcodefixe-20) | Overcurrent during constant speed |
| [OC3](https://www.amazon.com/s?k=OC3&tag=errorcodefixe-20) | Overcurrent during deceleration |
| [OV1](https://www.amazon.com/s?k=OV1&tag=errorcodefixe-20) | Overvoltage during acceleration |
| [OV2](https://www.amazon.com/s?k=OV2&tag=errorcodefixe-20) | Overvoltage during run |
| [OV3](https://www.amazon.com/s?k=OV3&tag=errorcodefixe-20) | Overvoltage during deceleration |
| [THT](https://www.amazon.com/s?k=THT&tag=errorcodefixe-20) | Inverter overtemperature |
| [THM](https://www.amazon.com/s?k=THM&tag=errorcodefixe-20) | Motor thermal overload |
| [UVT](https://www.amazon.com/s?k=UVT&tag=errorcodefixe-20) | Undervoltage |
| [GF](https://www.amazon.com/s?k=GF&tag=errorcodefixe-20) | Ground fault |
| [OLT](https://www.amazon.com/s?k=OLT&tag=errorcodefixe-20) | Stall prevention / overload trip |
| [CPU](https://www.amazon.com/s?k=CPU&tag=errorcodefixe-20) | Internal control fault |

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
| [Cooling fan](https://www.amazon.com/s?k=Cooling%20fan&tag=errorcodefixe-20) | Common thermal trip cause |
| [Keypad](https://www.amazon.com/s?k=Keypad&tag=errorcodefixe-20) | For damaged display/buttons |
| [Replacement FR-D700 drive](https://www.amazon.com/s?k=Replacement%20FR-D700%20drive&tag=errorcodefixe-20) | For CPU faults |
| [Braking resistor](https://www.amazon.com/s?k=Braking%20resistor&tag=errorcodefixe-20) | If fast stop is application-critical |

## When to Call a Pro

Persistent CPU faults or repeated GF trips with the motor disconnected usually mean internal inverter damage. Mitsubishi drive service or a qualified controls technician should evaluate before the drive is put back into production.
