---
title: "Westinghouse Furnace E1 Error Code — Causes & Fix"
description: "What Westinghouse furnace error code E1 means, why the system locks out, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - westinghouse
---

## Westinghouse Furnace E1 Error Code — What It Means

E1 on a Westinghouse furnace indicates a system lockout following a failed startup sequence. Westinghouse residential furnaces are manufactured by Nortek/Nordyne (the same parent behind Gibson, Frigidaire, and Maytag HVAC products) and use the ICP-derived control platform. The E1 code fires after the furnace exhausts its retry attempts — typically three ignition trials — without establishing a confirmed flame. The board then locks out until manually reset.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface igniter** — Silicon carbide igniters crack after several years of thermal cycling. A cracked igniter cannot reach ignition temperature, and the burners never light.
- **Contaminated flame sensor** — A film of oxidation on the sensor rod prevents the microamp flame-detection signal from reaching the board, causing the board to treat each ignition as a failure even if the flame briefly lights.
- **No gas supply** — A closed manual shutoff, low utility pressure, or a failed gas valve means no fuel reaches the burners despite a good igniter.
- **Pressure circuit fault** — If the inducer or pressure switch fault occurs before ignition begins, the board may log E1 as the generic lockout code rather than a pressure-specific code.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Turn the thermostat off, disconnect power for 30 seconds, then restore. This clears the lockout so the sequence can be observed.
2. **Observe the startup sequence** — Watch through the sight glass during a heat call. The igniter should glow orange within 45 seconds. Failure to glow = bad igniter.
3. **Test the igniter** — Measure resistance across the igniter leads: 40–200 Ω is serviceable. Open circuit = replace.
4. **Clean the flame sensor** — Remove the sensor and polish the rod tip with fine steel wool. Reinstall and test.
5. **Verify gas is on** — Confirm the shutoff valve at the furnace and the main gas supply are both open. Check that a gas range or water heater nearby is working.
6. **Check the pressure switch hose** — Inspect for blockage, cracks, or moisture. Clear or replace as needed.
7. **Reset and run a full cycle** — Power cycle and run a 15-minute heat call to confirm the repair holds.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/s?k=Hot+surface+igniter&tag=errorcodefixes-20) \| Match Westinghouse/Nordyne model number for correct wattage |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Clean first; replace if cleaning does not resolve |
| Pressure switch | [Amazon](https://www.amazon.com/s?k=Pressure+switch&tag=errorcodefixes-20) \| Match WC rating from original switch label |
## When to Call a Pro

If resetting and basic component inspection does not resolve E1 after two attempts, a technician should check gas valve operation, measure inlet gas pressure, and inspect the heat exchanger for cracks that could cause recurring lockouts.
