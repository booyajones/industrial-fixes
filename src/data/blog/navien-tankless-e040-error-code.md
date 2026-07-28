---
title: "Navien E040 Error Code - Causes & Fix"
description: "E040 means outdoor thermistor short circuit on Navien tankless. Most common cause: damaged sensor wiring. Replace outdoor thermistor."
pubDatetime: 2026-06-30T10:07:25Z
modDatetime: 2026-06-30T10:07:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - water-heater
  - navien
money_part: "Navien Outdoor Thermistor (Outdoor Air Temperature Sensor)"
most_likely_cause: "Damaged sensor wiring"
likelihood: "the most frequent cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the outdoor sensor wiring for visible damage like cuts, rodent bites, or pinched insulation where bare wires might be touching."
  - "Check the sensor connector at the PCB for corrosion or loose pins that could cause erratic readings."
part_price: "$30-60"
---

## What this code means
The E040 error code on a Navien tankless water heater means the outdoor air temperature sensor (thermistor) has detected a short circuit. The controller is reading a resistance value near 0 Ω from the sensor, which is far below the normal 10,000 to 50,000 Ω range at standard temperatures. This tells the unit the sensor wiring or internal element has shorted, and the system cannot accurately determine ambient temperature for combustion or freeze protection.

When this fault occurs the unit shuts down immediately to prevent unsafe operation. The outdoor thermistor monitors the air temperature around the unit so the controller can adjust combustion and protect against freezing. A short in the sensor circuit gives false readings and the unit fails safe until the problem is corrected.

## Before You Replace Anything

Some technicians replace the main PCB before testing the outdoor thermistor. Always measure the sensor resistance with a multimeter first (should be 10kΩ to 50kΩ at room temperature). A reading near 0 Ω confirms the sensor or its wiring is shorted, not the board.

## Common Causes

- **Damaged sensor wiring (~50%)** Physical breaks in the wire insulation allow the conductors to touch and short, often from rodent damage, vibration, or poor installation at the sensor connection.
- **Failed thermistor element (~30%)** The sensor itself can internally short out due to age, moisture ingress into the sensor housing, or thermal stress from repeated temperature cycles.
- **Corroded or loose connector (~15%)** Corrosion or a poor connection at the PCB terminal or sensor plug can mimic a short or cause the controller to read a false resistance value.
- **Shorted main controller board input (~5%)** A fault in the PCB input circuit for the outdoor sensor can trigger E040, though the sensor and wiring are far more common culprits.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the outdoor sensor wire have visible cuts, bite marks, or exposed bare wire?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring is likely shorted at that damage point. Repair or replace the harness before replacing the sensor.<br><strong>No:</strong> Move on to resistance testing of the sensor and harness to isolate the short.</div>
</details>

<details class="dtree"><summary>With the sensor unplugged, does the sensor itself measure near 0 Ω across its terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The outdoor thermistor has failed internally and needs replacement.<br><strong>No:</strong> The sensor is good. Measure the harness side at the board. If that reads near 0 Ω, the wiring between sensor and board is shorted.</div>
</details>

<details class="dtree"><summary>Does the error clear and stay off after replacing the outdoor thermistor and resetting the unit?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor was the root cause and the repair is complete.<br><strong>No:</strong> Recheck all connections and wiring. If the fault returns immediately, the PCB input circuit may be damaged and require board replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker and shut off gas and water supplies to the unit.
2. **Locate the outdoor thermistor** (typically mounted on the exterior of the unit or in the outdoor air intake path) and trace its wiring back to the main controller board inside the unit.
3. **Inspect the wiring visually** for any signs of damage such as cuts, rodent bites, pinched insulation, or bare wire contact. Pay special attention to areas where the wire passes through holes or near sharp edges.
4. **Disconnect the sensor** from the controller board by unplugging the connector.
5. **Measure resistance across the sensor terminals** (sensor side, not the board side) with a multimeter set to ohms. A shorted sensor will read near 0 Ω. A working sensor should read between 10,000 Ω and 50,000 Ω at room temperature.
6. **Test the wiring harness** by measuring resistance across the board terminals (harness side) with the sensor still disconnected. If this reads near 0 Ω, the wiring is shorted internally and must be repaired or replaced.
7. **Replace the faulty component** (sensor or harness). If the sensor reads 0 Ω, install a new outdoor thermistor. If the harness is shorted, repair the damaged section or replace the entire wire run.
8. **Reconnect all components** and make sure the new sensor plug is firmly seated at the PCB. Restore power, gas, and water.
9. **Reset the unit** by pressing the power button on the front panel. Verify the E040 error does not return and the unit fires normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Navien Outdoor Thermistor (Outdoor Air Temperature Sensor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e040-error-code&k=Navien+Outdoor+Thermistor+%28Outdoor+Air+Temperature+Sensor%29&tag=errorcodefixes-20) \| Verify the part number matches your specific Navien model (NPE, NPN, NCB, etc.) before ordering. |
| Thermistor Wiring Harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-tankless-e040-error-code&k=Thermistor+Wiring+Harness&tag=errorcodefixes-20) \| Only needed if the sensor tests good but the harness is shorted; confirm length and connector type for your model. |

## When to Call a Pro

Call a licensed technician if you are not comfortable working with gas appliances, measuring electrical resistance with a multimeter, or accessing the internal controller board. The outdoor sensor is part of the combustion and freeze-protection system, so correct diagnosis and installation are important for safe operation. If you replace the sensor and wiring but the E040 error returns immediately, the main PCB likely has a shorted input circuit and requires professional replacement. Gas and electrical work on tankless water heaters should be performed by qualified service personnel to meet code and warranty requirements.

**Rough cost:** A pro service call runs about $150-300.
