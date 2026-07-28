---
title: "Goodman 7 Flash Error Code — Ignition Lockout Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-28T08:00:00Z
modDatetime: 2024-03-28T08:00:00Z
slug: goodman-7-flash-error-code
featured: false
draft: false
tags:
  - hvac
  - goodman
  - furnace
  - ignition
description: "Goodman 7 flashes means the furnace locked out after failing to ignite three times. This guide covers diagnosis and fixes for the Goodman furnace ignition lockout fault."
---

## Error Code: Goodman 7 Flashes

**What it means:** Seven flashes on a Goodman furnace indicates a gas heating lockout — the control board attempted ignition three consecutive times, failed to confirm flame each time, and locked out. During each ignition trial, the board energizes the hot surface igniter, waits for it to reach ignition temperature, opens the gas valve, then monitors the flame sensor for a microamp signal confirming a live flame. If the flame sensor does not respond within the trial period (typically 4–7 seconds after valve opens), the board closes the gas valve and logs a failed attempt. After three failures, it locks out with 7 flashes. Power must be cycled or the lockout timer (typically 60 minutes) must expire before another attempt.

## Common Causes

- **Oxidized flame sensor** — The single most common cause across all gas furnace brands. A thin oxide layer on the sensor rod insulates it from the flame, preventing microamp signal. Cleaning takes 5 minutes.
- **Failed hot surface igniter** — Igniters degrade over 7–10 years. A cracked or weakened igniter fails to reach ignition temperature reliably.
- **Low gas pressure** — Manifold pressure below spec (typically 3.2–3.5" W.C. for natural gas) produces a weak flame that the sensor cannot reliably detect.
- **Gas valve not opening** — The board sends 24V AC to the gas valve; if the valve solenoid has failed, no gas flows despite the igniter glowing.
- **Failed control board** — Less common, but a board with a failed gas valve relay will not energize the valve even when it intends to.

## Diagnosis Steps

1. Reset the lockout by cycling the furnace power. Watch the ignition sequence carefully. You should see: inducer starts → igniter glows orange-white → gas valve clicks open → burner flames light → flame stabilizes.
2. If igniter glows but no flame: suspect gas valve or gas supply. Verify other gas appliances work (range, water heater). If those work, gas supply is fine — suspect gas valve.
3. If flame lights briefly and then goes out: suspect flame sensor. The flame lights, sensor fails to detect it, board cuts gas.
4. Remove and clean the flame sensor: one screw, pull the rod out, clean the metal rod with fine steel wool or emery cloth, reinstall. Test immediately.
5. Check igniter resistance: disconnect power, remove igniter, measure across terminals. Silicon nitride igniters should read 40–90 ohms. Open (OL) = cracked igniter, replace.

## Fix

Flame sensor cleaning resolves this fault roughly 60% of the time. Do it first, it costs nothing. If cleaning doesn't hold, replace the sensor ($15–25).

If the igniter is weak (visibly dim red rather than bright orange-white), replace it. Goodman/Amana furnaces commonly use a Norton/Saint-Gobain silicon nitride igniter. Order by furnace model number for correct fit.

If both sensor and igniter check out and gas is flowing: the control board gas valve relay may have failed. Measure 24V AC at the gas valve terminals during ignition trial. If voltage is present but valve doesn't open (no click, no gas), replace the valve. If no voltage is reaching the valve, replace the control board.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Flame sensor](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) | RepairClinic, Amazon |
| [Hot surface igniter](https://www.amazon.com/dp/B00BTLLJ40?ascsubtag=ecf-goodman-7-flash-error-code&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Gas valve](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-goodman-7-flash-error-code&tag=errorcodefixes-20) | SupplyHouse, Grainger |
| [Control board](https://www.amazon.com/s?k=Control+board&tag=errorcodefixes-20) | RepairClinic, Grainger |

## When to Call a Technician

Flame sensor cleaning and igniter replacement are appropriate DIY repairs. Gas valve replacement and gas pressure adjustment require a licensed HVAC technician. If the board is involved, a tech can perform a faster diagnosis using a service analyzer.
