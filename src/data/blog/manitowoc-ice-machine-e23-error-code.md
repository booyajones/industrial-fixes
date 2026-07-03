---
title: "Manitowoc E23 Error Code - Causes & Fix"
description: "E23 signals a T3 temperature sensor fault on the evaporator plate. Replace the sensor (10kΩ type) or repair its wiring to fix."
pubDatetime: 2026-07-01T10:08:36Z
modDatetime: 2026-07-01T10:08:36Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - manitowoc
money_part: "Manitowoc T3 Temperature Sensor (10kΩ)"
most_likely_cause: "Failed T3 sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the T3 sensor wiring harness (KE4) from the evaporator to the control board for visible breaks, pinches, or corrosion"
  - "Reseat the T3 connector at the control board and check that it is fully seated and clean"
part_price: "$50-90"
---

## Manitowoc E23 Error Code — What It Means

The E23 error code on a Manitowoc ice machine indicates a T3 Temperature Sensor fault. The control board is not receiving a valid temperature reading from the sensor mounted inside the evaporator plate (the flat surface where ice forms). The sensor circuit is either open, shorted, or providing a resistance value outside the expected range, so the machine halts production because it cannot monitor the freezing process accurately.

The T3 sensor is physically located inside the evaporator, not on the discharge line or condenser. When the machine throws E23, it means the control board sees no valid signal or an out-of-spec resistance reading from that probe. Fixing the error requires diagnosing whether the sensor itself has failed, the wiring is damaged, or the control board's input circuit is faulty.

## Before You Replace Anything

Technicians sometimes replace the control board when the problem is just a corroded connector or broken wire at the KE4 harness. Always measure sensor resistance (should be approximately 10kΩ at room temperature) and inspect the wiring before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Failed T3 sensor (~45%)** The probe itself has internally failed due to age or thermal stress, showing infinite resistance (open circuit) or zero ohms when tested with a multimeter.
- **Loose or corroded wiring (~30%)** The connection at the control board (often labeled KE4) or the sensor connector is loose, corroded, or has a damaged cable.
- **Control board relay failure (~15%)** The relay on the control board that reads the sensor circuit is not opening or closing correctly, mimicking a sensor fault even when a new sensor is installed.
- **Scale buildup on the evaporator (~10%)** Extreme mineral deposits insulate the T3 sensor and cause it to read stagnant or incorrect temperatures relative to the plate's actual state.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the diagnostic menu show a T3 reading or just dashes/error?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is communicating with the board. Check if the reading changes with temperature (should be around 10kΩ at room temperature, higher when cold). If it does not change, replace the sensor.<br><strong>No:</strong> The board is not seeing the sensor at all. Inspect the wiring harness and connector for breaks or corrosion, then test sensor resistance with a multimeter.</div>
</details>

<details class="dtree"><summary>When you measure resistance across the T3 sensor leads (disconnected from the board), do you read approximately 10,000 ohms at room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is good. The fault is in the wiring or the control board's input circuit. Trace the harness for damage or replace the board.<br><strong>No:</strong> The sensor is failed (open or shorted). Replace it with a 10kΩ temperature sensor and reset the machine.</div>
</details>

<details class="dtree"><summary>After replacing the T3 sensor, does the E23 error clear and stay off through a full freeze cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor was the problem. Monitor for a few cycles to confirm the fix is stable.<br><strong>No:</strong> The control board's sensor input circuit is faulty. Replace the control board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access diagnostic mode** by pressing the blue "i" button on Indigo NXT models (or holding the Power button for 5 seconds on older Indigo models) and view real-time T3 sensor readings.
2. **Disconnect power** to the machine at the breaker or service switch before working on any electrical components.
3. **Unplug the T3 sensor** from the control board connector (often labeled KE4) and inspect the connector pins and harness for corrosion, breaks, or pinches.
4. **Measure resistance** across the T3 sensor leads with a multimeter. At 25°C (77°F), you should read approximately 10kΩ (10,000 ohms). At 0°C (32°F), expect around 30kΩ. If you read infinite resistance (open circuit) or zero ohms, the sensor is failed.
5. **Replace the sensor** if the resistance is out of spec. Order an OEM 10kΩ temperature sensor and install it in the evaporator plate, routing the wire carefully through the harness.
6. **Reconnect the sensor** to the control board, restore power, and enter diagnostic mode again to verify the T3 reading is now stable and changes with temperature.
7. **Reset the machine** using the on-screen reset function or by cycling power. Monitor the unit through a complete freeze cycle to confirm the E23 error does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Manitowoc T3 Temperature Sensor (10kΩ) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e23-error-code&k=Manitowoc+T3+Temperature+Sensor+%2810k%CE%A9%29&tag=errorcodefixes-20) \| OEM evaporator sensor; verify your model number before ordering |
| Manitowoc Control Board (Indigo series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e23-error-code&k=Manitowoc+Control+Board+%28Indigo+series%29&tag=errorcodefixes-20) \| Only if the sensor and wiring test good but the error persists |

## When to Call a Pro

Call a qualified commercial refrigeration technician for E23 errors. Diagnosing the fault requires working inside the machine's electrical cabinet, measuring sensor resistance with a multimeter, and accessing the evaporator compartment where the T3 sensor is mounted. Replacing the sensor involves routing wiring through sealed or tight spaces and verifying the refrigerant system is not affected. If the control board is at fault, the technician will need to swap the board and reprogram machine settings. Commercial ice machines also require periodic cleaning and scale removal, which a tech can handle during the same visit to prevent future sensor errors.

**Rough cost:** A pro service call runs about $200-400.
