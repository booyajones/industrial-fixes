---
title: "Cornelius Ice Machine Error Code — IMI / Cornelius Fault Diagnosis"
description: "Cornelius (formerly IMI Cornelius, now part of Marmon Foodservice Technologies) ice machines show E-series fault codes (E01 through E12 typically) when the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: cornelius-ice-machine-error-code
featured: false
draft: false
tags:
  - cornelius
  - production-sensor-fault
  - troubleshooting
---
## Quick answer

Cornelius (formerly IMI Cornelius, now part of Marmon Foodservice Technologies) ice machines show E-series fault codes (E01 through E12 typically) when the controller detects a production rate problem, sensor failure, or water/refrigerant system anomaly. Most common in the field are E04 (low water) and E06 (high condenser temp) — both addressable with proper preventive maintenance. About 40% of Cornelius fault calls in beverage-dispensing applications (the most common use case) are water-side issues, not refrigeration issues. Always check water supply and filtration before assuming refrigerant problems.

## What E-codes mean on Cornelius ice machines

Cornelius is one of the dominant beverage equipment manufacturers — their ice machines are typically paired with soda dispensers in fast-food and quick-service restaurants, where ice is dispensed directly into beverage cups. Common Cornelius ice machine models include the IAF, ICM, CCM, and the modular Multiplex line that pairs with a remote ice bin and soda dispenser combo.

Cornelius ice machines produce cube ice via a vertical evaporator plate design: a refrigerated stainless steel plate has cube-shaped indentations; water flows over the plate from a pump-driven spray header at the top, freezes into the indentations, and is released by a brief hot-gas defrost that warms the plate and drops the cube sheet into the bin.

The control board monitors: water pump current, water level in the sump, condenser temperature (inlet and outlet on water-cooled units), evaporator temperature, cycle time (each freeze-harvest cycle should complete in 12-25 minutes depending on model and ambient), and bin level (full sensor stops production).

Common E-codes:
- **E01** — Communication fault (UI to main board)
- **E02** — Evaporator temperature sensor open or shorted
- **E03** — Cycle time too long (slow production)
- **E04** — Low water / sump empty
- **E05** — Water pump current out of range
- **E06** — High condenser temperature (cutout, typically 165°F outlet)
- **E07** — Bin sensor fault
- **E08** — Compressor not running when commanded
- **E09** — Harvest failure (ice didn't release from plate)
- **E10-E12** — Manufacturer-internal / model-specific

## Common causes (ranked by frequency)

In Cornelius ice machine service (especially in QSR beverage applications):

1. **Inlet water filter clogged** — about 22%. Restaurants run thousands of gallons through these units; filter scale and sediment.
2. **Low water pressure or water supply restriction** — about 18%. Branched supply with too many appliances.
3. **Dirty condenser (air-cooled) or scaled condenser coil (water-cooled)** — about 18%.
4. **Failed water pump** — about 10%. Centrifugal pump bearings worn, motor failed.
5. **Failed water inlet valve** — about 8%.
6. **Failed evap temp sensor** — about 7%.
7. **Scaled evaporator plate** — about 5%. Hard water deposits on the plate reduce heat transfer.
8. **Refrigerant low** — about 5%. Sealed system leak.
9. **Failed bin level sensor** — about 4%.
10. **Failed control board** — about 3%.

**Pro nugget:** Cornelius ice machines in beverage-dispensing applications often share water supply with the soda dispenser, the coffee maker, and sometimes a tea brewer — all from a single 3/8-inch line behind the counter. The result: dynamic water pressure drops during peak service when multiple devices draw simultaneously. The ice machine's water inlet valve is designed for static 30-120 psi but performs poorly below 20 psi dynamic. **Diagnostic test**: install a pressure gauge on the ice machine inlet and watch it during peak rush — if it dips below 20 psi for more than 30 seconds at a time, you have a supply-side problem, not an ice machine problem. The fix is either splitting the supply line or upsizing it.

## Step-by-step fix

Before you start: shut off water at the inlet valve, disconnect power at the dedicated outlet or breaker.

1. **Read the fault history.** Enter service mode (hold the mode button for 5 seconds on most Cornelius IAF and ICM units). Display shows current fault and recent history.

2. **Verify water supply.** Disconnect the inlet line at the unit, hold in a bucket, briefly open water valve. Should give vigorous flow (1+ GPM). Weak flow = supply-side problem.

3. **Replace the inlet water filter.** Cornelius typically uses a 5-micron carbon block filter in a sediment-and-taste cartridge housing. Replace every 6 months minimum in busy restaurants. New filter is $35-65 — cheapest preventive component on the machine.

4. **For E06 (high condenser temp on air-cooled):** Pull the front panel, vacuum and clean the condenser fins. Verify the condenser fan is spinning.

5. **For E06 (water-cooled):** Verify cooling water flow to the condenser. Inspect for scale on the water-side of the condenser; descaling may be required (Cornelius sells an OEM descaling kit).

6. **For E04 (low water):** Pull the top cover, observe the water sump during a fill cycle. Inlet valve should energize, water should flow visibly into sump. If no flow, valve failed; if slow flow, supply or filter is restricted.

7. **For E05 (water pump current):** With the unit running, clamp an ammeter on a pump motor lead. Compare to spec (typically 0.5-1.5A for the small centrifugal pump on most Cornelius units). High = stuck/bound pump; low = motor failing.

8. **For E09 (harvest failure):** Inspect the evap plate. Heavy scale prevents ice release. Descaling required — drain water, fill with Cornelius descaling solution per instructions (typically a 30-60 minute soak), drain, rinse multiple times.

9. **For E02 (sensor):** Ohm-test the evap temp sensor. NTC 10kΩ thermistor at 70°F.

10. **Restore power and water, run a full cycle.** Watch for fault recurrence over 2-3 cycles.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Inlet water filter (5-micron carbon) | Cornelius 558800 | $35-65 | [PartsTown](https://www.partstown.com), [Amazon](https://www.amazon.com) |
| Water pump (centrifugal, 60W) | Cornelius 558705 | $185-285 | [PartsTown](https://www.partstown.com), [RepairClinic](https://www.repairclinic.com) |
| Water inlet valve (24VAC) | Cornelius 558710 | $85-145 | [PartsTown](https://www.partstown.com), [Amazon](https://www.amazon.com) |
| Condenser fan motor (air-cooled) | Cornelius 558720 | $145-225 | [PartsTown](https://www.partstown.com), [RepairClinic](https://www.repairclinic.com) |
| Evaporator temperature sensor (NTC) | Cornelius 558730 | $45-85 | [PartsTown](https://www.partstown.com), [Amazon](https://www.amazon.com) |
| Bin level sensor (photoelectric) | Cornelius 558740 | $115-185 | [PartsTown](https://www.partstown.com), [Amazon](https://www.amazon.com) |
| Control board (IAF series) | Cornelius 558750 | $385-585 | [PartsTown](https://www.partstown.com), [RepairClinic](https://www.repairclinic.com) |
| Spray header / water distribution tube | Cornelius 558760 | $85-145 | [PartsTown](https://www.partstown.com) |
| Descaling solution (1 gallon, food grade) | Cornelius 558770 | $35-55 | [PartsTown](https://www.partstown.com), [Amazon](https://www.amazon.com) |
| Pressure gauge (water inlet test) | Generic | $25-45 | [Home Depot](https://www.homedepot.com), [Amazon](https://www.amazon.com) |

PartsTown is primary distributor. Cornelius part numbers in newer Marmon Foodservice catalog may use different prefixes; cross-reference by serial-tag.

## When to call a professional

Call an EPA-certified commercial refrigeration tech when:

- Refrigerant pressure is out of spec. EPA Section 608 required.
- The compressor isn't running or is making unusual noise. Compressor work is sealed-system.
- The unit is paired with a remote ice bin and the issue spans both units. Cornelius modular systems have inter-unit communication that requires factory training to diagnose.
- E09 (harvest failure) persists after descaling. May indicate evaporator plate damage or hot-gas defrost solenoid failure.
- The unit is under Cornelius/Marmon warranty (typically 1 year parts and labor; some accounts have extended contract terms).

## FAQs

**My Cornelius is making cloudy ice. Is that an error?**
Cloudy ice = water has high mineral content or air content. Not a fault, but a sign that descaling and filtration upgrade may be needed.

**How often should the filter be changed?**
Every 6 months for low-volume use, every 3 months for high-volume QSR. Track gallons through the filter — most are rated for 5,000-10,000 gallons.

**My Cornelius E06 keeps coming back after I cleaned the condenser. Why?**
For water-cooled units, the issue may be on the cooling water side (scaled internal coil); for air-cooled, the kitchen ambient might be too high (above 100°F is outside spec for most Cornelius units). Verify ambient and consider relocation or supplemental cooling.

**Will softened water cause problems?**
Softened water replaces calcium with sodium — corrosive to some components. Cornelius specifies non-softened or RO-filtered water on most models.

**Difference between Cornelius and Manitowoc / Scotsman / Hoshizaki?**
Different evaporator architectures (Cornelius uses vertical plate; Manitowoc uses horizontal plate or grid; Scotsman uses tube-bank; Hoshizaki uses cell-style with auger). Diagnostic procedures and part numbers don't cross over.

## Related guides

- [Follett Ice Machine Error Code E1 — 7CI/Vu Fix](/posts/follett-ice-machine-error-code-e1)
- [Master-Bilt Walk-In Error Code — Controller Fault Fix](/posts/master-bilt-error-code)
- [Norlake Walk-In Error Code — Defrost Issue Fix](/posts/norlake-walkin-error-code)
