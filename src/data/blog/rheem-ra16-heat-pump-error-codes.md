---
title: "Rheem RA16 Heat Pump Error Codes — Flash Code Diagnostic Guide"
description: "Rheem RA16 heat pump error codes: complete LED flash code reference, common causes, step-by-step fix instructions, and OEM parts guide for the 16 SEER RA16."
pubDatetime: 2026-04-24T08:00:00Z
modDatetime: 2026-04-24T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - rheem
  - heat-pump
  - error-codes
  - diagnostics
---

## Rheem RA16 Heat Pump Error Codes — What They Mean

The Rheem RA16 (and its Ruud counterpart, the UA16) is a 16 SEER single-stage heat pump using R-410A refrigerant and a Copeland scroll compressor. It operates in both heating and cooling modes and is designed for split-system installation with a compatible indoor air handler or furnace.

Fault codes are displayed via LED flash sequences on the **outdoor unit control board**. Open the electrical access panel on the side of the unit to view the LED. Codes blink in a repeating pattern: count the flashes, note the pause, then count the next group. The RA16 also stores the last fault in memory — on some board revisions, you can hold the test button for 5 seconds to retrieve the stored fault even after a power cycle.

When paired with a Rheem EcoNet thermostat or communicating air handler, faults also appear as alphanumeric codes on the thermostat display.

[Jump to Fix](#step-by-step-fix)

### RA16 LED Flash Code Reference

| Flash Sequence | Fault | Action |
|----------------|-------|--------|
| 1 flash | Normal standby — no fault | None |
| 2 flashes | High-pressure switch open | Check coil and fan |
| 3 flashes | Low-pressure switch open | Check refrigerant charge |
| 4 flashes | Compressor protection device open | Allow cooldown |
| 5 flashes | Control board fault | Replace board |
| 6 flashes | Outdoor thermistor fault | Check/replace sensor |
| 7 flashes | Anti-short cycle delay (5 min) | Wait — clears automatically |
| 8 flashes | Communicating fault (EcoNet) | Check data wiring |
| Rapid continuous | Low voltage — below 18VAC at board | Check transformer and wiring |

### EcoNet Thermostat Codes (RA16 with Communicating Air Handler)

| Code | Description |
|------|------------|
| E1 | Communication loss — outdoor unit |
| E2 | High-pressure protection |
| E3 | Low-pressure protection |
| E4 | Compressor overload |
| E5 | Reversing valve fault |
| E6 | Discharge line temperature fault |

## Common Causes by Code

**2 flashes — High pressure:**
The condenser coil is dirty or airflow is blocked. The RA16 condenser fan draws air upward through the aluminum-fin coil. Grass clippings, cottonwood seed, and debris accumulate on the lower coil edges (facing the ground). Also check for a failed condenser fan capacitor — a fan running at half speed can't reject enough heat, and head pressure spikes above the 400+ PSIG cutout threshold on R-410A.

**3 flashes — Low pressure:**
Refrigerant undercharge is the primary cause. The RA16's low-pressure cutout triggers below 50 PSIG on R-410A. Leaks most commonly occur at Schrader valve cores (tighten or replace the cores), the flare fittings at the service valves, or the indoor evaporator coil. In heating mode at temperatures below 20°F, ice accumulation on the outdoor coil from a failed defrost cycle can drop suction pressure enough to trigger this code.

**4 flashes — Compressor protection open:**
The Copeland scroll compressor in the RA16 has an internal thermal overload (klixon). It trips when the compressor overheats. Common causes: refrigerant overcharge (liquid flooding the compressor), loss of suction superheat, compressor running at high ambient temperatures (above 105°F) with restricted airflow, or the beginning of compressor winding failure. Do not restart immediately — the klixon resets automatically after 30–45 minutes of cooldown.

**6 flashes — Thermistor fault:**
The outdoor ambient temperature thermistor plugs into the control board and is attached to the top of the coil or located in the electrical compartment. A disconnected plug, damaged sensor lead, or failed sensor reads as either open (infinite resistance) or shorted (near-zero resistance), triggering this fault. The board cannot make defrost timing decisions without a valid outdoor temperature reading.

**7 flashes — Anti-short cycle:**
This is normal protection, not a true fault. After compressor shutdown, the board holds the compressor off for 5 minutes to prevent short-cycling (repeated quick starts that damage motor windings and bearings). Set the thermostat to OFF, wait 5 minutes, and restart. If this fires after every call for cooling/heating, check the refrigerant charge and thermostat differential settings.

## Step-by-Step Fix {#step-by-step-fix}

**Before starting:** Set thermostat to OFF. Flip the outdoor disconnect. Turn off the circuit breaker. Wait 5 minutes for capacitors to discharge before opening the electrical compartment.

1. **Record the flash code before cutting power.** The LED clears when power is removed. Write down the code and the number of times it fired since the last service.

2. **2-flash (high pressure) — clean the coil.** With power off, spray the outdoor coil with a gentle garden hose from the inside out through the top grille. If the coil has heavy buildup, apply Nu-Brite or similar alkaline coil cleaner, let it dwell 5 minutes, then rinse. Also check that vegetation or fencing is not blocking the airflow within 18 inches of the unit sides.

3. **3-flash (low pressure) — test refrigerant pressure.** If you're a licensed technician, connect manifold gauges. On a 70°F day in cooling mode, suction pressure on R-410A should be 120–130 PSIG. A reading below 90 PSIG indicates a leak or significantly low charge. Do not add refrigerant without finding the leak.

4. **Test the run capacitor.** This is the most common repair on any heat pump system over 5 years old. With power OFF and capacitor discharged, test with a capacitor meter. The HERM value must be within 10% of the label rating; the FAN value within 10%. A 45/5 capacitor reading 36/3.5 is failed.

5. **Test the contactor.** With power off, inspect the contact surfaces. They should be smooth and silver-gray. Pitted, blackened, or asymmetrically worn contacts = replace the contactor. This is a $20–$40 repair and is often done as a preventive measure at tune-up.

6. **Check the defrost cycle (heating mode, iced coil).** If the outdoor coil is encased in ice (more than light frost) during heating season, the defrost system is failing. Check:
   - Defrost thermostat: Should close at temperatures below 28°F (test by submerging in ice water — should read continuity).
   - Defrost board relay: Should click when the board initiates a defrost cycle.
   - Reversing valve: Should shift to cooling mode during defrost (you'll feel warm air from the outdoor fan during defrost).

7. **Check outdoor thermistor (6-flash fault).** Unplug the thermistor connector from the board. Use a multimeter on resistance mode — at 70°F (21°C), the NTC thermistor should read approximately 10–12 kΩ. If it reads OL (open) or below 1 kΩ, it's failed. Replacement is a sub-$20 repair.

8. **EcoNet communication fault (8-flash / E1).** Inspect the 4-wire communication cable between the outdoor unit, air handler, and thermostat. Check that it's connected to the correct terminals (follow the label on each board). Replace with a properly rated 18–22 AWG shielded cable if damaged.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| Dual run capacitor — 45/5 µF 440VAC (match label exactly) | $15–$35 | [Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) |
| Contactor — 2-pole, 40A, 24VAC coil | $18–$45 | [Amazon](https://www.amazon.com/dp/B0CJFZQVPT?tag=errorcodefixes-20) |
| Defrost control board (Rheem/Ruud OEM — match model) | $50–$130 | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) |
| Defrost thermostat — coil clip type | $10–$25 | [Amazon](https://www.amazon.com/s?i=industrial&k=defrost+thermostat+heat+pump+coil+clip+on&tag=errorcodefixes-20) |
| Outdoor thermistor sensor (Rheem OEM) | $15–$40 | [Amazon](https://www.amazon.com/s?i=industrial&k=Rheem+outdoor+thermistor+heat+pump+sensor&tag=errorcodefixes-20) |
| Reversing valve solenoid coil — 24VAC (Sporlan or OEM) | $30–$70 | [Amazon](https://www.amazon.com/s?i=industrial&k=reversing+valve+solenoid+coil+24VAC+R410A&tag=errorcodefixes-20) |
| Condenser fan motor — 1/6 HP, 208–230V, match RPM/FLA | $75–$195 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) |

## When to Call a Professional

**DIY-accessible:** Run capacitor, contactor, defrost thermostat, outdoor thermistor — all low-voltage or capacitive components that don't require refrigerant certification.

**Require a licensed HVAC tech:**
- Any fault related to refrigerant charge (3-flash, low pressure) — handling R-410A requires EPA 608 Section 608 certification.
- Compressor overload that repeats after 1 hour cooldown — the compressor winding or refrigerant circuit needs professional diagnosis.
- Reversing valve stuck — reversing valve replacement requires refrigerant recovery and brazing.
- Persistent E1/communication faults after wire inspection — may indicate a failed outdoor control board or air handler board.

> **Field tip:** If you're getting a 2-flash (high pressure) fault only on hot days (above 95°F ambient), and the coil is clean, suspect a refrigerant overcharge. Overcharged systems spike head pressure at high ambient. A technician should recover and recharge to factory spec (weigh-in method, not pressure method).

## See Also

- [Rheem RA13 Air Conditioner Error Codes — Fault Code Guide](/posts/rheem-ra13-error-codes/)
- [Rheem Furnace Error Codes — Complete Reference](/posts/rheem-furnace-error-codes/)
- [Rheem Furnace 3 Flashes — Pressure Switch Fault Fix](/posts/rheem-furnace-3-flashes/)
- [Rheem Furnace 4 Flashes — Open Limit Switch Diagnosis](/posts/rheem-furnace-4-flashes/)
- [Heat Pump Error Code Guide — All Brands](/posts/heat-pump-error-code-guide/)

## Related Articles

- [Rheem Classic Series Furnace Error Codes — Complete Guide](/posts/rheem-classic-furnace-error-codes/)
- [Rheem Air Handler E1 Error Code — Causes & Fix](/posts/rheem-error-code-e1/)
- [Rheem Furnace 2 Flashes — Pressure Switch Fault](/posts/rheem-furnace-2-flashes/)
- [Rheem Furnace 3 Flashes Error Code — Causes & Fix](/posts/rheem-furnace-3-flashes/)
- [Rheem Furnace 4 Flashes — Open High Temperature Limit Fix](/posts/rheem-furnace-4-flashes/)
