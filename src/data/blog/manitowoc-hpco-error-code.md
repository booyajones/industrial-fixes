---
title: "Manitowoc HPCO Error Code — High Pressure Cut Out Fix"
description: "HPCO means the high-pressure cutout switch opened — discharge pressure hit roughly 450 PSI on an air-cooled unit and the safety tripped the compressor..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: manitowoc-hpco-error-code
featured: false
draft: false
tags:
  - manitowoc
  - commercial-refrigeration
  - ice-machine
  - high-pressure-cut-out
  - troubleshooting
---
## Quick answer

HPCO means the high-pressure cutout switch opened — discharge pressure hit roughly 450 PSI on an air-cooled unit and the safety tripped the compressor offline. Nineteen out of twenty times the cause is a packed condenser coil, not a bad switch.

## What Manitowoc HPCO means

HPCO is a hardware safety, not a soft fault. There's a physical pressure switch plumbed into the discharge line that opens at approximately 450 PSI on R-404A air-cooled units (around 580 PSI on R-410A units, where used). When the switch opens, it breaks the low-voltage safety circuit on the Indigo NXT board, the board shuts the compressor down, and the controller displays HPCO.

The switch is a manual-reset on most Manitowoc commercial models — meaning you have to physically push the reset button on the switch body after fixing the underlying cause. The Indigo NXT controller will not clear HPCO from the panel until the mechanical switch is reset, by design. If you push the panel reset and the fault comes right back, the switch is still open and you need to find it (usually plumbed into the liquid line manifold or the discharge service port area).

Head pressure climbs for one reason: the condenser can't reject the heat the compressor is putting into the refrigerant. On air-cooled units that's an airflow problem. On water-cooled and remote condenser units it's a coolant flow or remote-side problem. Diagnose accordingly.

## Common causes (ranked by frequency)

- **Dirty or packed condenser coil** — by a huge margin the most common.
- **Failed condenser fan motor or capacitor** — fan stopped or running slow, no airflow.
- **Recirculated discharge air** — machine installed without proper clearance or in a closed cabinet with no ventilation.
- **Water-cooled supply restricted or shut off** — closed valve, plugged strainer, scale in the condenser tubes.
- **Overcharge** — usually from a previous "top off" by someone who didn't weigh in the charge.
- **Non-condensable gas in the system** — air introduced during a previous service call without proper evacuation.
- **Stuck-closed water regulating valve (water-cooled units)** — won't open to dump more water as head pressure rises.
- **Failed HPCO switch itself** — opens below spec; uncommon but real.

## Step-by-step fix

1. **Reset the HPCO switch and the controller.** Locate the manual-reset switch (small button on a brass body, usually on the high-side liquid line near the condenser). Press firmly until you feel it click. Then clear the fault on the controller. If it trips again within one freeze cycle, immediately pull gauges before condemning anything.

2. **Pull a full set of gauges and watch one cycle.** Connect a clean gauge manifold to the high-side and low-side service ports. Watch discharge pressure throughout freeze. Healthy R-404A air-cooled discharge at 75°F ambient sits around 215–245 PSI. If you see it ramp past 350 PSI within 5 minutes of freeze start, something is restricting heat rejection.

3. **Clean the condenser coil thoroughly.** Pull the front panel, hold a flashlight behind the coil, and look for daylight through every section. If you see anything less than clear, brush the fins with a soft coil brush (working in the direction of the fins, not across them), then hit it with a non-acid coil cleaner — Nu-Calgon Evap Foam No Rinse or Nu-Brite for heavily-fouled coils. Kitchen-environment coils need a degreaser first; lint-only coils just need a brush and CO2 gun. After cleaning, look through the coil again — you should see clear daylight.

4. **Verify condenser fan operation.** With the machine running, clamp your amp meter on the fan motor lead. Most Indigo NXT condenser fans draw 0.5–1.2 A depending on model. Below that, suspect the run capacitor first (typically 5 µF, sometimes 7.5 µF — check nameplate). Above nameplate amperage indicates a failing motor or a bearing dragging. Swap the capacitor before condemning the motor — it's a $20 part that fixes 30% of "bad fan motor" calls.

5. **Check installation clearances and discharge air recirculation.** Manitowoc spec is 8" minimum clearance at the rear and sides for air-cooled units, 12" preferred. If the machine is installed in a cabinet, against a wall, or where hot discharge air loops back into the inlet, head pressure will climb on a clean coil. Don't underestimate this — I've seen brand-new IDT0500s throw HPCO on day one because the installer slid them into a too-tight built-in space.

6. **For water-cooled units, verify water flow and condenser cleanliness.** Inlet water temperature should be 45–90°F, flow should be at least 1–2 GPM depending on model. Check the strainer at the inlet — pull it and inspect for debris. If the unit has been in service 3+ years on hard water, the condenser tubes may be scaled internally — that requires a descaling pump and CLR-type circulating cleaner, or a tube replacement on heavily fouled units.

7. **Test the HPCO switch directly.** With the system pumped down (or recovered, depending on switch location and isolation valves), remove the switch and test it on the bench with a hand pump and pressure gauge. It should open right around 450 PSI on R-404A air-cooled spec, and close back when pressure drops to roughly 320 PSI. If it opens early, replace it. The K-00432 HPCO switch kit fits most Indigo NXT models.

8. **Verify refrigerant charge by weight.** If you've cleaned the coil, the fan is good, and head pressure is still high, the system may be overcharged from a previous "top off." Recover the entire charge, evacuate to 500 microns, and weigh in the exact nameplate charge. On R-290 hydrocarbon Indigo NXT units, the tolerance is ±5 g / ±0.25 oz — there is no "close enough" on a critically-charged hydrocarbon system.

> **Field knowledge nugget:** On Manitowoc IDT-series air-cooled units installed in QSR (quick-service restaurant) kitchens, the condenser fouls 3–4× faster than the same machine in a sit-down restaurant. Fryer aerosol gets into the coil, mixes with airborne flour or breading dust, and creates a sticky paste that traps everything else. I've pulled condenser coils on 18-month-old IDT0900s in burger joints that looked like 10-year-old units. If the machine is in a QSR, recommend quarterly condenser cleaning to the operator, not the standard 6-month interval. Sell them a service contract or they'll be calling you for HPCO every summer.

**Safety:** Discharge line surface temperature can exceed 200°F during a high-head-pressure event. Wear gloves. If you arrive at a machine that's just tripped HPCO, give it 10 minutes for the discharge line to cool before touching anything. Also — when working on R-290 (propane) Indigo NXT units, do not vent refrigerant to atmosphere, do not braze without proper hydrocarbon-rated leak checks and ventilation, and do not use a halide torch leak detector. R-290 service requires EPA 608 Type II plus a hydrocarbon endorsement.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| HPCO switch kit (R-404A) | K-00432 | $115–$160 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-hpco-error-code) |
| Condenser fan motor (IDT0500) | 7626833 | $210–$295 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-hpco-error-code) |
| Fan motor run capacitor 5 µF | 000002777 | $18–$28 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-hpco-error-code) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Water regulating valve (water-cooled) | K-00298 | $185–$245 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-hpco-error-code) |
| Nu-Calgon Nu-Brite condenser cleaner | 4148-04 | $42–$60 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) / [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=manitowoc-hpco-error-code) |

If you're descaling a water-cooled condenser, also pick up a CLR-rated descaling pump or rent one — a hand-pump approach won't move enough cleaner through a scaled tube bundle in a reasonable time.

## When to call a professional

Call a CFESA-certified tech if:

- HPCO trips repeatedly after you've cleaned the coil and verified the fan is good — you may be dealing with non-condensable gas in the system, overcharge, or a failing compressor that needs proper sealed-system work.
- You suspect non-condensables (air) in the refrigerant — fixing this requires recovery, evacuation to 500 microns, and weighing in a fresh nameplate charge. Not a DIY job.
- The machine uses R-290 and you don't have hydrocarbon-rated recovery, leak detection, and EPA endorsement.
- The HPCO switch is plumbed in a location requiring system pump-down to replace — Schrader-port-mounted switches you can swap with the system running, but liquid-line-tapped switches require proper isolation.
- The condenser is internally scaled on a water-cooled unit and needs chemical descaling or tube replacement — that's specialty work.

## FAQs

**Why does my Manitowoc keep tripping HPCO every afternoon?**
Almost always a marginal cooling situation: coil dirty enough to push head pressure right at the edge, plus rising afternoon ambient temperature tipping it over the 450 PSI limit. Clean the coil, verify fan amp draw, and confirm the equipment-room ventilation is adequate. Closet-installed machines in restaurants are notorious for this.

**Can I just push the HPCO reset and keep using the machine?**
You can reset it once to test, but if it trips a second time, stop. Running an ice machine repeatedly into HPCO is hard on the compressor — discharge valves and motor windings see thermal abuse every time, and you'll be paying for a compressor replacement long before the warranty would have covered it.

**Should I replace the HPCO switch if it keeps tripping?**
Only after you've ruled out high head pressure. The switch is doing its job when it trips — the question is whether the pressure is actually high (real fault) or the switch is faulty (opens below spec). Put gauges on it before condemning the switch.

**What's the difference between HPCO and E01?**
E01 is a soft fault from the controller saying the freeze cycle took too long. HPCO is a hardware safety that physically opened from real overpressure. They often appear in the same machine because the same root cause (dirty condenser, weak fan) can trigger both — but HPCO is the more serious of the two and needs the underlying head pressure issue fixed immediately.

**Will a hot kitchen cause HPCO on a healthy machine?**
If the kitchen ambient at the condenser inlet exceeds about 95°F sustained, yes — Manitowoc's published ambient operating range is 50–110°F but performance degrades sharply above 95°F. If the equipment room runs hot in summer, add an exhaust fan or relocate the machine. Don't try to make a marginal install survive on a marginal coil.

## Related guides

- [Manitowoc E01 Error Code — Long Freeze Cycle Fix](/manitowoc-e01-error-code)
- [Manitowoc E02 Error Code — Long Harvest Cycle Fix](/manitowoc-e02-error-code)
- [Manitowoc E03 Error Code — Probe / Thermistor Open Fix](/manitowoc-e03-error-code)
