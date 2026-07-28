---
title: "Bryant Evolution Code 21 — Gas Heating Lockout Fix"
description: "Bryant Evolution code 21 is a gas heating lockout — the integrated furnace control attempted ignition three times in a row, failed to prove flame each time,..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: bryant-error-code-21
featured: false
draft: false
tags:
  - bryant
  - hvac
  - error-codes
  - gas-heating-lockout
---
## Quick answer

Bryant Evolution code 21 is a gas heating lockout — the integrated furnace control attempted ignition three times in a row, failed to prove flame each time, and has locked out gas heating for one hour. About 60% of these in the field are flame sensor problems (carbon-coated rod, bent away from the flame, or wire chafed against the burner box), not gas supply or igniter problems. Pull the sensor, wipe it with fine emery cloth, and reset before you order any other parts.

## What code 21 means on a Bryant

The Bryant Evolution, Preferred, and Legacy gas furnace lines share the same Carrier-built integrated furnace control (IFC) chassis — HK42FZ-series boards with Bryant HK-prefix stickers in place of Carrier's HC-prefix. Code 21 is signaled with two slow flashes, a pause, then one fast flash on the diagnostic LED behind the lower door. Evolution thermostats with the color touchscreen show "Code 21 — Gas Heating Lockout" in the service alerts menu.

The ignition sequence: thermostat call → inducer pre-purge → pressure switch closes → hot surface igniter (HSI) energizes for 30-45 seconds of warmup → board energizes gas valve → flame establishes on burner #1 and carries across the burners → flame sensor (a single ceramic-insulated rod inserted into the flame envelope of burner #1) generates a microamp current via flame rectification → board reads the current and proves flame.

Code 21 fires when the board completes three full trial-for-ignition sequences but cannot prove flame within the trial window (typically 7-10 seconds after the gas valve opens). After the third failure the gas valve is locked closed for one hour or until 24V power is cycled. The board is being deliberately conservative — three failed trials with gas flowing means burner gas could be accumulating in the heat exchanger, and another trial without proof of flame could ignite a larger volume of gas at once.

The flame rectification signal is a low-amperage DC current (typically 1-6 microamps for a healthy Bryant burner) measured across the flame between the sensor rod and the burner ground. The signal works because flame ionization acts as a one-way conductor — DC passes from rod to ground through the flame, AC does not. A clean sensor in a hot blue flame gives 4-6 µA; a dirty sensor reads 0.5-1.5 µA and the board often rejects the reading.

## Common causes (ranked by frequency)

In residential service experience, code 21 distributes like this:

1. **Carbon-coated flame sensor** — about 50%. Months of cycling deposit a thin oxide layer that insulates the rod from the flame ions.
2. **Flame sensor bent out of the flame envelope** — about 12%. Vibration, prior service, or aggressive cleaning bent the rod so it's only catching the edge of the flame.
3. **Failed hot surface igniter** — about 12%. The HSI glows but doesn't reach ignition temperature, or it's cracked and the burner gas escapes before lighting.
4. **Low gas supply pressure** — about 8%. Inlet pressure below 5 inches WC at the gas valve inlet, often from a meter regulator failure or a tankless water heater drawing on the same line.
5. **Failed gas valve** — about 7%. Valve doesn't fully open, gas flow is below minimum for ignition.
6. **Cracked or contaminated burners** — about 6%. The burner ports near the flame sensor are partially blocked.
7. **Wiring or ground fault on the flame sensor lead** — about 3%. The single white wire from the sensor to the board has chafed against the burner box or lost continuity.
8. **Control board fault** — about 2%. The flame-sensing input on the IFC has failed.

**Pro nugget:** Bryant flame sensors carry HK-prefix part numbers but are physically identical to Carrier HC-prefix sensors of the same era. The trick: when you order a replacement, the **bracket dimensions** are what matter, not the brand. A Bryant Evolution 80% AFUE single-stage uses a 4.5-inch-overall flame sensor with a 1.625-inch insertion depth (HK06WB003). An Evolution 90% AFUE two-stage uses a 5.25-inch sensor with a 2-inch insertion depth (HK06WB006). Mixing these up means the rod ends up too short to reach flame or too long and grounding against the burner — either way you get code 21.

## Step-by-step fix

Before you start: shut off power at the furnace switch and gas at the gas cock. Wait 5 minutes for everything to cool. Verify zero gas at the burner inlet with a manometer if you're going to remove the burner assembly.

1. **Confirm the code and review the history.** Read the LED through one cycle to verify code 21. On an Evolution thermostat, pull the last 10 fault history events. If code 21 is preceded by code 13 (limit lockout) or code 25 (gas valve fault), the diagnostic path changes.

2. **Pull the flame sensor.** Remove the single screw holding the sensor to the burner box, slide the sensor out, then unplug the single white wire on the back. The sensor is a ceramic-insulated rod about 4-6 inches long with one threaded ground tab and one terminal.

3. **Clean the sensor.** Wipe the rod with fine-grit emery cloth (400-grit or finer — do **not** use sandpaper, steel wool, or a wire brush, all of which leave residue that contaminates flame rectification). Wipe gently — you want to remove the oxide layer, not abrade the rod itself. A clean rod looks like uniform dull stainless steel; a fouled rod has visible black or rust-orange patches.

4. **Inspect the wire.** Trace the white flame-sense wire from the sensor terminal back to the board. Look for chafing where it routes around the burner box, the inducer, or the gas valve. A pinhole through the insulation to a grounded surface kills flame rectification.

5. **Reinstall and check positioning.** The sensor rod should sit in the flame envelope of the leftmost burner (burner #1, the carry-over burner that lights first), about 3/8 inch from the burner port, with the rod parallel to the burner crown. If it's bent down into the burner crown or angled up out of the flame, gently re-form it with needle-nose pliers.

6. **Test with a microamp meter.** With the burners running, place a true-RMS DC microamp meter in series between the sensor and the board (pull the white wire off the sensor, put one probe on the sensor, the other probe on the wire). A healthy reading on a Bryant burner is 4-6 µA. Anything below 1.5 µA and the board will reject the signal — pull the sensor and re-clean, or replace it.

7. **Verify gas pressure.** With a manometer tee'd into the inlet of the gas valve (test port on the valve body), the inlet pressure on natural gas should be 5-7 inches WC standing and 4.5-5.5 inches WC during firing. Below 4 inches and the board cannot establish stable flame. The outlet pressure (manifold pressure) should be 3.2-3.5 inches WC on natural gas, set per the unit's nameplate.

8. **Reset and observe.** Cycle 24V to clear the lockout. Watch a full ignition: HSI glows orange-white (good — about 2400°F), gas valve clicks open, flames roll across all burners within 1-2 seconds, sensor proves flame within 4 seconds, no code 21 fault. If the HSI doesn't glow white-hot, replace it (HSIs degrade slowly and eventually can't ignite gas).

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Flame sensor (80% AFUE single stage) | Bryant HK06WB003 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21), [Amazon](https://www.amazon.com) |
| Flame sensor (90% AFUE two stage) | Bryant HK06WB006 | $30-50 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21), [Amazon](https://www.amazon.com) |
| Hot surface igniter (silicon nitride) | Bryant LH33ZS006 | $55-85 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21) |
| Gas valve (24V natural gas, single stage) | Bryant EF32CW182 / Honeywell VR8205 | $185-265 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21), [Amazon](https://www.amazon.com) |
| Gas valve (24V natural gas, two stage) | Bryant EF32CW190 / Honeywell VR9205 | $245-340 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21) |
| Integrated furnace control | Bryant HK42FZ035 | $235-340 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=bryant-error-code-21) |
| Microamp DC meter | Fieldpiece SC480 | $145-185 | [Amazon](https://www.amazon.com) |

The Bryant HK-prefix gas valves are Honeywell VR8205/VR9205-series gas valves with a Bryant sticker — if your supply house only stocks the Honeywell direct part, it drops in without modification and saves you 20-30%.

## When to call a professional

Call a licensed HVAC tech for:

- Persistent code 21 after sensor cleaning, HSI replacement, and verified gas pressure. The next step is a combustion analysis with a CO probe and verification of manifold pressure under firing load — both require a tech with calibrated instruments.
- Any indication of delayed ignition (a "whoosh" or "thump" when the burners light). This is a dangerous condition that can crack the heat exchanger and demands immediate service shutdown.
- Replacement of the gas valve. In most jurisdictions, gas valve work requires a licensed gas fitter or HVAC tech with gas credentials. The work involves leak-testing with soap solution or electronic gas detector after install — not something to skip.
- Bryant warranty repairs. Evolution series carries 10-year parts with registration; non-licensed work voids it.

## FAQs

**The sensor looked clean. Why is it tripping code 21?**
Flame sensor oxide is sometimes invisible to the eye — a thin oxide layer can insulate enough to kill the microamp signal without showing a visible coating. Always wipe with emery cloth even if it "looks fine," and always verify with a microamp meter after install.

**Can I substitute a generic universal flame sensor?**
Universal sensors work in a pinch but the bracket geometry rarely fits a Bryant cabinet correctly. The OEM HK-prefix sensors are not expensive ($25-50) — order the exact part.

**My HSI glows but the burners don't light. Code 21 trips. What's wrong?**
Either the HSI isn't reaching ignition temperature (silicon-nitride igniters degrade gradually — replace if it's over 5 years old), or you have low gas pressure. Check inlet pressure first with a manometer.

**Will turning the gas valve manifold pressure up fix code 21?**
Almost never — and it's dangerous. Manifold pressure is factory-set to the unit's nameplate spec (3.2-3.5 inches WC on natural gas, 10-11 on propane). Turning it up over-fires the unit, overheats the heat exchanger, and trips code 13. Leave the manifold pressure alone unless you have a combustion analyzer and certification.

**Code 21 only happens on cold mornings. Why?**
Two possibilities: cold start gas pressure is marginal (the regulator can't keep up with the inrush), or the flame sensor is right at the edge of useable signal at room temperature and gets worse in cold burner conditions. Replace the sensor first; if it still happens, get a tech to verify gas pressure under load on a cold morning.

## Related guides

- Carrier 33 Error Code — Limit Circuit Fault Fix
- [Bryant Error Code 13 — Limit Lockout Fix](/posts/bryant-error-code-13)
- [Payne Error Code 31 — Pressure Switch Fix](/posts/payne-error-code-31)
