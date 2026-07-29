---
title: "Carrier Infinity 24VNA6 Heat Pump Error Codes - Greenspeed Fault Reference"
description: "Full fault code reference for the Carrier Infinity 24VNA6 Greenspeed variable-speed heat pump, covering Infinity system fault codes 168, 178, 179, inverter faults, control board errors, and refrigerant diagnostics for homeowners and HVAC technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Carrier Infinity 24VNA6 is the flagship residential heat pump in Carrier's lineup, the Greenspeed Intelligence platform. It uses a variable-speed inverter-driven compressor capable of modulating from roughly 25% to 100% capacity, the Infinity communicating system bus, and full integration with the Infinity Touch thermostat. When something fails on the 24VNA6, the Infinity system reports detailed numeric fault codes directly on the thermostat display. This guide covers every code the system generates, what each means at the component level, and how to diagnose and fix it.

## What Does a Carrier 24VNA6 Error Code Mean?

The 24VNA6 communicates entirely through the Infinity system bus, a 4-wire communicating network connecting the outdoor unit, air handler, and thermostat. Fault codes appear on the Infinity Touch thermostat under the System menu → Current Status → Alerts. The outdoor unit's control board also has a status LED that blinks a simplified fault code for technicians working without thermostat access.

Carrier categorizes faults as **alerts** (informational, system still running) and **faults** (system locked out). The thermostat shows both types.

### Infinity System Fault Code Reference

| Code | Fault Description |
|------|-----------------|
| 14 | Low ambient temperature lockout, outdoor temp below equipment operating limit |
| 24 | High pressure switch trip |
| 25 | Low pressure switch trip |
| 26 | Discharge temperature exceeded cutout |
| 27 | Loss of charge (low pressure alert before full lockout) |
| 33 | Outdoor fan motor fault |
| 34 | Outdoor unit communication fault (no signal on Infinity bus) |
| 41 | Outdoor ambient temperature sensor failure |
| 42 | Outdoor coil temperature sensor failure |
| 43 | Discharge temperature sensor failure |
| 44 | Suction temperature sensor failure |
| 45 | Liquid line temperature sensor failure |
| 53 | Inverter module communication fault, no signal from inverter to main board |
| 54 | Inverter module fault, internal error (overcurrent, overtemp, undervoltage) |
| 55 | Compressor protection, inverter detected locked rotor or phase imbalance |
| 57 | Compressor contactor fault |
| 63 | Reversing valve fault |
| 65 | Defrost cycle fault |
| 168 | Air handler communication fault, outdoor unit lost contact with indoor unit |
| 178 | EEV (electronic expansion valve) drive fault |
| 179 | EEV position fault, valve not responding to drive commands |
| 185 | Supply voltage fault, L1-L2 outside acceptable range |
| 200 | Control board internal fault |

### Key Codes Explained: 168, 178, 179

These three codes come up most often on the 24VNA6 because they relate to the communicating system and EEV, which are unique to variable-speed Infinity units.

**Code 168 (Air handler communication fault):** The outdoor unit's control board has lost communication with the air handler's communicating control board. This shuts down the entire system because the outdoor unit cannot receive indoor coil temperature data needed to run the inverter safely. Root causes: disconnected or damaged communication wire, failed air handler control board, or power loss to the air handler.

**Code 178 (EEV drive fault):** The electronic expansion valve's stepper motor driver circuit on the outdoor control board has failed or is not getting a response from the EEV motor. The EEV is the heart of the 24VNA6's efficiency, it continuously adjusts refrigerant flow to match the inverter's variable output. Without EEV control, the system cannot run safely.

**Code 179 (EEV position fault):** Distinguishable from 178, this means the driver circuit is functioning but the valve itself isn't responding as commanded. The EEV may be mechanically stuck, or the stepper motor connector may have a broken pin. This code also appears when the EEV loses its reference position after a power outage, requiring a valve home cycle (usually clears automatically on next startup).

**Inverter faults (codes 53–55):** The Greenspeed inverter module (Carrier uses a module manufactured by Hitachi or equivalent) converts 240V single-phase power to variable-frequency output for the scroll compressor. Code 53 means the main control board can't see the inverter module at all, check the communication harness between boards. Code 54 is an internal inverter fault; a Carrier service tool can pull sub-codes. Code 55 means the inverter tried to start the compressor but the compressor didn't respond, winding failure or rotor lock.

## How to Fix It

### For High/Low Pressure Faults (Codes 24, 25, 27)

1. On the Infinity Touch, go to System → Service Diagnostics → Fault History. Check how many times each fault occurred and when.
2. Power cycle the system (thermostat to OFF, breaker off, 30 seconds, restore). If fault returns within minutes, it's an active failure.
3. For code 24 (high pressure): inspect outdoor coil for debris, verify outdoor fan is running, check that the return air filter indoors is clean and not restricting indoor airflow.
4. For code 25 (low pressure): check suction line for ice, inspect indoor coil for ice or fouling. If suction pressure is below 100 psig in cooling at normal conditions, the system needs refrigerant, but find the leak first.
5. For code 27 (loss of charge alert): this is a pre-fault warning. The system is still running but marginal. Schedule refrigerant service before a full lockout.

### For Sensor Faults (Codes 41–45)

1. The Infinity Touch display under Service Diagnostics shows live sensor readings, check whether the affected sensor reads an obviously wrong value (–40°F or 250°F typically indicates an open or shorted sensor).
2. Locate the sensor: ambient sensor on coil guard or cabinet bracket; coil sensor clipped to outdoor coil bottom circuit; discharge and suction sensors clamped to refrigerant lines.
3. Unplug the sensor and measure resistance. Carrier outdoor sensors on the 24VNA6 are 10k NTC thermistors, approximately 10,000 ohms at 77°F.
4. Replace faulty sensor. Carrier uses part **HH79NZ074** for coil and ambient sensors on many Infinity outdoor units; confirm with the model-specific parts list.

### For Code 168 (Air Handler Communication Fault)

1. Check the Infinity system bus wiring between the air handler and outdoor unit. The bus uses 4 wires; the two data wires are typically red/blue or color-coded per the installation manual.
2. Verify the air handler has power: check the indoor unit's breaker and confirm the air handler's indoor control board has power (LED status light visible on the board).
3. Measure 24VAC between R and C at the outdoor unit terminal block. If absent, the air handler's transformer may have failed.
4. Reseat all Infinity bus connectors at both ends. Outdoor unit terminal block connections must be snug, Carrier uses a screw-terminal block that can work loose over time.
5. If wiring is confirmed good and fault persists, the air handler's communicating control board may have failed.

### For EEV Faults (Codes 178, 179)

1. Turn power off to the unit and reseat the EEV stepper motor connector at the outdoor control board. Power up and observe whether the fault returns.
2. For code 179: power cycle completely. The EEV performs a home cycle on startup, if the fault clears after a clean restart, a power interruption caused the valve to lose its reference position.
3. If code 178 persists: check for 12VDC at the EEV drive output on the outdoor control board. Absence confirms the drive circuit has failed, the control board needs replacement.
4. If 12VDC is present but code 179 persists: the EEV stepper motor has failed. This requires refrigerant recovery, EEV replacement, evacuation, and recharge.

### For Inverter Faults (Codes 53–55)

1. For code 53: check and reseat the communication harness between the main control board and the inverter module.
2. For code 54: check incoming voltage at the inverter input (contactor output), should be 208–240VAC L1-L2. Clean the inverter heat sink if it shows dust or debris accumulation.
3. For code 55: measure compressor winding resistance across all three terminal pairs. Equal resistance (typically 2–8 ohms) with no phase-to-ground fault indicates the compressor is intact. If windings are open or shorted, the compressor has failed.
4. Do not attempt to replace the inverter module with a non-Carrier part. The Greenspeed inverter is firmware-matched to the control board and will not operate correctly with a substitute.

### For Reversing Valve Fault (Code 63)

1. Confirm at the thermostat which mode the unit is failing in, heating or cooling.
2. At the outdoor unit, locate the reversing valve solenoid (mounted on the valve body). Measure 24VAC across the solenoid terminals during the mode that triggers the fault.
3. If 24V is present: measure solenoid coil resistance. Good solenoid reads 15–40 ohms. Open circuit means solenoid replacement.
4. If solenoid tests good but valve won't shift: valve body is mechanically stuck. Refrigerant recovery and valve replacement required.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Carrier Outdoor Sensor HH79NZ074](https://www.amazon.com/s?ascsubtag=ecf-carrier-24vna6-error-codes&k=Carrier+Outdoor+Sensor+HH79NZ074&tag=errorcodefixes-20) | Ambient and coil sensor replacement for codes 41, 42; 10k NTC thermistor | $20–$45 |
| [Carrier 24VNA6 Outdoor Control Board](https://www.amazon.com/s?k=Carrier+24VNA6+Outdoor+Control+Board&tag=errorcodefixes-20) | Required for EEV driver failure (code 178) or control board fault (code 200) | $250–$550 |
| [Carrier Infinity Touch Thermostat](https://www.amazon.com/s?ascsubtag=ecf-carrier-24vna6-error-codes&k=Carrier+Infinity+Touch+thermostat&tag=errorcodefixes-20) | Required for full Infinity fault code display on the 24VNA6 | $200–$400 |
| [High Pressure Switch Carrier Heat Pump](https://www.amazon.com/dp/B013IHQ8CU?ascsubtag=ecf-carrier-24vna6-error-codes&tag=errorcodefixes-20) | Replace if code 24 persists with normal refrigerant pressures | $25–$60 |
| [Reversing Valve Solenoid Coil 24V](https://www.amazon.com/s?ascsubtag=ecf-carrier-24vna6-error-codes&k=reversing+valve+solenoid+coil+24V+heat+pump&tag=errorcodefixes-20) | Required when code 63 trips with confirmed 24V at solenoid terminals | $20–$45 |
| [Refrigerant Manifold Gauge Set R-410A](https://www.amazon.com/s?ascsubtag=ecf-carrier-24vna6-error-codes&k=R-410A+manifold+gauge+set+HVAC&tag=errorcodefixes-20) | Essential for diagnosing pressure faults 24, 25, 27 accurately | $45–$120 |

## When to Call a Pro

The 24VNA6 Greenspeed is not a system for DIY refrigerant work or inverter diagnosis:

- **Any refrigerant-related code (24, 25, 26, 27) with confirmed abnormal pressures.** The Greenspeed runs R-410A at higher operating pressures than conventional heat pumps. EPA 608 certification required.
- **Codes 53, 54, 55 (inverter and compressor faults).** Inverter replacement requires Carrier factory parts and startup commissioning procedures. Compressor replacement requires full refrigerant recovery.
- **Code 178 or 179 with confirmed EEV failure.** EEV replacement requires a certified technician and full system evacuation.
- **Code 168 with confirmed failed air handler control board.** Infinity communicating boards must be matched to the system; an incorrect replacement will generate additional faults.
- **Warranty claims.** The 24VNA6 Greenspeed carries a 10-year registered parts warranty through Carrier dealers. Non-dealer repairs can void coverage.

Sensor replacements, pressure switch swaps, and communication wiring troubleshooting are within reach for a qualified DIYer or general HVAC service technician.

## Frequently Asked Questions

**Q: The Carrier Infinity thermostat shows code 168 and 42 at the same time. Where do I start?**
A: Start with code 168 (air handler communication). The outdoor coil sensor (code 42) may actually be fine, a communication loss between outdoor and indoor units prevents the thermostat from reading the outdoor sensors correctly, which can generate phantom sensor faults. Restore communication first, then see if code 42 clears on its own.

**Q: My 24VNA6 only runs at full speed and won't modulate down. No fault codes. What's happening?**
A: The Greenspeed needs a fully functioning Infinity communicating system to modulate. Check that the thermostat and air handler are both on the bus and showing "Connected" in the thermostat's system status. If the outdoor unit can't communicate with the indoor unit, it defaults to maximum capacity as a fail-safe. Also check whether the iQ Drive sub-code shows any inverter limitation in service diagnostics.

**Q: How often does the 24VNA6 defrost in winter, and when should I be concerned?**
A: Normal defrost cycles occur every 30–90 minutes during heating operation in cold, humid weather (30–45°F outdoor). Each cycle lasts 5–10 minutes. If the unit is going into defrost more than once per hour or defrost cycles are lasting 15+ minutes, that's abnormal. Common causes: low refrigerant charge (low suction pressure = coil ices faster), failed defrost sensor not reading coil temperature correctly, or outdoor fan running at too low a speed in variable mode.

**Q: Code 185 (voltage fault) appeared after a summer storm. The unit won't run. What do I check first?**
A: Check your main electrical panel for a tripped breaker or a breaker that appears on but has internally tripped (flip it fully off, then back on). If the panel looks fine, check the outdoor disconnect for a blown fuse or tripped disconnect. Then measure L1-L2 voltage at the outdoor unit's contactor with a multimeter. Carrier specifies 208–240VAC; anything below 187V or above 253V will trigger code 185. If voltage is consistently outside range, that's a utility or panel issue for an electrician.
