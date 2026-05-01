---
title: "ABB ACS880 Fault 2310 - Overcurrent Diagnosis and Fix"
description: "Diagnose and fix the ABB ACS880 fault 2310 overcurrent fault. Covers motor overload, short circuit, acceleration ramp, and inverter module causes with step-by-step fixes."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The ABB ACS880 fault 2310 is an overcurrent fault — the drive has detected that the output current exceeded the instantaneous trip threshold. Unlike a sustained overload fault (like 2350), fault 2310 is a fast-acting protection that trips in microseconds when current spikes above a safe level. It protects both the motor and the drive's IGBT power modules from damage caused by a sudden high-current event.

This guide covers all causes of fault 2310 on the ACS880, how to distinguish between motor-side and drive-side causes, and the step-by-step procedure for restoring normal operation.

## What Does ACS880 Fault 2310 Mean?

Fault 2310 means the ACS880 measured a peak phase current exceeding the overcurrent trip limit. The ACS880 monitors output current on all three phases continuously. When any phase current exceeds approximately 3.5–4x the drive's rated current (depending on configuration), fault 2310 trips immediately.

The ACS880 stores a fault snapshot in its fault history (accessible via the ACS880 control panel or DriveStudio software), including:
- Fault timestamp
- Output frequency at fault
- Output current at fault
- DC bus voltage at fault
- Motor torque at fault

This data is critical for diagnosis — look at it before changing any parameters.

**Related faults to distinguish from 2310:**

| Fault | Meaning |
|-------|---------|
| 2310 | Overcurrent (instantaneous trip) |
| 2330 | Earth (ground) fault |
| 2340 | Short circuit |
| 2350 | Overcurrent (thermal overload) |
| 3210 | DC overvoltage |
| 3220 | DC undervoltage |

### Common Causes

The most common causes of ACS880 fault 2310 are:

1. **Acceleration ramp too aggressive** — the motor can't accelerate fast enough; current spikes during ramp
2. **Short circuit on output cables or motor windings** — phase-to-phase or phase-to-ground short
3. **Motor bearings seized or mechanical jam** — load suddenly demands more torque than the drive can provide without spiking current
4. **Incorrect motor parameters** — motor nominal values programmed incorrectly lead to poor current regulation
5. **Drive IGBT module failure** — internal fault in the power electronics
6. **Cable length too long without output reactor** — long output cables create distributed capacitance that causes capacitive charging current spikes during switching

## How to Fix It

**Step 1: Check the Fault Snapshot**

Before touching anything, read the fault snapshot from the ACS880:
- Panel: Fault > History > View latest fault data
- DriveStudio: Diagnostics > Fault Logger

Key values to record:
- **Output current at fault:** If it's near 3.5x drive rated current, you have a true overcurrent event. If it's only slightly above rated current, the overcurrent detection threshold may be set too low.
- **Output frequency at fault:** If fault 2310 always trips at a specific frequency (e.g., near line frequency), suspect resonance or a motor issue at that speed.
- **Fault timestamp pattern:** Random/single trip suggests transient cause; repeated trips suggest persistent cause.

**Step 2: Check Motor and Output Cable Insulation**

With the drive powered OFF and locked out:
- Disconnect the output cables at the drive output terminals (U2, V2, W2) and at the motor terminal box.
- Use a megohmmeter (insulation resistance tester) to measure resistance between each output phase and PE (ground):
  - Phase U to PE
  - Phase V to PE
  - Phase W to PE
  - Phase U to Phase V
  - Phase U to Phase W
  - Phase V to Phase W
- At 500V DC test voltage: readings should be >1 MΩ (ideally >100 MΩ for a good motor and cable).
- Readings below 1 MΩ indicate insulation breakdown — damaged cable or failed motor winding. Replace the affected cable or motor.

**Step 3: Check Motor Shaft for Mechanical Jam**

With power OFF, attempt to rotate the motor shaft by hand. It should rotate smoothly with resistance appropriate for the load. If it's locked or very stiff:
- Disconnect the motor from the load (coupling, gearbox) and test the motor shaft alone.
- If the motor shaft is free but the load is jammed, clear the mechanical obstruction.
- If the motor shaft itself won't turn, the motor bearings have failed.

A seized load or failed motor bearing causes an instantaneous torque demand spike on startup that exceeds 2310's trip threshold.

**Step 4: Adjust Acceleration Ramp Time**

If the motor and cables are healthy, the most common cause of ACS880 fault 2310 is an acceleration ramp time that's too short for the driven load.

- Navigate to parameter group 23 (Speed Reference Ramp) or 28 (Frequency Reference Chain) in the ACS880 parameter tree.
- Find parameter **23.12 Acceleration time 1** (or the active acceleration time parameter for your application macro).
- Increase the acceleration time. Start by doubling the current value (e.g., 5 seconds → 10 seconds).
- Test: restart the drive and observe if it completes acceleration without faulting.

For high-inertia loads (large fans, centrifuges, large pumps), acceleration times of 30–120 seconds are common. Don't use a 5-second ramp on a 50,000 kg-cm² inertia load.

**Step 5: Verify Motor Nameplate Parameters**

The ACS880 uses motor nominal parameters to calculate current limits and control gains. If these are entered incorrectly, the drive's current regulator is tuned for the wrong motor and may generate current spikes.

Check parameter group 99 (Motor Data) against the motor nameplate:
- 99.04 Motor nominal voltage (V)
- 99.05 Motor nominal frequency (Hz)
- 99.06 Motor nominal speed (RPM)
- 99.07 Motor nominal current (A)
- 99.08 Motor nominal power (kW or HP)
- 99.09 Motor nominal power factor (cos φ)

Correct any discrepancies. After changing motor data, re-run the motor ID run (parameter 99.13).

**Step 6: Check for Long Cable Effects**

Output cable runs longer than 100 meters (roughly 330 feet) can cause capacitive charging current spikes during IGBT switching transitions. These spikes appear as overcurrent events to the drive's protection circuitry.

- If cable length exceeds 50–100 meters, install a du/dt output reactor or sine wave filter at the drive output.
- Check ABB ACS880 hardware manual for maximum cable length specifications for your drive frame size.

**Step 7: Check IGBT Gate Driver / Power Module**

If fault 2310 occurs immediately at power-on before any output, or occurs randomly with no load, the drive's internal IGBT power module may have failed.

- Check the drive's fault history for other concurrent faults: 5210 (Gate Drive), 5250 (IGBT overcurrent), 7121 (Control Unit Supply).
- Inspect the drive's cooling fins and fans — overheated IGBTs fail prematurely. Clean any dust from the cooling fins.
- IGBT power module failure in the ACS880 requires professional service by an ABB-certified technician or repair center.

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| Megohmmeter / Insulation Resistance Tester | Test motor winding and cable insulation | [View on Amazon](https://www.amazon.com/s?k=megohmmeter+insulation+resistance+tester+500V&tag=errorcodefixes-20) |
| True RMS Clamp Meter | Measure output current during drive operation | [View on Amazon](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20) |
| ABB du/dt Output Reactor | Protect against long cable capacitive current spikes | [View on Amazon](https://www.amazon.com/s?k=ABB+VFD+output+reactor+du+dt&tag=errorcodefixes-20) |
| Motor Shaft Coupling (flexible) | Replace coupling if mechanical transmission is causing jam | [View on Amazon](https://www.amazon.com/s?k=flexible+motor+shaft+coupling&tag=errorcodefixes-20) |

## When to Call a Pro

- **Fault 2310 with concurrent fault 5250 (IGBT overcurrent):** The drive's power module has likely failed. Contact ABB service or a certified VFD repair shop.
- **Insulation resistance below 1 MΩ on motor or cables:** Requires cable replacement or motor rewind/replacement.
- **Mechanical seizure at the motor or load:** Major mechanical repairs require qualified personnel.
- **Fault 2310 on a new drive installation:** If the drive is new and faulting from day one, the system commissioning may have errors — get the commissioning engineer back on-site.

## FAQ

**Q: The ACS880 faults on 2310 only when starting under load at low frequency. What's wrong?**

A: This is a classic sign of an acceleration ramp that's too fast combined with a high starting torque demand. In the fault snapshot, if current is near trip level and frequency is 1–10 Hz, increase the acceleration time or enable the ACS880's speed controller anti-windup function. Also verify that the current limit parameters (30.17 Maximum current) are set appropriately for your motor.

**Q: ACS880 fault 2310 trips randomly during normal operation, not at startup. What causes random overcurrent?**

A: Random fault 2310 during running (not startup) suggests: (1) intermittent mechanical jam or load spike (conveyor, mixer with lumpy material), (2) intermittent insulation failure on output cable (fault worsens with cable temperature), (3) loose output terminal connection causing arcing. Check mechanical load behavior, retest insulation when the cable is warm, and retorque all output terminal connections.

**Q: Can I increase the overcurrent trip threshold on the ACS880 to prevent nuisance trips?**

A: The instantaneous overcurrent trip (2310) threshold is fixed in firmware and is not user-adjustable — it's a hardware protection. What you can adjust is the current limit (parameter 30.17) which limits how much current the drive will command. Lower current limit = less chance of tripping 2310 on demand spikes, but also less torque capability. Do not attempt to defeat 2310 protection — it exists to prevent IGBT destruction.

**Q: How do I reset fault 2310 on the ACS880?**

A: After addressing the root cause, press the RESET button on the ACS880 control panel, or send a reset command via fieldbus (bit 7 of the Control Word). The fault clears and the drive is ready to start. If the fault reappears immediately on start attempt, the root cause has not been resolved.
