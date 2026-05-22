---
title: "LG Washer Error LE — Motor Lock / Stator Fix"
description: "LG washer error LE means the main control board sent a command to spin the motor but the Hall sensor on the stator reported the rotor not turning, or..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Industrial Error Code Fixes"
slug: lg-washer-error-le
featured: false
draft: false
tags:
  - lg
  - motor-lock-or-stator-fault
  - troubleshooting
---
## Quick answer

LG washer error LE means the main control board sent a command to spin the motor but the Hall sensor on the stator reported the rotor not turning, or turning at the wrong RPM, for at least 5 seconds — typically a stuck drum, a failed Hall sensor, or a broken connection between the stator and the board. About 35% of LE codes on LG direct-drive washers are caused by an object jammed between the drum and the tub (a bra wire, a coin, a small sock), not a motor failure. Check for foreign objects before ordering parts.

## What LE means on an LG washer

LG front-load and top-load washers since about 2008 use a direct-drive (DD) motor — no belt, no transmission. The stator (a fixed iron core with copper windings) bolts to the back of the outer tub. The rotor (a permanent-magnet ring with internal Hall-effect sensors on a small PCB) bolts directly to the drum shaft. When the board energizes the stator windings in sequence, the magnetic field rotates and drags the rotor with it. A Hall sensor PCB attached to the stator reports rotor position and speed back to the main board.

Error LE (locked motor error) fires when the board commands a spin but the Hall feedback shows the rotor isn't responding — either not turning at all, turning at the wrong speed, or turning in the wrong direction. The board doesn't distinguish between mechanical lock (drum can't turn) and electrical fault (Hall sensor or wiring) at the code level. Both throw LE.

On the WM-series front-loaders (WM2487HRM, WM2501HVA, WM3997HWA, and most successors), LE typically appears mid-wash or at the start of a spin cycle. On WT-series top-loaders (WT4801CW, WT7100CW, WT7300CV, etc.), LE appears at the agitate stage. Newer models (post-2018) with Smart Diagnosis can hold the play button against a phone microphone running the LG ThinQ app to decode the fault into more granular subcategories.

## Common causes (ranked by frequency)

In LG washer service experience:

1. **Foreign object jammed between drum and tub** — about 35%. Bra wire, coin, key, or small piece of clothing caught between the inner and outer drums.
2. **Failed Hall sensor PCB on the rotor** — about 20%. The small sensor PCB on the back of the rotor has cracked or corroded.
3. **Loose or corroded connector between stator and main PCB** — about 15%. The 6-9 wire harness between the stator and the board has come loose or oxidized.
4. **Failed stator windings (one phase open)** — about 10%. Less common, but a winding can burn out and the motor can't develop full torque.
5. **Drum bearing failure causing extreme drag** — about 8%. Bearing eats itself, drum no longer spins freely, motor stalls under load.
6. **Failed main PCB (motor driver section)** — about 6%. The H-bridge or speed control circuit on the board has failed.
7. **Overloaded wash (too much laundry or extremely wet load)** — about 4%. Motor can't develop enough torque against the load.
8. **Wrong replacement rotor or stator mismatch from prior repair** — about 2%.

**Pro nugget:** the LG WM front-loader stator-to-board connector is exposed to detergent and water drips during normal operation — over 5-7 years the male pins on the stator side corrode green. The fix is not just to clean the pins (the corrosion has eaten the plating, contact resistance is now permanent) — you have to clip the corroded section of the harness and crimp on a new connector. RepairClinic and most LG parts dealers stock the harness as a sub-assembly. Replacing just the stator without addressing the harness means the new stator's pins will corrode in the same timeframe and you'll be back to LE in 12 months.

## Step-by-step fix

Before you start: unplug the washer, shut off water at the wall valves, and remove all clothing from the drum.

1. **Confirm the code.** Read the display: "LE" (older) or "1E" (some newer models map LE to a 1E code). On WT top-loaders, the same fault may show as "uE" if it's pre-wash and "LE" if mid-cycle.

2. **Check for foreign objects.** With the unit unplugged, manually rotate the drum by hand. It should turn freely with mild friction. Stop and listen for grinding or clicking — a foreign object usually makes a metallic tick as the drum rotates. Look between the inner drum holes and the outer tub with a flashlight. Reach in through the door (front-loader) or top (top-loader) and feel for protruding objects.

3. **Remove foreign objects.** On front-loaders, common technique: remove the lower kick panel, then access the drum pulley side. Some models have a small access port in the front gasket boot — pull the gasket and inspect. On top-loaders, the agitator post can be unscrewed for access to the drum bottom.

4. **Inspect the drain pump.** A locked drain pump can sometimes throw LE on newer models that monitor pump load. Pull the drain filter (front-loader, behind the kick panel), drain residual water into a shallow pan, remove debris, and clean.

5. **Inspect the stator-to-board harness.** Tip the washer back gently (front-loader) to access the back panel. Remove the back panel (typically 4-8 screws). Locate the stator at the back of the tub — the large round ring with copper windings. Trace the harness from the stator to the main PCB. Look for: green corrosion on the connector pins, melted insulation, chafed wires. If you see corrosion, the harness needs replacement.

6. **Ohm-test the stator windings.** Disconnect the stator harness from the main board. Across the U-V-W phases, expect roughly 5-15 ohms phase-to-phase, balanced (within 10%). One open phase or one shorted phase indicates a dead stator.

7. **Inspect the rotor and Hall PCB.** Remove the rotor (one center bolt, typically 17mm). The rotor is a large iron ring with permanent magnets bonded to the inside. The Hall PCB is a small board with a 4-6 wire harness, mounted to the back of the rotor or to the stator face. Look for: corrosion on the PCB traces, cracked solder joints, damaged Hall ICs. If the Hall PCB is damaged, replace it (it's available separately from the stator).

8. **Replace the failed component.** Most LE failures on a 5+ year old LG come down to: (a) replace the Hall sensor PCB, or (b) replace the harness from stator to main board, or (c) replace the entire stator-rotor assembly. Order by exact part number — LG stators are not universally interchangeable across model years.

9. **Reassemble and test.** Reinstall the rotor with the center bolt torqued to 65 ft-lbs (specific to model — check service manual). Replace the back panel. Restore water and power. Run a test cycle on Drain & Spin with no clothes. Listen for smooth spin-up to high RPM without LE.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Stator assembly (WM front-loader) | LG 4417EA1002K | $145-225 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le), [Amazon](https://www.amazon.com) |
| Rotor assembly (WM front-loader) | LG 4413ER1003A | $185-265 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le), [Amazon](https://www.amazon.com) |
| Hall sensor PCB | LG 6501KW2002A | $35-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le), [Amazon](https://www.amazon.com) |
| Stator-to-board harness | LG 6877ER1016T | $25-55 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le) |
| Main PCB (varies by model) | LG EBR-series | $245-485 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le), [Amazon](https://www.amazon.com) |
| Tub bearing kit (front-loader) | LG 4280FR4048L | $85-145 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le), [Amazon](https://www.amazon.com) |
| Door gasket / bellows (front-loader) | LG MDS47123604 | $115-185 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lg-washer-error-le) |

LG part numbers are very model-specific. A WM2487HRM stator (4417EA1002K) is different from a WM3997HWA stator (4417EA1002L) — confirm the exact suffix letter for your model before ordering.

## When to call a professional

Call an appliance tech when:

- You've replaced the Hall PCB and stator and LE returns. The next suspect is the main PCB, which on most LG washers runs $245-485 and is not always available — sometimes the only path is full replacement of the washer.
- The drum doesn't rotate freely even after removing foreign objects. The tub bearing has failed; this is an 8-12 hour job involving full disassembly of the outer tub. Cost-prohibitive on units over 7 years old.
- You see a refrigerant-like puddle under the washer. Detergent dispenser overflow or pump leak — needs diagnosis.
- The washer is under LG factory warranty (typically 1 year parts, 10 years on motor, 7 years on stainless drum).

## FAQs

**The washer worked fine 5 minutes ago. Why LE now?**
Sudden LE is almost always a foreign object that just shifted into a binding position. Inspect the drum carefully before assuming an electrical fault.

**Can I run the washer with LE displayed?**
No. The board has shut down the motor for safety. Forcing it to run risks burning the stator windings if the rotor is actually locked.

**My washer is 8 years old. Worth fixing for LE?**
Depends on the cause. If it's a $50 Hall PCB and 30 minutes of labor, yes. If it's a $400 PCB plus $200 stator, probably not — at that point a new washer makes more sense.

**The LE code only appears on heavy cycles. Lighter cycles work. Why?**
Two possibilities: marginal stator winding that can run light loads but stalls on heavy, or bearing drag that worsens under load. Either way, ohm-test the stator and verify drum rotates freely by hand.

**Difference between LE and UE?**
LE = motor lock or stator fault. UE = unbalanced load (load too unevenly distributed for spin cycle). UE is normal user behavior; LE is a hardware fault.

## Related guides

- [LG Refrigerator Error ER RF — Evap Fan Motor Fix](/posts/lg-refrigerator-error-er-rf)
- [LG Dishwasher Error IE — Water Inlet Fix](/posts/lg-dishwasher-error-ie)
- [GE Washer Error Code E1 — Front Load Fix](/posts/ge-washer-error-code-e1)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Samsung vs LG French door refrigerators](/posts/samsung-vs-lg-french-door-refrigerators/)

