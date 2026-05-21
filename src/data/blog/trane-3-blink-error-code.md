---
title: "Trane 3-Blink Error Code — Pressure Switch Fault Fix"
description: "A 3-blink fault on a Trane furnace LED means the integrated furnace control did not see the pressure switch close after the inducer started, or..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: trane-3-blink-error-code
featured: false
draft: false
tags:
  - trane
  - hvac
  - error-codes
  - pressure-switch-fault
---
## Quick answer

A 3-blink fault on a Trane furnace LED means the integrated furnace control did not see the pressure switch close after the inducer started, or alternatively saw it stuck closed at startup. On most Trane and American Standard residential furnaces (XV80, XV95, XR95, S9V2, XC95M and similar — they share boards), it's most often a plugged condensate trap on 90% AFUE units, a tired pressure switch (Trane uses Tridelta and Sensata switches that age in characteristic ways), or a tubing problem at the inducer barb. Diagnose with a digital manometer to read draft and isolate root cause in 15 minutes.

## What 3-blink means on a Trane

Trane (and its sister brand American Standard, which uses the same boards under different paint) uses the SEN, LMT, and CNT prefix part-numbering family on their furnace control boards. The status LED behind the lower blower door blinks the code: three quick blinks / pause / three quick blinks = code 3. The label inside the door identifies it as "Pressure Switch Fault" or "Pressure Switch Stuck Open" depending on model year and board revision.

Trane's pressure switch logic is similar to other manufacturers but with one specific nuance: Trane boards check the switch state BEFORE energizing the inducer (expecting open) and AFTER inducer has run for the verification window (expecting closed). A failure on either check produces the 3-blink code. The board doesn't differentiate between "stuck open" and "stuck closed" with separate codes on most models — both come up as 3-blink.

The pressure switch on a 90% AFUE Trane (XV95, XC95M, S9V2 series) is typically a dual switch — one switch monitoring inducer draft, a second monitoring the secondary heat exchanger or condensate drain. Either failing trips 3-blink. On 80% AFUE Trane (XR80, XV80) you get a single switch.

Trane's modern variable-speed equipment (XV95, XC95M) also communicates pressure switch state through the integrated control's diagnostic data to the ComfortLink II thermostat. If you have a CL2 thermostat, you can read more diagnostic detail there than the LED alone provides.

## Common causes (ranked by frequency)

1. **Plugged condensate trap (90% AFUE only)** — about 35%. The trap collects biofilm and partial blockage chokes secondary heat exchanger draft.
2. **Pressure switch fatigue** — about 25%. Trane's switches age with the diaphragm losing flexibility; trip pressure rises over time until normal draft can't satisfy.
3. **Cracked or kinked switch tubing** — about 15%. The silicone hose between inducer port and switch develops cracks or melts against the inducer body.
4. **Inducer wheel buildup** — about 10%. Dust, web, rust scale on the squirrel cage reduces draft.
5. **Vent system restriction** — about 7%. Bird nest, ice, snow drift at termination; or partial blockage in horizontal vent run.
6. **Failed inducer motor** — about 5%. Bearings dragging, motor runs slow, draft inadequate.
7. **Loose or chafed switch wiring** — about 3%.

**Pro nugget:** Trane S9V2 series 90% AFUE units installed in attics or unconditioned spaces have a specific cold-weather failure pattern where the condensate trap freezes during a long off-period. On the next heat call, the inducer can't develop draft past the frozen trap, 3-blink fires, the homeowner clears the code, and as soon as the furnace runs long enough to thaw the trap (10-20 minutes of fault-cleared retries) it works fine the rest of the day. The fix is not the trap or the switch — it's heat tape on the condensate line and trap, or relocating the trap to a more conditioned space. I worked this on a Colorado mountain home with three Trane attic installs — heat tape on the traps in the fall, no 3-blink calls for two winters.

## Step-by-step fix

Before you start: turn off power at the furnace switch and shut off gas. Let the furnace cool for at least 5 minutes if it's been running.

1. **Confirm the code at the LED.** Three blinks / pause / three blinks. Photograph the wiring diagram on the inside of the lower blower door.

2. **Test the pressure switch state at rest.** Power off, pull the two wires from the switch, ohm across the terminals. At rest (no inducer running) the switch should read open (OL). If it reads closed, the switch is stuck closed — replace.

3. **Inspect the switch tubing.** Pull the silicone hose from the inducer barb and from the switch. Look for kinks, melt marks (hose touching the inducer body), water droplets inside, or split ends. Blow through — should be wide open. White scale inside = condensate wicking back, replace hose and clean trap.

4. **Service the condensate trap (90% AFUE only).** Pop the U-shaped trap off (typically a friction fit with O-ring seal — be careful not to crack the plastic). Dump into a bucket. Flush with 50/50 white vinegar / water. Scrub gentle with a soft brush — do NOT use a wire or stiff brush, you'll enlarge the orifices and alter the trap's seal. Re-prime with fresh water before reinstalling.

5. **Measure draft with a manometer.** Tee a digital manometer into the switch hose at the inducer port. Power on, call for heat, watch reading during inducer startup. Trane 90% AFUE inducers should pull approximately -0.50" to -0.95" WC during steady draft (exact target depends on model — check installation manual). Below -0.40" WC = inadequate draft.

6. **Inspect the inducer wheel.** Power off. Disconnect inducer (typically four screws to remove from housing). Look at squirrel cage blades — anything more than a thin dust film impacts draft. Wipe with damp rag or vacuum carefully. Reinstall with original orientation.

7. **Walk the vent termination outside.** PVC for 90% AFUE, metal Type B or single-wall for 80% AFUE. Look for nests, ice, snow drift, vegetation. Clear any obstruction. On concentric vent terminations, check both the inner exhaust and outer intake.

8. **Replace the pressure switch if needed.** Trane uses specific switch part numbers per model — order by exact OEM number stamped on the switch body. Common Trane switches include the SEN02021 family and CNT05226. Verify on the bench that the new switch reads open at rest before installing.

9. **Reassemble and verify with a full cycle.** Restore power and gas. Cold start: thermostat call → inducer → pressure switch close (audible click at proper draft) → HSI glow → gas valve → flame → blower delay → blower on.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Pressure switch (single, 80% AFUE) | Trane SEN02021 | $45-75 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Pressure switch (dual, 90% AFUE) | Trane CNT05226 | $75-115 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Pressure switch tubing (silicone) | Generic 1/4" silicone | $5-10 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |
| Inducer motor assembly | Trane MOT12376 (varies) | $235-380 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Condensate trap | Trane TRP03325 | $35-65 | [Amazon](https://www.amazon.com), [RepairClinic](https://www.repairclinic.com) |
| Integrated furnace control | Trane CNT05165 (varies) | $235-380 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Digital manometer | Testo 510i / Fieldpiece SDMN6 | $130-275 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com) |

## When to call a professional

Call a licensed HVAC pro if:

- You replaced the pressure switch and 3-blink returns. That's either the wrong switch part, a remaining tubing or trap issue, or a control board sensing problem.
- The furnace is a Trane XV95M, XC95M, or any other ComfortLink II communicating system. CL2 systems have additional diagnostic data accessible only through the thermostat or service software — troubleshooting from the LED alone misses information.
- Vent system needs evaluation — the unit has Type B vent with multiple elbows, a long horizontal run, or shares venting with a water heater (common-vent applications need professional venting code review).
- You smell flue gas anywhere in the home or near the furnace closet. Leave the area, ventilate, call the gas utility and HVAC pro.
- The furnace is under Trane factory warranty. Warranty terms typically void if non-licensed personnel replace control or safety components.

## FAQs

**Why does my Trane work fine in summer (off-season) and throw 3-blink the first cool day in fall?**
Several reasons cluster here: the condensate trap dried out and any biofilm hardened during the off-season, the pressure switch sat with its diaphragm in one position long enough to develop a stick, and the vent termination may have collected debris over warm months. First-of-season 3-blink is so common that some HVAC service contracts include a "fall startup" visit specifically to clean the trap and verify switch operation before homeowners turn on heat.

**Can I jumper the pressure switch to test if the rest of the system works?**
Strongly discouraged. The pressure switch is a primary safety preventing CO buildup if vent is blocked. Even a 60-second test with the switch jumpered can allow combustion gas accumulation if there's a real vent problem. Don't do it.

**My switch ohms closed at rest but the furnace works fine sometimes. Replace it?**
Yes. A switch that's already showing intermittent stuck-closed behavior is on its way to permanent failure. Replace it before it fails completely on the coldest night of the year.

**What's the difference between Trane 3-blink and 4-blink?**
3-blink is pressure switch. 4-blink on most Trane boards is "limit circuit fault" (high-temp limit or rollout opened). Different problem, different diagnostic path. Always confirm the count.

**Will a smart thermostat upgrade cause 3-blink?**
Indirectly possible. If the new thermostat's wiring is wrong (especially the C wire) and creates intermittent 24V drops or short-cycles the inducer, you can see pressure switch fault codes that aren't really switch problems. Check thermostat wiring on the integrated control if 3-blink started right after a t-stat install.

## Related guides

- [Trane 2-Blink Error Code — Pressure Switch Stuck Closed Fix](/posts/trane-2-blink-error-code)
- [Trane 4-Blink Error Code — Limit Circuit Trip Fix](/posts/trane-4-blink-error-code)
- [Goodman 3-Flash Error Code — Pressure Switch Open Fix](/posts/goodman-3-flash-error-code)
