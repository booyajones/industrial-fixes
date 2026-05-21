---
title: "Carrier WeatherMaker RTU Error Code 23 — Fix"
description: "Carrier WeatherMaker rooftop unit (RTU) error code 23 on the Comfortlink II or i-Vu control system means the unit's compressor circuit has locked out due to..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: carrier-weathermaster-rtu-error-code-23
featured: false
draft: false
tags:
  - carrier
  - hvac
  - error-codes
  - compressor-lockout-low-pressure
---
## Quick answer

Carrier WeatherMaker rooftop unit (RTU) error code 23 on the Comfortlink II or i-Vu control system means the unit's compressor circuit has locked out due to a low-pressure cutout — the suction-side pressure switch opened during a cooling call. About 45% of these in commercial buildings are low-refrigerant conditions from slow leaks, not actual compressor or sensor failures, but you must verify with a manifold gauge set because the symptoms overlap with several other conditions. Always check refrigerant pressure before assuming the switch or compressor has failed.

## What code 23 means on Carrier WeatherMaker RTU

Carrier WeatherMaker is Carrier's commercial packaged rooftop product line — 48-ton and 50-ton single-stage cooling units, 480V 3-phase, with integrated economizers, electric or gas heat, and Carrier's Comfortlink II microprocessor controls (or the older Comfortlink I on legacy units). Common WeatherMaker models include the 48HCQ, 50HCQ, 48HCR, 50HCR series.

Code 23 on Comfortlink II identifies a low-pressure trip on a specific compressor circuit. On dual-circuit units (most 5-ton and larger), the code is paired with an indicator showing Circuit A (compressor 1) or Circuit B (compressor 2). The low-pressure switch is a pressure-actuated electrical switch wired in the compressor safety string — it opens when suction pressure drops below approximately 55-65 psi (R-410A) or 22-26 psi (R-22) for more than 60 seconds. The controller then de-energizes the compressor contactor, posts code 23, and enters a lockout for 30-60 minutes before allowing automatic reset.

After 3 consecutive low-pressure trips within an hour, the controller enters a "hard lockout" requiring manual reset at the unit display. This is to prevent compressor damage from repeated startup attempts into a fault condition that hasn't been diagnosed.

The reasons low pressure trips are critical: at suction pressure below cutout, the refrigerant returning to the compressor isn't fully vaporized (potential slugging), the compressor isn't getting adequate cooling from the suction gas (overheating risk), and the system is losing refrigerant from somewhere (leak that will progressively worsen if not addressed).

## Common causes (ranked by frequency)

In commercial RTU service experience:

1. **Refrigerant low from slow leak** — about 35%. Most common single cause.
2. **Dirty or restricted evaporator coil** — about 18%. Air flow restriction drops evap pressure.
3. **Failed indoor blower or low CFM through coil** — about 12%. Same effect as dirty coil.
4. **Stuck or restricted expansion valve (TXV or EEV)** — about 10%. Refrigerant flow restricted.
5. **Failed low-pressure switch (drifted high or stuck open)** — about 8%.
6. **Excessive evaporator frosting (ambient too cold or coil staying wet too long)** — about 6%.
7. **Reversing valve issue (heat pump units only)** — about 4%.
8. **Compressor internal mechanical wear (low capacity)** — about 4%.
9. **Wiring issue at the pressure switch** — about 2%.
10. **Comfortlink II controller fault** — about 1%.

**Pro nugget:** Carrier WeatherMaker units use a high-side and low-side pressure switch wired in series with the compressor contactor coil — when *either* switch opens, the contactor drops out and the compressor stops. **Both switches share a 24V circuit**, so a fault at either switch presents the same way at the contactor. The Comfortlink II controller wires the switches to separate digital inputs so it can identify which switch tripped — but in legacy non-Comfortlink units, you only get a generic "compressor lockout" indication. Always trace the wiring at the controller side to confirm code 23 is actually low-pressure and not high-pressure misidentified. Also: the WeatherMaker pressure switches are field-replaceable but they're not the cheap residential type — Carrier specifies switches with **manual reset on hard trips** that cost $145-225 each, not the $35 residential units. Don't substitute residential parts.

## Step-by-step diagnosis

Before you start: turn off the unit at the disconnect (typically a 60-100A 480V disconnect on the rooftop curb), lock and tag, verify zero voltage at the contactor poles. Follow OSHA roof-access safety and have a fall-protection harness if required by the building.

1. **Read the Comfortlink II fault history.** At the unit display (front panel or i-Vu interface), navigate to Faults → History. Note all faults in the last 24 hours — preceding faults often reveal the root cause.

2. **Verify cooling demand is real.** Code 23 only occurs during a cooling call. If the building zone thermostats aren't calling for cooling, the unit shouldn't be trying to run. Check the BAS (building automation) for a stuck zone or oversized cooling setpoint.

3. **Visually inspect the unit on the rooftop.** Look for: ice on the evap coil access (suggests low refrigerant or low airflow), oil residue on copper lines (refrigerant leak indicator), debris on the condenser coil, blower motor running, economizer in correct position.

4. **Check filter and indoor coil access.** Pull the unit's filter access panel. Inspect filter — replace if dirty. Look at the inlet side of the evaporator coil — clean if visibly dirty. Verify the indoor fan is spinning and developing airflow.

5. **Connect manifold gauges.** Schrader fittings on the suction (low) and discharge (high) sides allow gauge connection. With the unit running in cooling mode for 10+ minutes (stable conditions), read both pressures and convert to saturation temp using a P-T chart for R-410A or R-22 (whichever the unit uses — typically R-410A on newer WeatherMakers).

6. **Calculate superheat.** Measure suction line temperature with a clamp-on thermistor about 6 inches before the compressor. Subtract saturation temperature (from suction pressure on the P-T chart). Result should be 8-15°F for a TXV system, 15-25°F for a fixed-orifice system. Very low superheat = liquid floodback risk; very high superheat = refrigerant low or TXV stuck.

7. **For low refrigerant indication:** Leak-detect with an electronic leak detector (Bacharach H-10 PRO, Inficon TLD or similar). Common leak points: TXV brazed joints, Schrader cores under the caps, suction line at the compressor inlet, condenser coil U-bends.

8. **For pressure switch suspicion:** Ohm-test the suction-side switch with the unit off and refrigerant pressure normal. Should be closed (low ohms). If pressure is normal but switch is open, switch is bad. Replace.

9. **Recover, repair leak, evacuate, recharge.** For confirmed leak, this is EPA-certified work. Recovery to a recovery cylinder; repair leak (typically braze); pressure test with nitrogen; deep-vacuum evacuation to 500 microns or less; recharge to nameplate weight.

10. **Verify operation after repair.** Run the unit through a full cooling cycle. Watch suction and discharge pressures, superheat, sub-cooling. Confirm code 23 doesn't return.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Low-pressure switch (R-410A, auto-reset 50 psi) | Carrier HK02ZA111 | $145-225 | [Johnstone](https://www.johnstonesupply.com), [Grainger](https://www.grainger.com) |
| High-pressure switch (R-410A, manual reset 600 psi) | Carrier HK02ZA112 | $185-265 | [Johnstone](https://www.johnstonesupply.com), [Grainger](https://www.grainger.com) |
| Compressor contactor (3-pole, 40A, 480V) | Carrier HC67EZ027 | $185-285 | [Johnstone](https://www.johnstonesupply.com), [Grainger](https://www.grainger.com) |
| TXV (R-410A, 5-ton) | Carrier 33ZCFCR001 | $385-485 | [Johnstone](https://www.johnstonesupply.com), [Grainger](https://www.grainger.com) |
| Compressor (Copeland Scroll 5-ton, R-410A) | Copeland ZP67KCE-PFV | $1,485-1,985 | [Johnstone](https://www.johnstonesupply.com), [Grainger](https://www.grainger.com) |
| Comfortlink II RTU controller | Carrier CESO110057 | $785-985 | [Johnstone](https://www.johnstonesupply.com) |
| Indoor blower motor (3 HP, 460V, 3-phase) | Carrier HC52BE462 | $585-885 | [Johnstone](https://www.johnstonesupply.com), [Grainger](https://www.grainger.com) |
| Manifold gauge set (R-410A/R-22) | Yellow Jacket 49967 | $185-285 | [Amazon](https://www.amazon.com), [Grainger](https://www.grainger.com) |
| Electronic leak detector | Inficon TLD-1 | $585-785 | [Grainger](https://www.grainger.com), [Amazon](https://www.amazon.com) |
| Recovery machine (R-410A capable) | Yellow Jacket Recover-XLT | $885-1,285 | [Grainger](https://www.grainger.com), [Johnstone](https://www.johnstonesupply.com) |

Commercial HVAC parts distribution is dominated by Johnstone Supply, Grainger, and Carrier's own distribution. AutomationDirect carries the controls and contactors but not the sealed-system parts.

## When to call a professional

Commercial rooftop work in nearly all jurisdictions requires EPA Section 608 certification for any refrigerant work, and most jurisdictions also require:

- A licensed mechanical or HVAC/R contractor for compressor or sealed-system work
- A licensed electrician for 480V 3-phase work
- Roof access compliance (some buildings require fall-protection certification)
- AHJ inspection after compressor replacement

Specific situations:

- Refrigerant leak — recovery and repair work is EPA-regulated.
- Compressor replacement. Multi-step process including oil charge, system evacuation, motor megger, current draw verification.
- Comfortlink II controller replacement. Requires Carrier service tool to download/upload configuration.
- The unit is on a critical-use building (hospital, data center, mission-critical retail). Service contracts typically require authorized providers.

## FAQs

**My code 23 comes back the day after refrigerant recharge. Why?**
Slow leak you didn't find. Common locations: TXV brazed joints, Schrader cores, suction line connections. Use a higher-sensitivity electronic detector or soap bubble test under operating pressures.

**Can I just disable the low-pressure switch?**
Absolutely not. Operating without low-pressure protection can damage the compressor catastrophically (within minutes if running with severe low refrigerant). Illegal in most jurisdictions per ASHRAE 15.

**Why does code 23 only happen on hot days?**
Counterintuitively, hot days can lower suction pressure if airflow across the condenser drops — head pressure climbs, capacity drops, suction drops below cutout. Verify condenser coil is clean and condenser fan(s) running.

**How often should refrigerant be checked?**
Annual PM at minimum. Commercial RTUs in critical service should be checked twice yearly (spring and fall). Track refrigerant charge over time — slow declines indicate slow leaks.

**Difference between code 23 (low pressure) and code 25 (high pressure)?**
Code 23 = low-side cutout (suction). Code 25 = high-side cutout (discharge). Different failures: low side = refrigerant short, airflow issue, restriction; high side = condenser issue, overcharge, non-condensables.

## Related guides

- [Trane Voyager RTU Error Code 31 — Fix](/posts/trane-voyager-rtu-error-code-31)
- [Carrier 41 Error Code — Blower Motor Failure Fix](/posts/carrier-41-error-code)
- [Bryant Error Code 13 — Limit Lockout Fix](/posts/bryant-error-code-13)
