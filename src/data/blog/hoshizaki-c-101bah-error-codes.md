---
title: "Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker Error Codes — Full Fault Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T22:00:00Z
modDatetime: 2026-04-24T22:00:00Z
slug: hoshizaki-c-101bah-error-codes
featured: false
draft: false
tags:
  - hoshizaki
  - ice-machine
  - commercial-refrigeration
  - food-service
  - error-codes
description: "Hoshizaki C-101BAH and C-201BAH countertop crescent cube ice maker error codes explained — diagnose and fix E1 through E6 and F-series safety faults on the most common compact commercial ice machine in hotels, bars, and restaurants."
---

## Error Codes: Hoshizaki C-101BAH / C-201BAH Countertop Ice Maker

**What it means:** The Hoshizaki C-101BAH (87 lbs/day) and C-201BAH (~169 lbs/day) are self-contained countertop crescent cube ice machines used extensively in hotel rooms, break rooms, small bars, and food-service prep areas. Like all Hoshizaki machines, they communicate faults through LED blink codes on the main control board — count the repeating flashes to identify the fault.

These compact machines pack full commercial refrigeration systems into a countertop footprint. When a fault code appears, the machine shuts down ice production and the diagnostic LED begins flashing. Because these units serve continuous-demand environments (hotel bars, coffee stations, convenience stores), downtime is high-urgency. Correct diagnosis before ordering parts prevents costly mistakes on these relatively small machines.

**How to read the blink codes:** With the machine in fault state, observe the red diagnostic LED on the control board (accessed by removing the front panel). Count the short flashes in each repeating group. A pause between groups separates each count. E-codes use a separate LED or alternate flash pattern depending on production year.

---

## Hoshizaki C-101BAH / C-201BAH Fault Code Reference

### E1 — Water Supply Fault

The water trough did not fill to the required level within the allotted time (approximately 5–8 minutes). This is the most common fault on C-series countertop units.

**Common causes:**
- Low water pressure at inlet (minimum 20 PSI required — countertop units are particularly sensitive because the water valve opens time-based rather than flow-based)
- Clogged water inlet valve screen strainer (mineral scale in hard-water areas blocks flow at the screen)
- Failed water inlet valve solenoid (coil burned open, or valve body stuck closed due to scale)
- Float switch stuck in the "full" position (trough reads full even though it's empty)
- Kinked or frozen supply line

See also: [Hoshizaki E1 error code guide](/posts/hoshizaki-e1-error-code/) for the full diagnostic procedure common to all Hoshizaki KM and C-series machines.

---

### E2 — High Water Level Fault

The water level in the trough exceeded the safe limit. The overflow sensor or float switch detected water above the normal operating level.

**Common causes:**
- Failed water inlet valve stuck open (most common — valve coil burns open causing the plunger to remain de-energized/open)
- Float switch stuck in the "empty" position (reads "low" continuously, causing the valve to keep filling)
- Drain partially blocked, causing slow drainage and trough overflow during a fill cycle

---

### E3 — Freeze Cycle Too Long

The ice-making (freeze) cycle exceeded the maximum allowed time. On C-101BAH/C-201BAH units, the normal freeze cycle runs 15–22 minutes depending on water and ambient temperature. E3 triggers when this time limit is exceeded by approximately 50%.

**Common causes:**
- Dirty condenser coil — C-series countertop units have a small condenser in a tight enclosure. Lint, grease, and dust accumulate quickly, especially in hotel and restaurant environments. This is the #1 cause of E3 on C-series machines.
- Ambient temperature too high — C-101BAH rated for max 90°F ambient. C-201BAH rated for max 90°F. Machines placed near ovens, in hot utility closets, or in poorly ventilated cabinets overheat.
- Low refrigerant charge — A slow refrigerant leak reduces cooling capacity gradually. E3 appearing on a clean machine that was previously running well strongly suggests refrigerant loss.
- Scale buildup on evaporator — Hard-water scale acts as insulation, slowing ice formation and extending freeze time.
- Weak or failed compressor — Compressors in countertop machines work harder per square inch than in larger units. After 5–10 years, valve wear reduces compression efficiency.

---

### E4 — Harvest Cycle Too Long

The harvest phase (where hot refrigerant gas is circulated to release ice from the evaporator) exceeded its time limit.

**Common causes:**
- Failed or stuck-closed hot gas solenoid valve (most common mechanical cause)
- Low refrigerant charge (insufficient hot gas temperature to release ice)
- Heavy evaporator scale holding ice on the surface
- Harvest thermostat out of calibration or failed open

---

### E5 — Low Ice Production / Extended Bin Full

The ice bin thermostat or ice level probe indicated the bin was full for an extended period without the detected ice level dropping — suggesting the bin is not dispensing ice as expected, or the bin sensor is mispositioned/failed.

On C-series machines used in hotel ice dispensers, this can also indicate the dispenser mechanism is blocked or the bin is over-full and bridging.

---

### E6 — Bin Thermostat / Ice Level Sensor Fault

The bin thermostat or ice level sensor is reading open circuit or short circuit. The controller cannot determine whether the bin is full or empty, so the machine halts as a safety measure.

**Common causes:**
- Bin thermostat bulb dislodged from its mounting clip (common after cleaning or servicing)
- Thermostat failed (open circuit)
- Wiring to bin thermostat chafed or cut
- Ice bridging holding the thermostat activated (machine thinks bin is full)

---

### F1 — High-Pressure Safety Cutout

The high-pressure safety switch tripped. This is a safety fault, not a controller-detected condition — the refrigerant circuit pressure exceeded the cutout limit.

**Common causes:**
- Extremely dirty condenser (most common on C-series in dusty environments)
- Condenser fan not running (failed motor or blade)
- Ambient temperature far above rated limit
- Non-condensables in refrigerant circuit (air/moisture contamination — typically a sign of prior improper service)
- Overcharge of refrigerant

**Important:** F1 requires finding and correcting the root cause before the high-pressure switch can be manually reset. Do not repeatedly reset without fixing the underlying cause — repeated high-pressure trips damage the compressor.

---

### F2 — Freeze Cycle Safety Fault

A safety cutout during the freeze cycle detected a dangerous operating condition (e.g., low-pressure cutout, or a combined time/temperature safety).

---

## Common Causes on C-101BAH / C-201BAH Specifically

- **Condenser cleaning neglect:** The C-series countertop form factor places the condenser in a tight enclosure with limited airflow. In hotel rooms, kitchens, and break rooms, lint and dust accumulate fast. Hoshizaki recommends condenser cleaning every 6 months minimum — in dusty environments, quarterly.
- **Hard water scale:** These machines are often installed without in-line water filtration. In hard-water areas (>150 ppm TDS), scale on the evaporator fins and water distribution components builds up within 6–12 months. Hoshizaki recommends descaling every 6 months.
- **Improper installation clearance:** The C-series requires 6 inches of clearance on sides and 12 inches at top for proper airflow. Machines built into cabinets or pushed against walls overheat and trigger E3 and F1 repeatedly.
- **Ice bridging:** In high-humidity environments, ice can bridge across the bin opening, preventing new ice from falling to the bottom. The machine reads "full" (E5) even when usable ice supply is low.

---

## Step-by-Step Fix {#step-by-step-fix}

1. **Record the exact blink code.** Before touching anything, count the diagnostic LED flashes carefully. Write the count. If you've missed it, power cycle the unit — the code will reappear when the machine tries to restart.

2. **For E1 (water supply) — check pressure first.** Attach a pressure gauge to the inlet supply line. Minimum 20 PSI; optimal 40–60 PSI. Low pressure is common in hotel rooms with multiple fixtures running. Then remove and clean the inlet valve screen strainer (fine brass mesh at the valve inlet fitting). In hard-water areas, this screen clogs within a year.

3. **For E3 (long freeze cycle) — clean the condenser first.** Remove the front panel. Locate the condenser (typically on the right or left side, depending on model year). Use a coil brush and/or compressed air to remove lint and dust from the fins. On C-series machines in hotel environments, a heavily clogged condenser resolves approximately 70% of E3 faults.

4. **Descale the machine.** If the machine has not been descaled in the past 6 months, run Hoshizaki's recommended descale procedure before further diagnostics. Drain the trough, add Hoshizaki Scale Remover or an equivalent nickel-safe food-grade descaler per the concentration instructions, run a full cleaning cycle, then flush thoroughly with clean water. Scale on the evaporator and water distributor tube causes E3 and E4 and can cause false E1 readings.

5. **Test the float switch.** With the power off, manually move the float switch arm up and down. It should move freely without sticking. Connect a multimeter to the float switch terminals: when the float is in the "up" (full) position, the switch should be open (OL). When float is down (empty), switch should be closed (continuity). Sticky or reversed readings = failed float switch.

6. **Check the hot gas solenoid for E4.** With the machine running in a harvest cycle, hold your hand on the refrigerant line going to the hot gas solenoid outlet side — you should feel hot gas surge through within 1–2 minutes of harvest start. No heat surge = stuck-closed solenoid. Test the coil with a multimeter: typical resistance 10–30 Ω. Open circuit (OL) = burned coil.

7. **Check refrigerant pressure for persistent E3/E4.** If the condenser is clean, the evaporator is scaled, and harvesting is weak, connect a manifold gauge set to the service ports. C-101BAH uses R-134A; C-201BAH uses R-404A (check the nameplate). Low suction pressure with low subcooling = refrigerant leak. This step requires EPA 608 certification.

8. **Replace the bin thermostat for E5/E6.** Unclip the bin thermostat from its mounting location inside the bin area. Test resistance: at ambient temperature above the bin thermostat cutout point (~45°F), contacts should be open. At temperatures below the setpoint, contacts should be closed. Failed = replace. Also verify the thermostat bulb is securely mounted in its clip and making full contact with the bin air space.

---

## Parts Often Needed {#parts-often-needed}

| Part | Notes | Typical Cost | Where to Buy |
|------|-------|--------------|--------------|
| Water inlet valve | Check C-101 vs C-201 part number | $45–$85 | [Amazon](https://www.amazon.com/dp/B0CNFHW1ZJ?ascsubtag=ecf-hoshizaki-c-101bah-error-codes&tag=errorcodefixes-20) \| Parts Town |
| Float switch assembly | Common failure on high-use units | $35–$60 | [Amazon](https://www.amazon.com/dp/B005D4RFEM?ascsubtag=ecf-hoshizaki-c-101bah-error-codes&tag=errorcodefixes-20) \| Parts Town |
| Bin thermostat | Verify temp rating matches model | $30–$50 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-c-101bah-error-codes&k=Hoshizaki+bin+thermostat+C-101BAH&tag=errorcodefixes-20) \| Parts Town |
| Hot gas solenoid valve | Match refrigerant type (R-134A or R-404A) | $80–$160 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-c-101bah-error-codes&k=Hoshizaki+hot+gas+solenoid+valve+countertop+ice+maker&tag=errorcodefixes-20) \| Parts Town |
| Condenser fan motor | Verify shaft diameter and RPM | $60–$110 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-hoshizaki-c-101bah-error-codes&tag=errorcodefixes-20) \| Parts Town |
| Hoshizaki Scale Remover | 9381-10, food-safe, nickel-safe | $30–$50 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-c-101bah-error-codes&k=Hoshizaki+scale+remover+9381-10&tag=errorcodefixes-20) \| Restaurant supply |
| Main control board | Last resort after sensor/mechanical diagnosis | $200–$450 | Parts Town \| Hoshizaki authorized distributor |

---

## When to Call a Professional

Any refrigerant-related fault — persistent E3 after condenser cleaning and descaling, or F1 high-pressure cutout — requires an EPA 608-certified technician. The C-101BAH uses R-134A and the C-201BAH uses R-404A (verify on nameplate); both are HFC refrigerants requiring certification to purchase and legally handle. Refrigerant leak detection on these compact machines requires electronic leak detectors since the refrigerant circuit is fully enclosed. Additionally, if the compressor has failed or the system has been contaminated with air or moisture, professional evacuation and recharge is mandatory.

> **Pro tip:** Hoshizaki C-series machines have a fault history accessible by holding the SERVICE button (if equipped) or checking the LED blink pattern sequence. The machine stores the last few fault events. On machines with the newer SafeGuard II control board, you can access diagnostic mode by pressing CLEAN → CLEAN → WASH in sequence while the machine is powered off — this displays the fault log. Use this before ordering any parts.

---

## See Also

- [Hoshizaki E1 Error Code — Water Supply Fault](/posts/hoshizaki-e1-error-code/)
- [Hoshizaki E3 Error Code — Freeze Cycle Fault](/posts/hoshizaki-e3-error-code/)
- [Hoshizaki E4 Error Code — Harvest Fault](/posts/hoshizaki-e4-error-code/)
- [Hoshizaki KM-515 Error Codes](/posts/hoshizaki-km-515-error-codes/)
- [Hoshizaki KM-330 Error Codes](/posts/hoshizaki-km-330-error-codes/)
- [Ice Machine Error Code Lookup](/posts/ice-machine-error-code-lookup/)

## Related Articles

- [Hoshizaki DKM-500 Cube Dispenser Error Codes — Fault Code Diagnostic Guide](/posts/hoshizaki-dkm-500-error-codes/)
- [Hoshizaki Ice Machine E1 Error Code — Water Inlet Fix](/posts/hoshizaki-e1-error-code/)
- [Hoshizaki E2 Error Code — Harvest Fault Fix](/posts/hoshizaki-e2-error-code/)
- [Hoshizaki E3 Error Code — Causes & Fix](/posts/hoshizaki-e3-error-code/)
- [Hoshizaki E4 Error Code — Causes & Fix](/posts/hoshizaki-e4-error-code/)
