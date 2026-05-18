---
title: "Bosch Dishwasher Error Codes — Complete Fix Guide"
description: "Bosch dishwasher error codes for 100, 300, 500, 800, and Benchmark series including E01-E32, H01-H02, and flashing-light fault patterns. Covers heater, drain, fill, and door faults."
pubDatetime: 2026-05-17T20:35:00Z
modDatetime: 2026-05-17T20:35:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - bosch
  - dishwasher
  - appliances
  - kitchen
---
<!-- VOICE-GUARD-OFF -->

## Bosch Dishwasher Error Code Reference

Bosch dishwashers across the 100, 300, 500, 800, and Benchmark series share the same E-prefix fault dictionary at the control-board level. Older models (pre-2015) flash error codes via the rinse-aid or clean light blink pattern. Newer models with displays show the code directly.

| Code | Fault | Most Likely Cause | First Action |
|------|-------|-------------------|--------------|
| E01 | Control / electronics fault | Loose connector or failed control board | Power-cycle 5 min, re-seat board harness |
| E02 | Heater relay (NTC) sensor fault | Failed water temperature sensor | Test NTC resistance at the sump |
| E03 | Heating element open | Heating element burned out | Test element continuity |
| E04 | Flow meter fault | Clogged flow meter or wiring | Clean flow meter, test wiring |
| E05 | Overfill / aquastop | Float switch raised or water in base | Pull dishwasher out, drain base pan |
| E06 | Door sensor / latch fault | Latch not engaging fully | Inspect latch and door switch |
| E07 | Fan / vent fault | Failed drying fan | Replace fan assembly |
| E09 | Heating circuit short | Heating relay welded closed | Replace heating relay |
| E11 | NTC temperature sensor out of range | Sensor failure or wiring break | Test sensor resistance |
| E12 | Heating temperature exceeded | NTC stuck low, heater overheating | Replace NTC, inspect heater |
| E14 | Flow meter (filling) | Stuck flow meter | Clean impeller |
| E15 | Water in the base / aquastop tripped | Leak in tub, hose, or door seal | Find and fix leak, drain base |
| E16 | Inlet valve stuck open | Failed inlet solenoid | Replace inlet valve |
| E17 | Inlet water pressure too high or flow meter | Verify supply <60 PSI, test flow meter | |
| E18 | Insufficient water supply | Low pressure, kinked hose, blocked screen | Verify supply, clean inlet screen |
| E19 | Optical sensor (cloudiness) | Failed turbidity sensor | Clean sensor lens, replace if needed |
| E21 | Drain pump blocked | Foreign object in drain pump | Clean drain pump impeller |
| E22 | Filter clogged | Sump filter blocked | Pull and clean sump filter |
| E23 | Drain pump fault | Drain pump electrically failed | Test pump leads, replace |
| E24 | Drain hose blocked | Kinked or blocked drain hose | Inspect hose, verify standpipe height |
| E25 | Drain pump cover dislodged | Cover seated incorrectly | Re-seat cover |
| E27 | Low voltage | Supply voltage below 90 VAC | Check breaker and supply |
| E28 | Aqua sensor (turbidity) | Sensor needs cleaning | Clean lens |
| E29 | Diverter motor fault | Failed wash-arm diverter | Replace diverter |
| E30 | Heating circuit (high) | Heater drawing too much current | Replace heater |
| E31 | Heating circuit (medium) | Heater intermittent | Test heater under load |
| E32 | Heating circuit (low) | Open neutral, partial heater failure | Verify supply, replace heater |
| H01 | Service / hint message | Salt low or rinse aid low | Refill consumables |
| H02 | Service hint | Check user manual for context | |

## The 5 Most Common Bosch Dishwasher Faults

### E15 — Water in the Base / Aquastop Tripped (most common)

E15 is the #1 callback. The aquastop is a float switch in the base pan; any water in the pan raises the float and trips the controller into permanent leak-protection mode (constant drain pump operation, can't start a cycle).

Fix workflow:
1. Pull the dishwasher out from under the counter. Disconnect water and drain (have a towel ready).
2. Tip the dishwasher 45° toward the front and drain any water from the base pan into a shallow tray. Towel-dry the pan completely.
3. Re-install with the front feet leveled. Run a short rinse cycle. If E15 doesn't return, the leak was a one-time event (overfill, briefly clogged drain, etc.).
4. If E15 returns within one cycle, you have an active leak. Common sources: door seal (perished), pump hose clamp (loose), heater gasket (corroded), or tub crack (rare). Find and fix.

The float switch itself rarely fails — about 95% of E15s are real water, not a sensor fault.

### E22 — Filter Clogged

The sump filter at the bottom of the tub needs cleaning. Bosch's design has 2-3 nested mesh filters that catch food debris.

1. Pull the lower rack out.
2. Twist the cylindrical filter assembly counter-clockwise to unlock. Lift out.
3. Disassemble the nested mesh elements. Rinse under hot water. A toothbrush helps with stuck food bits.
4. Re-install in the reverse order. Twist clockwise to lock.

If E22 returns immediately after cleaning, the wash-pump impeller is blocked (different fix: pull the impeller cover at the sump base, clear debris).

### E24 — Drain Hose Blocked

The drain hose from the dishwasher to the under-sink standpipe is blocked. Common spots:

- High loop missing (drain hose must rise to ~32 in then drop) — water back-siphons and clogs over time.
- Air gap (at the sink top, if installed) is clogged with food debris — unscrew the cap and clean.
- Standpipe inside the cabinet is reduced/restricted by buildup.

Pull the hose at both ends and run water through it. If flow is reduced, replace.

### E01 — Control / Electronics Fault

Generic "the control board threw an exception" code. Workflow:

1. Power off at the breaker for 5 minutes (not just unplug — Bosch boards retain state for 60s).
2. Power back on. If E01 doesn't return, it was a one-time event.
3. If E01 returns, open the door panel (six Torx T20 screws on the top) and inspect the ribbon cable + power-board connectors. Re-seat both.
4. If E01 persists after re-seat, the main power board has failed (~$220-$380 part).

### E02 — Heater NTC Sensor Fault

The water temperature sensor at the sump has gone open or shorted. It's a thermistor — same diagnosis flow as the LG fridge / Mitsubishi mini-split sensor swap: pull the connector, measure resistance, expect ~10K ohms at 25°C, replace if outside range.

Replacement NTC sensors are ~$15-$25 and a 15-minute job. Don't replace the whole heater assembly first.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Drain pump (Bosch 00642239 / 00611332-style) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%2200642239%22+Bosch+drain+pump&tag=errorcodefixes-20) \| RepairClinic | $55-$130 |
| Inlet water valve (aquastop solenoid) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%22Bosch+aquastop+valve%22&tag=errorcodefixes-20) | $90-$180 |
| Door latch / interlock | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%22Bosch+dishwasher+door+latch%22&tag=errorcodefixes-20) | $30-$70 |
| NTC temperature sensor (heater) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%22Bosch+dishwasher+NTC+sensor%22&tag=errorcodefixes-20) | $15-$25 |
| Heating element (Bosch flow-through) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%22Bosch+dishwasher+heater%22&tag=errorcodefixes-20) | $80-$170 |
| Sump filter assembly | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%22Bosch+dishwasher+filter+assembly%22&tag=errorcodefixes-20) | $20-$45 |
| Door seal / gasket | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-dishwasher-error-codes&k=%22Bosch+dishwasher+door+seal%22&tag=errorcodefixes-20) | $40-$95 |
| Main control board (power module) | RepairClinic, Bosch parts | $220-$380 |

## Technician Tips

- **Bosch dishwashers have a "tilt sensor" anti-shipping feature.** Units shipped with the lock screw still engaged will throw spurious errors. Look for a small Phillips screw under the front kickplate marked with a sticker — remove it on first install.
- The aquastop solenoid is in the inlet hose connector, not at the dishwasher. Replacing the dishwasher's inlet hose without ordering the correct aquastop assembly = E15 on first cycle.
- For chronic E22 / E21 in households with hard water: descale the dishwasher monthly with citric acid (1 cup citric acid in an empty dishwasher, hot cycle). Buildup on the wash impeller throws drain-cycle errors first.
- The "Service" menu (hold Power + Regenerate together for 5 seconds on most newer models) shows the last 10 fault codes with timestamps. Useful for "what happened last week" diagnostics.

## Common Code Combinations

- **E15 → E24**: leak triggered aquastop, but the drain pump can't clear because the hose is also blocked. Fix drain first.
- **E22 → E21**: clogged filter caused the wash pump to overload and trip. Clean filter, reset, retest.
- **E02 → E11 → E12**: sensor wiring intermittent, board reads wildly different temps. Replace sensor + wiring harness.

If errors return within 48 hours of clearing them, the underlying fault is active — not transient. Schedule the next-step diagnostic instead of resetting again.

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG refrigerator error codes (complete guide)](/posts/lg-refrigerator-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Whirlpool washer error codes (F-codes + Cabrio)](/posts/whirlpool-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Maytag washer error codes (Bravos + Centennial)](/posts/maytag-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Samsung refrigerator error codes](/posts/samsung-refrigerator-error-codes/)

