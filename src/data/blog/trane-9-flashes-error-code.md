---
title: "Trane 9 Flashes Error Code — Causes & Fix"
description: "What Trane 9 flash error code means, why flame signal is low or absent, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
money_part: "Flame sensor rod"
most_likely_cause: "Dirty or oxidized flame sensor"
---

## Trane 9 Flashes Error Code — What It Means

Nine flashes on a Trane furnace status LED indicates a **low or no flame signal** — the ignitor lit the burner, but the flame sensor returned a microamp reading too low for the board to confirm stable combustion. The board will allow 3–4 ignition trials before locking out. This fault most often points to a contaminated flame sensor, but a weak gas supply or marginal ignitor can also cause it. The furnace will attempt to restart after the lockout timer, then lock out again if the issue isn't resolved.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or oxidized flame sensor** — Carbon or oxide buildup on the rod reduces conductivity; this is the most common cause and the easiest fix.
- **Weak or cracked ignitor** — A hot surface ignitor that hasn't fully failed may light the burner inconsistently, leading to a marginal flame signal.
- **Low gas pressure** — Under-pressure at the manifold produces a weak, unstable flame that the sensor can't read reliably.
- **Flame sensor grounding issue** — Loose mounting or a cracked ceramic insulator can cause the sensor signal to bleed to ground.

## Step-by-Step Fix {#fix}

1. **Locate the flame sensor** — It's a single metal rod with a ceramic insulator, positioned in the burner flame path, with one wire leading to the control board.
2. **Clean the flame sensor rod** — Remove the sensor (one screw). Lightly buff the metal rod with fine steel wool or emery cloth until it's shiny. Do not use sandpaper — it leaves abrasive residue.
3. **Check the sensor wire and connector** — Inspect the wire for cracking or pinching; check the connector at the board for corrosion or looseness.
4. **Verify gas pressure** — Check manifold pressure with a manometer. Typical natural gas manifold pressure is 3.5" W.C.; LP is 10" W.C. Low pressure points to a regulator or gas valve issue.
5. **Test ignitor resistance** — With power off, measure resistance across the ignitor terminals. Silicon nitride ignitors typically read 40–80 Ω when cold. Open circuit = replace ignitor.
6. **Reset the system** — Power off for 30 seconds. Restore power and call for heat. Watch the ignitor glow bright orange and confirm flame holds after ignition.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Inexpensive universal or OEM; match length and mounting bracket style |
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-trane-9-flashes-error-code&tag=errorcodefixes-20) \| Silicon nitride (most Trane) — match voltage (120V) and resistance spec |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-trane-9-flashes-error-code&tag=errorcodefixes-20) \| Only if manifold pressure is confirmed low and regulator adjustment doesn't correct it |
## When to Call a Pro

If cleaning the flame sensor and verifying gas pressure don't resolve the fault, and the furnace consistently fails to hold flame, suspect a cracked heat exchanger pulling excess combustion air across the burner. This is a safety issue requiring professional inspection — do not continue operating the furnace.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)

## See Also

- [Trane Rooftop Unit Error Codes: Common Faults Guide](/posts/trane-rooftop-unit-error-codes/)
- [Trane XV20i Error Code 79: Communicating Thermostat Fault Fix](/posts/trane-error-79-xv20i/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane XL18i Heat Pump Error Codes: Flash Codes and ComfortLink II Faults](/posts/trane-xl18i-error-codes/)
