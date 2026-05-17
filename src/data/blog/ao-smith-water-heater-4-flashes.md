---
title: "AO Smith Water Heater 4 Flashes — What It Means and How to Fix It"
description: "AO Smith water heater flashing 4 times indicates an igniter fault or flame sense failure. Learn what causes it, how to test the igniter, and which parts fix it."
pubDatetime: 2026-04-25T12:00:00Z
modDatetime: 2026-04-25T12:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - water-heater
  - ao-smith
  - error-codes
---

AO Smith's 4-flash code points to a problem with the electronic ignition or flame sensing circuit. On power-vent and high-efficiency AO Smith models with electronic spark ignition (no standing pilot), this is the code that fires when the igniter can't prove a flame exists. On standard atmospheric models, 4 flashes typically indicates a problem with the igniter or ignition control module.

[Jump to Fix](#how-to-fix-ao-smith-4-flashes)

## What Does AO Smith 4 Flashes Mean?

Count the blinks on the LED of your gas control valve. Four blinks in a repeating group = fault code 4.

**AO Smith 4 flash code = Igniter Fault / Flame Sense Failure**

This fault fires in these situations:
- The electronic igniter is not sparking
- The igniter is sparking but the flame sensor (flame rod) isn't detecting the burner flame
- The ignition control board has an internal fault
- On power-vent models: the induced draft blower isn't running, preventing ignition from starting

**Difference from 3 flashes:** Code 3 = pilot outage (thermocouple/thermopile issue on standing-pilot models). Code 4 = electronic ignition failure (igniter, flame sensor, or control board on spark-ignition models). Some AO Smith models use code 4 to indicate the thermal cutoff or limit switch has tripped — check your model's label for confirmation.

---

## How to Fix AO Smith 4 Flashes

### Step 1: Reset the Control

Before doing anything else:

1. Turn the gas control knob to **OFF**.
2. Wait 30 seconds.
3. Turn back to **PILOT** and attempt a normal light.
4. If the unit fires up and the fault clears, it may have been a one-time ignition failure — monitor for recurrence.

### Step 2: Check the Thermal Cutoff (TCO)

Many AO Smith models use a Thermal Cutoff (TCO) device — a one-shot safety fuse that trips if the flue area overheats. Once it trips, the heater won't fire until it's replaced.

1. Locate the TCO — typically a white or yellow disc-shaped device on the flue or near the top of the tank, with two wires.
2. Use a multimeter set to continuity or resistance.
3. Disconnect the two TCO wires and test across the terminals.
4. **Open circuit (no continuity)** = the TCO has blown — replace it.
5. TCOs are rated by temperature; match the rating on the original (typically 190°F / 88°C for residential units).

### Step 3: Inspect the Igniter

On models with electronic spark ignition:

1. Remove the burner access panel (typically two screws and a lift-off panel).
2. Visually inspect the igniter tip — look for cracking, heavy carbon buildup, or a broken electrode.
3. Check the igniter gap: should be approximately **0.1–0.15 inches** (3–4 mm) between the electrode tip and the burner.
4. Clean carbon buildup from the electrode tip with fine sandpaper or a wire brush — gently.
5. If the electrode is cracked or the igniter doesn't spark when triggered, replace it.

### Step 4: Test the Flame Sensor / Flame Rod

On spark-ignition AO Smith models, a flame rod sits in the burner flame to prove combustion. A dirty or faulty flame rod causes 4 flashes even when the burner is firing.

1. Locate the flame rod — it's a metal rod extending into the burner area, separate from the igniter electrode.
2. Turn off gas and power to the unit.
3. Remove the flame rod (one screw) and clean the rod with steel wool or fine sandpaper. Oxidation on the rod surface is the most common cause of flame sense failure.
4. Reinstall and test.
5. If cleaning doesn't fix it, test the flame rod signal. With the burner running and the flame rod connected, you should see **1–5 microamps DC** at the rod's wire connection to the control board. Below 1 µA = replace the rod.

### Step 5: Check the Blower Motor (Power-Vent Models)

On AO Smith ProLine Power Vent and Vertex models, the draft inducer blower must be running before ignition can start. Code 4 can fire if the blower fails.

1. Listen for the blower motor running when the unit calls for heat.
2. If silent, check the blower wiring harness connection.
3. Spin the blower wheel by hand — if it drags or won't spin freely, the motor bearing is seized.
4. Test voltage at the blower motor terminals with a multimeter: should match the motor's rated voltage (typically 120V AC for power-vent models).
5. No voltage with a call for heat = control board output fault. Full rated voltage but no spin = blower motor failed.

### Step 6: Replace the Ignition Control Board

If the igniter, flame sensor, and blower are all working but 4 flashes persists:

1. Document the existing wiring before disconnecting anything (photo works).
2. Match the board to your model number — AO Smith service boards are model-specific.
3. The board is typically in an access panel on the side or top of the unit.
4. Swap the board, reconnect all wiring per your photos, and test.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|--------------|
| [Thermal Cutoff (TCO)](https://www.amazon.com/s?i=industrial&k=Thermal+Cutoff+%28TCO%29&tag=errorcodefixes-20) | Blown safety fuse — no continuity on test | $10–$25 |
| [Spark Igniter / Electrode](https://www.amazon.com/s?i=industrial&k=Spark+Igniter+%2F+Electrode&tag=errorcodefixes-20) | Cracked, corroded, or won't spark | $20–$45 |
| [Flame Sensor / Flame Rod](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) | Oxidized or failed — burner runs but code persists | $15–$35 |
| [Blower Motor (power-vent)](https://www.amazon.com/s?i=industrial&k=Blower+Motor+%28power-vent%29&tag=errorcodefixes-20) | Seized, dragging, or no rotation | $70–$150 |
| [Ignition Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | All sensors good but fault persists | $80–$180 |
| [Gas Control Valve](https://www.amazon.com/s?i=industrial&k=Gas+Control+Valve&tag=errorcodefixes-20) | Valve internal fault (only after above ruled out) | $90–$160 |

*AO Smith part numbers vary by model. Pull your model number from the label on the side of the tank (format: GPS6-50T40-NV) and verify part numbers at aosmithpartsplus.com or your local plumbing supply.*

---

## When to Call a Pro

- You smell gas at any point — leave and call the gas company
- The TCO has blown more than once — repeated tripping means the root cause (overheating, blocked flue) hasn't been fixed
- You're replacing the gas control valve and aren't comfortable with gas line work
- The blower motor tests bad on a power-vent unit — blower replacement requires draining the combustion circuit and can be complex on ceiling-mounted configurations
- Your water heater is over 10 years old and facing a second major repair — a new unit may be more cost-effective

---

## Frequently Asked Questions

**Is AO Smith 4 flashes the same as 3 flashes?**
No. Three flashes is a pilot outage — the standing pilot flame went out or the thermocouple/thermopile failed. Four flashes is an igniter or flame sense fault on electronic ignition models, or a thermal cutoff fault on some standard models. Check the diagnostic label on your unit's access panel to confirm what code 4 means on your specific model.

**Can I reset an AO Smith 4-flash code without parts?**
Sometimes. Turn the gas control to OFF, wait 30 seconds, and retry. If the fault comes back immediately and consistently, parts replacement is needed. One-time 4-flash codes after a power outage are usually not a sign of hardware failure.

**How do I tell if my AO Smith has a standing pilot or electronic ignition?**
Look at the gas valve — if there's a red or black piezo push-button igniter and a pilot light you light manually, it's standing pilot. If there's no manual igniter button and the unit has a power cord, it uses electronic ignition. Electronic ignition models are more common on power-vent and high-efficiency units made after 2010.

**My AO Smith is 12 years old and showing 4 flashes — should I repair or replace?**
At 12 years, a residential water heater is near end of life (typical lifespan is 10–15 years). If the repair requires a control board ($80–$180) or blower motor ($70–$150), compare that to the cost of a new unit. If the tank itself is showing rust or the anode rod has never been replaced, replacement is usually the better value.

**Why does my AO Smith show 4 flashes right after installation?**
On new or recently installed units, 4 flashes often means air in the gas line. Open a gas appliance nearby to purge air, then retry lighting. Also confirm the gas shutoff valve is fully open — a partially closed valve restricts gas flow enough to prevent ignition but not enough to be immediately obvious.

## Related Articles

- [A.O. Smith Water Heater E1 Error Code — Sensor Fault Guide](/posts/ao-smith-error-code-e1/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
