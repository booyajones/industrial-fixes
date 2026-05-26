---
title: "Goodman GMS96 Error Codes — Fault Code Guide"
description: "Goodman GMS96 furnace error codes: all flash codes for the popular 96% AFUE single-stage furnace with causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - goodman
---

## Goodman GMS96 Error Codes — What It Means

The Goodman GMS96 is a single-stage, 96% AFUE gas furnace and one of the most widely installed value-segment furnaces in North America. It uses a standard Goodman/Amana IFC control board with a diagnostic LED visible through the lower access panel. Like all 96% AFUE models, the GMS96 uses a secondary heat exchanger and condensate drain — making drain-related pressure switch faults the most common service issue.

[Jump to Fix](#fix)

## Flash Code Quick Reference

| Flashes | Meaning | Most Common Cause |
|---------|---------|------------------|
| 1 | Lockout — retries exceeded | Ignition failure |
| 2 | Pressure switch stuck open | Condensate trap, hose, or inducer |
| 3 | Pressure switch stuck closed | Hose routing or switch failure |
| 4 | High limit device open | Dirty filter or blocked airflow |
| 5 | Flame without call / roll-out | Gas valve or safety switch |
| 6 | Reversed line polarity | Fix wiring at disconnect |
| 7 | Gas valve energized — no call | Board or gas valve fault |
| 8 | Low flame sensor signal | Clean flame sensor rod |
| 9 | Igniter fault | Check igniter continuity |

## GMS96-Specific Issues

### 2 Flashes: Pressure Switch — GMS96
The GMS96 uses a plastic condensate trap assembly (Goodman part PCBBF118S and related variants). This trap is press-fit together and can develop hairline cracks at the joints over time, causing air leaks. Cracks may not be visible — submerse the trap in water while applying air pressure to check for bubbles.

The GMS96 pressure switch is typically rated at –0.60" WC. Check whether the inducer creates sufficient draft by temporarily connecting a manometer to the pressure switch port — draft should reach –0.60" or more during inducer operation.

### 4 Flashes: High Limit — GMS96
The GMS96 uses a low-static airflow design. It's sensitive to filter restriction. Goodman recommends checking the filter monthly during heating season. The GMS96 also uses a PSC blower motor — the 7.5 µF or 10 µF run capacitor is the first thing to check when the blower seems slow. A capacitor that reads below rated value (>10% low) means the motor isn't reaching full speed, which causes limit trips.

### 1 Flash: Ignition Lockout — GMS96
The GMS96 uses a silicon nitride hot-surface igniter (Goodman B1401015S or B1401015). Typical life is 5–7 years. If the unit is older, the igniter is the first thing to replace during a lockout diagnosis. Cold resistance should measure 40–90 ohms; a reading of OL means the element is cracked and open.

## Step-by-Step Fix {#fix}

**For 2-flash / pressure switch:**
1. Power off the furnace at the disconnect.
2. Locate the condensate drain trap (plastic U-shape, usually clear or white).
3. Disconnect the outlet drain line and pour water through — it should drain freely.
4. Inspect the trap body for cracks. If cracked, replace the trap assembly.
5. Check the pressure switch hose from the inducer outlet — replace if cracked or brittle.
6. Restore power and run a heat cycle.

**For 1-flash / lockout:**
1. Remove the flame sensor rod (single screw in the burner box) and clean with steel wool.
2. Verify gas supply is on and pressure is adequate.
3. Test the igniter — measure resistance with a multimeter. Replace if OL.
4. Power cycle and attempt to start.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot-surface igniter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-gms96-error-codes&k=Hot-surface+igniter&tag=errorcodefixes-20) \| Goodman B1401015S |
| Condensate trap | [Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-goodman-gms96-error-codes&tag=errorcodefixes-20) \| Goodman PCBBF118S or PCBBF133 |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-goodman-gms96-error-codes&tag=errorcodefixes-20) \| 0.60" WC — Goodman B1370169 or B1370138 |
| Flame sensor | [Amazon](https://www.amazon.com/dp/B0CZ7M9V4D?ascsubtag=ecf-goodman-gms96-error-codes&tag=errorcodefixes-20) \| Goodman 20285401 |
| Blower run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-goodman-gms96-error-codes&tag=errorcodefixes-20) \| 7.5 or 10 µF / 370V |
## When to Call a Pro
If you're seeing 7-flash or 5-flash codes (gas valve faults), or if the furnace has rolled out, stop using the furnace and contact a licensed HVAC technician before restarting.

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix](/posts/goodman-3-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)

## See Also

- [Goodman Furnace EE2 Error Code — Causes & Fix](/posts/goodman-furnace-ee2-error-code/)
- [Goodman Furnace 2 Flashes — Pressure Switch Stuck Closed Fix](/posts/goodman-furnace-2-flashes/)
- [Goodman Furnace E1 Error Code — Causes & Fix](/posts/goodman-furnace-e1-error-code/)
- [Goodman EE2 Error Code: Control Board Communication Fault Fix](/posts/goodman-ee2-error-code/)
