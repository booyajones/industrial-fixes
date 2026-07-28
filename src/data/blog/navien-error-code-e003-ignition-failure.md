---
title: "Navien Error Code E003 — Ignition Failure Fix"
author: "James Rutherford"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: navien-error-code-e003-ignition-failure
featured: false
draft: false
tags:
  - boiler
  - navien
  - tankless
  - heating
description: "Navien error code E003 means ignition failure on NPE, NPN, and NCB series tankless water heaters and combi boilers — here's how to diagnose and fix it."
---

## Error Code: Navien Error Code E003

**What it means:** Error code E003 on Navien NPE series tankless water heaters, NPN series non-condensing water heaters, and NCB/NFC series combi boilers indicates an ignition failure. The control board initiated a call for heat, opened the gas valve, and energized the igniter, but failed to detect a stable flame signal within the designated trial-for-ignition period. After several failed attempts, the unit locks out and displays E003.

This is the most common fault code on Navien's extensive line of residential and commercial tankless heaters and boilers, which have a massive install base. The causes range from simple maintenance issues to component failures.

## Common Causes

- **Dirty or failed flame sensor** — Condensate and combustion byproducts can foul the flame sensor rod, preventing it from sending a clear microamp signal back to the control board. This is the #1 cause of E003 faults.
- **Gas supply or pressure issue** — An improperly sized gas line, low gas pressure, a closed manual shutoff valve, or a stuck gas utility meter can starve the unit for fuel. Navien units are very sensitive to gas pressure and require a specific dynamic pressure during operation.
- **Cracked or failed igniter** — The hot surface igniter has developed a hairline crack, causing its resistance to increase and preventing it from reaching the temperature required for ignition.
- **Blocked condensate drain** — On NPE and NCB/NFC condensing units, a clogged condensate trap can cause water to back up into the combustion chamber, interfering with ignition.
- **Improper vent termination or length** — Navien units have strict venting requirements. An excessively long vent run, incorrect vent termination (e.g., too close to a wall or under a deck), or a blocked vent can cause combustion instability and ignition failures.
- **Failed gas valve** — The internal solenoid on the gas valve has failed, preventing gas from flowing to the burner.
- **Incorrect DIP switch settings** — After installation or a board replacement, the DIP switches that configure the unit for natural gas vs. propane, or for high-altitude operation, may be set incorrectly.

## Step-by-Step Fix {#step-by-step-fix}

1. **Reset the unit and observe the ignition sequence.** Press the power button to turn the unit off, wait 30 seconds, and turn it back on. Initiate a call for hot water. Listen and watch: you should hear the combustion fan start, then the spark or glow of the igniter, followed by the "whoosh" of the burner lighting. If you hear a click but no whoosh, suspect a gas valve or supply issue. If you see no spark/glow, suspect the igniter.

2. **Check gas supply.** Ensure the manual gas valve on the line feeding the Navien is fully open. If you have other gas appliances, check if they are operating normally. A qualified technician should connect a manometer to the gas valve's inlet and outlet ports to verify both static and dynamic gas pressure against the unit's rating plate.

3. **Inspect and clean the flame sensor.** The flame sensor is a metal rod located opposite the igniter in the burner assembly. Turn off power and gas to the unit. Remove the front cover. The sensor is held by one screw. Remove it and clean the rod with fine steel wool or emery cloth until shiny. Reinstall and test.

4. **Test the igniter.** Disconnect the igniter's wiring harness. For spark igniters, check for a clean, uncracked ceramic insulator and a sharp electrode tip. For hot surface igniters (found on some models), measure resistance with a multimeter. A typical Navien hot surface igniter (Part. No. BH2040180A) should read between 80-120 ohms when cold. An open circuit (OL) indicates a failed igniter.

5. **Inspect the condensate trap.** On condensing models, locate the clear plastic condensate trap at the bottom of the unit. If it's full of water or debris, it needs to be cleaned. Unscrew the trap, empty it, and rinse it thoroughly. Ensure the drain line is not frozen or blocked.

6. **Check the vent termination.** Go outside and inspect the PVC vent pipes. Ensure they are free of obstructions like nests, leaves, or snow. Check that the termination fittings are installed correctly per the Navien installation manual.

7. **Verify DIP switch settings.** On the main control board, there is a block of small DIP switches. Consult the installation manual for your specific model to ensure the switches for gas type (NG/LP) and altitude are set correctly for your installation. Incorrect settings will cause poor combustion and lead to E003.

8. **Replace failed components.** If the flame sensor is pitted or cleaning doesn't help, replace it. If the igniter is cracked or measures out of spec, replace it. These are the two most common parts to fail.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Navien Igniter (NPE-A/S) | BH2040180A | $50–$65 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-navien-error-code-e003-ignition-failure&k=BH2040180A+Navien+Igniter+%28NPE-A%2FS%29&tag=errorcodefixes-20) \| SupplyHouse / Amazon |
| Navien Flame Sensor (Rod) | 30010972A | $25–$40 | [Amazon](https://www.amazon.com/s?k=Navien+Flame+Sensor+%28Rod%29&tag=errorcodefixes-20) \| SupplyHouse / Amazon |
| Navien Gas Valve (NPE-A/S) | BH1680178A | $170–$200 | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-navien-error-code-e003-ignition-failure&tag=errorcodefixes-20) \| SupplyHouse / Navien Parts |
| Navien Condensate Trap | 30011532A | $15–$25 | [Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-navien-error-code-e003-ignition-failure&tag=errorcodefixes-20) \| SupplyHouse |
## When to Call a Professional

Diagnosing gas pressure issues requires a manometer and experience. Any work involving disconnecting the gas line, including replacing the gas valve, must be performed by a licensed plumber or HVAC technician. Additionally, after any repair that affects combustion, a Navien boiler or water heater should have its combustion performance checked with a calibrated combustion analyzer to ensure CO levels are safe and the unit is operating at peak efficiency. If you've cleaned the flame sensor and checked for obvious blockages and the E003 code persists, it's time to call a Navien-certified technician.

> **Pro tip:** Navien E003 faults that occur intermittently, especially on windy days, are almost always related to improper vent termination. The wind can create pressure fluctuations in the vent system that snuff out the flame during ignition. Ensure the vent termination is located away from prevailing winds and has the proper clearance as specified in the installation manual. Many intermittent E003 calls are resolved by simply correcting the venting.
