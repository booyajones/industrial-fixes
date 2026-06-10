---
title: "LG Dryer LE2 Error Code - Causes & Fix"
description: "LE2 on LG dryers means a compressor fault on heat-pump models or motor/airflow issues on standard models. Reset power first."
pubDatetime: 2026-06-08T03:40:41Z
modDatetime: 2026-06-08T03:40:41Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - lg
most_likely_cause: "compressor circuit failure on heat-pump models"
likelihood: "the most common cause on heat-pump dryers"
diy_or_pro: "pro"
---

## LG Dryer LE2 Error Code — What It Means

LE2 is model-dependent across LG dryers. On newer heat-pump dryers, LG lists LE2 (alongside AE and CE1) as a compressor problem in the refrigerant circuit that generates heat. On older standard condensing dryers, LE2 can signal lint or filter blockage restricting airflow, or the main PCB failing to supply voltage to the drum motor. On some LG Styler appliances, LE2 appears when the surrounding temperature is too low for normal operation. Because the code has different meanings by platform, always confirm your model family before diagnosing.

Heat-pump dryers use a sealed compressor system to move heat, so an LE2 typically points to a failed compressor or loss of power to it. Standard condensing dryers rely on electric heaters and a motor-driven drum, so the same code may instead reflect a motor-winding fault or a clogged lint filter choking airflow. LG recommends a power reset as the first action, because the control electronics can latch a fault that clears when you unplug and reconnect power.

## Before You Replace Anything

Homeowners sometimes replace the main PCB when the compressor itself has failed. Measure compressor winding resistance and verify power at the compressor terminals before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Compressor failure (heat-pump models) (~50%)** The sealed refrigerant compressor has failed windings or a stuck piston, preventing heat generation.
- **Main PCB not powering the compressor or motor (~25%)** The control board is not outputting the correct voltage to run the compressor on heat-pump units or the drum motor on standard models.
- **Clogged lint filter or airflow restriction (standard condensing models) (~15%)** A blocked filter or vent reduces airflow to the point that the dryer cannot operate safely.
- **Drum motor winding fault (standard condensing models) (~7%)** The motor windings are open or out of specification, preventing the drum from spinning.
- **Low ambient temperature (Styler and some products) (~3%)** Installation in a space below about 10 °C can trigger a low-temperature error displayed as LE2.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear after unplugging for one minute and reconnecting power?</summary>
<div class="dtree-body"><strong>Yes:</strong> A latched fault or transient event caused the code. Run a test load and monitor; if it returns, continue diagnostics.<br><strong>No:</strong> The fault is persistent. Proceed to model identification and component tests.</div>
</details>

<details class="dtree"><summary>Is your dryer a heat-pump model (compressor-based cooling/heating)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Focus on compressor power and winding checks. This is a sealed-system repair requiring a technician.<br><strong>No:</strong> Check lint filter, airflow, and drum motor voltage. A clogged filter or motor fault is more likely.</div>
</details>

<details class="dtree"><summary>Is the installation area unusually cold (below 10 °C / 50 °F)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Warm the space or relocate the appliance. Some LG products will not operate in very low ambient temperatures.<br><strong>No:</strong> Ambient temperature is normal. Test the compressor or motor as appropriate for your model.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Identify your model family** by checking the rating plate and user manual to confirm whether you have a heat-pump dryer, a standard condensing dryer, or another LG product like Styler.
2. **Perform a power reset** by unplugging the dryer, waiting one full minute, then reconnecting power and running a test cycle to see if the fault clears.
3. **Inspect and clean the lint filter** on standard condensing models, verify it is fully seated, and clear any visible lint or debris from the filter housing and exhaust vent.
4. **Check the compressor on heat-pump models** by verifying wiring connections, measuring resistance across the compressor windings (for example Yellow to Blue = 1.21 Ω ± 7% and Yellow to White = 5.04 Ω ± 7% on some models, or 2.56 Ω ± 0.3 Ω on inverter BLDC compressors at 240 VAC), and confirming power supply from the main PCB.
5. **Test the drum motor on standard condensing models** by measuring winding resistance (U to V, V to W, and W to U should each be 20 Ω ± 2 Ω) and checking for 220–240 VAC at the motor terminals when the control board commands a run.
6. **Replace the failed component**: if the compressor windings are out of range or the motor windings are open, replace that component; if power is absent and all wiring is intact, replace the main PCB.
7. **Run a full test cycle** after repair to confirm the dryer heats, tumbles, and completes without returning the LE2 code.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Heat-pump compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-le2-error-code&k=Heat-pump+compressor&tag=errorcodefixes-20) \| Model-specific sealed unit; verify winding resistance and supply voltage before ordering. |
| Drum motor (standard condensing dryer) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-le2-error-code&k=Drum+motor+%28standard+condensing+dryer%29&tag=errorcodefixes-20) \| Measure winding resistance (20 Ω ± 2 Ω per phase pair on many models) to confirm failure. |
| Main control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-le2-error-code&k=Main+control+PCB&tag=errorcodefixes-20) \| Replace only if it fails to output the correct voltage and all other components test good. |

## When to Call a Pro

Call a technician if you own a heat-pump dryer, because compressor diagnosis and replacement involve a sealed refrigerant system that requires recovery equipment, vacuum pumps, and refrigerant-handling certification. Standard condensing dryers also require high-voltage testing at the motor and control board, so professional help is recommended unless you are comfortable working with 220–240 VAC circuits. A qualified service technician will use the model-specific wiring diagram to confirm whether the main PCB is delivering power, measure winding resistance on the compressor or motor, and replace only the component that has failed. If you see the LE2 code alongside unusual noises or a burning smell, disconnect power immediately and arrange a service call to prevent further damage.

**Rough cost:** A pro service call runs about $300–600.
