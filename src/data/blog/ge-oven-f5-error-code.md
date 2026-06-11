---
title: "GE Oven F5 Error Code - Causes & Fix"
description: "F5 on a GE oven signals a control-board fault. The most common fix is replacing the Electronic Oven Control (EOC) board."
pubDatetime: 2026-06-08T06:27:53Z
modDatetime: 2026-06-08T06:27:53Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - oven
  - ge
most_likely_cause: "Failed ERC/EOC control board"
likelihood: "the most common cause"
diy_or_pro: "diy"
money_part: "ERC/EOC control board (Electronic Oven Control)"
---

## GE Oven F5 Error Code — What It Means

The F5 code on a GE oven indicates a problem in the supervisory control circuit, with the Electronic Range Control or Electronic Oven Control (ERC/EOC) board as the primary suspect. The control board has detected an internal logic fault or a problem in the circuits it monitors. This is not a temperature-sensor code in GE's diagnostic system, though sensor wiring or sensor faults can sometimes mislead the control and contribute to the problem.

The fault typically appears during preheat or normal operation and may lock out the oven. The code points to the control board itself or related wiring and connectors in the control circuit, rather than pointing to a specific heating element or sensor as the direct cause.

## Before You Replace Anything

Homeowners often replace the oven temperature sensor first, assuming F5 is a sensor code. Check the sensor resistance with a multimeter (field rule of thumb is 1,000 to 1,100 ohms at room temperature) and inspect all harness connectors before ordering the sensor, because the control board is the usual culprit in GE F5 cases.

[Jump to Fix](#fix)

## Common Causes

- **Failed ERC/EOC control board (~60%)** An internal logic fault or component failure inside the Electronic Oven Control triggers F5 and is the most frequent root cause.
- **Loose or corroded control-circuit connector (~20%)** Heat, vibration, or age can loosen pins or corrode the harness connector between the control board and sensor or safety inputs.
- **Damaged wiring harness (~10%)** Chafed, pinched, or burned wires in the control circuit can create intermittent opens or shorts that the control reads as a fault.
- **Faulty oven temperature sensor or RTD (~8%)** A sensor that has drifted out of range or gone open-circuit can send bad data to the control, though the control board remains the main suspect.
- **Heat-damaged traces on the control board (~2%)** Prolonged high heat near the board can crack solder joints or char traces, causing intermittent faults that show up as F5.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the F5 code clear and stay away after a 5-minute power reset at the breaker?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient glitch. Monitor the oven over the next few uses. If F5 returns, proceed with board and wiring inspection.<br><strong>No:</strong> The fault is persistent. Inspect the control board area, connectors, and harness for visible damage, then test the oven sensor resistance.</div>
</details>

<details class="dtree"><summary>Are any connectors on the control board or sensor harness loose, corroded, or visibly burned?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean or replace the damaged connector and harness. Reconnect firmly, restore power, and retest. If F5 persists, the control board has likely failed.<br><strong>No:</strong> The wiring appears intact. Measure the oven temperature sensor resistance. If the sensor tests within the expected range and F5 continues, replace the control board.</div>
</details>

<details class="dtree"><summary>Does the oven temperature sensor measure between roughly 1,000 and 1,100 ohms at room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is probably fine. The control board is the likely cause. Confirm no wiring faults exist, then replace the ERC/EOC.<br><strong>No:</strong> The sensor is out of range or open. Replace the sensor, clear the code, and retest. If F5 returns, the control board also needs replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the circuit breaker and wait five minutes to reset the control board's memory.
2. **Restore power** and observe whether F5 returns immediately or stays cleared during a test cycle.
3. **Pull the oven out** (or remove the back access panel for a wall oven) to access the control board and wiring harness behind the control panel.
4. **Inspect all connectors** on the ERC/EOC board and the oven temperature sensor harness for loose pins, corrosion, heat discoloration, or burned insulation.
5. **Measure the oven sensor resistance** with a multimeter at the sensor connector (disconnect it first). Compare the reading to the field rule of thumb of 1,000 to 1,100 ohms at room temperature, or consult your model's wiring diagram for the exact specification.
6. **Check continuity** in each wire of the sensor harness from the sensor to the control board to rule out open or intermittent connections.
7. **Replace the ERC/EOC control board** if connectors and sensor test normally and F5 persists. Transfer all harness plugs to the new board, secure it with mounting screws, restore power, and run a bake cycle to confirm the fault is cleared.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ERC/EOC control board (Electronic Oven Control) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-oven-f5-error-code&k=ERC%2FEOC+control+board+%28Electronic+Oven+Control%29&tag=errorcodefixes-20) \| Match your oven's model number exactly. The board is model-specific and not interchangeable across GE ranges. |
| Oven temperature sensor / RTD probe | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-oven-f5-error-code&k=Oven+temperature+sensor+%2F+RTD+probe&tag=errorcodefixes-20) \| Only replace if resistance is out of range or the probe is visibly damaged. Verify the connector and harness first. |
| Wiring harness or connector kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-oven-f5-error-code&k=Wiring+harness+or+connector+kit&tag=errorcodefixes-20) \| Order if you find melted, corroded, or broken pins that cannot be cleaned and repaired. |

## When to Call a Pro

Call a professional if you are uncomfortable working inside the oven's control-panel area or if you cannot safely isolate power at the breaker. Also call a tech if you replace both the sensor and the control board and F5 continues to appear, because that points to a less common fault such as a short in a concealed harness run or a grounding issue that requires advanced diagnostics and possibly a wiring-diagram trace. If your oven is still under warranty or you lack a multimeter and soldering skills to repair connectors, professional service is the safer choice.

**Rough cost:** DIY runs about $100–250 for a control board, 45–90 min. A pro service call runs about $200–400 including labor.
