---
title: "Luxaire Furnace E1 Error Code — System Lockout"
description: "What the Luxaire furnace E1 error code means, why the system locks out, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - luxaire
---

## Luxaire Furnace E1 Error Code — What It Means

Luxaire is a York-branded product line (both are owned by Johnson Controls/Bosch), and Luxaire furnaces share the same control systems and fault codes as York. On Luxaire furnaces with LED display panels, E1 indicates a system lockout — the control board has exhausted its retry attempts after repeated ignition failures and has locked the unit out to prevent unburned gas accumulation. The furnace will not attempt to restart until the lockout is cleared manually. E1 is the control board's final state after multiple consecutive faults, not a first-attempt failure.

[Jump to Fix](#fix)

## Common Causes

- **Ignition failure chain** — E1 typically follows multiple failed ignition attempts. The root cause is usually a cracked hot surface ignitor, a contaminated flame sensor, low gas pressure, or a faulty gas valve. Fix the underlying ignition fault and E1 clears.
- **Repeated pressure switch faults** — If the pressure switch trips multiple times in sequence (due to a blocked condensate drain, cracked hose, or inducer issue), the board accumulates faults and locks out with E1.
- **Repeated limit switch trips** — Multiple high-limit or rollout trips in sequence drive the board to lockout. Underlying cause is always restricted airflow or a combustion problem.
- **Control board fault** — Less commonly, the control board itself fails and logs E1 as a self-diagnostic code, independent of any external fault. This typically follows a power surge event.
- **Low-voltage power issue** — Erratic 24VAC supply (from a failing transformer or corroded wiring) can cause the board to misfire through multiple operating sequences and enter lockout.

## Step-by-Step Fix {#fix}

1. **Read the LED diagnostic code before clearing** — Before resetting E1, note any prior codes blinking on the board LED. On most Luxaire/York boards, the LED will display the last fault code before E1 was logged. That prior code tells you what repeatedly failed (31 = pressure switch, 33 = limit, 13 = ignition). Fix that fault first.
2. **Clear the E1 lockout** — Turn the thermostat off. Turn off the furnace power switch (or flip the breaker). Wait 30 seconds. Restore power. The control board will reset and attempt the ignition sequence again.
3. **For prior ignition fault** — Inspect the hot surface ignitor for cracks; test resistance (40–75 ohms cold). Clean the flame sensor with fine steel wool. Verify gas supply valve is open.
4. **For prior pressure switch fault** — Clear the condensate drain, inspect hoses for cracks, verify inducer motor spins at full speed.
5. **For prior limit fault** — Check and replace the air filter, verify blower operation, open all registers.
6. **Verify 24VAC supply** — Measure 24VAC at the transformer secondary under load. Below 22VAC suggests a failing transformer that causes erratic control board behavior.
7. **Monitor for recurrence** — After clearing E1 and addressing the root fault, run two full heat cycles back-to-back. If E1 returns, the root cause was not fully resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface ignitor | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-luxaire-furnace-e1-error-code&tag=errorcodefixes-20) \| Most common fix when prior fault was ignition — match voltage (80V or 120V) |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Replace if ceramic is cracked; clean if just dirty |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-luxaire-furnace-e1-error-code&tag=errorcodefixes-20) \| Match setpoint from switch body |
| Air filter | [Amazon](https://www.amazon.com/dp/B0CLBFXLYJ?ascsubtag=ecf-luxaire-furnace-e1-error-code&tag=errorcodefixes-20) \| Replace if limit trips were caused by restricted airflow |
| Control board | [Amazon](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) \| Replace if E1 appears without prior fault history (board self-fault) |
## When to Call a Pro

If E1 returns within one or two heat cycles after clearing, the root fault isn't fully resolved or there's a more complex issue (cracked heat exchanger, intermittent gas valve). A licensed HVAC technician can attach a service analyzer to the control board to read real-time fault data during the heating sequence, identifying the exact failure point without guessing.

## Related Articles

- [AirEase Furnace E1 Error Code — Causes & Fix](/posts/airease-furnace-e1-error-code/)
- [Amana Furnace 3 Flash Error Code — Causes & Fix](/posts/amana-furnace-3-flash-error-code/)
- [American Standard Furnace 3 Flash Error Code — Causes & Fix](/posts/american-standard-furnace-3-flash/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
