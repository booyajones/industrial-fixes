---
title: "Copeland Scroll Compressor Fault Codes — Complete Troubleshooting Guide"
description: "Copeland scroll compressor fault codes for ZR, ZF, ZP, and ZS series. What each code means and how to fix it."
pubDatetime: 2026-04-27T20:00:00Z
modDatetime: 2026-04-27T20:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - compressor
  - copeland
---

## Copeland Scroll Compressor Fault Codes — What You're Looking At

Copeland scroll compressors use two diagnostic platforms depending on application and vintage: the **CoreSense Diagnostics module** (LED flash codes) and the **Electronic Unit Controller (EUC)** (alphanumeric display codes on condensing units). A third platform, **CoreSense Diagnostics v2.11**, applies specifically to Discus compressors.

This guide covers all three. It assumes you know how to pull pressures, read a clamp meter, and are licensed to work on refrigerant systems.

[Jump to CoreSense AC Codes](#coresense-ac) | [Jump to CoreSense Refrigeration Codes](#coresense-ref) | [Jump to EUC Display Codes](#euc-codes) | [Jump to Reset Procedures](#reset)

---

## CoreSense LED Color Meaning — Quick Reference

Before reading any code, confirm which LED is doing what.

**CoreSense AC module (AE8-1385 — ZPS*K5 UltraTech single-phase A/C):**

| LED | State | Meaning |
|-----|-------|---------|
| Green | Solid | Normal operation, no fault |
| Yellow (ALERT) | Flashing | Alert — count the flashes |
| Red (TRIP/LOCK) | Solid | Trip — demand present, compressor not running, will auto-reset |
| Red (TRIP/LOCK) | Flashing | Lockout — count flashes, manual reset required |
| Both LEDs | Flashing simultaneously | Brown-out — control circuit voltage too low |

**CoreSense Refrigeration module (AE8-1424 — ZB/ZF/ZS K4/KC/K5 series):**

| LED | State | Meaning |
|-----|-------|---------|
| Green | Solid | Normal run |
| Green | Flashing | Alert without protective shutdown |
| Yellow | Flashing | Trip alert — compressor stopped, auto-resets when condition clears |
| Yellow | Solid | Demand present, no current sensed — compressor not running |
| Red | Flashing | Lockout — count flashes, power cycle required to reset |
| Blue | Slow flashing | Digital unloader is energized (ZFD/ZBD Digital Scroll) |

---

## CoreSense AC Flash Codes (A/C and Heat Pump — AE8-1385) {#coresense-ac}

These apply to Copeland Scroll **ZPS\*K5** single-phase UltraTech compressors with the CoreSense module (P/N 571-0072-00). The module monitors current draw via internal sensing and infers system faults from run time and trip behavior patterns.

### Code 1 — Long Run Time

**LED:** Yellow, 1 flash | **Lockout:** None — advisory only (disabled in heat pump mode)

The compressor has run continuously for more than 18 hours at full load.

**Causes (order of frequency):**
1. Low refrigerant charge — system can't satisfy setpoint
2. Dirty condenser coil or blocked airflow
3. Undersized equipment for the load
4. Failed or restricted TXV

**Diagnosis:** Pull suction and discharge pressures. Low suction pressure with long run time is a charge problem. Normal pressures with a dirty coil — clean it. If pressures and airflow are correct, do a Manual J load check.

**Reset:** Advisory only. Clears automatically once run time drops below threshold.

---

### Code 2 — Compressor Pressure Trip

**LED:** Yellow, 2 flashes | **Lockout:** Red flash 2 after 4 consecutive or 10 total events

The compressor ran for 12 seconds to 15 minutes, then tripped on a condition lasting longer than 7 minutes. The CoreSense module infers a pressure-related hard trip.

**Causes:**
1. Condenser fan not running — head pressure climb trips the compressor
2. Dirty or blocked condenser coil
3. Non-condensables in the system
4. Refrigerant overcharge
5. Defective high-pressure switch or wiring to it

**Diagnosis:** Check condenser fan operation first. Measure head pressure against outdoor ambient — if discharge pressure is unusually high for the conditions, you have a heat rejection problem. Verify the HPS setting and check for open or erratic switch behavior.

**Reset:** If in lockout, remove condition first, then power cycle the module or press manual reset.

---

### Code 3 — Pressure Switch Cycling

**LED:** Yellow, 3 flashes | **Lockout:** Red flash 3 after 4 consecutive or 10 total events

The compressor ran for 12 seconds to 15 minutes, then tripped on a condition lasting 35 seconds to 7 minutes. Shorter trip duration than Code 2 — the pressure switch is opening and resetting rapidly.

**Causes:**
1. Low refrigerant charge — low-side pressure cycling near the LPS cutout
2. Dirty evaporator coil or restricted airflow across the indoor coil
3. Defective or miswired low-pressure switch
4. Marginal TXV operation
5. Condenser fan cycling erratically causing head pressure surges

**Diagnosis:** Monitor suction pressure in real time while the compressor tries to run. If it drops to the LPS cutout point quickly, you have a charge or airflow problem. If pressures are correct but cycling continues, check LPS wiring and set point.

**Reset:** Same as Code 2 — clear the condition, then power cycle.

---

### Code 4 — Locked Rotor

**LED:** Yellow, 4 flashes | **Lockout:** Red flash 4 after 10 consecutive events

The compressor tripped within 12 seconds of attempted start and failed to restart within 35 seconds. Indicates the motor is not getting up to speed.

**Causes:**
1. Failed run or start capacitor — most common on single-phase systems
2. Low line voltage — check at the contactor, not at the panel
3. Liquid refrigerant slugging the compressor at startup
4. Failed motor windings or seized bearings
5. Defective contactor not fully closing

**Diagnosis:** Measure capacitor microfarads with a capacitor tester — even a cap that reads "in range" on a multimeter can fail under load. Check line voltage under start attempt. Measure winding resistance from each terminal to ground. If the compressor hums but doesn't start and a new capacitor doesn't fix it, the compressor has failed.

**Reset:** Power cycle after 10 lockout events. A Code 4 lockout after a new capacitor install and correct voltage means compressor replacement.

---

### Code 5 — Compressor Moderate Run Trip

**LED:** Yellow, 5 flashes | **Lockout:** Red flash 5 after 4 consecutive or 10 total events

The compressor ran for 15 minutes to 18 hours, then tripped on a condition lasting longer than 7 minutes. Distinguished from Code 2 by the longer successful run time before failure.

**Causes:**
1. Thermal overload — motor temperature rises over a full run cycle
2. High discharge temperature from inefficient operation
3. Low refrigerant charge causing elevated motor temperature
4. High ambient conditions pushing motor above thermal limit
5. Worn motor winding insulation causing intermittent shorts

**Diagnosis:** Let the system run until it trips. Check discharge line temperature — should stay below 225°F (107°C) for most applications. If the compressor runs fine for an hour then shuts off, motor thermal protection is doing its job. Measure winding resistance cold versus after a run cycle if you suspect winding degradation.

**Reset:** Allow full cool-down before resetting — minimum 30 minutes. If Code 5 repeats, the compressor needs replacement.

---

### Code 6 — Open Start Circuit (Immediate Lockout)

**LED:** Red, 6 flashes | **Lockout:** 1 occurrence — immediate

The module sees demand (Y terminal energized) and current in the R (run) winding, but detects no current in the S (start) winding after 2 seconds.

**Causes:**
1. Failed run capacitor (the start winding capacitor-switched circuit is open)
2. Open circuit in the start winding wiring or at the S terminal
3. Damaged start winding inside the compressor
4. Loose or corroded terminal connection at S

**Diagnosis:** Check capacitor first. Measure resistance of start winding from S terminal to common (C). An open start winding reads infinite resistance. Compare R and S winding resistance values — they should be close on most single-phase scrolls.

**Reset:** Fix the electrical fault, then power cycle the module.

---

### Code 7 — Open Run Circuit (Immediate Lockout)

**LED:** Red, 7 flashes | **Lockout:** 1 occurrence — immediate

The inverse of Code 6 — demand is present, current is in the S (start) winding, but no current in the R (run) winding after the normal window.

**Causes:**
1. Open circuit in run winding wiring or at the R terminal
2. Damaged run winding inside the compressor
3. Defective contactor not closing one set of contacts

**Diagnosis:** Check R terminal wiring continuity. Measure run winding resistance R-to-C. If winding resistance is open, compressor needs replacement.

---

### Code 8 — Welded Contactor

**LED:** Yellow, 8 flashes | **Lockout:** Alert only — does not lock out

The module sees current in both S and R windings for 15 seconds while demand is absent. The contactor contacts are stuck closed.

**Causes:**
1. Welded contactor contacts from repeated high-inrush starts
2. Contactor coil failure causing contacts to stay energized
3. Contactor undersized for the application

**Diagnosis:** Remove demand (turn off thermostat), wait 15+ seconds. If the compressor keeps running, disconnect power and physically inspect the contactor — try to separate the contacts manually. A welded contactor is a fire and compressor-damage risk. Replace immediately.

**Reset:** Module alerts but does not lock out for Code 8. Fix the contactor.

---

### Code 9/10 — Low Voltage / Over-Current at PROT Terminal

**Code 9 (Low Voltage):** Both ALERT and TRIP/LOCK LEDs flash simultaneously — brown-out condition. Control voltage is too low for reliable operation.

**Code 10 (Over-Current at PROT terminal):** Red flashes 10 times, yellow off. Current at the PROT terminal exceeds 2A for 40ms. Indicates miswiring or a shorted contactor coil. Immediate lockout.

---

## CoreSense Refrigeration Flash Codes (ZB/ZF/ZS/ZP Series — AE8-1424) {#coresense-ref}

The refrigeration CoreSense module is factory-mounted in the terminal box on 7.5–15 HP **ZB\*K5 and ZF\*K5** compressors, and available as a panel-mount kit (P/N 543-0223-00) for 2–7.5 HP **ZB\*KC, ZF\*K4/KVE, and ZS\*K4** compressors. The 7.5–15 HP module is P/N 543-0209-00.

These modules are **not interchangeable** — the current detection ranges differ between compressor families. Swapping modules causes nuisance trips.

The refrigeration version has four LEDs: **Green, Yellow, Red, and Blue**. Alert codes that cause a protective shutdown (severe alerts) trip the compressor via the M1-M2 relay. A trip auto-resets once the condition clears and the minimum off time expires. A lockout requires a manual power cycle.

### Severe Alert Codes — Compressor Trip or Lockout

| Code | Flash Color | Condition | Default Action |
|------|------------|-----------|----------------|
| 1 | Yellow, 1 flash | High discharge temperature | Trip (configurable to lockout) |
| 2 | Yellow, 2 flashes | Missing/open phase | Trip (configurable to lockout) |
| 4 | Yellow, 4 flashes | Locked rotor | Trip (configurable to lockout) |
| 6 | Yellow, 6 flashes | Reverse phase | **Automatic lockout — cannot be changed** |
| 7 | Yellow, 7 flashes | Short cycling | Trip |
| 9 | Yellow, 9 flashes | Low current / compressor not running with demand | Alert/trip |

### Non-Severe Alert Codes

| Code | Flash Color | Condition |
|------|------------|-----------|
| 3 | Green, flashing | Communication error (network mode only) |
| 5 | Yellow, 5 flashes | Current sensor fault / missing CT |

---

### High Discharge Temperature — Code 1 (Refrigeration)

Triggered when discharge line temperature or top cap temperature exceeds the protection threshold. For low-temp scroll compressors, this threshold is tighter because the operating envelope is narrower.

**Causes:**
1. Low refrigerant charge — insufficient mass flow to cool the scroll sets
2. Liquid injection system malfunction (ZF low-temp models with EXV injection)
3. High condensing temperature from dirty coil or fan failure
4. Excessive superheat at suction
5. Refrigerant migration — liquid in the compressor at startup

**Diagnosis:** Monitor discharge temperature with the thermistor data via the E2 controller or an independent DLT clamp probe. A properly charged system should keep DLT below 225°F (107°C) on medium-temp, below 250°F (121°C) on low-temp. Check that the DLT thermistor is making full contact with the discharge line and that the insulation boot is intact.

For low-temp ZF models with liquid injection: verify the EXV is receiving the stepper motor signal from the CoreSense module and that the EXV isn't stuck or blocked.

---

### Phase Loss / Missing Phase — Code 2 (Refrigeration)

One leg of the three-phase supply is absent or significantly low. On a scroll compressor, loss of phase means the remaining two phases carry the full load — the compressor will attempt to run but will pull extremely high current and fail quickly without protection.

**Causes:**
1. Blown fuse in one phase of the disconnect
2. Loose or burned connection at the contactor or terminal block
3. Utility supply issue — single phase on a three-phase feed
4. Failed contactor contact

**Diagnosis:** Measure all three phase voltages at the compressor contactor with the contactor pulled in. All three should be within 2% of each other. Phase voltage imbalance above 2% causes derating; above 5% causes immediate concern. If one phase is zero or significantly low, trace upstream to the disconnect and utility.

---

### Reverse Phase — Code 6 / Lockout (Refrigeration)

**This is the only refrigeration CoreSense code that always results in a lockout and cannot be configured to trip.** A Copeland scroll compressor will run in reverse if phasing is wrong — the orbiting scroll attempts to move opposite its design direction, which causes immediate internal damage. The CoreSense module catches this at startup before damage occurs.

**Causes:**
1. Incorrect phase sequence at installation — L1/L2/L3 not connected in proper order
2. Phase correction work upstream that changed the rotation

**Diagnosis:** You'll typically see this on new installations or after electrical work. Verify rotation direction agrees with the phase sequence indicator or check the phase rotation with a phase meter.

**Fix:** Swap any two power leads at the contactor (not at the compressor terminals). Do not use the compressor rotation to check — the scroll will not indicate the problem externally.

**Reset:** Power cycle the CoreSense module. Do not attempt multiple restart cycles — each restart attempt with reversed phasing causes mechanical damage.

---

## Electronic Unit Controller (EUC) Display Codes (AE8-1376) {#euc-codes}

Copeland condensing units with the **Electronic Unit Controller** show alphanumeric codes on a small display. The EUC handles low-pressure control (suction transducer-based), fan cycling, bump start, and data logging. It does NOT replace the fixed high-pressure UL safety switch.

| Code | Condition | Action Required |
|------|-----------|----------------|
| **HP** | High pressure trip | Compressor off, auto-resets after HP switch resets + 5 min minimum off time |
| **HPL** | High pressure lockout | Manual reset required (see below) |
| **dLt** | Discharge line temperature alarm | Compressor tripped — DLT above threshold |
| **dLL** | Discharge line temperature lockout | Manual reset required |
| **HA** | High condenser temperature alarm | Fan-side issue |
| **P1** | Suction pressure probe failure | Replace transducer or check wiring |
| **P2** | Condenser probe failure | Replace probe or check wiring |
| **P3** | DLT probe failure | Check thermistor connections |
| **EE** | Module failure (EEPROM error) | Replace EUC module |
| **PoF** | Keypad locked | Press and hold buttons per AE8-1376 to unlock |

### HP — High Pressure Trip

The fixed high-pressure safety switch has opened. This is a mechanical switch, not a sensor — it opens at a set pressure and must cool/reset before the EUC will restart the compressor (5-minute minimum).

**Causes:**
1. Condenser fan failure — head pressure climbs unchecked
2. Blocked condenser coil or discharge air recirculation
3. Refrigerant overcharge
4. Non-condensables in the system
5. Defective HP switch (opens prematurely)

**Diagnosis:** Pull head pressure while the fan is running. Compare against a P-T chart for your refrigerant at the outdoor ambient temperature. Head pressure 50–100 PSI above expected for ambient = heat rejection problem. Measure fan amp draw — a weak fan can cause recurrent HP trips without obviously stopping.

### HPL — High Pressure Lockout

After multiple HP trips within the counter window, the EUC locks out. The HP counter threshold and lockout behavior can be reset via the Advanced Options menu (code **rSA** — set N to Y).

**Reset procedure:** Hold the Start button for 3 seconds, release, then hold again for 3 seconds. Or cycle unit power. The alarm condition (HP switch) must have already reset and the 5-minute minimum off time must have completed before the manual reset will take effect.

### dLt / dLL — Discharge Line Temperature Alarm and Lockout

The discharge line thermistor has measured a temperature above the DLT trip set point. Like the HPL, repeated dLt trips trigger a dLL lockout.

**Default trip settings:** Factory defaults vary by condensing unit model — refer to the inside panel label or AE8-1376 for the specific set point. Typical medium-temp units trip around 225°F (107°C).

**Reset:** Same procedure as HPL — hold Start 3 seconds twice, or power cycle. Temperature must have dropped below the reset threshold first.

---

## Copeland Digital Scroll Compressors (ZFD/ZBD Series)

Digital Scroll compressors (ZFD low-temp, ZBD medium-temp) modulate capacity by unloading the scroll sets via a digital solenoid valve. When the solenoid energizes, the orbiting scroll lifts off the fixed scroll — the compressor keeps running but moves no refrigerant. The duty cycle between loaded and unloaded states determines actual capacity.

The **Blue LED on the CoreSense refrigeration module** indicates the digital unloader solenoid is energized. Slow blue flashing is normal — the duty cycle changes from 2 to 20 seconds depending on how much capacity the rack controller is requesting.

**Common Digital Scroll faults:**

| Symptom | First Check |
|---------|------------|
| System runs but cannot pull down | Solenoid stuck open — compressor stays unloaded. Check 110/220VAC at solenoid coil terminals |
| System pulls down but hunts constantly | E2 suction group configuration, enhanced suction group not enabled |
| No blue LED but DIP switch 2 is ON | Verify demand signal and analog input wiring (1-5V) |
| Communication error (Code 3) | Check RS485 wiring polarity, DIP switch 10 termination on last unit, baud rate match |

**Capacity ranges:**
- 2–7.5 HP ZBD/ZFD (KC/K4/KVE): 10–100%
- 7.5–15 HP ZFD K5 (low-temp): 30–100%
- 7.5–15 HP ZBD K5 (medium-temp): 10–100%

---

## Reset Procedures {#reset}

### CoreSense AC Module Reset (AE8-1385)
1. Confirm the fault condition no longer exists (pressures normal, voltage correct, capacitor good)
2. Press the manual reset button on the module face, **or** cycle power to the module
3. The lockout code clears and the compressor restarts on the next demand signal
4. If the lockout recurs within the same call, diagnose the root cause — resetting alone doesn't fix it

### CoreSense Refrigeration Module Reset (AE8-1424)
1. Verify the cause is corrected
2. Cycle power to the CoreSense module (not just the compressor contactor — the module must lose power)
3. For E2-networked systems, a remote reset can be sent via the E2 controller without physically cycling power
4. Module returns to normal operation on next demand signal

### EUC HPL / dLL Reset
1. Confirm HP switch has reset (for HPL) or DLT has dropped below reset threshold (for dLL)
2. Wait for 5-minute minimum off time to complete
3. Hold Start button for 3 seconds, release, hold again for 3 seconds
4. Alternatively, cycle unit power
5. To reset the alarm counter: enter Advanced Options menu → find **rSA** → change N to Y

### Factory Reset (CoreSense Refrigeration Module)
To erase all stored fault history and return to factory defaults: transition **Blue DIP switch 5 from OFF to ON within 5 seconds of module power-up**. This clears configuration and history — use only when replacing a module or during initial commissioning.

---

## Parts Reference

| Part | P/N | Application |
|------|-----|-------------|
| CoreSense Diagnostics Module (7.5–15 HP K5) | 543-0209-00 | ZB*K5, ZF*K5 refrigeration |
| CoreSense Diagnostics Module (2–7.5 HP) | 543-0223-00 | ZB*KC, ZF*K4/KVE, ZS*K4 |
| Current Transducer (CT) | 543-0159-00 | All refrigeration CoreSense |
| Medium-Temp CoreSense Kit (2–7.5 HP) | 943-0050-00 | ZB*KC/ZS*K4 with CT + thermistor |
| Low-Temp CoreSense Kit (4–7.5 HP KVE) | 943-0051-00 | ZF*KVE with CT + EXV |
| Low-Temp CoreSense Kit (4–7.5 HP K4) | 943-0051-01 | ZF*K4 with CT + EXV |
| Top Cap Thermistor Kit | 998-0176-00 | Discharge temp sensing |
| Top Cap Thermistor Only | 998-0229-00 | Replacement sensor |
| External Motor Protection Module | 971-0641-00 | Motor protection |
| 120V Digital Solenoid Coil | 998-0060-03 | Digital Scroll ZFD/ZBD |
| 240V Digital Solenoid Coil | 998-0060-04 | Digital Scroll ZFD/ZBD |
| CT Extension Cable, 3 ft | 529-0297-00 | Panel-mount installs |
| CT Extension Cable, 10 ft | 529-0297-01 | Panel-mount installs |

---

## Key Takeaways for Field Diagnosis

**The CoreSense module reports behavior, not root cause.** A Code 3 (pressure switch cycling) can come from a dirty evaporator, a malfunctioning LPS, marginal charge, or a failing TXV. The code tells you what the compressor experienced — your job is to find out why.

**Lockout threshold matters.** Code 2 and Code 3 lock out after 4 consecutive events. Code 4 (locked rotor) requires 10. Reverse phase on refrigeration CoreSense locks out immediately on the first occurrence. If you're seeing a lockout, count how many attempts were logged before it tripped — it changes the urgency of the root cause.

**Don't reset and leave.** A reset without root-cause correction is a temporary fix. If the system trips again within the same service call, log your pressures, temperatures, and amp draws before you leave. Repeated lockouts degrade compressor windings through thermal cycling even when each individual event appears minor.

**Digital Scroll blue LED is not a fault.** A slow-flashing blue LED means the unloader solenoid is energized and the compressor is running at reduced capacity — this is normal operation, not an alarm.

**Module part numbers are not interchangeable between compressor families.** Installing a K5 module (3A minimum detection) on a 2–4 HP KC compressor (1A minimum) will cause nuisance current-based trips at low load. Match module P/N to compressor family exactly.

---

*Sources: Copeland Application Engineering Bulletins AE8-1385, AE8-1424, AE8-1376, AE8-1367, AE8-1368 (Emerson/Copeland). Copeland is now a standalone brand under Emerson's Climate Technologies division.*

## Where to Buy Replacement Parts

Find replacement parts for Copeland scroll compressors on Amazon:

- [Copeland Compressor Parts & Accessories](https://www.amazon.com/s?ascsubtag=ecf-copeland-scroll-compressor-fault-codes&k=Copeland+compressor+parts&tag=errorcodefixes-20)
- [Copeland CoreSense Module Replacement](https://www.amazon.com/s?ascsubtag=ecf-copeland-scroll-compressor-fault-codes&k=Copeland+CoreSense+module+replacement&tag=errorcodefixes-20)
- [Copeland Scroll Compressor Thermistor](https://www.amazon.com/s?ascsubtag=ecf-copeland-scroll-compressor-fault-codes&k=Copeland+scroll+compressor+thermistor&tag=errorcodefixes-20)