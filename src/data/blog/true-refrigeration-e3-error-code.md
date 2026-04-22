---
title: "True Refrigeration E3 Error Code — Causes & Fix"
description: "What True refrigeration E3 error code means, why defrost termination faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - true
---

## True Refrigeration E3 Error Code — What It Means

True Refrigeration E3 indicates a **defrost termination fault** — the defrost cycle did not terminate normally. True refrigeration units (reach-in coolers, prep tables, display cases) use a defrost heater to melt frost off the evaporator coil periodically. The defrost cycle is supposed to end when either the defrost termination thermostat (or temperature sensor) reaches the setpoint temperature, or the backup timer expires. E3 means the defrost thermostat didn't terminate the cycle as expected — either the thermostat failed to respond or the heater couldn't bring the coil temperature up to the termination point within the time limit.

[Jump to Fix](#fix)

## Common Causes

- **Failed defrost termination thermostat** — The thermostat that ends the defrost cycle fails open, never sending the termination signal; the backup timer eventually shuts off the cycle and logs E3.
- **Failed defrost heater** — The heater element fails (open circuit); no heat is generated, so the coil temperature never reaches the termination point and the cycle times out.
- **Defrost heater wiring fault** — A loose or broken wire to the defrost heater prevents it from running.
- **Excessive frost buildup** — Unusual frost load (door gasket failure, frequent door opening) causes so much ice accumulation that even a functioning heater can't complete defrost in the allotted time.

## Step-by-Step Fix {#fix}

1. **Manually initiate defrost** — On units with a defrost override (check the control panel), manually start a defrost cycle and listen for the heater clicking on. If you hear no change, the heater may not be running.
2. **Check the defrost heater** — With power off, disconnect the defrost heater from its wiring and measure resistance across the heater terminals. A healthy heater reads 15–100 Ω depending on wattage. Open circuit (infinite resistance) = failed heater.
3. **Check the defrost termination thermostat** — With the unit cold and the coil frosted over, the termination thermostat should be closed (conducting). Measure continuity across it. If it reads open at coil temperature, the thermostat has failed open and won't terminate defrost.
4. **Inspect door gaskets** — Poor door seals let warm humid air into the cabinet continuously, creating excessive frost. Close each door and run a dollar bill along the full perimeter of the gasket — resistance should be felt throughout.
5. **Check heater wiring** — Trace heater wires from the timer/controller to the heater. Look for loose terminals, burned connectors, or chafed insulation.
6. **Reset after repairs** — After replacing components, restore power and allow the unit to cycle through a complete refrigeration and defrost cycle. Confirm E3 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Defrost heater | Match wattage and physical length to the original; True OEM or compatible |
| Defrost termination thermostat | Match the setpoint temperature (typically 45–55°F for reach-ins) |
| Door gasket | Replace if the gasket is torn, compressed, or no longer sealing |

## When to Call a Pro

If E3 returns after replacing the heater and thermostat, the defrost timer or electronic controller may have a fault in the defrost timing circuit. True Refrigeration's authorized service network can diagnose the controller board and timer assembly.
