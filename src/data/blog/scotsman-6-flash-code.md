---
title: "Scotsman 6-Flash Code — Refrigerant Pressure Out of Range Fix"
description: "A 6-flash code on a Scotsman Brilliance-series ice machine means the controller has detected refrigerant pressure outside the expected operating range —..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: scotsman-6-flash-code
featured: false
draft: false
tags:
  - scotsman
  - commercial-refrigeration
  - ice-machine
  - refrigerant-pressure-out-of-range
  - troubleshooting
---
## Quick answer

A 6-flash code on a Scotsman Brilliance-series ice machine means the controller has detected refrigerant pressure outside the expected operating range — either high-side pressure too high, low-side too low, or a sustained imbalance suggesting a refrigeration fault. On Brilliance models (CU0515, CU0715, CU1526, and similar) the controller reads pressure transducers (not just switches) and can detect a broader range of pressure faults than older models. The most common single cause is a dirty condenser coil restricting head pressure flow; second most common is low refrigerant charge from a slow leak; third is a failed condenser fan motor or capacitor.

## What 6-flash means on a Scotsman

Scotsman's Brilliance line introduced pressure transducer feedback on both high and low sides, replacing the simple pressure switches of older models. The controller reads both pressures continuously and uses them for diagnostic decisions. The 6-flash code (LED visible behind the front panel, sometimes also displayed on the optional iAuCS communicator) means:

- High-side pressure exceeded its high-trip threshold (typically 425-450 PSIG on R-404A air-cooled), OR
- Low-side pressure dropped below its low-trip threshold (typically 5-10 PSIG suction during freeze on R-404A), OR
- The pressure ratio (high/low) is significantly outside the expected band, suggesting compressor capacity loss or refrigerant restriction.

The controller doesn't differentiate between these subcases in the basic LED code — all of them trigger 6-flash. To distinguish them you read the actual pressure transducer values via the controller's diagnostic menu (button sequence varies by model — typically hold the Off button while powering up, navigate to diagnostics).

The Brilliance controller logs the most recent fault to its diagnostic memory, accessible without clearing the fault. Pressure values at the moment of trip are stored.

This is one of Scotsman's smarter fault codes because it tells you the system has a real refrigeration problem rather than just a single switch tripping. But you still need to read the actual pressure values to know which direction the problem is.

## Common causes (ranked by frequency)

1. **Dirty condenser coil** — about 35%. High-side spike from restricted airflow.
2. **Low refrigerant charge from slow leak** — about 20%. Suction pressure drops below trip threshold during freeze; often accompanied by low ice production.
3. **Failed condenser fan or capacitor** — about 15%. Same effect as dirty coil — head pressure rises.
4. **Failed pressure transducer** — about 10%. The transducer itself drifted or failed, sending readings out of range to the controller.
5. **TXV restriction or failure** — about 7%. Thermal expansion valve restricted from contamination or failed sensing bulb produces high-side high / low-side low simultaneously.
6. **Compressor capacity loss** — about 5%. Worn compressor doesn't make pressure; both sides drift out of range.
7. **Recirculated air at condenser** — about 4%. Poor install location.
8. **Liquid line filter-drier restriction** — about 4%. Saturated drier from moisture in system or contaminants.

**Pro nugget:** Scotsman Brilliance CU0715 and CU1526 units installed in commercial environments where the condenser intake is near a kitchen fryer or a steam-heavy operation often have intermittent 6-flash that's actually a transducer problem, not a refrigeration problem. The high-side transducer is mounted on the discharge line, and a slow film of grease+steam aerosol builds up on the transducer housing's electrical connection. The transducer reads correctly cold but drifts as it heats up — discharge pressure reading climbs while actual pressure is normal, controller declares 6-flash. I worked a Wendy's in Phoenix where the issue was traced by putting a service gauge on the high-side Schrader and watching it during operation while the transducer was reporting "high pressure" to the controller. Real pressure was 240 PSIG; transducer was reading 460. New transducer fixed it. Don't assume the transducer is right — verify with a mechanical gauge.

## Step-by-step fix

Before you start: power off at the disconnect, wait 5 minutes for high-side pressure to bleed down to the suction side via the equalization path (or if installed, the expansion valve's bleed orifice).

1. **Read the fault detail before clearing.** Open the front panel, access the controller diagnostic menu (typically hold the Off button while powering up — model-specific sequence). Read: high-side pressure at trip, low-side pressure at trip, ambient temperature, evaporator temperature, and run time elapsed in cycle.

2. **Inspect and clean the condenser coil.** Pull the front panel, shine a flashlight through the fins. Light should be visible through every fin gap. If grease or lint blocks airflow, clean with Nu-Calgon Evap Foam or similar coil cleaner. In heavy-grease environments use degreaser first, then foaming cleaner.

3. **Verify condenser fan operation.** Watch the fan with power on — should run steady at full speed during compressor operation. Amp-meter the motor leads (typically 0.5-1.2 A depending on model). Low amps = capacitor or motor issue. Test the run capacitor with a capacitance meter; replace if outside ±6% of rating.

4. **Connect gauges to the suction and discharge Schrader ports.** Watch actual high-side and low-side pressure during a freeze cycle. Compare to the transducer-reported values from the controller diagnostic. If they disagree significantly (more than ±20 PSIG), the transducer is bad.

5. **Verify operating pressures.** On R-404A air-cooled at 75°F ambient with a clean coil: discharge 200-240 PSIG, suction 28-40 PSIG during freeze. Outside those ranges = real refrigeration problem.

6. **Check for low refrigerant charge.** Suction pressure below 15 PSIG and superheat above 20°F on a Brilliance system suggests low charge. Find the leak (electronic leak detector, soap solution at brazed joints and Schrader ports), repair it (recover charge, repair leak, evacuate to 500 microns), and recharge by weight from the nameplate critical charge.

7. **Inspect the filter-drier.** Feel the inlet and outlet of the liquid line filter-drier during operation. A working drier should be the same temperature side-to-side. A noticeable temperature drop across the drier indicates restriction — replace.

8. **Test the TXV bulb attachment.** The thermal bulb on the suction line near the evaporator outlet must be securely clamped and well-insulated. A loose or poorly insulated bulb gives the TXV bad feedback, causing wrong superheat and pressure imbalance.

9. **After repair, clear the fault and run a complete cycle while monitoring pressures.** Watch for at least one full freeze-harvest cycle to confirm stable operating pressures.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| High-side pressure transducer | Scotsman 02-3987-01 | $145-235 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |
| Low-side pressure transducer | Scotsman 02-3987-02 | $145-235 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |
| Condenser fan motor (CU0715) | Scotsman 02-1473-21 | $185-265 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |
| Fan motor run capacitor (5 µF) | Generic | $18-28 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Liquid line filter-drier | Scotsman 03-0568-01 | $35-55 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |
| TXV (Brilliance series) | Scotsman 12-2842-21 | $185-285 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |
| Coil cleaner (Nu-Calgon Evap Foam) | Nu-Calgon 4171-75 | $20-35 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |
| Refrigerant leak detector (electronic) | Inficon TEK-Mate | $145-235 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-6-flash-code) |

## When to call a professional

Call a CFESA-certified commercial refrigeration tech for 6-flash if:

- You confirm a refrigerant leak. Recovery, repair, evacuation, and weighing in critical charge requires EPA 608 certification and proper equipment.
- The TXV is suspected. TXV replacement on a charged system requires recovery and re-charge.
- Compressor pressures suggest capacity loss. Compressor testing and replacement on commercial refrigeration is licensed work.
- Discharge pressures stay outside spec after coil cleaning and fan verification. Sealed-system diagnosis required.
- The unit is under warranty.
- You're working on R-290 (propane-charged Brilliance models). Hydrocarbon-rated recovery and proper safety procedures required.

## FAQs

**Why does Scotsman use a 6-flash code for so many different problems?**
Brilliance controllers prioritize identifying a system-level pressure fault over differentiating subcauses. The flash code says "pressure isn't right"; the diagnostic menu tells you which direction. Older Scotsman models used multiple codes for different pressure faults but the Brilliance approach trades that for richer transducer-based data.

**Can I run the machine with the pressure transducer disconnected?**
Strongly no. The transducer is part of the safety chain. The controller will continue logging faults and may lock out completely. The transducer is also feedback for the modulating valves on Brilliance models — disconnecting it disables intelligent control.

**My ice production has dropped but I haven't seen a 6-flash. Bad refrigerant?**
Possible early-stage low charge. The 6-flash threshold has some hysteresis built in to avoid nuisance trips. A unit with low charge often shows reduced production for weeks before tripping. Pull gauges and check superheat.

**How accurate are Brilliance pressure transducers?**
±5 PSIG within calibration. Drift over time happens, especially in grease-laden environments. Verify against mechanical gauges if you suspect the transducer.

**Difference between Scotsman 6-flash and Manitowoc HPCO?**
6-flash on a Brilliance Scotsman = pressure transducer-detected out-of-range condition. HPCO on a Manitowoc = mechanical pressure switch tripped. Different sensing methods, different troubleshooting paths, similar root causes (dirty coil, low charge, fan failure).

## Related guides

- [Scotsman 4-Flash Code — Long Freeze Cycle Fix](/posts/scotsman-4-flash-code)
- [Scotsman 5-Flash Code — Long Harvest Cycle Fix](/posts/scotsman-5-flash-code)
- [Manitowoc E15 Error Code — High-Side Pressure Switch Open Fix](/posts/manitowoc-e15-error-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Hoshizaki vs Manitowoc ice machines](/posts/hoshizaki-vs-manitowoc-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc vs Scotsman ice machines](/posts/manitowoc-vs-scotsman-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc E01 long freeze cycle fix](/posts/manitowoc-e01-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** Hoshizaki E2 long freeze cycle fix

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Scotsman 1-flash bin full fix](/posts/scotsman-1-flash-code/)
