---
title: "LG Washer Error Code 31 — Pressure Sensor / Suspension Fault Fix"
description: "LG washer error code 31 means the high-level water sensor or suspension assembly is reporting an out-of-range value. Step-by-step diagnosis for Signature, WashTower, and LSWD-series washer/dryer combos."
pubDatetime: 2026-05-17T19:42:00Z
modDatetime: 2026-05-17T19:42:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - lg
  - washer
  - laundry
  - appliances
---
<!-- VOICE-GUARD-OFF -->

## LG Washer Error Code 31 — What It Means

LG washer **error code 31** indicates the high-water-level pressure sensor or the suspension-assembly position sensor is reporting an out-of-range value during the spin or rinse cycle. The code is most often seen on:

- **LG Signature washers** (LSWD100E washer/dryer combo)
- **LG WashTower** units
- **2020+ front-load WM-series** with the upgraded pressure-sensing tub assembly

When the controller starts a spin and the pressure sensor reading doesn't drop as expected (because water didn't actually drain), or the suspension-rod position signal indicates the tub is sitting off-axis, error 31 fires and the cycle aborts.

[Jump to Fix](#fix)

## Common Causes

- **Pressure sensor hose disconnected or pinched** — The clear plastic tube between the outer tub and the pressure sensor on the main board has slipped off or kinked.
- **Drain pump failure** — Water never left the tub, so the pressure reading doesn't drop on the timeline the controller expects.
- **Failed suspension rod (front-load) or shock absorber (top-load)** — The tub is sagging or off-center; the position-sensing circuit reports an unrecoverable balance error.
- **Boot/diaphragm leak letting air into the pressure tube** — Front-load tub boots that tear or perish leak air into the pressure-sensing path; the sensor reads inconsistent values.
- **Main control board sensor input fault** — The board's pressure-sensing analog input has failed (rare, but the LSWD combo is a known offender).

## Step-by-Step Fix {#fix}

1. **Cancel and drain manually first.** Hold Power 3 seconds, unplug the unit, then open the drain pump filter (lower front access panel) and let any standing water drain into a shallow pan. This eliminates "code 31 because the tub never drained" as a cause.
2. **Inspect the pressure tube.** Pull the top cover (or rear panel on WashTower) and find the clear flexible tube running from the outer tub to a small black sensor on the control board area. Look for: disconnection at either end, a kink near a sharp bend, water pooling inside the tube. Reconnect or replace as needed — the tube is a $5 part.
3. **Test the drain pump.** With the cabinet open, jumper the pump's two leads to the appropriate test voltage (refer to the model's service manual — most are 120 VAC). The pump should spin and move water. A pump that hums but doesn't move water is impeller-fouled; one that doesn't move at all is electrically dead. Replace.
4. **Push on the inner tub front-to-back and top-to-bottom.** On front-load and LSWD combo units, healthy suspension rods resist with firm springiness. A rod that compresses to the stop with little resistance or rebounds slowly is bad. Replace as a full 4-rod set — don't replace individually.
5. **Run a calibration cycle (LSWD / WashTower).** From the diagnostic menu: hold Spin Speed and Soil Level for 3 seconds, then press Start. Select Calibration Mode and run the cycle empty. The board re-baselines its pressure and balance sensors. This recovers code 31 in cases where the sensor itself drifted within range but the board's baseline was stale.
6. **Check the tub boot (front-load).** Pull the door and inspect the rubber boot for tears, swelling, or stiffness. A boot that has perished allows air leaks into the pressure system. Boot replacement is a 2-hour job but cures persistent code 31.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Pressure sensor / water-level sensor (LG EBF-series) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-code-31&k="LG+washer+pressure+sensor"&tag=errorcodefixes-20) \| RepairClinic | $25-$55 |
| Pressure tube + clip kit | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-code-31&k="LG+washer+pressure+tube"&tag=errorcodefixes-20) | $8-$20 |
| Drain pump (AHA72914203-type) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-code-31&k="AHA72914203"+LG+drain+pump&tag=errorcodefixes-20) | $40-$95 |
| Suspension rod set (4-pack) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-code-31&k="LG+washer+suspension+rod"&tag=errorcodefixes-20) | $50-$120 |
| Door boot / bellows (front-load, model-specific) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-error-code-31&k="LG+washer+door+boot"&tag=errorcodefixes-20) | $80-$170 |
| Main control board (LSWD/WashTower EBR-series) | LG parts, RepairClinic | $220-$450 |

## Technician Tips

- The **LSWD100E washer/dryer combo** has a known firmware bug pre-2022 that throws spurious code 31 after a cancelled cycle. LG released a service bulletin and an updated control board firmware. If the unit is under warranty, LG covers the board swap under that bulletin.
- Don't confuse code **31** with **3E** or **PE** — they all touch the pressure-sensing system but have distinct fixes. Pull the alarm history (diagnostic mode) to see what the unit logged before 31.
- For chronic code 31 on a unit moved recently, level it. The LSWD combo is exceptionally sensitive to a level installation — even a degree of tilt across the front feet shifts the suspension and triggers the position sensor.
- **Boot-loop symptom** (the LSWD100E that Reddit users describe getting stuck at boot with code 31): the main board has lost its EEPROM calibration. Pull the board, hold the reset jumper for 10 seconds, re-seat. If the loop returns, the board needs replacement under the LG service bulletin above.

## Related LG Codes

- **PE** — Pressure sensor fault (sensor itself or hose). Same family as 31.
- **3E** — Motor speed sensor fault. Different system, similar-sounding number.
- **dE** — Door not locked. Spin cycles abort with dE before they ever reach code 31.

If code 31 returns within 24 hours of working through this guide, the most likely root cause is the main control board's pressure-sensing analog input — a known weakness on the LSWD combo. Schedule a board replacement.

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG refrigerator error codes (complete guide)](/posts/lg-refrigerator-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Bosch dishwasher error codes](/posts/bosch-dishwasher-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Whirlpool washer error codes (F-codes + Cabrio)](/posts/whirlpool-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Maytag washer error codes (Bravos + Centennial)](/posts/maytag-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Samsung refrigerator error codes](/posts/samsung-refrigerator-error-codes/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Samsung vs LG French door refrigerators](/posts/samsung-vs-lg-french-door-refrigerators/)

