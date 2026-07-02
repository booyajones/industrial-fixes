---
title: "Daikin H9 Error Code - Causes & Fix"
description: "H9 means a bad outdoor air temperature sensor. Most often the sensor itself has failed. Replace the thermistor for about $15."
pubDatetime: 2026-06-30T09:56:56Z
modDatetime: 2026-06-30T09:56:56Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor suction air thermistor"
most_likely_cause: "Failed outdoor suction air thermistor"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Power-cycle the system: turn off the AC, disconnect power for 10 minutes, restore power, and check if H9 clears (transient board glitch)."
  - "Inspect the outdoor unit sensor clip and wiring harness for obvious damage, corrosion, or a loose connector at the board."
part_price: "$15-25"
---

## Daikin H9 Error Code — What It Means

The H9 error code signals that your Daikin mini split's control board is reading an abnormal resistance from the outdoor suction air temperature thermistor. This sensor monitors the temperature of air entering the outdoor unit. When resistance falls to near zero (short circuit) or climbs to infinite (open circuit), the board cannot accurately track outdoor conditions and throws H9. This is strictly an outdoor unit problem, separate from indoor sensor faults or discharge pipe sensors.

The board expects a specific resistance range at any given temperature. When the thermistor degrades, its internal element breaks or shorts, sending an out-of-range signal. Loose connectors, corroded terminals, or damaged wiring between the sensor and the outdoor PC board can also produce the same fault. In rare cases the board input circuit itself fails even when the sensor is healthy.

## Before You Replace Anything

Some technicians replace the outdoor PC board when the sensor is the actual culprit. Always measure thermistor resistance with a multimeter first-a $15 sensor will show 0 ohms (short) or infinite resistance (open) if bad, saving you the cost of a $300+ board.

[Jump to Fix](#fix)

## Common Causes

- **Failed thermistor (~60%)** The sensor itself has degraded internally, showing a short circuit (near 0 kΩ) or open circuit (infinite resistance), and no longer changes resistance with temperature.
- **Loose or corroded connector (~20%)** The wiring harness plug at the outdoor PC board is not fully seated, or the terminals have corroded, breaking the electrical path to the sensor.
- **Broken sensor wire (~10%)** The wire between the thermistor and the board has been cut, pinched, or burned, creating an open circuit that reads as infinite resistance.
- **Dislodged sensor (~5%)** The thermistor has slipped out of its clip on the outdoor unit's heat exchanger or air inlet, causing intermittent contact or exposure to direct metal that skews the reading.
- **Faulty outdoor PC board input (~5%)** The inverter control board has a damaged input circuit that cannot read the sensor correctly, even when the sensor and wiring test normal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the H9 error clear after a 10-minute power cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a transient board glitch. Monitor the system for a few days; if H9 does not return, no further action is needed.<br><strong>No:</strong> The fault is persistent. Proceed to test the outdoor suction air thermistor with a multimeter.</div>
</details>

<details class="dtree"><summary>With the sensor unplugged, does the thermistor measure 0 ohms or infinite resistance at room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is shorted or open and must be replaced. Order a new outdoor suction air thermistor for your model.<br><strong>No:</strong> The sensor resistance is in a normal range (typically 2–10 kΩ at room temperature). Inspect the wiring and board input; if both are clean and tight, the outdoor PC board may need replacement.</div>
</details>

<details class="dtree"><summary>When you gently warm the sensor with your hand, does the resistance drop?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermistor is responding to temperature change, so it is likely healthy. Check the connector and wiring for intermittent faults or replace the board.<br><strong>No:</strong> The sensor is stuck at a fixed resistance and is faulty. Replace it.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the breaker and the outdoor disconnect, then wait 10 minutes. Restore power and check if the H9 code reappears. If it clears, monitor the system for recurring faults.
2. **Locate the outdoor suction air thermistor** near the air inlet or heat exchanger of the outdoor unit. Verify the sensor is securely clipped in its bracket and not touching bare metal surfaces.
3. **Inspect the wiring harness** from the sensor to the outdoor PC board. Look for cuts, burns, corrosion, or a loose connector plug. Reseat the connector firmly if it appears loose.
4. **Disconnect the sensor** from the board. Set your multimeter to the kilo-ohm (kΩ) scale and measure resistance across the thermistor terminals. A healthy sensor will read between 2 kΩ and 10 kΩ at room temperature (consult your model's resistance table for exact values). A reading of 0 Ω or infinite resistance confirms the sensor is faulty.
5. **Perform a temperature test** by gently warming the sensor body with your hand while watching the multimeter. Resistance should decrease smoothly. If the reading stays static or jumps erratically, the sensor is bad.
6. **Replace the thermistor** if resistance is abnormal. Remove the old sensor from its clip, route the new sensor into position, plug it into the board connector, and secure the clip. Clear the error code from the controller or power-cycle the system.
7. **Inspect the outdoor PC board** if the sensor tests normal. Look for burnt traces, blown components, or loose solder joints at the sensor input terminals. If the board shows damage or the error persists with a known-good sensor, replace the outdoor PC board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor suction air thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h9-error-code&k=Daikin+outdoor+suction+air+thermistor&tag=errorcodefixes-20) \| Match your exact model number; resistance curve varies by unit. |
| Daikin outdoor inverter control board (PC board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h9-error-code&k=Daikin+outdoor+inverter+control+board+%28PC+board%29&tag=errorcodefixes-20) \| Only if sensor and wiring test good but H9 persists. |

## When to Call a Pro

Call a professional if you are uncomfortable working with live electrical connections or if you lack a multimeter to test sensor resistance. A licensed HVAC technician can quickly measure the thermistor, verify wiring continuity, and replace the sensor or board as needed. Also call a pro if the H9 code returns after you have replaced the sensor and confirmed correct installation, since the outdoor PC board may require replacement or the system may have a refrigerant-side fault that needs refrigerant gauges and recovery equipment.

**Rough cost:** DIY runs about $15-25 in parts, 30-60 min. A pro service call runs about $150-300.
