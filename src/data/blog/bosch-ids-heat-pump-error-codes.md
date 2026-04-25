---
title: "Bosch IDS Heat Pump Error Codes - Original Series Fault Guide"
description: "Complete fault code guide for the Bosch IDS original series heat pump. Covers all error codes, diagnostic steps, and differences from the IDS 2.0 series."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Bosch IDS (Inverter Ducted Split) heat pump was a landmark product in the residential market — a variable-speed, communicating inverter heat pump offered at a mid-market price point before the IDS 2.0 replaced it. If you own an original IDS system, finding accurate fault code documentation can be difficult because Bosch has focused support resources on the newer platform. This guide covers all known fault codes for the original IDS series, explains key differences from the IDS 2.0, and gives you a clear diagnostic path for each fault.

## What Do Bosch IDS Error Codes Mean?

The original Bosch IDS system communicates error conditions through the IDS Touch or IDS Basic thermostat display, the indoor unit's LED, and the outdoor unit's control board. Fault codes appear as alphanumeric codes on the thermostat and as blink sequences on the control board LEDs.

The IDS original uses a communicating system architecture — the thermostat, indoor air handler, and outdoor unit exchange data on a communication bus. This means a single fault at any component can generate secondary faults at the others. Always trace a fault back to its source component before replacing parts.

**IDS Original vs. IDS 2.0 — Key Differences:**
- The original IDS uses a different communication protocol; IDS 2.0 components are NOT backward-compatible.
- The original IDS outdoor unit uses a different inverter board than the IDS 2.0.
- The original IDS fault code numbering scheme differs from IDS 2.0; do not use an IDS 2.0 manual to diagnose an original IDS system.

**Common Bosch IDS Original Fault Codes:**

| Code | Description |
|------|-------------|
| E1 | Indoor coil temperature sensor fault |
| E2 | Outdoor ambient temperature sensor fault |
| E3 | Discharge temperature sensor fault |
| E4 | High pressure protection activated |
| E5 | Low pressure protection activated |
| E6 | Communication fault (thermostat to indoor unit) |
| E7 | Communication fault (indoor to outdoor unit) |
| E8 | Indoor fan motor fault |
| E9 | Outdoor fan motor fault |
| F1 | Compressor overload protection |
| F2 | IPM (inverter module) overheat |
| F3 | DC bus overvoltage |
| F4 | DC bus undervoltage |
| F5 | Compressor overcurrent |
| F6 | Phase loss or reverse phase |
| H1 | Defrost in progress (normal operation indicator) |
| P1 | High discharge temperature lockout |
| P4 | Low ambient lockout (unit shut down due to temperature below operating range) |

## How to Fix It

**1. E1 / E2 / E3 — Temperature Sensor Faults**

Sensor faults are among the most common IDS codes. Before replacing sensors:
- Inspect the sensor wiring harness for pinched, chafed, or corroded wires. These are low-voltage signal wires that are vulnerable at sheet metal edges inside the unit.
- Disconnect the sensor connector and measure resistance. Compare to the resistance-temperature chart in the Bosch IDS service manual (typically 10kΩ at 77°F / 25°C for NTC sensors).
- A resistance reading of open (OL) or short (near 0Ω) confirms sensor failure.
- If the wiring is intact and the sensor reads correctly, the fault may be on the control board's sensor input circuit.

**2. E4 — High Pressure Fault**

High pressure faults indicate the refrigerant circuit is not rejecting heat properly in cooling mode, or absorbing heat properly in heating mode. Diagnose:
- Check outdoor coil cleanliness — a dirty or blocked condenser coil is the most common cause in cooling mode.
- Verify outdoor fan is running and rotating in the correct direction.
- Check refrigerant charge: overcharge causes high pressure on the liquid side. Measure subcooling at the liquid service valve.
- A failed TXV (expansion valve) can also cause high pressure — if subcooling is high and superheat is high simultaneously, suspect TXV restriction.

**3. E5 — Low Pressure Fault**

Low pressure faults typically indicate low refrigerant charge or a restriction in the system:
- Check system superheat at the suction line. High superheat + low suction pressure = low charge.
- Inspect the indoor coil for ice — a frozen coil from low airflow or low refrigerant can trigger E5.
- Check filter and return air — restricted airflow starves the indoor coil and drops suction pressure.
- If suction pressure is normal but the low pressure switch keeps triggering, the switch itself may be faulty.

**4. E6 / E7 — Communication Faults**

These are the most frustrating faults to diagnose. Follow this sequence:
- Power cycle the entire system (thermostat, indoor unit, outdoor unit) by turning off the breaker for 5 minutes.
- Inspect the communication wiring between thermostat and air handler, and between air handler and outdoor unit. Look for broken wires, loose terminals, and wire contacts corroded at the air handler terminal strip.
- On the original IDS, communication between the indoor and outdoor unit uses a 2-wire bus — polarity matters on some models. Verify the wires are on the correct terminals (A and B).
- E6 (thermostat to indoor) is often caused by a failed thermostat or a bad communication board in the air handler.
- E7 (indoor to outdoor) is usually the outdoor control/inverter board or wiring between units.

**5. F1 / F5 — Compressor Faults**

Compressor overload (F1) and overcurrent (F5) share common causes:
- Check supply voltage at the outdoor unit — low voltage causes high amperage draw on the compressor.
- Measure compressor winding resistance (with power off). Readings should be within 10% of each other across all three windings. Any reading near 0Ω indicates a shorted winding.
- Check for refrigerant overcharge — a severely overcharged system forces the compressor to work against excessive head pressure.
- If the compressor is mechanically seized (won't start even with correct voltage and charge), it requires replacement.

**6. F2 — IPM Overheat**

The Intelligent Power Module (inverter module) overheats when:
- The outdoor unit is severely restricted (blocked panels, debris against the outdoor coil).
- Ambient temperature is extremely high and the unit is operating at maximum capacity.
- The IPM's thermal compound has dried out (common on older units).
- The IPM cooling fan is not running.
Clear any obstructions, clean the outdoor coil, and verify the IPM fan circuit. If the IPM itself is damaged, it typically needs replacement as a complete assembly.

**7. F3 / F4 — DC Bus Voltage Faults**

These point to problems with incoming power quality or the inverter drive board:
- Measure supply voltage at the outdoor unit disconnect under load. F3 (overvoltage) above 265V AC, F4 (undervoltage) below 195V AC.
- Loose connections at the outdoor unit's terminal block cause voltage drop under load — check and retighten.
- If supply voltage is normal, the inverter board's DC bus capacitors may be failing. This requires board replacement.

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| NTC Temperature Sensor (10kΩ) | Replace failed E1/E2/E3 sensors | [View on Amazon](https://www.amazon.com/s?k=NTC+10k+temperature+sensor+HVAC&tag=errorcodefixes-20) |
| HVAC Refrigerant Manifold Gauge Set | Diagnose E4/E5 pressure faults | [View on Amazon](https://www.amazon.com/s?k=HVAC+manifold+gauge+set+refrigerant&tag=errorcodefixes-20) |
| Low Voltage Thermostat Wire 18/5 | Replace communication wiring for E6/E7 | [View on Amazon](https://www.amazon.com/s?k=18+5+thermostat+wire+low+voltage&tag=errorcodefixes-20) |
| Coil Fin Comb and Coil Cleaner | Clean outdoor coil for E4 and F2 faults | [View on Amazon](https://www.amazon.com/s?k=HVAC+coil+fin+comb+cleaner&tag=errorcodefixes-20) |
| Clamp Meter with True RMS | Measure compressor amperage for F1/F5 | [View on Amazon](https://www.amazon.com/s?k=true+rms+clamp+meter+HVAC&tag=errorcodefixes-20) |

## When to Call a Pro

Call a certified HVAC technician when:
- **E4 or E5 faults** persist after checking airflow and coil condition — refrigerant work requires EPA 608 certification.
- **F1 or F5 (compressor faults)** are active — compressor diagnosis and replacement is a major repair.
- **F2 faults** after cleaning the outdoor unit — IPM replacement on an inverter drive requires inverter board expertise.
- **F3 / F4 DC bus faults** with normal supply voltage — inverter board failure is a complex repair.
- **E7 communication faults** that don't resolve with wiring inspection — the outdoor control/inverter board may need replacement, and Bosch IDS original parts require a sourcing strategy from HVAC distributors since the unit is older.

## FAQ

**Q: My Bosch IDS shows E7 constantly after a power outage. How do I clear it?**

A: Power surges during outages can corrupt the control boards' communication registers. Turn off the outdoor unit breaker, the indoor unit/air handler breaker, and the thermostat (or its circuit). Wait 5 full minutes, then restore power to the air handler first, then the outdoor unit, then the thermostat. This full power cycle clears most post-outage communication faults.

**Q: How do I tell if I have an original IDS or an IDS 2.0?**

A: Check the model number on the outdoor unit nameplate. Original IDS outdoor units typically start with BOVA (air-to-air) and have model numbers ending in a format like BOVA60HDN1. IDS 2.0 units have different model number structures and will have "IDS 2.0" on the unit's label. You can also check the thermostat — IDS 2.0 ships with the BCC100 touchscreen thermostat.

**Q: Can I use any communicating thermostat with the original Bosch IDS?**

A: The original IDS uses a proprietary communication protocol. You must use the Bosch IDS Touch or IDS Basic thermostat for communicating control. Some installers have used the Bosch BCC100 in conventional (non-communicating) mode, but this disables variable-speed operation and fault reporting. Stick with the correct IDS thermostat.

**Q: The H1 code shows during winter heating. Is my system broken?**

A: No. H1 simply means the outdoor unit is in defrost mode — a completely normal operation in cold weather. The outdoor coil accumulates frost when ambient temperatures are between 17°F and 45°F with high humidity. The unit periodically reverses the refrigerant flow to melt the frost. H1 clears automatically when defrost completes, typically within 10-15 minutes.
