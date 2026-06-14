---
title: "Nordyne E1 Error Code — Causes & Fix"
description: "What Nordyne E1 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - nordyne
money_part: "Hot surface igniter"
most_likely_cause: "Failed hot surface igniter"
---

## Nordyne E1 Error Code — What It Means

Nordyne error code E1 means the furnace has gone into system lockout after repeated ignition failures. Nordyne covers several brands including Frigidaire, Westinghouse, Gibson, Tappan, and Comfort Maker residential furnaces. The E1 lockout is triggered after 3 failed ignition attempts — the board has tried to establish a flame and failed each time. Until manually reset, the furnace will not attempt another ignition cycle. E1 is a lockout indicator; the root cause is somewhere in the ignition chain: igniter, gas, flame sensor, or draft/pressure system.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface igniter** — Nordyne units use silicon nitride igniters that degrade over 5–7 years of service. Resistance should be 20–100 ohms at room temperature (varies by model). Crack or open circuit means replace.
- **Dirty flame sensor** — After ignition succeeds, the board looks for microamp current through the sensor rod. Oxidation on the rod prevents detection, and the board shuts gas off — triggering E1 lockout after retries.
- **Pressure switch fault** — If the draft system isn't proving before ignition attempts, the board may still count the failed sequence and eventually lock out. Check hose and motor.
- **Gas supply issue** — Verify the manual gas shutoff upstream of the furnace is open. If gas was recently interrupted (utility work, meter maintenance), air in the line causes the first 1–2 attempts to fail.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Press the reset button on the furnace (typically a red button on the burner assembly) or cut power for 30 seconds. Power on and observe the ignition sequence closely.
2. **Test the hot surface igniter** — Power off. Measure resistance at the igniter leads. 20–100 ohms is acceptable; open or below 15 ohms means replace. Look for physical cracks under a flashlight.
3. **Clean the flame sensor** — Remove the sensor rod (one screw, one lead). Sand with fine steel wool until the rod surface shines. Reinstall.
4. **Verify draft system operation** — Confirm the draft motor spins at startup. Check the pressure switch hose for cracks. On 90%+ units, clear the condensate trap.
5. **Reset the system** — After repairs, power cycle and monitor. Two successful heating cycles without E1 confirms the fix.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-nordyne-furnace-e1-error-code&tag=errorcodefixes-20) \| Nordyne part 904334; verify by model — several variants exist |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Universal fit available |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-nordyne-furnace-e1-error-code&tag=errorcodefixes-20) \| Match WC rating from the existing switch label |
## When to Call a Pro

If E1 lockout returns after addressing igniter and flame sensor, a tech should verify gas valve operation and combustion quality. Gas pressure testing requires a manometer and gas-certified technician.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
