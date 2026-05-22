---
title: "Mitsubishi P3 Error Code — Outdoor Coil Thermistor Fix"
description: "A Mitsubishi P3 means the outdoor unit's coil thermistor (typically TH4, sometimes labeled TH-7 or TH-DEFROST depending on platform) is reading outside the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: mitsubishi-p3-error-code
featured: false
draft: false
tags:
  - mitsubishi
  - hvac
  - error-codes
  - outdoor-coil-thermistor-error
---
## Quick answer

A Mitsubishi P3 means the outdoor unit's coil thermistor (typically TH4, sometimes labeled TH-7 or TH-DEFROST depending on platform) is reading outside the valid range — open, shorted, or sensing temperature wildly inconsistent with conditions. The thermistor mounts on the outdoor heat exchanger and is critical for defrost control, target superheat, and capacity modulation. Ohm-test the sensor cold; if it reads OL or near 0 Ω, replace it. Field-replaceable on most M-Series and P-Series outdoor units.

## What P3 means on a Mitsubishi

Mitsubishi P-codes are protection codes — the microcontroller decided something was unsafe or unverifiable and shut the system down. P3 specifically targets the outdoor coil thermistor, also called TH4 on most platforms (the labeling varies between MUZ, MXZ, PUZ, PUY, and PU series, but the function is the same).

The thermistor mounts in physical contact with the outdoor heat exchanger — usually clipped to a return bend in the bottom of the coil where defrost frost typically forms first. It's a 10 kΩ NTC sensor at 25°C / 77°F (with platform-specific B-value curves). The outdoor PCB reads voltage across the thermistor as part of a divider circuit. If the input pegs at rail voltage (open thermistor) or drops near zero (shorted), the firmware logs P3.

P3 doesn't always lock out immediately. On some platforms the system attempts a few retries (especially during cold-weather defrost cycles where thermistor readings naturally swing rapidly) before declaring the hard fault. Once locked, you need to cycle power at the disconnect to clear after fixing the cause.

The wired remote controller (PAR-31MAA, PAR-32MAA, MA Smart, etc.) displays P3 directly. The Kumo Cloud or central controller (AE-200) display P3 with associated address and unit number for multi-unit systems.

## Common causes (ranked by frequency)

1. **Open thermistor element** — about 45%. NTC bead fails open. Reads OL on the meter. Most common failure mode on outdoor sensors 6+ years old.
2. **Chafed or pinched lead wire** — about 20%. Cable abrasion against sheet metal, rodent damage in outdoor cabinets (more common than you'd think — mice and squirrels nest in PUZ outdoor units in winter).
3. **Connector backed out at the outdoor PCB** — about 15%. Vibration over time, especially in coastal installs where corrosion adds to it.
4. **Shorted thermistor** — about 8%. Less common; usually moisture intrusion at the lead-wire splice.
5. **Failed outdoor PCB input** — about 5%. Lightning or surge damage to the ADC input or divider resistor.
6. **Thermistor positioned wrong (not in contact with coil)** — about 4%. Recent service installed without seating in the clip; reads ambient air, not coil temp.
7. **Wrong thermistor (different B-value curve)** — about 3%. Generic replacement with wrong specs.

**Pro nugget:** Mitsubishi PUZ-A and PUY series outdoor units installed in northern climates have a specific P3 failure pattern in winter that traces to the sensor lead, not the sensor element. The thermistor lead exits the outdoor cabinet, runs through a gland, and the gland's silicone seal degrades over 5-8 winters of UV and thermal cycling. Cold winter rain or snowmelt enters the gland, freezes inside the lead jacket, splits the insulation, and creates a moisture-shorted phase-to-ground path. Symptom: P3 only in winter, especially after a freeze-thaw event; resolves in spring when the gland dries out. Fix isn't the thermistor — it's a new gland seal and a length of new lead wire from the outdoor cabinet exit to the splice. I solved this on three Vermont PUZ installs by re-running the thermistor lead with a fresh gland; the original thermistors tested fine and were reused.

## Step-by-step fix

Before you start: turn off power at the outdoor disconnect, lock out, wait at least 5 minutes for capacitors to discharge in the outdoor unit. The outdoor PCB has high-voltage DC bus capacitors.

1. **Confirm the code on the remote controller display.** P3 with address indicator.

2. **Open the outdoor service panel.** PUZ series: typically four screws around the side panel. M-Series MUZ outdoor units: front cover, usually six screws. Note the model and serial from the rating plate.

3. **Locate TH4 thermistor.** It will be clipped to a return bend on the heat exchanger coil — usually toward the bottom or lower side. The lead is typically a 2-wire shielded cable, often blue or yellow color-coded, with a 2-pin connector at the outdoor PCB. Confirm by checking the wiring diagram inside the service panel cover.

4. **Disconnect the thermistor at the PCB.** Note the connector position (CN20, CN23, CN-T depends on platform — photograph the harness routing before disconnecting).

5. **Ohm-test the thermistor.** Set multimeter to ohms. Probe the two wire ends at the PCB connector side (or at the sensor side after pulling it off the coil). At 77°F (25°C) the sensor should read approximately 9-11 kΩ. At freezing (32°F / 0°C), about 27-33 kΩ. At hot summer ambient (90°F / 32°C), about 7-9 kΩ. Reading OL (open) or near 0 Ω = bad. Reading wildly off the expected value = bad or wrong sensor.

6. **Verify the lead wire integrity.** With the sensor disconnected, ohm from each wire end to the chassis ground. Should read OL (no continuity). Any continuity to ground = chafed lead or moisture-shorted insulation.

7. **Inspect the gland and lead path.** Trace the lead from PCB back to thermistor. Look at every transition point, especially where the lead exits the outdoor cabinet through a gland. Cracked grommet or sealed-up moisture indicates lead damage.

8. **Replace the thermistor.** Mitsubishi outdoor thermistors are field-replaceable. Order the exact part number for your model — examples include E22M52301 (PUZ family), E22M62301 (M-Series). Confirm B-value curve matches.

9. **Mount the new thermistor in the original clip and seat firmly against the coil.** Apply Mitsubishi-specified thermal paste if your kit includes it (some kits do, some don't).

10. **Reroute the lead with a fresh gland if the original gland is degraded.** Use a Mitsubishi replacement gland kit or a high-quality silicone-rated 1/4" cable gland. Seal the cabinet penetration carefully — water intrusion ruins outdoor PCBs.

11. **Reconnect at the PCB and verify with a complete cycle.** Restore power. The system should run through a full cycle without P3 returning.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor coil thermistor TH4 (M-Series MUZ) | Mitsubishi E22M62301 | $45-85 | [HVAC Parts Shop](https://www.hvacpartsshop.com), [Amazon](https://www.amazon.com) |
| Outdoor coil thermistor (PUZ series) | Mitsubishi E22M52301 | $55-95 | [HVAC Parts Shop](https://www.hvacpartsshop.com), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-p3-error-code) |
| Outdoor coil thermistor (P-Series PUY) | Mitsubishi E12758450 | $65-105 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| Cable gland (replacement, 1/4" weatherproof) | Heyco generic | $8-15 | [Amazon](https://www.amazon.com), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-p3-error-code) |
| Thermistor lead wire (per ft, with shielding) | Generic Belden 9450 | $3-5/ft | [Amazon](https://www.amazon.com), [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mitsubishi-p3-error-code) |
| Outdoor PCB (M-Series outdoor) | Mitsubishi E22270301 | $385-585 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| Service manual access (model-specific) | Mitsubishi MyLink portal | Free for registered techs | Mitsubishi Electric |

## When to call a professional

Call a licensed HVAC tech with Mitsubishi training for P3 if:

- You replaced the thermistor and P3 returns immediately. That points to an outdoor PCB input issue requiring board replacement and proper system address/configuration reset.
- The system is City Multi VRF (PUMY, PURY) rather than M-Series or P-Series single-zone. VRF outdoor sensor work requires the Mitsubishi service tool and proper system protocol handling.
- You suspect outdoor PCB damage from lightning or surge. PCB replacement requires careful address-switch configuration matching the original board.
- Refrigerant work is needed alongside the P3 fix (rare, but if the sensor problem masked a real refrigeration issue).
- The unit is under Mitsubishi warranty. Most factory warranties require licensed installer service for outdoor unit work.

## FAQs

**Why does P3 happen more in winter?**
Outdoor thermistors fail more in winter for two reasons: thermal cycling stress on the sensor element accelerates aging, and moisture infiltration through degraded grommets is more common during freeze-thaw cycles. A marginal sensor that passes in summer fails when the temperature drops.

**Can I substitute a generic 10 kΩ NTC thermistor?**
Possibly, but match the B-value curve. Mitsubishi outdoor thermistors typically use a B-value around 3950K. A generic 10 kΩ NTC with a different B-value (3380K, 3477K) reads correctly at 25°C but diverges at temperature extremes — defrost timing and capacity control go wrong. Use OEM where possible.

**My P3 cleared after a power cycle but came back two days later. Is that normal?**
No — that's an intermittent fault. Either the thermistor is failing intermittently (lead chafe that opens with thermal expansion) or moisture is intermittently shorting it (gland seal issue). Both require replacement, not just a clear.

**Will P3 damage the system if I run it?**
On most Mitsubishi platforms, P3 locks out the affected outdoor unit completely. The system won't damage anything because it isn't running. On a multi-zone system, the other indoor units may still operate while the outdoor is locked.

**Difference between P3 and U4?**
P3 = outdoor coil thermistor fault. U4 = communication error between indoor and outdoor units. Different problems. U4 means the boards aren't talking; P3 means the sensor reading is bad.

## Related guides

- [Mitsubishi Mini Split P1 Error Code — Indoor Coil Thermistor Fix](/posts/mitsubishi-p1-error-code)
- [Mitsubishi Mini Split P2 Error Code — Liquid Pipe Thermistor Fix](/posts/mitsubishi-p2-error-code)
- [Mitsubishi P4 Error Code — Drain Switch Fix](/posts/mitsubishi-p4-error-code)
