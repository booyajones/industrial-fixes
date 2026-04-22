---
title: "Weil-McLain E05 Error Code — Sensor Fault"
description: "Weil-McLain E05 error means a temperature sensor fault on the boiler. Learn which sensor triggered E05, how to test it, and whether to repair or replace."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - weil-mclain
  - boiler
  - hvac
  - error-code
  - sensor
---

## Weil-McLain E05 Error — Sensor Fault

**E05 on a Weil-McLain boiler** indicates a **temperature sensor fault** — typically the supply or return water temperature sensor has failed or gone out of the expected resistance range. E05 appears on Ultra, Gold series, and CGi-style boilers with digital control boards.

## Which Sensor Triggers E05

Weil-McLain boilers use multiple NTC (negative temperature coefficient) thermistor sensors:

| [Sensor](https://www.amazon.com/s?k=Sensor&tag=errorcodefixe-20) | Location | Monitors | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| Supply sensor | [Outlet side of boiler](https://www.amazon.com/s?k=Outlet%20side%20of%20boiler&tag=errorcodefixe-20) | Water leaving boiler |
| [Return sensor](https://www.amazon.com/s?k=Return%20sensor&tag=errorcodefixe-20) | Inlet side | Water returning from system | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Flue/exhaust sensor | Exhaust vent | [Combustion gases](https://www.amazon.com/s?k=Combustion%20gases&tag=errorcodefixe-20) |  | DHW (indirect) sensor | [Hot water tank (if present)](https://www.amazon.com/s?k=Hot%20water%20tank%20(if%20present)&tag=errorcodefixe-20) | Domestic hot water temp |

E05 most commonly points to the **supply sensor** but the control board display or service manual will indicate which sensor triggered the fault.

## How to Check the Sensor

NTC thermistors change resistance with temperature. At room temperature (~70°F / 21°C), a typical Weil-McLain sensor reads:

- **10,000 ohms (10kΩ)** at 77°F (25°C)
- Higher resistance at lower temperatures
- Lower resistance at higher temperatures

**Testing procedure:**
1. Disconnect wiring from the boiler control board
2. Set multimeter to ohms (Ω)
3. Measure across the two sensor leads
4. Compare to the sensor's resistance table in the service manual
5. If reading is 0 (shorted) or OL (open circuit), replace the sensor

## What Causes Sensor Failure

- **Age** — sensors 10+ years old are common failure points
- **Water intrusion** — if the sensor well leaks, water damages the sensor element
- **Thermal cycling stress** — repeated heat/cool cycles crack the sensor housing
- **Corrosion at connector** — the Molex connector on the wiring harness corrodes, causing high resistance reading interpreted as a fault

## Common Connector Fix

Before replacing the sensor, inspect the connector at the control board and at the sensor end. Green or white corrosion on the terminals causes resistance spikes that the board reads as an open sensor.

Fix: disconnect, clean terminals with electronic contact cleaner, apply dielectric grease, reconnect. This clears E05 in a significant percentage of cases.

## Parts Reference

| Part | Weil-McLain Part # | Cost | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --- |---|---|
| Supply/return sensor (Ultra) | [383-500-332](https://www.amazon.com/s?k=383-500-332&tag=errorcodefixe-20) | $30–60 |
| [Sensor (Gold Plus)](https://www.amazon.com/s?k=Sensor%20(Gold%20Plus)&tag=errorcodefixe-20) | 383-500-239 | $25–50 | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Sensor immersion well | 381-334-234 | [$15–30](https://www.amazon.com/s?k=%2415%E2%80%9330&tag=errorcodefixe-20) |  | Control board (last resort) | [Various](https://www.amazon.com/s?k=Various&tag=errorcodefixe-20) | $200–500 |

## Related Weil-McLain Error Codes

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning |
|---|---|
| [E01](https://www.amazon.com/s?k=E01&tag=errorcodefixe-20) | High limit tripped |
| [E02](https://www.amazon.com/s?k=E02&tag=errorcodefixe-20) | Ignition failure |
| [E03](https://www.amazon.com/s?k=E03&tag=errorcodefixe-20) | Low water cutoff |
| [E04](https://www.amazon.com/s?k=E04&tag=errorcodefixe-20) | Pressure fault |
| [E05](https://www.amazon.com/s?k=E05&tag=errorcodefixe-20) | Sensor fault (this post) |
| [E06](https://www.amazon.com/s?k=E06&tag=errorcodefixe-20) | Ignition lockout |
| [E08](https://www.amazon.com/s?k=E08&tag=errorcodefixe-20) | Condensate fault |
| [E10](https://www.amazon.com/s?k=E10&tag=errorcodefixe-20) | Vent pressure fault |

## After Replacing the Sensor

After installing a new sensor, clear the fault by cycling power to the boiler. The boiler should start a normal ignition sequence within 30 seconds. If E05 returns immediately after sensor replacement, the control board's sensor input circuit may have failed — but this is uncommon. More likely, the replacement sensor is also defective or installed incorrectly.
