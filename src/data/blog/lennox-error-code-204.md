---
title: "Lennox 204 Error Code — Causes & Fix"
description: "What Lennox 204 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - lennox
---

## Lennox 204 Error Code — What It Means

Lennox error code 204 means ignition failure — the furnace attempted to light the burners but failed to establish a flame within the allowed trial time. On iComfort systems this shows as "204" on the thermostat. On SureLight boards it appears as a flash sequence. The board allows 3 ignition attempts before locking out. Code 204 tells you the ignition sequence ran (draft proved, gas valve opened) but no stable flame was detected by the sensor. The igniter, gas supply, and flame sensor are the three components to check in that order.

[Jump to Fix](#fix)

## Common Causes

- **Weak or cracked hot surface igniter** — The igniter reaches ignition temperature (about 1800°F) only when resistance is in spec (40–90 ohms). A cracked igniter may glow dimly but not hot enough to light gas.
- **Dirty flame sensor** — The flame sensor rod must conduct a small current (2–10 microamps) through the flame to confirm combustion. Carbon or oxide coating on the rod insulates it and the board shuts gas off — exactly mimicking ignition failure.
- **Insufficient gas pressure** — If manifold pressure is below 3.2" WC for natural gas, the flame may light but immediately extinguish before the sensor confirms it.
- **Gas valve not opening fully** — A partially stuck gas valve can allow too little gas to sustain a flame through the trial period.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Power off the furnace for 30 seconds, then restore. Watch the ignition sequence: draft motor starts, igniter glows, gas valve clicks, burners should light.
2. **Observe the igniter** — If you can safely see the igniter through the observation window, confirm it glows bright orange. Dull red or no glow means test resistance (power off): should read 40–90 ohms.
3. **Clean the flame sensor** — Locate the rod (single-wire probe near the burners). Remove with one screw. Lightly sand the rod with fine steel wool. Reinstall and test.
4. **Check gas supply** — Ensure the gas meter is running and the manual shutoff upstream of the furnace is fully open. If gas was recently shut off, the first attempt often fails due to air in the line — try 2 resets before replacing parts.
5. **Reset the system** — After repairs, power cycle and confirm the furnace completes 2–3 heating cycles without returning code 204.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot surface igniter | [Amazon](https://www.amazon.com/s?k=Hot+surface+igniter&tag=errorcodefixes-20) \| Lennox uses OEM part 62W21; verify for your model |
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Universal fit for most Lennox units; $12–18 |
| Gas valve (24V) | [Amazon](https://www.amazon.com/s?k=Gas+valve+%2824V%29&tag=errorcodefixes-20) \| Replace only after confirming voltage is present at valve terminals during trial |
## When to Call a Pro

If igniter and flame sensor check out and gas is confirmed at the valve, the issue is likely gas valve internal failure or a combustion problem that needs a combustion analyzer. These require a licensed tech.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
