---
title: "Peerless Pinnacle Boiler Error Code Guide"
description: "Peerless Pinnacle boiler error codes explained. Learn what each code means, how to diagnose lockouts, sensor faults, and draft errors on Pinnacle condensing boilers."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - peerless
  - boiler
  - hvac
  - error-code
---

## Peerless Pinnacle Boiler Error Codes

The Peerless Pinnacle is a high-efficiency condensing gas boiler used in residential and light commercial applications. It uses a digital control board that displays fault codes when problems are detected. This guide covers all common Peerless Pinnacle error codes.

## Peerless Pinnacle Error Code Table

| [Code](https://www.amazon.com/s?i=industrial&k=Code&tag=errorcodefixes-20) | Description | Common Cause |
|---|---|---|
| E01 | High limit trip | Overtemperature, poor circulation |
| E02 | Ignition failure | No gas, failed igniter, flame sensor |
| E03 | Flame loss | Flame drops out during operation |
| E04 | Low water pressure | System pressure below 8 PSI |
| E05 | Draft/pressure switch fault | Blocked flue, failed inducer |
| E06 | Return temperature sensor fault | Failed NTC thermistor |
| E07 | Supply temperature sensor fault | Failed supply sensor |
| E08 | Condensate backup | Blocked drain, frozen line |
| E09 | False flame signal | Stuck gas valve, nuisance signal |
| E10 | Blocked flue fault | Flue pressure switch won't close |
| E11 | Lockout (manual reset required) | After 3+ safety trips |
| E12 | Control board internal fault | Board failure |

## Most Common Pinnacle Codes

### E02 — Ignition Failure

The most common service call. Clean the flame sensor rod first — this alone fixes E02 in over half of cases. If cleaning doesn't help:
1. Verify gas supply
2. Test hot surface igniter (should read 40–120 ohms cold)
3. Check draft pressure switch closes when inducer runs
4. Verify gas valve opens (24VAC at valve terminals during trial for ignition)

### E04 — Low Water Pressure

The Pinnacle has a water pressure switch that requires minimum 8–10 PSI to allow operation. If the pressure gauge reads below this:
- Check for system leaks
- Add water to the system at the fill valve
- Verify the pressure reducing valve (PRV/feed valve) is set correctly (typically 12–15 PSI)
- Check for an open expansion tank

A leaking pressure relief valve will dump water continuously and keep tripping E04.

### E05 — Draft/Pressure Switch Fault

The combustion blower must prove draft before ignition is allowed. E05 means the pressure switch didn't close.
- Check condensate drain (backs up and blocks switch port)
- Inspect all small hoses from inducer to switch
- Verify flue and intake pipes are unobstructed (clear from outside)
- Test the pressure switch (should close under applied suction)

### E08 — Condensate Backup

Pinnacle boilers produce significant condensate (up to 2 gallons per hour at high firing rates). E08 means the condensate detection system has detected water backup.
- Clear the condensate trap — disconnect and blow out
- Verify drain line is continuous and slopes to floor drain
- In freezing spaces, insulate drain line or use heat trace
- Clean the condensate neutralizer cartridge if installed (replace annually)

### E11 — Hard Lockout

After 3 or more safety trips (E01, E02, E03) within a short window, the Pinnacle escalates to E11 which requires manual reset. This is the control's way of saying "stop cycling and find the problem."

Reset: press and hold RESET button for 5 seconds. Then diagnose the underlying fault before restarting.

## Reset Procedure

1. Press and hold the RESET button on the Pinnacle control panel (typically red or labeled RST)
2. Hold for 3–5 seconds until the display clears
3. The boiler will begin a startup sequence automatically

## Checking System Pressure (E04 Prevention)

The pressure gauge on a residential hot water heating system should read:
- **Cold system:** 12–15 PSI
- **Hot system (180°F):** 18–22 PSI
- **Pressure relief valve:** opens at 30 PSI

If your cold pressure is below 10 PSI, add water. If you're adding water frequently (more than twice a year), you have a leak or a failed expansion tank.

## When to Call a Technician

- E11 (lockout) that keeps returning
- E12 (board fault) — requires board replacement
- E02 that returns after cleaning flame sensor and verifying gas
- Any code accompanied by gas smell — call the gas company first

## Related Articles

- [Boiler Lockout Error Codes: All Brands Guide](/posts/boiler-lockout-error-codes/)
- [Buderus Boiler Fault Code A1 — Causes & Fix](/posts/buderus-boiler-fault-code-a1/)
- [Burnham Alpine Boiler Error Code Guide — Causes & Fix](/posts/burnham-alpine-error-codes/)
- [Burnham Boiler E1 Lockout Code Fix](/posts/burnham-boiler-e1-lockout-code/)
- [Burnham Boiler E2 Error Code — Causes & Fix](/posts/burnham-boiler-e2-error-code/)
