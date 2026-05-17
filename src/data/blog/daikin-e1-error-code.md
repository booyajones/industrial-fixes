---
title: "Daikin E1 Error Code Fix — Indoor Sensor Fault"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-08T08:00:00Z
modDatetime: 2024-03-08T08:00:00Z
slug: daikin-e1-error-code
featured: false
draft: false
tags:
  - hvac
  - daikin
  - mini-split
  - sensor
  - thermistor
description: "Daikin E1 error code signals an indoor unit PCB or room temperature sensor fault. Here's how to test thermistors, check connections, and know when to replace the board."
---

## Error Code: Daikin E1

**What it means:** E1 on Daikin mini split and heat pump systems indicates a fault with the indoor unit PCB (printed circuit board) or one of the room temperature thermistors connected to it. Specifically, the indoor board detected an out-of-range or implausible signal from the room temperature sensor circuit, and shut down to prevent operating based on bad temperature data.

On some Daikin models, E1 can also indicate a communication error between the indoor PCB and the main control board — similar in symptom to Mitsubishi's E6.

## Common Causes

- **Failed room temperature thermistor** — The thermistor that measures return air temperature develops an open circuit or drifts out of range. The board receives a reading it can't logically accept (e.g., -40°F in summer) and throws E1.
- **Disconnected or corroded thermistor connector** — The connector plug on the thermistor wiring harness corrodes or backs out of the PCB socket, creating an intermittent open circuit.
- **Failed indoor PCB** — The board itself has a failed component in the thermistor input circuit (op-amp, resistor, or ADC input damaged by surge).
- **Moisture intrusion on the PCB** — Condensate dripping onto the board during a drain overflow event can cause corrosion on the sensor input tracks.
- **Incorrect model number PCB installed** — A replacement board from an incompatible model will throw E1 immediately due to thermistor reference value mismatches.

## Step-by-Step Fix {#step-by-step-fix}

1. **Power off the unit completely.** Flip the circuit breaker and wait 60 seconds. Do not attempt to diagnose with live voltage on the PCB.

2. **Remove the front panel and locate the thermistors.** On most Daikin air handlers, there are 2–3 thermistors: a room temperature (return air) sensor, a pipe temperature sensor, and sometimes a discharge air sensor. They're small cylindrical probes with 2-wire leads plugged into the PCB. The room temperature sensor is typically clipped near the filter or at the return air intake.

3. **Inspect thermistor connectors.** Unplug each thermistor connector from the PCB and inspect for corrosion (green or white buildup on pins), bent pins, or debris. Clean with electrical contact cleaner and reconnect firmly. Check that each connector clicks into place.

4. **Measure thermistor resistance.** With a multimeter on Ohms, measure across the two thermistor leads (disconnected from PCB). Daikin NTC thermistors typically read 10,000 Ω (10 kΩ) at 77°F (25°C). As temperature increases, resistance decreases; as temperature drops, resistance increases. A reading of 0 Ω (short) or OL (open circuit) at room temperature means the thermistor has failed and needs replacement.

5. **Check the PCB for moisture damage.** Visually inspect the PCB surface near the thermistor input connectors. Look for white corrosion, brown burn marks, or residue from water contact. If moisture damage is present, the board will need replacement — cleaning corrosion off PCB tracks rarely produces a lasting repair.

6. **Cross-reference the thermistor resistance with the Daikin service manual.** Daikin publishes temperature/resistance tables for their thermistors. Match your measured resistance to the current ambient temperature and confirm it falls within 10% of the table value. Values outside 20% of the table indicate a drifted thermistor even if it hasn't fully failed.

7. **Replace the faulty thermistor and retest.** Thermistors are inexpensive (under $20 in most cases) and model-specific. With the replacement installed and connectors confirmed seated, restore power and initiate a normal operating cycle. E1 should clear immediately on startup.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Where to Buy | Typical Cost |
|------|-------------|-------------|
| Room temperature thermistor (Daikin #2501038) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e1-error-code&k=Room+temperature+thermistor+%28Daikin+%232501038%29&tag=errorcodefixes-20) \| Daikin dealer, HVAC Parts Shop | $12–$30 |
| Pipe temperature thermistor (Daikin #2501039) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e1-error-code&k=Pipe+temperature+thermistor+%28Daikin+%232501039%29&tag=errorcodefixes-20) \| Daikin dealer, Amazon OEM | $12–$30 |
| Indoor PCB main board (model-specific) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-daikin-e1-error-code&tag=errorcodefixes-20) \| Daikin dealer, HVAC Parts Shop | $150–$450 |
| Electrical contact cleaner (CRC 05103) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-e1-error-code&k=Electrical+contact+cleaner+%28CRC+05103%29&tag=errorcodefixes-20) \| Home Depot, Amazon | $8–$15 |
## When to Call a Professional

If thermistor resistance tests normal, connectors are clean and seated, and E1 persists — the fault is inside the PCB itself. Daikin PCB diagnostics require the service manual for your specific model (not a generic Daikin manual — get the one for your exact model number). Board replacement is possible as a DIY job if you're comfortable with electronics, but sourcing the right part number is critical — the wrong board will throw E1 immediately. Tell the tech: "E1 fault, both thermistors test within 10% of spec, connectors are clean. I need a board-level diagnosis."

> **Pro tip:** If your Daikin unit is throwing E1 specifically after rain events or in high-humidity months, check the drain pan and evaporator coil for signs that condensate has been dripping toward the PCB. A unit with a clogged drain that overflowed can silently damage the PCB over multiple events before E1 becomes a permanent fault. Fix the drain first, then assess the board.

## Related Articles

- [Daikin A3 Error Code — Causes & Fix](/posts/daikin-a3-error-code/)
- [Daikin Applied Chiller Fault Codes Guide — WMC / AGZ / ALZ Series](/posts/daikin-applied-fault-codes/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin C9 Error Code — Compressor Discharge Temperature Sensor Fault](/posts/daikin-c9-error-code/)
- [Daikin E3 Error Code — Causes & Fix](/posts/daikin-e3-error-code/)
