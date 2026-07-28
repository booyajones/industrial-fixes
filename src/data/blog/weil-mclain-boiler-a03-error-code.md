---
title: "Weil-McLain A03 Error - Causes & Fix"
description: "A03 is a high-temperature lockout from poor water flow. Most often caused by scale buildup in the plate heat exchanger."
pubDatetime: 2026-06-30T10:15:23Z
modDatetime: 2026-06-30T10:15:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Primary loop circulator pump"
most_likely_cause: "Scale buildup in the plate heat exchanger"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Listen for the primary circulator pump running when the boiler calls for heat"
  - "Check for air in the system by opening a zone bleeder valve"
---

## What this code means
The A03 error is a high-temperature lockout that occurs when your Weil-McLain boiler's internal temperature sensor detects the unit has overheated beyond a safe limit. This is a hard lockout, meaning the boiler will not restart until you manually reset it after correcting the problem.

The boiler overheats because heat is not being removed fast enough, almost always due to poor water circulation through the system. The control shuts down the burner to prevent damage to the heat exchanger and other components.

## Before You Replace Anything

Homeowners and techs sometimes replace the temperature sensor first, but sensor failures are rare. Instead, check water flow through the plate heat exchanger and verify the circulator pump is running before replacing any sensor.

## Common Causes

- **Scaled plate heat exchanger (~55%)** Mineral deposits from hard water block flow through the narrow channels of the plate heat exchanger, preventing heat transfer and causing the boiler to overheat.
- **Failed primary loop circulator (~25%)** The circulator pump motor has died or the impeller is broken, clattering, or unable to move water through the boiler.
- **Air trapped in the system (~10%)** Air pockets block water flow through the heat exchanger or zones, preventing proper heat removal.
- **Faulty zone circulator pump (~8%)** A failed zone pump outside the boiler prevents water from circulating through the heating loop.
- **Defective temperature sensor (~2%)** The sensor itself has failed and is sending a false high-temperature reading to the control board.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Can you hear or feel the primary circulator pump running when the boiler calls for heat?</summary>
<div class="dtree-body"><strong>Yes:</strong> The pump is working, so the problem is likely a blockage in the plate heat exchanger or trapped air in the system.<br><strong>No:</strong> The circulator has failed and needs replacement, or the control board is not sending power to it.</div>
</details>

<details class="dtree"><summary>Does the error occur during or immediately after the burner fires?</summary>
<div class="dtree-body"><strong>Yes:</strong> This points to a flow restriction (scaled heat exchanger) or air blocking circulation during the heating cycle.<br><strong>No:</strong> If the error occurs during post-purge (after the burner shuts off), the pump may be stopping too soon or water flow is still restricted.</div>
</details>

<details class="dtree"><summary>Do you have hard water and no water softener installed?</summary>
<div class="dtree-body"><strong>Yes:</strong> Scale buildup in the plate heat exchanger is highly likely and should be your first check.<br><strong>No:</strong> Look for mechanical pump failure, air in the system, or a rare sensor fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check lockout history** by holding the UP and DOWN buttons for 10 seconds to enter the Contractor Menu, then navigate to Diagnostics > Errors > Lockout History to confirm A03 and note the temperature delta.
2. **Inspect the primary circulator pump** by listening for clattering sounds or feeling for vibration and heat while it runs, indicating the impeller is moving water.
3. **Remove and inspect the plate heat exchanger** by isolating and removing it from the boiler, then looking through the openings with a light to check for white or brittle scale buildup.
4. **Clean the plate heat exchanger** if scale is present by filling it with water and shaking vigorously to dislodge deposits, repeating until water runs clear.
5. **Purge air from the system** by opening bleeder valves on each zone with a hose attached, running water until all air is expelled.
6. **Test the temperature sensor** if all other checks pass by measuring its resistance against the manufacturer's specifications in the manual to rule out a false reading.
7. **Reset the boiler** once the fault is corrected by pressing the Reset button for one second to clear the lockout and restart operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Primary loop circulator pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a03-error-code&k=Primary+loop+circulator+pump&tag=errorcodefixes-20) \| Replace if the impeller is broken, clattering, or the motor is dead |
| Plate heat exchanger | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a03-error-code&k=Plate+heat+exchanger&tag=errorcodefixes-20) \| Only replace if cleaning does not restore flow or if the exchanger is cracked or damaged |
| High-temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a03-error-code&k=High-temperature+sensor&tag=errorcodefixes-20) \| Replace only after confirming all flow issues are resolved and the sensor tests out of spec |

## When to Call a Pro

Call a licensed boiler technician for an A03 code. This error involves diagnosing water flow through a pressurized hydronic system, removing and cleaning or replacing the plate heat exchanger, testing electrical components, and verifying safe operation of a gas-fired appliance. A pro has the tools to measure flow rates, test sensors accurately, and access the Contractor Menu diagnostics. They can also check combustion and make sure the boiler operates safely after the repair. Attempting this repair yourself risks gas leaks, water damage, or improper operation that could damage the boiler or create a safety hazard.

**Rough cost:** A pro service call runs about $150-400.
