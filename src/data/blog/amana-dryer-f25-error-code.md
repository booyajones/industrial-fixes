---
title: "Amana Dryer F25 Error Code - Causes & Fix"
description: "F25 signals a control board fault related to the inlet thermistor, usually shorted. Reset power first, then check and replace the thermistor."
pubDatetime: 2026-06-12T05:20:20Z
modDatetime: 2026-06-12T05:20:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - amana
money_part: "Inlet thermistor"
most_likely_cause: "shorted inlet thermistor"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Turn off the circuit breaker for 5 minutes, then restore power to reset the control"
  - "Remove and clean the lint screen, inspect the blower wheel and fan cage for packed lint, and verify the external vent is not crushed or kinked"
part_price: "$15-35"
no_buy_pct: "25%"
---

## What this code means
F25 on an Amana dryer indicates the control board has detected a fault in the inlet thermistor circuit, typically interpreted as a shorted thermistor. Amana's official product-help documentation lists F25 and recommends a power-cycle reset as the first troubleshooting step. Because Amana shares control architecture with Whirlpool-family dryers, the code is understood to mean the inlet thermistor is shorted or the control circuit has failed, though the exact Amana wording is not publicly detailed in available documentation.

The inlet thermistor monitors incoming air temperature and helps the control board regulate heating cycles. When the thermistor shorts or its wiring fails, the control board throws F25 and halts the dryer. Lint buildup and restricted airflow can overheat the dryer and contribute to thermistor or thermal cutoff failures, so airflow inspection is a core part of the diagnostic process.

## Before You Replace Anything

Many people replace the control board first without testing the thermistor. Measure the inlet thermistor resistance with a multimeter (expect around 50,000 ohms at room temperature in typical installations) before ordering expensive electronics.

## Common Causes

- **Shorted inlet thermistor (~50%)** The inlet thermistor senses incoming air temperature, and when it shorts internally or its wiring grounds out, the control board throws F25.
- **Lint buildup restricting airflow (~25%)** Lint packed in the blower wheel, fan cage, or vent duct can overheat the dryer and damage the thermistor or trigger thermal cutoffs, sometimes repeatedly until the blockage is cleared.
- **Thermal fuse or cutoff open (~15%)** A blown thermal fuse or high-limit thermostat on the heater box can interrupt the thermistor circuit or contribute to overheating conditions that damage the thermistor.
- **Thermistor wiring damaged or corroded (~7%)** Connections at the thermistor terminals or the control board can corrode or break, creating a short-circuit path that triggers the fault.
- **Failed control board (~3%)** If the thermistor and wiring test good and airflow is clear, the control board itself may have a fault in the thermistor input circuit.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the code clear and stay away after you turn off the breaker for 5 minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control recovered from a transient fault. Monitor the next few cycles and verify the lint screen and vent are clean to prevent overheating.<br><strong>No:</strong> The fault is persistent. Continue diagnostic testing of the thermistor and airflow path.</div>
</details>

<details class="dtree"><summary>Is the blower wheel or fan cage packed with lint when you remove the lower front panel?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the fan cage thoroughly and check the external vent for blockage. Lint restriction is a common contributor to F25 codes.<br><strong>No:</strong> Airflow is likely adequate. Focus on testing the inlet thermistor and thermal cutoff components.</div>
</details>

<details class="dtree"><summary>Does the inlet thermistor measure around 50,000 ohms at room temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The thermistor is within typical range. Inspect the wiring for damage and consider testing the thermal fuse and control board if the code persists.<br><strong>No:</strong> The thermistor is shorted (near zero ohms) or open (infinite resistance). Replace the inlet thermistor and retest.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker and unplug the dryer before opening any panels or touching internal components.
2. **Reset the control** by leaving the breaker off for at least 5 minutes, then restore power and run a test cycle to see if the code returns.
3. **Remove the lower front panel or blower housing** (consult your model's service manual for access) and inspect the blower wheel and fan cage for packed lint, cleaning thoroughly with a vacuum and brush.
4. **Check the external vent** from the dryer to the outside termination for kinks, crushing, excessive length, or lint blockage, and clean or repair as needed.
5. **Locate the inlet thermistor** on the blower housing or heater box (refer to the wiring diagram) and disconnect the wire leads.
6. **Measure thermistor resistance** with a multimeter set to ohms. A typical room-temperature reading is around 50,000 ohms. If the reading is near zero (shorted) or infinite (open), replace the thermistor.
7. **Inspect thermistor wiring and connectors** for corrosion, abrasion, or loose terminals, and repair or replace damaged wiring harnesses.
8. **Check the thermal fuse and high-limit thermostat** on the heater box with a continuity tester. If either is open, replace it and address the airflow restriction that caused it to blow.
9. **Reassemble the dryer**, restore power, and run a full heated cycle to confirm the F25 code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Inlet thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f25-error-code&k=Inlet+thermistor&tag=errorcodefixes-20) \| Verify the part number on your model's wiring diagram or service label before ordering. |
| Thermal fuse (dryer heater box) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f25-error-code&k=Thermal+fuse+%28dryer+heater+box%29&tag=errorcodefixes-20) \| One-time cutoff that opens on overheat. Replace if blown and always fix the airflow restriction that caused it. |
| High-limit thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f25-error-code&k=High-limit+thermostat&tag=errorcodefixes-20) \| Cycling limit on the heater assembly. Test for continuity and replace if open. |

## When to Call a Pro

Call a professional if you are uncomfortable working inside the dryer cabinet, if the thermistor and all wiring test good but the code persists (suggesting a control board fault), or if you find evidence of repeated overheating that may have damaged multiple components. A technician can perform voltage checks on the control board, trace harness faults with a meter, and safely diagnose whether the main control needs replacement. If the dryer has burned wiring, scorching, or a history of thermal fuse failures, a pro should evaluate the entire heating and airflow system to prevent fire risk.

**Rough cost:** DIY runs about $20-50 in parts, 30-60 min. A pro service call runs about $120-250.
