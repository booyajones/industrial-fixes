---
title: "Navien Error Code E022 — Hot Water Outlet Thermistor Fault Fix"
author: "James Rutherford"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: navien-error-code-e022
featured: false
draft: false
tags:
  - navien
  - tankless
  - water-heater
  - thermistor
description: "Navien E022 error code means the hot water outlet thermistor is shorted or open. Learn how to diagnose the NTC sensor and wiring on Navien NPE, NPN, and NCB models."
---

## Error Code: Navien Error Code E022

**What it means:** Error code E022 on Navien tankless water heaters and combi boilers — NPE, NPN, NCB, and NFC series — indicates a fault in the hot water outlet thermistor. Unlike E021, which covers an open circuit (no signal) on the inlet thermistor, E022 can be triggered by either an open circuit or a short circuit (shorted to ground or across the thermistor terminals) on the outlet thermistor.

The hot water outlet thermistor measures the temperature of the water leaving the heat exchanger. This is the most critical temperature measurement in the entire system — the control board uses it to modulate the burner rate and maintain the set point temperature. When this sensor fails or sends an implausible signal, the unit cannot safely control output temperature and must shut down.

## Common Causes

- **Short-circuited thermistor** — The NTC element inside the sensor has developed an internal short. A shorted thermistor reads near-zero resistance, which the control board interprets as an impossibly high temperature (since lower resistance = higher temperature on an NTC curve) and immediately shuts down.
- **Open-circuit thermistor** — The internal resistance element has broken, giving an infinity reading. Same physical sensor type as E021, different location on the water circuit.
- **Damaged or shorted wiring harness** — A harness routed too close to the burner or heat exchanger can have its insulation melted, shorting the two wires together or shorting one wire to the unit chassis. This mimics a shorted thermistor.
- **Connector pin pushed back into housing** — The small female Molex-type connector can have a pin pushed back out of its retention slot, either causing an intermittent open or a short if the loose pin contacts an adjacent metal surface.
- **Water intrusion and corrosion** — If condensate has dripped onto the thermistor or harness over time, the water can cause copper corrosion that bridges the two wires, creating a short circuit.
- **Control board fault on thermistor input circuit** — Rare, but a failed pull-up resistor or input protection component on the board itself can cause the board to read the thermistor as shorted regardless of the actual thermistor condition.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Locate the hot water outlet thermistor.** This sensor is mounted on the hot water outlet manifold or plumbing connection at the top of the heat exchanger, on the outlet side. It is typically adjacent to the cold water inlet thermistor but on the opposite — outlet — end of the heat exchanger.

2. **Inspect the harness for thermal damage.** With the unit powered off, trace the outlet thermistor's harness carefully. Look for any sections where the insulation is melted, cracked, or discolored from heat. If the harness runs near a combustion component, check for heat damage particularly at any sharp bends.

3. **Measure thermistor resistance.** Disconnect the thermistor at the board connector. Measure resistance across the thermistor's two terminals (at the thermistor end). At room temperature (~70°F / 21°C):
   - Expected reading: ~10,000–15,000 ohms
   - Open circuit (OL / infinity): thermistor is broken internally
   - Near-zero ohms (0–50 ohms): thermistor is shorted
   - Both conditions require thermistor replacement.

4. **Check wiring harness continuity and isolation.** With the harness disconnected at both ends, test each wire for continuity end-to-end. Then test each wire against the unit chassis (ground) — any wire showing continuity to ground indicates an insulation breach and the harness must be replaced.

5. **Re-test with harness disconnected at thermistor.** Disconnect the harness at the thermistor body. If the harness tests good but the thermistor tests bad, replace the thermistor only. If the harness is shorted, replace the harness section.

6. **Reconnect and clear the code.** After replacing the thermistor or repairing the harness, reconnect everything and power on the unit. E022 should clear. If E022 immediately recurs with a confirmed-good new thermistor and intact harness, the board input circuit has failed.

## How to Fix It

The outlet thermistor is the same NTC sensor style used for the inlet thermistor (E021) — the sensors are often interchangeable between the inlet and outlet positions on the same model. Confirm the correct part number using your model's service manual or Navien's parts lookup.

- **Shorted or open thermistor:** Replace the outlet thermistor.
- **Shorted harness:** Repair the short by isolating and splicing the damaged section, or replace the entire harness. Use high-temperature wire rated for the environment inside the unit.
- **Corroded connector:** Clean with electrical contact cleaner, replace pins if bent, or replace the connector housing.

## Parts You May Need {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Navien NTC Thermistor (outlet sensor) | $20–$50 | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-navien-error-code-e022&tag=errorcodefixes-20) |
| High-Temperature Wire (for harness repair) | $10–$20 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e022&k=high+temperature+wire+HVAC+sensor+repair&tag=errorcodefixes-20) |
| Electrical Contact Cleaner | $6–$12 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e022&k=electrical+contact+cleaner+spray+HVAC&tag=errorcodefixes-20) |
| Waterproof Heat-Shrink Connectors | $8–$15 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e022&k=waterproof+heat+shrink+wire+connector+splice&tag=errorcodefixes-20) |
| Digital Multimeter | $20–$60 | [Amazon](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-navien-error-code-e022&tag=errorcodefixes-20) |

## When to Call a Technician

E022 is similar in scope to E021 — a thermistor swap is within reach of a careful DIYer. The key additional concern with E022 vs E021 is that a shorted harness can sometimes mean thermal damage near the combustion section, which requires careful inspection to ensure no ongoing risk. If the harness shows burn marks near the burner or heat exchanger, have a licensed technician inspect the unit for any combustion housing integrity issues before putting it back in service.

> **Pro tip:** Navien uses the same thermistor part across multiple positions on many models — the cold water inlet, hot water outlet, and sometimes the bypass thermistor are all the same NTC sensor with the same resistance curve. Check the service bulletin for your model. If you buy two thermistors to replace both inlet and outlet at the same time (E021 + E022), you may get a discount on shipping and avoid a second service call if the adjacent sensor also fails soon.

## Related Error Codes

- [Navien Error Code E021 — Cold Water Inlet Thermistor Fault](/posts/navien-error-code-e021/)
- [Navien Error Code E016 — Heat Exchanger Outlet High Temperature](/posts/navien-error-code-e016/)
- [Navien Error Code E003 — Ignition Failure](/posts/navien-error-code-e003-ignition-failure/)
- [All Navien Error Codes](/posts/navien-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Rheem Performance Platinum PDN tankless error codes](/posts/rheem-performance-platinum-pdn-error-codes/)
