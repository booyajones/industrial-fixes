---
title: "Bosch IDS 2.0 Heat Pump Error Codes - Full Diagnostic Guide"
description: "Complete guide to Bosch IDS 2.0 inverter-driven heat pump error codes. Covers all E-codes and F-codes, inverter faults, refrigerant issues, and control board diagnosis."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - heat-pump
  - bosch
  - error-codes
---

The Bosch IDS 2.0 (Inverter-Driven Split) is one of the most-installed variable-capacity heat pumps from a non-Big-4 brand, known for its ultra-quiet operation and SEER2 ratings up to 20. When it faults, the indoor unit's status LED and the communicating thermostat both display error codes. This guide covers every major fault, what causes it, and how to fix it.

## What Does the Bosch IDS 2.0 Error Code System Mean?

The IDS 2.0 uses a two-tier fault system:

- **E-codes** (E01–E99): Active faults that stop operation. The system shuts down and displays the code on the thermostat or indoor air handler LED.
- **F-codes** (F01–F99): Fault history — codes stored from previous trips. Access fault history via the BCC100 thermostat under Settings → Service → Fault History.

The system also uses LED blink patterns on the indoor unit if no communicating thermostat is installed.

---

## Most Common IDS 2.0 Error Codes

### E01 — Indoor Communication Fault

**What it means:** The indoor air handler cannot communicate with the outdoor inverter unit. The IDS 2.0 uses a proprietary 3-wire communication bus (24V signal + 2 low-voltage data wires) between indoor and outdoor units.

**Common causes:**
- Loose or corroded communication wire terminals at indoor or outdoor unit
- Wrong wire gauge used for communication (requires 18-gauge minimum, 2-conductor shielded preferred)
- Damaged communication wire from UV exposure or staple penetration
- Control board failure (indoor or outdoor)

**Fix steps:**
1. Check all communication wire connections at both units — push and re-seat each terminal
2. Measure continuity on the communication wires with a multimeter (should read <5Ω per conductor)
3. Check for 24VAC between C and R terminals — if absent, check transformer
4. If wiring is good, replace the indoor control board first (cheaper) before the outdoor inverter board

---

### E02 — Outdoor Communication Fault

Same diagnosis as E01 but specifically the outdoor inverter failing to respond. If E01 and E02 appear together, start at the outdoor unit terminals.

---

### E03 — Discharge Temperature Too High

**What it means:** Refrigerant discharge line temperature exceeded safe limits (typically >260°F). The inverter trips on high-side overheat.

**Common causes:**
- Low refrigerant charge (most common)
- Dirty outdoor coil restricting heat rejection
- Outdoor fan not running
- Refrigerant restriction (filter-drier blockage)

**Fix steps:**
1. Check outdoor coil — clean if dirty (fins bent, debris)
2. Verify outdoor fan spins freely and runs at full speed
3. Check refrigerant charge — requires gauges and licensed tech
4. If charge was correct, check filter-drier for restriction (temperature drop across drier = blockage)

---

### E04 — Low Pressure Fault

Low suction pressure tripped the inverter. On heat pump systems, this code appears in both heating and cooling modes.

**Causes:**
- Low refrigerant (most common)
- Dirty indoor coil in cooling mode (airflow restriction)
- Dirty air filter
- Expansion valve failure

**Fix:**
1. Replace air filter immediately — check monthly
2. Clean indoor coil if dirty
3. If clean and charge is normal, check TXV/EEV operation

---

### E05 — High Pressure Fault

High-side pressure exceeded limit (~550 PSI on R-410A systems).

**Causes:**
- Dirty outdoor coil (most common in hot weather)
- Outdoor fan not running
- Refrigerant overcharge
- Non-condensables (air) in system

**Fix:**
1. Clean outdoor coil with coil cleaner spray
2. Check outdoor fan motor and capacitor
3. If pressure is high at correct charge, recover and recharge

---

### E06 — Inverter Module Fault

The inverter module (IPM — Intelligent Power Module) in the outdoor unit detected an overcurrent, overheat, or short circuit condition.

**Causes:**
- Inverter IPM overheated (blocked ventilation, dirty fins)
- Failed compressor (drawing locked-rotor current)
- Voltage transient damaged IPM
- Capacitor on DC bus failure

**Fix:**
1. Check outdoor unit clearances — 12" minimum on all sides, 24" on service side
2. Clean heatsink fins on inverter board
3. Measure compressor winding resistance (should be balanced within 0.5Ω)
4. Test run capacitor if equipped
5. Replace inverter board if all else checks out — **Part: Bosch IDS 2.0 outdoor inverter PCB** (~$380–$550)

---

### E07 — Low Voltage to Inverter

DC bus voltage dropped below minimum. Can indicate a power quality issue or capacitor failure on the DC bus.

**Fix:**
1. Measure incoming line voltage (should be 208–240VAC ±10%)
2. Check and tighten all power connections at outdoor disconnect
3. If voltage is correct, capacitor bank on inverter board is likely failing

---

### E08 — Defrost Sensor Fault

Defrost sensor (thermistor) on outdoor coil is open, shorted, or reading out-of-range.

**Fix:**
1. Disconnect defrost sensor connector and measure resistance — Bosch uses a 10KΩ NTC thermistor (at 77°F, should read ~10KΩ)
2. Replace sensor if out-of-range: **Part: Bosch IDS defrost thermistor** (~$35–$60)

---

### E09 — Indoor Ambient Sensor Fault

Same diagnosis as E08 but for the indoor return air temperature sensor.

---

### E10 — Compressor Overload

Compressor PTC (current protection) tripped. Indicates the compressor is running at excess current.

**Causes:**
- High load condition (extreme temperatures)
- Refrigerant overcharge
- Compressor failing (worn bearings drawing more current)

---

### E11 — Fan Motor Fault (Indoor or Outdoor)

Fan motor overcurrent or speed feedback fault.

**Fix:**
1. Check fan motor for physical binding
2. Check fan motor capacitor (if single-phase motor)
3. For IDS 2.0 outdoor unit: the ECM outdoor fan is controlled by the inverter — check inverter output voltage to motor
4. Replace ECM fan motor if faulty: **Part: Bosch IDS outdoor ECM fan motor** (~$180–$280)

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Bosch IDS outdoor inverter PCB](https://www.amazon.com/s?k=Bosch+IDS+heat+pump+inverter+control+board&tag=errorcodefixes-20) | E06 inverter module fault, IPM failure | $380–$550 |
| [Defrost thermistor / NTC sensor](https://www.amazon.com/s?k=heat+pump+defrost+sensor+10k+thermistor&tag=errorcodefixes-20) | E08 defrost sensor fault | $35–$60 |
| [Indoor air handler control board](https://www.amazon.com/s?k=Bosch+IDS+indoor+air+handler+control+board&tag=errorcodefixes-20) | E01/E02 communication fault after wiring is confirmed good | $220–$380 |
| [ECM outdoor fan motor](https://www.amazon.com/s?k=heat+pump+ECM+outdoor+fan+motor&tag=errorcodefixes-20) | E11 fan motor fault | $180–$280 |
| [Filter-drier (liquid line)](https://www.amazon.com/s?k=liquid+line+filter+drier+refrigerant&tag=errorcodefixes-20) | E03 after refrigerant system work | $25–$50 |

---

## When to Call a Pro

- Any fault involving refrigerant (E03, E04, E05) — requires EPA 608 certification to handle refrigerant
- E06 inverter module — replacing the IPM board involves working near high-voltage DC bus (400VDC+) which retains charge after power-off
- Any fault that returns immediately after reset — indicates underlying failure, not a transient
- If fault codes don't match this guide — Bosch occasionally updates firmware and fault code definitions; download the current service manual from bosch-climate.us

---

## Frequently Asked Questions

**How do I reset the Bosch IDS 2.0 after a fault?**
Power off the outdoor disconnect for 5 minutes to allow the DC bus capacitors to discharge, then restore power. If using a BCC100 thermostat, you can also navigate to Settings → Service → Clear Faults. If the fault returns within a few minutes of reset, the root cause has not been fixed.

**What refrigerant does the Bosch IDS 2.0 use?**
R-410A. The IDS 2.0 was designed before the R-410A phase-down; newer models may use R-32. Check the nameplate on the outdoor unit. R-410A systems require gauges and recovery equipment rated for 400+ PSI working pressure.

**The E01 code appeared after installation — is this normal?**
No. E01 immediately after installation almost always means a wiring error on the communication circuit. Double-check that the C, R, Y, and communication wires are landed on matching terminals at both indoor and outdoor units. The IDS 2.0 uses a dedicated 2-wire communication bus — it cannot share wiring with a conventional thermostat wire.

**Can I diagnose the IDS 2.0 without the BCC100 thermostat?**
Yes, but with less detail. The indoor air handler has a diagnostic LED that blinks fault codes in sequences. Count blinks: pause, count again. A service manual translates these blink codes. However, the BCC100 thermostat gives you the full numeric E-code, fault history, and system status — strongly recommended for this system.
