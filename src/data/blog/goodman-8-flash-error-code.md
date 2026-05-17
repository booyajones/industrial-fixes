---
title: "Goodman 8 Flash Error Code — Causes & Fix"
description: "What Goodman 8 flash means, why ignition fails, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T10:00:00Z
modDatetime: 2026-04-22T10:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - goodman
---

## Goodman 8 Flash Error Code — What It Means

Eight flashes on a Goodman furnace diagnostic LED indicates an ignition failure lockout. The control board attempted to light the burners (up to three tries, depending on model) and the flame sensor never confirmed a stable flame. After exhausting its retry attempts, the board locks out and flashes code 8 until the fault is manually cleared. This code covers both hot surface ignitor failures and situations where gas never reaches the burner.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface ignitor (HSI)** — The ignitor glows to light the gas but cracks or burns out over time. A cracked ignitor may glow dimly or not at all, preventing ignition.
- **Dirty or failed flame sensor** — Even if the burner lights, a coated flame sensor won't confirm the flame, causing the board to abort the cycle and log an ignition failure.
- **No gas pressure or low gas pressure** — A closed shutoff valve, failed gas valve, or low supply pressure prevents gas from reaching the burners.
- **Induced draft motor or pressure switch fault** — If the draft inducer is not running at speed or a pressure switch is stuck open, the board will not open the gas valve at all, which looks like an ignition failure.

## Step-by-Step Fix {#fix}

1. **Check gas supply** — Confirm the manual shutoff valve is open. Check that other gas appliances in the building are working. If gas supply is confirmed, check furnace gas valve voltage (24VAC on the valve coil terminals during an ignition attempt indicates the board is commanding it open).
2. **Inspect the hot surface ignitor** — With power off, remove the ignitor (typically one screw). Visually inspect for cracks. Test resistance with a multimeter — most HSIs read 40–100 ohms when cold. An open circuit (OL) means it is broken; replace it.
3. **Clean the flame sensor** — Remove the sensor rod and clean with fine steel wool or emery cloth. Reinstall and retry.
4. **Check the induced draft motor** — Power the furnace and listen for the inducer to start at the beginning of the heat cycle. If it runs sluggishly or not at all, test the inducer motor and its capacitor.
5. **Reset and monitor** — After repairs, restore power and initiate a heat call. Watch the ignition sequence: inducer starts → pressure switch closes → ignitor glows → gas valve opens → flame lights. If any step fails, that component is the fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-goodman-8-flash-error-code&tag=errorcodefixes-20) \| Most common fix; verify correct model (120V or 80V HSI) |
| Flame sensor rod | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-goodman-8-flash-error-code&tag=errorcodefixes-20) \| Clean first; replace if cleaning does not help |
| Inducer motor capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-goodman-8-flash-error-code&tag=errorcodefixes-20) \| Test before replacing the full motor |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-goodman-8-flash-error-code&tag=errorcodefixes-20) \| Replace if voltage is present at coil but valve does not open |
## When to Call a Pro

If gas supply is confirmed but the valve is not opening and you are not familiar with 24VAC control circuits, have a licensed HVAC technician diagnose the gas valve and control board. Do not bypass safety controls to force ignition.

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix](/posts/goodman-3-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)
