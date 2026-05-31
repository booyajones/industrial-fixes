---
title: "Trane AC E2 Error Code — Sensor and Communication Fault Fix"
author: "Marcus Webb"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - hvac
  - trane
  - air-conditioner
  - heat-pump
description: "Trane E2 error code means a sensor or communication fault on AC and heat pump systems. Learn the causes, how to diagnose, and how to fix E2 step by step."
---

## Trane AC E2 Error Code — What It Means

The **E2 error code** on a Trane air conditioning or heat pump system indicates a **sensor fault or communication fault** detected by the system's control board. E2 appears on the thermostat display or the outdoor unit's diagnostic LED and signals that either a temperature sensor has failed (open or shorted), or a communication signal between system components has been lost or corrupted. Trane's communicating systems (ComfortLink II, iComfort, and TCS — Trane Communicating System) use a proprietary bus to pass data between the outdoor unit, air handler, and thermostat; an E2 on these systems often means that the control board is unable to read a critical sensor it needs to operate safely.

On single-stage non-communicating systems, E2 is most often an outdoor ambient temperature sensor (OAT) or refrigerant temperature sensor fault that prevents the unit from entering defrost cycles correctly. On variable-speed and communicating systems, E2 can also represent a control board communication breakdown.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor ambient temperature sensor (OAT)** — The outdoor ambient sensor is a thermistor mounted on the outdoor unit chassis near the coil inlet. When it fails open or short, the control board cannot calculate the correct operating parameters and faults with E2.
- **Failed refrigerant temperature sensor** — On heat pump systems, sensors monitoring liquid line and discharge line temperatures feed directly into defrost and compression control logic. A failed refrigerant sensor triggers E2 and disables automatic defrost.
- **Damaged sensor wiring** — Rodents, vibration wear, or corrosion can damage the thin wire leads connecting sensors to the control board. A broken wire reads as an open circuit — identical to a failed sensor from the control board's perspective.
- **Moisture in wiring connectors** — Water intrusion into the outdoor unit's wiring harness corrodes sensor pin connectors, increasing contact resistance until the signal falls outside the board's valid range.
- **Control board failure** — The sensor input circuit on the main control board has failed, causing false E2 faults even when the sensor is good. This is the least common cause but becomes likely when sensors and wiring all test within spec.
- **Communication wiring fault (communicating systems)** — On TCS/ComfortLink II systems, a loose or corroded connection on the communication bus between the outdoor unit and air handler generates E2 as a communication alert.

## Step-by-Step Fix {#fix}

1. **Identify which sensor is faulting** — On communicating systems (ComfortLink II or iComfort), check the thermostat's diagnostic menu for a full fault description. It will typically specify which sensor is out of range. On non-communicating systems, the E2 code defaults to the outdoor ambient sensor as the most common culprit.

2. **Locate and inspect the outdoor ambient sensor** — The OAT sensor is typically clipped to the outdoor coil, the side panel, or the chassis near the coil air inlet. Visually inspect the sensor body and wire leads for physical damage. On heat pumps, also locate the liquid line and suction line sensors clipped to the refrigerant piping.

3. **Test sensor resistance** — Disconnect the sensor connector at the control board. Using a multimeter set to resistance, measure across the two sensor leads. At 70°F (21°C), most Trane NTC thermistors read approximately 10 kΩ. Open circuit (OL) or near-zero resistance confirms sensor failure. Check the service manual for the resistance-temperature table for your model.

4. **Inspect the wiring harness** — Trace the sensor wire from the sensor clip to the control board connector. Look for chafed insulation, crimped sections, or connector pins that are pushed back or corroded green. Gently wiggle the harness while monitoring the multimeter — if resistance changes with movement, you have an intermittent wire fault.

5. **Clean the sensor connectors** — Spray electrical contact cleaner into both sides of the sensor connector. Dry with compressed air. Re-seat the connector firmly and listen for the latch click. Re-test resistance at the board connector to confirm a clean signal path.

6. **Check communication wiring (communicating systems)** — If E2 is flagged as a communication fault rather than a sensor fault, inspect the low-voltage communication wiring between the outdoor unit, air handler, and thermostat. The communication bus is typically 2 wires (R and C plus the comm pair). Verify all terminal screws are tight and wires are not nicked or shorting.

7. **Reset and test** — After any repair, restore power, clear the fault code (cycle the breaker or use the thermostat reset), and run a complete operating cycle. On heat pump systems, initiate a manual defrost cycle (if your thermostat supports it) to confirm the sensors are feeding correct data.

## Parts You May Need

| Part | Notes |
|------|-------|
| Trane outdoor ambient temp sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-trane-e2-ac-sensor-fault&tag=errorcodefixes-20) — Match by model number; many Trane OAT sensors share part numbers across product lines |
| Trane liquid / suction line thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-e2-ac-sensor-fault&k=trane+heat+pump+refrigerant+thermistor&tag=errorcodefixes-20) — Required for heat pump defrost control; clip-type sensor |
| Electrical contact cleaner | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-e2-ac-sensor-fault&k=electrical+contact+cleaner+CRC&tag=errorcodefixes-20) — Use before replacing sensors if connector corrosion is visible |
| Trane outdoor unit control board | [Amazon](https://www.amazon.com/s?k=Trane+outdoor+unit+control+board&tag=errorcodefixes-20) — Replace only after sensors and wiring are confirmed good |

## When to Call a Technician

If E2 persists after sensor replacement and wiring inspection, the outdoor unit control board has likely failed. Control board replacement on Trane systems involves verifying system configuration dip switches or jumpers, which must be set correctly for the equipment model and refrigerant type. Additionally, if E2 is accompanied by loss of cooling or heating performance, a refrigerant issue may also be present — refrigerant diagnosis and recharge requires EPA 608 certification. Call a Trane-authorized HVAC technician for these scenarios.

## Related Articles

- [Trane Heat Pump E2 Error Code — Causes & Fix](/posts/trane-heat-pump-error-code-e2/)
- [Trane ComfortLink II Error Codes — Complete Diagnostic Guide](/posts/trane-comfortlink-ii-error-codes/)
- [Trane Furnace Error Codes — Complete Guide](/posts/trane-furnace-error-codes/)
- [Trane 3 Flashes — Pressure Switch Fault Fix](/posts/trane-3-flashes-pressure-switch/)
- [Trane XL20i Heat Pump Error Codes — Complete Guide](/posts/trane-xl20i-heat-pump-error-codes/)

## See Also

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Chiller Fault Codes — Complete Troubleshooting Guide](/posts/trane-chiller-fault-codes/)
- [Trane / American Standard 2-Blink Error Code — External Lockout Fix](/posts/trane-2-blink-error-code/)
- [Trane XR13 Air Conditioner Error Codes — Fault Code Diagnostic Guide](/posts/trane-xr13-error-codes/)
