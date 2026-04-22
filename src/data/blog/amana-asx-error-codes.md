---
title: "Amana ASX Air Conditioner Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Amana ASX air conditioner error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - amana
  - air-conditioner
---

## Amana ASX Air Conditioner Error Codes — What They Mean

The Amana ASX series (ASX13, ASX14, ASX16) are residential central air conditioners manufactured by Daikin (which owns both Amana and Goodman brands). The ASX uses the same outdoor control board, compressor platform, and flash-code diagnostic system as equivalent Goodman GSX units. If you have an ASX, the flash codes below apply directly — Amana and Goodman share service parts and diagnostic logic across the entire lineup.

[Jump to Fix](#fix)

## Amana ASX LED Flash Code Reference

| [Flash Sequence](https://www.amazon.com/s?k=Flash%20Sequence&tag=errorcodefixe-20) | Fault |
|---|---|
| [1 flash](https://www.amazon.com/s?k=1%20flash&tag=errorcodefixe-20) | Normal — standby |
| [2 flashes](https://www.amazon.com/s?k=2%20flashes&tag=errorcodefixe-20) | High-pressure switch open |
| [3 flashes](https://www.amazon.com/s?k=3%20flashes&tag=errorcodefixe-20) | Low-pressure switch open |
| [4 flashes](https://www.amazon.com/s?k=4%20flashes&tag=errorcodefixe-20) | Compressor protection device open (thermal overload) |
| [5 flashes](https://www.amazon.com/s?k=5%20flashes&tag=errorcodefixe-20) | Control board fault |
| [6 flashes](https://www.amazon.com/s?k=6%20flashes&tag=errorcodefixe-20) | Outdoor ambient thermistor fault |
| [7 flashes](https://www.amazon.com/s?k=7%20flashes&tag=errorcodefixe-20) | Discharge temperature thermistor fault |
| [Rapid flash](https://www.amazon.com/s?k=Rapid%20flash&tag=errorcodefixe-20) | Low voltage — check 24VAC transformer |

## Common Causes by Code

- **2 flashes — High pressure** — Fouled condenser coil is the leading cause. On Amana/Goodman units, the coil fins can be cleaned with Nu-Calgon Evap Pow'r or similar foaming cleaner — spray between the fins, let dwell, then rinse from inside-out. Also check that the fan is spinning (capacitor failure = fan stops = high pressure within minutes).
- **3 flashes — Low pressure** — Refrigerant leak or seasonal low-ambient lockout. Common leak points: service port Schrader valves (cheap to fix), flare fittings at the unit connection, and the evaporator coil inside the air handler.
- **4 flashes — Compressor protection** — The scroll compressor has an internal thermal overload that resets after 20–30 minutes. Check the dual run capacitor before assuming the compressor has failed. A capacitor that has drifted 20% low causes hard starts and thermal overload trips.
- **5 flashes — Control board** — Check the board fuse (5A glass fuse) before ordering a new board. A shorted thermostat wire (G, Y, W) can blow the fuse without damaging the board.
- **6/7 flashes — Thermistor** — Thermistor resistance should be approximately 10kΩ at 25°C (77°F). Measure across the thermistor with the unit powered down — if open circuit or shorted, replace the sensor.

## Step-by-Step Fix {#fix}

1. **Locate the LED** — Open the electrical access panel on the Amana ASX outdoor unit. The control board is mounted near the contactor. The LED flashes the fault code repeatedly until the fault is cleared or power is cycled.
2. **For 2 flashes (high pressure)** — Confirm the condenser fan is running. Use an amp clamp on the fan motor wire — compare to nameplate. Test the capacitor with a capacitor meter. If the fan is running normally, clean the coil.
3. **For 3 flashes (low pressure)** — Connect manifold gauges. A system with no refrigerant should not be operated — running a compressor without refrigerant (and the oil it carries) damages it quickly. Find and fix the leak before recharging.
4. **For 4 flashes (compressor protection)** — Wait 30 minutes after shutdown before testing. Measure both legs of supply voltage at the disconnect under load. Unbalanced voltage (more than 2% imbalance) causes overheating in scroll compressors.
5. **Clear and test** — After repairs, power up and monitor for the first cooling cycle. Confirm suction and discharge pressures are within the expected range for the ambient conditions.

## Parts Often Needed

| Part | Notes |
|---|---|
| [Dual run capacitor](https://www.amazon.com/s?k=Dual%20run%20capacitor&tag=errorcodefixe-20) | Most common ASX failure; shared compressor and fan capacitor |
| [Contactor](https://www.amazon.com/s?k=Contactor&tag=errorcodefixe-20) | 2-pole; check contact gap and coil pull-in voltage |
| [High-pressure switch](https://www.amazon.com/s?k=High-pressure%20switch&tag=errorcodefixe-20) | Spade terminals; direct swap |
| [Low-pressure switch](https://www.amazon.com/s?k=Low-pressure%20switch&tag=errorcodefixe-20) | 50 PSIG cutout for R-410A |
| [Ambient thermistor](https://www.amazon.com/s?k=Ambient%20thermistor&tag=errorcodefixe-20) | For Code 6; usually on a pigtail connector |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | For Code 5; verify fuse and transformer first |

## When to Call a Pro

Refrigerant service on the Amana ASX requires EPA 608 certification and proper manifold gauge equipment. Amana (Daikin/Goodman) offers a Lifetime Compressor Warranty on some ASX models for the original registered homeowner — check warranty status before authorizing a compressor replacement, as the part may be covered at no cost.
