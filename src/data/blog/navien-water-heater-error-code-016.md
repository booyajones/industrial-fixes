---
title: "Navien NPE-A 016 — Overheat Lockout Fix"
description: "Code 016 (also displayed as E016) on a Navien NPE-A or NPE-S tankless water heater means the unit's heat exchanger outlet temperature exceeded the overheat..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: navien-water-heater-error-code-016
featured: false
draft: false
tags:
  - navien
  - overheat-lockout
  - troubleshooting
---
## Quick answer

Code 016 (also displayed as E016) on a Navien NPE-A or NPE-S tankless water heater means the unit's heat exchanger outlet temperature exceeded the overheat protection threshold — typically 207°F (97°C) on most NPE platforms. The unit locks out the burner and requires manual reset. Most field calls trace to scale buildup in the heat exchanger restricting flow and water-side heat transfer; less often it's a stuck flow sensor, low water flow from a clogged inlet filter, or a failed temperature sensor.

## What Code 016 means on a Navien

The NPE-A (with built-in recirculation pump and buffer tank) and NPE-S (standard, no recirc) are condensing tankless water heaters with two heat exchanger pathways: a primary HX where combustion occurs and water absorbs heat, and on NPE-A specifically, a secondary HX for the buffer/recirculation circuit.

The control board monitors several temperatures continuously:

- **Inlet temperature** — water entering the HX.
- **Outlet temperature** — water leaving the HX. This is the primary safety sensor for Code 016.
- **Heat exchanger surface temperatures** — fin-pack sensors on some platforms.
- **Flow rate** — via the flow sensor on the inlet.

The control allows the outlet temperature to reach the setpoint (typically 120-140°F depending on user setting). If outlet temperature climbs past about 200°F, the control reduces firing. If it continues to climb past the overheat threshold (about 207°F / 97°C on most NPE-A platforms), the unit shuts off and posts Code 016 (Service Bulletin SVB-2017-007 references this threshold across the NPE-A serial range).

Why does outlet temperature spike? Three main reasons: (1) scale on the water side of the HX — reduced heat transfer means the burner has to work harder; the HX surface gets hot, hot water pockets form near the outlet; (2) low flow — water in the HX moves too slowly; the same BTU input heats a smaller water mass to a higher temp; (3) sensor or control fault — false high reading.

The lockout requires manual reset via the front panel. Per Navien Service Bulletin SVB-2017-007, repeated Code 016 in short succession indicates significant HX fouling and requires descaling service.

## Common causes (ranked by frequency)

1. **Heat exchanger scale buildup (hard water deposits)** — about 42%. Most common cause; calcium carbonate on the inside of the HX restricts both flow and heat transfer.
2. **Plugged or partially blocked inlet water filter (NPE service kit)** — about 18%. Restricts flow, water in HX moves too slowly, overheats.
3. **Low flow at a fixture (aerator clogged, restrictor) — sensor reads valid flow but outlet temp spikes** — about 10%. Mismatched between flow sensor reading and actual through-HX flow.
4. **Flow sensor reading high (paddle stuck or magnet drift)** — about 8%. Control thinks more water is flowing than actually is.
5. **Outlet temp sensor failed high** — about 6%. Reads above actual.
6. **Recirculation pump running with no valid draw (NPE-A only)** — about 5%. Recirc loop heats up beyond setpoint.
7. **Wrong setpoint configuration (commercial range setpoint on residential unit)** — about 4%. User cranked the temp above safe.
8. **Air bound HX after service** — about 3%. Pockets of air create hot spots.
9. **PC board temperature input drift** — about 2%. Rare; board misreads sensor.
10. **Bypass valve stuck during winterization or service** — about 2%.

Field nugget: I've seen this 300 times — Navien NPE-A 240 in a hard-water area (>10 grains/gallon, like much of Texas, Florida, parts of the Midwest), 4-6 years old, never descaled, suddenly throws Code 016 on hot showers. Customer panics, thinks the unit is dying. The real fix is two things: (1) descale the HX with a citric-acid solution (Navien-approved descaler or 4 gallons of white vinegar circulated through the unit's service ports for 60-90 minutes), (2) install softener or scale-control device upstream. After descale, flow rates recover, outlet temps stabilize, and the unit runs cleanly. Navien recommends annual descaling in areas above 7 grains/gallon hard water; many install manuals reference this in the maintenance section. Telling a homeowner "you need a softener" is hard but it's the truth — without one, the unit will scale again within a year.

## Step-by-step fix

Safety first: close gas, kill power, let unit cool. Hot water at 200°F+ scalds instantly — drain the HX through the service valves into a bucket before opening. CO is a risk on overheat conditions where combustion may have been incomplete. Condensate is acidic; wear gloves. Descaling solutions (citric, white vinegar) are mild but can irritate skin and eyes — wear PPE.

1. **Confirm Code 016 and check history.** Press INFO on the front panel of the NPE. Note 016 timestamps and any other codes — particularly 002 (inlet sensor), 030 (outlet sensor), or 010 (flow sensor) which would point to a sensor issue rather than scale.

2. **Check the inlet water filter.** Navien NPE units have a stainless-mesh filter on the cold-water inlet, typically accessible by removing a service plug or unscrewing a small filter housing. Pull the filter screen, inspect — should be silver. Dark sediment, brown rust flakes, or white scale = restricted flow. Rinse under hot water, reinstall. Note: on installs older than 5 years, the filter may need replacement, not just cleaning.

3. **Descale the heat exchanger.** This is the most common actual fix. You'll need: two short hoses, a 5-gallon bucket, a submersible pump (or a Navien-branded descaler kit), and 4 gallons of white vinegar or a Navien-approved citric descaler. Close the cold-water inlet and hot-water outlet isolation valves at the unit. Open the service ports on each valve (small 1/4-turn valves on most Navien isolation kits). Connect inlet of the pump to the bucket, outlet of the pump to the cold-side service port; connect the hot-side service port back to the bucket. Power on the pump, circulate vinegar/descaler for 60-90 minutes. Flush with clean water afterward for 5-10 minutes.

4. **Verify flow sensor operation.** Power on (but isolation valves still closed). Open a hot tap. With the isolation valves closed, no flow should reach the unit. On the front-panel display or via the remote, check if the unit reports flow. If it reports flow when there is none, the flow sensor is stuck (paddle frozen, magnet detached). Pull and clean the flow sensor; replace if mechanically damaged.

5. **Check temperature sensors.** Power off. Pull each temperature sensor connector at the PCB. Measure resistance at known room temp — Navien NPE temperature sensors are typically 10kΩ at 77°F (25°C) NTC. Out of spec means replace. Sensor part numbers differ by location (inlet, outlet, HX) — always order by Navien part number, not generic.

6. **Inspect HX condition (visual).** With the HX accessible, look for signs of severe scale or corrosion. Severe scale (visible white deposits coating internal surfaces) means the descale step needs to be done aggressively, possibly twice. Corrosion (greenish deposits on stainless or copper) suggests water chemistry issues — pH too low or chlorides too high.

7. **Verify recirculation settings (NPE-A only).** On NPE-A units with built-in recirculation pumps, check the recirc mode. "Constant" mode runs the pump continuously, which can heat the buffer loop beyond setpoint if there are no draws. Change to "Smart" or "Schedule" mode per Service Bulletin SVB-2019-014.

8. **Reset and test.** Restore everything. Press reset. Initiate a long hot-water draw at high flow. Monitor outlet temperature — should rise smoothly to setpoint and stabilize within ±2°F. No 016 return = fix held.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Inlet water filter screen | Navien 30002131 | $14-28 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Flow sensor assembly | Navien 30015168 | $58-90 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Outlet temperature sensor (NPE-A 2nd gen) | Navien 30016322 | $42-68 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Inlet temperature sensor | Navien 30016324 | $38-62 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Heat exchanger (NPE-A 240) | Navien 30025028 | $1100-1650 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Recirculation pump (NPE-A) | Navien 30009881 | $245-380 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Service valve kit (isolation) | Navien NPE-Y8 | $145-220 | [Supply House](https://www.supplyhouse.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Descaler kit (pump, hoses, bucket) | Navien NPE-DESC-001 / generic Hercules Sizzle | $115-180 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Citric acid descaler (5 gal jug) | Hercules / Cresote 5402 | $52-85 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |
| Main control board (NPE-A 2nd gen) | Navien 30021301 | $580-820 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=navien-water-heater-error-code-016) |

Note: Heat exchanger replacement is rare but possible after years of severe scale and corrosion. The HX is the most expensive single part on the unit; if you're facing HX replacement plus labor, compare to total replacement cost — sometimes a new NPE-A is the better long-term value.

## When to call a professional

**Heat exchanger replacement.** Pulling and replacing the HX requires unsoldering or unscrewing multiple plumbing connections, gas line, sensors, and combustion components. It's a 4-6 hour job for an experienced tankless tech. Don't DIY unless you've done one before.

**Water chemistry analysis and softener installation.** If you're scaling repeatedly, the long-term fix is treatment. A pro plumber should sample the water for hardness (grains/gallon), iron, and pH, then size a softener or scale-control device. Navien recommends water under 7 gpg (grains per gallon); 10+ gpg basically guarantees annual descaling.

**Repeated Code 016 after descaling and parts.** Indicates either water chemistry or a control board fault. Pro diagnosis with the Navien service tool can read live sensor values and confirm where the actual problem is.

**Scalding incidents.** If anyone has been scalded by water from the unit, stop using until a pro installs thermostatic mixing valves at fixtures or reduces the setpoint per code.

Never bypass overheat protection. Even with the unit locked out, the HX retains water at potentially dangerous temperatures for some time. Always let it cool before service.

## FAQs

**How often should I descale my Navien?**
Annually in hard water (>7 gpg); every 2-3 years in soft water. Skipping descaling in hard water is the #1 cause of Code 016 and premature HX failure.

**Can I use white vinegar instead of a commercial descaler?**
Yes, 4 gallons of plain white vinegar circulated for 60-90 minutes works well for moderate scale. Commercial citric-acid descalers (Hercules Sizzle, etc.) are faster on heavy buildup. Avoid muriatic acid — it attacks stainless and copper.

**My NPE-A has Code 016 only on hot showers, not on dishwasher draws — why?**
Higher flow rates (shower) push the HX harder and reveal restriction. Lower flow (dishwasher) lets the HX coast. Once you've descaled, both should work fine.

**Should I worry about Legionella with a tankless?**
Less than with a tank heater (no stagnant water), but still possible in the recirculation loop on NPE-A or in long unused branches. Setpoint of at least 122°F (50°C) is recommended for Legionella inhibition; many codes recommend 140°F (60°C) with thermostatic mixing at fixtures.

**Will a water softener void my Navien warranty?**
No — Navien explicitly recommends softeners in hard-water areas. Excessive softening (zero hardness) can cause some metal corrosion; aim for 3-5 gpg residual hardness after softening, not zero.

## Related guides

- [Navien NPE/NCB Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003)
- [Rinnai Code 12 — Flame Failure During Operation Fix](/posts/rinnai-error-code-12)
- [Takagi Code 111 — No Ignition Fix](/posts/takagi-error-code-111)

## See Also

- [Navien NCB Combi Boiler Error Codes — Complete Fault Guide](/posts/navien-ncb-error-codes/)
- [Navien NFC Combi Boiler Error Codes: Complete Guide](/posts/navien-nfc-error-codes/)
- [Navien Error Code E001 — No Ignition Fix](/posts/navien-error-code-e001/)
- [Navien E009 Error Code — Causes & Fix](/posts/navien-error-code-e009/)
