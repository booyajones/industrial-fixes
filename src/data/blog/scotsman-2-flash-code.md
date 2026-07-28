---
title: "Scotsman 2-Flash Code — Long Freeze Cycle Fix"
description: "Two flashes on a Scotsman Prodigy (or \"FC\" extended on a Prodigy Plus) means the freeze cycle ran past the maximum time limit programmed into the board —..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: scotsman-2-flash-code
featured: false
draft: false
tags:
  - scotsman
  - commercial-refrigeration
  - ice-machine
  - long-freeze-cycle
  - troubleshooting
---
## Quick answer

Two flashes on a Scotsman Prodigy (or "FC" extended on a Prodigy Plus) means the freeze cycle ran past the maximum time limit programmed into the board — typically 60 minutes — without the harvest thermostat satisfying. The unit safed off rather than keep running. In my experience the cause splits roughly 40% condenser, 30% water side, 20% refrigerant charge, and 10% TXV or other expansion-device drift.

## What the 2-flash code means on a Scotsman

The freeze cycle on a healthy Prodigy or Prodigy Plus should complete in 12-25 minutes depending on head model and ambient — a C0322 at 70°F room / 50°F water should be near 17 minutes; a C0830 in a 95°F mechanical room with hot incoming water might legitimately run 22-24 minutes. The control board starts a freeze timer the moment the compressor energizes. If the harvest thermostat (the bulb clipped to the evaporator suction line) doesn't drop into the harvest-initiate range before the maximum freeze time expires, the controller logs a 2-flash and locks out.

On Prodigy, that's two flashes on the front-panel LED. On Prodigy Plus, it's an "FC" or "Long Freeze" entry in the code history — pull it up via Service > Codes from the menu. Brilliance units will throw a more descriptive "Freeze Time Exceeded" message because they have a real display.

The 2-flash is not the failure itself — it's a symptom that the evaporator never got cold enough to satisfy the harvest sensor. Your job is to figure out why. Diagnostic mode entry: hold OFF + ON for 5 seconds on Prodigy; menu navigation on Prodigy Plus. While you're in diagnostic mode, look at the freeze-cycle time on the most recent successful cycles in history. A unit that used to freeze in 17 minutes and now runs 45 has a different problem than one that's always been slow.

## Common causes (ranked by frequency)

1. **Dirty air-cooled condenser** — the single most common cause. Lint, grease aerosol, and dust pack the fin face. Head pressure climbs, capacity drops, freeze time extends. Always check this first.
2. **Low water flow to the evaporator** — clogged inlet screen, scaled water distributor tube, weak water pump, or a partially-stuck float valve. Symptoms include incomplete cube formation and a slimy/scaled distributor.
3. **Low refrigerant charge** — slow leak, usually at a Schrader, a flare on the receiver line, or a brazed joint on the suction line. Look for oil staining first, not bubbles in the sight glass (Prodigy doesn't have one).
4. **Failed or drifting TXV** — superheat goes high, evaporator under-feeds, freeze cycle extends. Less common than #1-3 but real, especially on older C0830 / C0530 units past the 8-year mark.
5. **Water-cooled units: low water flow on the condenser side** — partially closed water-regulating valve, scaled water-cooled condenser tubes, or a building hot-water cross-connection.
6. **Failed harvest thermostat** — reads warmer than the evap actually is, so the cycle never satisfies. Bench-test like the bin stat.

## Step-by-step fix

1. **Read the code history and recent freeze times.** Enter diagnostic mode. Note current and historical 2-flash counts plus the last 5-10 freeze-cycle durations if the firmware logs them. A trend (slowly increasing freeze time over weeks) points to a slow leak or progressive condenser fouling. A sudden jump from 17 to 60 minutes points to a flow blockage or a stuck component.

2. **Inspect and clean the condenser.** Pull the front panel. On air-cooled Prodigy heads, the condenser sits behind a foam filter on most models — that filter is almost always destroyed or missing. Vacuum the fin face, then comb out any bent fins. If it's grease-caked (any kitchen within 10 feet of a fryer), pull the condenser and treat it with a no-rinse coil cleaner. Don't pressure-wash an aluminum/copper coil — you'll lay the fins flat.

3. **Check the air-handling path.** Confirm the rear/side air intakes are clear. Operators love to push the unit tight to a wall or stack cardboard against the side panel. Minimum clearance per Scotsman spec is 6 inches on all sides for an air-cooled head; less than that and ambient air re-circulates and head pressure climbs even with a clean condenser.

4. **Verify water flow and quality.** Pull the inlet hose at the float valve, run it into a measuring cup, and confirm at least 12-15 GPH flow. Inspect the float valve seat — calcium buildup keeps the valve cracked open or stuck closed. Check the water distributor tube above the evaporator: it should be sheeting water evenly across all sections. A dry section means a plugged orifice; pull the distributor and soak it in nickel-safe scale remover. **Critical insight: on C0530 and C0630 Prodigy units, the rear-most distributor orifices scale shut first because the water pump pushes harder at the inlet end — when you see an evaporator with poor cube formation on only the back half, it's almost always the distributor, not the TXV.**

5. **Take operating pressures.** Connect a manifold gauge set. On R-404A air-cooled Prodigy at 70°F / 50°F water, you should see suction around 18-24 psig early in the freeze settling to 12-18 psig late, and discharge around 200-230 psig. Brilliance units running R-290 (propane) require a hydrocarbon-rated gauge set and you should not be in the unit at all without HC training and the correct recovery setup. R-290 pressures look different — don't apply R-404A numbers. Low subcooling and high superheat point to undercharge. High head and low subcooling point to a condenser or airflow issue.

6. **Inspect for refrigerant leaks if charge is low.** Electronic leak detector around all brazed joints, Schraders, and flares. Soap bubbles on suspect spots. The most common leak point on a 5+ year old Prodigy is the suction-line Schrader cap o-ring — tighten the cap, retest. Don't top off and walk away on a Scotsman without finding the leak; the EPA log alone makes it not worth it.

7. **Bench-test the harvest thermostat.** Same procedure as the bin stat — closed in ice water, open at room temp. OEM part 11-0408-21 (same body, different cut-in/cut-out range on some models — verify by part number, not appearance).

8. **Inspect the TXV if everything else checks out.** Confirm bulb is clipped tight to the suction line at 4-5 o'clock position with insulation tape over it. A loose or uninsulated bulb reads ambient instead of suction-line temp and the TXV hunts. Superheat at the bulb location should be 6-10°F mid-freeze; over 15°F and the TXV is likely starved or failing.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|------|------------|--------------|--------------|
| Condenser air filter (Prodigy) | 02-3927-01 | $18-$32 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-2-flash-code) |
| Float valve assembly | 12-2917-01 | $52-$78 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-2-flash-code) |
| Water distributor tube (C0322) | 02-3879-01 | $42-$68 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-2-flash-code) |
| Harvest thermostat | 11-0408-21 | $48-$72 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-2-flash-code) |
| TXV (C0530/C0630 air-cooled R-404A) | 12-2849-01 | $145-$210 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-2-flash-code) |
| Water pump | 12-2588-21 | $185-$260 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-2-flash-code) |
| Nickel-safe scale remover (1 gal) | — | $24-$38 | [Amazon](https://amazon.com) |
| Fin comb set | — | $14-$22 | [Amazon](https://amazon.com) |

Confirm exact part number against your head's serial-plate model and revision — Scotsman ran multiple distributor and TXV variants across model years.

## When to call a professional

Anything sealed-system — recovery, charge adjustment, leak repair, TXV replacement — requires EPA Section 608 certification. If you're not certified, stop at "the head pressure is high" or "the suction looks low" and call a refrigeration contractor. Same for any work on Brilliance R-290 units; those are hydrocarbon and have to be handled with the right tools and ventilation. If the unit is under warranty and the cause is a TXV or compressor, call Scotsman before you cut a single line — warranty claims get denied for unauthorized sealed-system work.

## FAQs

**Q: How long should a freeze cycle actually take?**
A: On a Prodigy C0322 at 70°F ambient and 50°F incoming water, expect 15-19 minutes. C0530 and C0630 run 17-22 minutes. Hot ambient (90°F+) or warm incoming water (70°F+) legitimately stretches that 25-40%. Compare to historical cycle times for that specific unit, not a textbook number.

**Q: I cleaned the condenser and the cycle time barely improved. What next?**
A: Two possibilities. First, you cleaned the face but the back of the coil and the fan blade are still loaded — pull the condenser and inspect both sides. Second, the airflow path itself is restricted (intake louvers blocked, install clearance violated). Don't move on to refrigerant until you've verified condenser leaving-air temperature is no more than 25-30°F above ambient.

**Q: The unit makes ice but the cubes are half-formed and the cycle is long. Charge?**
A: Almost always water side, not refrigerant. Cubes are formed by water flowing over a cold evaporator; if the water flow is uneven (clogged distributor) or insufficient (weak pump, scaled lines), you get partial cubes and an extended freeze. Refrigerant problems usually show as small but fully-formed cubes, not partial ones.

**Q: Can I just replace the harvest thermostat as a first step?**
A: You can, and on a high-hours unit it's not a bad preventive move (they're $48 and 20 minutes to swap), but you'll mask the real cause if you don't also check condenser and water flow. I only lead with the harvest stat if bench-testing shows it out of spec.

**Q: My pressure readings look fine but the cycle is still long. What am I missing?**
A: Check the suction-line temperature at the compressor inlet versus the evap outlet. A big delta means the suction line isn't insulated properly or there's a heat-exchanger issue. Also check the inlet water temperature — if the building is feeding 85°F water (common with under-counter installs on a hot-water line by mistake), the cycle physics are working against you and no refrigerant fix will help.

## Related guides

- [Scotsman 1-Flash Code — Bin Full / Bin Thermostat Fix](/posts/scotsman-1-flash-code)
- [Scotsman 3-Flash Code — Long Harvest Cycle](/posts/scotsman-3-flash-code)
- [Scotsman 4-Flash Code — High Discharge Temperature](/posts/scotsman-4-flash-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Hoshizaki vs Manitowoc ice machines](/posts/hoshizaki-vs-manitowoc-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc vs Scotsman ice machines](/posts/manitowoc-vs-scotsman-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigeration vacuum pump](/posts/best-vacuum-pump-for-refrigeration/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc E01 long freeze cycle fix](/posts/manitowoc-e01-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc HPCO high pressure cutout](/posts/manitowoc-hpco-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** Hoshizaki E2 long freeze cycle fix
