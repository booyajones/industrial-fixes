---
title: "Weil-McLain A16 Error Code - Causes & Fix"
description: "A16 means the outdoor temperature sensor is missing or disconnected. Most common fix: connect the sensor to the correct terminals or exempt it."
pubDatetime: 2026-07-01T09:55:52Z
modDatetime: 2026-07-01T09:55:52Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain AquaBalance outdoor temperature sensor kit"
most_likely_cause: "No sensor installed or wires disconnected from the control module"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the outdoor sensor wires are plugged into the correct Outdoor Reset terminals on the control module, not DHW or other contacts"
  - "Press and hold the RESET button for 1.5 seconds to clear the fault after confirming connections"
no_buy_pct: "60%"
---

## Weil-McLain A16 Error Code — What It Means

The A-16 error code on a Weil-McLain AquaBalance Central Heating Only boiler indicates the outdoor temperature sensor is not connected or installed. The control module detects an open circuit at the outdoor sensor input terminals during startup and halts the heating call until the fault is cleared. If an outdoor sensor is not physically present and has not been exempted in the system parameters, the boiler will display A-16 and refuse to fire. A faulty sensor that gives extreme readings or a short circuit typically triggers a different fault (F-39), so A-16 specifically points to a missing or disconnected sensor.

## Before You Replace Anything

Homeowners sometimes replace the control module thinking the board is bad, when the real issue is simply a missing sensor or loose wiring at the outdoor reset terminals. Measure resistance across the sensor wires (should be 8,000-15,000 ohms) before buying any parts.

[Jump to Fix](#fix)

## Common Causes

- **No sensor installed (~40%)** The outdoor temperature sensor is physically missing, and the system has not been set to exempt the sensor via the parameter menu.
- **Loose or disconnected wiring (~30%)** Sensor wires are not properly seated in the control module terminals or have come loose during service.
- **Wrong terminal connection (~15%)** The sensor wires are plugged into incorrect terminals (such as DHW instead of Outdoor Reset), creating an open circuit at the expected input.
- **Fault not cleared after repair (~10%)** The sensor was installed or reconnected but the A-16 fault was not manually reset, so the code persists.
- **Damaged wiring harness (~5%)** The sensor cable is chafed, broken, or has an internal open circuit between the sensor head and the boiler.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an outdoor temperature sensor physically installed on the exterior of the building?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check that the sensor wires are connected to the correct Outdoor Reset terminals on the control module and measure resistance (should be 8,000-15,000 ohms). If resistance is out of range or open, replace the sensor.<br><strong>No:</strong> Decide if you need outdoor reset control. If not, exempt the sensor by holding ECO + DHW+ for 10 seconds, navigating to the outdoor sensor parameter, and changing the value to 1. If you do need it, install the sensor and connect it to the correct terminals.</div>
</details>

<details class="dtree"><summary>After confirming or exempting the sensor, did you press and hold the RESET button for 1.5 seconds?</summary>
<div class="dtree-body"><strong>Yes:</strong> Start a heating call from the thermostat. If A-16 clears and the boiler fires, the repair is complete. If the code returns, inspect the wiring harness for damage or intermittent connection.<br><strong>No:</strong> The fault will not clear on its own. Press and hold RESET for 1.5 seconds, then restart the heating call.</div>
</details>

<details class="dtree"><summary>Does measuring resistance across the sensor wires at the boiler give 8,000-15,000 ohms?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is good. The problem is likely a loose connection at the terminals or incorrect terminal assignment. Reseat the wires firmly in the Outdoor Reset contacts.<br><strong>No:</strong> If you read 0 ohms or infinite resistance, the sensor is bad or the wiring is broken. Replace the sensor or repair the cable.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify sensor connection.** Confirm the outdoor temperature sensor is physically installed and its wires are plugged into the correct Outdoor Reset terminals on the control module, not DHW or other contacts.
2. **Measure resistance at the boiler.** Disconnect the sensor wires at the boiler terminals and use a multimeter to measure resistance across the two leads. You should see 8,000-15,000 ohms depending on outdoor temperature. If you read 0 ohms or open circuit, the sensor is faulty or the wiring is broken.
3. **Inspect wiring integrity.** Trace the sensor cable from the outdoor unit to the boiler, looking for chafing, pinched insulation, loose connections at the sensor head, or breaks in the wire.
4. **Exempt the sensor (if not needed).** If your installation does not require outdoor reset control, press and hold ECO + DHW+ buttons for 10 seconds to enter the parameter menu. Navigate to the outdoor sensor parameter (default 0) and change it to 1 using the minus button, then exit the menu.
5. **Clear the fault.** After confirming the sensor connection or exempting it, press and hold the RESET button on the boiler control for 1.5 seconds to clear the A-16 code.
6. **Restart the system.** Call for heat from the thermostat and verify the boiler fires normally without displaying A-16. If the code returns, recheck wiring and connections.
7. **Replace the sensor or harness.** If resistance is out of range and wiring is intact, replace the outdoor temperature sensor. If the cable is damaged, replace the wiring harness between the sensor and the boiler.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain AquaBalance outdoor temperature sensor kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a16-error-code&k=Weil-McLain+AquaBalance+outdoor+temperature+sensor+kit&tag=errorcodefixes-20) \| Confirm the exact part number for your boiler model from the installation manual or serial tag. |
| Outdoor sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a16-error-code&k=Outdoor+sensor+wiring+harness&tag=errorcodefixes-20) \| Only needed if the cable is cut, chafed, or shows an open circuit between the sensor and the boiler. |

## When to Call a Pro

Call a qualified boiler technician if you are not comfortable working with low-voltage control wiring or entering the boiler's parameter menu. A technician can quickly verify sensor resistance, trace wiring faults, and configure the system to exempt the sensor if it is not required for your installation. If you have replaced the sensor and wiring and the A-16 code persists, the control module input may be damaged and requires professional diagnosis and replacement. Any work involving gas supply pressure (3.5-11 inches w.c.) or system water pressure (12-15 PSI) also requires a licensed professional.

**Rough cost:** A pro service call runs about $150-300.
