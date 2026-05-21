---
title: "Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix"
description: "Fault 126 on a Trane XV20i, XV18, or XL20i variable-speed heat pump means the outdoor unit's low-pressure switch opened — refrigerant suction pressure..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: trane-heat-pump-error-code-126
featured: false
draft: false
tags:
  - trane
  - low-pressure-cutout
  - troubleshooting
---
## Quick answer

Fault 126 on a Trane XV20i, XV18, or XL20i variable-speed heat pump means the outdoor unit's low-pressure switch opened — refrigerant suction pressure dropped below the safety threshold (typically 22-25 PSIG on R-410A, lower on R-454B units). The compressor stops to prevent damage. About 70% of the time it's a refrigerant leak, restricted airflow over the indoor or outdoor coil, or a stuck/contaminated TXV; the remaining 30% is a failed low-pressure switch, sensor wiring, or rare control-side faults.

## What 126 means on a Trane

Trane's ComfortLink II / XL1050 thermostats display numeric fault codes when paired with XV20i, XV18, and XL20i platforms. Fault 126 specifically maps to "Low Pressure Switch Open" — the outdoor unit's low-side pressure switch (cuts at approximately 22 PSIG, closes at 50 PSIG on R-410A units) has opened, signaling the variable-speed control to shut down the compressor.

The protective logic: the variable-speed inverter monitors low-side pressure continuously. If pressure drops below the cutout, it indicates either (a) insufficient refrigerant mass in the system, (b) inadequate heat absorption at the evaporator (low airflow, dirty coil), or (c) refrigerant flow restriction (plugged TXV, kinked line). Any of these will damage the compressor if firing continues — low suction pressure means low refrigerant return, which means inadequate motor cooling and lubrication.

Trane has a soft-fail behavior on 126: the system will attempt 3 retries with progressively longer waits before hard-locking out. The fault history captures both the soft-retry events and the eventual lockout. On XV20i specifically, this also blocks defrost initiation, so during winter the unit can ice up quickly while 126 is active.

Note: starting with the 2024 model-year refresh (some XV19/XR17 platforms), Trane is shipping R-454B units to comply with the EPA's 2025 refrigerant transition. Fault 126 cause set is the same, but cutout thresholds may differ slightly and refrigerant handling must follow A2L procedures.

## Common causes (ranked by frequency)

1. **Refrigerant undercharge from a slow leak** — about 30%. Most common cause. Leaks at flare fittings, Schrader cores, brazed joints, or coil rub-throughs.
2. **Restricted airflow over the indoor coil** — about 18%. Plugged filter, blocked return, evaporator coil iced or fouled.
3. **TXV stuck or contaminated** — about 12%. Power head bulb lost charge, or moisture/debris fouling the seat.
4. **Outdoor coil airflow restriction or dirty coil** — about 9%. Particularly in heat mode where outdoor coil is the evaporator.
5. **Low-pressure switch failed open** — about 8%. Switch contacts pitted, internal mechanism stuck.
6. **Pressure sensor wiring or connector fault** — about 7%. Loose spade or corroded pin.
7. **Reversing valve partial shift / stuck mid-stroke** — about 6%. Causes refrigerant to bypass in both directions.
8. **Indoor blower not running at correct speed** — about 5%. ECM blower fault, wrong tap, or stuck CFM setting.
9. **Outdoor ambient too cold for the unit's heat range** — about 3%. Some XV platforms cut out below 5°F outdoor.
10. **Refrigerant overcharge causing flood-back and oil migration** — about 2%. Rare but happens after a careless top-off.

Field nugget: I've seen this 300 times — XV20i in heat mode, throws 126 every morning around 5-6 AM when outdoor temps bottom out. Tech checks charge (looks fine), replaces the low-pressure switch, charges a little extra "just in case," 126 returns. The actual problem was almost always a filter the homeowner hadn't changed in 8 months. Indoor airflow drops below the minimum, indoor coil becomes the constraint, low side pulls down hard when the heat pump tries to extract heat from cold outdoor air with insufficient air-side heat at the indoor coil. New filter, system runs perfectly. Always check the filter and indoor blower CFM before touching the gauges. R-454B units make this lesson sharper because pressure-temperature relationship is slightly different — small undercharges show up faster as low-side pressure dropouts.

## Step-by-step fix

Safety first: kill power at the outdoor disconnect. Variable-speed inverters retain DC bus charge for 5+ minutes — wait before opening the inverter compartment. For R-454B (A2L) units, follow A2L handling: no ignition sources within 10 feet during refrigerant work, ventilate the work area, use A2L-rated leak detectors and recovery equipment. Refrigerant in any large concentration displaces oxygen; refrigerant burns can occur if liquid refrigerant contacts skin.

1. **Read full fault history.** On the ComfortLink II or XL1050 thermostat, navigate to MENU → SYSTEM REPORT → FAULT HISTORY. Note 126 timestamps and any related codes — 79 (refrigerant pressure sensor), 86 (compressor over-current), or 93 (outdoor coil temp). Multiple codes paint the picture.

2. **Check the indoor filter and airflow path.** Pull the air filter. If it's dirty, replace and run for 30 minutes before doing anything else. Open the return grille — verify nothing blocks it (furniture, drapes, supply registers all closed). Inspect the evaporator coil if accessible — should not be iced. If iced, shut down, let it thaw fully (several hours), then investigate cause.

3. **Inspect the outdoor coil.** Look for debris (leaves, grass clippings, cottonwood seed). Coil fins should be straight; minor combing OK. Wash the coil with a coil cleaner approved for R-410A or R-454B systems (do not use bleach or strong acids — strip aluminum). Pay attention to the lower bend where leaves accumulate.

4. **Verify indoor blower speed.** With the system running on a heat call, listen for the blower. ComfortLink can show indoor CFM in the service menu. Trane spec for XV20i ranges from 400-450 CFM/ton; for a 3-ton unit, you want 1200-1350 CFM measured. Low CFM = low coil temp = low refrigerant pressure. If blower is sluggish or noisy, check motor and capacitor (PSC variable platforms) or motor module communication (ECM platforms).

5. **Connect gauges and read pressures.** Use R-410A or R-454B-specific gauges as appropriate. With the system running in heat mode at design conditions, suction pressure should be 60-80 PSIG on R-410A in moderate ambient (40°F outdoor); R-454B will read slightly lower (55-75 PSIG) for equivalent conditions. Below 40 PSIG in heat = serious undercharge or restriction. Superheat target on XV20i is 8-15°F at the compressor; subcool at the condenser exit 8-15°F. Compare against rating plate target.

6. **Find the leak (if undercharged).** A 5-15% charge loss over a year is "normal" on heat pumps — leaks are everywhere. Use an electronic leak detector or fluorescent dye and UV light. Common spots: Schrader cores at the service ports, flare nuts at the indoor coil, brazed joints near the reversing valve, coil U-bend rubs. If you find and fix the leak, recover all refrigerant before brazing, replace the liquid line filter-drier, evacuate to 500 microns, and recharge to the rating plate's subcool target.

7. **Test the low-pressure switch.** With the system off and pressures equalized, ohm across the LPS terminals. A healthy switch reads closed (zero ohms) when both sides of the system are at standing pressure (above 50 PSIG). It opens at 22-25 PSIG. If it reads open at standing pressure, the switch is bad. If it reads closed but the system reports 126, the wiring or board may be at fault.

8. **Reset and run a full cycle.** Reset faults via the thermostat. Run a heat call (or cool call if it's summer) for 30 minutes. Monitor pressures, listen for compressor cycling, watch for 126 to return. If it doesn't return after 30 minutes of steady-state operation, the fix held.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Low-pressure switch (R-410A, XV20i) | Trane SWT03408 | $48-75 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Low-pressure switch (R-454B units) | Trane SWT03520 | $58-90 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| TXV (R-410A indoor coil, 3-ton) | Trane VAL07879 | $145-220 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Liquid line filter-drier (3/8") | Trane FLR01089 / Sporlan C-163-S | $35-58 | [RepairClinic](https://www.repairclinic.com), [Home Depot](https://www.homedepot.com) |
| Indoor ECM blower module (variable speed) | Trane MOD03046 | $410-620 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Reversing valve solenoid coil | Trane CCY01083 | $55-95 | [RepairClinic](https://www.repairclinic.com), [Home Depot](https://www.homedepot.com) |
| Outdoor control board (XV20i inverter) | Trane CNT05746 | $620-920 | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Schrader core (R-410A/R-454B rated) | Trane SCR00121 / generic 1/4" SAE | $5-12 (pair) | [RepairClinic](https://www.repairclinic.com), [Amazon](https://www.amazon.com) |
| Air filter (4" pleated, MERV 11) | Honeywell FC100A1029 | $25-45 | [Home Depot](https://www.homedepot.com), [Lowes](https://www.lowes.com) |

Note: Trane has been transitioning XV20i variants from R-410A to R-454B. Always check the rating plate before ordering — refrigerant-specific parts (pressure switches, TXVs, Schraders) differ. Crossing parts between refrigerants is not safe.

## When to call a professional

**Refrigerant leak repair on R-454B (A2L) units.** A2L work requires certified technicians, A2L-rated equipment, and proper ventilation. The repair itself is similar to R-410A work, but recovery, evacuation, and recharging procedures differ. Don't DIY.

**Suspected compressor damage.** Repeated 126 events can cause compressor oil migration and bearing wear. If the unit makes new noises (grinding, rattling at startup) or struggles to ramp up, internal damage may have occurred. Compressor diagnosis and replacement is pro work.

**TXV replacement.** Brazing the TXV into a sealed system requires nitrogen purge while brazing (to prevent oxidation inside the lines), proper evacuation (500 microns), and precise recharge. Without the right tools you'll trash the new TXV with debris.

**Multiple consecutive 126 events without obvious cause.** If you've verified airflow, charge, and the LPS, but 126 keeps returning, look for intermittent issues — control board glitches, reversing valve partial shifts, or compressor inverter faults. Pro-level diagnostics.

Never just top off refrigerant without finding the leak. EPA Section 608 requires leak repair if leak rate exceeds 10% per year on residential systems. Topping off is a violation and a short-term fix at best.

## FAQs

**My Trane runs fine for a few hours then trips 126 — what's the pattern?**
Probably airflow degrading over time during the cycle. Common with marginal filters that build up restriction as they run, or evaporator coils that ice progressively when refrigerant is slightly low.

**Can I just replace the low-pressure switch and call it done?**
Only if the switch is verified bad. A failed-open LPS will throw 126 with normal pressures. But if pressures are actually low, replacing the LPS removes the safety and lets the compressor run damaged. Always verify pressure first.

**Why does 126 happen more in winter?**
Heat pump operating in heat mode pulls heat from outdoor air. Cold ambient means low evaporator (outdoor coil) temperature and pressure. Any restriction or undercharge magnifies in cold weather. Summer cooling mode has more headroom.

**Is R-454B different to work on than R-410A?**
Operationally similar but A2L flammability adds work practice requirements: no ignition sources during open-circuit refrigerant work, A2L-rated tools, proper ventilation. Pressure-temperature curves are similar but not identical — use R-454B-specific PT charts.

**What's the difference between Fault 126 and Fault 79?**
126 is the binary low-pressure switch (opens at threshold). Fault 79 is the analog low-pressure sensor (variable reading). Some platforms have both; others use one or the other. They typically point to the same root causes but 79 includes additional information about how low pressure dropped.

## Related guides

- [Carrier Greenspeed A3 — Defrost Fault Fix](/posts/carrier-heat-pump-error-code-a3)
- [Goodman Heat Pump 2-Flash — Low Pressure Fix](/posts/goodman-heat-pump-error-code-2)
- [Mitsubishi P-Series H6 — Outdoor Fan Motor Fix](/posts/mitsubishi-heat-pump-error-code-h6)
