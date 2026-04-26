---
title: "Rheem Split System Heat Pump Error Codes — RA14, RA15, RP15 Fault Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: rheem-heat-pump-error-codes
featured: false
draft: false
tags:
  - rheem
  - heat-pump
  - hvac
  - error-codes
description: "Rheem heat pump error codes E1, E2, E4, E5 for RA14, RA15, and RP15 series. Diagnose indoor coil sensor, outdoor coil sensor, high pressure, and low pressure faults."
---

## Rheem Split System Heat Pump Error Codes

The **Rheem RA14, RA15, and RP15 series** split system heat pumps display alphanumeric fault codes via a communicating thermostat (such as the Rheem EcoNet or compatible systems) when a fault occurs. These codes help technicians and homeowners quickly identify what has failed and whether service is needed immediately.

This guide covers the four most common Rheem heat pump error codes and what to do about each one.

---

## Common Rheem Heat Pump Error Codes

| Code | Description |
|------|-------------|
| E1 | Indoor Coil Temperature Sensor Fault |
| E2 | Outdoor Coil Temperature Sensor Fault |
| E4 | High Pressure Trip |
| E5 | Low Pressure Trip |

---

## E1 — Indoor Coil Temperature Sensor Fault {#e1-indoor-coil-sensor}

**What it means:** The NTC thermistor monitoring the indoor coil (evaporator in cooling, condenser in heating) has failed or is reading outside its expected range. The system controller cannot properly manage refrigerant metering, defrost cycles, or freeze protection without a valid indoor coil temperature reading.

**Common causes:**
- Thermistor has failed (open or short circuit)
- Sensor lead wires damaged (pinched in cabinet, corroded connector)
- Sensor has slipped out of its clip on the indoor coil
- Control board NTC input circuit has failed

**Diagnosis and fix:**
1. Turn off the system at the thermostat and disconnect power at the indoor unit disconnect or breaker.
2. Locate the indoor coil sensor — it is a small clip-on thermistor attached to the evaporator coil. Inspect that it is firmly seated in its clip and making good contact with the coil surface.
3. Disconnect the sensor connector from the control board. Measure resistance across the sensor terminals. At room temperature (70°F/21°C), a healthy NTC thermistor typically reads 10–12 kΩ. An open circuit (OL on multimeter) or near-zero reading indicates a failed sensor.
4. Inspect the wire leads from sensor to control board for pinching, cuts, or corrosion at the connector. A corroded connector pin can cause an intermittent open circuit.
5. If sensor and wiring test good, the control board input circuit may be at fault — contact a Rheem technician.

**Parts:**
- [Rheem Heat Pump Indoor Coil Sensor NTC Thermistor](https://www.amazon.com/s?k=Rheem+heat+pump+indoor+coil+thermistor+sensor+replacement&tag=errorcodefixes-20)

---

## E2 — Outdoor Coil Temperature Sensor Fault {#e2-outdoor-coil-sensor}

**What it means:** The outdoor coil (condenser in cooling, evaporator in heating) temperature sensor has failed. This sensor is critical for defrost cycle control in heat pump mode — without it, the outdoor coil can ice up severely and damage the unit.

**Common causes:**
- Thermistor failed due to moisture exposure (outdoor environment)
- Sensor lead wire damaged by UV, rodents, or vibration
- Connector corroded at the control board
- Physical damage to the sensor from hail, debris, or improper service

**Diagnosis and fix:**
1. Shut off power to the outdoor unit at the disconnect box. Wait 5 minutes for capacitors to discharge.
2. Locate the outdoor coil sensor — it is clipped to the outdoor coil and wired back to the outdoor unit control board.
3. Inspect the sensor and its clip for physical damage. Outdoor sensors are exposed to weather and are more prone to physical damage than indoor sensors.
4. Disconnect the sensor connector from the outdoor board and measure thermistor resistance. At 70°F (21°C), expect 10–12 kΩ. Open circuit or zero resistance = failed sensor.
5. Inspect the entire wire run from the coil to the control board for rodent damage — this is a common cause of E2 faults in rural installations.
6. Replace the sensor. Outdoor coil sensors are typically inexpensive (under $25) and straightforward to replace — the hardest part is routing the new wire through the outdoor unit cabinet.

**Parts:**
- [Rheem Outdoor Coil Sensor / NTC Thermistor](https://www.amazon.com/s?k=Rheem+outdoor+coil+temperature+sensor+thermistor+RA14+RA15&tag=errorcodefixes-20)

---

## E4 — High Pressure Trip {#e4-high-pressure}

**What it means:** The refrigerant high-side pressure has exceeded the high pressure switch setpoint (typically 400–450 PSI for R-410A systems). The system shuts down to prevent compressor damage and refrigerant line rupture.

**Common causes:**
- Dirty or blocked condenser coil (outdoor unit) — most common cause in cooling mode
- Condenser fan not running or running slowly
- Refrigerant overcharge
- Restriction in the liquid line (kinked line, failed TXV/EEV, plugged filter drier)
- Outdoor ambient temperature extremely high (above 115°F), exceeding system design limits
- Non-condensables (air or nitrogen) in the refrigerant circuit

**Diagnosis and fix:**
1. Inspect the outdoor coil for debris. A coil clogged with cottonwood, leaves, or grass clippings will cause E4 in cooling mode. Rinse the coil from inside-out with a garden hose (after shutting off power) or use coil cleaner.
2. Verify the condenser fan is running and spinning in the correct direction (should pull air upward through the coil). A failed run capacitor is a very common cause of fan issues.
3. Check that adequate clearance exists around the outdoor unit — minimum 12–18 inches on all sides and 48 inches above. Nearby bushes or fences can recirculate hot discharge air back to the coil.
4. If the coil is clean and the fan is running, the system needs refrigerant pressure checked by a licensed HVAC technician with a certified manifold gauge set. Overcharge or non-condensables require professional service.
5. In heating mode, E4 can occur if the outdoor ambient is extremely cold and the defrost cycle is not functioning correctly — causing ice buildup that blocks airflow.

**Parts:**
- [High Pressure Switch for R-410A Heat Pump](https://www.amazon.com/s?k=high+pressure+switch+R410A+heat+pump+replacement&tag=errorcodefixes-20)
- [Condenser Fan Motor Capacitor 5/45 MFD](https://www.amazon.com/s?k=condenser+fan+motor+capacitor+5+45+mfd+heat+pump&tag=errorcodefixes-20)

---

## E5 — Low Pressure Trip {#e5-low-pressure}

**What it means:** The refrigerant low-side (suction) pressure has dropped below the low pressure switch setpoint (typically 50–55 PSI for R-410A in cooling). Low suction pressure means the compressor is not getting adequate refrigerant, which causes slugging, overheating, and premature failure.

**Common causes:**
- Refrigerant leak — the most serious and most common cause of E5
- Dirty air filter or blocked indoor unit (reduced airflow causes the evaporator to run too cold)
- Frozen evaporator coil (from low airflow or previous low-charge operation)
- Faulty TXV/EEV not opening properly
- Blower motor not running or running slowly in the indoor unit
- Low pressure switch failed closed

**Diagnosis and fix:**
1. **Check the air filter first.** A heavily restricted filter is the most common non-refrigerant cause of E5. Replace the filter and allow a frozen coil 1–2 hours to thaw (with power off) before restarting.
2. Inspect the indoor unit for ice accumulation on the evaporator coil. If frozen, turn off cooling but leave the fan running to thaw the coil.
3. Verify the indoor blower is running at the correct speed. Reduced airflow from a dirty blower wheel or a failing motor will cause suction pressure to drop.
4. If the system runs for more than an hour with a clean filter, good airflow, and still trips E5, there is likely a refrigerant leak. Have a licensed technician leak-check the system, recover the remaining charge, repair the leak, and recharge to factory specification.
5. Do not simply add refrigerant to a system without finding and repairing the leak — it is illegal (EPA Section 608) and will only delay the inevitable compressor failure.

**Parts:**
- [Low Pressure Switch R-410A Heat Pump](https://www.amazon.com/s?k=low+pressure+switch+R410A+heat+pump+HVAC&tag=errorcodefixes-20)
- [Pleated Air Filter MERV 11 (various sizes)](https://www.amazon.com/s?k=pleated+air+filter+MERV+11+furnace+heat+pump&tag=errorcodefixes-20)

---

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Indoor Coil Sensor (NTC) | $15–$30 | [Amazon](https://www.amazon.com/s?k=Rheem+heat+pump+coil+thermistor+sensor&tag=errorcodefixes-20) |
| Outdoor Coil Sensor (NTC) | $15–$30 | [Amazon](https://www.amazon.com/s?k=Rheem+outdoor+unit+coil+thermistor&tag=errorcodefixes-20) |
| Condenser Fan Motor Capacitor | $15–$40 | [Amazon](https://www.amazon.com/s?k=dual+run+capacitor+heat+pump+condenser+fan&tag=errorcodefixes-20) |
| Condenser Fan Motor | $80–$200 | [Amazon](https://www.amazon.com/s?k=Rheem+condenser+fan+motor+replacement&tag=errorcodefixes-20) |
| High / Low Pressure Switch | $20–$50 | [Amazon](https://www.amazon.com/s?k=Rheem+heat+pump+pressure+switch+R410A&tag=errorcodefixes-20) |

---

## When to Call a Technician

E4 and E5 faults that persist after checking airflow and coil cleanliness require refrigerant pressure testing — which requires EPA 608 certification and a certified gauge set. Any refrigerant leak repair, refrigerant recovery, and recharge must be performed by a licensed HVAC technician. Attempting to charge your own system without certification is illegal and dangerous.

> **Pro tip:** Keep a log of when E4 and E5 faults occur. E4 that only happens on the hottest summer days (>100°F) often indicates a system operating at its design limits with marginal airflow — cleaning the coil and improving clearances usually resolves it without refrigerant work. E5 that happens randomly regardless of temperature almost always means a refrigerant leak.

## Related Articles

- [Rheem RA14 Heat Pump Error Codes](/posts/rheem-ra14-heat-pump-error-codes/)
- [Rheem Furnace Error Code 57](/posts/rheem-furnace-error-code-57/)
- [Rheem Furnace Error Codes — Complete Guide](/posts/rheem-furnace-error-codes/)
