---
title: "Navien Error Code E021 — Cold Water Inlet Thermistor Fault Fix"
author: "James Rutherford"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: navien-error-code-e021
featured: false
draft: false
tags:
  - navien
  - tankless
  - water-heater
  - thermistor
description: "Navien error code E021 means the cold water inlet thermistor has an open circuit. Learn how to diagnose and replace the NTC sensor on NPE, NPN, and NCB series units."
---

## Error Code: Navien Error Code E021

**What it means:** Error code E021 on Navien tankless water heaters and combi boilers — including the NPE, NPN, and NCB/NFC series — indicates that the control board has detected an open circuit (disconnected or broken) in the cold water inlet thermistor. This NTC (negative temperature coefficient) thermistor measures the temperature of the incoming cold water supply before it enters the heat exchanger. The control board uses this reading to calculate the temperature rise needed and modulate the burner accordingly.

With the inlet thermistor reporting no signal (open circuit), the control board cannot safely control the outlet temperature and locks out the unit, displaying E021.

## Common Causes

- **Failed NTC thermistor (open circuit)** — The thermistor's internal resistance element has fractured or broken. This is the most common cause. NTC thermistors are reliable but can fail after years of thermal cycling, especially if the cold water supply is very cold in winter and thermally shocks the sensor repeatedly.
- **Disconnected or damaged wiring harness** — The two-wire harness connecting the thermistor to the control board has a broken wire, a pulled-out connector pin, or a corroded connector. This is the second most common cause and should be checked before condemning the thermistor.
- **Corroded thermistor connector** — In high-humidity or coastal environments, the small Molex-style connector on the thermistor harness can develop corrosion that creates an open circuit even though the wires themselves are intact.
- **Control board input circuit failure** — Less commonly, the input circuit on the control board that reads the thermistor signal has failed. This is usually accompanied by other faults and should only be suspected after the thermistor and its wiring have been confirmed good.
- **Water leak damage to the thermistor or wiring** — A previous condensate drain backup or heat exchanger leak may have soaked the thermistor harness or connector, causing corrosion damage that eventually opened the circuit.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Power off the unit and locate the cold water inlet thermistor.** The cold water inlet thermistor is typically mounted in a brass or stainless fitting on the cold water manifold at the bottom of the unit, before the water enters the heat exchanger. On NPE-A and NPE-S models, it is accessible from the front after removing the cover panel.

2. **Inspect the connector and wiring.** Trace the thin two-wire harness from the thermistor to its connector on the main control board. Look for: pinched or chafed wires where they pass through any metal edges, corrosion on the connector pins, or a connector that has simply come unplugged. Clean corroded pins with electrical contact cleaner and a fine wire brush.

3. **Measure thermistor resistance.** Disconnect the thermistor harness at the board connector. Set a multimeter to resistance (Ohms). Probe across the two thermistor terminals (at the thermistor end, not the board end). At room temperature (~70°F / 21°C), a typical Navien NTC thermistor should read approximately 10,000–15,000 ohms. An "OL" or "infinity" reading confirms an open circuit — the thermistor has failed.

4. **Compare to the resistance-temperature chart.** Navien service data includes a resistance-temperature chart for all thermistors. If the reading is within range for the current water temperature, the thermistor is good and the fault is in the wiring or board.

5. **Test for continuity in the wiring harness.** With the harness disconnected at both ends, use the multimeter in continuity mode to verify each wire end-to-end. A broken wire will show no continuity.

6. **Replace the thermistor.** If the thermistor is confirmed open, replacement is straightforward — unscrew the old thermistor from its fitting (it may be threaded or have a clamp), apply thread sealant if required, and install the new thermistor. Reconnect the harness and power on.

## How to Fix It

In the majority of cases, E021 is resolved by:
1. Cleaning the connector and reseating it firmly (free fix — try this first)
2. Replacing the cold water inlet thermistor ($20–$50 part)
3. Repairing a broken wire in the harness (splice with waterproof heat-shrink connectors)

Board replacement is rarely needed for an E021 fault. If replacing the thermistor and verifying the wiring does not clear E021, contact Navien technical support before condemning the board.

## Parts You May Need {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Navien NTC Thermistor (inlet sensor) | $20–$50 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e021&k=Navien+NTC+thermistor+inlet+sensor+tankless&tag=errorcodefixes-20) |
| Electrical Contact Cleaner Spray | $6–$12 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e021&k=electrical+contact+cleaner+spray&tag=errorcodefixes-20) |
| Waterproof Heat-Shrink Butt Connectors | $8–$15 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e021&k=waterproof+heat+shrink+butt+connectors+wire+splice&tag=errorcodefixes-20) |
| Digital Multimeter | $20–$60 | [Amazon](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-navien-error-code-e021&tag=errorcodefixes-20) |

## When to Call a Technician

E021 is one of the more DIY-accessible Navien fault codes. The thermistor replacement does not require disconnecting gas or refrigerant — it's a plumbing sensor swap on the water side. However, if the repair requires replacing the control board or if you're unsure about working inside the unit, a certified Navien technician can diagnose and replace the sensor quickly. Navien's tech support line (1-800-519-8794) is also helpful for confirming the correct part number for your specific model.

> **Pro tip:** Before ordering a replacement thermistor, clean the connector first. Navien harness connectors are small and can accumulate mineral dust or slight corrosion from the humid environment inside the unit. A shot of electrical contact cleaner and a firm reconnect resolves a surprising number of thermistor-related fault codes at zero cost.

## Related Error Codes

- [Navien Error Code E022 — Hot Water Outlet Thermistor Fault](/posts/navien-error-code-e022/)
- [Navien Error Code E003 — Ignition Failure](/posts/navien-error-code-e003-ignition-failure/)
- [Navien Error Code E016 — Heat Exchanger Outlet High Temperature](/posts/navien-error-code-e016/)
- [All Navien Error Codes](/posts/navien-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem Performance Platinum PDN tankless error codes](/posts/rheem-performance-platinum-pdn-error-codes/)
