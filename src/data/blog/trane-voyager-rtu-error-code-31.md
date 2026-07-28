---
title: "Trane Voyager RTU Error Code 31 — Fix"
description: "Trane Voyager rooftop unit (RTU) error code 31 on the UCM (Unit Control Module) or Tracer SC controller indicates a high-pressure cutout — the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: trane-voyager-rtu-error-code-31
featured: false
draft: false
tags:
  - trane
  - hvac
  - error-codes
  - compressor-lockout-high-pressure
---
## Quick answer

Trane Voyager rooftop unit (RTU) error code 31 on the UCM (Unit Control Module) or Tracer SC controller indicates a high-pressure cutout — the discharge-side pressure switch opened during a cooling call, indicating head pressure exceeded approximately 600 psi (R-410A) or 350 psi (R-22). The most common single cause in commercial rooftop service is a dirty or restricted condenser coil reducing airflow across the condensing surface, not a refrigerant overcharge or actual mechanical failure. Always start with a coil cleaning and condenser fan check before pulling refrigerant.

## What code 31 means on Trane Voyager RTU

Trane Voyager is Trane's commercial packaged rooftop product line — 3-ton through 25-ton units across the YSC, YCD, YHC, TSC, TKD, TKH series, plus the larger Voyager 3 (now Voyager Light Commercial 25-50 ton) line. Most units use either the UCM 4 or UCM 5 microprocessor control with optional ReliaTel diagnostics, or the newer Tracer SC building automation interface for multi-zone applications.

Code 31 on Trane Voyager controls is the high-pressure trip code. The high-pressure switch is wired in the compressor safety string and opens when discharge pressure exceeds the cutout setpoint — typically 600 psi for R-410A systems and 350 psi for legacy R-22 systems. Unlike low-pressure switches which often have auto-reset, Trane high-pressure switches are typically **manual-reset** — they remain open even after pressure drops, requiring a physical press of the reset button before the compressor can restart. This is a safety design: a high-pressure trip indicates a serious condition (condenser fan failure, refrigerant overcharge, blocked airflow) and Trane wants a tech to investigate before letting the unit run again.

After the first code 31 trip, the controller posts the code and starts a 30-minute lockout timer. After 3 trips within 24 hours, the controller enters hard lockout requiring manual diagnostic reset at the unit.

Why high-pressure trips matter: at discharge pressures above the cutout, the compressor is working at the limit of its mechanical capability. Pressures higher than the cutout for any sustained time can crack the compressor head gasket, damage the discharge valves, or cause oil breakdown. The cutout is sized to stop the compressor before these failures occur.

## Common causes (ranked by frequency)

In commercial Trane Voyager RTU service:

1. **Dirty condenser coil** — about 32%. Years of leaves, cottonwood seed, dust, building dust accumulating on the outdoor coil.
2. **Failed or slow condenser fan motor** — about 18%. Bearings worn, capacitor weak, or motor windings degraded.
3. **Refrigerant overcharge** — about 12%. Too much refrigerant from prior service.
4. **Non-condensables in the system (air, moisture)** — about 10%. Improper evacuation during prior service.
5. **Failed high-pressure switch (drifted low or stuck open)** — about 8%.
6. **Condenser fan blade broken or imbalanced** — about 6%.
7. **Reversing valve issue (heat pumps only, partially stuck)** — about 5%.
8. **TXV stuck restricted causing both high and low pressure issues** — about 4%.
9. **Compressor internal valve plate damage** — about 3%.
10. **Wiring issue at the switch or contactor** — about 2%.

**Pro nugget:** Trane Voyager units up through the 12.5-ton size use a **single condenser fan motor** — and that single fan is the entire heat-rejection capacity of the unit. When that fan fails or slows, head pressure climbs fast. The Voyager 15-ton and larger units have **two condenser fans** wired in parallel; if one fails, the unit can still run with degraded capacity (and elevated head pressure that may or may not trip 31 depending on ambient temperature). **Field check**: count the operating fans during a cooling call. If you see one fan running on a 15+ ton unit, the other is dead — investigate. If you see no fans running on any size unit, you have a dead fan motor or contactor issue and code 31 is imminent. Carry a 3/8 HP and 1/2 HP condenser fan motor on the truck for Trane Voyager service — these are the most common sizes and you'll use them.

## Step-by-step diagnosis

Before you start: turn off the unit at the rooftop disconnect, lock and tag. Verify zero voltage at the compressor contactor poles. Follow rooftop safety procedures.

1. **Read the controller's fault history.** UCM units have a 6-button service panel with LED display; Tracer SC has a touchscreen interface. Navigate to Faults → History. Note code 31 and preceding faults.

2. **Reset the high-pressure switch.** Find the HP switch (typically on the discharge line near the compressor, with a small red reset button). Push the reset button until you feel/hear a click. The switch should close (reset) only if pressure has dropped below threshold.

3. **Visually inspect the unit.** On the roof, look at: condenser coil cleanliness (fins should be clean, uniform), condenser fan(s) presence and condition, blower compartment access, refrigerant line connections.

4. **Clean the condenser coil.** Use a non-acid coil cleaner spray plus pressure rinse (back-to-front direction through the coil, not front-to-back which packs debris deeper). A heavily fouled coil can require commercial coil cleaning service ($300-600).

5. **Test condenser fan motor(s).** Restore power briefly, command a cooling call (jumper the thermostat at the controller terminals if needed). Verify fan(s) spin within 30 seconds. Check air discharge from the top of the unit — should be a strong, uniform updraft. Weak airflow = bad motor or capacitor.

6. **Capacitor test on the condenser fan motor.** Power off, discharge capacitor with a 20kΩ resistor. Measure capacitance — a typical Trane condenser fan run capacitor is 5-7.5 µF. Reading below 90% of nameplate = degraded capacitor; replace.

7. **Connect manifold gauges and verify pressure.** With unit running stable for 10+ minutes, read discharge and suction. Discharge on R-410A should be 350-450 psi at 95°F ambient; on R-22, 200-275 psi. Pressures above these and code 31 is real, not a switch issue.

8. **Check sub-cooling.** Measure liquid line temperature at the condenser outlet. Subtract liquid line saturation temp (from discharge pressure on P-T chart). Sub-cooling should be 8-15°F. Above 15°F = overcharge; below 8°F = undercharge or other issue.

9. **For non-condensable suspicion:** If pressures are high and there's no obvious airflow or fan issue, suspect non-condensables. A vacuum decay test (recover refrigerant, evacuate, isolate, watch vacuum for rise over 30 minutes) confirms non-condensables. Recovery and re-evacuation required.

10. **Replace the HP switch only if pressures are verified normal but switch keeps tripping.** Bench-test the switch by applying air pressure to confirm setpoint. Switches drift over time and can trip prematurely.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| High-pressure switch (R-410A, 600 psi, manual reset) | Trane SWT2476 | $145-225 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| High-pressure switch (R-22 legacy, 350 psi) | Trane SWT2477 | $115-185 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| Condenser fan motor (1/2 HP, 460V, 825 RPM) | Trane MOT09224 | $385-585 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| Condenser fan blade (24", 4-blade) | Trane FAN02256 | $145-225 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| Condenser fan run capacitor (7.5 µF, 440V) | Trane CPT00658 | $35-65 | [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Amazon](https://www.amazon.com) |
| Compressor contactor (3-pole, 50A, 480V) | Trane CTR03773 | $185-285 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| UCM 4 control module | Trane MOD03003 | $585-885 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| Tracer SC controller | Trane X13651531-01 | $1,485-1,985 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| Compressor (Copeland Scroll, 5-ton R-410A) | Copeland ZP67KCE-TFD | $1,585-2,085 | [Johnstone](https://www.johnstonesupply.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |
| Coil cleaner (non-acid, gallon) | NU-Calgon Evap Foam | $35-55 | [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31), [Amazon](https://www.amazon.com) |
| Manifold gauge set (R-410A/R-22) | Yellow Jacket 49967 | $185-285 | [Amazon](https://www.amazon.com), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-voyager-rtu-error-code-31) |

Johnstone Supply and Grainger are primary commercial HVAC distributors. AutomationDirect carries the controls but not sealed-system parts. Trane's own distribution (Trane Supply) carries the deepest OEM inventory but at premium pricing.

## When to call a professional

Commercial RTU work requires EPA Section 608 certification for refrigerant and typically requires:

- Licensed mechanical or HVAC/R contractor for compressor or sealed-system work
- Licensed electrician for 480V 3-phase electrical
- Roof access compliance
- AHJ inspection on major component replacement

Specific situations:

- Compressor replacement. Oil charge handling, evacuation procedure, motor megger.
- Refrigerant overcharge requires controlled recovery.
- Non-condensables require system flush and re-evacuation.
- Tracer SC controller replacement. Trane's Rover service tool needed for configuration.
- Critical-use building (data center, hospital, mission-critical retail).

## FAQs

**Why does code 31 only happen during summer?**
Higher ambient temperature directly raises head pressure (refrigerant condensing pressure follows ambient). A condenser that's marginal at 75°F can trip at 95°F. Cleaning the coil and verifying fans handles most summer 31 trips.

**My condenser fan is spinning. Why high head?**
Verify the fan is spinning at full speed in the correct direction (discharge upward). A fan running on a weak capacitor turns slowly and produces inadequate airflow even though it looks "fine." Use an anemometer or rough-check by feeling for strong updraft.

**Can I just press the reset button and keep running?**
No. High-pressure trips happen for real reasons and ignoring them risks compressor damage. Investigate the root cause every time.

**What's the typical Trane Voyager service life?**
Properly maintained, 15-20 years. Most failures past 15 years are compressor or coil-related and may not be cost-effective to repair on the original equipment.

**Difference between Trane code 31 and Carrier code 25 (both high pressure)?**
Same condition, different manufacturer's code numbering. Diagnostic path is identical: coil cleaning, fan check, refrigerant verification.

## Related guides

- [Carrier WeatherMaker RTU Error Code 23 — Fix](/posts/carrier-weathermaster-rtu-error-code-23)
- Carrier 41 Error Code — Blower Motor Failure Fix
- [Bryant Error Code 13 — Limit Lockout Fix](/posts/bryant-error-code-13)
