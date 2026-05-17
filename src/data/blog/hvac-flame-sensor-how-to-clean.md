---
title: "How to Clean an HVAC Flame Sensor - Step-by-Step Guide"
description: "Step-by-step guide to cleaning a gas furnace flame sensor. Includes how to test with a microamp meter, cleaning with emery cloth, and when to replace the rod entirely."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

A dirty flame sensor is the single most common reason a gas furnace ignites and then shuts off after 5–10 seconds. The repair takes about 15 minutes and costs nothing if you have emery cloth on hand. This guide walks you through the entire process: understanding how the flame sensor works, testing it with a microamp meter, cleaning it correctly, and knowing when cleaning won't save it.

## What Does a Flame Sensor Do?

The flame sensor (also called a flame rod or rectifier rod) is a safety component that proves a flame is actually present after the gas valve opens. Here's the sequence:

1. The furnace control board calls for heat.
2. The draft inducer motor starts and the pressure switch proves airflow.
3. The igniter heats up (hot surface igniter) or sparks (spark igniter).
4. The gas valve opens.
5. The burners light.
6. The flame sensor detects the flame by measuring a tiny electrical current (4–10 microamps) that flows through the flame between the sensor rod and ground (the burner).
7. If the board doesn't see this current within 7–10 seconds, it assumes no flame is present and shuts off the gas valve as a safety measure.

When the sensor is coated with oxidation, it can't pass enough current to satisfy the board. The board interprets this as "no flame" and shuts down — even though there's a perfectly good flame burning right in front of the rod.

## What Does a Flame Sensor Fault Look Like?

- **Symptom:** Furnace starts, burners ignite, then the burners shut off after 5–10 seconds. The system tries again 2–3 times and then goes into lockout.
- **LED flash code:** Most furnaces flash a specific code for flame sensor fault. Common codes: Carrier/Bryant 34, Lennox 232, Goodman/Amana 5 flashes, Trane/American Standard 5 flashes, Rheem/Ruud 5 flashes.
- **Microamp reading:** Less than 0.5 µA with a dirty sensor vs. 2–10 µA with a clean sensor.

## How to Fix It

**What you need:**
- Emery cloth (fine grit, 400–600 grit) or steel wool (0000 grade)
- A screwdriver (usually 1/4-inch hex or Phillips)
- Optionally: a clamp meter with microamp (µA) DC range for testing

**Step 1: Turn Off Power and Gas**

- Switch the furnace power switch off (usually a wall switch near the furnace or disconnect box above it).
- Flip the circuit breaker for the furnace to the OFF position.
- Turn the gas valve on the gas supply line to OFF.

Never work inside a furnace with power on. You'll be near the gas valve, igniter wires, and 120V components.

**Step 2: Allow the Furnace to Cool**

If the furnace ran recently, the igniter and sensor area will be hot. Wait at least 10 minutes before reaching inside the burner compartment.

**Step 3: Open the Furnace Panels**

Remove the upper furnace panel (some models require removing both the upper and lower doors). Set the panels aside.

**Step 4: Locate the Flame Sensor**

The flame sensor is a metal rod mounted in the burner area on a porcelain insulator. It looks like a bent metal rod (typically 2–4 inches long) with a single wire connector attached to it. It sits near the burner flames — usually in the path of the first or second burner flame.

Don't confuse it with the hot surface igniter — the igniter is a larger fragile element that glows orange-red. The flame sensor rod is thinner and shinier (when clean) or matte/grey (when oxidized).

**Step 5: Disconnect the Wire**

Pull the wire connector off the flame sensor. It's a single spade connector — just pull straight off. No tools needed.

**Step 6: Remove the Sensor**

One or two screws hold the flame sensor mounting bracket to the burner assembly. Remove these screws (typically 1/4-inch hex head) and carefully pull the sensor out. Set the screws somewhere you won't lose them.

**Step 7: Inspect the Rod**

Hold the sensor so you can see the metal rod. A clean sensor rod is shiny metal — typically stainless steel. A dirty sensor rod looks:
- Dull grey or white (mild oxidation)
- Flaky or powdery (heavy oxidation)
- Coated with a visible film or crust

This oxidation layer acts as an insulator, preventing the microamp current from flowing through the rod to ground. Cleaning removes this layer.

**Step 8: Clean the Rod**

Fold a small piece of emery cloth (400–600 grit) and lightly rub the metal rod — not the porcelain insulator, only the metal part. Use light pressure and short strokes. The goal is to remove the oxidation layer without gouging the rod.

You should see the metal brighten after 10–20 strokes. Don't over-sand — you're removing microns of material, not reshaping the rod.

**Alternatives if you don't have emery cloth:**
- 0000 (four-zero) steel wool works well.
- A dollar bill (yes, really) — the fine cotton-linen fibers lightly abrade the oxidation without scratching.
- Do NOT use sandpaper coarser than 400 grit — you risk removing too much material and shortening the rod's life.
- Do NOT use chemical cleaners, WD-40, or any spray on the flame sensor. Residue interferes with the microamp measurement.

**Step 9: Wipe Clean**

After cleaning, wipe the rod with a clean dry cloth to remove any residue. Don't touch the cleaned rod with bare fingers — oils from your skin can leave a film. Hold the sensor by the porcelain insulator or mounting bracket only.

**Step 10: Reinstall the Sensor**

Slide the sensor back into position and hand-tighten the mounting screws. Don't overtighten — the porcelain insulator can crack. Reconnect the wire spade connector.

**Step 11: Test the Furnace**

Turn the gas back on, restore power, and set the thermostat to call for heat. Watch the ignition sequence:
- Draft inducer starts.
- Igniter glows / sparks.
- Burners light.
- **The burners should stay on.** If they stay lit for more than 30 seconds and continue through a full heat cycle, the cleaning worked.

**Optional: Test with a Microamp Meter**

For a definitive test, clip a clamp meter (set to DC microamps) inline on the flame sensor wire while the burners are lit:
- **Good reading:** 2–10 µA
- **Marginal reading:** 0.5–2 µA (may pass today, fail when the sensor warms up more)
- **Bad reading:** Below 0.5 µA (cleaning didn't work; replace the sensor)

Most clamp meters don't have a µA range — you need a meter with a separate µA input jack (like a Fluke 87V or similar). An inline ammeter approach works too: break the flame sensor wire circuit and place the meter in series.

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| Universal Flame Sensor Rod (Supco or equivalent) | Replace corroded or broken flame sensor | [View on Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) |
| Emery Cloth Assortment (400-600 grit) | Clean oxidized flame sensor rod | [View on Amazon](https://www.amazon.com/s?i=industrial&k=emery+cloth+assortment+400+600+grit&tag=errorcodefixes-20) |
| Fluke 87V Digital Multimeter (µA capable) | Test flame sensor microamp output | [View on Amazon](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20) |
| 1/4-inch Hex Nut Driver | Remove flame sensor mounting screws | [View on Amazon](https://www.amazon.com/s?i=industrial&k=1+4+inch+hex+nut+driver+HVAC&tag=errorcodefixes-20) |

## When to Call a Pro

- **Cleaning doesn't fix the short-cycling:** If the burners still shut off after 10 seconds after a thorough cleaning, and your microamp reading is still below 1 µA after sensor replacement, the control board's flame sensing circuit may have failed. Board diagnosis requires technical knowledge.
- **The burners won't light at all:** If the igniter isn't glowing (for hot surface igniter models) or the gas valve isn't opening, you have a different fault — not a flame sensor issue. Read your furnace's flash code.
- **You smell gas:** If you smell gas at any point during this procedure, stop immediately. Leave the house, don't touch any switches, and call the gas company from outside.
- **The furnace is making unusual noises:** Banging, scraping, or grinding noises indicate a mechanical issue unrelated to the flame sensor.

## FAQ

**Q: How often should I clean the flame sensor?**

A: Cleaning every 1–2 years as part of annual furnace maintenance is a good practice. Many HVAC technicians clean it during a fall tune-up as a matter of course. If you live in an area with hard water and high humidity, or if your furnace runs a lot, clean it annually.

**Q: Can I just replace the flame sensor instead of cleaning it?**

A: Yes, and it's often the right call if the sensor is more than 5 years old or if the rod has visible pitting or cracks in the porcelain. A new universal flame sensor costs $10–20 and takes the same time to install as cleaning the old one.

**Q: My furnace has a lockout code. Do I need to reset it after cleaning the sensor?**

A: Yes. After cleaning the sensor and replacing the panels, the furnace may still be in lockout. To reset: most furnaces reset when you turn the power off for 30 seconds and back on. Some models require you to hold the reset button on the control board. Consult your furnace manual or check the wiring diagram inside the furnace panel door for the reset procedure.

**Q: I cleaned the sensor and it worked for a week, then failed again. What's happening?**

A: This typically means the oxidation is reforming quickly, which happens when the sensor is at the end of its service life. The rod may have micro-pitting that holds oxidation better than a smooth new rod. Replace the sensor — at $15–20, it's not worth repeated cleaning cycles.

**Q: What causes a flame sensor to get dirty so fast?**

A: The most common causes are: a furnace running in a dusty environment (near a workshop or unfinished space), a cracked heat exchanger allowing combustion products to contaminate the burner area, or a furnace that's been sitting idle for years. Inspect your furnace filter — if it's clogged, dust bypasses the filter and coats internal components including the flame sensor.
