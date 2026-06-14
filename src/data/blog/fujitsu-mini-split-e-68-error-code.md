---
title: "Fujitsu Mini Split E:68 Error - Causes & Fix"
description: "E:68 on a Fujitsu mini split likely means outdoor coil thermistor fault. Most common fix: check sensor wiring and connector."
pubDatetime: 2026-05-31T01:14:34Z
modDatetime: 2026-05-31T01:14:34Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Outdoor coil thermistor sensor"
most_likely_cause: "Open or failed outdoor coil thermistor"
---

## Fujitsu Mini Split E:68 Error — What It Means

E:68 is not a standard documented error code in Fujitsu mini split service literature. The closest verified match is E6, which indicates an outdoor coil thermistor open circuit. This means the outdoor unit cannot read a valid temperature signal from the coil sensor. The fault locks the system out to prevent damage from operating without proper temperature feedback. If your display truly shows E:68, it may be model-specific, a misread display, or a code from a different Fujitsu product line. One Fujitsu heat pump platform uses E68 for high-pressure switch failure, but that has not been confirmed for mini split systems.

For the thermistor fault interpretation, the outdoor unit's control board expects a specific resistance range from the sensor. When the circuit is open, shorted, or out of range, the board triggers the fault. Common causes include damaged wiring from weather or pests, corroded connectors, a failed sensor, or less often a faulty control board input. The code will not clear until the root cause is repaired and the system is power-cycled.

[Jump to Fix](#fix)

## Common Causes

- **Open or failed outdoor coil thermistor** The temperature sensor itself has failed internally or has broken solder joints, causing an open circuit the board cannot read.
- **Damaged or pinched sensor wiring** Rodent damage, sharp edges, or weather degradation can cut or break the thin wires between the sensor and the control board.
- **Loose or corroded connector at outdoor unit** Moisture intrusion or vibration can corrode or unseat the thermistor plug at the outdoor PCB or sensor pigtail.
- **Outdoor control board input failure** The PCB's thermistor input circuit can fail due to power surge, moisture, or component wear, even when the sensor itself is good.
- **Airflow or refrigerant issue (if E68 is high-pressure related)** On some Fujitsu heat pump platforms, E68 indicates high-pressure switch fault from blocked airflow, dirty coil, or overcharge.

## Step-by-Step Fix {#fix}

1. **Power-cycle the system** by turning off the breaker or disconnect for 60 seconds, then restore power to clear any transient lockout.
2. **Inspect the outdoor unit** for visible damage, pest activity, pinched wires, or water intrusion around the control box and sensor locations.
3. **Locate the outdoor coil thermistor** (a small bead or clip-on sensor attached to the refrigerant line or coil fins) and check that its connector is fully seated and free of corrosion.
4. **Measure the thermistor resistance** at the sensor side and at the board connector with a multimeter, and compare to the service data for your model (typically a few kilohms at room temperature).
5. **Test continuity through the harness** from sensor to board to identify any open wires, and inspect for cuts, abrasion, or pinch points along the routing path.
6. **Replace the outdoor coil thermistor** if resistance is out of range or open, making sure to match the correct part number for your Fujitsu model.
7. **Replace the outdoor main PCB** if the sensor and wiring test good but the fault persists, indicating a failed input circuit on the control board.
8. **Check airflow and refrigerant** if you suspect the code is E68 high-pressure related: clean the condenser coil, verify fan operation, and test system pressures with gauges.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor coil thermistor sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-68-error-code&k=Outdoor+coil+thermistor+sensor&tag=errorcodefixes-20) \| Match the exact Fujitsu part number for your model to make sure correct resistance curve and mounting style. |
| Outdoor unit main control board / PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-68-error-code&k=Outdoor+unit+main+control+board+%2F+PCB&tag=errorcodefixes-20) \| Order by model and serial number from Fujitsu or an authorized distributor, board must match your outdoor unit exactly. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working inside energized electrical enclosures, do not own a multimeter and thermistor test data for your model, or if the fault returns after you have verified wiring and connectors. High-pressure faults require refrigerant gauges, recovery equipment, and EPA certification. A technician will have the correct Fujitsu service manual, can definitively identify whether your display shows E6, E68, or another code, and can safely measure live circuits and pressures. If your unit is still under warranty, any DIY board or sensor replacement may void coverage, so verify warranty status before ordering parts.
