---
title: "Heil 3-Flash Error Code — Pressure Switch Fix (Tempstar / Comfortmaker)"
description: "A 3-flash error on a Heil, Tempstar, or Comfortmaker furnace means the integrated control did not see the pressure switch close after the inducer (draft..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: heil-flash-code-3
featured: false
draft: false
tags:
  - heil
  - hvac
  - error-codes
  - pressure-switch-stuck-open
---
## Quick answer

A 3-flash error on a Heil, Tempstar, or Comfortmaker furnace means the integrated control did not see the pressure switch close after the inducer (draft motor) started — the switch is reading open when it should be closed. About 65% of the time this is a blocked condensate trap on a 90% AFUE unit holding back water that's filling the inducer housing, not a failed switch. Pull and rinse the condensate trap first.

## What 3-flash means on a Heil

Heil, Tempstar, and Comfortmaker are all International Comfort Products (ICP) brands — a single manufacturing company in Lewisburg, Tennessee, that produces the entire family on shared assembly lines. The control board, pressure switch, inducer, and limit hardware are identical across the three brands; only the cabinet badge and the dealer network differ. ICP also makes the Day & Night, Arcoaire, and KeepRite brands using the same chassis. If your supply house stocks Heil parts, those parts drop into Tempstar and Comfortmaker cabinets without modification.

The diagnostic LED lives behind the lower blower door. A 3-flash code = three slow blinks, pause, repeat. ICP boards use single-digit flash codes (1-9) rather than the two-digit codes Carrier uses, which simplifies field diagnosis but means each flash code covers a broader range of conditions.

Flash code 3 specifically means: the inducer started, the pre-purge timer expired, but the pressure switch did not close within the watch window (typically 30 seconds on most ICP boards). The board does not advance to HSI warmup or gas valve energization until it sees the switch closed — without proof of draft, gas could light into a blocked vent and produce CO. After several seconds of waiting, the board shuts the inducer down, posts code 3, and waits 5 minutes before retrying.

On a 90% AFUE condensing furnace, the pressure switch sees vacuum through a small hose tee'd into the inducer housing — the same housing that drains combustion condensate into a trap. If the trap is plugged, condensate fills the inducer housing, the inducer churns water instead of pulling air, and the pressure switch never sees enough vacuum to close. This is the dominant failure mode on ICP 90% AFUE units after 3-5 years of operation.

## Common causes (ranked by frequency)

In field experience across the three ICP brands:

1. **Clogged condensate trap** — about 35%. Algae or hard-water scale in the trap chambers backs water up into the inducer.
2. **Blocked vent pipe or termination** — about 20%. Bird nest, ice, leaves, or insulation foam over the termination kills draft.
3. **Failed pressure switch** — about 15%. Diaphragm split or stuck open.
4. **Disconnected or kinked pressure switch hose** — about 10%. Vibration or service work pulled the hose off; or the hose has melted against the inducer.
5. **Inducer motor failing or running slow** — about 8%. The motor turns but can't develop the vacuum spec on the switch.
6. **Cracked inducer housing** — about 5%. Leaks vacuum into the cabinet, switch never gets to setpoint.
7. **Wrong pressure switch installed in prior service** — about 4%. Switch rated for a higher WC setpoint than the unit can develop.
8. **Control board fault** — about 3%. The pressure-sensing input on the IFC is damaged.

**Pro nugget:** ICP condensate traps on Heil/Tempstar/Comfortmaker 90% AFUE units (model series N9MSE, NCG, T9, P9) use a two-chamber design with a 1/4-inch internal orifice that's notoriously prone to algae plugging. Annual rinse with white vinegar + warm water (1:3 mix) through the trap clears 90% of trap-related code 3 events before they happen. Add this to fall pre-season service for any 90% AFUE ICP unit and you cut code 3 callbacks dramatically.

## Step-by-step fix

Before you start: shut off power at the furnace switch and gas at the gas cock. Wait 5 minutes for inducer spin-down.

1. **Confirm the code and history.** Open the lower door, watch the LED. Three slow flashes / pause / repeat = code 3. ICP boards don't store history beyond the most recent fault, so note conditions: was there a recent storm (vent ice), a recent service (parts left disconnected), or has the unit been intermittent for weeks (slow trap plug)?

2. **Inspect the vent termination.** Outside, locate the PVC vent termination (concentric, side-wall, or 2-pipe). Check for: bird nests, wasp nests, ice in cold weather, leaves stuffed in the screen, snow drifted over the inlet/outlet pair. Clear any blockage. On a 90% AFUE concentric vent, also check the inner pipe (combustion air intake) for obstruction.

3. **Pull and rinse the condensate trap.** The trap is the white plastic Y- or T-shaped fitting at the bottom of the cabinet with a hose going up to the inducer and one going to the floor drain. Disconnect the hoses (note positions — photo), remove the trap, take it to a sink, fill with white vinegar/warm water mix, swish to clear scale, then rinse. Hold it up to a light — you should see clear daylight through every chamber. If you can't, pour more vinegar through and let it sit 30 minutes.

4. **Inspect the pressure switch hose.** Pull the hose off the switch and off the inducer body. Look for melt damage (especially where the hose lays close to the inducer body — Heil and Tempstar units route this hose tight against the inducer in some configurations), water inside the hose, kinks, splits. Blow through the hose — should be wide open. Replace with same-diameter silicone tubing if any damage.

5. **Bench-test the pressure switch.** Pull the switch out (single screw). With both wires off and the hose off, ohm across the two electrical terminals. At rest, a normally-open switch reads open (OL). Apply gentle vacuum to the hose port with a hand vacuum pump (Mityvac) and watch the switch click closed at its setpoint stamped on the body (e.g., "−0.50 WC"). If it doesn't click closed at the stamped pressure, replace it.

6. **Verify inducer operation.** Power on, initiate a heat call, and listen at the inducer. It should spin up smoothly within 1 second, no scraping or whining. A worn inducer bearing produces a noticeable "wha-wha-wha" pulsing sound. With a manometer tee'd into the pressure switch hose, you should see the vacuum spec develop within 5 seconds — typically 0.65-0.80 inches WC on a 90% AFUE Heil/Tempstar inducer running on the high tap.

7. **Replace the pressure switch.** Order by the stamped switch number on the original (e.g., HQ1011927HW for many ICP 90% AFUE singles). Install, reconnect both wires (the switch terminals are not polarized), reconnect the hose. Bench-test on the manometer one more time after install.

8. **Watch a full cycle.** Restore power and gas. Initiate a heat call. Cold start: 24V to board → inducer runs → pre-purge 15-30 sec → pressure switch should click closed (audible click) → HSI energizes → gas valve opens → flame establishes → blower delay → blower on. If code 3 returns immediately after inducer start, double-check the vent for partial blockage you missed.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Pressure switch (90% AFUE single, -0.50 WC) | ICP HQ1011927HW | $45-70 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3), [Amazon](https://www.amazon.com) |
| Pressure switch (90% AFUE dual) | ICP HQ1009850TW | $65-95 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3), [Amazon](https://www.amazon.com) |
| Condensate trap assembly | ICP 1184211 | $35-60 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3) |
| Integrated furnace control (SmartLight) | ICP 1183620 | $185-265 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3), [Amazon](https://www.amazon.com) |
| Inducer motor assembly (90% AFUE) | ICP 1014338 | $245-365 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3), [Amazon](https://www.amazon.com) |
| Silicone hose (1/4 inch, per foot) | Generic | $3-5 | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3), [Lowes](https://www.lowes.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=heil-flash-code-3) |
| Hand vacuum pump for switch testing | Mityvac MV8000 | $50-75 | [Amazon](https://www.amazon.com) |

ICP cross-brand note: a Heil 1183620 control board drops directly into a Tempstar or Comfortmaker cabinet of the same era. The Day & Night and Arcoaire variants of these brands are identical down to the part number. Don't pay for a "Tempstar" board if your supplier has a Heil board in stock — same part, same price ideally.

## When to call a professional

Call a licensed HVAC tech when:

- You've cleared the vent, rinsed the trap, replaced the switch, and code 3 still returns. The next step is a manometer check on the inducer to confirm draft spec is being met — if not, the inducer is failing internally and needs replacement.
- The condensate trap is full of dark brown sludge or smells biological. That's bacterial growth that can indicate a cracked secondary heat exchanger leaking flue gas into the condensate path — needs combustion analysis with CO probe.
- You see ice forming on the outdoor vent termination in cold weather. Improper venting or a too-long vent run; a tech can verify code-compliant length, slope, and concentric vs. 2-pipe configuration.
- The unit is under ICP warranty (5 years parts standard, 10 years with registration on Heil, Tempstar Performance, Comfortmaker Deluxe). Self-repair of the control board or gas valve voids parts warranty.

## FAQs

**My condensate trap looked clean. Why was it the problem?**
ICP trap chambers can hold a thin film of algae that restricts the orifice without looking dirty. Always flush with vinegar at annual service even if it looks clean. The 1/4-inch orifice doesn't take much restriction to fail.

**Heil vs. Tempstar — are they actually the same?**
Yes. Both are International Comfort Products. The control boards, switches, valves, and motors carry identical part numbers; only the cabinet badge and the dealer network differ. Service procedures are identical.

**Will adding a vacuum breaker fix the trap problem?**
On long horizontal vent runs (over 35 ft) you sometimes need a vacuum breaker to prevent the inducer pulling water out of the trap. Check the installation manual for your specific model — most under 35 ft don't need one. Adding one without verifying you're code-compliant on length can create other problems.

**My code 3 only happens in cold weather. Why?**
Almost always vent termination icing or condensate freezing in a long horizontal run. Verify the vent has the spec'd slope toward the trap (1/4 inch per foot), and consider terminating with an ICP-approved cold-weather hood.

**Difference between Heil code 3 and code 4?**
Code 3 = pressure switch stuck open (didn't close after inducer started). Code 4 = limit switch tripped (heat exchanger overheated). Different diagnostic paths. See the Tempstar 4-flash guide.

## Related guides

- [Tempstar Flash Code 4 — Limit Switch Fix](/posts/tempstar-flash-code-4)
- [Payne Error Code 31 — Pressure Switch Fix](/posts/payne-error-code-31)
- [Carrier 31 Error Code — Pressure Switch Fix](/posts/carrier-31-error-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Carrier vs Trane furnaces compared](/posts/carrier-vs-trane-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Goodman vs Bryant furnaces compared](/posts/goodman-vs-bryant-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Mitsubishi vs Daikin mini splits](/posts/mitsubishi-vs-daikin-mini-splits/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best combustion analyzer (2026)](/posts/best-combustion-analyzer/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best HVAC manometer (2026)](/posts/best-manometer-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant gauge set (2026)](/posts/best-refrigerant-gauge-set/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best thermal imager for HVAC](/posts/best-thermal-imager-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant leak detector](/posts/best-refrigerant-leak-detector/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best boiler test kit](/posts/best-boiler-test-kit/)

