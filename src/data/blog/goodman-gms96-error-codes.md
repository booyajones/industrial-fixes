---
title: "Goodman GMS96 Error Codes — Fault Code Guide"
description: "Goodman GMS96 furnace error codes: all flash codes for the popular 96% AFUE single-stage furnace with causes and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
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

| [Flashes](https://www.amazon.com/s?k=Flashes&tag=errorcodefixe-20) | Meaning | Most Common Cause | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | --------- |---------|------------------|
| 1 | [Lockout — retries exceeded](https://www.amazon.com/s?k=Lockout%20%E2%80%94%20retries%20exceeded&tag=errorcodefixe-20) | Ignition failure |
| [2](https://www.amazon.com/s?k=2&tag=errorcodefixe-20) | Pressure switch stuck open | Condensate trap, hose, or inducer | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 3 | Pressure switch stuck closed | [Hose routing or switch failure](https://www.amazon.com/s?k=Hose%20routing%20or%20switch%20failure&tag=errorcodefixe-20) |  | 4 | [High limit device open](https://www.amazon.com/s?k=High%20limit%20device%20open&tag=errorcodefixe-20) | Dirty filter or blocked airflow |
| [5](https://www.amazon.com/s?k=5&tag=errorcodefixe-20) | Flame without call / roll-out | Gas valve or safety switch | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 6 | Reversed line polarity | [Fix wiring at disconnect](https://www.amazon.com/s?k=Fix%20wiring%20at%20disconnect&tag=errorcodefixe-20) |  | 7 | [Gas valve energized — no call](https://www.amazon.com/s?k=Gas%20valve%20energized%20%E2%80%94%20no%20call&tag=errorcodefixe-20) | Board or gas valve fault |
| [8](https://www.amazon.com/s?k=8&tag=errorcodefixe-20) | Low flame sensor signal | Clean flame sensor rod | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | 9 | Igniter fault | [Check igniter continuity](https://www.amazon.com/s?k=Check%20igniter%20continuity&tag=errorcodefixe-20) | ## GMS96-Specific Issues

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

## Parts Often Needed | Part | [Notes](https://www.amazon.com/s?k=Notes&tag=errorcodefixe-20) |  |------|-------|
| Hot-surface igniter | [Goodman B1401015S](https://www.amazon.com/s?k=Goodman%20B1401015S&tag=errorcodefixe-20) |  | Condensate trap | [Goodman PCBBF118S or PCBBF133](https://www.amazon.com/s?k=Goodman%20PCBBF118S%20or%20PCBBF133&tag=errorcodefixe-20) |  | Pressure switch | [0.60" WC — Goodman B1370169 or B1370138](https://www.amazon.com/s?k=0.60%22%20WC%20%E2%80%94%20Goodman%20B1370169%20or%20B1370138&tag=errorcodefixe-20) |  | Flame sensor | [Goodman 20285401](https://www.amazon.com/s?k=Goodman%2020285401&tag=errorcodefixe-20) |  | Blower run capacitor | 7.5 or 10 µF / 370V |

## When to Call a Pro
If you're seeing 7-flash or 5-flash codes (gas valve faults), or if the furnace has rolled out, stop using the furnace and contact a licensed HVAC technician before restarting.
