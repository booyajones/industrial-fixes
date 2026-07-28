---
title: "Hoshizaki E9 Error Code - Causes & Fix"
description: "Hoshizaki E9 means compressor overload or condenser thermistor fault. Most common fix: clean the condenser coils to lower head pressure."
pubDatetime: 2026-07-01T10:04:30Z
modDatetime: 2026-07-01T10:04:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - hoshizaki
money_part: "Condenser fan motor"
most_likely_cause: "Dirty condenser coils or blocked airflow causing high head pressure"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Clean the condenser coils and intake vent of dust and debris"
  - "Verify the condenser fan motor is running when the unit tries to start"
  - "Cycle power (Off, On, Ice) and run one full cycle to see if the error clears"
no_buy_pct: "60%"
---

## What this code means
The Hoshizaki E9 error code has two definitions depending on your model. On most machines, it indicates a compressor overload condition: the control board detects the compressor is drawing excessive current or cannot run due to high system pressure, and shuts down to protect the motor. On certain models (some KM-series and older boards), E9 (labeled EE(E9)) instead means the condenser thermistor is open or shorted for 2 seconds, stopping the unit. Note that models like the IM-500SAA do not use a condenser thermistor, so on those machines E9 is strictly a compressor overload fault.

Because the code has two meanings, check your service manual or wiring diagram to confirm which applies to your specific model. The repair steps differ: overload faults are usually caused by high head pressure from a dirty condenser or failed fan, while thermistor faults point to a wiring or sensor problem.

## Before You Replace Anything

Technicians sometimes replace the compressor when the real cause is a dirty condenser or failed fan motor. Clean the condenser and verify the fan runs before condemning the compressor.

## Common Causes

- **Dirty condenser coils or blocked airflow (~40%)** Dust and debris on the condenser or blocked intake vents push head pressure high enough to trip the compressor overload protection.
- **Failed condenser fan motor (~20%)** If the fan does not run, the condenser cannot reject heat and head pressure spikes, causing compressor overload.
- **Condenser thermistor open or shorted (~15%)** On models that use a condenser thermistor, a break or short in the sensor or its wiring triggers the E9 fault (specific to certain boards).
- **Low or high supply voltage (~10%)** Voltage outside the 92V to 147V range can cause the compressor to draw high amps or fail to start, tripping overload.
- **Refrigerant system fault (~10%)** Low refrigerant charge causes overheating, while overcharge or restriction drives head pressure too high.
- **Failing compressor (~5%)** Internal winding damage or mechanical binding raises current draw and trips the overload protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the condenser fan run when the machine tries to start?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan motor is working; move to cleaning the condenser coils and checking voltage.<br><strong>No:</strong> The fan motor has failed or lost power; test the motor windings and replace the fan if needed.</div>
</details>

<details class="dtree"><summary>Are the condenser coils visibly dusty or clogged?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the coils thoroughly with a brush or vacuum, then reset and test; this often clears the E9.<br><strong>No:</strong> The condenser is clean; check supply voltage and test the condenser thermistor (if your model has one).</div>
</details>

<details class="dtree"><summary>Does the error clear after a power reset and stay off for a full cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> It may have been a one-time voltage dip or transient fault; monitor for recurrence.<br><strong>No:</strong> The fault is persistent; proceed to electrical diagnostics and refrigerant pressure checks.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power reset:** Turn the power switch to Off, wait 30 seconds, then turn to On and Ice. If the code clears and the machine completes a full cycle without returning, it may have been a transient fault.
2. **Clean the condenser:** Inspect the intake vent and condenser coils for dust, lint, and debris. Use a soft brush or vacuum to clean thoroughly. A blocked condenser is the most common cause of compressor overload.
3. **Verify fan operation:** Watch the condenser fan motor when the unit tries to start. If the fan does not spin, test the motor windings with a multimeter and replace the fan if it is open or shorted.
4. **Check supply voltage:** Measure incoming voltage with the machine running. Confirm it stays between 92V and 147V. Low voltage (below 92V) causes high amp draw and can trigger overload.
5. **Test the condenser thermistor (if applicable):** Access the condenser thermistor and measure its resistance. If you read 0Ω (short) or infinite (open), the sensor is faulty. If resistance is within spec, inspect the wiring harness for breaks or shorts.
6. **Inspect refrigerant pressure:** Use manifold gauges to check head pressure. High pressure indicates a dirty condenser, restriction, or overcharge. Low pressure points to a refrigerant leak or undercharge. Consult your model's pressure table for target values.
7. **Check compressor amperage:** If the compressor hums but will not start, or draws amps above the nameplate rating, the compressor windings or internal mechanics are likely failing and the compressor needs replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Condenser fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e9-error-code&k=Condenser+fan+motor&tag=errorcodefixes-20) \| Match the voltage, CFM, and mounting pattern to your model's service manual. |
| Condenser thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-ice-machine-e9-error-code&k=Condenser+thermistor&tag=errorcodefixes-20) \| Only for models that use a condenser thermistor; verify the resistance spec in your wiring diagram. |

## When to Call a Pro

Call a qualified refrigeration technician if you are not comfortable working with high-voltage components, refrigerant systems, or compressor diagnostics. Cleaning the condenser and verifying the fan are safe homeowner tasks, but testing refrigerant pressures, recovering refrigerant, and replacing the compressor require EPA certification and specialized equipment. If the error persists after cleaning and resetting, or if you measure abnormal voltage or compressor amps, professional diagnosis is needed to avoid replacing expensive parts by mistake.

**Rough cost:** A pro service call runs about $150-400.
