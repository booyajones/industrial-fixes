---
title: "Rheem Prestige RP20 Heat Pump Error Codes - Full Fault Code Reference"
description: "Complete guide to Rheem Prestige RP20 variable-speed heat pump error codes, including LED flash codes, communicating thermostat faults, and refrigerant fault diagnostics. Learn what each fault means and how to fix it."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Rheem Prestige RP20 is one of the most capable residential heat pumps on the market — a variable-speed, communicating unit designed for maximum comfort and efficiency. But when something goes wrong, it speaks in flash codes and fault numbers that can be confusing to decipher. This guide covers every major RP20 error code so you can diagnose the problem fast.

## What Does the Rheem RP20 Error Code Mean?

The Rheem Prestige RP20 uses two parallel fault-reporting systems: **LED flash codes** on the control board inside the unit, and **alphanumeric fault codes** displayed on a compatible communicating thermostat (such as the Rheem EcoNet Smart Thermostat or the Prestige IAQ touchscreen). If you have a non-communicating thermostat, you'll need to read the LED blinks on the control board directly.

### How to Read LED Flash Codes

On the RP20 outdoor unit, locate the diagnostic LED on the control board (visible through the service panel). Count the number of flashes in a sequence, then pause, then count again. The pattern tells you the fault category.

---

## Common Rheem RP20 Error Codes

### 1 Flash — Normal Operation / Standby
The unit is powered and in standby. No fault present. If you see this and the unit still won't run, check thermostat demand signals and wiring continuity.

### 2 Flashes — High Pressure Fault
The high-pressure switch tripped. This typically means refrigerant pressure on the discharge side exceeded safe limits.

**Causes:**
- Dirty or blocked condenser coil (most common)
- Refrigerant overcharge
- Failed condenser fan motor
- Restricted refrigerant flow (kinked line, failed TXV/EEV)

**Fix:** Turn off the unit. Inspect the outdoor coil for debris — leaves, grass, and cottonwood are frequent offenders. Clean with a hose at low pressure. If the coil is clean, call a licensed tech; overcharge and TXV problems require refrigerant tools.

### 3 Flashes — Low Pressure Fault
The low-pressure switch tripped, indicating insufficient refrigerant pressure on the suction side.

**Causes:**
- Low refrigerant charge (leak)
- Blocked indoor coil or dirty air filter
- Failed expansion valve
- Extreme cold temperatures causing low suction pressure

**Fix:** Start by replacing the air filter and checking indoor airflow. If airflow is fine and fault persists, suspect a refrigerant leak. This requires a certified HVAC technician to locate the leak, repair it, and recharge.

### 4 Flashes — Open Start Circuit / Defrost Fault
This code appears when the defrost cycle fails to initiate or terminate correctly. In heating mode, frost builds on the outdoor coil; the defrost board is supposed to manage it automatically.

**Causes:**
- Faulty defrost control board
- Bad defrost thermostat or sensor
- Reversing valve stuck in heating position (won't switch to cooling mode for defrost)
- Outdoor ambient temperature sensor failure

**Fix:** Check the defrost thermostat resistance with a multimeter. It should show continuity when cold and open when warm. If the reversing valve is suspect, you'll hear a "click" when it's commanded — silence indicates solenoid or valve failure.

### 5 Flashes — Open Outdoor Temperature Sensor
The outdoor ambient temperature sensor has failed or its circuit is open.

**Fix:** Locate the sensor on the outdoor coil tubing. Unplug the connector and test resistance across the two terminals with a multimeter. Compare to the temperature/resistance chart in the service manual. Out-of-spec readings mean sensor replacement. The sensor is inexpensive and a straightforward swap.

### 6 Flashes — Open Indoor Temperature Sensor (Communicating Mode)
The indoor coil thermistor or suction line sensor has failed. This sensor helps the variable-speed compressor modulate capacity.

**Fix:** Access the indoor air handler. Locate the thermistor clipped to the refrigerant tubing. Test resistance. Replace if out of spec.

### 7 Flashes — Compressor Protection / Lockout
The unit experienced a compressor fault. This is a hard lockout — the unit shuts down to protect the compressor from damage.

**Causes:**
- Compressor overcurrent
- Low voltage at compressor
- High discharge temperature
- Inverter drive fault

**Fix:** After a compressor lockout, wait 30 minutes before attempting a restart. Check supply voltage at the unit — it must be within ±10% of nameplate rating. If voltage is correct and the unit locks out again immediately, the inverter drive or compressor may require professional diagnosis.

### 8 Flashes — Reversing Valve Fault
The reversing valve solenoid failed to switch the system between heating and cooling mode.

**Causes:**
- Failed solenoid coil
- Stuck valve spool
- Low voltage to solenoid

**Fix:** Test the solenoid coil with a multimeter — it should show 20–30Ω resistance. An open reading means the coil is burned out. A mechanically stuck valve requires a refrigerant system recover and valve replacement — a tech job.

### Communicating Thermostat Fault Codes (EcoNet / Prestige IAQ)

If you use a communicating thermostat, you'll see alphanumeric codes:

| Code | Meaning |
|------|---------|
| E1 | Indoor coil sensor fault |
| E2 | Outdoor ambient sensor fault |
| E3 | Discharge line sensor fault |
| E4 | Suction line sensor fault |
| E5 | High pressure switch open |
| E6 | Low pressure switch open |
| E8 | Communication loss between indoor and outdoor units |
| HP | High pressure lockout |
| LP | Low pressure lockout |
| dF | Defrost cycle active (not a fault — normal operation) |

**Code E8 — Communication Loss** is one of the most common calls on communicating systems. Check:
1. The communication wire between indoor and outdoor units (typically a 2-conductor 18 AWG wire)
2. Both boards for loose terminals
3. Power to both units — if the indoor board lost power, communication drops

---

## How to Fix It

1. **Record the fault code** — write down the flash count or thermostat code before resetting.
2. **Power cycle the unit** — turn off the disconnect for 30 seconds, then restore power.
3. **Check the air filter first** — a clogged filter causes more fault codes than almost anything else.
4. **Inspect the outdoor coil** — debris blocking airflow causes high-pressure faults.
5. **Check all wiring connections** — loose terminals at the control board are a common root cause.
6. **Test sensor resistances** — use a multimeter to check thermistors against their spec table.
7. **If the compressor locked out** — wait at least 30 minutes before reset attempt.
8. **For refrigerant faults (E5, E6, 2-flash, 3-flash)** — call a licensed HVAC technician. These require specialized tools.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Rheem RP20 Defrost Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Controls defrost cycles; fails with 4-flash fault | $85–$150 |
| [Heat Pump Outdoor Ambient Temperature Sensor](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) | Triggers 5-flash fault when failed; inexpensive fix | $15–$40 |
| [Reversing Valve Solenoid Coil](https://www.amazon.com/s?i=industrial&k=heat+pump+reversing+valve+solenoid+coil&tag=errorcodefixes-20) | Replaces burned-out coil on 8-flash faults | $20–$55 |
| [HVAC Multimeter with Temperature Probe](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20) | Essential for testing sensors, voltage, and continuity | $35–$120 |
| [18 AWG 2-Conductor Communication Wire](https://www.amazon.com/s?i=industrial&k=18+AWG+2+conductor+thermostat+wire&tag=errorcodefixes-20) | Fixes communication loss faults between indoor/outdoor | $15–$40 |

---

## When to Call a Pro

Call a licensed HVAC technician immediately if:

- **The unit repeatedly trips high or low pressure faults** — this indicates a refrigerant issue that requires recovery equipment and EPA 608 certification to diagnose and repair.
- **The compressor keeps locking out** — repeated compressor lockouts can indicate a failing inverter drive or compressor. Operating a damaged compressor will destroy it.
- **You see a refrigerant leak** — oil stains near refrigerant lines, ice buildup on lines, or hissing sounds all indicate a leak. Do not restart the unit.
- **Voltage at the unit is low** — if your supply voltage is consistently under 208V on a 230V unit, you have a utility or panel issue that needs an electrician.
- **Communication faults persist after rewiring** — if the E8 code won't clear after checking wiring, one of the control boards may need replacement, which requires board-level diagnosis.

The RP20 is a sophisticated variable-speed system. The control boards, inverter drive, and refrigerant system are not DIY-friendly. The sensors and wiring checks are — start there.

---

## Frequently Asked Questions

**Q: My Rheem RP20 shows 2 flashes but the outdoor coil looks clean. What else should I check?**

A: After verifying the coil is clean, check the condenser fan motor — if it's spinning slowly or not at all, airflow drops and pressure spikes. Also check for refrigerant overcharge if the system was recently serviced. A tech can confirm overcharge with manifold gauge readings.

**Q: The E8 communication fault keeps coming back after I reset it. What's causing it?**

A: Intermittent E8 faults are usually caused by a marginal connection in the communication wire, especially at the terminals on either board. Re-strip and re-terminate both ends of the wire. If that doesn't solve it, check that the outdoor unit control board has clean, stable 24VAC power from its transformer. A sagging transformer voltage will cause intermittent communication dropouts.

**Q: Can I reset a compressor lockout by simply cycling the breaker?**

A: Yes, but wait at least 30 minutes after cycling power. The variable-speed compressor has built-in protection timers. Forcing a restart too quickly can cause repeated lockouts. If the unit locks out immediately after a proper restart, the fault is active and the underlying cause — high discharge temperature, low voltage, or inverter fault — needs to be diagnosed before forcing more restarts.

**Q: What's the difference between the Rheem RP20 and the Ruud RP20?**

A: They're functionally identical — Rheem and Ruud are sister brands manufactured by Paloma Industries. The control boards, sensors, fault codes, and parts are all interchangeable. Service manuals from either brand apply to both units.
