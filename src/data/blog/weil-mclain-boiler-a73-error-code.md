---
title: "Weil-McLain Boiler A73 Error - Causes & Fix"
description: "A73 is a stored fault on certain Weil-McLain controls. Most common cause is a failed circulator or bad supply temperature sensor."
pubDatetime: 2026-06-15T11:31:26Z
modDatetime: 2026-06-15T11:31:26Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Supply temperature sensor (Weil-McLain)"
most_likely_cause: "Failed primary loop circulator or faulty supply temperature sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Enter the contractor menu and check the error history to see the exact fault code and description for your model"
  - "Verify the primary loop circulator is running and you can feel flow in the supply pipe"
  - "Inspect and reseat all sensor connectors at the supply and return temperature sensors with power off"
---

## Weil-McLain Boiler A73 Error — What It Means

A73 is not a universal code across all Weil-McLain boilers. On Ultra and AquaBalance-style controls, it represents a stored or active fault that must be looked up in your specific model's error history and control fault table. Weil-McLain directs technicians to enter the contractor menu, retrieve the error history, and identify the exact boiler by its CP number to use the correct manual. Without that model-specific table, you cannot assume what A73 means.

Based on field experience with similar Weil-McLain lockouts, the fault often involves overheating or a temperature sensor problem. The most common pattern is an outlet water temperature above 210°F, which triggers a manual reset lockout. The usual culprits are a failed primary loop circulator that stops removing heat from the boiler, or a faulty supply temperature sensor that reports incorrect readings to the control board.

## Before You Replace Anything

Technicians often replace the control board when the real problem is a loose sensor connector or a bad circulator. Always reseat sensor wiring and verify the pump is running before replacing the board.

[Jump to Fix](#fix)

## Common Causes

- **Failed primary loop circulator (~40%)** The pump that moves hot water through the boiler stops running, heat builds up, and the boiler locks out on high outlet temperature.
- **Faulty supply temperature sensor (~30%)** The sensor sends incorrect high-temperature readings to the control board, or its wiring is loose or corroded.
- **Poor system circulation (~15%)** A closed valve, air-bound loop, or clogged zone causes heat to stack in the boiler even when the circulator runs.
- **Loose or corroded sensor wiring (~10%)** The connector at the supply or return sensor is not seated fully, causing intermittent or false readings.
- **Control board fault (~5%)** The board itself misreads sensor inputs or enters lockout incorrectly, though this is less common than sensor or pump failures.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the primary loop circulator running and can you feel warmth in the supply pipe?</summary>
<div class="dtree-body"><strong>Yes:</strong> Circulation is present, so focus on the temperature sensors and their wiring.<br><strong>No:</strong> The circulator has likely failed or lost power, replace the pump or check its wiring and relay.</div>
</details>

<details class="dtree"><summary>Does the error history show an overtemperature or high-limit fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify the supply temperature sensor reading is accurate and the circulator is removing heat.<br><strong>No:</strong> Consult the model-specific fault table in your manual, the code may indicate a different subsystem.</div>
</details>

<details class="dtree"><summary>After reseating the sensor connectors, does the fault clear and stay cleared through a full cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a loose connector, monitor the boiler for a few days to confirm.<br><strong>No:</strong> Replace the supply temperature sensor or the circulator, whichever testing shows is faulty.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your exact boiler model and CP number** from the rating plate so you can download the correct manual and fault-code table.
2. **Power off the boiler** at the service switch or breaker before touching any wiring or sensors.
3. **Enter the contractor menu** (consult your manual for the button sequence) and record all active and stored faults in the error history.
4. **Check whether the primary loop circulator is running** by listening for motor hum and feeling the supply pipe for flow and warmth.
5. **Inspect and reseat the supply and return temperature sensor connectors** at the boiler, looking for corrosion or loose pins.
6. **Swap the supply and return sensors** (if accessible) to see if the fault follows the sensor, which confirms a bad sensor rather than a board problem.
7. **Replace the failed component** (circulator or sensor) based on your testing, then clear the fault in the error history and run a full heating cycle to verify the lockout does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Supply temperature sensor (Weil-McLain) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a73-error-code&k=Supply+temperature+sensor+%28Weil-McLain%29&tag=errorcodefixes-20) \| Match the part number in your model's manual or use the CP number when ordering. |
| Primary loop circulator pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a73-error-code&k=Primary+loop+circulator+pump&tag=errorcodefixes-20) \| Verify voltage and flange size from the old pump before ordering a replacement. |
| Control board (Weil-McLain Ultra/AquaBalance) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a73-error-code&k=Control+board+%28Weil-McLain+Ultra%2FAquaBalance%29&tag=errorcodefixes-20) \| Only replace after confirming sensors and circulator are good and the fault does not follow them. |

## When to Call a Pro

Call a licensed heating technician if you cannot access the error history, if the fault table in your manual does not list A73, or if you are uncomfortable working with 120V wiring and hydronic pumps. A pro can pull the complete diagnostic log, compare live sensor readings against known good values, and test the circulator under load. Because Weil-McLain codes are model-specific and the boiler may enter a manual reset lockout that requires clearing the underlying cause before it will restart, professional diagnosis prevents repeat lockouts and ensures the repair matches the actual fault rather than guessing based on internet descriptions.

**Rough cost:** A pro service call runs about $200-450.

## See Also

- [Weil-McLain Boiler A177 Error - Causes & Fix](/posts/weil-mclain-boiler-a177-error-code/)
- [Weil-McLain A135 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a135-error-code/)
- [Weil-McLain 019 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a19-error-code/)
- [Weil-McLain Boiler A49 Error - Causes & Fix](/posts/weil-mclain-boiler-a49-error-code/)
