---
title: "Navien E032 Error - Causes & Fix"
description: "E032 means the secondary cold water inlet thermistor has failed or its wiring is loose. Most often a loose connector or bad sensor."
pubDatetime: 2026-06-30T10:04:13Z
modDatetime: 2026-06-30T10:04:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - water-heater
  - navien
money_part: "Navien Cold Water Inlet Thermistor 2"
most_likely_cause: "Loose or disconnected thermistor wire connector"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the unit at the circuit breaker and reseat the thermistor wire connector at the control board to rule out a loose connection"
  - "Inspect the thermistor wiring and connectors for visible corrosion, moisture, or physical damage"
part_price: "$40-80"
no_buy_pct: "35%"
---

## Navien E032 Error — What It Means

The E032 error code on a Navien tankless water heater indicates a Cold Water Inlet Thermistor 2 (secondary sensor) failure. The control board detects that the resistance from this sensor is outside the acceptable range, which it interprets as either an open circuit (infinite resistance, broken wire) or a short circuit (near-zero resistance, damaged component). Without a valid temperature reading from this sensor, the unit cannot calculate the correct gas flow or burner operation for the desired output temperature, so it shuts down to prevent unsafe operation or overheating.

## Before You Replace Anything

Homeowners sometimes replace the main PCB thinking the board is bad, when a simple resistance test across the thermistor terminals would reveal the sensor itself is open or shorted.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected wiring (~35%)** The thermistor wire connector becomes loose, corroded, or disconnected from the PCB due to vibration or thermal cycling.
- **Thermistor failure (~30%)** The sensor itself has degraded internally (damaged semiconductor) over time, causing it to short or open.
- **Water leaks or moisture ingress (~20%)** Moisture near the sensor connection point causes corrosion on the terminals, leading to a high-resistance (open) fault.
- **PCB issues (~10%)** A damaged trace on the PCB or a failed input circuit on the board mimics a sensor fault.
- **Wire harness damage (~5%)** The wiring between the sensor and the board is broken (open) or shorted to ground.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear when you reseat the thermistor connector at the control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> The connection was loose. Monitor the unit for a few days to confirm the fix holds.<br><strong>No:</strong> The sensor or wiring is likely faulty. Proceed to resistance testing with an ohmmeter.</div>
</details>

<details class="dtree"><summary>With the thermistor disconnected, does an ohmmeter read 10kΩ to 15kΩ at room temperature across the sensor leads?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is good. Check the wire harness for breaks or shorts, or suspect the PCB input circuit.<br><strong>No:</strong> The thermistor is open (infinite resistance) or shorted (0Ω). Replace the Cold Water Inlet Thermistor 2.</div>
</details>

<details class="dtree"><summary>After replacing the thermistor, does the E032 code return?</summary>
<div class="dtree-body"><strong>Yes:</strong> The PCB input circuit or a wire harness fault is the cause. A technician should test the board and wiring continuity.<br><strong>No:</strong> The repair is complete. The new sensor has resolved the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the unit** at the circuit breaker to make sure safety before opening the cover.
2. **Locate the Cold Water Inlet Thermistor 2** (usually mounted near the water inlet on the cold side) and visually inspect the wire harness for physical damage, corrosion, or loose connections at the PCB.
3. **Reseat the thermistor connector** by unplugging it from the control board and firmly reconnecting it to rule out a loose connection.
4. **Measure resistance** with an ohmmeter by disconnecting the thermistor wires from the PCB and measuring across the two sensor leads. At room temperature (approx. 20°C), the resistance should be approximately 10kΩ to 15kΩ. A reading of 0Ω indicates a short and infinite (OL) indicates an open.
5. **Check the wire harness** by measuring resistance from the PCB pin to the sensor end to make sure the wires are not broken (open) or shorted to ground.
6. **Replace the thermistor** if the resistance is out of spec. If the sensor is good but the fault persists, inspect the PCB for damage and replace the control board if needed.
7. **Restore power** and clear the error code (usually by cycling power or pressing the power button), then run the unit to verify the error does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Navien Cold Water Inlet Thermistor 2 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e032-error-code&k=Navien+Cold+Water+Inlet+Thermistor+2&tag=errorcodefixes-20) \| Verify the part number for your specific Navien model (NPE, NPN, etc.) before ordering |
| Navien Control Board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e032-error-code&k=Navien+Control+Board+%28PCB%29&tag=errorcodefixes-20) \| Only needed if the thermistor and wiring test good but the fault persists |

## When to Call a Pro

Call a licensed technician if you are not comfortable working inside a gas-fired appliance or if you lack an ohmmeter to test resistance. The technician will measure the thermistor resistance, check the wire harness for continuity, and replace the sensor or control board as needed. Because tankless water heaters involve gas connections and high-voltage wiring, professional service ensures the repair is done safely and the unit is tested for proper combustion and venting after the fix.

**Rough cost:** A pro service call runs about $150-300.

## See Also

- [Navien NCB-700 Combination Boiler Error Codes - Full Fault Guide](/posts/navien-ncb-700-error-codes/)
- [Navien E110 Error Code - Causes & Fix](/posts/navien-tankless-e110-error-code/)
- [Navien Water Heater Pilot Won't Stay Lit - Causes & Fix](/posts/navien-water-heater-pilot-wont-stay-lit/)
- [Navien E010 Error Code - Causes & Fix](/posts/navien-tankless-e010-error-code/)
