---
title: "Whirlpool Washer Error Codes — Complete Fix Guide (F-Codes + Cabrio)"
description: "Whirlpool washer error codes for top-load, front-load, Duet, Cabrio, and HE models. Covers F1-F35, F20, F21, F23, F26, F8E1, F8E2, F9E1, LF, LD, Sd, Sud codes and door/drain/balance faults."
pubDatetime: 2026-05-17T20:40:00Z
modDatetime: 2026-05-17T20:40:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - whirlpool
  - washer
  - laundry
  - appliances
---
<!-- VOICE-GUARD-OFF -->

## Whirlpool Washer Error Code Reference

Whirlpool washers use two different code families depending on era and platform:

- **F-codes** (F1, F20, F35 etc.) on older Duet and top-load models
- **F#E#** codes (F8E1, F9E1 etc.) on newer Cabrio, HE, and 2018+ direct-drive models
- **Letter codes** (Sd, Sud, LF, LD) appear on display panels regardless of platform

The dictionary below covers ~95% of what shows up on the panel display in residential service.

| Code | Fault | Most Likely Cause | First Action |
|------|-------|-------------------|--------------|
| F1 / F1E1 | Main control board fault | Failed CCU (central control unit) | Power-cycle, then replace CCU |
| F1E2 | Motor control unit (MCU) fault | Failed MCU board | Replace MCU |
| F2E1 | Stuck keypad button | Liquid intrusion or worn button | Clean / replace user interface |
| F3E1 | Inlet water temperature sensor | Failed thermistor | Test sensor resistance |
| F5E1 | Door switch fault | Switch open or failed | Test door switch continuity |
| F5E2 | Door lock fault | Lock motor failed | Replace lock assembly |
| F5E3 | Door cannot unlock | Lock motor stuck closed | Cycle power, replace lock |
| F6E1 | Communication: CCU to UI | Wiring or one board failed | Re-seat ribbon, swap UI first |
| F6E2 | Communication: CCU to MCU | Wiring or MCU failure | Inspect MCU cable |
| F7E1 | Motor drive fault | MCU or motor failure | Test motor windings |
| F8E1 | Long fill / inlet fault | Water supply, inlet valve, or pressure sensor | Verify supply, clean inlet screen |
| F8E2 | Dispenser fault | Stuck dispenser actuator | Inspect dispenser drawer |
| F8E3 | Overflow | Pressure sensor or inlet valve stuck | Shut supply, drain tub |
| F9E1 | Long drain / drain fault | Pump blocked, drain hose kinked | Clean pump filter |
| F9E2 | Pump fault | Drain pump electrically failed | Replace pump |
| F20 | Inlet water (older Duet equivalent of F8E1) | Same as F8E1 | Verify supply |
| F21 | Long drain (older Duet equivalent of F9E1) | Same as F9E1 | Clean pump |
| F22 | Door lock | Door not locking | Replace lock |
| F23 | Heater (front-load with heater models) | Heater open or relay failed | Test heater continuity |
| F25 | Drive motor tachometer | MCU not reading motor speed | Inspect tachometer wiring |
| F26 | Door switch / lock combination | Door switch + lock mismatch | Replace door switch |
| F28 | Communication fault | Same as F6E1 family | Re-seat ribbon |
| F31 | MCU heat-sink overheat | Ventilation blocked or MCU failing | Check vents, replace MCU |
| F35 | Pressure switch / sensor | Failed analog pressure sensor | Replace sensor |
| LF | Long fill (older display equivalent of F8E1) | Verify water supply | |
| LD | Long drain (older display equivalent of F9E1) | Clean pump filter | |
| Sd | Suds detected | Too much detergent | Run a clean cycle empty |
| Sud | Suds detected | Same as Sd | Use HE detergent in proper dose |
| dL | Door won't lock | Foreign object in latch, failed lock | Inspect lock |
| dU | Door won't unlock | Lock motor stuck | Power-cycle, replace lock |

## The 5 Most Common Whirlpool Washer Faults

### F8E1 / F20 / LF — Long Fill (most common)

The washer hasn't reached the target water level in the fill window. Three checks in order:

1. **Both supply valves fully open + supply pressure ≥20 PSI.** Surprisingly common: a partially-closed valve from a recent service call.
2. **Inlet hoses not kinked + inlet screens clean.** The mesh screens at the dishwasher valve clog with sediment in older houses. Pop them out (needle-nose pliers) and rinse.
3. **Inlet solenoid valve working.** Test by jumpering each side (hot and cold) of the valve with the supply on. Valve should click and water flow. Dual-coil valves often have one side fail while the other works — symptom: long fill only on cold or only on hot cycles.

### F9E1 / F21 / LD — Long Drain

Drain pump can't move water within the expected window.

1. **Clean the drain pump filter.** Front-load Whirlpools have an access panel on the lower-front kickplate. Newer Cabrio top-loads have the filter inside the tub (lift the front-right corner of the inner tub to access). Lint, coins, and small items collect here.
2. **Verify drain hose has a high loop.** Hose must rise to ~32-39 in before dropping to the standpipe. A flat install causes intermittent F9E1.
3. **Test the drain pump.** With the cabinet open, jumper the pump leads. A pump that hums but doesn't move water = impeller fouled (often a sock or underwire). A pump that doesn't move at all = electrically dead, replace.

### F5E3 — Door Cannot Unlock (front-load)

The lock motor is stuck in the locked position. Common after a power outage mid-cycle.

1. Cancel cycle, power off at breaker for 5 minutes.
2. Power on, attempt to unlock from the panel. If F5E3 clears, the lock recovered.
3. If still stuck, the lock motor or wax actuator inside has failed. **Manual unlock**: pull the lower front kick plate, reach up through the access opening to the door lock assembly, pull the manual release tab. Then replace the lock (~$45-$80 part).

### Sd / Sud — Suds Detected

Not really a fault — the sensor has detected excessive suds that prevent normal water-level reading. Caused by:

- Non-HE detergent in an HE machine
- Too much detergent (HE machines use ~2 tablespoons, not the cap-full your grandmother used)
- Detergent buildup in the dispenser

Fix: pause for 30 minutes (suds dissipate), then run a hot cleaning cycle empty with vinegar or affresh tablet.

### F1E1 — Main Control Board (CCU) Fault

Generic "the CCU threw an exception" code. The CCU is the brain — failures cascade everywhere.

1. Power off at breaker for 10 minutes (not just unplug).
2. Power on. If F1E1 doesn't return immediately, it may have been a transient.
3. If F1E1 returns, the CCU has likely failed. Cost: $180-$380 part + labor. Before replacing, verify it's not a wiring harness break to the MCU or door lock — those cascade into "F1E1 in disguise" patterns.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Drain pump (Whirlpool W10581874 / WPW10730972-style) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22W10581874%22+Whirlpool+drain+pump&tag=errorcodefixes-20) \| RepairClinic | $35-$95 |
| Inlet valve (dual coil) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22Whirlpool+washer+inlet+valve%22&tag=errorcodefixes-20) | $45-$95 |
| Door lock assembly (front-load) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22Whirlpool+washer+door+lock%22&tag=errorcodefixes-20) | $45-$80 |
| Pressure sensor (water level) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22Whirlpool+washer+pressure+sensor%22&tag=errorcodefixes-20) | $25-$55 |
| Drive motor (direct-drive Cabrio) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22Whirlpool+Cabrio+drive+motor%22&tag=errorcodefixes-20) | $180-$320 |
| Motor Control Unit (MCU) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22Whirlpool+washer+MCU%22&tag=errorcodefixes-20) | $130-$240 |
| Central Control Unit (CCU) - main board | RepairClinic, Whirlpool parts | $180-$380 |
| Door seal / bellows (front-load) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-whirlpool-washer-error-codes&k=%22Whirlpool+washer+door+bellows%22&tag=errorcodefixes-20) | $80-$170 |

## Technician Tips

- **Whirlpool's diagnostic mode** is entered by rotating the cycle selector knob to 12 o'clock, then turning it 3 clicks right, 1 left, 1 right, 1 left (on knob-based models). On button models: hold Spin Speed and Soil Level together for 3 seconds. Mode shows last 5 codes with timestamps.
- The **CCU and MCU look similar** — don't swap them. CCU is the larger of the two, usually mounted near the top rear of the cabinet. MCU is smaller, near the motor at the bottom.
- For repeat F5E3 on units installed in laundry rooms above garages (cold install): the door wax actuator slows in cold weather and reports unlock-fail false-positives. Move installation to a warm room or accept seasonal recurrence.
- The **W10581874 drain pump** fits ~80% of post-2012 Whirlpool / Maytag / Kenmore washers because Whirlpool consolidated parts. Cheaper aftermarket equivalents work fine — premium-brand isn't required for this part.

## Common Code Combinations

- **F8E1 → F35**: Long fill triggered the pressure sensor to throw range error. Check supply first, sensor second.
- **F9E1 → Sd**: Drain blocked + suds detected. Clean filter and run cleaning cycle with vinegar.
- **F5E3 → F1E1**: Door lock failed in a way that took down the CCU communication. Replace door lock; CCU usually recovers.

If a code returns within 24 hours of clearing, the failure is real — stop resetting and diagnose.

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error code 31 (pressure / suspension fault)](/posts/lg-washer-error-code-31/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG refrigerator error codes (complete guide)](/posts/lg-refrigerator-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Bosch dishwasher error codes](/posts/bosch-dishwasher-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Maytag washer error codes (Bravos + Centennial)](/posts/maytag-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Samsung refrigerator error codes](/posts/samsung-refrigerator-error-codes/)

