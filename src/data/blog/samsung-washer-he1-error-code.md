---
title: "Samsung HE1 Error Code - Causes & Fix"
description: "HE1 means a heater error in your Samsung washer's water-heating system. Most often caused by a failed heating element or thermistor."
pubDatetime: 2026-06-08T03:19:20Z
modDatetime: 2026-06-08T03:19:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - samsung
most_likely_cause: "Failed heating element or NTC thermistor"
likelihood: "the most common causes"
diy_or_pro: "pro"
money_part: "Samsung washer heating element"
part_price: "$30-80"
---

## Samsung HE1 Error Code — What It Means

The HE1 error code on a Samsung front-load washer indicates that a heater error has occurred in the water-heating system. The machine has detected a fault somewhere in the circuit responsible for heating wash water, which may involve the heating element itself, the temperature sensor (NTC thermistor), the wiring and connectors, or the control board's heater drive circuit. Samsung groups HE1 and HE2 together and provides limited public diagnostic guidance beyond confirming that a heater fault is present.

Because the code flags the heating system broadly rather than pinpointing a single component, technicians follow a methodical troubleshooting path that checks the heater element for continuity, the thermistor for proper resistance response, all wiring and connectors for damage or corrosion, and finally the control board's output stage if the load-side components test good. The error typically allows cold-water cycles to run but prevents heated wash programs from completing normally.

## Before You Replace Anything

Many people replace the control board first without testing the heater element and thermistor. Use a multimeter to check continuity on the heater and resistance on the thermistor before ordering expensive electronics.

[Jump to Fix](#fix)

## Common Causes

- **Faulty heating element (~40%)** The resistive heater that warms wash water develops an open circuit or internal short, preventing current flow and triggering the error.
- **Defective NTC thermistor (~30%)** The temperature sensor reports out-of-range resistance or fails to respond to heat, so the control board cannot monitor or regulate water temperature.
- **Damaged wiring or connectors (~15%)** Corrosion, heat damage, or broken conductors in the harness between the control board and heater assembly interrupt the signal or power path.
- **Failed control board heater relay or triac (~10%)** The switching component on the main PCB that energizes the heater burns out or develops damaged traces, even though the heater and sensor test good.
- **Loose or corroded connector terminals (~5%)** Oxidation or poor contact at the heater or thermistor plugs creates intermittent open circuits that the board reads as a fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the washer complete a cold-water cycle without showing HE1?</summary>
<div class="dtree-body"><strong>Yes:</strong> The heater circuit is likely at fault rather than a broader control or mechanical issue. Proceed with heater and thermistor testing.<br><strong>No:</strong> The problem may be a control board fault or wiring issue affecting more than just the heater. Call a technician to diagnose the main board and harness.</div>
</details>

<details class="dtree"><summary>After unplugging for five minutes and restarting, does the code clear and stay away for at least one heated cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may be intermittent, often caused by a loose connector or marginal thermistor. Inspect all heater-circuit connections and monitor for recurrence.<br><strong>No:</strong> The fault is persistent. Test the heater element and thermistor with a multimeter to isolate the failed component.</div>
</details>

<details class="dtree"><summary>With power off, does the heater element show continuity and the thermistor show changing resistance when warmed gently?</summary>
<div class="dtree-body"><strong>Yes:</strong> Both load components are likely good. Check wiring integrity and consider a faulty control board heater relay or triac.<br><strong>No:</strong> Replace whichever component tests open or out of spec, then retest the system.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the washer** and wait at least five minutes to allow the control board to reset and residual voltage to dissipate.
2. **Remove the rear access panel** by taking out the screws around the perimeter (some models require front or bottom access, consult your service manual).
3. **Locate the heating element and thermistor** mounted on or near the wash tub, typically at the bottom rear, and inspect all visible wiring and connectors for burns, corrosion, or loose pins.
4. **Disconnect the heater element terminals** and use a multimeter set to continuity or low resistance to check for a closed path through the element (open circuit means replace the heater).
5. **Disconnect the thermistor connector** and measure resistance across the sensor pins, then gently warm the sensor body and confirm the resistance value changes (no change or infinite resistance means replace the thermistor).
6. **If both heater and thermistor test good**, trace the wiring harness back to the main control board and inspect for broken wires, damaged insulation, or blown fuse links in the heater circuit.
7. **Reassemble the washer**, plug it in, and run a heated wash cycle to verify the error does not return and water temperature rises normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Samsung washer heating element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-samsung-washer-he1-error-code&k=Samsung+washer+heating+element&tag=errorcodefixes-20) \| Match the wattage and mounting style to your model number; typically 1200-1800 W. |
| Samsung washer NTC thermistor (temperature sensor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-samsung-washer-he1-error-code&k=Samsung+washer+NTC+thermistor+%28temperature+sensor%29&tag=errorcodefixes-20) \| Verify connector type and resistance range for your specific washer series. |
| Heater wiring harness or connector repair kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-samsung-washer-he1-error-code&k=Heater+wiring+harness+or+connector+repair+kit&tag=errorcodefixes-20) \| Use only if you find broken wires or burnt terminals; includes heat-shrink terminals and high-temp wire. |

## When to Call a Pro

Call a professional if you are uncomfortable working with household voltage (even with the machine unplugged, the heater circuit carries live AC when powered), if you cannot safely access the rear or underside of the washer in your laundry space, or if both the heater and thermistor test good but the error persists (indicating a control board fault that requires board-level diagnosis and possibly soldering or full board replacement). Technicians have model-specific wiring diagrams, the correct replacement parts on their trucks, and the tools to test control board outputs safely. If your washer is still under warranty or covered by a service plan, contact Samsung or your retailer before opening any panels to avoid voiding coverage.

**Rough cost:** DIY runs about $30-80 in parts, 1-2 hours. A pro service call runs about $150-300.
