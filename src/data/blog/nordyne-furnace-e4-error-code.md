---
title: "Nordyne Furnace E4 Error Code — Causes & Fix"
description: "What Nordyne furnace error code E4 means, why ignition locks out, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - nordyne
---

## Nordyne Furnace E4 Error Code — What It Means

E4 on a Nordyne furnace (and Nordyne-built brands including Frigidaire, Gibson, Westinghouse, and Maytag residential furnaces) indicates an ignition lockout. The control board attempted the ignition sequence — typically three tries — and never detected a stable flame signal. After exhausting retries, the board locks out and flashes E4. The furnace will not attempt another ignition until the lockout is manually cleared by cycling power. The most likely causes are a failed hot surface igniter, dirty flame sensor, or interrupted gas supply.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface igniter** — The silicon carbide igniter is the most frequent cause. A cracked element draws current but cannot reach ignition temperature; an open element does nothing at all.
- **Dirty flame sensor** — Oxidation on the sensor rod attenuates the microamp flame-detection signal below the threshold the board requires to confirm ignition, causing retry and lockout.
- **Gas supply problem** — A closed shutoff valve, low gas pressure, or failed gas valve solenoid means no gas reaches the burners even when the igniter glows.
- **Pressure switch not proving** — If the pressure switch fault (E1) is intermittent or borderline, the board may allow the ignition trial to start but abort before flame confirmation, ultimately logging E4 on the last attempt.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Cycle furnace power off for 30 seconds and restore. Set thermostat to heat call.
2. **Watch the ignition attempt** — The sequence: inducer on → igniter glow → gas valve open → flame detected. Identify where the sequence stops.
3. **Test the hot surface igniter** — Measure resistance: a good igniter reads 40–200 Ω. Replace if the reading is open (infinite) or if the element is visibly cracked.
4. **Clean the flame sensor** — Remove the sensor rod and polish the tip with fine steel wool. Reinstall. Dirty sensors are responsible for a large percentage of E4 faults even when the igniter is functioning.
5. **Verify gas supply** — Confirm all gas shutoffs are open. Listen for the gas valve to click during the ignition trial. If you hear the valve click but no gas flows, the valve may be failed.
6. **Check pressure switch if the sequence never reaches ignition** — Inspect the hose for blockage; test switch continuity during inducer operation.
7. **Clear and run a full cycle** — After repair, cycle power and run 15 minutes of heating to confirm no recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-nordyne-furnace-e4-error-code&tag=errorcodefixes-20) \| Nordyne-specific part; use OEM or a direct replacement with matching wattage |
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-nordyne-furnace-e4-error-code&tag=errorcodefixes-20) \| Standard universal sensors work in most Nordyne models |
| Gas valve | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-nordyne-furnace-e4-error-code&tag=errorcodefixes-20) \| Replace only after confirming 24VAC input with no gas output |
## When to Call a Pro

If E4 returns within a few days of clearing, have a technician check the heat exchanger for cracks. A cracked heat exchanger causes erratic combustion that can trip the flame sensor even when the burner appears to be operating.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
