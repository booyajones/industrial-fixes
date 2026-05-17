---
title: "Heil Ion Heat Pump Error Codes - iComfort Communicating Fault Guide"
description: "Complete fault code reference for the Heil Ion variable-speed heat pump, including Ion system communicating faults, control board codes, reversing valve errors, and step-by-step diagnostics. Covers both LED flash and thermostat display codes."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

The Heil Ion is ICP Group's top-tier variable-speed heat pump, built on the same platform as the Lennox XP21 and sharing engineering with the Carrier Infinity line. It's a communicating system — meaning the outdoor unit, air handler, and thermostat all talk to each other over a proprietary two-wire data bus. When something goes wrong, the Ion system logs specific fault codes that can save a technician hours of diagnostic time — if you know how to read them.

This guide covers the Heil Ion heat pump fault code system from top to bottom.

## What Does the Heil Ion Error Code Mean?

The Heil Ion system uses the **Ion System Control** (ISC), a communicating control board that collects fault data from every component in the system. Faults display on the **Ion System Control Thermostat** and can also be read via the control board's diagnostic LED. There are two types of faults:

- **Soft lockout** — the system attempts to restart automatically after a cooldown period
- **Hard lockout** — the system shuts down and requires a manual reset at the thermostat or by cycling power

All faults are logged with a timestamp in the thermostat's fault history — a feature that's invaluable for tracking intermittent problems.

---

## Heil Ion Heat Pump Fault Codes

### Fault 1 — High Pressure Cutout
The high-pressure switch opened, indicating refrigerant pressure on the discharge side exceeded the safety threshold (typically 610 PSI for R-410A systems).

**Causes:**
- Dirty condenser coil with blocked airflow
- Condenser fan motor failure or reduced speed
- Refrigerant overcharge
- Restricted metering device (TXV or EEV failure)
- Ambient temperature extreme

**Fix:** Inspect and clean the outdoor coil. Verify all fan blades are intact and spinning at full speed. If the coil and fan check out, you'll need refrigerant gauges to verify charge and pressure — call a tech.

### Fault 2 — Low Pressure Cutout
The low-pressure switch opened, typically indicating low refrigerant charge or restricted airflow across the indoor coil.

**Causes:**
- Refrigerant leak
- Frozen indoor coil (blocked filter, low airflow)
- Failed expansion valve
- Low ambient temperature operation

**Fix:** Check the air filter first — a clogged filter is the most common cause of indoor coil icing and low-pressure faults. If the filter is clean and the fault persists, a refrigerant leak is likely. This requires professional repair.

### Fault 3 — Defrost Fault
The defrost cycle failed to complete within the expected time window. On the Ion system, defrost is demand-controlled using outdoor coil temperature sensors — it only runs when frost is actually detected.

**Causes:**
- Failed outdoor coil temperature sensor
- Reversing valve not switching to cooling mode for defrost
- Defrost control board failure
- Extremely heavy frost accumulation (secondary to low refrigerant)

**Fix:** Verify the outdoor coil sensor resistance. If the reversing valve is suspect, command a defrost cycle manually (available through the Ion thermostat service menu) and listen for the reversing valve click. No click = solenoid or valve failure.

### Fault 4 — Outdoor Coil Sensor Fault
The outdoor coil temperature sensor (also called the defrost sensor) is reading out of range or has an open/short circuit.

**Fix:** Locate the sensor clipped to the outdoor coil tubing. Unplug and measure resistance at room temperature — it should be near 10kΩ (verify against the service manual for your specific outdoor unit model). Replace if out of spec. This is a DIY-accessible repair.

### Fault 5 — Outdoor Ambient Sensor Fault
The outdoor ambient temperature sensor (separate from the coil sensor) has failed or is reading implausibly.

**Fix:** Same procedure as Fault 4. The ambient sensor is typically mounted on the control board bracket inside the outdoor unit. Replace the sensor — they're inexpensive and plug in.

### Fault 6 — Indoor Coil Sensor Fault
The indoor coil thermistor is failed or reading out of range. This sensor is critical for EEV (electronic expansion valve) control on variable-speed systems.

**Fix:** Access the air handler. The sensor clips to the refrigerant tubing on the indoor coil. Test resistance and compare to spec. This is a straightforward sensor swap.

### Fault 7 — Indoor Blower Fault
The air handler's variable-speed blower motor reported a fault, or failed to reach the commanded airflow target within the expected time.

**Causes:**
- Restricted airflow (dirty filter, closed registers, blocked return)
- ECM motor failure
- Communication loss between air handler and outdoor unit
- Motor module failure (common failure mode on ECM motors)

**Fix:** Check airflow restriction first. If airflow is clear, the ECM motor or its module may need replacement. ECM modules can sometimes be replaced separately from the motor — verify the specific part number for your air handler model.

### Fault 8 — Communication Fault (System Bus Fault)
The Ion system bus lost communication between one or more components. This is one of the most common faults on communicating systems.

**Causes:**
- Loose or damaged communication wire
- Failed control board (outdoor unit or air handler)
- Power loss to one component
- Wiring polarity reversal

**Fix:** Check the two-wire communication bus between the thermostat, air handler, and outdoor unit. Verify terminals are tight and wires are not pinched or damaged. Confirm both units have power. Check for correct polarity — the Ion system is polarity-sensitive.

### Fault 9 — Compressor Lockout / Inverter Fault
The variable-speed compressor's inverter drive reported a fault. This is a hard lockout.

**Causes:**
- Input voltage out of spec (too high or too low)
- Compressor winding short or ground fault
- Inverter board overtemperature
- Rapid cycling (multiple starts within a short window)

**Fix:** Verify supply voltage is within ±10% of nameplate rating. Wait 30 minutes after power cycle before restart attempt. If the fault recurs immediately, the inverter drive or compressor requires professional diagnosis. Do not continue cycling the unit — you'll damage the compressor.

### Fault 10 — Reversing Valve Fault
The reversing valve failed to switch modes as commanded. The system detected the unit operating in the wrong refrigerant flow direction.

**Fix:** Test the solenoid coil resistance (expect 20–40Ω). Listen for the valve click when switching modes at the thermostat. If there's no click and the solenoid tests good, the valve spool may be mechanically stuck — this requires refrigerant recovery and valve replacement.

### Fault 11 — Discharge Temperature Fault
The discharge line temperature sensor detected abnormally high compressor discharge temperature.

**Causes:**
- Low refrigerant charge (superheated discharge gas)
- Failed metering device
- Compressor efficiency loss
- High ambient temperatures combined with a dirty coil

**Fix:** This fault often accompanies low refrigerant charge — check for other low-pressure indicators. If refrigerant charge is correct, the discharge sensor itself may have failed.

---

## How to Fix It

1. **Navigate to the fault log** on the Ion thermostat — go to Settings > Service > Fault History. Note the fault code, timestamp, and how many times it occurred.
2. **Clear the fault** at the thermostat and observe whether it returns immediately or intermittently.
3. **Check airflow first** — filter, blower rotation, and outdoor coil cleanliness.
4. **Test all sensors** with a multimeter before ordering boards.
5. **Check communication wiring** if Fault 8 is present — re-terminate all connections at both boards.
6. **For refrigerant faults** — do not reset more than twice. Repeated restarts under refrigerant stress damage the compressor.
7. **Record supply voltage** at the disconnect when the fault is active — low voltage trips more faults than most technicians expect.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Heat Pump Defrost Thermostat / Coil Sensor](https://www.amazon.com/s?i=industrial&k=heat+pump+defrost+thermostat+sensor&tag=errorcodefixes-20) | Fault 4 fix; controls defrost cycle initiation | $15–$45 |
| [Reversing Valve Solenoid Coil 24V](https://www.amazon.com/s?i=industrial&k=reversing+valve+solenoid+coil+24v+heat+pump&tag=errorcodefixes-20) | Fault 10 fix; activates reversing valve switching | $20–$60 |
| [ECM Blower Motor Module](https://www.amazon.com/s?i=industrial&k=ECM+blower+motor+module+replacement&tag=errorcodefixes-20) | Fault 7 fix; module-only replacement often cheaper than full motor | $80–$250 |
| [18 AWG 2-Conductor Thermostat Wire](https://www.amazon.com/s?i=industrial&k=18+AWG+thermostat+wire+2+conductor&tag=errorcodefixes-20) | Fault 8 fix; replace damaged communication wiring | $15–$40 |
| [HVAC Manifold Gauge Set R-410A](https://www.amazon.com/s?i=industrial&k=R410A+manifold+gauge+set+HVAC&tag=errorcodefixes-20) | Required for refrigerant pressure diagnosis | $45–$150 |

---

## When to Call a Pro

The Heil Ion is not a DIY-repair system. The variable-speed compressor and inverter drive are sophisticated electronic components that require factory-trained diagnosis. Call a licensed HVAC technician when:

- **Fault 9 (compressor lockout) repeats** after proper restart procedures
- **Fault 2 (low pressure) persists** after confirming airflow is clear — you have a refrigerant leak
- **Fault 10 (reversing valve) requires valve replacement** — needs refrigerant recovery
- **The Ion thermostat is blank or unresponsive** — possible control board failure requiring component-level diagnosis
- **Fault 1 (high pressure) repeats** after cleaning the coil — may indicate overcharge or TXV failure

Always pull the fault history from the Ion thermostat before the tech arrives. That timestamp data is gold for diagnosing intermittent failures.

---

## Frequently Asked Questions

**Q: My Heil Ion shows a fault but clears itself after a reset. Should I be concerned?**

A: Yes. Faults that clear on reset but return intermittently usually indicate a developing hardware problem — a sensor drifting out of spec, a loose connection, or a compressor starting to struggle under load. Pull the fault history and note frequency. If the same fault has occurred more than 3 times in 30 days, have a tech look at it before it becomes an emergency breakdown.

**Q: What's the difference between the Heil Ion and the Tempstar Ion heat pump?**

A: They're mechanically identical — both are produced by ICP Group (part of Carrier Global) and share the same control platform, fault codes, service procedures, and parts. The Ion brand and premium features are the same across Heil, Tempstar, and Comfortmaker Ion lines. A Heil Ion service manual applies directly to the Tempstar Ion.

**Q: Can I access the Ion fault codes without the communicating thermostat?**

A: Yes. The outdoor unit control board has a diagnostic LED that flashes fault codes. Refer to the service manual for your specific model to decode the flash sequence. However, the thermostat's fault log gives you timestamps and frequency data that the LED can't — it's worth installing the communicating thermostat if you want proper diagnostics.

**Q: Fault 8 appeared once during a storm and hasn't come back. Do I need to do anything?**

A: A single communication fault during a power event (lightning, voltage spike, brief outage) is usually benign. Clear the fault and monitor. If it returns under normal operating conditions, inspect the communication wiring and terminals. Communication faults that correlate with weather events can sometimes be traced to a damaged surge protector or a failing control board that's sensitive to power quality.
