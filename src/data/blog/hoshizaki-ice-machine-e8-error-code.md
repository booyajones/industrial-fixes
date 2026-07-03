---
title: "Hoshizaki E8 Error Code - Causes & Fix"
description: "E8 means bin-thermistor fault: the ice-level sensor is open, shorted, or wired wrong. Replace the bin thermistor or fix the harness."
pubDatetime: 2026-07-01T10:03:39Z
modDatetime: 2026-07-01T10:03:39Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
money_part: "Hoshizaki bin thermistor (ice level sensor)"
most_likely_cause: "failed bin thermistor"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Power cycle the machine (switch OFF then back to ICE) and observe if the code returns within 1-2 cycles"
  - "Inspect the bin thermistor wiring for cuts, burns, or loose connections at the sensor and control board"
part_price: "$25-60"
---

## Hoshizaki E8 Error Code — What It Means

The E8 error code on a Hoshizaki ice machine signals a bin-thermistor fault. The bin-full sensor (thermistor) is reading out of range, is open-circuited, or is shorted, so the control board cannot correctly detect whether the ice bin is full. The error triggers when the resistance value from the sensor falls outside the manufacturer's expected window, indicating an electrical failure in the sensor itself or its wiring.

This is distinct from pressure switch faults or defrost thermistor problems, which generate different codes. The machine will not operate normally until the thermistor and its circuit are restored to the correct resistance range.

## Before You Replace Anything

Technicians sometimes replace the control board first. Always measure the thermistor resistance and test the wiring harness continuity before condemning the board.

[Jump to Fix](#fix)

## Common Causes

- **Failed bin thermistor (~60%)** The sensor has degraded internally, showing infinite resistance (open circuit) or zero resistance (short circuit).
- **Wiring harness damage (~25%)** The wire harness connecting the thermistor to the control board is cut, corroded, or disconnected.
- **Control board input fault (~10%)** The control board's thermistor input circuit has failed, though this is usually secondary to a sensor problem.
- **Scale or debris at sensor (~5%)** Physical obstruction or buildup around the sensor area can sometimes produce erratic readings.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did the E8 code clear after a power cycle and stay gone for at least two full ice cycles?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient. Monitor the machine over the next few days. If it returns, proceed to test the thermistor.<br><strong>No:</strong> The thermistor or its wiring has failed. Continue diagnostics by inspecting connections and measuring resistance.</div>
</details>

<details class="dtree"><summary>Does the bin thermistor measure infinite (OL) or zero ohms when you test it with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermistor is open or shorted and must be replaced.<br><strong>No:</strong> Compare the reading to your model's resistance-to-temperature chart. If the value is within spec, test the wiring harness for continuity.</div>
</details>

<details class="dtree"><summary>Does the wiring harness show continuity from the thermistor connector to the control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> The harness is good. If the thermistor is also within spec, the control board input circuit has likely failed.<br><strong>No:</strong> Repair or replace the wire harness between the sensor and the board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the machine** and switch it to the OFF position to safely begin diagnostics.
2. **Locate the bin thermistor** mounted in or near the ice storage bin. Trace its wires to the control board and inspect all connections for corrosion, looseness, or visible damage.
3. **Disconnect the thermistor wires** from the control board. Using a multimeter set to resistance (ohms), measure across the thermistor terminals.
4. **Compare the resistance reading** to the manufacturer's specification curve for your model. A reading of 0 Ω indicates a short, infinite (OL) indicates an open circuit, and any value far outside the specified range confirms the sensor is defective. Consult your model's service manual for the exact resistance-to-temperature table.
5. **Test the wiring harness** for continuity if the thermistor resistance is within spec. Measure from the sensor connector to the board connector to rule out a broken wire.
6. **Replace the bin thermistor** if it is open, shorted, or out of spec. If the harness fails the continuity test, replace the wiring harness.
7. **Reconnect all wiring**, restore power, and switch the machine back to ICE mode. Clear the error by cycling the power. Monitor for two full ice cycles to confirm the fault is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hoshizaki bin thermistor (ice level sensor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e8-error-code&k=Hoshizaki+bin+thermistor+%28ice+level+sensor%29&tag=errorcodefixes-20) \| Match the part number to your specific model year and series |
| Thermistor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e8-error-code&k=Thermistor+wiring+harness&tag=errorcodefixes-20) \| Replace if continuity test fails or connector is corroded |

## When to Call a Pro

Call a commercial refrigeration technician if you are not comfortable working with electrical components or if the thermistor and wiring both test good yet the error persists, indicating a control board fault. Technicians have model-specific resistance charts and can quickly isolate board-level failures. Also call a pro if the machine has refrigerant leaks, compressor issues, or other simultaneous faults that require licensed service.

**Rough cost:** DIY runs about $30-80 in parts, 30-60 min. A pro service call runs about $150-300.

## See Also

- [Hoshizaki Ice Machine E7 Error Code — High-Side Pressure Switch Fault Fix](/posts/hoshizaki-e7-pressure-switch/)
- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki KM-2000SAJ Ice Machine Error Codes - Full Diagnostic Guide](/posts/hoshizaki-km-2000saj-error-codes/)
- [Hoshizaki F2 Error Code — Ice Full Sensor Fault Causes & Fix](/posts/hoshizaki-f2-error-code/)
