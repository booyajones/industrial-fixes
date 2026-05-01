---
title: "Copeland Compressor Error Code 1 — High Pressure Cutout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-18T08:00:00Z
modDatetime: 2024-03-18T08:00:00Z
slug: copeland-compressor-error-code-1
featured: false
draft: false
tags:
  - commercial-refrigeration
  - copeland
  - compressor
  - high-pressure
  - hvac
description: "Copeland compressor error code 1 means the high pressure safety cutout tripped. This guide covers how to diagnose and fix high pressure trips on Copeland scroll compressors in commercial refrigeration and HVAC systems."
---

## Error Code: Copeland Compressor Error Code 1

**What it means:** Error Code 1 on a Copeland scroll compressor (including Copeland Discus, ZP, ZR, and ZB series) indicates a high pressure safety cutout. The high pressure switch — a safety device wired in series with the compressor contactor — tripped because discharge-side refrigerant pressure exceeded its set point (typically 400 PSI for R-404A systems, 450 PSI for R-22, 600 PSI for R-410A systems).

Copeland compressors are the backbone of commercial refrigeration: walk-in coolers, reach-in cases, roof-mounted condensing units, and packaged HVAC systems. When the high pressure switch trips, the compressor shuts off and will not restart until the switch is manually reset (on most manual-reset HP switch configurations) or until pressure drops below the reset threshold (on auto-reset configurations).

High pressure trips are serious. Sustained high discharge pressure overheats the compressor, breaks down the lubricating oil, and accelerates bearing wear. Repeated trips without addressing the root cause will destroy a Copeland compressor over time.

## Common Causes

- **Dirty or fouled condenser coil** — The single most common cause of high pressure trips in commercial refrigeration. Grease, dust, cottonwood seeds, and debris accumulate on the condenser fins and restrict airflow. The refrigerant can't reject heat fast enough, discharge pressure climbs, and the HP switch trips.
- **Condenser fan motor failure** — If one or more condenser fan motors fail (especially on multi-fan condensing units), the remaining fans can't maintain adequate airflow across the coil. High pressure trips follow within minutes on a hot day.
- **Refrigerant overcharge** — Too much refrigerant in the system means the condenser has insufficient volume to subcool all the liquid refrigerant, which backs up liquid into the condenser and raises head pressure.
- **Non-condensable gases (air) in the system** — Air introduced during improper service work raises head pressure because air does not condense at normal system pressures. This presents identically to a dirty condenser but doesn't respond to cleaning.
- **Ambient temperature too high** — Air-cooled condensers are rated to specific maximum ambient temperatures. In unusual heat events or in poorly ventilated machine rooms, ambient temperature may exceed design limits and push head pressure over the HP switch set point even with a clean coil.
- **Faulty high pressure switch set point drift** — Over time, the mechanical HP switch can drift lower, tripping at a lower pressure than intended. A switch that should trip at 400 PSI might trip at 340 PSI, causing nuisance trips on otherwise normal system operation.

## Step-by-Step Fix {#step-by-step-fix}

1. **Reset the high pressure switch.** Locate the high pressure switch on the compressor's discharge line (a small round or rectangular device with a reset button or manual reset button visible). If it's a manual-reset switch, press the button firmly until it clicks. If the system immediately trips again on restart, do not keep resetting — there is an active high-pressure condition that must be resolved first.

2. **Inspect the condenser coil immediately.** This is the first and most important check. Find the condenser coil (typically on the roof unit or condensing unit adjacent to the equipment). Look at the fin face: you should see clean, open aluminum fins. If the fins are loaded with grease, debris, cottonwood seeds, or dirt, the condenser needs cleaning before the system will run reliably. Use a commercial coil cleaner and a fin comb for best results.

3. **Verify all condenser fans are running.** With the system powered and attempting to run, look and listen at each condenser fan. Every fan should be spinning at full speed. A fan running backwards, running slowly (failed run capacitor), or not running at all is causing a significant portion of the high pressure condition. Measure voltage at the fan motor and test the capacitor with a capacitor tester.

4. **Check ambient temperature conditions.** Use a thermometer to measure the actual ambient air temperature entering the condenser. Compare to the condensing unit's rated ambient limit (typically 95°F–115°F depending on the unit). If ambient exceeds the limit, the only short-term solution is to shade the condenser or add supplemental ventilation. Long-term, the system may need to be de-rated or upgraded.

5. **Measure and record system pressures.** Using a refrigeration manifold gauge set, connect to the high-side and low-side service ports. Record suction and discharge pressures. Compare to the system's pressure-temperature chart for the refrigerant type. An abnormally high discharge pressure with a normal or low suction pressure usually indicates a condenser problem. A high discharge pressure with a high suction pressure can indicate refrigerant overcharge or a restriction.

6. **Check for refrigerant overcharge.** An overcharged system will show high discharge pressure, high suction pressure, and higher-than-normal subcooling at the liquid line (measure with a clamp-on thermometer at the liquid line outlet and compare to the saturation temperature at that pressure). Recovering excess refrigerant requires EPA 608 certification — this step requires a licensed technician.

7. **Test the high pressure switch set point.** With a manifold gauge set and a multimeter monitoring the HP switch contacts, slowly raise system head pressure by blocking condenser airflow. Note the exact pressure at which the switch opens. Compare to the specification on the switch label or the system datasheet. A switch tripping 50+ PSI below its spec has drifted and should be replaced.

8. **Check for non-condensables.** If all of the above checks out — clean condenser, all fans running, correct charge — and head pressure is still abnormally high, suspect air or nitrogen in the system. Non-condensables typically present as unusually high head pressure relative to outdoor ambient and do not respond to condenser cleaning. Recovering, evacuating, and recharging the system is the only fix.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| High pressure switch (400 PSI R-404A) | Ranco 010-1766 | $25–$45 | [Amazon](https://www.amazon.com/dp/B013IHQ8CU?tag=errorcodefixes-20) \| Grainger / Johnstone Supply |
| Condenser fan motor (1/4 HP, 208/230V) | Fasco D7909 | $55–$90 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| Grainger / Amazon |
| Fan motor run capacitor | Various (per motor rating) | $8–$20 | [Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) \| Grainger / Amazon |
| Condenser coil cleaner (commercial) | Nu-Brite or similar | $20–$35 | [Amazon](https://www.amazon.com/s?k=Nu-Brite+or+similar+Condenser+coil+cleaner+%28commercial%29&tag=errorcodefixes-20) \| HVAC distributors |
## When to Call a Professional

Any diagnosis involving refrigerant — measuring charge, recovering refrigerant, checking for non-condensables, or recharging — legally requires EPA Section 608 certification. Do not attempt to add or remove refrigerant without proper certification and equipment. Additionally, if the high pressure switch trips immediately on restart even with a clean condenser and functioning fans, there may be a refrigerant-side restriction (failed expansion valve, plugged filter drier) or a compressor internal fault — both of which require a licensed refrigeration technician with proper diagnostic equipment.

> **Pro tip:** On multi-fan condensing units (2, 3, or 4 fans), a single failed fan motor is easily missed during a quick visual inspection — especially if the other fans are loud enough to mask the silence of the dead one. Walk close to each fan and hold your hand a few inches from the discharge air. You should feel strong, warm airflow from each one. A fan running at low speed due to a failed capacitor can look like it's running fine but delivers only a fraction of its rated airflow — barely detectable by sight, easy to catch by feel.

## Related Articles

- [Air Compressor Fault Codes: Complete Guide](/posts/air-compressor-fault-codes/)
- [Atlas Copco Air Compressor Fault Codes — Complete Guide](/posts/atlas-copco-compressor-fault-codes/)
- [BOGE Air Compressor Error Codes - Complete Guide](/posts/boge-compressor-error-codes/)
- [Chicago Pneumatic Compressor Fault Codes — Complete Guide](/posts/chicago-pneumatic-compressor-faults/)
- [CompAir Air Compressor Fault Codes - Complete Guide](/posts/compair-compressor-fault-codes/)
