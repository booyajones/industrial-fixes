---
title: "Weil-McLain A06 Error Code - Causes & Fix"
description: "A06 means outdoor sensor fault on AquaBalance controls. Usually a missing, disconnected, or failed outdoor sensor or wrong configuration."
pubDatetime: 2026-06-13T12:54:33Z
modDatetime: 2026-06-13T12:54:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain outdoor sensor"
most_likely_cause: "outdoor sensor not installed or disconnected"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify outdoor sensor is installed and cable is plugged firmly into both the sensor and the control terminal block"
  - "Check control programming to confirm outdoor reset parameter matches whether sensor is actually installed"
no_buy_pct: "40%"
---

## What this code means
The A06 code on a Weil-McLain AquaBalance or AquaBalance Series 2 control means the boiler is not getting a valid outdoor temperature input from the outdoor sensor. The control sees the sensor circuit as open, shorted, missing, or otherwise invalid for the configured logic. This is a sensor, wiring, or configuration fault rather than a combustion problem.

On central-heating-only boilers, the outdoor sensor may be intentionally omitted. If the control is still configured to expect the sensor, it will throw A06 at power-up. The fix can be as simple as adjusting the control parameter to exempt the sensor, or as straightforward as reconnecting loose wires or replacing a failed sensor.

## Before You Replace Anything

Some technicians replace the control board before checking the outdoor sensor and its wiring. Always inspect the sensor connections and measure sensor resistance at both ends to confirm the fault before replacing the control module.

## Common Causes

- **Outdoor sensor not installed or configuration mismatch (~35%)** The boiler is set for outdoor reset but the sensor was never installed, or the control parameter still expects the sensor even though it is intentionally omitted on a central-heating-only system.
- **Loose, damaged, or open sensor wiring (~30%)** The two-conductor cable between the outdoor sensor and control has a loose terminal, corroded connection, cut wire, or open circuit.
- **Failed outdoor sensor (~20%)** The outdoor temperature sensor itself is open, shorted, or reading out of range and needs replacement.
- **Shorted sensor wiring (~10%)** The sensor cable is pinched, melted, or shorted to ground, causing an invalid reading at the control input.
- **Control module input problem (~5%)** The outdoor sensor input circuit on the control board itself has failed, though this is far less common than sensor or wiring faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an outdoor sensor actually installed on the exterior of the building?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the sensor wiring and connections at both ends. Disconnect the sensor and measure its resistance to determine if the sensor or wiring is faulty.<br><strong>No:</strong> The control is configured to expect a sensor that is not present. Enter the installer menu and change the outdoor reset parameter to exempt the sensor.</div>
</details>

<details class="dtree"><summary>Is the sensor cable plugged firmly into the control terminal block and does the wiring look intact?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect the sensor at the outdoor end and measure resistance across the sensor leads. If open, shorted, or far outside the expected range, replace the sensor.<br><strong>No:</strong> Reconnect or repair the loose, cut, or corroded wiring. Clear the fault and recheck.</div>
</details>

<details class="dtree"><summary>After replacing the sensor and verifying wiring, does the A06 fault return immediately?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control module input circuit may be damaged. Verify all parameter settings first, then consider replacing the control board.<br><strong>No:</strong> The repair is complete. Monitor the boiler for normal operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the boiler model** and open the manufacturer manual and error table for that specific model before making any changes.
2. **Confirm whether an outdoor sensor is supposed to be installed** on this system. For central-heating-only configurations, the sensor may be intentionally omitted.
3. **Inspect the outdoor sensor location** and its two-conductor cable. Look for loose terminals, corrosion, cuts, pinches, or shorts at the sensor, along the cable run, and at the control terminal block.
4. **Disconnect the sensor at the outdoor end** and measure resistance across the sensor leads using a multimeter. Also measure continuity and resistance from the control terminal end to determine whether the fault is in the sensor or the wiring. Consult your model's table for the expected resistance range.
5. **Replace the sensor** if it is open, shorted, or out of range. Replace or repair the wiring harness if the sensor tests good but the circuit is open or shorted.
6. **Check the control programming** in the installer menu. If the outdoor sensor is not installed and not needed, change the outdoor reset parameter to exempt the sensor.
7. **Clear the fault** using the control interface reset procedure and verify the A06 does not return. Monitor the boiler for normal operation and confirm the display shows valid outdoor temperature if the sensor is installed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain outdoor sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a06-error-code&k=Weil-McLain+outdoor+sensor&tag=errorcodefixes-20) \| Confirm the exact part number for your boiler model before ordering. |
| Outdoor sensor wiring harness or field cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a06-error-code&k=Outdoor+sensor+wiring+harness+or+field+cable&tag=errorcodefixes-20) \| Two-conductor cable rated for outdoor use and the temperature range at the sensor location. |
| AquaBalance control module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a06-error-code&k=AquaBalance+control+module&tag=errorcodefixes-20) \| Only if the sensor input circuit on the board is proven faulty after sensor and wiring are verified good. |

## When to Call a Pro

Call a qualified heating technician for A06 diagnostics and repair. The outdoor sensor circuit requires careful resistance measurement, knowledge of the control parameter menu, and access to the manufacturer specifications for your exact boiler model. If the sensor and wiring are intact, the technician will verify control programming and determine whether a control board replacement is needed. Gas-fired boiler work also requires proper venting checks and combustion analysis after any control repair, so professional service is the safe and correct approach.

**Rough cost:** A pro service call runs about $150-300.
