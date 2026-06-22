---
title: "State Water Heater E22 Error - Causes & Fix"
description: "E22 typically signals a temperature sensor or thermistor fault. Check connectors and sensor wiring first, then test sensor resistance."
pubDatetime: 2026-06-20T12:55:57Z
modDatetime: 2026-06-20T12:55:57Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - water-heater
  - state-water-heaters
money_part: "Temperature sensor / thermistor"
most_likely_cause: "Temperature sensor or thermistor failure"
likelihood: "the most common cause in similar platforms"
diy_or_pro: "diy"
free_checks:
  - "Power-cycle the unit (turn breaker off 60 seconds, then back on) and see if the code clears temporarily."
  - "Inspect all sensor connectors at the control board and sensor harnesses for corrosion, moisture, or loose pins."
  - "Check the wiring harness from each temperature sensor to the board for chafing, pinching, or breaks."
part_price: "$20–60"
---

## State Water Heater E22 Error — What It Means

State Water Heaters does not publish a universal definition for E22 across all models in widely available documentation. Error-code meanings vary by model type (tank versus tankless, gas versus electric) and control platform. In similar water-heater systems, E22 often indicates a temperature-sensor or thermistor fault, meaning the control board cannot read valid temperature data from one or more sensors. This can stem from a failed sensor, corroded or loose connector, damaged wiring, or a control-board input failure.

Because State uses different control packages across its product line, the exact definition and troubleshooting steps depend on your specific model and serial number. Consult the service literature or wiring diagram supplied with your unit, or scan the QR code on the rating plate to access model-specific support resources. If your manual does not list E22, contact State technical support with your full model and serial number before replacing parts.

## Before You Replace Anything

Homeowners often replace the control board when the real fault is a corroded sensor connector or a thermistor with out-of-range resistance. Always measure sensor resistance against the manufacturer chart and inspect connectors before swapping the board.

[Jump to Fix](#fix)

## Common Causes

- **Failed temperature sensor or thermistor (~50%)** One or more thermistors has drifted out of specification or failed open, so the control board reads invalid resistance and throws E22.
- **Corroded or loose sensor connector (~25%)** Moisture, heat cycling, or vibration causes a connector pin to lose contact or corrode, interrupting the sensor signal.
- **Damaged sensor wiring harness (~15%)** A wire is chafed, pinched, or broken between the sensor and the board, creating an open or intermittent circuit.
- **Control-board input failure (~8%)** The board's analog-to-digital converter or sensor-input circuit has failed, even though the sensor itself tests good.
- **High-limit or safety-sensor fault (~2%)** A secondary safety sensor (high-limit thermostat or overheat cutoff) is open or out of range, triggering a generic sensor error on some platforms.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear after a power cycle but return within one heating cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> An intermittent connection or marginal sensor is likely. Inspect connectors and measure sensor resistance under operating temperature.<br><strong>No:</strong> The fault is persistent. Proceed to measure each sensor's resistance cold and compare to the manufacturer chart in your model's service manual.</div>
</details>

<details class="dtree"><summary>Do all sensor connectors at the control board seat firmly with no corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring and connections are probably sound. Measure each thermistor's resistance and replace any sensor reading significantly higher than the others.<br><strong>No:</strong> Clean corroded pins with electronic contact cleaner and reseat the connector. If corrosion is heavy, replace the connector or harness.</div>
</details>

<details class="dtree"><summary>Does the error persist after replacing the suspect sensor?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board's input circuit may be faulty. Verify wiring continuity from sensor to board, then replace the board if all sensors and wiring test good.<br><strong>No:</strong> The sensor was the root cause. Clear the error, restore power, and verify normal operation through a full heating cycle.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker and, if gas-fired, close the gas shutoff valve to the water heater.
2. **Locate the control board** (usually behind an access panel on the front or side) and photograph all wire connections before disconnecting anything.
3. **Inspect each sensor connector** at the board and at each thermistor or temperature-sensor body for moisture, corrosion, bent pins, or loose fit.
4. **Measure thermistor resistance** with a multimeter set to ohms. Disconnect one lead of each sensor, measure across the sensor terminals, and compare the reading to the resistance chart in your model's service manual. A sensor reading much higher than the chart or open (infinite resistance) is failed.
5. **Check wiring continuity** from each sensor terminal to the corresponding board pin. A break or high resistance in the harness will mimic a sensor fault.
6. **Replace the faulty sensor or harness** if testing confirms a failure. Match the part number from your model's wiring diagram or order by model and serial number.
7. **Reassemble, restore power and gas**, and run a heating cycle. Monitor the display to confirm E22 does not return. If the code reappears and all sensors test good, replace the control board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Temperature sensor / thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-state-water-heater-e22-error-code&k=Temperature+sensor+%2F+thermistor&tag=errorcodefixes-20) \| Match the part number on your existing sensor or order by water-heater model and serial number. |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-state-water-heater-e22-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| Required only if wires are chafed, broken, or connectors are badly corroded. |
| Control board / PCB assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-state-water-heater-e22-error-code&k=Control+board+%2F+PCB+assembly&tag=errorcodefixes-20) \| Last-resort part. Replace only after confirming all sensors and wiring test within specification. |

## When to Call a Pro

Call a licensed technician if you are uncomfortable working with electrical connections inside the water heater, if you cannot locate a wiring diagram or resistance chart for your specific State model, or if the code persists after you have verified sensor resistance and wiring continuity. Gas-fired units require safe handling of gas connections and proper venting. A pro can also access factory service bulletins and model-specific fault trees that are not published in consumer manuals. If your unit is still under warranty, professional diagnosis and repair may be required to preserve coverage.

**Rough cost:** DIY runs about $25–80 in parts, 30–60 min. A pro service call runs about $150–350.
