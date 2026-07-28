---
title: "Hoshizaki KM-1301SAH Error Codes — Commercial Ice Machine Fault Guide"
author: "Marcus Webb"
pubDatetime: 2026-04-24T21:00:00Z
modDatetime: 2026-04-24T21:00:00Z
slug: hoshizaki-km-1301sah-error-codes
featured: false
draft: false
tags:
  - hoshizaki
  - ice-machine
  - commercial-refrigeration
  - food-service
  - error-codes
description: "Hoshizaki KM-1301SAH error codes explained — this large crescent-cube commercial ice machine communicates faults through LED blink codes on the control board. Here's how to diagnose and fix each one."
money_part: "Water inlet valve"
---

## Error Codes: Hoshizaki KM-1301SAH

**What it means:** The Hoshizaki KM-1301SAH is a large-capacity commercial undercounter/modular cube ice machine producing approximately 1,301 lbs of crescent ice per day. Like all Hoshizaki KM-series machines, it communicates faults via diagnostic LED blink codes on the main control board, visible behind the front panel. Count the number of LED flashes in a repeating sequence to identify the fault.

This machine is common in high-volume bar, restaurant, and hotel operations. Parts are expensive and lead times can be long — accurate diagnosis before ordering parts saves significant downtime and cost.

## Hoshizaki KM-1301SAH Fault Code Reference

### E1 — Water Supply Fault
The water trough did not fill within the allotted time. The most common fault on KM-series machines in high-use environments. See the [Hoshizaki E1 error code guide](/posts/hoshizaki-e1-error-code/) for full diagnosis.

**Common causes on KM-1301SAH specifically:** Water pressure at the inlet is adequate for smaller machines but marginal for the KM-1301SAH's higher volume demand (minimum 20 PSI, recommended 40–80 PSI). High-volume operations may need a booster pump.

### E2 — High Water Level Fault
The water level in the trough exceeded the safe operating level. Causes:
- Failed water inlet valve (stuck open or leaking)
- Float switch stuck in the down position (reads "not full" even though trough is full)
- Overflow condition from a backed-up drain

### E3 — Ice-Making Cycle Too Long
The freeze cycle exceeded the maximum allowed time (approximately 30 minutes on the KM-1301SAH). This indicates reduced refrigeration capacity:
- Low refrigerant charge (leak)
- Dirty or scaled evaporator
- Condenser coil fouled with debris (air-cooled) or scale (water-cooled)
- Ambient temperature exceeding rating (max 100°F for KM-1301SAH-A)
- Failed or undersized condenser fan motor

### E4 — Harvest Cycle Too Long
The harvest cycle (where the ice releases from the evaporator) took too long. Causes:
- Low refrigerant charge preventing hot gas from reaching temperature
- Failed hot gas solenoid valve
- Evaporator scale buildup holding ice on the plate
- Harvest thermostat or thermistor out of calibration

### E5 — Low Ice Level (Full-Time Alarm)
The bin thermostat or ice level probe detected ice for an extended period without the bin filling — suggesting the ice is melting faster than the machine can produce, or the bin thermostat/level probe is mispositioned.

### E6 — Bin Thermostat Fault
The bin thermostat or ice level sensor is open or short-circuit. On KM-series machines, this typically means the bin thermostat needs replacement or its mounting position has shifted.

### Flashing Lights — Defrost/Safety Mode
If all LEDs flash simultaneously, the machine is in a safety shutdown:
- High-pressure cutout tripped (condenser problem)
- Low-pressure cutout tripped (refrigerant leak or TXV issue)
- Compressor thermal overload tripped

## Common Causes on KM-1301SAH

- **Scale buildup** — The KM-1301SAH produces a high ice volume, requiring more water throughput than smaller machines. Hard water scale accumulates faster. Hoshizaki recommends descaling every 6 months in hard water areas (>200 ppm TDS). Scale on the evaporator causes E3 and E4.
- **Condenser fouling** — Air-cooled models (KM-1301SAH-A) pull significant airflow. In kitchen environments, grease-laden air coats the condenser fins. Clean condenser coils quarterly.
- **Water-cooled condenser scaling** — Water-cooled models (KM-1301SAH-WB) develop scale on the condenser water passages over time, reducing heat rejection and causing E3.
- **Float switch failure** — At this production volume, the float switch cycles more frequently than on smaller machines, wearing it out faster. E1 and E2 both relate to float switch or water valve issues.
- **Refrigerant loss** — Large commercial machines have more refrigerant circuit connections (service valves, solenoids) that can develop minor leaks over years of vibration. E3 and E4 with a clean condenser strongly suggest refrigerant loss.

## Step-by-Step Fix {#step-by-step-fix}

1. **Note the exact LED blink count.** Count the flashes on the diagnostic LED (located on the main control board). Write down the number before opening the machine further.

2. **For E1 (water supply) — start with the basics.** Check incoming water pressure (20 PSI minimum, test with a gauge at the inlet valve). Clean the inlet valve screen strainer. Manually lift and lower the float switch arm to confirm it moves freely. Verify the drain is not backing up into the trough.

3. **For E3 (long freeze cycle) — check the condenser first.** On air-cooled models, inspect the condenser coil for lint, grease, or debris. Clean with coil cleaner and a stiff brush or compressed air. On water-cooled models, check that condenser water flow is adequate (3–5 gpm at normal load for KM-1301SAH). A dirty condenser resolves E3 in commercial kitchens approximately 60% of the time.

4. **For E4 (long harvest) — check the hot gas solenoid.** The hot gas solenoid valve allows hot refrigerant gas to flow over the evaporator during harvest. With the machine in harvest, hold your hand near the hot gas line — you should feel heat surging when the solenoid opens. No heat surge = stuck-closed solenoid.

5. **Perform a descale cycle.** If the machine has not been descaled recently, run Hoshizaki's recommended descale procedure using Hoshizaki Scale Remover (or equivalent food-safe descaler). Drain the trough, add descaler per instructions, run the machine in cleaning mode for the specified cycle time, then flush thoroughly. Heavy scale can cause E3, E4, and even false E1 readings (scale blocking the float switch).

6. **Check refrigerant charge.** For persistent E3 after condenser cleaning and descaling, check refrigerant pressures with a manifold gauge set. Hoshizaki KM-1301SAH uses R-404A or R-448A depending on production date. Low suction pressure and low subcooling confirm refrigerant loss — this requires a licensed refrigeration technician and EPA 608 certification.

7. **Test the bin thermostat.** For E5 and E6, disconnect the bin thermostat wire connector and measure resistance across the thermostat contacts. At ambient temperature (above ~45°F for the bin thermostat setting), the contacts should be open (OL on multimeter). If reading continuity at ambient temp, the thermostat is stuck closed and needs replacement.

8. **Replace the control board only after all other diagnostics.** The KM-1301SAH control board (approximately $400–$700) is a last resort. False fault codes on a good board are rare — if you've confirmed the sensor, refrigerant, and mechanical systems are healthy and faults persist, then the board becomes suspect.

## Parts Often Needed {#parts-often-needed}

| Part | Part Number | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| Water inlet valve | 4A5375-02 | $80–$120 | [Amazon](https://www.amazon.com/dp/B0CNFHW1ZJ?ascsubtag=ecf-hoshizaki-km-1301sah-error-codes&tag=errorcodefixes-20) \| Parts Town |
| Float switch | 4A3624-01 | $40–$65 | [Amazon](https://www.amazon.com/dp/B005D4RFEM?ascsubtag=ecf-hoshizaki-km-1301sah-error-codes&tag=errorcodefixes-20) \| Parts Town |
| Bin thermostat | 4A6599-01 | $35–$55 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-1301sah-error-codes&k=Hoshizaki+4A6599-01+bin+thermostat&tag=errorcodefixes-20) \| Parts Town |
| Hot gas solenoid valve | 4A0559-01 | $150–$250 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-1301sah-error-codes&k=Hoshizaki+4A0559-01+hot+gas+solenoid&tag=errorcodefixes-20) \| Parts Town |
| Condenser fan motor (air-cooled) | 4A1410-01 | $120–$200 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-hoshizaki-km-1301sah-error-codes&tag=errorcodefixes-20) \| Parts Town |
| Main control board | 2A2665-01 | $400–$700 | Parts Town \| Hoshizaki authorized distributor |
| Hoshizaki Scale Remover (6 pack) | 9381-10 | $30–$50 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-hoshizaki-km-1301sah-error-codes&k=Hoshizaki+scale+remover+9381-10&tag=errorcodefixes-20) \| Restaurant supply |

## When to Call a Professional

Any fault code related to refrigerant (persistent E3 or E4 after mechanical fixes) requires an EPA 608-certified technician to handle the refrigerant system. The KM-1301SAH uses R-404A or R-448A — these are HFC refrigerants requiring certification to purchase and handle. Additionally, this machine's size and complexity make refrigerant leak detection and recharge a job requiring proper equipment and experience. For a 1,300 lb/day machine in a commercial kitchen, downtime is measured in hundreds of dollars per hour — professional diagnosis is usually more cost-effective than trial-and-error parts replacement.

> **Pro tip:** Hoshizaki's KM-1301SAH has a service log mode that stores the last 15 fault events with timestamps. Access it by holding the START/STOP button for 10 seconds with the machine off. Review the fault history before any repair — intermittent faults that only appear under load (like E3 during peak production hours) are almost always refrigeration capacity problems, not sensor failures.
