---
title: "Goodman GMS80 Furnace Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Goodman GMS80 furnace error codes, LED flash sequences, common fault causes, and step-by-step repair procedures for HVAC technicians."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - goodman
  - furnace
money_part: "Hot surface igniter"
---

## Goodman GMS80 Furnace Error Codes — What They Mean

The Goodman GMS80 is an 80% AFUE single-stage gas furnace with a PSC blower motor. It is a straightforward, high-reliability unit widely used in residential applications and is one of the most common furnaces in service across North America. The GMS80 uses a single-LED diagnostic system on the Goodman control board — the same flash code system used across the Goodman/Amana/Daikin residential furnace lineup. The LED is visible on the board through the lower access panel window.

## Goodman GMS80 LED Flash Code Reference

| Flash Count | Fault |
|---|---|
| 1 flash | Normal — system waiting for call |
| 2 flashes | Pressure switch stuck open |
| 3 flashes | Pressure switch stuck closed |
| 4 flashes | Open limit device (high-limit or aux limit) |
| 5 flashes | Flame sensed without gas valve call |
| 6 flashes | 6 ignition retries failed — hard lockout |
| 7 flashes | Gas valve (low-fire) fault |
| 8 flashes | Low igniter current detected |
| 9 flashes | Rollout switch open |
| Rapid flash | Low control voltage (below 19VAC) |

## Common Causes by Code

- **2 flashes — Pressure switch open** — On an 80% furnace like the GMS80, the most common cause is a blocked flue pipe or a bad inducer motor that isn't creating enough draft negative pressure. Also check the pressure switch hose for cracks or separation at the inducer housing.
- **3 flashes — Pressure switch stuck closed** — The switch is closing before the inducer starts. A condensate-filled pressure switch hose can keep the switch closed. Disconnect the hose and drain/blow it clear.
- **4 flashes — Limit open** — Dirty filter, blocked supply or return, or a failed blower motor. The GMS80 high-limit switch opens around 160–180°F on the heat exchanger outlet. Check the temperature rise (should be 35°F–65°F for most GMS80 configurations).
- **6 flashes — Ignition lockout** — After 6 failed ignition attempts, the GMS80 locks out and requires manual reset (press the board reset button or cycle power). Common causes: failed igniter, no gas, dirty flame sensor.
- **9 flashes — Rollout switch** — Manual reset safety switch at the burner. Trips if flames escape the burner box. Do not operate the furnace until the root cause is found — typically a cracked heat exchanger or blocked flue.

## Step-by-Step Fix {#fix}

1. **Find the LED** — Look through the lower access panel observation window on the GMS80. The LED is on the right side of the control board. Count the flashes (pause → flashes → pause = one code cycle).
2. **For 2 flashes (pressure switch open)** — Disconnect the pressure switch hose at the inducer housing and at the switch. Blow air through the hose — should be clear. Also check the flue pipe run for bird nests or ice blockage (common in late fall/early spring).
3. **For 4 flashes (limit open)** — Replace the air filter immediately. Check the return air temperature — should be between 65°F and 80°F entering the furnace. Also spin the blower wheel by hand (with power off) to confirm it's not obstructed by debris (socks, plastic bags often get sucked into the return).
4. **For 6 flashes (ignition lockout)** — Reset the board. Watch the ignition sequence through the sight glass: inducer on → igniter glow (visible orange in 17–25 seconds) → gas valve click → flame. If the igniter doesn't glow brightly, measure its resistance (40–90 Ω cold is normal for silicon nitride).
5. **For 9 flashes (rollout)** — Find and press the manual reset button on the rollout switch (red button at the burner compartment). Before resetting, look into the burner compartment — excessive carbon deposits indicate a heat exchanger blockage. An HVAC tech with a combustion analyzer should inspect before returning to service.

## Parts Often Needed

| Part | Notes |
|---|---|
| Hot surface igniter | [Amazon](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-goodman-gms80-error-codes&tag=errorcodefixes-20) \| Goodman uses both silicon nitride and silicon carbide depending on production year |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Rod-type; clean before replacing |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-goodman-gms80-error-codes&tag=errorcodefixes-20) \| Check hose first; switches fail after condensate contamination |
| High-limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-goodman-gms80-error-codes&tag=errorcodefixes-20) \| L160 or L180 depending on GMS80 variant |
| Rollout switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-goodman-gms80-error-codes&tag=errorcodefixes-20) \| L195°F or L270°F; manual reset |
| PSC blower capacitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-gms80-error-codes&k=PSC+blower+capacitor&tag=errorcodefixes-20) \| Single-run capacitor on PSC motor; check µF |
## When to Call a Pro

A Goodman GMS80 that trips the rollout switch (Code 9) requires professional inspection before return to service. A cracked heat exchanger allows combustion gases to mix with circulated air — a carbon monoxide risk. Do not bypass the rollout switch. If the furnace repeatedly trips the limit (Code 4) after filter replacement, a cracked heat exchanger or ECM motor issue may be the root cause requiring professional diagnosis.
