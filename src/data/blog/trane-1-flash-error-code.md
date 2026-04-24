---
title: "Trane 1 Flash Error Code — Causes & Fix"
description: "What Trane 1 flash means on a furnace LED, why it signals normal operation or lockout depending on model, and how to respond."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane 1 Flash Error Code — What It Means

On most Trane furnaces, a single LED flash (1 blink, pause, repeat) signals normal standby operation — the furnace is powered and waiting for a heat call. However, on select Trane and American Standard models, particularly those manufactured before 2010, a 1-flash pattern indicates a system lockout or watchguard fault. Always cross-reference your specific model's diagnostic chart (printed on the inside of the furnace door) to confirm which interpretation applies.

[Jump to Fix](#fix)

## Common Causes

- **Normal standby (most models)** — No fault present; the furnace is idle and ready. No action required.
- **Lockout after repeated ignition failure (older models)** — The board attempted ignition three or more times, failed each time, and shut the system down to prevent gas accumulation.
- **Flame sensor fault** — A dirty or failed flame sensor caused the board to lose flame signal during operation, triggering repeated lockout attempts.
- **Gas supply issue** — Low gas pressure or a closed shut-off valve caused failed ignition sequences that culminated in lockout.

## Step-by-Step Fix {#fix}

1. **Check the diagnostic chart on the furnace door** — Before doing anything else, match the 1-flash pattern to your exact model's code table. Confirm whether 1 flash is normal or a fault code.
2. **If normal standby — verify thermostat call** — Ensure the thermostat is set above room temperature and the system switch is set to Heat. Check thermostat wiring at the furnace board for a proper W (heat) signal.
3. **If lockout — power cycle to reset** — Turn the furnace power switch off for 30 seconds, then back on. This resets the board and allows another ignition attempt. Watch the igniter sequence carefully.
4. **Inspect the flame sensor** — Locate the flame sensor rod in the burner assembly. Remove it and lightly clean the rod with fine steel wool or emery cloth. Reinstall and test.
5. **Check the gas supply** — Confirm the manual shut-off valve on the gas line to the furnace is fully open. Verify other gas appliances in the home have normal pressure.
6. **Watch the ignition sequence** — With power restored and a heat call active, observe: igniter should glow, gas valve should open, flame should establish within 4 seconds. If flame does not hold, the flame sensor or gas valve is the next target.
7. **Reset the system** — After repairs, restore power and verify the furnace completes a full heating cycle without returning to the 1-flash pattern.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor | [Amazon](https://www.amazon.com/s?k=Flame+sensor&tag=errorcodefixes-20) \| Universal or OEM; clean before replacing to confirm the part is actually faulty |
| Hot surface igniter | [Amazon](https://www.amazon.com/s?k=Hot+surface+igniter&tag=errorcodefixes-20) \| Replace if cracked or reading open resistance |
| Furnace control board | [Amazon](https://www.amazon.com/s?k=Furnace+control+board&tag=errorcodefixes-20) \| Last resort if power cycling and component replacement do not resolve lockout |
## When to Call a Pro

If the furnace locks out repeatedly after power cycling and you cannot identify a failed igniter, flame sensor, or gas supply problem, call a licensed HVAC technician. Persistent lockout may indicate a gas valve fault or combustion air issue that requires combustion analysis to diagnose safely.

## See Also

- [Trane Rooftop Unit Error Codes: Common Faults Guide](/posts/trane-rooftop-unit-error-codes/)
- [Trane ComfortR ER Error Code — Causes & Fix](/posts/trane-comfort-r-error-codes-er/)
- [Trane ComfortLink II Error Codes — Common Faults and Fixes](/posts/trane-comfortlink-ii-error-codes/)
- [Trane 9 Flashes Error Code — Causes & Fix](/posts/trane-9-flashes-error-code/)
