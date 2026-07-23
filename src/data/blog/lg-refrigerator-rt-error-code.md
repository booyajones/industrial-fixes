---
title: "LG Refrigerator rT Error Code - Causes & Fix"
description: "rT means a shorted or open room-temperature sensor circuit. Most often the sensor thermistor itself has failed and needs replacement."
pubDatetime: 2026-06-08T04:22:20Z
modDatetime: 2026-06-08T04:22:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - refrigerator
  - lg
most_likely_cause: "Failed room-temperature sensor thermistor"
likelihood: "the most common cause"
diy_or_pro: "diy"
money_part: "LG refrigerator room-temperature sensor / thermistor"
part_price: "$15-35"
---

## LG Refrigerator rT Error Code — What It Means

The rT code on LG refrigerators indicates the control system has detected a shorted or open room-temperature sensor circuit. The refrigerator's main control board is not receiving a valid signal from the temperature sensor (thermistor) that monitors compartment or ambient air temperature. This is an electrical fault in the sensing circuit, not a performance complaint about cooling or temperature drift. The control board expects a specific resistance range from the sensor, and when the circuit reads zero ohms (short) or infinite ohms (open), it logs the rT fault and may interrupt normal cooling logic.

## Before You Replace Anything

Many people replace the main control board first when they see any error code. Before ordering a board, ohm-test the sensor and inspect the connector for corrosion or loose pins. A $15 sensor fix often solves what looks like a $200 board problem.

[Jump to Fix](#fix)

## Common Causes

- **Failed thermistor or temperature sensor (~55%)** The sensor itself goes open or shorted due to age, thermal stress, or moisture intrusion, and no longer provides a valid resistance to the control board.
- **Loose, corroded, or backed-out connector (~25%)** Oxidation, vibration, or poor initial seating breaks contact between the sensor harness and the connector terminals, creating an intermittent or permanent open circuit.
- **Damaged wiring harness (~12%)** Pinched, abraded, or moisture-soaked wiring shorts to ground or breaks continuity anywhere between the sensor and the control board.
- **Main control board fault (~8%)** A failed sensor input circuit on the PCB misreads a healthy sensor as open or shorted, though this is much less common than sensor or wiring issues.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear for at least a few hours after you unplug the refrigerator for 60 seconds and plug it back in?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is intermittent, usually a loose connector or harness chafing. Inspect all sensor connectors and harness routing before replacing parts.<br><strong>No:</strong> The fault is steady, pointing to a completely open or shorted sensor or a failed board input. Proceed to sensor resistance testing.</div>
</details>

<details class="dtree"><summary>Can you locate and unplug the room-temperature sensor connector (often clipped near the fresh-food ceiling or air duct)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Measure resistance across the sensor's two terminals with an ohmmeter. If it reads open (infinite) or near-zero (shorted), replace the sensor. If it reads a plausible value (usually a few thousand to tens of thousands of ohms at room temp), check wiring continuity back to the board.<br><strong>No:</strong> Consult your model's service manual or wiring diagram to identify the sensor location. Without the correct location, you risk testing the wrong component.</div>
</details>

<details class="dtree"><summary>After replacing the sensor, does the rT code still return immediately on power-up?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wiring harness or main control board is faulty. Verify harness continuity pin-to-pin, then evaluate the board.<br><strong>No:</strong> The sensor was the problem. Monitor for 24 hours to confirm stable operation and normal temperature readings.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the refrigerator** and wait 60 seconds to discharge the control board and clear any transient fault.
2. **Locate the room-temperature sensor** by consulting your model's service sheet or wiring diagram. It is often clipped to the fresh-food ceiling, air duct, or evaporator cover, with a two-pin connector.
3. **Inspect the sensor connector** for corrosion, bent pins, moisture, or incomplete seating. Clean or reseat as needed.
4. **Disconnect the sensor** and measure its resistance with a multimeter. Compare the reading to the manufacturer's specification for ambient temperature. If the sensor reads open (infinite ohms) or shorted (near-zero ohms), it is faulty.
5. **Check wiring continuity** from the sensor connector back to the main control board if the sensor itself tests within normal range. Look for pinched, abraded, or broken wires.
6. **Replace the failed sensor** with the correct OEM or exact-equivalent part for your model. Reconnect, secure the harness away from sharp edges, and restore power.
7. **Monitor operation** for at least one cooling cycle. If the rT code does not return and the compartment cools normally, the repair is complete. If the code persists with a new sensor and verified wiring, evaluate the main control board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG refrigerator room-temperature sensor / thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-rt-error-code&k=LG+refrigerator+room-temperature+sensor+%2F+thermistor&tag=errorcodefixes-20) \| Match the part number to your exact model; sensors are not universal across all LG refrigerators. |
| Wiring harness repair kit or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-rt-error-code&k=Wiring+harness+repair+kit+or+connector&tag=errorcodefixes-20) \| Use only if you find damaged insulation or broken pins; generic appliance-grade connectors and heat-shrink are acceptable for field repair. |
| LG refrigerator main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-rt-error-code&k=LG+refrigerator+main+control+board&tag=errorcodefixes-20) \| Order only after confirming the sensor and wiring test correctly; boards are expensive and rarely the true cause of rT. |

## When to Call a Pro

Call a professional if you cannot safely access the sensor location (for example, behind a sealed evaporator cover that requires refrigerant recovery), if ohm-testing and wiring checks are unfamiliar, or if the code returns after you have replaced the sensor and verified all harness continuity. Technicians carry model-specific resistance tables, can perform board-level input testing, and will warranty both parts and labor. Refrigerant work is never DIY, but the rT sensor circuit itself does not involve the sealed system or high voltage and is otherwise a straightforward swap for a confident home repairer with a multimeter.

**Rough cost:** DIY runs about $15-35 in parts, 20-40 min. A pro service call runs about $120-220 service call.

## See Also

- [LG Dishwasher Leaking - Causes & Fix](/posts/lg-dishwasher-leaking/)
- [LG Oven F6 Error Code - Causes & Fix](/posts/lg-oven-f6-error-code/)
- [LG LMXS28626S Refrigerator Problems & Error Codes](/posts/lg-lmxs28626s-refrigerator-problems/)
- [LG Refrigerator CO Error Code - Causes & Fix](/posts/lg-refrigerator-co-error-code/)
