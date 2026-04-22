---
title: "Navien Error Code E013 — Causes & Fix"
description: "What Navien error code E013 means, why the domestic hot water inlet sensor faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - boiler
  - navien
---

## Navien Error Code E013 — What It Means

Navien E013 indicates a **domestic hot water (DHW) inlet temperature sensor fault** — the cold water inlet thermistor is reading outside its valid range (open circuit, short circuit, or severely out-of-spec resistance). This sensor measures the temperature of the incoming cold water, which Navien uses to calculate how much heat to apply to reach the desired outlet temperature. Without a valid inlet reading, the unit cannot modulate accurately and shuts down to prevent scalding or damage.

[Jump to Fix](#fix)

## Common Causes

- **Failed DHW inlet thermistor** — The sensor element fails (open or short), causing the board to read an invalid signal.
- **Loose sensor connector** — The thermistor connector at the PCB or at the sensor mounting location vibrates loose.
- **Corroded or water-damaged connector** — Moisture ingress corrodes the sensor connector pins, increasing resistance and producing an out-of-range reading.
- **PCB thermistor input failure** — Rarely, the board's thermistor input circuit fails; sensor tests fine but the board still stores E013.

## Step-by-Step Fix {#fix}

1. **Locate the DHW inlet thermistor** — Open the Navien service panel. The cold water inlet sensor is typically a small thermistor mounted in a well on the cold water inlet pipe, near the flow sensor assembly.
2. **Inspect the connector** — Check the sensor connector at both the sensor and the PCB. Look for moisture, corrosion, or backed-out pins. Clean with electrical contact cleaner and reseat firmly.
3. **Measure thermistor resistance** — With power off, disconnect the sensor. Measure resistance across the two sensor wires. At room temperature (~70°F/21°C), a Navien thermistor typically reads ~10 kΩ. Compare to the resistance-temperature table in your service manual. Out-of-range = replace.
4. **Check for shorts to ground** — Measure from each wire to the unit chassis. Should read open (∞ Ω). Any finite reading indicates a shorted thermistor or wire.
5. **Replace the thermistor** — The DHW inlet thermistor on most Navien NR/NPE series units is secured by a clip or a compression fitting. Match the part number to your model. Reinstall and tighten securely.
6. **Reset and verify** — Power off for 30 seconds, restore, and draw hot water. Confirm E013 is cleared and the unit fires normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [DHW inlet thermistor](https://www.amazon.com/s?k=DHW%20inlet%20thermistor&tag=errorcodefixe-20) | Navien model-specific — verify part number for NPE vs. NR series |
| [Thermistor connector repair kit](https://www.amazon.com/s?k=Thermistor%20connector%20repair%20kit&tag=errorcodefixe-20) | If pins are corroded and sensor itself is good |

## When to Call a Pro

If the sensor measures in-spec and connections are clean but E013 persists, the PCB has a failed input and requires replacement. Navien PCB replacement should be done by a Navien-trained technician to ensure the new board is matched and configured correctly for your unit's model and gas type.
