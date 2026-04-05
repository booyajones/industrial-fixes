---
title: "Error Code E1 – HVAC Indoor Unit Sensor Fault"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-01-15T08:00:00Z
modDatetime: 2024-01-15T08:00:00Z
slug: hvac-e1-sensor-fault
featured: true
draft: false
tags:
  - hvac
  - sensor
  - error-codes
description: "E1 on most HVAC systems signals an indoor unit temperature sensor failure. Here's how to diagnose and fix it fast."
---

## What E1 Means

Error code **E1** on HVAC split systems (Daikin, Mitsubishi, Carrier, LG, and most OEM brands) indicates an **indoor unit return air or coil temperature sensor fault**. The control board detected an open circuit, short circuit, or reading outside acceptable range from the NTC thermistor.

## Common Causes

- Sensor connector unplugged or corroded
- Damaged sensor wire (pinched, cut, or burnt)
- Failed NTC thermistor (resistance out of spec)
- Control board failure (rare)
- Water intrusion into sensor harness

## Diagnostic Steps

1. **Power down the unit** at the breaker before touching any components.
2. Locate the indoor PCB — the sensor harness is typically a 2-wire connector labeled `T1` or `TS`.
3. Disconnect the sensor and measure resistance with a multimeter at room temperature (~77°F / 25°C). A healthy NTC thermistor reads **approximately 10kΩ at 25°C**.
4. If resistance reads `OL` (open) or `0Ω` (short), the sensor has failed and needs replacement.
5. If resistance is in spec, inspect the connector and harness for corrosion or damage. Re-seat the connector and clear the fault.
6. If fault returns after replacing sensor, suspect the control board.

## Replacement Parts

| Brand | Sensor Part # | Notes |
|---|---|---|
| Daikin | 2109283 | 15kΩ NTC |
| Mitsubishi | E22D55726 | 10kΩ NTC |
| Carrier/Bryant | HK06NB019 | 10kΩ NTC |

> **Pro tip:** Always confirm the replacement sensor's resistance curve matches the original. Mismatched sensors will throw the same E1 code even after replacement.

## Clearing the Fault

After repair, restore power and run a test cycle. Most units clear E1 automatically on the next successful sensor read. If the code persists, perform a hard reset: power off at breaker for 30 seconds, then restore.
