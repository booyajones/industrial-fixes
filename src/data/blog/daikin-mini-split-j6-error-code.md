---
title: "Daikin J6 Error Code - Causes & Fix"
description: "J6 means the outdoor heat exchanger thermistor has failed or is disconnected. Most common fix: replace the sensor on the coil."
pubDatetime: 2026-06-30T09:58:25Z
modDatetime: 2026-06-30T09:58:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor heat exchanger thermistor"
most_likely_cause: "Failed or open thermistor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the system: turn off the breaker for 5-20 minutes, then restore power to see if the error clears"
  - "Inspect the outdoor unit to confirm the thermistor is securely clipped to the heat exchanger tube and the connector is fully seated"
part_price: "$20-50"
---

## Daikin J6 Error Code — What It Means

The J6 error code on a Daikin mini split signals a malfunction of the outdoor heat exchanger thermistor (temperature sensor) or a problem in its connection circuit. The outdoor unit control board detects an incorrect resistance value from the sensor (often labeled R4T in service manuals), which monitors the outdoor coil temperature. When this sensor fails or disconnects, the system cannot accurately control refrigerant temperature or detect freeze-up conditions, so it stops operation to prevent damage.

This fault points specifically to the outdoor coil sensor, not the indoor unit or other thermistors. The control board expects a resistance value in a specific range (typically around 10 kΩ at 25°C for many Daikin models, but consult your model's service manual). If it reads zero ohms (shorted), infinite resistance (open), or an out-of-range value, the J6 code appears.

## Before You Replace Anything

Some technicians replace the outdoor PCB first when the thermistor itself is the problem. Always test the thermistor resistance with a multimeter and warm it with your hand to confirm it changes value before ordering a new control board.

[Jump to Fix](#fix)

## Common Causes

- **Open or shorted thermistor (~45%)** The sensor itself has failed internally, showing infinite resistance (open) or zero resistance (shorted) instead of the expected value.
- **Disconnected or corroded wiring (~30%)** The two-wire connector between the thermistor and the outdoor PCB is loose, corroded, or the wire is broken.
- **Defective outdoor PCB (~15%)** The control board's input circuit for the thermistor has failed, even when the sensor is functioning correctly.
- **Poor sensor placement (~10%)** The thermistor is not securely clipped to the heat exchanger tube, leading to erroneous temperature readings.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did the error clear after a 5-20 minute power reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient glitch. Monitor the system for recurrence.<br><strong>No:</strong> The thermistor or its circuit has a persistent fault. Proceed to electrical testing.</div>
</details>

<details class="dtree"><summary>Is the thermistor connector firmly seated and the sensor clipped to the coil?</summary>
<div class="dtree-body"><strong>Yes:</strong> Physical connections are good. Test the sensor resistance with a multimeter.<br><strong>No:</strong> Reconnect the plug fully and secure the sensor clip. Restore power and check if the error clears.</div>
</details>

<details class="dtree"><summary>Does the thermistor resistance read between 10-15 kΩ at room temperature and drop when you warm it with your hand?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is good. Check the outdoor PCB input circuit or call a technician.<br><strong>No:</strong> The thermistor is defective. Replace it.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the indoor and outdoor units at the breaker. Wait 5-20 minutes to allow the control board to fully reset, then restore power and check if the error clears.
2. **Access the outdoor unit** and locate the heat exchanger thermistor (a small sensor clipped to one of the coil tubes, with a two-wire connector running to the PCB).
3. **Inspect the sensor and wiring** for visible damage, corrosion, or a loose connector. make sure the thermistor is securely clipped to the heat exchanger tube.
4. **Disconnect the thermistor** from the outdoor PCB. Set your multimeter to ohms (kΩ scale) and measure the resistance across the two thermistor leads.
5. **Compare the reading** to the expected value (typically 10-15 kΩ at 25°C, but consult your model's service manual). The value should never be zero ohms (shorted) or infinite (open). Warm the sensor with your hand and confirm the resistance drops, which is normal thermistor behavior.
6. **Test the PCB circuit** if the thermistor resistance is correct. Measure resistance between the PCB terminals (where the sensor plugs in) to rule out a board failure. If the PCB shows an open circuit, the outdoor control board is defective.
7. **Replace the faulty component** identified in the steps above. Restore power, run a test cycle, and confirm the J6 error does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor heat exchanger thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-j6-error-code&k=Daikin+outdoor+heat+exchanger+thermistor&tag=errorcodefixes-20) \| Match the part number in your service manual or note the resistance rating (typically 10 kΩ at 25°C). |
| Daikin outdoor unit PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-j6-error-code&k=Daikin+outdoor+unit+PCB&tag=errorcodefixes-20) \| Only if the thermistor tests good and the PCB input circuit is open or shorted. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with the outdoor unit, if you do not own a multimeter or have no experience testing electrical components, or if the thermistor tests good and the fault points to the outdoor PCB. Refrigerant-system work and control-board replacement require EPA certification and specialized tools. A technician will test the sensor, verify wiring continuity, and replace the correct component. If you replace the thermistor yourself and the error persists, professional diagnostics of the PCB are needed to avoid unnecessary parts swaps.

**Rough cost:** A pro service call runs about $150-300.

## See Also

- [Daikin VRV System Error Codes: Complete Guide](/posts/daikin-vrv-error-codes/)
- [Daikin H9 Error Code - Causes & Fix](/posts/daikin-heat-pump-h9-error-code/)
- [Daikin U0 Error Code - Causes & Fix](/posts/daikin-heat-pump-u0-error-code/)
- [Daikin A7 Error Code - Causes & Fix](/posts/daikin-mini-split-a7-error-code/)
