---
title: "Trane 2 Flashes Error Code — Causes & Fix"
description: "What Trane 2 flashes means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
money_part: "Hot surface igniter"
most_likely_cause: "Failed igniter"
---

## Trane 2 Flashes Error Code — What It Means

Two flashes on a Trane furnace LED indicates a system lockout — the furnace tried to ignite multiple times, failed, and the control board locked out to prevent unburned gas from accumulating. The board will repeat the flash sequence continuously until the fault is cleared. Lockout doesn't mean something is permanently broken; it means the ignition sequence failed more than once (typically 3 attempts) and the board is waiting for a manual reset before trying again. The underlying cause could be anything in the ignition chain.

[Jump to Fix](#fix)

## Common Causes

- **Failed igniter** — Hot surface igniters are ceramic and crack with age. A cracked igniter may still glow visibly but not reach ignition temperature (should hit ~1800°F). Resistance should be 40–90 ohms at room temp; outside that range, replace it.
- **Weak gas pressure or closed gas valve** — Low inlet pressure or a manual gas valve that wasn't fully opened means gas doesn't reach the burner in time to light. Check that the manual shutoff upstream is fully open.
- **Dirty or failed flame sensor** — If the igniter works but the flame sensor can't confirm flame, the board shuts gas off and retries. Oxide buildup on the rod is the usual culprit.
- **Induced draft motor not proving** — If the pressure switch doesn't close because the draft motor isn't running at speed, the ignition sequence never starts — but the board still counts it as a failed attempt.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Cut power at the furnace switch or breaker for 30 seconds, then restore. This clears the lockout and allows the furnace to attempt ignition again. Watch the startup sequence.
2. **Watch the igniter** — Stand at the furnace during the startup attempt. You should see the igniter glow orange-hot within 30–60 seconds. If it doesn't glow at all, test its resistance with a multimeter (power off): 40–90 ohms is good.
3. **Check the gas valve** — Confirm the manual shutoff handle is parallel to the gas line (open). If gas was recently shut off, purge may be needed — the first attempt often fails because air is in the line.
4. **Clean the flame sensor** — Locate the flame sensor rod (1–3 inches long, near the burner, connected by a single wire). Lightly sand the rod with fine steel wool or 400-grit sandpaper. Clean the connector pin as well.
5. **Reset the system** — After any repair, power cycle and observe 2–3 full ignition cycles. If the furnace lights and stays on, you're clear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-trane-2-flashes-error-code&tag=errorcodefixes-20) \| Match OEM part number; aftermarket igniters often have shorter lifespans |
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Universal fit in most cases; costs under $15 |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-trane-2-flashes-error-code&tag=errorcodefixes-20) \| Test with manometer; replace if diaphragm is torn |
## When to Call a Pro

If the igniter glows, gas is flowing, and the flame sensor is clean but lockout still happens, the problem is likely in the gas valve or control board — both require a tech with proper test equipment to diagnose safely.

## See Also

- [Trane XR15 Heat Pump Error Codes — Complete Guide](/posts/trane-xr15-error-codes/)
- [Trane XV20i/XV18 Variable Speed Heat Pump Error Codes](/posts/trane-variable-speed-heat-pump-codes/)
- [Trane 8 Flashes Error Code — Causes & Fix](/posts/trane-8-flashes-error-code/)
- [Trane Furnace Error Codes — Complete Flash Code Guide](/posts/trane-furnace-error-codes/)

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
- [Trane 4 Flashes Error Code — Open High Limit Fix](/posts/trane-4-flashes-error-code/)
