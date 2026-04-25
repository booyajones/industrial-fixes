---
title: "Lochinvar Boiler Error Code E03 — High Limit Tripped"
description: "Lochinvar E03 error means the high limit switch opened due to overtemperature. Learn why this happens on Knight and Crest boilers and how to fix it."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - lochinvar
  - boiler
  - hvac
  - error-code
  - high-limit
---

## Lochinvar E03 Error — High Limit Tripped

**E03 on a Lochinvar boiler** means the **high limit switch opened** — water temperature exceeded the safety limit. This is a soft lockout on most Lochinvar models: the boiler stops firing, the limit switch cools, auto-resets, and the boiler restarts. If the high limit trips repeatedly, Lochinvar control boards will eventually escalate to a hard lockout.

E03 appears on Lochinvar Knight (WHN, WHB series), Crest, and Commercial Fire Tube boilers.

## High Limit Switch Function

The high limit switch is set to open when supply water temperature exceeds a factory setpoint (typically 210–215°F on hot water boilers). It's a safety device — if the water gets too hot, pressure builds, pipes can fail, and scalding becomes a risk.

The switch is typically located on the supply outlet of the boiler, mounted in a well that contacts the water.

## Why Water Gets Too Hot — Common Causes

| Cause | Explanation |
|---|---|
| [Setpoint too high](https://www.amazon.com/s?k=Setpoint+too+high&tag=errorcodefixes-20) | Boiler set to run near limit temp |
| [Blocked heat distribution](https://www.amazon.com/s?k=Blocked+heat+distribution&tag=errorcodefixes-20) | Radiators, baseboard, or zone valves closed |
| [Zone valve failure](https://www.amazon.com/s?k=Zone+valve+failure&tag=errorcodefixes-20) | Zone valve stuck closed, no load |
| [Pump failure](https://www.amazon.com/s?k=Pump+failure&tag=errorcodefixes-20) | Circulator not moving water through system |
| [Airlock in system](https://www.amazon.com/s?k=Airlock+in+system&tag=errorcodefixes-20) | Air pocket preventing water circulation |
| [Sensor miscalibration](https://www.amazon.com/s?k=Sensor+miscalibration&tag=errorcodefixes-20) | Wrong reading, causing boiler to overshoot |
| [Oversized boiler](https://www.amazon.com/s?k=Oversized+boiler&tag=errorcodefixes-20) | Too much output for the system's load |

## How to Diagnose E03

**Step 1 — Check the circulator pump.** Touch the pump housing — it should be warm and you should feel vibration when the boiler is running. If cold and silent, the pump may have failed or the wiring is off. Check pump power (120VAC or 24VAC depending on model).

**Step 2 — Check zone valves.** If you have a zoned system, open all zone valves manually. A zone valve that's stuck closed means all the boiler's output has nowhere to go — supply temp skyrockets.

**Step 3 — Check for air in the system.** Hydronic systems develop air pockets that prevent circulation. Look for auto-air vents at high points — verify they're open and functioning. Try bleeding manual air vents on radiators or baseboards.

**Step 4 — Verify boiler setpoint.** On the Lochinvar control: Menu → Settings → Supply Setpoint. If it's set at 200°F or above, lower it to 180°F for typical hot water heating. This gives more headroom before the 210–215°F limit trips.

**Step 5 — Check the supply temperature sensor.** If the sensor is reading incorrectly (reporting a lower temp than actual), the boiler fires too long, overshoots, and trips the limit. Compare the display reading to a contact thermometer on the supply pipe.

## Reset Procedure

On Lochinvar Knight boilers: the E03 fault is typically auto-resetting once the water cools. If it doesn't auto-reset, press and hold the RED RESET button on the control panel for 3 seconds. 

**Do not reset repeatedly without finding the cause** — cycling a high-limit fault without repair risks heat exchanger damage.

## Parts Reference

| Part | Cost |
|---|---|
| [Circulator pump (Taco 007)](https://www.amazon.com/s?k=Circulator+pump+%28Taco+007%29&tag=errorcodefixes-20) | $120–200 |
| [Zone valve (Taco, Honeywell)](https://www.amazon.com/s?k=Zone+valve+%28Taco%2C+Honeywell%29&tag=errorcodefixes-20) | $80–150 |
| [High limit switch](https://www.amazon.com/s?k=High+limit+switch&tag=errorcodefixes-20) | $30–80 |
| [Supply temperature sensor](https://www.amazon.com/s?k=Supply+temperature+sensor&tag=errorcodefixes-20) | $30–60 |

## E03 vs. E01 on Lochinvar

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixes-20) | Meaning |
|---|---|
| E01 | Ignition failure (no flame) |
| E02 | Ignition lockout after retries |
| E03 | High limit tripped (this post) |
| E04 | Low water pressure fault |

If E03 happens only on very cold days when the boiler is running at full capacity, the boiler may be appropriately sized but the distribution system has too much resistance. A hydronic balancing tech can verify.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)
