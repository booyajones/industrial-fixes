---
title: "Scotsman 1-Flash Code — Bin Full / Bin Thermostat Fix"
description: "A single flash on a Scotsman Prodigy (or \"BF\" / \"Bin Full\" on a Prodigy Plus alphanumeric display) means the bin thermostat has opened and told the control..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: scotsman-1-flash-code
featured: false
draft: false
tags:
  - scotsman
  - commercial-refrigeration
  - ice-machine
  - bin-full
  - troubleshooting
---
## Quick answer

A single flash on a Scotsman Prodigy (or "BF" / "Bin Full" on a Prodigy Plus alphanumeric display) means the bin thermostat has opened and told the control board the bin is full. About 60% of the calls I run for this code are a genuinely full bin — the other 40% are a pinched capillary, a bridged probe tip, or a tired sensor that needs to come out.

## What the 1-flash code means on a Scotsman

The 1-flash code is the Bin Full signal. On legacy Prodigy heads (C0322, C0530, C0630, C0830 and the matching B-series bins), Scotsman uses a capillary-tube thermostat clipped to the inside wall of the bin. The capillary is gas-charged. When ice piles up against the bulb, the charge contracts, the contacts open, and the control board ends the freeze cycle and locks out the compressor until the bulb warms back above the cut-in temperature (roughly 55°F on most factory specs).

On the Prodigy Plus C0322 / C0522 / C0722 / C0830 platform, the alphanumeric display will show **BF** rather than a flash count, but it is the exact same circuit — the controller is only watching the bin thermostat's normally-closed contacts. Brilliance units (the AC/AS/MV series) replaced the cap-tube with a thermistor and reads temperature directly, so for those models a "bin full" is a calculated value rather than a mechanical opening. The diagnostic path is similar but the failure modes are different — a Brilliance bin thermistor will usually throw an out-of-range error rather than a stuck-full reading.

To enter diagnostic mode on a Prodigy, press and hold the **OFF** and **ON** buttons simultaneously for 5 seconds — the LEDs will sequence and you can read the active and historical codes. On a Prodigy Plus, scroll the menu with the up/down arrows to **Service** then **Codes**. Brilliance units expose this through the touch interface under Diagnostics.

The lockout matters: even after you've cleared the actual cause, the unit won't restart until the bin thermostat closes again (warms up) or you cycle power. Don't waste 20 minutes chasing a ghost — pop the cover, jumper the bin thermostat leads at the control board, and if the machine starts up immediately the thermostat circuit is your problem, not the head.

## Common causes (ranked by frequency)

1. **Actual full bin** — operator hasn't scooped, ice is mounded against the bulb. Embarrassingly common on weekend service calls.
2. **Ice bridging the thermostat bulb** — ice has frozen across the bulb and the bin wall, holding the sensor cold even when the bin level drops. Common in high-humidity kitchens.
3. **Pinched or kinked capillary tube** — usually from a sloppy reassembly after a previous service. The capillary runs behind the splash shield on Prodigy Plus 2019-2021 builds and gets crushed.
4. **Failed (lost charge) bin thermostat** — the gas charge has leaked from the bulb or capillary. Reads open at room temperature.
5. **Refrigerant leak in the bulb/capillary itself** — rare but real, mostly from corrosion at the bulb-to-capillary braze.
6. **Wiring fault** — chafed harness inside the bin, open at the control board J-plug, or a loose terminal at the thermostat body.

## Step-by-step fix

1. **Confirm the actual bin level.** Open the door, look at the bin. If ice is mounded above the thermostat bulb, scoop the bin down 4-6 inches below the bulb and wait 3 minutes for the thermostat to close. If the unit kicks on, the code was legitimate — talk to the operator about scoop frequency.

2. **Enter diagnostic mode and pull the history.** On Prodigy hold OFF+ON for 5 seconds; on Prodigy Plus go to Service > Codes. Note how many 1-flash codes are logged and the time stamps. A unit throwing a 1-flash three times a day during a slow lunch shift is almost never a real full-bin condition.

3. **Inspect the bulb for ice bridging.** Pull the splash curtain. Look for a frozen ice bridge between the thermostat bulb and the bin liner wall. Break it free with a plastic scraper — never a screwdriver, you'll puncture the bulb. If you find a bridge, also look for a water dripper or splash pattern feeding it; the cure is rerouting the splash curtain, not just removing the ice.

4. **Trace and inspect the capillary.** Follow the cap tube from the bulb back to the thermostat body. On C0322 Prodigy Plus units built 2019-2021, the capillary routes behind the right-side splash shield and gets pinched against the shield bracket during reassembly. This is the #1 false-positive cause of the 1-flash code on those serial ranges. A pinched cap tube reads exactly like a legitimately full bin.

5. **Bench-test the thermostat.** Disconnect both leads. With the bulb at room temperature (above 60°F), you should read continuity (closed contacts). Plunge the bulb into a cup of ice water — within 30-45 seconds the contacts should open and you should read OL. If it stays closed in ice water or stays open at room temp, it's done.

6. **Jumper test at the control board.** With the thermostat leads disconnected at the board (J6 on Prodigy, J3 on Prodigy Plus — verify against the legend on the cover), jumper the two terminals. If the machine starts a freeze cycle and runs normally, you've isolated the fault to the thermostat or its wiring. Do not leave a jumper installed and walk away — the bin will overflow.

7. **Replace the bin thermostat.** OEM part is Scotsman 11-0408-21 on most Prodigy heads. Mount the new bulb in the original clip, route the capillary exactly as you found it (or better — away from the splash shield if you found a pinch), and tighten the clip just enough to hold the bulb. Crushing the bulb in the clip is the #2 way to kill a fresh thermostat.

8. **Verify, reset, and document.** Power-cycle the unit, watch a full freeze and harvest, confirm the bin thermostat opens when you pack ice around the bulb, and clear the code history in diagnostic mode. Write the fix on the unit log so the next tech doesn't chase the same ghost.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|------|------------|--------------|--------------|
| Bin thermostat (Prodigy / Prodigy Plus cap-tube) | 11-0408-21 | $48-$72 | [Parts Town](https://partstown.com) |
| Bin thermistor (Brilliance series) | 12-2920-01 | $58-$85 | [Parts Town](https://partstown.com) |
| Thermostat mounting clip | 02-3413-01 | $6-$12 | [Parts Town](https://partstown.com) |
| Splash curtain (C0322) | 02-3866-01 | $34-$58 | [Parts Town](https://partstown.com) |
| Control board (Prodigy Plus) | 12-2838-21 | $295-$420 | [Parts Town](https://partstown.com) |
| Multimeter (Fluke 117 or equivalent) | — | $189-$220 | [Amazon](https://amazon.com) |
| Plastic ice scraper | — | $8-$14 | [Amazon](https://amazon.com) |

Prices reflect what I've paid in 2025-2026 — verify before you quote a customer.

## When to call a professional

If the bin thermostat tests good, the wiring is clean, and the unit still throws a 1-flash within minutes of a clean bin, you may be looking at a control board issue — a stuck input on the bin-thermostat channel. Board replacement on a Prodigy Plus runs $295-$420 for the part alone and requires the dip-switch and parameter configuration to match the head model. If you're not comfortable setting the model parameters on a fresh board, call a CFESA-certified tech. Same goes for any sealed-system work if you find the cap tube has lost charge from a braze-joint leak — that's manufacturer warranty territory if the unit is under 3 years old.

## FAQs

**Q: My Prodigy throws a 1-flash but the bin is half empty. What now?**
A: Pull the splash curtain and check for an ice bridge on the thermostat bulb first — that's the most common cause when the bin clearly isn't full. If the bulb is clean, jumper the thermostat at the board to confirm it's a sensor problem and not a control board input.

**Q: Can I just leave the thermostat jumpered until I get the part in?**
A: No. The jumper disables the bin-full safety entirely. The unit will run until ice mounds up into the evaporator and refreezes the harvest cycle, and you'll be replacing an evap, not a thermostat. Take the unit out of service or have the operator scoop manually every 2 hours.

**Q: How do I tell if it's the thermostat or a bridged probe without pulling parts?**
A: Bench-test logic: with the bin empty and the bulb at room temp (let it sit 10 minutes), measure continuity across the thermostat leads at the board. Closed = thermostat is fine, look at wiring or ice bridging. Open = thermostat is bad or the bulb is still cold from an ice bridge you didn't see.

**Q: Does the Brilliance bin thermistor throw a 1-flash too?**
A: Brilliance uses the alphanumeric display, not flashes. A "Bin Full" message can come from either a legitimately cold thermistor reading or an out-of-range fault — check the diagnostic history. The thermistor (12-2920-01) reads roughly 10kΩ at 77°F; anything outside 4kΩ-30kΩ at room temp means the sensor is bad.

**Q: After I replaced the thermostat, the code came back in 48 hours. Did I get a bad part?**
A: Possible but unlikely. More likely you pinched the capillary during reassembly — same failure mode as the original. Pull the splash shield, trace the cap tube, and check for crush marks against the bracket. Reroute it forward of the shield, not behind it.

## Related guides

- [Scotsman 2-Flash Code — Long Freeze Cycle](/posts/scotsman-2-flash-code)
- [Scotsman 3-Flash Code — Long Harvest Cycle](/posts/scotsman-3-flash-code)
- [Scotsman 5-Flash Code — Pressure Sensor Fault](/posts/scotsman-5-flash-code)
