---
title: "Lennox iComfort EFO Error Code — Excessive Flame Out and Common iComfort Faults"
author: "Marcus Webb"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
  - thermostat
description: "Lennox iComfort EFO (Excessive Flame Out) error code explained — causes, step-by-step diagnosis, and fixes for EFO and other common iComfort alert codes."
---

## Lennox iComfort EFO Error Code — What It Means

The **EFO (Excessive Flame Out)** alert on a Lennox iComfort S30 or M30 communicating thermostat means the furnace burner lit successfully but lost flame unexpectedly — and this has happened multiple times in a short window. The iComfort system tracks how many times the burner lights and then goes out abnormally. When that count exceeds the threshold (typically 5 flame-out events within a set period), the system escalates from a routine lockout to an EFO alert and shuts down for safety.

EFO is distinct from a simple ignition failure (where the burner never lights). With EFO, the burner does light — but something is snuffing it out before the call for heat is satisfied. That intermittent nature is what makes EFO harder to diagnose than a hard no-light condition.

[Jump to Fix](#fix)

## Common Causes

- **Dirty flame sensor** — The most common cause. The flame sensor rod detects combustion through ionization current. Contamination from condensate residue, dust, or siloxane buildup on the rod reduces the microamp signal below the control board's threshold, causing the board to cut gas even though the flame is present. The burner then relights and the cycle repeats until EFO trips.
- **Improper gas pressure** — Low gas supply pressure or high manifold pressure causes unstable combustion. The flame may lift off the burner or flicker out intermittently under varying demand conditions.
- **Cracked heat exchanger** — A crack in the primary heat exchanger allows supply air to blow across the burner, disrupting the flame. This is a serious safety issue — combustion gases can enter living space.
- **Blocked flue or vent restriction** — A partially blocked vent increases back pressure in the combustion chamber, destabilizing the flame. Nests, ice, or debris at the vent termination are common culprits.
- **Weak igniter** — An igniter that is beginning to fail may light the burner but with a weak, unstable flame that drops out once the igniter cools.
- **Draft inducer motor issue** — If the draft inducer slows down mid-cycle due to a bad bearing or capacitor, the combustion airflow changes and the flame can become unstable.

## Step-by-Step Diagnosis {#fix}

1. **Read the iComfort alert history** — On the S30 or M30, go to Menu > Settings > Advanced Settings > Alerts. Look for the pattern: how many EFO events have occurred, and at what time of day. EFO that always occurs after 10–15 minutes of runtime points toward the heat exchanger or vent. EFO that occurs immediately on every ignition attempt points toward the flame sensor or gas pressure.

2. **Clean the flame sensor first** — This resolves EFO in the majority of cases. Shut off power at the disconnect. Remove the furnace access panel and locate the flame sensor — a single metal rod with a ceramic insulator, positioned in the burner flame path. Remove the one screw holding it, slide it out, and lightly polish the metal rod with fine steel wool or a dollar bill (a non-abrasive option). Do not sand aggressively — you want to remove contamination, not metal. Reinstall and test.

3. **Check gas manifold pressure** — A qualified tech should connect a manometer to the gas valve's manifold pressure port. For natural gas, the typical manifold pressure is 3.5 inches WC; for propane, 10 inches WC. Pressures outside these ranges cause unstable combustion and EFO.

4. **Inspect the vent termination** — Go outside and check the PVC exhaust termination. Clear any obstructions. On cold days, ice can form on the termination cap. Also check that the air intake termination isn't drawing in exhaust gases (short-cycling the combustion air).

5. **Test the draft inducer** — With the furnace running, listen to the inducer motor for changes in pitch or speed during the operating cycle. A motor with a failing bearing will often slow down as it warms up, changing the combustion air volume mid-cycle.

6. **Inspect the heat exchanger** — If EFO occurs 10–20 minutes into a cycle after supply air temperature builds up, suspect the heat exchanger. A cracked exchanger is confirmed with a combustion analyzer, a dollar bill test at supply registers (looking for flutter when the blower turns on), or a qualified inspection with a camera scope.

7. **Reset the alert and monitor** — After cleaning the flame sensor, reset the iComfort (Settings > Advanced Settings > Reset > Equipment Reset). Run a complete heating cycle and watch the heat status screen for flame-out events.

## Other Common Lennox iComfort Error Codes

| Code | Meaning | Quick Fix |
|------|---------|-----------|
| Alert 225 | Outdoor unit communication loss | Check low-voltage wiring between air handler and outdoor unit |
| Alert 31 | Indoor unit communication fault | Verify thermostat wiring at air handler terminal block |
| EFO | Excessive Flame Out | Clean flame sensor; check gas pressure and vent |
| High Limit | Heat exchanger over-temperature | Replace air filter; check blower operation |
| Low Pressure | Refrigerant low pressure fault | Refrigerant charge check by licensed tech |

## Parts You May Need

| Part | Notes |
|------|-------|
| Replacement flame sensor | [Amazon](https://www.amazon.com/s?k=Replacement+flame+sensor&tag=errorcodefixes-20) — Verify part number on the label; common Lennox sensors are 38L73, 10L56 |
| Draft inducer capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-lennox-icomfort-error-codes&tag=errorcodefixes-20) — A failed run capacitor causes the inducer to run slow |
| Draft inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-lennox-icomfort-error-codes&tag=errorcodefixes-20) — Replace when bearings are noisy or motor won't reach full speed |
| iComfort S30 thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lennox-icomfort-error-codes&k=lennox+icomfort+s30+thermostat&tag=errorcodefixes-20) — Replace if the thermostat itself is generating false alerts |

## When to Call a Technician

If cleaning the flame sensor doesn't resolve EFO within 1–2 heating cycles, call a Lennox-certified HVAC technician. Gas pressure measurement requires a manometer and knowledge of the gas train components. A cracked heat exchanger is a carbon monoxide hazard and must be inspected — and the furnace taken out of service — by a licensed professional. Do not continue operating a furnace with confirmed EFO that doesn't respond to the flame sensor cleaning step.

## Related Articles

- [Lennox iComfort Error Code 225 — Communication Fault Fix](/posts/lennox-icomfort-error-code-225/)
- [Lennox iComfort Error Code 31 — Causes & Fix](/posts/lennox-icomfort-error-code-31/)
- [Lennox Elite Series Furnace Error Codes — Complete Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox Error Code 412 — Inducer Fault Fix](/posts/lennox-error-code-412-inducer/)
- [Lennox Error Code 414 — Gas Valve Circuit Fault Fix](/posts/lennox-error-code-414-gas-valve-circuit-fault/)

## See Also

- [Lennox Error Code 540 — Communicating System Fault (Detailed Guide)](/posts/lennox-error-code-540-communicating/)
- [Lennox XP20 Heat Pump Error Codes - Full iComfort Fault Reference](/posts/lennox-xp20-heat-pump-error-codes/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Error Code 540 — Causes & Fix](/posts/lennox-error-code-540/)
