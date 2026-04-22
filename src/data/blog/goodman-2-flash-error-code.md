---
title: "Goodman 2 Flash Error Code — Causes & Fix"
description: "What Goodman 2 flashes means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - goodman
---

## Goodman 2 Flash Error Code — What It Means

Two flashes on a Goodman furnace LED means system lockout — the furnace control board has attempted ignition the maximum number of times (typically 3 retries) without success and has locked out to prevent unburned gas buildup. The board holds this fault until manually reset. This is a catch-all lockout: the root cause could be in any part of the ignition sequence — igniter, flame sensor, gas pressure, or pressure switch. The 2-flash code tells you the furnace gave up; the diagnostic work starts from there.

[Jump to Fix](#fix)

## Common Causes

- **Failed hot surface igniter** — Goodman GMSS/GMVC series igniters are known to crack and fail. A cracked igniter often still glows but at insufficient temperature to light gas. Normal resistance: 40–90 ohms.
- **Dirty flame sensor** — After successful ignition, the board looks for microamp current through the flame sensor rod. Oxide buildup on the rod prevents conductance and the board shuts gas off thinking no flame is present.
- **Pressure switch not closing** — Draft motor not reaching speed, blocked hose, or flooded condensate collector keeps the switch open and prevents the ignition sequence from ever starting.
- **Low gas pressure** — Gas pressure below the required manifold pressure (typically 3.5" WC for natural gas) won't sustain a flame through the first few seconds and causes lockout.

## Step-by-Step Fix {#fix}

1. **Reset the lockout** — Turn the furnace power switch off for 30 seconds, then back on. Watch the startup sequence. This clears the lockout count.
2. **Test the igniter** — Power off. Disconnect the igniter leads and read resistance with a multimeter. 40–90 ohms = good. Open or out of range = replace. Visually inspect for cracks.
3. **Clean the flame sensor** — Remove the sensor rod (one screw, one wire). Lightly sand the rod with steel wool or 400-grit. Reinstall and test.
4. **Check draft motor and pressure switch hose** — Confirm the draft motor spins freely at startup. Check the small rubber hose from the motor housing to the pressure switch for blockages or cracks.
5. **Reset the system** — After addressing the root cause, power cycle and observe 2 full heating cycles. Confirm no 2-flash lockout returns.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Hot surface igniter (Goodman B1401015S)](https://www.amazon.com/s?k=Hot%20surface%20igniter%20(Goodman%20B1401015S)&tag=errorcodefixe-20) | Common Goodman igniter; verify part number for your model |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | Universal silicon nitride sensor fits most Goodman units |
| [Pressure switch](https://www.amazon.com/s?k=Pressure%20switch&tag=errorcodefixe-20) | Check water column rating on the old switch before ordering |

## When to Call a Pro

If the igniter tests good, flame sensor is clean, and draft system checks out, but lockout keeps returning, a combustion analysis and gas valve test requires a licensed tech with the right instruments.
