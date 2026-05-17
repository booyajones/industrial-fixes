---
title: "Carrier 40MAQ / 40MVC Mini Split Error Codes — Causes & Fix"
description: "Carrier 40MAQ and 40MVC mini split error codes explained — what each code means, why it happens, and how to fix it."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - mini-split
  - carrier
---

## Carrier 40MAQ / 40MVC Mini Split Error Codes — What They Mean

The Carrier 40MAQ and 40MVC are single-zone mini-split indoor units paired with Carrier 38MAQ/38MVC outdoor units. These units use a 7-segment or LED display to flash diagnostic codes when a fault occurs. The control platform is Carrier's commercial-grade mini-split architecture, and many codes align with Carrier's broader ductless line (which shares hardware with Midea at the OEM level). Codes lock out operation until the fault is cleared.

[Jump to Fix](#fix)

## Common Error Codes and Causes

- **E1 — Indoor/Outdoor Communication Error** — The S-wire connecting the indoor and outdoor units has lost continuity or developed a short. Check terminal connections at both units; test wire continuity.
- **E2 — Indoor Temperature Sensor Fault** — The indoor ambient thermistor (T1) is open or shorted. Verify the sensor connector is seated; replace the thermistor if resistance is out of spec (~10 kΩ at 25°C).
- **E3 — Indoor Coil Sensor Fault** — The evaporator coil thermistor (T2) has failed. Same diagnosis as E2 — check connector and measure resistance.
- **E4 / F4 — Outdoor Temperature or Discharge Sensor Fault** — An outdoor-side thermistor (ambient or discharge) is reading outside its valid range. Inspect the outdoor unit's sensor connectors for moisture or corrosion.
- **P1 — High Pressure Protection** — Outdoor unit high-side refrigerant pressure is too high. Causes: dirty outdoor coil, blocked airflow, overcharge, or failed outdoor fan motor.
- **P2 — Low Pressure Protection** — Suction pressure too low. Causes: refrigerant undercharge (leak), restricted filter, or low ambient temperature operation outside the unit's rated range.
- **P4 — Compressor Discharge Temperature High** — Discharge line is too hot. Check refrigerant charge, outdoor airflow, and ambient temperature.
- **F1 — Indoor Fan Motor Fault** — The indoor blower is not reaching target speed. Check for a blocked wheel, failed motor, or failed motor control board.

## Step-by-Step Fix {#fix}

1. **Identify the displayed code** — Note the exact alphanumeric code shown on the display or the LED blink pattern on models without a display.
2. **Cut power and inspect wiring** — For communication errors (E1), check the S-wire terminal block at both units for loose or corroded connections.
3. **Check and replace sensors** — For sensor faults (E2, E3, E4, F4), measure thermistor resistance. Replace sensors that are open, shorted, or reading outside spec.
4. **Inspect refrigerant pressures** — For P1/P2/P4, connect gauges to the service ports and compare to Carrier's published R-410A pressure-temperature chart for the current ambient.
5. **Clean outdoor coil** — A dirty outdoor coil is the most common cause of P1 high-pressure faults. Rinse the coil with a garden hose (fin side out) and confirm airflow is unrestricted.
6. **Reset the unit** — Power cycle for 2 minutes after any repair and confirm the code clears on restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor ambient thermistor (T1) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-40maq-error-codes&k=Indoor+ambient+thermistor+%28T1%29&tag=errorcodefixes-20) \| Carrier 40MAQ OEM part; match resistance curve |
| Indoor coil thermistor (T2) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-40maq-error-codes&k=Indoor+coil+thermistor+%28T2%29&tag=errorcodefixes-20) \| Same resistance curve as T1 on most models |
| Communication wire (S-wire) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-40maq-error-codes&k=Communication+wire+%28S-wire%29&tag=errorcodefixes-20) \| 18 AWG; replace full run if damaged |
| Outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-40maq-error-codes&tag=errorcodefixes-20) \| Match HP, RPM, and shaft direction |
## When to Call a Pro

P1/P2 refrigerant pressure codes require EPA 608 certification to access refrigerant and add/recover charge. Always call a licensed HVAC technician for refrigerant work on Carrier mini splits.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
