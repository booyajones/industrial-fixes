---
title: "Manitowoc E03 Error Code — Probe / Thermistor Open Fix"
description: "E03 means the control board cannot read the evaporator thermistor — the circuit is open. Half the time it's a connector that came unseated during cleaning;..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: manitowoc-e03-error-code
featured: false
draft: false
tags:
  - manitowoc
  - commercial-refrigeration
  - ice-machine
  - probe-thermistor-open
  - troubleshooting
---
## Quick answer

E03 means the control board cannot read the evaporator thermistor — the circuit is open. Half the time it's a connector that came unseated during cleaning; the other half it's a wire chafed through against the compressor or condenser frame.

## What Manitowoc E03 means

E03 is a sensor open-circuit fault. The Indigo NXT controller (and the older S- and Q-series boards) constantly read voltage across the evaporator thermistor — a 10kΩ NTC sensor clipped to the suction tube near the evaporator outlet. As the coil cools during freeze, thermistor resistance climbs and the board uses that resistance to time the freeze cycle.

When the board sees infinite resistance (an open circuit), it doesn't know the coil temperature, can't safely run the cycle, and throws E03. The machine locks out and won't start a new cycle until the fault clears. On newer Indigo NXT units, the controller displays "PROBE FAULT" alongside the E03 code.

Open circuits in the thermistor leg happen for three reasons, in this order: the molex connector at the board got bumped loose, the wire chafed through somewhere on its run, or the thermistor itself failed open. The thermistor element rarely fails — they're glass-bead NTCs and they're either fine or smashed. If it's not physically damaged, the problem is almost always in the wiring.

## Common causes (ranked by frequency)

- **Connector at the control board unseated** — often happens after someone has been inside the box (cleaning, board swap, voltage check).
- **Wire chafed through against compressor housing or chassis frame** — vibration over years.
- **Broken wire at the thermistor clip** — flexing fatigue where the lead exits the sensor body.
- **Failed thermistor (rare, open mode)** — physical damage or moisture intrusion into the bead.
- **Corroded connector pins** — common on units in salty kitchens (seafood prep, coastal installs).
- **Bad control board input** — last suspect, almost never the actual problem.

## Step-by-step fix

1. **Power the unit off completely.** Pull the disconnect, don't just hit the power switch. Thermistor leads sit close to 120V/240V wiring inside the control box, and you'll be working in there.

2. **Locate the evaporator thermistor and its harness path.** On Indigo NXT IDT and IYT units, the thermistor clips to the suction line just past the evaporator outlet, behind the right-side panel on most models. Trace the two-wire harness back to the control board. Note where it routes — past the compressor, behind the condenser, through grommets. You're looking for chafe points.

3. **Inspect the molex connector at the board.** Pull the connector, look at the pins for green corrosion or bent terminals, and reseat it firmly. On 60% of E03s I get called for, this alone is the fix. If the connector pins look corroded, replace the connector pigtail — Manitowoc sells a service pigtail under the K-00339 thermistor kit.

4. **Ohm out the thermistor leads end-to-end.** With the connector unplugged at the board, set your multimeter to resistance and check across the two pins of the harness side connector. At room temperature (~70°F), you should see approximately 11–12 kΩ. At 32°F (machine recently iced down), you should see ~32 kΩ. Open circuit means the wire is broken somewhere or the thermistor is dead.

5. **Isolate the thermistor from the harness.** Unclip the thermistor from the suction line and unplug it from its inline connector (if equipped). Ohm the thermistor directly across its two leads. If you get a valid reading there but open at the board, the break is in the harness — physically inspect every inch of the wire run. If the thermistor itself reads open, replace it.

6. **Inspect chafe points along the harness.** The known bad spots: where the harness crosses the compressor mounting bracket, where it passes through any sheet-metal grommet, and where it bundles with other lines near the condenser fan. Look for shiny spots on the wire jacket, exposed copper, or insulation melted from contact with a hot line. Wrap any wear point with high-temp wire loom and re-route with zip ties to keep it off metal edges.

7. **Replace the thermistor with the K-00339 kit if it tests open.** Use the new wire clip — don't reuse the old one, the spring tension is shot and the new sensor will fall off the suction line on the next harvest cycle vibration. Route the new harness following the original path, but secure it away from any compressor or condenser fan contact points.

8. **Verify the repair.** Reseat all connectors, restore power, and clear the fault. Watch one complete freeze cycle. The displayed evaporator temperature on the diagnostic screen should drop smoothly from room temp down to roughly 8–12°F over the course of freeze. If it shows wild jumps, no movement, or pegs at -40°F, you've got a different sensor problem — likely the new thermistor isn't making good thermal contact with the suction line.

> **Field knowledge nugget:** On Indigo NXT IDT0900 units installed between roughly 2018 and 2020, the evaporator thermistor lead routes too close to the compressor head and chafes through within 4 years of run time — the failure point is consistent, about 6 inches from the thermistor clip where the harness passes near the discharge line. Before you replace the thermistor on any IDT0900 in that vintage, pull the harness loom open at that point and look for chafe. If you replace the thermistor without re-routing, the new one will fail at the same spot in another 3–4 years. The fix is to re-route the harness behind the compressor mounting bracket and zip-tie it away from the discharge line. Manitowoc quietly updated the harness routing on 2021+ builds — if you compare an old and a new unit side by side, the route is visibly different.

**Safety:** The control box contains line-voltage terminals within inches of the low-voltage thermistor harness. Pull the disconnect, not just the front panel switch, before working on the harness. Test for voltage with a non-contact tester before putting hands in the box, even if you're sure power is off — I've seen UL-listed disconnects fail to break one leg on a 208V system, and someone got hurt.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Evaporator thermistor kit | K-00339 | $95–$140 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e03-error-code) |
| Thermistor clip only | 000007541 | $14–$22 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e03-error-code) |
| Control board harness loom (3/8" split) | n/a | $12–$20 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Manitowoc service pigtail (molex) | 7628021 | $32–$48 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-e03-error-code) |
| High-temp wire ties (UL94 V-0, 10 in) | n/a | $9–$15 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

The thermistor kit is the right part to order for any E03 that turns out to be a hardware failure — it includes the sensor, the clip, the inline connector, and the gasketing material.

## When to call a professional

Call a CFESA-certified tech if:

- You've replaced the thermistor with a known-good unit, confirmed the harness is intact end-to-end, and the board still shows E03 — you've got a board-level input failure and that's a control board replacement decision.
- The control board shows water damage, burn marks, or popped components. Don't keep poking at it; replace the board.
- The harness shows multiple chafe-through points, indicating a vibration problem in the cabinet. Compressor mounts may be failing.
- E03 is intermittent and you can't reproduce it — running diagnostics with the controller's service menu (and reading recent fault history) requires the Manitowoc service tool.
- You're in a warranty period. Manitowoc will not honor a sensor warranty claim if a non-authorized servicer has already opened the harness.

## FAQs

**Can I bypass the thermistor temporarily to keep the machine running?**
No. The board uses the thermistor to time freeze cycles safely. Without a valid reading, it can't tell when to harvest, and you'll either get long freeze cycles or harvest at the wrong time, both of which can damage the evaporator. There's no jumper trick that works on Indigo NXT controllers.

**My thermistor reads correctly with a meter but the machine still throws E03 — what gives?**
Reseat both ends of the harness, then look for a partial short to ground somewhere along the wire run. A wire that's almost chafed through can ohm out fine with no load on it, but pulls down when the board energizes the circuit. Wiggle the harness while watching resistance on your meter.

**Is the harvest thermistor the same part as the evaporator thermistor?**
On most Indigo NXT machines there's a single evaporator thermistor that's used for both freeze and harvest timing. Some larger commercial models have a separate bin thermistor and a discharge sensor — check the wiring diagram on your specific unit. The K-00339 kit fits the evap sensor on IDT/IYT machines.

**Will moisture in the control box cause E03?**
Yes, if the molex connector at the board gets wet. The thermistor circuit is low voltage and even minor corrosion across the pins can open the circuit. If you find moisture in the control box, fix the source — usually condensate dripping from above or a roof leak — before the board itself corrodes.

**How long does the K-00339 thermistor kit usually last?**
On a properly routed harness, 8–12 years. On a unit with the factory routing problem (IDT0900 2018–2020), expect 3–5 years until the same chafe point fails again. Re-route the harness when you replace the sensor and you'll get the long service life.

## Related guides

- [Manitowoc E01 Error Code — Long Freeze Cycle Fix](/manitowoc-e01-error-code)
- [Manitowoc E54 Error Code — Water Curtain Switch Open Fix](/manitowoc-e54-error-code)
- [Manitowoc HPCO Error Code — High Pressure Cut Out Fix](/manitowoc-hpco-error-code)

## See Also

- [Manitowoc E02 Error Code — Long Harvest Cycle Fix](/posts/manitowoc-e02-error-code/)
- [Manitowoc vs Scotsman Ice Machines — A Commercial Tech's Honest Comparison (2026)](/posts/manitowoc-vs-scotsman-ice-machines/)
- [Manitowoc Ice Machine Error Code 4 — Water Curtain Fault Fix](/posts/manitowoc-ice-machine-error-code-4-water-curtain/)
- [Manitowoc Ice Machine E01 Error Code — Causes & Fix](/posts/manitowoc-ice-machine-error-code-e01/)
