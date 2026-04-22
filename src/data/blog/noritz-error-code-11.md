---
title: "Noritz Error Code 11 — Causes & Fix"
description: "What Noritz 11 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - boiler
  - noritz
---

## Noritz Error Code 11 — What It Means

Noritz error code 11 means ignition failure — the unit attempted to light the burner and failed. The control board runs the fan, opens the gas valve, and fires the igniter. If no flame is detected by the ionization sensor within the trial-for-ignition period, the attempt is logged as a failure. After 3 failed attempts, the unit locks out with code 11 and requires a manual reset before trying again. This is Noritz's primary ignition lockout code and points to the igniter electrode, gas supply, or venting system.

[Jump to Fix](#fix)

## Common Causes

- **No gas or low gas pressure** — The manual shutoff valve upstream of the unit may be partially closed, or line pressure may be insufficient. At full fire, Noritz units require significant gas flow.
- **Failed spark igniter** — The igniter electrode wears and carbons up over time. A fouled electrode produces a weak spark that can't reliably light the gas.
- **Air in the gas line** — After a gas shutoff (utility work, meter replacement), air trapped in the supply line causes the first 1–3 ignition attempts to fail.
- **Venting problem preventing fan proving** — If the combustion fan's pressure switch doesn't close (blocked vent or failed fan), the ignition sequence is blocked and the board counts it as an ignition failure.

## Step-by-Step Fix {#fix}

1. **Verify gas supply** — Check that the manual gas shutoff at the unit (and any upstream valves) is fully open. If gas was recently interrupted, open a gas appliance elsewhere in the building to purge air.
2. **Reset and observe** — Press the reset button. Watch the startup: fan should spin, then clicking spark, then flame. If the fan runs and clicking is audible but no flame, suspect gas supply or igniter.
3. **Clean the igniter electrode** — Remove the burner access panel. Locate the spark electrode at the burner. Clean the electrode tip with fine sandpaper. Verify the gap is approximately 3–4mm.
4. **Check vent terminations** — Inspect exhaust and intake at the exterior for blockages. A blocked vent prevents the pressure switch from proving and halts the ignition sequence.
5. **Reset the system** — After repairs, press reset and run a hot water draw. If the unit ignites on the first attempt and holds flame, the fault is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Igniter/spark electrode | Noritz model-specific; verify part number from service manual |
| Combustion fan | Replace if fan doesn't reach operating speed |
| Gas valve | Only after confirming correct voltage present at valve with no gas output |

## When to Call a Pro

Persistent code 11 after verifying gas supply and cleaning the igniter needs a tech with a manometer to check gas pressure at the manifold and a combustion analyzer to verify ignition quality.
