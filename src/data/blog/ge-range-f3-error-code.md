---
title: "GE Range F3 Error Code - Causes & Fix"
description: "F3 means the control sees the oven temperature sensor circuit as open or out of range. Usually fix by replacing the sensor."
pubDatetime: 2026-06-08T02:51:44Z
modDatetime: 2026-06-08T02:51:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - oven
  - ge
most_likely_cause: "failed oven temperature sensor"
likelihood: "the most common cause"
diy_or_pro: "diy"
---

## GE Range F3 Error Code — What It Means

The F3 code on a GE range means the electronic control board thinks the oven temperature sensor circuit has failed open or is reading out of range. The control board cannot trust the sensor reading, so it throws the fault and usually shuts down the oven. In practical terms, the control may see the circuit as above about 2,900 Ω at the board when it expects a healthy sensor to read around 1,100 Ω at room temperature.

The fault can live in the sensor itself, in the two-wire harness and connectors between the sensor and the main control board, or in the control board if the sensor circuit tests good. A technician's approach is to verify the sensor first, then the wiring, and only replace the control board if the sensor circuit is sound but the error persists.

## Before You Replace Anything

Many people replace the main control board (ERC) first. Always test the sensor resistance at room temperature and inspect the harness connectors for corrosion or loose pins before ordering a board.

[Jump to Fix](#fix)

## Common Causes

- **Failed oven temperature sensor (~60%)** The sensor is open, reads out of the normal 1,050-1,150 Ω range at room temperature, or shows continuity to its mounting shell.
- **Loose, corroded, or burned harness connectors (~25%)** The two-pin connector at the sensor or at the control board has poor contact, green corrosion, or heat damage that creates an open circuit.
- **Pinched, melted, or damaged sensor wiring (~10%)** A wire in the sensor circuit is cut, melted by insulation contact with the oven wall, or pinched behind the range, causing an open reading.
- **Faulty main control board (ERC) (~5%)** If the sensor and wiring both test good, the control board itself may be misreading the circuit or have a failed input stage.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the F3 code clear after unplugging the range for 5 minutes and restoring power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may be intermittent or a one-time glitch. Monitor the oven; if F3 returns, proceed to test the sensor.<br><strong>No:</strong> The fault is persistent. Move on to inspecting and testing the temperature sensor and wiring.</div>
</details>

<details class="dtree"><summary>With the sensor disconnected, does it measure 1,050-1,150 Ω at room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is good. Check for continuity and damage in the wiring and connectors between the sensor and control board.<br><strong>No:</strong> The sensor is faulty. Replace it and retest.</div>
</details>

<details class="dtree"><summary>Do you see any melted, pinched, or corroded wires or connector pins in the sensor circuit?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repair or replace the damaged harness section or connector, then clear the code and test the oven.<br><strong>No:</strong> If the sensor and wiring are both good but F3 persists, the main control board is the likely cause.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Kill all power** to the range by unplugging it or switching off the dedicated circuit breaker at the panel.
2. **Reset the control** by leaving power off for about 5 minutes, then restore power and see whether the F3 code returns immediately or after heating.
3. **Access the oven temperature sensor** by removing the oven racks and the rear panel inside the oven cavity (or the external rear panel on some models) to expose the sensor probe and its two-wire connector.
4. **Disconnect the sensor** and use a multimeter set to resistance (Ω) to measure across the two sensor terminals at room temperature; a healthy GE sensor should read approximately 1,100 Ω, typically 1,050-1,150 Ω.
5. **Check for a grounded sensor** by measuring continuity from each sensor terminal to the sensor's metal mounting plate or shell; any continuity there means the sensor is shorted and must be replaced.
6. **Inspect the sensor harness and connectors** from the sensor all the way to the main control board for loose pins, green corrosion, melted insulation, or pinched wires; repair or replace any damaged sections.
7. **Replace the sensor** if it reads open, out of range, or shorted; install the new sensor with thermal paste if supplied, reconnect the harness, restore power, and test the oven.
8. **Replace the main control board (ERC)** only if the sensor measures correctly, the wiring and connectors are sound, and the F3 code still appears after all other checks.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GE oven temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f3-error-code&k=GE+oven+temperature+sensor&tag=errorcodefixes-20) \| Verify the sensor resistance spec and connector style for your model before ordering. |
| Sensor wiring harness or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f3-error-code&k=Sensor+wiring+harness+or+connector&tag=errorcodefixes-20) \| Only needed if the harness is melted, cut, or the connector housing is cracked or burned. |
| GE electronic range control board (ERC) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f3-error-code&k=GE+electronic+range+control+board+%28ERC%29&tag=errorcodefixes-20) \| Order by your range's full model number; only replace after confirming the sensor and wiring are good. |

## When to Call a Pro

Call a professional if you are uncomfortable working with 240-volt wiring, if you cannot safely access the sensor or control board, or if you have tested the sensor and wiring and both are good but the F3 code persists and you prefer not to diagnose or replace the control board yourself. A qualified appliance technician has the tools to test the sensor circuit at the board connector and can confirm whether the board needs replacement or whether an intermittent wiring fault is at play.

**Rough cost:** DIY runs about $20-50 in parts, 30-60 min. A pro service call runs about $150-300.
