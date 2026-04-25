---
title: "Bryant Furnace 31 Error Code — Pressure Switch Open"
description: "What the Bryant furnace 31 error code means, why the pressure switch fault triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - bryant
---

## Bryant Furnace 31 Error Code — What It Means

Bryant furnaces share engineering with Carrier (both are UTC/Carrier brands), so error code 31 carries the same meaning across both: the pressure switch failed to close — or opened unexpectedly — during the inducer startup sequence. The control board starts the inducer draft motor, waits for the pressure switch to confirm adequate negative pressure, and proceeds to ignition. If the switch doesn't close within the trial window, the board halts, logs fault 31, and blinks the status LED 31 times. This is a safety interlock to ensure combustion gases are being properly vented before gas is introduced.

[Jump to Fix](#fix)

## Common Causes

- **Blocked condensate drain** — High-efficiency Bryant furnaces (90%+ AFUE) produce significant condensate. A clogged drain trap creates back-pressure on the pressure switch port and prevents the switch from detecting the correct differential.
- **Cracked pressure switch hose** — The small rubber hose connecting the pressure switch to the inducer housing ages and cracks. A crack allows ambient air to leak in, preventing the necessary vacuum from forming at the switch.
- **Failed inducer draft motor** — A worn motor bearing or a failed run capacitor slows the inducer, reducing the negative pressure it creates. The pressure switch never sees enough differential to close.
- **Blocked flue pipe or intake** — Snow, ice, bird nests, or debris at the exterior PVC terminations restricts airflow through the inducer and collapses the pressure differential needed to close the switch.
- **Faulty pressure switch** — The diaphragm inside the switch can rupture, or the switch contacts can fail. A failed switch produces a persistent 31 code even with a healthy inducer and clear venting.

## Step-by-Step Fix {#fix}

1. **Check the condensate drain** — Locate the condensate drain outlet (typically clear tubing exiting at the furnace base or going to a floor drain). Pour a cup of water into the condensate trap and confirm it flows freely out the drain. If it backs up, clear the blockage with a wet/dry vac.
2. **Inspect exterior pipe terminations** — Go outside and check both the exhaust and intake PVC pipes. Clear any debris, ice, or obstruction. Verify the pipes are not kinked or sagging.
3. **Inspect the pressure switch hoses** — Disconnect power to the furnace. Trace the rubber hoses from the pressure switch ports to the inducer housing. Squeeze the hoses along their length — cracks will open. Replace any hose that feels stiff, brittle, or shows visible cracking.
4. **Test the pressure switch** — With the furnace powered and a call for heat, use a multimeter to check continuity across the pressure switch terminals during inducer operation. The switch should close (show continuity) once the inducer is at speed. If it doesn't close, apply vacuum with a hand pump and verify it closes at the rated setpoint (printed on the switch body).
5. **Test the inducer motor** — Listen to the inducer during startup. A slow, labored, or grinding motor needs its capacitor tested first (most failures are capacitor-related, not motor-related). A good capacitor reads within 10% of its rated µF value.
6. **Replace the pressure switch** — If inducer speed is correct and hoses are intact, replace the pressure switch. Match the setpoint stamped on the switch body.
7. **Reset and verify** — Cycle the furnace through a complete heating sequence and confirm 31 does not recur.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Pressure switch | [Amazon](https://www.amazon.com/s?k=Pressure+switch&tag=errorcodefixes-20) \| Match the setpoint — Bryant uses both single and dual switches depending on model |
| Inducer draft motor capacitor | [Amazon](https://www.amazon.com/s?k=Inducer+draft+motor+capacitor&tag=errorcodefixes-20) \| Test before replacing the motor — most motor failures are actually capacitor failures |
| Inducer draft motor assembly | [Amazon](https://www.amazon.com/s?k=Inducer+draft+motor+assembly&tag=errorcodefixes-20) \| Replace if motor is noisy, slow, or seized with a good capacitor |
| Condensate trap | [Amazon](https://www.amazon.com/s?k=Condensate+trap&tag=errorcodefixes-20) \| Replace if cracked or if the internal float is stuck |
| Pressure switch tubing | [Amazon](https://www.amazon.com/s?k=Pressure+switch+tubing&tag=errorcodefixes-20) \| Available by the foot at HVAC supply houses |
## When to Call a Pro

A persistent 31 after replacing the pressure switch and confirming inducer speed may indicate a cracked heat exchanger, which creates secondary pressure imbalances in the inducer path. A cracked heat exchanger is a serious safety concern — have a licensed HVAC technician perform a combustion analysis before returning the furnace to service.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
