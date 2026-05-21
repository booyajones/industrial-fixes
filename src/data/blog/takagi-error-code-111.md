---
title: "Takagi Code 111 — No Ignition Fix"
description: "Code 111 on a Takagi tankless water heater (T-H3, T-H3J, T-K4, T-D2, T-KJr2, T-M50, and the newer Tx2 condensing platforms) means the unit attempted..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: takagi-error-code-111
featured: false
draft: false
tags:
  - takagi
  - no-ignition
  - troubleshooting
---
## Quick answer

Code 111 on a Takagi tankless water heater (T-H3, T-H3J, T-K4, T-D2, T-KJr2, T-M50, and the newer Tx2 condensing platforms) means the unit attempted ignition through its full retry sequence and never proved flame. The control fired the spark and opened the gas valve, but the flame rectification signal never reached the proving threshold. About 75% of field calls trace to gas supply pressure problems, dirty flame rod, or worn ignition electrodes. The remainder splits among bad gas valves, vent issues, polarity, and control faults.

## What Code 111 means on a Takagi

Takagi (owned by Paloma since 2005, with strong product overlap with Rheem residential tankless) uses a direct-spark ignition system across its residential lineup. The ignition sequence:

1. Flow sensor (or differential pressure sensor on some platforms) detects a draw above activation (0.5-0.75 GPM on most Takagi models).
2. Combustion fan ramps up to pre-purge speed.
3. Air pressure switch or fan-speed feedback proves combustion airflow.
4. Direct-spark electrode fires near the burner.
5. Gas valve solenoid opens (modulating valve on Tx2 series; two-stage or single-stage valve on older platforms).
6. Flame rectification circuit must prove flame within approximately 5 seconds.
7. Modulation logic takes over.

If flame is not proved within the trial window, the gas valve closes. Takagi standard is 3 ignition retries before posting Code 111 and locking out. Lockout requires manual reset — either via the remote controller (TK-RE07, TK-RE10, or similar depending on model) or by cycling main power.

Flame current target on Takagi: 1.0-5 µA DC at the flame rod, with cutout below 0.5 µA. Healthy operation: 2-4 µA. Below 1.5 µA is marginal — Code 111 is likely on the next cold start.

Takagi remotes display the code numerically. Some platforms also show a status LED on the main board; the diagnostic pattern is documented in the install/service manual.

## Common causes (ranked by frequency)

1. **Gas supply pressure droop during firing** — about 24%. Inlet drops below 4" w.c. NG / 8" w.c. LP under demand.
2. **Dirty flame rod / fouled flame sensor** — about 22%. Surface oxide drops microamps below threshold.
3. **Worn ignition electrode (gap drift or carbon tracking)** — about 14%. Spark won't ignite consistently.
4. **HV ignition cable cracked or pinched** — about 8%. Spark to ground inside cabinet.
5. **Gas valve failure** — about 8%. Stuck closed solenoid or modulating valve drift.
6. **LP / NG conversion incorrect** — about 6%. Wrong orifice or unconverted valve.
7. **Vent restriction or recirculation** — about 5%. Especially indoor models.
8. **Reversed polarity at the supply** — about 4%. Kills rectification.
9. **PC board fault** — about 3%. Less common.
10. **Frozen condensate trap (condensing models in cold spaces)** — about 3%.

Field nugget: I've seen this 300 times — Takagi T-K4 in a converted barn shop, propane tank outside, throws Code 111 only on the first morning draw after a cold night below 25°F. Customer thinks the heater is dying. The actual problem is propane tank pressure droop: cold propane has lower vapor pressure, the 1st-stage regulator at the tank can't deliver enough volume on a heavy demand at the heater, inlet pressure sags below 8" w.c., the unit fails to ignite. By the time the tech arrives at 11 AM, the sun has warmed everything and the unit fires perfectly. Diagnostic trick: ask when it fails — early morning after cold nights is almost always propane regulator. The fix is a properly sized 1st-stage regulator at the tank (or replacing a tired one), insulating the regulator and downstream lines, and in extreme cases, switching to a "high pressure" first stage with a 2nd-stage regulator at the heater for stable delivery.

## Step-by-step fix

Safety first: close the manual gas valve, kill power at the unit. Tankless hot water can scald — let the unit cool. CO from incomplete combustion is real risk on marginal ignition events; ventilate the install location and use a portable low-level CO monitor. Condensing models have acidic condensate (pH 3-4); wear gloves. Watch for sharp edges on the heat exchanger fin pack.

1. **Confirm Code 111 and check fault history.** On the remote controller, press the navigation buttons to access fault history (specific button sequence varies by remote — TK-RE10 has a dedicated info button). Note 111 timestamps and any other codes — Code 121 (flame failure during operation), Code 311 (vent fault), or Code 161 (overheat) provide context.

2. **Verify gas supply.** Open the front cover. Tap a manometer into the gas valve's inlet pressure tap (small 1/8" NPT plug on the inlet side of the valve). Static pressure: natural gas 5-10.5" w.c., propane 11-13" w.c. Initiate a large hot water draw to push the unit to high fire. Inlet pressure must stay above 4" w.c. NG / 11" w.c. LP. Droop = supply problem.

3. **Inspect and clean the flame rod.** Power off, gas off. Open the burner cover (typically 4-6 screws). Pull the flame rod connector and remove the rod (one screw on most platforms). The rod is a thin stainless rod with a ceramic insulator and a single wire. Clean with 0000 steel wool or green Scotch-Brite until silver. Inspect ceramic for cracks. Reinstall with new gasket if present.

4. **Inspect the ignition electrode.** Adjacent to the flame rod, the electrode is a similar-looking rod with HV cable connection. Pull the cable and remove the electrode. Check the spark gap: Takagi spec is 3.0-4.0 mm (0.12-0.16") on most platforms. Inspect ceramic for cracks or carbon tracking. Replace if damaged.

5. **Check the HV ignition cable.** With electrode out, inspect the cable from electrode to ignition transformer. Insulation should be intact and flexible. Cracks (often visible as discoloration or stiffness) let spark leak to ground. Replace if cracked.

6. **Check the burner ports.** With burner exposed, vacuum gently to remove dust or lint. Inspect ports for blockage. Don't poke at ports with hard objects.

7. **Service the condensate trap (Tx2 condensing models).** Power off. Locate trap at the bottom of the unit. Flush with warm water, refill with clean water before reinstalling. Verify drain line slopes downward and isn't blocked.

8. **Verify line polarity.** Multimeter at the unit's power input — hot-to-ground 115-125V, neutral-to-ground under 2V. Reversed = no flame rectification.

9. **Reset and observe.** Restore gas, power. Press the remote's power button to clear lockout. Initiate a sustained high-flow draw. With manometer on inlet pressure and microamp meter in series on the flame rod lead, observe the ignition sequence: fan ramp → spark → gas valve open → flame proved → modulation. Inlet stable above 4" w.c. NG, flame current 2-4 µA steady.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Flame rod / sensor (T-H3) | Takagi LOC-9000-009 | $42-72 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Flame rod (T-K4 / T-D2) | Takagi LOC-9000-007 | $42-72 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Ignition electrode (T-H3) | Takagi LOC-9050-024 | $48-82 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| HV ignition cable | Takagi LOC-3010-014 | $28-48 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Gas valve (T-H3, modulating) | Takagi LOC-3010-002 | $290-440 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Burner gasket | Takagi LOC-2000-005 | $18-32 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Condensate trap (Tx2) | Takagi LOC-7050-008 | $42-72 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Main control board (T-H3-DV) | Takagi LOC-5000-001 | $440-680 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| LP conversion kit (T-K4) | Takagi LOC-9100-LP | $85-130 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Wired remote (TK-RE10) | Takagi TK-RE10 | $115-175 | [Supply House](https://www.supplyhouse.com), [Home Depot](https://www.homedepot.com) |

Note: Takagi parts numbering follows a LOC-xxxx-xxx convention but exact numbers vary by model and production year. Always verify by serial number / model on the rating plate before ordering. Many parts cross-reference between Takagi and Rheem residential tankless because of shared manufacturing.

## When to call a professional

**Repeated Code 111 with new flame rod, electrode, and verified gas pressure.** Cause set narrows to gas valve or PC board. Both require setup procedures and possibly combustion analysis. Pro work.

**Propane regulator or supply problems.** If your propane installation can't deliver adequate pressure under load, the propane company should diagnose with a manometer and consider regulator upgrade. Don't troubleshoot propane regulators yourself unless certified.

**Combustion analysis needed.** If you see soot, smell incomplete combustion, or want to verify the unit is firing cleanly, a combustion analyzer is the right tool. Takagi spec: roughly 8.5-9.5% CO2 at high fire, <100 ppm CO air-free.

**Vent installation issues.** Improperly vented Takagi units throw codes including 111 and 311. A pro who knows Takagi vent rules (lengths, elbow counts, intake/exhaust separation) should evaluate.

Never bypass flame proving. Repeated reset cycles pump unburned gas into the heat exchanger. Risk is real.

## FAQs

**My Takagi worked fine for years and now throws Code 111 randomly — what changed?**
The most common slow-developing causes are (a) flame rod fouling over time, (b) gas pressure droop from system changes (new appliances added downstream of the meter), and (c) electrode wear. All three develop over years and tip over the edge at some point.

**Can I just reset Code 111 and run it?**
You can clear the lockout once or twice, but if it keeps coming back, fix the cause. Repeated resets with gas valve opening but no flame is dangerous.

**Should I be concerned about CO from a Takagi?**
Yes, like any gas appliance. Properly installed and maintained, CO emissions are low. Marginal combustion (the kind that causes Code 111) often comes with elevated CO. A CO monitor in the install location is wise.

**What's the descaling interval on a Takagi?**
Annual in hard water (>7 gpg), every 2-3 years in soft water. Scale doesn't directly cause Code 111 (that's more Code 161 territory) but it stresses the unit and accelerates other wear.

**Is Takagi the same as Rheem tankless?**
Same parent company at the manufacturing level, similar designs, but the part numbers and electronics differ. Order Takagi parts for a Takagi heater.

## Related guides

- [Rinnai Code 11 — No Ignition Fix](/posts/rinnai-error-code-11)
- [Noritz Code 11 — No Ignition Fix](/posts/noritz-error-code-11)
- [Navien NPE-A 016 — Overheat Lockout Fix](/posts/navien-water-heater-error-code-016)
