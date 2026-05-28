---
title: "Siemens VFD F0002 Fault - Overvoltage: What It Means and How to Fix It"
description: "Siemens VFD fault F0002 means the DC bus voltage in the drive exceeded its safe limit — this overvoltage fault is one of the most common Siemens drive faults and is usually caused by regenerative energy from the motor or incoming line voltage spikes."
pubDatetime: 2026-04-25T00:00:00Z
tags: [vfd, error-codes, siemens, variable-frequency-drive, industrial]
---

## What Does Siemens VFD Fault F0002 Mean?

Fault F0002 on a Siemens variable frequency drive (VFD) — including SINAMICS G120, G110, V20, and Micromaster 420/440 series — is an **overvoltage fault on the DC bus**. 

Here's how it works: a VFD converts incoming AC power to DC (the "DC bus"), then back to AC at the frequency needed to control motor speed. The DC bus has a maximum voltage limit. When that limit is exceeded, the drive throws F0002 and trips to protect itself and the motor.

**Why does DC bus voltage spike?**

1. **Regenerative energy from the motor (most common cause).** When a motor decelerates rapidly, it acts as a generator. That energy has to go somewhere — if the VFD can't absorb it fast enough, the DC bus voltage climbs until F0002 triggers. This is especially common with high-inertia loads like fans, centrifuges, and conveyors.

2. **Incoming line voltage too high.** If the supply voltage is above the drive's rated range, the rectified DC bus voltage will be correspondingly high. On a 480V drive, F0002 typically trips at approximately 810V DC.

3. **Line voltage transients or spikes.** A voltage spike on the supply side — from power factor correction capacitor switching, a large nearby motor starting, or utility events — can push the DC bus over the limit momentarily.

4. **Drive deceleration ramp too aggressive.** If you've programmed the drive to stop too quickly, the motor generates more energy than the drive can handle. Extending the deceleration time (P1121 on G120/MM440) usually fixes this.

**Which Siemens drives use F0002?**

- SINAMICS G120 / G120C / G120D / G120P
- SINAMICS V20
- Micromaster 420
- Micromaster 440
- SINAMICS G110

The fault code is F0002 across all of these, with the same root cause.

---

## How to Fix Siemens VFD F0002

### Step 1: Identify the pattern

Ask: *When does F0002 occur?*

- **During deceleration** → Almost certainly regenerative energy. Extend the deceleration ramp.
- **During normal operation or at startup** → Likely incoming line voltage issue or transient.
- **Only under heavy loads or sudden load changes** → Could be both regeneration and line conditions.

### Step 2: Extend the deceleration ramp time

This is the fix for the majority of F0002 faults.

**On SINAMICS G120 / G120C:**
- Navigate to parameter **P1121** (Deceleration ramp time)
- Increase the value. Default is often 10 seconds. Try 20–30 seconds for fan/pump loads, 30–60 seconds for high-inertia loads like centrifuges.
- After changing P1121, run a test deceleration and observe whether F0002 clears.

**On Micromaster 440:**
- Parameter **P1121** is the same — deceleration ramp-down time.
- You can also enable the **Vdc controller** (P1240) which modulates deceleration to prevent overvoltage. Set P1240 = 1 to enable.

**On SINAMICS V20:**
- Access Quick Setup or Extended Setup and look for "Dec time" — this is the deceleration ramp parameter.

### Step 3: Enable the Vdc max controller

The Vdc max controller is a built-in feature on most Siemens drives that automatically extends deceleration when DC bus voltage approaches the trip point. This is the cleanest long-term solution when you can't simply extend the ramp time.

**On G120 / MM440:**
- Parameter **P1240** = 1 (enable Vdc max controller)
- This allows the drive to dynamically adjust the deceleration ramp in real time to keep DC bus voltage under the F0002 threshold.

### Step 4: Check incoming line voltage

Measure voltage at the drive input terminals with a true-RMS multimeter. Measure all three phases. For a 480V drive, input voltage should be 480V ±10% (432–528V). For a 230V drive: 230V ±10%.

If voltage is consistently high (above the upper limit), contact your utility. If voltage is within spec but you're seeing transient spikes, consider adding a line reactor or an input choke ahead of the drive.

### Step 5: Add a braking resistor (for high-inertia applications)

If extending the ramp and enabling the Vdc controller don't fully solve the problem — common with centrifuges, large fans at full speed, and applications with fast stop requirements — you need a **dynamic braking resistor (DBR)**. 

The braking resistor gives the regenerative energy somewhere to go (it dissipates as heat in the resistor). Most G120 and MM440 drives have a built-in braking transistor (chopper) — you just connect an appropriately sized external resistor to the DC bus terminals.

Resistor sizing depends on drive size and duty cycle. Siemens publishes braking resistor selection tables in the G120 and MM440 hardware installation manuals.

### Step 6: Reset the fault

After making parameter changes or hardware modifications:
1. Press the **OFF/Reset** button on the BOP (Basic Operator Panel), or send a reset command via your control system.
2. Restart the drive and test under load.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [Dynamic braking resistor (size-matched to drive)](https://www.amazon.com/s?ascsubtag=ecf-siemens-vfd-f0002-fault&k=Dynamic+braking+resistor+%28size-matched+to+drive%29&tag=errorcodefixes-20) | Dissipate regenerative energy — high inertia loads | $80–$400 |
| [Input line reactor (3–5% impedance)](https://www.amazon.com/s?ascsubtag=ecf-siemens-vfd-f0002-fault&k=Input+line+reactor+%283%E2%80%935%25+impedance%29&tag=errorcodefixes-20) | Protect against line transients causing F0002 | $100–$400 |
| [Siemens BOP-2 operator panel](https://www.amazon.com/s?ascsubtag=ecf-siemens-vfd-f0002-fault&k=Siemens+BOP-2+operator+panel&tag=errorcodefixes-20) | Access/change parameters if no panel present | $80–$150 |
| [Surge protection / MOV filter](https://www.amazon.com/s?ascsubtag=ecf-siemens-vfd-f0002-fault&k=Surge+protection+%2F+MOV+filter&tag=errorcodefixes-20) | Protect against utility voltage spikes | $50–$200 |
| [Replacement SINAMICS G120 Power Module](https://www.amazon.com/s?ascsubtag=ecf-siemens-vfd-f0002-fault&k=Replacement+SINAMICS+G120+Power+Module&tag=errorcodefixes-20) | Drive failure after repeated F0002 trips (rare) | $400–$2,000+ |

For braking resistors, Siemens part numbers follow the pattern **6SE6400-4BD...-...**. Match the resistance value and wattage to your drive's kW rating using the selection table in the G120 Hardware Installation Manual (available free at support.industry.siemens.com).

---

## When to Call a Pro

- **F0002 occurs on startup with no deceleration involved:** Incoming supply voltage is likely the issue. An electrician should measure and confirm line voltage before assuming the drive is at fault.
- **F0002 after extending ramp and enabling Vdc controller:** The application may need a braking resistor — sizing this correctly requires calculating load inertia and braking duty cycle.
- **Drive has a blown DC bus component:** If the drive also shows other faults (F0001 overcurrent, F0021 ground fault) alongside or following repeated F0002 events, the power electronics may be damaged. This requires a qualified drive technician.
- **G120 with Safety Integrated faults:** F0002 combined with safety-related alarms requires Siemens-qualified safety instrumented systems work — don't clear safety faults without understanding the safety interlock context.

---

## Frequently Asked Questions

**Q: What's the DC bus voltage threshold that triggers F0002 on Siemens drives?**

It depends on the drive's voltage rating:
- For 400V / 480V drives: approximately 810V DC
- For 230V drives: approximately 390V DC
These thresholds are hardware-fixed and cannot be adjusted. The fix is preventing the bus voltage from reaching those levels.

**Q: F0002 only happens when the drive stops. Is that always regeneration?**

Almost always, yes. When a drive decelerates a spinning motor, the motor's kinetic energy converts to electrical energy and flows back into the DC bus. If the bus can't absorb it (no braking resistor) and the ramp is fast, the bus voltage rises until F0002 trips. Slow the decel ramp or add a braking resistor.

**Q: What's the difference between F0002 and A0501 on Siemens SINAMICS?**

F0002 is a fault — the drive trips and stops. A0501 is an alarm (warning) that DC bus voltage is approaching the trip threshold. If you see A0501 repeatedly, take it seriously and address the root cause before it becomes F0002 trips.

**Q: Can I just increase the overvoltage trip level to prevent F0002?**

No. The F0002 trip threshold is a hardware protection level set by Siemens — it cannot be adjusted through parameters. The correct fix is keeping the DC bus voltage below the threshold through proper ramp configuration and/or braking resistors.

**Q: My G120 shows F0002 even with a very slow decel ramp. What's wrong?**

If F0002 occurs even with a 60-second or longer decel ramp, the incoming line voltage may be elevated. Measure L1-L2, L2-L3, and L1-L3 at the drive input. High line voltage means a high baseline DC bus voltage, leaving less headroom before F0002 trips. Also verify the Vdc max controller is enabled (P1240 = 1). If both are fine and F0002 persists, the drive's DC bus capacitors may be degraded — capacitors that have lost capacitance can't buffer voltage transients and the bus spikes more easily.

## Related Articles

- [Siemens Sinumerik 828D Alarm Codes Guide — Complete Diagnostic Reference](/posts/siemens-828d-alarm-codes/)
- [Siemens 840D Alarm 380000 — Causes & Fix](/posts/siemens-840d-alarm-380000/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)

## See Also

- [Siemens VFD Fault Codes — SINAMICS G120, V20, S120 Guide](/posts/siemens-vfd-fault-codes/)
- [Siemens SINAMICS G120 F30021 Fault — Ground Fault Fix](/posts/siemens-sinamics-f30021-fault/)
- [Siemens Desigo BMS Fault Codes - Complete Guide](/posts/siemens-desigo-fault-codes/)
- [Siemens SINAMICS G120 Fault F30021, Ground Fault Causes & Fix](/posts/siemens-sinamics-g120-fault-f30021/)
