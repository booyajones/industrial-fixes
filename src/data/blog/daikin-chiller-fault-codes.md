---
title: "Daikin Chiller Fault Codes — Complete Troubleshooting Guide"
description: "Daikin chiller fault codes for EWAD, EWAQ, and McQuay series. What each alarm means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - chiller
  - daikin
---

## Daikin Chiller Fault Codes — What They Mean

Daikin Applied chillers (sold under the Daikin, McQuay, and AAF-McQuay brands) use the iOM (intelligent Operation Module) or Rebel controller interface for alarm display. Fault codes appear as numbered alarms with short text descriptions. Older McQuay units use the MicroTech II/III controller, which has its own alarm numbering.

**Model families covered:**
- **EWAD** — air-cooled scroll and screw chillers
- **EWAQ** — water-cooled screw and centrifugal
- **McQuay WMC/WSC** — water-cooled scroll (MicroTech III)
- **McQuay AGS/AGZ** — air-cooled scroll (MicroTech II/III)
- **Rebel DCZS** — light commercial rooftop with chiller mode

---

## Accessing Alarm History

**iOM controller:**
1. Press **MENU** → **Alarm Log**
2. Last 50 alarms display with date, time, and description
3. Active alarms show in the main display with flashing indicator

**MicroTech II/III (McQuay):**
1. From the main screen, press **ALARM** key
2. Scroll through active alarms
3. For history: **MENU** → **Alarm History**

**Resetting alarms:**
- Most alarms auto-reset once the condition clears
- Lockout alarms require manual reset: acknowledge alarm, press **RESET**, verify condition is resolved
- Some alarms require technician password (Level 2 access)

---

## High Pressure Faults

### Alarm HP-1 — High Pressure Cutout (Safety)

What it means: The high pressure safety switch (manual reset) tripped. This is a non-auto-reset safety device — it requires manual intervention.

Setpoint: Typically 400 psig for R-410A, 275 psig for R-22, 430 psig for R-134a (varies by model).

Causes (in order of frequency):
1. Condenser fouling — dirty coils or scaling on water-cooled condenser
2. Non-condensables (air/nitrogen) in refrigerant circuit
3. Refrigerant overcharge
4. Condenser fan failure (EWAD air-cooled)
5. Condenser water flow insufficient (EWAQ water-cooled)
6. Liquid line service valve partially closed
7. Hot gas bypass valve stuck open

Diagnosis:
- Check condenser approach temperature: (condensing temp) minus (entering condenser water/air temp) should be within spec
- On air-cooled units, verify all condenser fans are spinning and correct direction
- On water-cooled, verify condenser water flow and leaving condenser water temp

Fix:
- Clean condenser coils (EWAD) — use foaming coil cleaner, low-pressure rinse
- Flush condenser tubes (EWAQ) — acid clean if scaling present
- Verify refrigerant charge — weigh in per charging chart
- Replace failed condenser fan motor

**Reset:** Physical reset button on HP switch, typically located at the compressor or in the electrical panel.

---

### Alarm HP-2 — High Pressure Alarm (Warning)

Same as HP-1 but from the pressure transducer — this is the software limit before the hardwired safety trips. Allows controlled shutdown before the safety cuts in.

Action: Same diagnostic steps as HP-1. Address immediately to prevent HP safety trip.

---

## Low Pressure / Low Refrigerant Faults

### Alarm LP-1 — Low Pressure Cutout

What it means: Suction pressure dropped below the low pressure safety threshold.

Setpoint: Typically 60 psig for R-410A, 24 psig for R-22 at full load (varies by refrigerant and application).

Causes:
1. Low refrigerant charge (leak)
2. Evaporator coil/tubes fouled — restricted heat transfer
3. Evaporator water flow low or pump failure
4. Evaporator freeze-up — entering chilled water too cold, or flow too low
5. Filter drier restriction
6. Expansion valve stuck closed or underfeeding
7. Liquid line solenoid valve not opening

Diagnosis:
- Check superheat at compressor: should be 10–20°F. High superheat with low suction = undercharge or expansion valve restriction.
- Check chilled water flow — compare to design GPM
- Check entering chilled water temperature — if too cold, chiller is short-cycling

Fix:
- Leak check, repair, recharge refrigerant
- Clean evaporator tubes
- Replace filter drier if pressure drop across it exceeds 2 psig
- Adjust/replace expansion valve

---

### Alarm LP-3 — Low Pressure Alarm During Startup

What it means: Pressure too low to start compressor. Often indicates low ambient conditions or low charge.

Action: Check refrigerant charge. On cold-weather starts, verify crankcase heater has been on for minimum 8 hours before attempting start.

---

## Compressor Fault Codes

### Alarm M-1 — Compressor Motor Overload

What it means: Motor protection relay tripped on one of the compressors.

Causes:
1. High discharge pressure causing high compressor current
2. Low voltage to motor — check voltage at compressor terminals under load
3. Motor winding failure
4. Refrigerant flooding — liquid slugging the compressor
5. Mechanical failure in compressor

Diagnosis:
- Measure amp draw on all three phases at the compressor terminals
- Compare to full-load amperage (FLA) on nameplate
- Check voltage phase balance — >2% imbalance causes rapid motor heating

---

### Alarm M-6 — Compressor Discharge Temperature

What it means: Discharge temperature exceeded the safety limit (typically 250°F / 121°C for scroll compressors).

Causes:
1. Low refrigerant charge — inadequate suction cooling of motor windings
2. High compression ratio (high discharge + low suction pressure simultaneously)
3. Compressor valve failure — hot gas recirculating inside compressor
4. Discharge temperature sensor failure

Diagnosis: Measure superheat. High superheat + low suction pressure = low charge or restriction. Normal suction + high discharge = valve failure or non-condensables.

---

### Alarm M-9 — Compressor Short Cycle

What it means: Compressor cycled on/off too many times in the monitoring period (typically >6 starts per hour).

Causes:
1. Control setpoint too tight — chilled water setpoint diff too small
2. Building load much less than chiller minimum capacity
3. Low pressure safety cycling due to low charge
4. Condenser pressure control issue causing high-pressure cycles

Fix: Widen control differential. Add buffer tank to chilled water loop.

---

## Oil and Lubrication Faults

### Alarm OIL-1 — Oil Pressure Differential Low (Screw Compressors)

What it means: The differential pressure across the oil separator/pump is below minimum. Compressor bearings are at risk.

Causes:
1. Oil level low — check sight glass
2. Oil pump failure
3. Oil filter clogged — check differential pressure across filter element
4. Oil separator plugged
5. Wrong oil viscosity for operating conditions

Fix: Check oil level first. Replace oil filter if pressure drop exceeds 20 psig. Send oil sample for analysis if repeated occurrence.

---

### Alarm OIL-3 — Oil Temperature High

What it means: Oil in the compressor sump exceeded maximum temperature.

Causes:
1. Oil cooler fouled or flow insufficient
2. High ambient temperature in mechanical room
3. Operating outside design conditions
4. Oil cooler valve stuck closed

---

## Evaporator Freeze Protection

### Alarm EFP-1 — Evaporator Freeze

What it means: Evaporator refrigerant temperature dropped to near-freeze conditions. Shutdown is imminent if not corrected.

Causes:
1. Chilled water flow lost or reduced — pump failure, valve closed
2. Entering chilled water temp too low — setpoint mismatch
3. Refrigerant overcharge — flooding evaporator
4. Expansion valve stuck open

This alarm requires immediate response — a fully frozen evaporator means burst tubes and expensive repairs.

Fix: Restore chilled water flow first. Verify pump and all isolation valves.

---

## Communication and Controller Faults

### Alarm COMM-1 — BACnet/Modbus Communication Loss

What it means: The chiller's building automation interface lost communication with the BAS.

Causes:
1. Network cable disconnected or damaged
2. BAS system fault or reconfiguration
3. Chiller controller reset cleared communication settings
4. Address conflict on the network

Fix: Verify cable. Check BAS-side connection. Re-enter communication parameters in iOM/MicroTech if needed.

---

### Alarm CTRL-5 — Controller Fault / Memory Error

What it means: Controller detected an internal error — memory checksum failure, board fault.

Action: Power cycle the controller (full power-off). If alarm persists after power cycle, controller board replacement is required.

---

## MicroTech II/III Specific (McQuay)

**McQuay AGZ air-cooled scroll:**
- **Alarm 40** — Compressor high pressure: same as HP-1
- **Alarm 41** — Compressor low pressure: same as LP-1
- **Alarm 43** — Compressor overload: same as M-1
- **Alarm 53** — Evaporator leaving water temp low
- **Alarm 90** — Compressor fault — check individual compressor module

**McQuay WMC water-cooled:**
- **Alarm 100** — Low condenser water flow
- **Alarm 101** — High condenser leaving water temp
- **Alarm 120** — Loss of charge / low superheat

---

## Parts Reference

| Component | Application | Notes |
|---|---|---|
| High Pressure Safety Switch | HP cutout | Manual reset type, match refrigerant rating |
| Low Pressure Switch | LP cutout | Auto-reset type |
| Discharge Temperature Sensor | Compressor protection | Thermistor, match resistance curve |
| Oil Filter Element | Screw compressor lube | Replace annually or at pressure drop |
| Expansion Valve | Refrigerant metering | Electronic EEV or TXV per model |
| Condenser Fan Motor | EWAD air-cooled | Match CFM and RPM to original |
| MicroTech III Controller Board | Control | Match to software version |

Contact Daikin Applied technical support: 1-800-432-1342. McQuay parts: Daikin Applied parts division.

---

## Amazon Affiliate Links

- [Refrigerant Manifold Gauges R-410A](https://www.amazon.com/s?k=refrigerant+manifold+gauges+r410a&tag=errorcodefixes-20)
- [High Pressure Safety Switch SPST](https://www.amazon.com/dp/B013IHQ8CU?tag=errorcodefixes-20)
- [Thermistor Temperature Sensor NTC](https://www.amazon.com/s?k=NTC+thermistor+sensor+chiller&tag=errorcodefixes-20)
- [Clamp Meter True RMS 600A](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20)
