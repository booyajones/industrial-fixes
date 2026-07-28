---
title: "Hoshizaki E6 Error Code - Causes & Fix"
description: "E6 means bin or evaporator thermistor fault (open or shorted sensor). Most likely cause: failed thermistor or damaged wiring harness."
pubDatetime: 2026-07-01T10:02:14Z
modDatetime: 2026-07-01T10:02:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
money_part: "Bin or Evaporator Thermistor"
most_likely_cause: "damaged or open/shorted thermistor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the machine (switch OFF then back to ICE) and run one full cycle to see if the code clears permanently."
  - "Inspect the thermistor wire harness for visible damage, cuts, or loose connections at the control board."
---

## What this code means
The E6 error code on a Hoshizaki ice machine signals a thermistor (temperature sensor) fault for either the ice bin or the evaporator plate. The control board has detected that the sensor's resistance is out of range, either reading as an open circuit (infinite resistance) or a short (zero resistance). This means the sensor cannot accurately report temperature, so the machine stops to prevent damage or poor ice production.

This is not a cleaning issue, a harvest problem (which would show as E1), or a voltage fault (which triggers six beeps without an E6 display). The fault is electrical, pointing to a broken sensor, damaged wiring, or a loose connection between the thermistor and the control board.

## Before You Replace Anything

Technicians sometimes replace the control board first when the real problem is a bad thermistor or corroded wire harness. Always test the sensor resistance with a multimeter before ordering a board.

## Common Causes

- **Damaged or Open/Shorted Thermistor (~50%)** The sensor itself has failed internally after years of thermal cycling, reading infinite or zero resistance instead of a valid temperature-dependent value.
- **Wiring Harness Issues (~30%)** The wire harness connecting the thermistor to the control board is damaged, corroded, or has a broken connection that creates an open circuit.
- **Loose Connections (~15%)** The thermistor wire is unplugged or not seated firmly in the control board connector, breaking the circuit intermittently or permanently.
- **Control Board Failure (~5%)** The control board itself fails to read the sensor correctly, though this is rare and is usually diagnosed only after ruling out the sensor and wiring.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the E6 code clear and stay off after a power cycle (OFF then back to ICE)?</summary>
<div class="dtree-body"><strong>Yes:</strong> It may have been a transient fault. Monitor the machine for one or two cycles. If the code returns, the thermistor or wiring has failed.<br><strong>No:</strong> The fault is persistent. Proceed to visual inspection and electrical testing of the thermistor and harness.</div>
</details>

<details class="dtree"><summary>With the thermistor disconnected, does your multimeter show continuity (not 0 Ω or Open)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermistor is good. Check the wiring harness for damage or test the control board.<br><strong>No:</strong> The thermistor is open or shorted. Replace it.</div>
</details>

<details class="dtree"><summary>Is the thermistor wire harness visibly damaged, corroded, or loose at the control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repair or replace the harness. Re-seat any loose connectors and test the machine.<br><strong>No:</strong> The issue is likely the thermistor itself or, rarely, the control board. Test resistance with a multimeter.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn the power switch OFF**, then back **ON** to the ICE position and run one full ice-making cycle to see if the E6 code clears and stays off.
2. **Inspect the thermistor wire harness** visually for cuts, corrosion, or loose connections at the control board and at the sensor mounting location in the bin or evaporator.
3. **Disconnect the thermistor wire harness** from the control board and set your multimeter to measure resistance (Ohms).
4. **Measure resistance** across the two pins of the harness (or the sensor leads if disconnected). A valid thermistor will show continuity and a resistance value that changes with temperature, not 0 Ω (short) or Open/Infinite (open circuit).
5. **Replace the thermistor** if the resistance reading is 0 Ω or Open. The sensor has failed internally and cannot report temperature.
6. **Replace the wire harness** if the thermistor tests good but the wiring is visibly damaged or corroded.
7. **Replace the control board** only if both the thermistor and wiring test correctly but the E6 error persists after reconnection and power-up.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Bin or Evaporator Thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e6-error-code&k=Bin+or+Evaporator+Thermistor&tag=errorcodefixes-20) \| Match the part number to your specific Hoshizaki model (bin vs. evaporator sensor). |
| Thermistor Wire Harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e6-error-code&k=Thermistor+Wire+Harness&tag=errorcodefixes-20) \| Order if the wiring is damaged but the sensor itself tests good. |
| Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e6-error-code&k=Control+Board&tag=errorcodefixes-20) \| Replace only after confirming the sensor and harness are both functional. |

## When to Call a Pro

Call a qualified refrigeration technician for this repair. The work involves diagnosing live control circuits with a multimeter, accessing sealed components inside a commercial ice machine, and replacing sensors or boards that must match your model's specifications. Incorrect sensor replacement or wiring mistakes can damage the control board or cause the machine to produce unsafe ice. A pro will test the thermistor resistance, verify the harness integrity, and replace only the failed component, avoiding expensive misdiagnosis and ensuring the machine runs reliably.

**Rough cost:** A pro service call runs about $150-300.
