---
title: "Bosch Washer F20 Error Code - Causes & Fix"
description: "F20 means unexpected heating: water is heating when it shouldn't. Most often the NTC temperature sensor or heater relay has failed."
pubDatetime: 2026-06-09T19:22:16Z
modDatetime: 2026-06-09T19:22:16Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - washer
  - bosch
money_part: "NTC temperature sensor (thermistor)"
most_likely_cause: "NTC temperature sensor fault or wiring issue"
likelihood: "the most common cause"
diy_or_pro: "pro"
---

## What this code means
Bosch F20 (also shown as E20 on some models) indicates unexpected heating in the washing machine. The washer is detecting that water is heating when the selected program should not be heating, or heating is occurring at the wrong time. According to Bosch support documentation, this fault means the heating element is energizing without a command from the central controller, or the temperature sensor is incorrectly reporting a rise in water temperature.

The code points to a problem in the heating circuit: either the control board is sending an unwanted heater command, the heater relay is stuck closed, the NTC temperature sensor or its wiring is faulty, or the heating element itself has an insulation breakdown allowing current to leak to the chassis. Bosch advises a power-cycle reset first. If the error returns, the issue requires component-level diagnosis of the temperature sensor, heater relay, heating element, and associated wiring.

## Before You Replace Anything

Many people replace the control board first when the real culprit is a failed NTC sensor or a heating element with insulation breakdown to ground. Always test the NTC sensor resistance and check the heater element for leakage to chassis before swapping the board.

## Common Causes

- **NTC temperature sensor fault (~40%)** The thermistor that monitors water temperature has failed or its wiring harness is broken, causing the control board to see false heating.
- **Heater relay or control board fault (~30%)** A stuck relay on the main control board energizes the heating element when the program does not call for heat.
- **Heating element insulation breakdown (~20%)** The heater has a short to the metal chassis or housing, allowing current leakage that the control board interprets as unwanted heating.
- **Damaged wiring or connector (~10%)** Corroded or pinched wires between the NTC sensor, heating element, and control board create intermittent signals or ground faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear after unplugging the washer for 15 minutes and restarting?</summary>
<div class="dtree-body"><strong>Yes:</strong> A transient glitch in the control board was likely the cause. Run a test cycle and monitor for recurrence.<br><strong>No:</strong> The fault is persistent. Proceed to check the NTC sensor and heating element circuits.</div>
</details>

<details class="dtree"><summary>Can you safely access the NTC sensor connector at the top or side of the tub?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect the sensor and measure its resistance with a multimeter (consult your model's specification sheet). If out of range or open, replace the sensor.<br><strong>No:</strong> The sensor or heater may require removing the outer cabinet or front panel. Call a technician if you are not comfortable disassembling the machine.</div>
</details>

<details class="dtree"><summary>Do you have a multimeter and experience testing for ground faults on 120/240 V circuits?</summary>
<div class="dtree-body"><strong>Yes:</strong> With power OFF, measure the heating element resistance to ground. Any continuity to the chassis indicates insulation breakdown and requires a new heater.<br><strong>No:</strong> Testing high-voltage components and relay circuits safely requires training. Schedule a service call to avoid shock or further damage.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off and unplug the washer** for at least 15 minutes to reset the control board and clear any transient faults.
2. **Restore power and run a short test cycle** to see if F20 reappears. If the error does not return, monitor the machine over the next few loads.
3. **Disconnect power again** and remove the cabinet or access panel to reach the NTC temperature sensor, typically mounted on the outer tub or sump.
4. **Unplug the NTC sensor connector** and use a multimeter in resistance mode to test the sensor (consult your model's service sheet for the correct resistance at room temperature). Replace the sensor if readings are out of range or open.
5. **Inspect the heating element wiring** and connectors for corrosion, burns, or pinched insulation. Repair or replace damaged harnesses.
6. **Test the heating element for leakage to ground** by measuring resistance between each heater terminal and the metal chassis with power off. Any continuity indicates breakdown and the heater must be replaced.
7. **If the NTC and heater both test good**, the fault lies in the heater relay or main control board. Consult the wiring diagram to verify relay operation or replace the control module.

## Parts Often Needed

| Part | Notes |
|------|-------|
| NTC temperature sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-washer-f20-error-code&k=NTC+temperature+sensor+%28thermistor%29&tag=errorcodefixes-20) \| Match the connector type and resistance spec to your Bosch washer model number. |
| Heating element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-washer-f20-error-code&k=Heating+element&tag=errorcodefixes-20) \| Verify voltage (120 V or 240 V) and wattage before ordering. Some models use a combined heater and pump assembly. |
| Main control board (electronic module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-washer-f20-error-code&k=Main+control+board+%28electronic+module%29&tag=errorcodefixes-20) \| Required only if relay testing confirms the board is driving the heater incorrectly. Verify your model and software version. |
| Wire harness and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-washer-f20-error-code&k=Wire+harness+and+connectors&tag=errorcodefixes-20) \| Order OEM connectors for the NTC and heater if terminals are corroded or melted. |

## When to Call a Pro

Call a technician if the error persists after a reset, if you are not comfortable working with 120 V or 240 V heating circuits, or if you lack a multimeter and the skills to safely test resistance and continuity on live and de-energized components. Diagnosing F20 requires opening the cabinet, disconnecting harnesses, and isolating whether the NTC sensor, heating element, or control board is at fault. A qualified service tech will follow the field troubleshooting flow: verify the NTC sensor circuit, check the heater relay output, test the heating element for insulation breakdown to chassis, and inspect all wiring before replacing parts. Bosch's own support documentation advises contacting their service network if a power cycle does not resolve the fault, since incorrect part replacement can be expensive and the root cause often requires meter checks that are outside typical homeowner tool sets.

**Rough cost:** A pro service call runs about $150–350 depending on which component needs replacement.
