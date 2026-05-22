---
title: "GE Dishwasher Error Code LC — Leak Detected Fix"
description: "GE dishwasher error LC means the leak-detection sensor at the bottom of the cabinet (a small float switch in the base pan or, on newer Profile models, a..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Industrial Error Code Fixes"
slug: ge-dishwasher-error-code-lc
featured: false
draft: false
tags:
  - ge
  - leak-detected
  - troubleshooting
---
## Quick answer

GE dishwasher error LC means the leak-detection sensor at the bottom of the cabinet (a small float switch in the base pan or, on newer Profile models, a conductive leak sensor strip) has triggered, and the control board has paused the cycle and energized the drain pump to evacuate water. About 30% of LC codes are false triggers from the leak sensor itself failing — corroded contacts, stuck float, or moisture residue on a strip-style sensor — not actual leaks. Pull the kick panel and inspect for visible water *before* assuming the sensor is bad.

## What LC means on a GE dishwasher

GE dishwashers (GDF, GDT, PDT, CDT series — Profile, Cafe, and standard GE lines) have included a base-pan leak detector since about 2014, mandated by UL flood-prevention standards. The detector is typically one of two designs: an older float-and-microswitch design (a foam float in a small reservoir in the base pan, with a magnetic switch under the dishwasher's floor pan), or a newer conductive-trace strip (a flat sensor with two exposed traces that complete a circuit when bridged by water).

When the base pan accumulates more than about 1/4 inch of water, the float lifts the magnetic switch, or the conductive trace bridges, and the sensor closes its circuit to the main board. The board immediately: (1) pauses the wash cycle, (2) energizes the drain pump continuously until cancelled, (3) displays LC on the panel, and (4) refuses to start any new cycle until the LC condition clears.

The leak sensor circuit is "fail-safe" — if the sensor itself shorts, the board sees the same signal as "water present" and posts LC. This is why a corroded sensor or a moisture-soaked sensor can throw LC even when the cabinet is dry. Newer Profile models (post-2020) include an additional "wet vs. dry" check that confirms moisture across multiple sensor points before triggering LC, reducing false alarms.

## Common causes (ranked by frequency)

In GE dishwasher service experience:

1. **Actual small leak from a hose connection** — about 25%. Most often the inlet valve fitting, the drain pump connection, or the sump-to-tub seal.
2. **False trigger from corroded sensor contacts** — about 22%. Older float-switch sensors corrode from years of humid base-pan environment.
3. **Door gasket leak (small)** — about 15%. Aged or damaged tub gasket lets a trickle of water out during high-pressure wash arm operation.
4. **Drain hose loop fault (high-loop missing, siphoning)** — about 12%. Improper install lets water siphon back during drain.
5. **Cracked tub or sump** — about 8%. Rare but happens on older units; needs replacement.
6. **Inlet valve dribbling when off** — about 6%. Valve doesn't fully close; small drips accumulate over hours.
7. **Detergent dispenser door leaking** — about 6%. Damaged dispenser gasket.
8. **Main PCB fault on the sensor input** — about 6%. Board reads LC even with no sensor signal.

**Pro nugget:** GE's leak sensor on Profile PDT and CDT models is part number **WD21X23467** (newer conductive-strip design) or **WD21X23030** (older float design). When you pull a leaked-out unit to dry it, you have to dry the base pan AND the sensor itself — wiping the visible water doesn't reset the sensor if moisture is still wicked into the float foam or the conductive trace. Pull the dishwasher out, towel-dry the base pan thoroughly, remove the sensor, and let it air-dry for 12-24 hours before reinstalling. Trying to test the unit immediately after drying often re-trips LC because residual moisture in the sensor itself completes the circuit.

## Step-by-step fix

Before you start: disconnect power at the breaker (GE dishwashers are typically hardwired), shut off water at the wall valve under the sink.

1. **Confirm the code.** Display reads "LC" or "lc". On some Profile models, an icon (water drop with exclamation) accompanies the text. The board will continue running the drain pump until you cut power.

2. **Pull the kick panel and inspect.** Remove the lower kick panel (typically 2 screws at the corners). Shine a flashlight on the base pan. Look for: standing water, recent puddle stains (chalky white from dried hard water), wet insulation, or rust spots. If you see active water, the leak is real. If the pan is dry, you likely have a sensor false-trigger.

3. **Identify the source if water is present.** Run a Rinse Only cycle and watch the base pan from below. Drip points usually become visible within the first 2-3 minutes — most commonly at: (a) the inlet valve fitting, (b) the connection between the sump and the drain pump, (c) the door gasket along the bottom edge during high-pressure wash, or (d) the detergent dispenser.

4. **Inspect the inlet valve.** Pull the supply line off the valve and check the fitting threads for cross-threading or missing washer. Reinstall with fresh tape or a new washer, snug to 25-30 in-lbs.

5. **Inspect the drain hose loop.** The drain hose must rise to at least the bottom of the sink basin (high-loop) before going down to the disposer or air gap. A missing high-loop allows siphoning that can pull water back into the dishwasher and over time leak past the tub fittings. Re-route or install an air gap if missing.

6. **Inspect the door gasket.** Open and close the door, watching the gasket. Check for: tears, missing pieces, deformation, or stiff sections that don't compress evenly. Replace if damaged.

7. **Replace the leak sensor.** Locate the sensor in the base pan (small black or white plastic unit with a 2-wire harness). With unit unplugged, disconnect the harness, remove the sensor (typically a single screw or snap-in), install the replacement, reconnect.

8. **Dry the base pan thoroughly.** Towel out any standing water. Use a hair dryer on low heat to evaporate moisture from corners. If the leak was significant, leave the kick panel off for 24 hours to air-dry.

9. **Reassemble and test.** Restore power and water. Run a Rinse Only cycle. Watch the LC code — should not return. Watch the base pan periodically over the first 2-3 days for any sign of recurrence.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Leak sensor (conductive strip, Profile) | GE WD21X23467 | $35-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Amazon](https://www.amazon.com) |
| Leak sensor (float type, older) | GE WD21X23030 | $25-50 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Amazon](https://www.amazon.com) |
| Water inlet valve | GE WD15X10003 | $55-95 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Amazon](https://www.amazon.com) |
| Drain pump assembly | GE WD26X25104 | $85-145 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc) |
| Tub gasket / door seal | GE WD08X10057 | $45-75 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Amazon](https://www.amazon.com) |
| Detergent dispenser assembly | GE WD12X10417 | $115-185 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc) |
| Sump-to-tub seal | GE WD08X10071 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Amazon](https://www.amazon.com) |
| Drain hose (with high-loop hardware) | GE WD24X10070 | $35-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=ge-dishwasher-error-code-lc) |

## When to call a professional

Call an appliance tech when:

- You can't identify the leak source after running multiple Rinse cycles. The leak might be at the sump-to-tub seal, which requires partial disassembly to inspect.
- You see rust on the base pan or signs of long-term water damage to the floor under the dishwasher. The pan or floor may need replacement.
- The leak is intermittent and only occurs during heavy-load cycles. Suggests the door gasket is compressing unevenly under high pressure — needs gasket replacement and possibly door alignment.
- The unit is under GE factory warranty (typically 1 year parts; some Profile and Cafe models carry 2-3 year racks and tub warranties).

## FAQs

**My base pan is dry but LC still shows. What's going on?**
False sensor trigger — the leak sensor is wet internally (residual moisture in the float foam or on the conductive trace), corroded, or has failed in the closed position. Replace the sensor.

**Can I just unplug the leak sensor to clear LC?**
The board interprets an open sensor circuit as a sensor failure (different code, typically displayed as a service fault). You can't bypass the leak sensor — it's a UL safety requirement.

**Why does the dishwasher keep pumping water out after LC?**
That's by design. The board energizes the drain pump continuously while LC is active to evacuate as much water as possible from the base pan. The pump runs until you cut power, even though no more water can be drained from a dry pan.

**Will a small drip from the inlet valve really set off LC?**
Yes. A persistent drip can accumulate 1/4 inch of water in the base pan over a few hours, especially with the dishwasher off. The leak sensor doesn't care whether the leak happened during a cycle or while idle.

**Difference between LC and OE on GE dishwashers?**
LC = leak detected (water in base pan). OE = drain timeout (couldn't drain wash water from sump). Different fault paths.

## Related guides

- [GE Refrigerator Error Code Er — Diagnostic Guide](/posts/ge-refrigerator-error-code-er)
- [GE Washer Error Code E1 — Front Load Fix](/posts/ge-washer-error-code-e1)
- [LG Dishwasher Error IE — Water Inlet Fix](/posts/lg-dishwasher-error-ie)
