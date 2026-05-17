---
title: "Comfortmaker Furnace E4 Error Code — Causes & Fix"
description: "What Comfortmaker furnace error code E4 means, why ignition fails, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - comfortmaker
---

## Comfortmaker Furnace E4 Error Code — What It Means

E4 on a Comfortmaker furnace indicates an ignition failure lockout — the control board attempted ignition the maximum number of times (typically three tries) and never detected a stable flame. Comfortmaker is an ICP brand sharing the same control platform as Heil, Tempstar, and Carrier. After E4, the furnace locks out and must be manually reset by cycling power. The root cause is almost always a bad igniter, contaminated flame sensor, or a gas supply problem.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface igniter (HSI)** — The silicon carbide or silicon nitride igniter cracks over time and either does not glow hot enough or has an open circuit. This is the most common cause of E4.
- **Dirty or coated flame sensor** — A thin oxide layer on the flame sensor rod prevents it from conducting the microamp signal back to the board, making the board think ignition never occurred even when the burners light briefly.
- **Gas valve not opening or low gas pressure** — A failed gas valve solenoid or gas supply pressure below the rated inlet pressure means no gas reaches the burners despite a glowing igniter.
- **Rollout or limit switch open** — If a safety limit is open before the ignition sequence begins, the board may abort and log E4 rather than the limit-specific code.

## Step-by-Step Fix {#fix}

1. **Cut power and restore to clear the lockout** — Cycle the disconnect for 30 seconds, then restore. This resets the lockout counter so you can observe the ignition attempt.
2. **Watch the ignition sequence** — Turn on a heat call and observe through the sight glass: the inducer should start, then the igniter should glow bright orange within 30–60 seconds. If the igniter does not glow, test its resistance — a good HSI reads 40–200 Ω; infinite resistance means it is broken.
3. **Clean the flame sensor** — Remove the flame sensor rod and lightly polish the metal tip with fine steel wool or emery cloth. Reinstall and test. This resolves many phantom ignition failures.
4. **Verify gas supply** — Confirm the gas shutoff at the furnace is fully open. If other gas appliances in the home are working but the furnace still does not light, check the gas valve for 24VAC at the operator terminals during the ignition trial.
5. **Test the gas valve** — If 24VAC is present at the valve but no gas flows, the valve is failed and needs replacement.
6. **Reset and confirm** — After any repair, power cycle and run a complete heat call to verify a clean ignition and steady flame for at least 10 minutes.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-comfortmaker-furnace-e4-error-code&tag=errorcodefixes-20) \| Match voltage (120V) and mounting style; OEM or quality aftermarket |
| Flame sensor rod | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-comfortmaker-furnace-e4-error-code&tag=errorcodefixes-20) \| Replace if cleaning does not restore normal microamp signal |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-comfortmaker-furnace-e4-error-code&tag=errorcodefixes-20) \| Replace only after confirming 24VAC input with no output |
## When to Call a Pro

If gas supply pressure requires measurement, or if the gas valve needs replacement, contact a licensed HVAC technician — gas valve work involves live gas lines and requires proper pressure gauges and leak-testing.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
