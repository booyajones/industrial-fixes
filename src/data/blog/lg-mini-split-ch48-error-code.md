---
title: "LG CH48 Error Code - Causes & Fix"
description: "LG CH48 means outdoor discharge or coil sensor is unplugged, open, or shorted. Most often a loose connector or bad thermistor."
pubDatetime: 2026-06-30T10:00:03Z
modDatetime: 2026-06-30T10:00:03Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - lg
money_part: "LG outdoor unit discharge sensor (thermistor)"
most_likely_cause: "Disconnected or loose sensor wiring harness at the PCB connector"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the unit: turn off the AC, disconnect from power for 3–5 minutes, reconnect, and power on to see if the error clears"
  - "Inspect the outdoor unit for loose sensor connectors at the PCB and reseat them firmly"
  - "Check for visible wire damage or rodent chewing on the sensor harness"
---

## LG CH48 Error Code — What It Means

The CH48 error code indicates that the outdoor unit discharge sensor and/or the outdoor unit air (coil) sensor are unplugged, open, or shorted. The electronic control board cannot receive a valid temperature reading from the sensors located at the outdoor unit discharge line (compressor outlet) and the outdoor unit air/coil line (condenser coil outlet, liquid line side). For Multi V systems, this code specifically refers to the outdoor unit coil sensor.

Without these temperature readings, the system cannot correctly calculate subcooling or superheating or monitor critical discharge temperatures. The unit will shut down to protect the compressor and refrigerant circuit from operating without proper thermal feedback.

## Before You Replace Anything

Homeowners often replace the PCB first, assuming the board is bad. Measure sensor resistance with a multimeter and clean the connectors before ordering a control board. A failed sensor is far more common and much cheaper.

[Jump to Fix](#fix)

## Common Causes

- **Disconnected or loose wiring (~40%)** The sensor wiring harness is unplugged, loose, or corroded at the PCB connector, interrupting the signal.
- **Sensor damage (open or short circuit) (~30%)** The thermistor itself has failed internally due to age, electrical surge, or physical damage, reading zero or infinite resistance.
- **Rodent damage (~15%)** Wires leading to the sensor have been chewed by animals, causing a break in the circuit.
- **Poor sensor placement (~10%)** The sensor tip is not firmly clamped against the pipe or the heat-conducting paste/clamp is missing, causing erratic readings.
- **PCB failure (~5%)** The input circuit on the main PCB or inverter PCB that reads the sensor resistance is defective.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>After power-cycling the unit (off for 3–5 minutes), does the CH48 error clear and the system run normally?</summary>
<div class="dtree-body"><strong>Yes:</strong> The error was a temporary glitch. Monitor the system for a day. If it returns, proceed to sensor testing.<br><strong>No:</strong> The fault is persistent. Inspect the sensor connectors and wiring at the outdoor unit.</div>
</details>

<details class="dtree"><summary>Are the sensor connectors at the outdoor PCB seated firmly with no corrosion or visible wire damage?</summary>
<div class="dtree-body"><strong>Yes:</strong> The connectors are good. Test the sensor resistance with a multimeter to check for an open or short.<br><strong>No:</strong> Clean and firmly reseat the connectors. If wires are damaged, repair or replace the sensor harness.</div>
</details>

<details class="dtree"><summary>When you measure the sensor resistance, does it read zero (0 kΩ) or infinite (∞), or does it fail to change when you warm it with your hand?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is bad. Replace the discharge sensor or coil sensor (whichever is reading open or shorted).<br><strong>No:</strong> The sensor resistance is normal. Check PCB voltage at the sensor input. If absent or abnormal, the PCB is likely defective.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the unit** and disconnect it from the electrical supply for 3–5 minutes, then reconnect and power on to attempt a reset.
2. **Locate the sensors** on the outdoor unit: the discharge sensor is clamped to the line exiting the compressor, and the coil sensor is clamped to the condenser coil outlet (liquid line side).
3. **Inspect the wiring** visually for loose connectors, corrosion, or physical damage (rodent chewing). Check that the sensor tip is firmly clamped to the pipe.
4. **Disconnect the sensor connectors** from the PCB, clean the terminals, and firmly reconnect them.
5. **Measure sensor resistance** with a multimeter set to kilo-ohms (kΩ): disconnect the sensor from the PCB completely, measure across the sensor terminals, and rub the sensor with your hand. Resistance should not be zero or infinite and should decrease when heated.
6. **Check PCB voltage** if the sensor resistance is normal: measure DC voltage between the sensor wires at the PCB connector. If voltage is absent or abnormal, the PCB input is likely defective.
7. **Replace the sensor** if it reads open (infinite) or shorted (zero) or does not change with heat. If the sensor is good but the PCB input is faulty, replace the PCB.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG outdoor unit discharge sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch48-error-code&k=LG+outdoor+unit+discharge+sensor+%28thermistor%29&tag=errorcodefixes-20) \| NTC thermistor for compressor discharge line. Verify model compatibility. |
| LG outdoor unit coil sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch48-error-code&k=LG+outdoor+unit+coil+sensor+%28thermistor%29&tag=errorcodefixes-20) \| NTC thermistor for condenser coil outlet. Verify model compatibility. |
| LG outdoor unit main PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch48-error-code&k=LG+outdoor+unit+main+PCB&tag=errorcodefixes-20) \| Control board with sensor input circuit. Only replace after confirming sensor is good and PCB voltage is absent. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with high-voltage electrical connections or refrigerant lines. The repair involves accessing the outdoor unit's control board, testing thermistor resistance with a multimeter, and potentially working near live circuits. A technician can also verify refrigerant pressures and subcooling/superheating values if the sensors are replaced, to confirm the system is operating correctly. If the PCB is faulty, a pro can source the correct replacement board and transfer any required settings or address codes.

**Rough cost:** A pro service call runs about $150-300.
