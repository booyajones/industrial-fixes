---
title: "Burnham/U.S. Boiler Fault Code 2 — Ignition Lockout Fix"
description: "Fault Code 2 on a Burnham (now U.S. Boiler Company) 7-Series, 8-Series, ESC2, or Alpine gas-fired boiler indicates an ignition lockout — the integrated..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: burnham-error-code-2
featured: false
draft: false
tags:
  - burnham
  - hydronic
  - residential
  - ignition-lockout
  - troubleshooting
---
## Quick answer

Fault Code 2 on a Burnham (now U.S. Boiler Company) 7-Series, 8-Series, ESC2, or Alpine gas-fired boiler indicates an ignition lockout — the integrated ignition control attempted ignition through its full trial sequence (typically three tries on Alpine, single trial on 7/8 Series) and never proved flame. The boiler is locked out and will not retry until reset. Most calls trace to a fouled flame sensor, gas pressure problem, or weak ignitor; on Alpine condensing units, blocked condensate or vent is a frequent secondary cause.

## What Fault 2 means on a Burnham

Burnham (rebranded U.S. Boiler Company starting 2015, though the boilers are still marketed under the Burnham name) uses two distinct fault display systems depending on the platform:

- **7-Series / 8-Series / ESC2 atmospheric cast-iron boilers:** the Honeywell S8610 or S8910 intermittent pilot ignition module flashes a fault LED. Two flashes = ignition lockout (sometimes labeled "Fault 2" on newer ESC2 control documentation).
- **Alpine ALP series condensing wall-hung/floor-mount boilers:** the Sage 2.2 or 2.3 boiler control displays a numeric code. "F02" or "Fault 2" indicates "Ignition Lockout — No Flame Sensed."

The ignition sequence: the boiler calls for heat, pre-purge fan runs (Alpine only — 7/8 Series are atmospheric draft and skip this), the gas valve opens, spark or HSI fires, and the flame sensor circuit (rectification) must prove flame within the trial window. Standard trial-for-ignition (TFI) is 4 seconds on 7/8 Series, 7 seconds on Alpine. If no flame is proved, the gas valve shuts. Alpine retries up to 3 times before locking out; 7/8 Series typically locks out after the first miss.

Flame rectification spec on Burnham Alpine is 1.5-6 µA DC with a healthy reading being 3-5 µA. The Sage control's lockout threshold is 0.8 µA. On 7/8 Series, the S8610M module needs at least 1.0 µA.

## Common causes (ranked by frequency)

1. **Dirty or oxidized flame sensor rod** — about 32%. Surface fouling drops microamp reading below threshold.
2. **Insufficient gas supply pressure during firing** — about 18%. Inlet pressure sags below 5" w.c. natural gas / 11" w.c. propane during demand.
3. **Cracked HSI (Alpine) or bad spark electrode (7/8 Series)** — about 15%. Ignitor doesn't reach temp or spark is shorted.
4. **Blocked vent or condensate trap (Alpine only)** — about 10%. Causes secondary ignition issues by triggering airflow faults that manifest as flame failures.
5. **Failed gas valve** — about 8%. Honeywell VK4115 (Alpine) or VR8200 (7/8 Series) drifts or fails to open.
6. **Wet flame sensor ceramic / cracked insulator** — about 7%. Especially common after high-humidity off seasons or condensate leaks.
7. **Bad ignition control module** — about 5%. S8610M (7/8) or Sage 2.x board (Alpine).
8. **Reversed line polarity** — about 3%. Hot/neutral swapped — kills flame rectification.
9. **Cracked HV ignition cable** — about 2%. Spark arcing to ground inside the boiler cabinet.

Field nugget: I've seen this 300 times — Alpine boiler, fall startup, throws Fault 2 right out of the gate after summer shutdown. Customer didn't run the boiler May through September; condensate trap dried out, condensate water sat in the vent's low spot, and now there's enough corrosion on the flame rod tip that microamp signal won't break 1 µA on first attempt. The fix isn't always parts — sometimes it's just pulling and polishing the rod, refilling the condensate trap with water, and giving it a clean fire. But if you see this pattern in a closed/seasonal home (vacation property, hunting cabin), schedule a fall startup service so you're not chasing it on a freezing call-out.

## Step-by-step fix

Safety first: kill power at the boiler service switch and close the manual gas shutoff before opening the burner section. On Alpine condensing units, the condensate is acidic (pH 3.5-4.5) — wear gloves and eye protection when handling the trap. Carbon monoxide risk is highest during marginal ignition where unburned gas may have entered the heat exchanger; ventilate the boiler room before extended troubleshooting. A portable CO monitor in the room is good practice.

1. **Confirm the fault and check history.** On 7/8 Series, count the LED flash pattern on the S8610M module — two flashes between pauses = ignition lockout. On Alpine, the Sage display shows the code; scroll the history menu to see if other faults preceded (F09 vent fault, F08 condensate, F07 air pressure).

2. **Verify gas supply.** Confirm the manual valve at the boiler is open. Fire another gas appliance to confirm utility supply. Tap a manometer into the gas valve's inlet pressure port. Natural gas should read 5-10.5" w.c. static and not drop below 5" w.c. during firing. Propane: 11-13" w.c. static, no lower than 11" w.c. during firing. Burnham specifically derates Alpine performance below 5" w.c. inlet — codes will appear erratically.

3. **Clear the condensate trap (Alpine only).** Power off, locate the condensate trap (clear plastic U or bottle trap, depending on Alpine model — ALP080-150 has the bottle trap, ALP210+ has U-trap). Remove and flush with warm water. Refill with clean water before reinstalling — running the trap dry lets flue gas migrate where it shouldn't and triggers vent faults that can manifest as Fault 2 on retry sequences.

4. **Pull and clean the flame sensor.** Power off. On Alpine, the flame sensor sits in the bottom of the combustion chamber, one ceramic-bodied rod with a single wire. On 7/8 Series with intermittent pilot, the flame sensor is integrated with the pilot assembly (Q345A pilot/sensor combo). Clean the sensor rod with 0000 steel wool or a green Scotch-Brite pad. Inspect the ceramic insulator for hairline cracks — replace the whole assembly if cracked.

5. **Inspect the ignitor / electrode.** On Alpine, the HSI is nitride, located in the combustion chamber adjacent to the burner. Check resistance cold — should be 40-90Ω. Open circuit means cracked. On 7/8 Series, check the spark electrode gap: 0.10-0.125" (2.5-3.2 mm). Look for carbon tracking down the side of either component (sign of HV leakage).

6. **Verify the burner is clean.** On 7/8 Series atmospheric, look for blocked main burner ports, spider webs, or rust flakes — vacuum the burner tray. On Alpine, do not touch the mesh burner with anything — inspect visually for damage and replace the burner gasket if disturbed during inspection.

7. **Check line polarity and ground.** With a multimeter or 3-light receptacle tester, verify hot-to-ground at 115-125 VAC and neutral-to-ground under 2V. Reversed polarity kills flame rectification on rectification-based systems. Verify the boiler chassis ground bond — Burnham specifies a continuous ground from the chassis ground lug to the panel ground bar, less than 1 Ω.

8. **Reset and watch a full cycle with instruments.** Reset the boiler: on 7/8 Series with S8610M, kill thermostat call for 30 seconds and reapply (or cycle power); on Alpine, press and hold RESET on the Sage display 3-5 seconds. Set thermostat for a heat call. With manometer on gas valve and microamp meter on flame sensor lead, watch ignition: pre-purge (Alpine) → ignition trial → flame sensed → modulation. Measure manifold pressure during firing — Alpine spec is approximately 3.5" w.c. natural gas / 10.0" w.c. propane at high fire, but exact spec varies by model (consult the install manual). Flame current should hold steady at 3-5 µA DC.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Flame sensor (Alpine ALP) | Burnham 8236157U / U.S. Boiler 8236157 | $55-90 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Pilot/sensor assembly (7/8 Series) | Honeywell Q345A-1305 | $65-110 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Hot surface igniter (Alpine, nitride) | Burnham 8236185U | $75-130 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Spark electrode (7/8 Series IID) | Burnham 8236092U | $30-50 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Ignition control module (S8610M) | Honeywell S8610M-3008 | $130-200 | [Supply House](https://www.supplyhouse.com), [Amazon](https://www.amazon.com) |
| Sage 2.2/2.3 boiler control (Alpine) | Burnham 109173-01 | $580-780 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Gas valve (Alpine modulating) | Honeywell VK4115V-1014 | $310-460 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |
| Condensate trap kit (Alpine) | Burnham 109094-01 | $45-75 | [Supply House](https://www.supplyhouse.com), [PexUniverse](https://www.pexuniverse.com) |

Note: Alpine flame sensors are not interchangeable across the model range — ALP080 through ALP285 use 8236157U, but the larger ALP399-740 commercial models use a different sensor assembly. Always cross-check against your serial-tagged install manual.

## When to call a professional

**Ignition issues with simultaneous combustion smell, soot, or yellow flames.** This indicates a combustion-air or gas-pressure issue serious enough that you risk CO production. A pro with a combustion analyzer can pin down O2, CO, CO2, and stack temp — Alpine should hit ~9.0% CO2, <100 ppm CO air-free, ~140-180°F stack on low fire return temp.

**You've replaced the sensor and HSI but Fault 2 persists.** Next likely fault is the gas valve or Sage board. Both require setup procedures, and the Sage board may need firmware/parameter migration via the U.S. Boiler PC tool. That's pro work.

**Smell of gas at any time during troubleshooting.** Stop, shut off the manual valve, ventilate, and call the gas utility. Do not relight until you've leak-tested every joint disturbed during the repair (Alpine's gas valve has two test ports — both seal with brass plug screws, both need to be snug after manometer work).

**Boiler is older than 25 years and parts are scarce.** Some 7-Series cast-iron boilers are pushing 30+ years old. Section failures and replacement cost lean heavily toward "replace the boiler" rather than continued repair. Get a quote on a modern condensing unit — efficiency gain alone pays back in 5-8 years.

## FAQs

**Why does my Alpine throw Fault 2 only on cold mornings?**
Cold-day demand spikes drop utility gas pressure. If your supply is already marginal, a 25°F outdoor temp can take inlet pressure below 5" w.c. and cause flame failure. Have the utility verify regulator setting, or upsize the supply line.

**Can I clear Fault 2 by cycling power?**
Yes on most platforms — cycling power resets the lockout. But repeatedly clearing without fixing the cause is dangerous: each retry is a chance for unburned gas to accumulate in the heat exchanger.

**My boiler fires sometimes after a Fault 2 — should I worry?**
Yes. Intermittent ignition is a "marginal flame proving" failure pattern. Microamp reading is borderline and will get worse. Clean or replace the flame sensor and verify gas pressure under firing load.

**Is Burnham still selling these boilers?**
Yes. U.S. Boiler Company owns Burnham as a brand. Current product is the Alpine, the ESC2, and the Series 8 atmospheric cast iron. Parts are widely stocked through Supply House, PexUniverse, and wholesale distributors.

**Should I use silicone or PTFE on the gas piping?**
Yellow PTFE tape rated for gas, or a fuel-rated pipe dope (Rectorseal #5 or Megaloc). Never silicone. Tape and dope should be on male threads only, two to three wraps of tape, never overhanging into the pipe bore.

## Related guides

- [Weil-McLain Code 1 — No Flame Sensed Fix](/posts/weil-mclain-error-code-1)
- [Lochinvar Knight E02 — High Limit / Stack Temp Fix](/posts/lochinvar-error-code-e02)
- [Navien NPE/NCB Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003)
