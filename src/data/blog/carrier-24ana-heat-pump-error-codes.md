---
title: "Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide"
description: "Carrier 24ANA heat pump error codes: LED flash sequences, fault causes, step-by-step fixes, and OEM parts guide for the Carrier Performance 15 heat pump."
pubDatetime: 2026-04-24T08:00:00Z
modDatetime: 2026-04-24T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - heat-pump
  - error-codes
  - diagnostics
---

## Carrier 24ANA Heat Pump Error Codes — What They Mean

The Carrier 24ANA (Performance 15 and Performance 16 heat pump series — model variants include 24ANA1, 24ANA6, 24ANB1, 24ANB6) is one of the most widely installed residential heat pumps in North America. It is a single-stage heat pump using R-410A refrigerant and a Copeland scroll compressor, rated at 15–16 SEER.

The 24ANA is a **non-communicating** unit — it does not use the Carrier Infinity SAB bus. It operates with a standard 24VAC thermostat (Y, G, O/B, C, R terminals) and communicates faults via **LED blink codes** on the outdoor control board.

To read the codes: open the electrical access panel on the lower-right side of the outdoor unit (2 screws). The status LED is on the main control board. Blink codes repeat in a pattern — count the flashes, note the pause, then count again. If you have an Infinity or Evolution thermostat connected, error codes display alphanumerically on the thermostat and are also covered in the Infinity System Error Codes guide.

### 24ANA LED Blink Code Reference

| Blinks | Fault Description | Response |
|--------|------------------|---------|
| 1 flash | System standby — no fault present | Normal |
| 2 flashes | High-pressure switch open | Compressor off |
| 3 flashes | Low-pressure switch open | Compressor off |
| 4 flashes | Compressor protection device (klixon) open | Compressor off |
| 5 flashes | Control board fault | Full lockout |
| 6 flashes | Outdoor ambient thermistor fault | Defrost disabled |
| 7 flashes | Anti-short cycle delay (5 minutes) | Temporary hold |
| 8 flashes | Low voltage — board supply below 18VAC | Compressor off |
| Rapid continuous | Control board fault or brownout | Unit off |

### Codes When Paired with Infinity/Evolution Thermostat

If the 24ANA is wired to a Carrier Infinity thermostat (non-SAB wired connection), the thermostat may display E-series codes based on the thermostat's own diagnostic logic:

| Code | Description |
|------|------------|
| E1 | Indoor/outdoor communication fault |
| E4 | Outdoor coil thermistor fault |
| E5 | High pressure protection |
| E6 | Low pressure protection |

See Carrier Heat Pump E1 Error Code and Carrier Heat Pump E4 Error Code for full diagnosis of those codes.

## Common Causes by Code

**2 flashes — High pressure:**
On the 24ANA, high-pressure trips almost always trace to one of three causes: (1) dirty condenser coil, (2) failed outdoor fan capacitor or motor, or (3) refrigerant overcharge. The 24ANA uses a spine-fin or aluminum slab condenser coil — the spine-fin variant can trap cottonwood and grass on the interior side of the coil where it's not visible from outside. Head pressure above 400–420 PSIG on R-410A trips the high-pressure cutout.

**3 flashes — Low pressure:**
The low-pressure switch trips below 50–55 PSIG on R-410A. Causes: refrigerant leak, extremely low ambient temperatures without a low-ambient kit, or a defrost cycle failure in heating mode that allows outdoor coil ice accumulation to restrict refrigerant flow. A clogged indoor filter or dirty evaporator coil can also drop suction pressure enough to trigger low-pressure during cooling.

**4 flashes — Compressor protection (klixon):**
The internal klixon thermal overload in the Copeland scroll compressor trips when the compressor overheats. After shutdown, the klixon resets in 20–45 minutes as the compressor cools. Causes: high ambient temperature with restricted airflow (dirty coil + failed fan), liquid refrigerant flooding the compressor (operating in very cold weather without a crankcase heater), or a beginning-of-life compressor failure.

**6 flashes — Thermistor fault:**
The outdoor ambient thermistor tells the defrost board the outdoor temperature for defrost timing decisions. A failed or disconnected thermistor disables defrost scheduling, which leads to outdoor coil ice buildup during heating season. The 24ANA's thermistor is an NTC type — at 70°F it reads approximately 10 kΩ.

**7 flashes — Anti-short cycle:**
This is normal protective behavior, not a fault. After compressor shutdown, the board enforces a 5-minute off period. This prevents back-to-back rapid starts that damage the compressor. Set the thermostat to OFF, wait 6 minutes, then restart. If the 7-flash occurs every cycle, check thermostat differential settings and refrigerant charge.

## Step-by-Step Fix {#step-by-step-fix}

**Safety:** Turn the thermostat to OFF. Flip the outdoor disconnect (located near the unit). Turn off the indoor air handler or furnace circuit breaker. Wait 5 minutes before opening the electrical compartment.

1. **Log the blink code.** Open the electrical access panel on the outdoor unit. Note the LED blink pattern carefully — it clears when power is cut. Photograph the board label (serial/model sticker) for parts reference.

2. **2-flash (high pressure) — clean the coil.** Inspect the coil from all sides. On the 24ANA spine-fin coil, debris collects on the inside face of the lower coil panels. With power off, gently rinse with a garden hose from inside out through the top. Do NOT use a pressure washer — the spine-fin coil is fragile. Also spin the fan blade by hand — it should spin freely. A bearing-seized fan shows up as dragging or grinding.

3. **Test the outdoor fan capacitor (for 2-flash).** The 24ANA typically uses a dual-run capacitor rated 35/5 or 45/5 µF at 370 or 440VAC. Discharge the capacitor, then test with a capacitor meter. Values must be within 10% of label rating. A 45/5 capacitor reading 37/4.2 may still look "close" but it's failed — replace it.

4. **Test the contactor.** With power off, inspect the contact pad surfaces. Fresh contacts are smooth and silver; failed contacts show pitting, burning, or melted edges. The 24ANA contactor is a 2-pole 40A unit. Replacement is a $20–$45 DIY job.

5. **3-flash (low pressure) — check filter and evaporator.** Replace the indoor air filter. If the filter is fresh and the fault persists, inspect the indoor evaporator coil for ice — if it's frozen, the problem is airflow or low refrigerant charge. Turn the system to FAN ONLY for 30 minutes to thaw the coil, then restart.

6. **Check the defrost system (heating mode only).** If the outdoor coil has heavy ice buildup (not just light frost) and the unit runs in heating mode without defrosting every 30–90 minutes, the defrost board or thermostat is failed. Initiate a test defrost by shorting the TEST pins on the defrost board for 2–3 seconds — the unit should shift to defrost mode (outdoor fan stops, indoor fan continues, reversing valve shifts). If it doesn't respond, the defrost board is failed.

7. **6-flash (thermistor) — test the sensor.** Unplug the thermistor connector from the control board. At 70°F, the sensor should read 10–12 kΩ on a multimeter set to resistance. An OL reading = open circuit (failed), near-zero = short circuit (failed). Thermistor replacement is a $15–$30 repair.

8. **Persistent 2-flash or 3-flash after coil/filter/capacitor checked:** At this point, suspect refrigerant charge. Connect manifold gauges (requires EPA 608 certification). On R-410A at 70°F, cooling mode suction should be approximately 120–130 PSIG. Low charge = add refrigerant after locating and repairing the leak. High charge (causing 2-flash) = recover refrigerant to proper charge by weight.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| Dual run capacitor — 35/5 or 45/5 µF 370/440VAC | $15–$35 | [View on Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-24ana-heat-pump-error-codes&tag=errorcodefixes-20) |
| Contactor — 2-pole, 40A, 24VAC coil | $20–$45 | [View on Amazon](https://www.amazon.com/dp/B0CJFZQVPT?ascsubtag=ecf-carrier-24ana-heat-pump-error-codes&tag=errorcodefixes-20) |
| Defrost control board (Carrier OEM #HH12ZB271 or match) | $50–$130 | [Amazon](https://www.amazon.com/s?k=Defrost+control+board+%28Carrier+OEM+%23HH12ZB271+or+match%29&tag=errorcodefixes-20) |
| Outdoor thermistor / ambient sensor (Carrier OEM) | $15–$40 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-24ana-heat-pump-error-codes&k=Carrier+outdoor+thermistor+ambient+sensor+heat+pump&tag=errorcodefixes-20) |
| Reversing valve solenoid coil — 24VAC | $30–$70 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-24ana-heat-pump-error-codes&k=reversing+valve+solenoid+coil+24VAC+carrier+heat+pump&tag=errorcodefixes-20) |
| Condenser fan motor — 1/5 HP, 208–230V (match specs on nameplate) | $85–$200 | [View on Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-24ana-heat-pump-error-codes&tag=errorcodefixes-20) |
| 24ANA outdoor control board (Carrier OEM — match model #) | $80–$185 | [Amazon](https://www.amazon.com/s?k=24ANA+outdoor+control+board+%28Carrier+OEM+%E2%80%94+match+model+%23%29&tag=errorcodefixes-20) |

## When to Call a Professional

**DIY-accessible on the 24ANA:** Run capacitor, contactor, defrost thermostat, outdoor thermistor, coil cleaning. These components are accessible without refrigerant handling and are the most common failure points.

**Call a licensed HVAC technician for:**
- 3-flash (low pressure) that returns after filter change and coil cleaning — refrigerant leak or charge issue requires EPA certification.
- 2-flash (high pressure) that returns after a clean coil and good capacitor test — possible refrigerant overcharge or TXV failure.
- 4-flash (compressor protection) that returns within an hour — compressor winding failure or liquid flood-back requires professional diagnosis.
- Reversing valve stuck in one mode — you'll know this is the issue if the heat pump cools when heating is commanded, or vice versa. Valve replacement requires brazing.

> **Homeowner quick test:** If you suspect a reversing valve fault — set the thermostat to HEAT. Go outside and put your hand in front of the outdoor fan. In heating mode, the outdoor unit should blow **cool air** out the top (it's extracting heat from outside air). If it blows warm air in heating mode, the reversing valve is stuck in cooling position and needs attention.
