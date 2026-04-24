---
title: "Copeland Scroll Compressor Fault Codes — Diagnostic LED Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T21:00:00Z
modDatetime: 2026-04-24T21:00:00Z
slug: copeland-scroll-compressor-fault-codes
featured: false
draft: false
tags:
  - copeland
  - scroll-compressor
  - hvac
  - refrigeration
  - fault-codes
description: "Copeland Scroll compressor fault codes from the Demand Cooling module, CoreSense Protection, and Copeland Digital modules — here's how to read LED blink codes and diagnose what's killing your scroll."
---

## Fault Codes: Copeland Scroll Compressors

**What it means:** Emerson's Copeland Scroll compressors are the dominant scroll compressor design used in HVAC and refrigeration across residential, commercial, and industrial applications. Modern Copeland Scroll compressors equipped with CoreSense Protection (factory-installed diagnostics module) or the external Demand Cooling module communicate fault conditions through LED blink codes and, in connected systems, through BMS/controller interfaces.

This guide covers fault codes for:
- **Copeland Scroll with CoreSense Protection** (ZP, ZF, ZR, ZB series with built-in module)
- **Copeland Scroll with Demand Cooling Module**
- **Copeland Digital Scroll** (variable capacity via modulation)

Compressor replacement on large tonnage units runs $1,500–$8,000 or more — accurate fault diagnosis before replacing a compressor is critical.

## Reading Copeland CoreSense Protection LED Codes

The CoreSense module has two LEDs: a green STATUS LED and an amber/red ALARM LED.

**Green STATUS LED:**
- Solid green = Normal operation
- Blinking green = Compressor running normally, no faults
- Off = No power to module

**Amber/Red ALARM LED codes:**
Count the number of rapid blinks in a repeating sequence, followed by a pause.

### 1 Flash — High Discharge Temperature
The discharge temperature thermistor sensed temperatures above the shutdown setpoint (typically 225°F / 107°C on most ZP/ZR series). The compressor shuts down and will auto-restart after a 15-minute anti-recycle delay.

**Common causes:**
- Low refrigerant charge (most common) — reduces mass flow, reducing cooling of the compressor
- Liquid-line filter-drier restriction
- Dirty condenser — high condensing pressure drives up discharge temperature
- Ambient temperature above design limit
- Suction superheat too high due to metering device issue

### 2 Flashes — High Pressure Protection
Discharge pressure exceeded the high-pressure cutout setpoint. The compressor tripped on high discharge pressure, not temperature.

**Common causes:**
- Dirty condenser coil (air-cooled) or fouled condenser water circuit (water-cooled)
- Failed condenser fan motor or reversed fan rotation
- Refrigerant overcharge
- Non-condensables (air) in the refrigerant circuit
- Liquid line restriction causing refrigerant pileup in condenser

### 3 Flashes — Low Pressure / Low Suction
The suction pressure dropped below the low-pressure cutout. The compressor shut down to prevent operation at low mass flow rates that would cause overheating and lubrication failure.

**Common causes:**
- Low refrigerant charge
- Metering device (TXV or EEV) stuck closed or undersized
- Evaporator coil iced over
- Suction filter-drier restriction
- Loss of airflow over evaporator coil

### 4 Flashes — Motor Winding Temperature (Thermistor)
The PTC thermistor embedded in the motor windings detected temperature above threshold. The motor is overheating due to:
- High current draw from mechanical loading
- Lost phase on 3-phase models
- Low voltage causing high current
- Liquid floodback washing oil off windings
- Compressor cycling too rapidly (short cycling)

### 5 Flashes — Low Voltage / Phase Fault
The module detected a voltage condition outside safe operating range:
- Single-phasing on three-phase models
- Voltage below minimum (typically 10% below nominal)
- Voltage imbalance exceeding 2% on three-phase supply

### 6 Flashes — Pressure Sensor Fault
The pressure transducer(s) connected to the CoreSense module are reading outside expected range or are open/short circuit.

### 7 Flashes — Low Superheat / Floodback Detection
The module detected operating conditions consistent with liquid refrigerant returning to the compressor. On Demand Cooling-equipped models, this may trigger demand cooling injection rather than a shutdown. Persistent 7-flash codes indicate a metering device problem.

## Copeland Demand Cooling Module Faults

The Demand Cooling module injects liquid refrigerant at the motor end of the compressor for cooling during high-load or high-ambient conditions. Its indicator LED:

- **Solid red** — Demand cooling active (normal, not a fault)
- **Rapid blinking red** — Demand cooling fault; liquid injection solenoid may be stuck open or wiring fault

## Copeland Digital Scroll Fault Codes

The Digital Scroll uses a modulation valve to vary capacity from 10–100%. Fault LED blink codes:

- **1 blink** — Modulation valve failure (valve stuck or solenoid fault)
- **2 blinks** — Capacity sensor fault
- **3 blinks** — Communication fault with controller
- **4 blinks** — High discharge temperature (same as CoreSense 1-flash)

## Step-by-Step Fix {#step-by-step-fix}

1. **Read the ALARM LED blink count.** Count the flashes on the amber/red LED before touching anything. The module stores the last fault code even after the compressor restarts — check it before cycling power.

2. **For 1-flash (high discharge temp) — check refrigerant charge first.** Connect a manifold gauge set. Check subcooling at the liquid line service valve and superheat at the suction service valve. Low subcooling and high superheat = low charge. Correct charge per system data plate before operating the compressor further.

3. **For 2-flash (high pressure) — inspect the condenser.** On air-cooled systems, feel the condenser coil — if it's too hot to touch (above 140°F) with the condenser fans running, the coil is fouled. Clean with coil cleaner and rinse. On water-cooled systems, check condenser water flow and outlet temperature. Also verify condenser fan motors are running and rotating in the correct direction (fan curve applies only in one direction).

4. **For 3-flash (low pressure) — check for ice on the evaporator.** Turn the system to fan-only to defrost for 30 minutes. If suction pressure rises after defrost and the system runs normally, the evaporator was iced over — investigate the cause (low airflow, low refrigerant, defrost control failure).

5. **For 4-flash (motor winding temp) — check power supply and cycling.** Measure supply voltage at the compressor contactor with the unit running. Verify all three phases are present and balanced on three-phase units (< 2% imbalance). Check the thermostat setpoint and anti-short-cycle timers — if the compressor is cycling more than 6 times per hour, the thermal mass in the windings never recovers.

6. **For 5-flash (voltage/phase fault) — check at the disconnect.** Measure all three phases at the compressor's disconnect and at the contactor. A missing or low phase usually indicates a bad contactor, blown fuse, or utility supply issue. Never continue operating a three-phase compressor with a missing phase — the motor will overheat within minutes.

7. **Perform a compressor megohm test if faults persist.** Disconnect all three compressor power leads. Using a 500V megohm meter, test each compressor terminal (T1, T2, T3) to the compressor body (ground). Readings should be >1 MΩ (healthy compressors typically read 100 MΩ or more). A reading below 1 MΩ indicates winding insulation breakdown — the compressor needs replacement.

8. **Check for liquid slugging (oil foaming at startup).** If the compressor is hot-starting frequently or sitting in a cold environment, liquid refrigerant can migrate into the crankcase. On restart, liquid slugging sounds like a mechanical knock. Install a crankcase heater if not present, and ensure anti-short-cycle protection is 5 minutes minimum.

## Parts Often Needed {#parts-often-needed}

| Part | Part Number | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| CoreSense Protection Module (replacement) | 087S2002 | $80–$150 | [Amazon](https://www.amazon.com/s?k=Copeland+CoreSense+Protection+087S2002&tag=errorcodefixes-20) \| Refrigeration supply |
| Demand Cooling Module | 527-0104-00 | $120–$200 | [Amazon](https://www.amazon.com/s?k=Copeland+Demand+Cooling+Module&tag=errorcodefixes-20) \| Emerson distributor |
| High-pressure switch (manual reset) | (matches system) | $25–$60 | [Amazon](https://www.amazon.com/s?k=refrigeration+high+pressure+switch+manual+reset&tag=errorcodefixes-20) \| HVAC supply |
| Low-pressure switch | (matches system) | $20–$45 | [Amazon](https://www.amazon.com/s?k=refrigeration+low+pressure+switch+auto+reset&tag=errorcodefixes-20) \| HVAC supply |
| TXV valve (size-matched to system) | Sporlan/Danfoss | $80–$250 | [Amazon](https://www.amazon.com/s?k=thermostatic+expansion+valve+TXV+refrigeration&tag=errorcodefixes-20) \| Refrigeration supply |
| Filter drier (liquid line) | Emerson EK series | $20–$80 | [Amazon](https://www.amazon.com/s?k=Emerson+liquid+line+filter+drier&tag=errorcodefixes-20) \| HVAC supply |
| Compressor contactor (3-pole) | (matched to HP) | $30–$80 | [Amazon](https://www.amazon.com/s?k=3+pole+compressor+contactor+HVAC&tag=errorcodefixes-20) \| HVAC supply |
| Crankcase heater | (matched to compressor) | $25–$60 | [Amazon](https://www.amazon.com/s?k=Copeland+scroll+crankcase+heater&tag=errorcodefixes-20) \| Refrigeration supply |

## When to Call a Professional

Refrigerant work on any Copeland Scroll application requires an EPA 608-certified technician — purchasing refrigerant and handling the refrigerant circuit is restricted to licensed professionals. Beyond the certification requirement, Copeland Scroll compressor diagnosis at the refrigerant circuit level (checking superheat, subcooling, pressures under load) requires a manifold gauge set, thermometers, and experience interpreting psychrometric data. Misdiagnosing a compressor fault can result in replacing a $2,000–$8,000 compressor when the actual problem was a $30 filter-drier or a metering device. Always run through the mechanical diagnostics before condemning the compressor itself.

> **Pro tip:** Copeland Scroll compressors have a unique failure mode called "reverse rotation" — on three-phase models, if any two power leads are swapped, the scroll runs backward. A scroll running in reverse sounds like a gravel-filled drum and will fault immediately on high discharge temperature or noise. If a three-phase scroll makes unusual noise on startup after any electrical work, check phase rotation with a phase rotation meter (or swap two leads and see if the noise stops) before any further diagnosis.
