---
title: "Trane Heat Pump E1 Error - Causes & Fix"
description: "E1 on a Trane mini-split means indoor room temperature sensor failure. Most often the thermistor is open, shorted, or unstable."
pubDatetime: 2026-06-21T10:12:21Z
modDatetime: 2026-06-21T10:12:21Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - trane
money_part: "Trane mini-split indoor room temperature sensor (T1 thermistor)"
most_likely_cause: "Faulty indoor room temperature sensor (thermistor)"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Check that the sensor plug at the indoor PCB is fully seated and free of corrosion"
  - "Verify the sensor is not located near a light bulb, direct sunlight, or the heat exchanger where local heat distorts the reading"
part_price: "$20-45"
---

## What this code means
The E1 error code on a Trane heat pump (specifically the mini-split and TVR-Pro series) signals an indoor room temperature sensor failure. The thermistor that measures room temperature is either open (infinite resistance), shorted (zero resistance), or producing unstable readings that the indoor PCB cannot interpret. This sensor is critical for the unit to regulate heating and cooling cycles based on actual room conditions.

While older models or user forums sometimes refer to E1 as a generic communication error, Trane's official mini-split service manual explicitly defines E1 as an indoor room temperature sensor fault. The unit cannot operate properly without a valid room temperature reading, so it will shut down or fail to start until the sensor circuit is repaired.

## Before You Replace Anything

Some technicians replace the indoor PCB first when the sensor itself is the actual problem. Always measure sensor resistance and compare it to the model chart before replacing the board.

## Common Causes

- **Faulty sensor (thermistor) (~50%)** The sensor itself is open, shorted, or unstable and cannot provide a valid resistance reading to the PCB.
- **Damaged wiring harness (~25%)** The harness connecting the sensor to the PCB has rub-through, moisture intrusion, pinched insulation, or disconnected pins.
- **Incorrect sensor placement (~10%)** The sensor is exposed to abnormal local heat from a light, direct sunlight, or the heat exchanger rather than measuring true room air.
- **PCB input circuit fault (~10%)** The indoor PCB's input circuit where the sensor connects is damaged, even though the sensor and harness are functional.
- **Loose or corroded connector (~5%)** The sensor plug at the PCB has poor contact due to corrosion, oxidation, or a partially unseated connection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the sensor plug fully seated and free of corrosion at the indoor PCB?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connector is good. Proceed to measure sensor resistance.<br><strong>No:</strong> Clean the pins with contact cleaner and reseat the plug firmly. If the error clears, the problem was a poor connection.</div>
</details>

<details class="dtree"><summary>Does the sensor resistance match the model chart for the current room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> Sensor is good. The indoor PCB input circuit is likely faulty and the board needs replacement.<br><strong>No:</strong> Sensor is open, shorted, or unstable. Replace the indoor room temperature sensor.</div>
</details>

<details class="dtree"><summary>When you warm the sensor slightly by hand, does the resistance decrease smoothly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Thermistor is responding normally. Check the harness for damage or suspect the PCB.<br><strong>No:</strong> Thermistor is unstable or defective. Replace the sensor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to both the indoor and outdoor units at the breaker or disconnect to prevent electrical damage during testing.
2. **Inspect the sensor location** and verify it is positioned to measure room air, not exposed to local heat from lights, sunlight, or the heat exchanger.
3. **Check the sensor plug** at the indoor PCB for loose connections, corrosion, or oxidation. Clean pins with contact cleaner and reseat firmly.
4. **Inspect the harness** from sensor to PCB for rub-through, moisture, pinched insulation, or disconnected pins. Repair or replace damaged wiring.
5. **Measure sensor resistance** by disconnecting the sensor and using a multimeter set to the kiloohm scale. Compare the value to the model chart for the current room temperature. Resistance should never be zero (short) or infinite (open).
6. **Perform a dynamic test** by warming the sensor slightly with your hand. Verify that resistance decreases smoothly as the thermistor warms. Erratic or no change indicates a faulty sensor.
7. **Replace the sensor** if it is open, shorted, or unstable. If the sensor checks normal, suspect the indoor PCB input circuit and replace the board.
8. **Restore power and test** by running a heating or cooling cycle. Confirm stable operation and that the E1 error does not return under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Trane mini-split indoor room temperature sensor (T1 thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-heat-pump-e1-error-code&k=Trane+mini-split+indoor+room+temperature+sensor+%28T1+thermistor%29&tag=errorcodefixes-20) \| Match the sensor part number to your specific Trane mini-split model. |
| Trane mini-split indoor unit PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-heat-pump-e1-error-code&k=Trane+mini-split+indoor+unit+PCB&tag=errorcodefixes-20) \| Required only if the sensor and harness are verified functional and the board input circuit is faulty. |

## When to Call a Pro

Call a professional if you are uncomfortable working with low-voltage electrical circuits or if you lack a multimeter and the skill to measure resistance and interpret a model chart. A technician can quickly isolate whether the fault is in the sensor, harness, or PCB and has access to OEM replacement sensors and boards. Also call a pro if the error persists after you have replaced the sensor and verified the harness, since the PCB replacement requires proper board configuration and refrigerant-side checks to rule out other faults.

**Rough cost:** DIY runs about $25-50 in parts, 30-60 min. A pro service call runs about $120-250.
