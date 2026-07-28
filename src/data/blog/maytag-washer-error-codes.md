---
title: "Maytag Washer Error Codes — Complete Fix Guide (Bravos + Centennial)"
description: "Maytag washer error codes for Bravos, Centennial, MVWB, MVWX, and MHW front-load models. Covers F1E1-F9E1, dE, Sud, Lid, dL, ndF and door/drain/balance faults."
pubDatetime: 2026-05-17T20:45:00Z
modDatetime: 2026-05-17T20:45:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - maytag
  - washer
  - laundry
  - appliances
---
<!-- VOICE-GUARD-OFF -->

## Maytag Washer Error Code Reference

Maytag washers share the Whirlpool platform at the control-board level (Whirlpool owns Maytag since 2006), so the F#E# code dictionary is nearly identical. Where Maytag differs is in the display vocabulary: more letter-codes (Lid, ndF, dL) and slightly different fault-priority logic on the Bravos top-load family.

| Code | Fault | Most Likely Cause | First Action |
|------|-------|-------------------|--------------|
| F1E1 | Main control board (ACU) fault | Failed appliance control unit | Power-cycle 10 min, then replace ACU |
| F2E1 | Stuck key on user interface | Liquid intrusion / worn membrane | Replace user interface |
| F3E1 | Water temperature sensor | Failed thermistor | Test sensor resistance |
| F5E1 | Door switch fault (front-load) | Switch open or failed | Test door switch |
| F5E2 | Door won't lock | Lock motor or wax actuator failed | Replace lock assembly |
| F5E3 | Door can't unlock | Same as F5E2, opposite direction | Manual unlock + replace |
| F6E1 / F6E2 / F6E3 | Communication fault (ACU↔UI or ACU↔MCU) | Wiring or board failure | Re-seat ribbon cables |
| F7E1 | Motor drive fault | Motor or MCU failed | Test motor windings |
| F8E1 | Long fill | Water supply or inlet valve issue | Verify supply |
| F8E2 | Detergent dispenser fault | Stuck actuator | Inspect dispenser |
| F8E3 | Overflow | Pressure sensor or inlet valve | Shut supply |
| F9E1 | Long drain | Drain pump blocked | Clean pump filter |
| F9E2 | Drain pump fault | Pump electrically failed | Replace pump |
| F0E1 | Foreign object in tub (Bravos) | Item between inner and outer tub | Disassemble and remove |
| dE | Door not locked | Same as F5E2 | Inspect door |
| dL | Door cannot lock | Same as F5E2 | Replace lock |
| dU | Door cannot unlock | Same as F5E3 | Manual unlock |
| Lid | Lid not closed or lid lock fault (top-load) | Lid switch failed | Test lid switch |
| LdL | Lid lock fault (Bravos) | Lock motor failed | Replace lid lock |
| Sud / Sd | Suds detected | Too much detergent | Run cleaning cycle |
| ndF | Drain fault (no drain detected) | Same as F9E1 | Clean pump |
| Int | Cycle interrupted | Power outage or door opened mid-cycle | Resume cycle |
| oFb | Off-balance | Load not distributed | Redistribute laundry |

## The 4 Most Common Maytag Washer Faults

### F8E1 — Long Fill

Most common Maytag fault by service-call frequency. Same diagnosis as Whirlpool F8E1:

1. Both supply valves fully open, pressure ≥20 PSI.
2. Inlet hoses not kinked, inlet screens clean.
3. Inlet solenoid working — test each coil (hot and cold) separately.

On the Bravos top-load (impeller drive), there's an extra failure mode: the "balance sensor" (a tilt switch) can intermittently report a non-level condition that prevents the fill cycle from starting. If you see F8E1 combined with no inlet-valve activation, level the unit first.

### F9E1 / ndF — Long Drain

Drain pump can't clear within the window.

1. Clean the drain pump filter. On front-load Maytags (MHW series), there's a lower-front access panel. On Bravos top-loads, lift the front-right corner of the inner tub.
2. Verify drain hose high loop (~32-39 in rise) before standpipe.
3. Test pump electrically. Hums but no water = impeller fouled. Dead = replace.

A subtle Bravos-specific failure: the recirculation pump (separate from drain pump) can fail closed and cause F9E1 by preventing the pressure switch from reading "drained". Verify both pumps move water.

### Lid / LdL — Lid Lock Fault (Bravos top-load)

Bravos washers have a lid lock that engages during spin. Failure modes:

- **Lid switch contacts dirty.** Spray contacts with electronics cleaner; if the lid open/close shows in diagnostic mode after cleaning, the switch was the issue.
- **Lid lock motor (solenoid) failed.** A common failure mode after 3-5 years of use. Replacement is ~$35-$60 part, 30-minute job.
- **Lid lock harness pinched.** The harness routes through the hinge and chafes on the sheet metal edge. Inspect, re-route if needed.

### F1E1 — ACU (Main Control Board) Fault

Same as Whirlpool F1E1. Power off at breaker for 10 minutes. If F1E1 returns, the ACU has failed.

Before swapping the ACU ($180-$380 part), verify:
1. All wiring harnesses re-seated firmly at the ACU.
2. No water intrusion at the ACU housing (Bravos units installed in basements with high humidity sometimes have ACU corrosion).
3. The MCU (motor control unit) is also healthy — F1E1 sometimes cascades from MCU failure.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Drain pump (W10581874 / WPW10730972-style) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22W10581874%22+washer+drain+pump&tag=errorcodefixes-20) \| RepairClinic | $35-$95 |
| Lid lock / strike assembly (Bravos top-load) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22Maytag+Bravos+lid+lock%22&tag=errorcodefixes-20) | $35-$65 |
| Door lock (front-load MHW) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22Maytag+washer+door+lock%22&tag=errorcodefixes-20) | $45-$80 |
| Inlet valve (dual coil) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22Maytag+washer+inlet+valve%22&tag=errorcodefixes-20) | $45-$95 |
| Pressure sensor | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22Maytag+washer+pressure+sensor%22&tag=errorcodefixes-20) | $25-$55 |
| Drive motor (Bravos direct-drive) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22Maytag+Bravos+drive+motor%22&tag=errorcodefixes-20) | $180-$320 |
| ACU (appliance control unit) - main board | RepairClinic, Maytag parts | $180-$380 |
| Lid switch (older Centennial / Atlantis) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-washer-error-codes&k=%22Maytag+washer+lid+switch%22&tag=errorcodefixes-20) | $20-$45 |

## Technician Tips

- **Maytag Bravos diagnostic mode**: knob units use the same 3R-1L-1R-1L pattern as Whirlpool. Button units (newer Bravos XL) hold Pause/Cancel and Spin Speed together for 3 seconds.
- The **Bravos suspension rods** (4 of them, support the outer tub) fail at year 5-7 reliably. Symptom: violent vibration during spin + chronic uE/oFb codes. Replace all four together — single-rod replacement creates an unbalanced suspension that re-fails within months.
- **The F0E1 "foreign object in tub" code** on Bravos units is real, not a sensor false-alarm. Disassemble and pull whatever's wedged between the inner and outer tub (usually a sock or coin). Failing to address it cascades into bearing damage.
- Maytag's **Whirlpool-shared parts** (W10581874 pump, dual-coil inlet valves, ACU/MCU boards) often work across Whirlpool, Maytag, Kenmore, and Amana lines. Cross-reference part numbers if your local supply doesn't stock Maytag-specific.

## Common Code Combinations

- **F8E1 → F35**: Same diagnosis as Whirlpool — supply issue triggered pressure sensor range error.
- **F9E1 → Sud**: Drain blocked AND suds present. Clean filter, run vinegar cleaning cycle.
- **Lid → F7E1**: Lid lock failure prevented spin, motor drive errored out. Fix lid lock first.
- **F0E1 → uE → F9E1**: Foreign object damaged the inner tub, threw the balance off, then jammed the drain. Disassemble and resolve at once.

If codes return within 24 hours of clearing, you have a real failure — not a glitch. Schedule the actual diagnostic.

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** LG washer error code 31 (pressure / suspension fault)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG refrigerator error codes (complete guide)](/posts/lg-refrigerator-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Bosch dishwasher error codes](/posts/bosch-dishwasher-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Whirlpool washer error codes (F-codes + Cabrio)](/posts/whirlpool-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Samsung refrigerator error codes](/posts/samsung-refrigerator-error-codes/)
