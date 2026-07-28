---
title: "LG Refrigerator FS Error Code - Causes & Fix"
description: "FS means freezer sensor error (short or open circuit). Most common fix: replace the freezer thermistor or repair its wiring harness."
pubDatetime: 2026-06-08T04:17:48Z
modDatetime: 2026-06-08T04:17:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - refrigerator
  - lg
most_likely_cause: "freezer sensor (thermistor) failure or wiring harness damage"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "LG freezer thermistor (freezer sensor)"
---

## What this code means
The FS code on LG refrigerators indicates a freezer sensor error. LG defines this as a short or disconnection of the freezer sensor (thermistor). The main control board displays FS when it detects either a direct short (0 Ω) or an open circuit from the freezer sensor, meaning the board cannot read a valid temperature signal from the freezer compartment.

This is a service-required fault according to LG. The refrigerator may continue to run but cannot regulate freezer temperature accurately. The error points to a problem in the sensor itself, its wiring harness, or the connection between the sensor and the main PCB.

## Before You Replace Anything

Homeowners sometimes replace the main control board first without testing the sensor. A multimeter resistance check of the freezer thermistor (in the kΩ range at room temperature, never 0 Ω or infinite) will confirm whether the sensor or wiring is the real problem before spending on a board.

## Common Causes

- **Open or shorted freezer thermistor (~50%)** The sensor itself fails internally, reading 0 Ω (short), infinite resistance (open), or a value far outside the normal kΩ range for its temperature.
- **Damaged or corroded sensor wiring harness (~30%)** A broken wire, loose connector pin, or corrosion between the freezer sensor and the main PCB interrupts the signal and triggers the FS code.
- **Loose or oxidized connector at sensor or main board (~15%)** The plug at either end of the sensor harness works loose or develops oxidation, creating an intermittent or open circuit.
- **Main PCB input circuit failure (~5%)** The control board's sensor input circuitry fails and reads the sensor as shorted or open even when the sensor and harness test good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear for a few minutes after you unplug the refrigerator and plug it back in?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code returns because the fault is still present. Proceed with sensor and harness testing.<br><strong>No:</strong> The code is persistent and locked. The board detects a constant fault condition and you need to test the sensor circuit immediately.</div>
</details>

<details class="dtree"><summary>Can you access the freezer sensor and measure its resistance with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> Compare the reading to LG's thermistor chart for your model. A normal sensor will read in the kΩ range (not 0 Ω or infinite). If out of range, replace the sensor.<br><strong>No:</strong> You will need to call a technician to disassemble the freezer compartment and perform the test safely.</div>
</details>

<details class="dtree"><summary>Do you see any visible damage, burn marks, or corrosion on the sensor connector or harness?</summary>
<div class="dtree-body"><strong>Yes:</strong> Repair or replace the damaged harness and connector. Even a small break or oxidation can trigger FS.<br><strong>No:</strong> The fault is internal to the sensor or the main board input circuit. A technician will need to isolate which component has failed.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the refrigerator** and allow it to fully power down before you open any panels or touch any wiring.
2. **Locate the freezer sensor** (thermistor), usually clipped or taped to the evaporator coil or the rear wall of the freezer compartment behind an access panel.
3. **Inspect the sensor harness and connector** at both the sensor end and the main PCB end for loose pins, broken wires, corrosion, or physical damage.
4. **Disconnect the sensor** and measure its resistance with a multimeter set to ohms. Consult your model's thermistor resistance chart (LG charts show values in the kΩ range, for example approximately 73 kΩ at -39°F or 1.4 kΩ at 104°F). A reading of 0 Ω or infinite resistance means the sensor is failed.
5. **Replace the freezer sensor** if it reads out of range or if the harness is damaged beyond repair. Use an OEM LG thermistor for your model family.
6. **Test harness continuity** from the sensor connector to the main PCB if the sensor itself reads correctly. Any break in the wire will cause FS.
7. **Reconnect all harnesses**, reassemble the freezer panel, plug in the refrigerator, and monitor for 24 hours to confirm the FS code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG freezer thermistor (freezer sensor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-fs-error-code&k=LG+freezer+thermistor+%28freezer+sensor%29&tag=errorcodefixes-20) \| OEM part for your model family. Verify part number from your refrigerator's service label or wiring diagram. |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-fs-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| If the harness between the sensor and main board is cut, melted, or corroded and cannot be repaired with a splice. |
| Main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-fs-error-code&k=Main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Only if the sensor and harness both test good and the board input circuit is confirmed failed. Expensive, so verify all other causes first. |

## When to Call a Pro

Call a professional if you are not comfortable working with a multimeter, disassembling the freezer evaporator cover, or interpreting a thermistor resistance chart. The freezer sensor is often buried behind insulation or clipped to the evaporator coil, and accessing it safely requires knowledge of the refrigerator's layout. A technician will have the correct LG thermistor chart for your model, the tools to test harness continuity end-to-end, and the ability to replace the main PCB if the sensor circuit on the board has failed. If the FS code persists after you have replaced the sensor and inspected the harness, the board is the likely culprit and professional diagnosis will save you from replacing parts by trial and error.

**Rough cost:** A pro service call runs about $150–$300.
