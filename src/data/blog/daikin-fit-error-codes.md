---
title: "Daikin Fit Error Codes — Inverter Heat Pump Diagnostic Guide"
description: "Daikin Fit error codes: complete fault code reference for the SQ/RZB series compact inverter heat pump, causes, step-by-step fixes, and OEM parts guide."
pubDatetime: 2026-04-24T08:00:00Z
modDatetime: 2026-04-24T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - daikin
  - heat-pump
  - mini-split
  - error-codes
  - diagnostics
---

## Daikin Fit Error Codes — What They Mean

The Daikin Fit (model series RZB, RZBQ, and the indoor SQ series — such as the SQ09TAVJU, SQ12TAVJU, SQ15TAVJU, SQ18TAVJU, SQ24TAVJU) is Daikin's compact inverter heat pump designed for tight installation spaces. Unlike traditional central systems, the Daikin Fit uses variable-speed inverter technology, meaning the compressor modulates capacity instead of cycling on and off.

Fault codes appear on the **wired remote controller** (BRC7EB518W) or **thermostat display**. They are two-character alphanumeric codes — for example, **E3**, **U4**, or **L5**. On the remote controller, the code appears in the status display area along with a blinking maintenance indicator.

When using a conventional (non-communicating) thermostat, fault codes are displayed on the indoor unit's **diagnostic LED** using blink patterns. The outdoor unit also has a diagnostic LED visible through the inspection port on the bottom of the unit.

### Daikin Fit Error Code Reference (RZB / SQ Series)

| Code | Description | System Response |
|------|-------------|----------------|
| **E1** | Indoor PCB fault | Unit shuts down |
| **E3** | High pressure protection | Unit shuts down |
| **E4** | Low pressure protection | Unit shuts down |
| **E5** | Compressor motor overcurrent | Unit shuts down |
| **E6** | Compressor motor lock — locked rotor | Unit shuts down |
| **E7** | Indoor/outdoor communication error | Unit shuts down |
| **E9** | Electronic expansion valve (EEV) fault | Unit shuts down |
| **H9** | Outdoor air temperature sensor fault | Reduced function |
| **J3** | Discharge pipe temperature sensor fault | Unit shuts down |
| **J6** | Outdoor heat exchanger sensor fault | Reduced function |
| **L3** | Electrical box overheat | Unit shuts down |
| **L4** | Radiation fin overheat | Unit shuts down |
| **L5** | Compressor overload / inverter protection | Unit shuts down |
| **L8** | Overcurrent protection | Unit shuts down |
| **U0** | Refrigerant shortage (low pressure detection) | Performance loss |
| **U2** | Low voltage / power supply fault | Unit shuts down |
| **U4** | Outdoor/indoor communication transmission error | Unit shuts down |

### Most Common Daikin Fit Fault Codes

**E3 — High Pressure Protection:**
The system shut down because refrigerant pressure exceeded the high-pressure cutout (~600 PSIG on R-410A systems). The most common cause on the Daikin Fit is a dirty outdoor coil — because the Fit uses a compact, vertically-oriented coil that can restrict airflow more quickly than a traditional horizontal-slab condenser. Also check for vegetation or fence panels blocking air intake/exhaust, and confirm the unit has the minimum required clearances (typically 12 inches on sides, 24 inches in front for air discharge).

**E4 — Low Pressure Protection:**
Refrigerant is below the low-pressure cutout setting. On the Daikin Fit, this occurs most commonly during heating season when: (1) the outdoor coil has heavy ice accumulation from a failed defrost cycle, or (2) there is a refrigerant leak. The Daikin Fit uses a variable-speed compressor — unlike a single-speed system, it will reduce speed and try to maintain operation before triggering E4, so when E4 appears, the pressure drop is significant.

**E7 — Communication Error:**
The indoor and outdoor units cannot communicate. This is the #1 installation error on Daikin Fit systems. The Fit uses a proprietary 3-wire communication cable (S1, S2, S3 terminals — often labeled U, V, W or A, B, C depending on the install guide revision) between the indoor and outdoor units. Incorrect wiring sequence, damaged cable, or a grounded wire triggers E7. This code also fires if the indoor or outdoor control board is faulty.

**U4 — Transmission Error:**
Similar to E7 but indicates a physical signal problem on the data bus rather than a loss of communication. Common causes: cable run too long (Daikin Fit max communication cable length is typically 100 feet), cable routed parallel to high-voltage power wire (causes interference), or a failed communication IC on either board.

**L5 — Inverter Protection:**
The inverter module in the outdoor unit is overheating or has detected an internal fault. The L5 usually comes with L3 or L4. Check that the inverter heatsink fins are not clogged with debris, and that the unit has adequate clearance. The inverter module is inside the outdoor unit's electrical compartment.

**U0 — Refrigerant Shortage:**
The system has detected low refrigerant based on discharge superheat readings. Unlike E4 which is a hard pressure switch trip, U0 is a logic-based fault from the inverter's operating parameters. This is typically the first indication of a slow refrigerant leak before the system reaches E4 pressure levels.

## Common Causes

- **E3/E4 (pressure faults):** Dirty coil, blocked clearances, refrigerant overcharge (E3) or undercharge/leak (E4), failed expansion valve (E9).
- **E7/U4 (communication):** Incorrect 3-wire communication wiring (most common on new installs), cable run too long, parallel high-voltage routing causing interference, water damage to outdoor board.
- **E5/E6/L5 (compressor/inverter):** High head pressure stressing the compressor, refrigerant liquid flooding back to compressor (slugging), or genuine compressor/inverter module failure.
- **H9/J3/J6 (sensors):** Sensor wire corrosion, connector worked loose from vibration, or failed NTC thermistor. Sensor faults are more common on coastal installations (salt air accelerates corrosion).

## Step-by-Step Fix {#step-by-step-fix}

**Before starting:** Turn the thermostat or remote controller to OFF. Turn off the indoor unit disconnect (if present) and the outdoor disconnect. Wait 5 minutes for capacitors to discharge.

1. **Record the error code.** On the wired remote (BRC7EB518W), press the **INSPECTION** button — it's a small recessed button on the front panel. The code cycles through stored faults. Write down the code(s) before cutting power.

2. **E3 (high pressure) — clean the outdoor coil.** The Daikin Fit's compact coil can restrict airflow with relatively minor dirt buildup. Remove the top grille (2 screws) and inspect the coil from above. Use a garden hose at low pressure to rinse from inside out. Check that the minimum clearances around the unit are maintained — the Fit requires more careful placement than a traditional condenser.

3. **E7 / U4 (communication) — verify wiring.** Locate the communication cable terminals on both the indoor and outdoor units. Confirm wiring sequence matches the installation manual exactly (S1→S1, S2→S2, S3→S3 — or the equivalent labeling for your revision). Use a multimeter in continuity mode to verify the cable is unbroken end-to-end. Confirm the communication cable is NOT bundled or run parallel to the high-voltage line set.

4. **E4 (low pressure) — check for iced outdoor coil.** In heating mode, inspect the outdoor unit. Light frost is normal. Ice coating more than 50% of the coil surface, or ice around the base pan, indicates a failed defrost cycle. The Fit should defrost every 30–90 minutes in heating operation below 40°F. If the unit is not defrosting, the defrost board or defrost sensor is likely failed.

5. **U0 (refrigerant shortage) — inspect for leak.** Check all accessible refrigerant connections: the service port Schrader valves, the flare fittings at the outdoor unit service valves, and the indoor coil connections (usually behind the front panel of the air handler). Refrigerant should be confirmed and charged by a licensed technician.

6. **H9/J3/J6 (sensor faults) — check connectors.** Open the outdoor unit's electrical compartment. Locate the sensor harness connectors on the PCB. Firmly reseat each connector — corrosion or vibration-induced looseness is common. If the fault clears and returns, test the sensor with a multimeter (NTC thermistors read approximately 10 kΩ at room temperature).

7. **E9 (EEV fault) — check EEV wiring.** The electronic expansion valve on the Daikin Fit has a 5-wire stepper motor. Inspect the EEV connector at the PCB. If the connector is seated but the code persists, the EEV itself may be seized or failed — this is a technician repair.

8. **After repair — reset and verify.** Restore power and set the unit to cooling mode (or heating mode, seasonally). Run for 15–20 minutes and monitor for fault recurrence. On the wired remote, hold INSPECTION to confirm no new faults are stored.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| Outdoor PCB / control board (Daikin OEM — match model) | $180–$450 | [Amazon](https://www.amazon.com/s?k=Outdoor+PCB+%2F+control+board+%28Daikin+OEM+%E2%80%94+match+model%29&tag=errorcodefixes-20) |
| Indoor PCB / main board (Daikin SQ series — match model) | $150–$380 | [Amazon](https://www.amazon.com/s?k=Indoor+PCB+%2F+main+board+%28Daikin+SQ+series+%E2%80%94+match+model%29&tag=errorcodefixes-20) |
| Inverter module (IPM module for RZB series) | $200–$600 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-fit-error-codes&k=Daikin+inverter+IPM+module+heat+pump&tag=errorcodefixes-20) |
| NTC temperature sensor / thermistor (Daikin OEM) | $12–$35 | [View on Amazon](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-daikin-fit-error-codes&tag=errorcodefixes-20) |
| Electronic expansion valve (EEV) kit — Sporlan or Daikin OEM | $80–$220 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-fit-error-codes&k=Daikin+electronic+expansion+valve+EEV+kit&tag=errorcodefixes-20) |
| Communication cable — 18 AWG 3-conductor shielded (per foot) | $0.50–$1.50/ft | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-fit-error-codes&k=18+AWG+3+conductor+shielded+communication+cable+HVAC&tag=errorcodefixes-20) |
| Wired remote controller BRC7EB518W | $85–$160 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-fit-error-codes&k=Daikin+BRC7EB518W+wired+remote+controller&tag=errorcodefixes-20) |

## When to Call a Professional

**DIY-accessible:** Communication wire re-termination, sensor connector reseating, outdoor coil cleaning, clearance restoration.

**Require a licensed HVAC technician:**
- E4 / U0 — refrigerant leak diagnosis and recharge. The Daikin Fit uses a pre-charged line set on some configurations; modifications require EPA certification.
- E9 (EEV fault) — the electronic expansion valve is deep inside the refrigerant circuit and requires careful decommissioning.
- E5 / E6 / L5 — compressor or inverter module replacement. Daikin inverter modules are model-specific and require calibration after installation.
- Any fault that returns within 24 hours after your repair — the root cause was not resolved and professional diagnosis is needed.

> **Daikin Fit installer note:** The E7 communication fault accounts for roughly 40% of all Daikin Fit service calls in the first year. It is almost always a wiring error made during installation. Before calling for service on a new Fit system, triple-check the communication wiring color sequence and verify there is no ground fault on any of the 3 communication wires (each should read >1 MΩ to ground).
