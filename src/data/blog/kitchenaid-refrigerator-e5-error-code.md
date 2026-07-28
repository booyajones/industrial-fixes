---
title: "KitchenAid Refrigerator E5 Error Code - Causes & Fix"
description: "E5 means ice-maker thermistor or harvest-cycle fault. Most often it's a failed ice-maker assembly requiring replacement."
pubDatetime: 2026-06-08T06:55:08Z
modDatetime: 2026-06-08T06:55:08Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - refrigerator
  - kitchenaid
most_likely_cause: "Failed ice-maker thermistor or temperature sensor inside the ice-maker assembly"
likelihood: "the most common cause"
diy_or_pro: "diy"
money_part: "Ice-maker assembly (KitchenAid/Whirlpool compatible)"
part_price: "$80-180"
---

## What this code means
E5 on KitchenAid refrigerator diagnostics indicates an ice-maker temperature-sensing or harvest-cycle problem. The exact meaning depends on your model platform. On many KitchenAid and Whirlpool designs, E5 in the ice-maker error table signals "Timed Ice Making," meaning the ice maker did not complete a harvest cycle within the expected window, usually because the thermistor or bimetal heater sensor inside the ice-maker assembly failed to detect proper harvest temperature. Some tech sheets also list E5 as "Heater Bimetal Faulty" in a different diagnostic context.

In practice, the most common real-world cause is a failed ice-maker thermistor or temperature sensor built into the ice-maker module. Because these sensors are embedded and not sold separately, the typical repair is to replace the entire ice-maker assembly. Incomplete harvest, slow ice production, or trays that stay partially filled with water are all symptoms that match this fault. Always pull your model's tech sheet and confirm which diagnostic table applies before ordering parts, because KitchenAid assigns different meanings to E5 across platforms.

## Before You Replace Anything

Many owners replace the main control board or assume a compressor problem when the refrigerator compartment runs warm. Run the ice-maker harvest and fill tests in service diagnostics first to confirm the E5 is isolated to the ice maker before spending money elsewhere.

## Common Causes

- **Failed ice-maker thermistor or temperature sensor (~60%)** The sensor inside the ice-maker module does not read mold temperature correctly, so the harvest cycle times out and the control logs E5.
- **Heater or bimetal sensing failure (~20%)** The ice-maker heater circuit or bimetal switch does not signal that the mold reached harvest temperature, preventing normal ice release.
- **Ice-maker module internal logic fault (~10%)** The embedded control or wiring inside the ice-maker assembly has failed, even though individual sensors may test normal in isolation.
- **Incomplete harvest or fill issues (~7%)** Water does not fill the mold completely or ice does not release, causing the cycle to time out and mimic a sensor fault.
- **Airflow or damper obstruction (~3%)** Blocked air ducts or a stuck damper prevent proper freezer air from reaching the ice-maker compartment, slowing freeze and harvest.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the ice maker receive water and attempt to make ice, but the harvest cycle never completes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermistor or heater-bimetal circuit inside the ice maker is most likely faulty. Replace the ice-maker assembly.<br><strong>No:</strong> Check that water supply is open and that the freezer compartment is cold. If no water arrives, the fill valve or inlet may be clogged.</div>
</details>

<details class="dtree"><summary>Is the freezer section cold (below 10°F) but the refrigerator compartment warm?</summary>
<div class="dtree-body"><strong>Yes:</strong> The E5 may coexist with an airflow or damper problem, but the ice-maker fault itself still points to the thermistor. Fix the ice maker first, then address airflow if needed.<br><strong>No:</strong> If the freezer is also warm, check the compressor and cooling system before replacing the ice maker.</div>
</details>

<details class="dtree"><summary>Can you successfully run Service Test 57 (Ice Maker Harvest) in diagnostics without the error returning?</summary>
<div class="dtree-body"><strong>Yes:</strong> The ice maker may be working now. Monitor for a few cycles. If E5 returns, replace the assembly.<br><strong>No:</strong> The ice-maker assembly has failed and should be replaced.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Pull the model and serial number** from the label inside the refrigerator compartment and download the correct tech sheet from KitchenAid or an appliance parts site to confirm the E5 definition for your platform.
2. **Enter service diagnostics** by pressing the two specified user-interface buttons together for three seconds until you hear the diagnostic-mode chime or see the display change.
3. **Read the ice-maker error code** in the diagnostic sequence and confirm that E5 appears in the ice-maker error table, not a different fault list.
4. **Run Service Test 57 (Ice Maker Harvest)** if your model supports it, and watch whether the ice maker completes a full harvest cycle or times out again with E5.
5. **Run the fill test** to verify that water enters the mold and that the sensor state changes afterward, or check for blockages in the fill tube if no water appears.
6. **Replace the ice-maker assembly** if the error persists and the harvest or fill test fails, because the thermistor and heater logic are embedded and not sold as separate parts.
7. **Retest in diagnostics** after installation to confirm E5 clears and that the ice maker completes harvest and fill cycles normally before closing up the unit.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Ice-maker assembly (KitchenAid/Whirlpool compatible) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kitchenaid-refrigerator-e5-error-code&k=Ice-maker+assembly+%28KitchenAid%2FWhirlpool+compatible%29&tag=errorcodefixes-20) \| Match your model number; thermistor and heater are built in and not sold separately. |
| Ice-maker fill valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kitchenaid-refrigerator-e5-error-code&k=Ice-maker+fill+valve&tag=errorcodefixes-20) \| Only if the fill test shows no water and the supply line is clear. |

## When to Call a Pro

Call a technician if you are not comfortable entering service diagnostics, if the refrigerator compartment is warm and you suspect a sealed-system or compressor issue, or if replacing the ice-maker assembly does not clear the E5 code after retesting. A pro can pull refrigerant pressures, check the evaporator and damper operation, and verify that the main control board is communicating correctly with the ice maker. Also call if you see frost buildup on the evaporator coils or hear the compressor cycling on and off rapidly, because those symptoms point to a cooling-system fault that goes beyond the ice-maker sensor.

**Rough cost:** DIY runs about $80–180 for ice-maker assembly, 30–60 min. A pro service call runs about $180–350 including parts and service call.
