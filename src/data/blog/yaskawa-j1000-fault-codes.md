---
title: "Yaskawa J1000 Fault Codes — VFD Troubleshooting Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: yaskawa-j1000-fault-codes
featured: false
draft: false
tags:
  - yaskawa
  - vfd
  - industrial
  - motor-drive
description: "Yaskawa J1000 fault codes OC, OV, UV, OL1, OL2, OH, GF explained. Diagnose and fix overcurrent, overvoltage, overload, and ground faults on J1000 AC drives."
---

## Yaskawa J1000 Fault Codes

The **Yaskawa J1000** is an entry-level V/f control AC drive widely used in HVAC fan applications, conveyor systems, pumps, and light industrial equipment. It's known for its compact footprint and straightforward commissioning — but when a fault code appears on the LED display, you need to know exactly what it means and how to respond.

This guide covers the most common J1000 fault codes and step-by-step fixes.

---

## Common J1000 Fault Codes

| Code | Description |
|------|-------------|
| OC | Overcurrent |
| OV | DC Bus Overvoltage |
| UV | DC Bus Undervoltage |
| OL1 | Motor Overload |
| OL2 | Drive Overload |
| OH | Heatsink Overtemperature |
| GF | Ground Fault |

---

## OC — Overcurrent {#oc-overcurrent}

**What it means:** The output current has exceeded the drive's instantaneous overcurrent threshold (typically 200% of rated current). OC is the most common fault on the J1000 and almost always indicates a problem with the load, motor, or acceleration settings.

**Common causes:**
- Acceleration time (C1-01) set too short for the load inertia
- Mechanical load is jammed or stalled
- Motor is undersized for the application
- Output wiring has a phase-to-phase short
- Motor winding failure (inter-turn short)

**Diagnosis and fix:**
1. Check the driven equipment for mechanical binding. Disengage the load if possible and jog the motor unloaded — if OC clears, the issue is load-side.
2. Extend the acceleration time (C1-01, Acceleration Time 1). For fan and pump loads, try 20–30 seconds. For conveyor applications, 10–15 seconds is typical.
3. Inspect output wiring for phase-to-phase contact. Even a momentary touch during vibration can cause OC trips.
4. Megger test the motor windings (1000 VDC). A winding-to-ground reading below 1 MΩ indicates insulation failure.
5. Verify the J1000 is correctly sized. The drive's rated output current (listed on the nameplate) must exceed the motor's FLA by a reasonable margin — never run a drive at 100% of its rated current continuously.

---

## OV — DC Bus Overvoltage {#ov-overvoltage}

**What it means:** The DC bus voltage has risen above the trip threshold (~400 VDC on 230 V drives, ~800 VDC on 460 V drives) due to regenerative energy from a decelerating load.

**Common causes:**
- Deceleration time (C1-02) too short for the load inertia
- High-inertia load (fan, flywheel)
- No dynamic braking resistor installed on a high-inertia application
- High incoming line voltage

**Diagnosis and fix:**
1. Extend the deceleration time (C1-02, Deceleration Time 1). For fans with significant inertia, try 30–60 seconds.
2. Enable Stall Prevention during deceleration (L3-04 = 1). This automatically extends decel time to prevent OV trips.
3. Check incoming line voltage. Sustained overvoltage at the input will push bus voltage over the limit even during normal operation.
4. For applications where fast stops are required, add an external dynamic braking resistor using the J1000's integrated braking transistor (available on CIMR-JU models with braking transistor option).

---

## UV — DC Bus Undervoltage {#uv-undervoltage}

**What it means:** The DC bus voltage has dropped below the minimum operating level. This means the drive is losing power — either from an input side problem or an internal supply issue.

**Common causes:**
- Incoming line voltage too low or dropping under load
- Blown input fuse or tripped input breaker
- Loose or corroded input wiring terminals
- Power line interruption or voltage sag
- Internal soft-charge circuit failure

**Diagnosis and fix:**
1. Check the input voltage at the drive's L1/L2/L3 (or L1/L2 for single-phase) terminals while the drive is running. Voltage must be within ±10% of drive rating.
2. Inspect input fuses for continuity. A blown fuse on one phase causes UV on three-phase drives.
3. Check all input terminal connections for tightness and corrosion. Torque to spec (see J1000 Technical Manual, Appendix A).
4. If voltage at input terminals is correct but UV persists, the internal soft-charge circuit or DC bus capacitors may have failed — contact a drive service center.

---

## OL1 — Motor Overload {#ol1-motor-overload}

**What it means:** The drive's electronic thermal overload function has calculated that the motor has been drawing excessive current for too long. OL1 is a protective fault — it prevents motor winding damage due to sustained overcurrent.

**Common causes:**
- Mechanical load exceeds motor rated torque
- Motor Current Level (E2-01) set higher than motor nameplate FLA
- Motor running at low speed for extended time on a standard induction motor (reduced cooling)
- Single-phase power supply to a three-phase motor

**Diagnosis and fix:**
1. Verify E2-01 (Motor Rated Current) matches the motor nameplate FLA exactly. Do not set it higher than nameplate.
2. Check mechanical load — confirm driven equipment is not jamming or operating above design point.
3. For fans and pumps operating at reduced speed, ensure adequate ventilation. TEFC motors rely on their shaft-mounted fan for cooling — at low speeds, cooling is reduced and the motor can overheat at lower current than at full speed.
4. Check all three output phases for balanced current. A significant imbalance suggests a motor winding issue.

---

## OL2 — Drive Overload {#ol2-drive-overload}

**What it means:** The drive itself has been operating above its rated current continuously. Unlike OL1 which protects the motor, OL2 protects the drive's internal components.

**Common causes:**
- Drive undersized for the application
- Ambient temperature above drive rating (40°C) reducing drive capacity
- Continuous operation above 100% rated current

**Diagnosis and fix:**
1. Log operating current (U1-03 in the monitor menu) over time. If consistently at or above drive rated amps, the drive must be upsized.
2. Check ambient temperature at the drive. Above 40°C reduces drive output capacity — derate per the J1000 Technical Manual.
3. If the drive is correctly sized and ambient is within spec, OL2 on a new installation suggests the load is larger than anticipated.

---

## OH — Heatsink Overtemperature {#oh-overtemperature}

**What it means:** The heatsink temperature has exceeded the trip threshold (typically 105°C). The drive trips to prevent IGBT damage.

**Common causes:**
- Blocked or failed cooling fan
- Ambient temperature above drive rating
- Drive mounted too close to other heat sources or other drives without adequate spacing
- Heatsink fins clogged with dust or lint

**Diagnosis and fix:**
1. Listen for the internal cooling fan when the drive is powered. If it's not spinning, check the fan wiring or replace the fan.
2. Clean the heatsink fins with compressed air — blow from bottom to top to clear accumulated debris.
3. Verify drive mounting orientation (must be vertical) and minimum clearances (see installation manual — typically 2 inches top and bottom, 1 inch sides).
4. Measure ambient temperature at the drive air inlet. If above 40°C, relocate the drive or improve enclosure ventilation.

---

## GF — Ground Fault {#gf-ground-fault}

**What it means:** The drive has detected excessive leakage current to ground in the output circuit. This indicates an insulation failure in the motor, motor cable, or output terminals.

**Common causes:**
- Motor winding insulation failure
- Damaged motor cable (abraded insulation, water ingress)
- Moisture in motor terminal box

**Diagnosis and fix:**
1. Disconnect the motor cable at both the drive and the motor.
2. Megger test the motor windings at 1000 VDC. Values below 1 MΩ to ground indicate insulation failure.
3. Megger test the cable conductors to conduit/ground.
4. Inspect the motor terminal box for moisture. Dry and seal as needed.
5. If motor and cable test clean, suspect the drive's internal GF detection circuit — verify with a Yaskawa service engineer.

---

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| J1000 Replacement Cooling Fan | $30–$80 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-j1000-fault-codes&k=Yaskawa+J1000+replacement+cooling+fan+CIMR-JU&tag=errorcodefixes-20) |
| External Braking Resistor | $40–$150 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-j1000-fault-codes&k=VFD+braking+resistor+external+dynamic+braking&tag=errorcodefixes-20) |
| Motor Insulation Tester (Megohmmeter) | $80–$300 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-j1000-fault-codes&k=megohmmeter+motor+insulation+tester+1000v&tag=errorcodefixes-20) |
| True-RMS Clamp Meter | $50–$180 | [Amazon](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-yaskawa-j1000-fault-codes&tag=errorcodefixes-20) |

---

## When to Call a Technician

GF faults involving motor replacement, UV faults involving internal drive components, and any situation where you are unsure of safe isolation procedures should be handled by a qualified electrician. Always verify the DC bus has discharged to safe levels before opening the drive enclosure — the J1000 Technical Manual specifies a minimum wait time of 5 minutes after power removal.

> **Pro tip:** The J1000 stores the last four faults in the fault history (U2-02 through U2-05). Each fault log records the current, voltage, and frequency at the time of the trip. Reviewing this history before working on the drive often reveals patterns — like OC faults that always occur at the same output frequency — that point directly to the root cause.

## Related Articles

- [Yaskawa V1000 Fault Codes — Complete Guide](/posts/yaskawa-v1000-complete-guide/)
- [Yaskawa VFD OC Fault — Overcurrent Diagnosis](/posts/yaskawa-vfd-fault-oc-overcurrent/)
- [Yaskawa VFD GF Fault — Ground Fault Fix](/posts/yaskawa-vfd-fault-gf/)

## See Also

- [Yaskawa VFD Fault UV1 — Causes & Fix](/posts/yaskawa-vfd-fault-uv1/)
- [Yaskawa GA800 Uv1 Fault — DC Undervoltage Fix](/posts/yaskawa-ga800-error-uv1/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Complete Guide - Fault Codes, Parameters, and Commissioning](/posts/yaskawa-a1000-complete-guide/)
