---
title: "Trane Heat Pump E2 Error Code — Outdoor Coil Sensor Fault"
description: "What Trane heat pump E2 means, why the outdoor coil sensor fails, and how to fix it on Trane XR, XL, and XC heat pump systems."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane Heat Pump E2 Error Code — What It Means

Trane heat pump error code **E2** typically indicates an **outdoor coil temperature sensor (thermistor) fault** — the sensor that monitors the outdoor heat exchanger temperature for defrost control has failed or is reading out of range. On Trane communicating systems (ComfortLink II), E2 may also represent a communication fault depending on the specific model and control configuration.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor coil thermistor** — The NTC thermistor clipped to the outdoor coil fins has failed, is shorted, or is open-circuit. Common failure modes: thermistor corroded at the sensing point (common in coastal or humid environments) or physically damaged by a coil cleaning.
- **Connector corrosion or loose connection** — The 2-pin connector where the thermistor plugs into the outdoor control board may have corroded pins or a loose connection.
- **Rodent or pest damage** — Wire chewing by mice or squirrels is a common cause of thermistor wiring faults in outdoor units.
- **Outdoor PCB fault** — The thermistor input on the outdoor board has failed. Diagnose after ruling out the sensor and wiring.

## Step-by-Step Fix {#fix}

1. **Turn off power** at the outdoor unit's disconnect box.
2. **Locate the outdoor coil thermistor** — on most Trane XR and XL heat pumps, the coil thermistor is a small bullet-shaped sensor clipped into the fins of the outdoor coil. Trace the wire from the sensor to where it connects to the outdoor control board.
3. **Inspect for visible damage** — look for chewed wires, kinked insulation, or corrosion at the sensor tip (often shows as white or green powder on the metal probe).
4. **Test thermistor resistance** — disconnect the thermistor from the board and measure resistance with a multimeter. At 70°F, a typical Trane coil thermistor reads approximately 10–12 kΩ. OL = open (failed), near 0 Ω = shorted (failed).
5. **Re-seat or replace the connector** — if the thermistor resistance is good but E2 persists, the connector is likely the problem. Clean with contact cleaner, or crimp a new connector if pins are bent.
6. **Replace the thermistor** — if resistance is out of spec, replace the sensor. Order using the Trane outdoor unit model number.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor coil thermistor | [Amazon](https://www.amazon.com/s?k=Outdoor+coil+thermistor&tag=errorcodefixes-20) \| Trane SEN1584 or model-specific; verify correct part |
| Wire repair kit | [Amazon](https://www.amazon.com/s?k=Wire+repair+kit&tag=errorcodefixes-20) \| Solder and heat shrink, or weatherproof butt connectors |
## When to Call a Pro
If E2 persists after thermistor and connector work, have a technician verify the outdoor PCB's sensor input. On Trane ComfortLink II communicating systems, E2 as a communication fault requires checking the communication bus and may indicate a failing outdoor unit board.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
