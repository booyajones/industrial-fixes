---
title: "Trane XE80 Furnace Error Codes — Fault Code Guide"
description: "Trane XE80 furnace error codes: flash code meanings and fixes for this popular 80% AFUE single-stage furnace still common in the field."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane XE80 Error Codes — What It Means

The Trane XE80 is an older 80% AFUE single-stage gas furnace that was widely installed throughout the 1990s and 2000s. Millions remain in service. It uses a Trane IFC control board with a diagnostic LED inside the lower access panel. Because the XE80 is an 80% furnace, it does **not** have a secondary heat exchanger or condensate drain — many pressure switch issues common on 90%+ furnaces don't apply here.

[Jump to Fix](#fix)

## Flash Code Quick Reference

| Flashes | Meaning | Notes |
|---------|---------|-------|
| 1 | Lockout — retries exceeded | Check igniter and gas |
| 2 | Pressure switch open | Check inducer and hose |
| 3 | High-limit or roll-out open | Filter, airflow, or roll-out |
| 4 | Ignition failure | Igniter or gas supply |
| 5 | Flame without call | Gas valve leaking |
| 6 | Reversed polarity | Fix incoming wiring |
| 7 | Gas valve problem | Valve or board fault |
| 8 | Low flame signal | Clean flame sensor |
| Slow flash | Standby | Normal |

## Common Causes for XE80-Specific Issues

### 2 Flashes: Pressure Switch (XE80 — 80% Furnace)
On the XE80, there is no condensate drain — so a 2-flash fault is almost always: (1) a cracked pressure switch hose between the inducer housing and the pressure switch, (2) a failed inducer motor or blower wheel, or (3) a dead pressure switch. The XE80 uses an atmospheric combustion chamber with an induced draft blower — the pressure switch monitors draft, not condensate.

### 3 Flashes: High Limit (XE80)
The XE80 has a single primary heat exchanger. Overheating is typically caused by: restricted airflow (dirty filter or closed registers), a failing PSC blower motor, or a weak blower capacitor. XE80 blower motor capacitors are a known wear item — a 5 µF or 7.5 µF run capacitor is inexpensive and worth replacing on any unit over 10 years old.

### 4 Flashes: Ignition Failure
The XE80 uses a hot-surface igniter (silicon carbide on older units, silicon nitride on later production). Silicon carbide igniters have a characteristic fragility — even a brief power bump can crack them. Resistance should read 40–80 ohms cold for silicon nitride; silicon carbide reads much lower (typically 20–40 ohms) and can be harder to test accurately.

## Step-by-Step Fix {#fix}

**For 2-flash / pressure switch fault:**
1. Power off the furnace.
2. Locate the rubber pressure switch hose — on the XE80 it's a short hose (6–10") between the inducer outlet and the pressure switch on the top of the inducer box.
3. Inspect the hose for cracks, especially near the fittings. Replace with 3/8" rubber vacuum hose if damaged.
4. Disconnect the wire from the pressure switch and test with a multimeter. Apply suction with a vacuum pump — switch should close.
5. Restore power and verify the inducer starts cleanly on a call for heat.

**For 3-flash / high limit fault:**
1. Replace the air filter.
2. Verify all supply and return air registers are open.
3. Test the blower run capacitor with a capacitor meter — replace if reading is more than 10% below rated value.
4. Verify the blower wheel is clean and spins freely.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot-surface igniter | [Amazon](https://www.amazon.com/s?i=industrial&k=Hot-surface+igniter&tag=errorcodefixes-20) \| Trane CNT1011, CNT05473 or OEM equivalent |
| Blower run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?tag=errorcodefixes-20) \| 5–10 µF / 370V depending on motor |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| 0.35"–0.50" WC for XE80 |
| Pressure switch hose | [Amazon](https://www.amazon.com/dp/B0CPTHML1N?tag=errorcodefixes-20) \| 3/8" ID rubber vacuum hose |
## When to Call a Pro
The Trane XE80 is aging — most units are 15–25+ years old. If you're facing repeated ignition failures, a cracked heat exchanger is possible. A CO detector test and heat exchanger inspection by a licensed tech is worth scheduling on any XE80 over 20 years old, especially before another heating season.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
