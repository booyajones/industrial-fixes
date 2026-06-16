---
title: "Weil-McLain A18 Error Code - Causes & Fix"
description: "A18/E18 means outlet water over 210°F lockout. Most common cause: faulty supply temperature sensor or poor pump circulation."
pubDatetime: 2026-06-14T11:43:47Z
modDatetime: 2026-06-14T11:43:47Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain supply / outlet temperature sensor"
most_likely_cause: "Faulty supply temperature sensor or loose sensor connection"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the boiler to clear the lockout and see if it returns immediately or only after a heating cycle."
  - "Inspect the supply temperature sensor wiring and connector at the control board for corrosion or loose contacts."
  - "Listen and feel for the circulator pump running during a call for heat to confirm water is actually moving."
part_price: "$40-80"
---

## Weil-McLain A18 Error Code — What It Means

The A18 or E18 fault on a Weil-McLain boiler is a high outlet water temperature lockout. The boiler has detected that the supply water temperature exceeded the manual's limit of 210°F and has shut down to protect itself from damage. This is an overheating event, not a sign the boiler itself is defective. In practice, the cause is usually a failed or misreading temperature sensor, poor water circulation through the heat exchanger, or a control issue that allows heat to build up faster than it can be carried away. The boiler will remain locked out until the root cause is corrected and the fault is cleared.

This fault is distinct from normal operating temperature swings. It indicates the control board received a signal (or lost a proper signal) that suggested dangerously high outlet water. The most common culprits are the supply temperature sensor itself, loose or corroded wiring at the sensor or control board, and a circulator pump that is not moving water properly during a call for heat.

## Before You Replace Anything

Homeowners sometimes replace the control board when the real problem is a bad supply sensor or a stuck circulator pump. Swap the supply and return sensors (if your model allows) or check pump operation before replacing any expensive electronics.

[Jump to Fix](#fix)

## Common Causes

- **Faulty supply temperature sensor (~40%)** The sensor sends a false high-temperature reading to the control board, triggering lockout even when the water is not overheating.
- **Loose or corroded sensor wiring (~25%)** Intermittent connection at the sensor plug or control board causes the board to misread the outlet temperature or default to lockout.
- **Failed or stuck circulator pump (~20%)** The pump does not move water through the heat exchanger, so the boiler heats the same water beyond 210°F and locks out.
- **Swapped or misconnected supply and return sensors (~10%)** If sensors were reversed during service, the board reads return temperature as supply and may lockout incorrectly.
- **Control board fault (~5%)** The board itself fails to interpret sensor signals correctly, though this is less common than sensor or circulation problems.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the circulator pump hum or spin when the boiler tries to fire?</summary>
<div class="dtree-body"><strong>Yes:</strong> The pump is getting power. Check that water is actually flowing by feeling supply and return pipes for a temperature difference. If both pipes stay the same temperature, the pump impeller may be stuck or the system has air or low water.<br><strong>No:</strong> The pump is not running. Check the pump wiring, reset button, and supply voltage. A dead pump will cause the boiler to overheat quickly and lock out on A18.</div>
</details>

<details class="dtree"><summary>Does the fault clear after a power cycle and stay off for at least one full heating cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The lockout was likely a one-time event from a transient spike or air bubble. Monitor the boiler for recurrence and check sensor connections.<br><strong>No:</strong> The fault returns immediately or after brief operation, which points to a sensor or wiring problem that needs replacement or repair.</div>
</details>

<details class="dtree"><summary>When you swap the supply and return temperature sensors, does the fault behavior change or move?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor that travels with the fault is defective. Replace that sensor.<br><strong>No:</strong> Both sensors are likely good, so focus on wiring, the control board, or circulation issues.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** to the boiler at the service switch or breaker before touching any wiring or sensors.
2. **Inspect the supply temperature sensor connector** at the control board and at the sensor itself for corrosion, moisture, or loose pins, and re-seat both ends firmly.
3. **Check the circulator pump operation** by listening for the motor and feeling the supply pipe for warmth and flow during a call for heat.
4. **Swap the supply and return temperature sensors** if your model allows, then restore power and run a heating cycle to see if the fault moves with the sensor.
5. **Replace the supply temperature sensor** if the fault follows it during the swap test or if resistance or voltage readings fall outside the manufacturer's range.
6. **Clear the fault code** using the boiler's reset button or contractor menu, then run a full heating cycle and monitor outlet temperature on the display.
7. **Verify proper circulation** by checking that the supply pipe is hotter than the return pipe by at least 15-20°F during steady firing, confirming the pump is moving water through the heat exchanger.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain supply / outlet temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a18-error-code&k=Weil-McLain+supply+%2F+outlet+temperature+sensor&tag=errorcodefixes-20) \| Order by your boiler model number; sensors are not universal across all Weil-McLain lines. |
| Weil-McLain return temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a18-error-code&k=Weil-McLain+return+temperature+sensor&tag=errorcodefixes-20) \| Used for diagnostic swap or replacement if proven faulty. |
| Circulator pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a18-error-code&k=Circulator+pump&tag=errorcodefixes-20) \| Required if the pump is not moving water; verify pump model and pipe size before ordering. |

## When to Call a Pro

Call a qualified boiler technician whenever the A18 fault returns after checking wiring and resetting the boiler. Proper diagnosis requires comparing sensor resistance values to the manufacturer's table, verifying control board inputs with a multimeter, and testing circulator pump performance under load. Gas-fired boilers also carry combustion and venting risks, so sensor replacement and control board work should be performed by a licensed technician. If you are not comfortable working around 120V wiring, high-temperature water, or gas piping, schedule a service call rather than attempting the repair yourself.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Weil-McLain A02 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a02-error-code/)
- [Weil-McLain Code 3 — Low Water Cutoff Fix](/posts/weil-mclain-error-code-3/)
- [Weil-McLain Boiler A62 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a62-error-code/)
- [Weil-McLain A29 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a29-error-code/)
