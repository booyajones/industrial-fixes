---
title: "Navien E337 Error Code - Causes & Fix"
description: "E337 error indicates a communication fault between the control board and a sensor or component. Check wiring connections first."
pubDatetime: 2026-07-14T08:50:51Z
modDatetime: 2026-07-14T08:50:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - water-heater
  - navien
money_part: "Navien temperature sensor (thermistor)"
most_likely_cause: "loose or corroded wiring connector"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Power-cycle the unit by switching off the circuit breaker for 60 seconds, then back on to clear transient faults"
  - "Open the front cover and inspect all wire harness connectors for looseness, corrosion, or moisture"
  - "Check the condensate drain and vent pipes for blockages that might cause sensors to read incorrectly"
part_price: "$40-120"
no_buy_pct: "60%"
---

## Navien E337 Error Code — What It Means

The E337 error code on Navien tankless water heaters signals a communication problem between the main control board and one of the system components or sensors. This can involve wiring faults, loose connectors, or a failed sensor that is no longer responding to the controller. Because Navien uses a network of temperature sensors, flow sensors, and ignition components that all report back to the central PCB, any break in that communication chain will trigger this fault and shut down normal operation.

The heater will typically not fire or will shut off mid-cycle when E337 appears. The exact component involved may vary by model, so consult your owner's manual or the wiring diagram on the inside of the unit's cover to identify which sensor or module corresponds to the code on your specific model.

## Before You Replace Anything

Homeowners often replace the main control board when the real fault is a loose wire harness or corroded pin at a sensor connection. Inspect and reseat every connector first before ordering a board.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded wiring connector (~40%)** Vibration, humidity, or installation handling can loosen or corrode the multi-pin connectors between sensors and the control board, breaking the communication link.
- **Failed temperature sensor (~25%)** Inlet, outlet, or heat-exchanger thermistors can fail open or short, causing the board to lose temperature feedback and throw a communication fault.
- **Control board firmware glitch (~15%)** A temporary software hang or voltage spike can lock up the microcontroller, preventing it from polling sensors correctly.
- **Faulty control board (PCB) (~12%)** The main printed circuit board itself may have a failed communication bus, damaged trace, or blown input circuit for one of the sensor channels.
- **Damaged sensor wiring harness (~8%)** Pinched, cut, or burned wires between a sensor and the board will interrupt signal transmission and appear as a communication error.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear after a power-cycle and stay off for at least one heating cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely transient (voltage spike or firmware glitch). Monitor for recurrence and proceed if it returns.<br><strong>No:</strong> A persistent hardware issue is present. Continue diagnostics on connectors and sensors.</div>
</details>

<details class="dtree"><summary>Are all wire harness connectors at the control board and sensors firmly seated with no visible corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is sound. Test individual sensors with a multimeter or swap a suspected sensor to isolate the fault.<br><strong>No:</strong> Reseat or clean every connector. Corrosion or loose pins are the likely cause.</div>
</details>

<details class="dtree"><summary>Do you have a multimeter and your model's service manual with sensor resistance tables?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure resistance at each thermistor and flow sensor. Compare readings to the manual's table to identify a failed component.<br><strong>No:</strong> Call a qualified technician to perform sensor diagnostics and avoid replacing parts by trial and error.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker or unplug the unit to work safely on electrical connections.
2. **Remove the front service panel** by unscrewing the cover fasteners to access the control board and sensor wiring.
3. **Inspect every wire harness connector** on the control board and at each sensor (inlet, outlet, heat exchanger, flow sensor). Press each connector firmly to reseat it and look for corrosion, bent pins, or moisture inside the plug housings.
4. **Power the unit back on** and observe whether the E337 code reappears immediately or after a heating demand starts.
5. **If the code persists, disconnect one sensor at a time** (with power off) and measure its resistance with a multimeter. Consult your model's service manual or wiring diagram for the correct resistance range at room temperature for each thermistor.
6. **Replace any sensor** that reads open (infinite resistance), short (near-zero resistance), or far outside the specified range. Use the exact replacement part number for your Navien model.
7. **If all sensors test good and connectors are clean, replace the main control board** as a last resort, since the fault lies in the board's communication circuits.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Navien temperature sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-water-heater-e337-error-code&k=Navien+temperature+sensor+%28thermistor%29&tag=errorcodefixes-20) \| Match the exact part number for your heater model (inlet, outlet, or heat-exchanger sensor) |
| Navien main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-water-heater-e337-error-code&k=Navien+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Confirm your model and serial number before ordering; boards are model-specific |

## When to Call a Pro

Call a licensed plumber or Navien-certified technician if you are uncomfortable working with 120-volt wiring or if sensor diagnostics with a multimeter are beyond your skill level. A pro can use Navien's service software to read real-time sensor data, pinpoint the failing component quickly, and make sure that gas and venting safety interlocks remain intact during repairs. If the error returns after you have cleaned connectors and replaced an obvious failed sensor, a technician can test the control board's communication bus and rule out intermittent faults that are hard to reproduce.

**Rough cost:** DIY runs about $50-180 in parts, 1-2 hours. A pro service call runs about $200-450.
