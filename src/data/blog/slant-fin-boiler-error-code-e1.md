---
title: "Slant/Fin Boiler Error Code E1 — Causes & Fix"
description: "What Slant/Fin boiler error code E1 means, why ignition locks out, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - boiler
  - slant-fin
---

## Slant/Fin Boiler Error Code E1 — What It Means

E1 on a Slant/Fin boiler (Galaxy, Eutectic, or Minuteman series) indicates an ignition lockout — the control board tried to light the burner and did not receive a flame confirmation signal within the trial-for-ignition window. After two or three failed attempts the board locks out and displays E1. Slant/Fin boilers use a Honeywell or Beckett ignition module for gas firing; the E1 lockout is the module's way of preventing a gas buildup in the combustion chamber.

[Jump to Fix](#fix)

## Common Causes

- **Failed or contaminated flame sensor** — The flame rod accumulates oxidation over the heating season. A dirty sensor cannot conduct the required microamp signal, causing the board to abort ignition even when the burner lights momentarily.
- **Faulty igniter or ignition module** — The spark igniter electrode gaps wider or the ignition module itself fails, preventing reliable ignition of the gas-air mixture.
- **Gas supply interruption** — A partially closed gas valve, low utility pressure during peak demand, or a failed gas valve solenoid means no gas is available during the ignition trial.
- **Blocked or flooded condensate system (condensing models)** — A blocked condensate trap on Slant/Fin condensing boilers creates a pressure imbalance that prevents draft proof, sometimes aborting the startup before the ignition trial even begins and producing E1 as a generic lockout code.

## Step-by-Step Fix {#fix}

1. **Press the reset button** — Most Slant/Fin controls have a manual reset button on the ignition module or the boiler control panel. Press it to clear E1 and allow observation of the next startup attempt.
2. **Watch the ignition sequence** — Listen for the inducer (if equipped), the igniter click, and the burner light. A burner that lights and then goes out within a few seconds points directly at a dirty flame sensor.
3. **Clean the flame sensor** — Remove the flame sensor rod (usually one 1/4" screw) and lightly polish the metal tip with fine steel wool. Reinstall with the tip in the flame path.
4. **Inspect the igniter electrode** — Check the electrode tip for carbon buildup and verify the gap is within the manufacturer's spec (typically 1/8"). Clean with a dry brush.
5. **Confirm gas supply** — Verify the manual shutoff is fully open and that other gas appliances in the home are working normally.
6. **Reset and run through a full cycle** — After any repair, reset and allow the boiler to complete at least one full heat cycle, then monitor for recurrence of E1.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Usually model-specific; match the part number from the Slant/Fin service manual |
| Ignition module | [Amazon](https://www.amazon.com/s?k=Ignition+module&tag=errorcodefixes-20) \| Honeywell S8600 or Beckett equivalent depending on model |
| Gas valve | [Amazon](https://www.amazon.com/s?k=Gas+valve&tag=errorcodefixes-20) \| Replace only after confirming 24VAC command and no gas output |
## When to Call a Pro

If E1 returns within days of cleaning the flame sensor, have a licensed plumber or HVAC technician measure gas inlet pressure and perform a combustion analysis. Low gas pressure and combustion air problems cause repeated ignition failures and are not safely addressed without proper instruments.
