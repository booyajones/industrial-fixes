---
title: "Schneider Altivar OSF Fault — Overspeed Fix"
description: "Schneider Altivar OSF (Overspeed Fault) means the drive's speed feedback (calculated from the back-EMF model in open-loop or from a real encoder in..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: schneider-altivar-fault-code-osf
featured: false
draft: false
tags:
  - schneider-electric
  - vfd
  - industrial-maintenance
  - drives
  - overspeed-fault
---
## Quick answer

Schneider Altivar OSF (Overspeed Fault) means the drive's speed feedback (calculated from the back-EMF model in open-loop or from a real encoder in closed-loop) exceeded the maximum speed setpoint (parameter 3.05) by more than the configured overspeed threshold (typically 10-15%). The single most common cause on closed-loop ATV340/930 systems is encoder feedback noise or wiring problems making the drive see speeds it isn't actually running, not an actual overspeed mechanical event. Read parameter 7.30 fault history before clearing — OSF disappears from real-time monitoring as soon as it trips.

## What OSF means on Schneider Altivar

OSF fires when the drive's speed measurement exceeds the configured limit. The configured limit is the value of parameter **3.05 (Max Frequency)** multiplied by the overspeed protection factor (parameter **6.05**, default 1.1 = 110%). On a typical 60 Hz application with 3.05 = 60.0 and 6.05 = 1.1, the drive trips OSF if measured frequency exceeds 66.0 Hz.

The drive measures speed in one of three ways depending on configuration:

1. **Open-loop induction motor (most common)**: speed is calculated from the back-EMF in the motor model — no physical encoder. The calculation uses the U-V-W terminal voltages and currents to estimate slip.
2. **Closed-loop induction motor**: speed is measured from a physical incremental or absolute encoder mounted to the motor shaft, connected to a feedback option card (VW3A3401, VW3A3402, etc.).
3. **Sensorless PMSM**: speed is calculated from the permanent-magnet motor's flux model. Higher accuracy than induction open-loop but still software-based.

OSF on open-loop systems often points to a parameter mismatch or motor model error. OSF on closed-loop systems often points to encoder hardware (noise, wiring) rather than actual motor overspeed.

The overspeed protection exists for two reasons: (a) mechanical safety — most loads have a maximum mechanical speed limit (centrifugal pumps cavitate, fans destroy bearings, conveyors throw material), and (b) drive protection — at speeds above the rated maximum, the back-EMF can exceed the drive's voltage capability, and braking might not work correctly.

## Common causes (ranked by frequency)

In Altivar OSF service:

1. **Encoder feedback noise (closed-loop systems)** — about 28%. Cable noise, ground loops, electromagnetic interference.
2. **Encoder cable damaged or connector loose** — about 18%.
3. **Wrong motor parameter (4.04 motor speed mismatch)** — about 15%. Drive expects motor at 1750 RPM but actual is 1800 — drive thinks motor is overspeed.
4. **Process condition (load drops suddenly, motor coasts up)** — about 10%. Pump discharge valve opens, conveyor empties out.
5. **Failed encoder** — about 8%.
6. **Brake circuit not engaging during deceleration** — about 7%. Regenerative energy speeds motor up briefly.
7. **Wrong overspeed protection factor (6.05 too tight)** — about 5%.
8. **Drive at end of life, internal feedback drift** — about 4%.
9. **Field weakening operation above base speed misconfigured** — about 3%.
10. **Wrong drive type for high-speed application** — about 2%.

**Pro nugget:** Encoder feedback on Altivar closed-loop systems requires **shielded cable with the shield bonded to ground at the drive end only** — single-ended grounding to prevent ground loops. The most common encoder fault that causes OSF in industrial environments is bonded shields at both ends (the motor end shield is connected through the conduit to building steel, and the drive end shield is bonded through the option card). This creates a ground loop that picks up noise from nearby VFDs or contactors, the noise rides on the encoder feedback signal, and the drive sees apparent speed spikes that trip OSF. **Field fix**: cut the shield connection at the motor end (use shrink tubing and electrical tape to keep it isolated), keep only the drive-end shield bonded. Verify with an oscilloscope on the A and B channels — should see clean square waves, not noisy.

## Step-by-step diagnosis

Before you start: lock and tag the disconnect for any work involving the drive output or encoder wiring.

1. **Read fault history (parameter 7.30) before clearing.** Note motor frequency at trip (typically 7.31), motor current at trip (7.32), and DC bus voltage at trip (7.33). Note the prior 3-5 faults.

2. **For closed-loop systems: inspect encoder cable.** Locate the encoder cable from motor to drive option card. Check for: chafing in cable carriers, melt damage near hot surfaces, connector seated correctly at both ends, shield drainwire connected at drive end only.

3. **Inspect the encoder itself.** Most Schneider closed-loop applications use a Heidenhain, Hengstler, or BEI encoder mounted to the motor non-drive end. Look for: physical damage to the encoder body, water ingress through the shaft seal, broken cable strain relief.

4. **Verify encoder configuration parameters.** Parameters under 10.00-10.20 configure the encoder type, PPR (pulses per revolution), direction, and feedback channel. Mismatched parameters cause the drive to calculate wrong RPM.

5. **For open-loop systems: verify motor nameplate parameters.** Parameters 4.01 (current), 4.02 (voltage), 4.03 (frequency), 4.04 (speed), 4.05 (power factor) must match the motor nameplate exactly. A motor parameterized at 1750 RPM but actually running at 1800 RPM appears as "overspeed" to the drive.

6. **Check parameter 3.05 (max frequency) and 6.05 (overspeed factor).** Default 6.05 is 1.1 (110%). For applications with deliberate overshoot during deceleration (high inertia loads with hard-decel programs), 6.05 may need to be 1.2 or 1.25.

7. **Run drive auto-tune (parameter 5.01).** With the motor connected and the load decoupled if possible, run auto-tune. This refreshes the motor model in the drive and corrects any drift in the estimated speed calculation.

8. **For brake circuit issues:** If you have a dynamic brake resistor, verify the brake chopper is enabled (parameter 7.40) and the resistor is wired correctly (BR+ and BR- terminals on the drive). Without the brake, regenerative energy can push speed up during deceleration.

9. **Set up SoMove trending.** If OSF is intermittent, trend the actual motor frequency (parameter 6.05) over time while running. Identify whether OSF happens during accel, decel, steady-state, or transient load events.

10. **Replace encoder if confirmed bad.** Bench-test encoders with an oscilloscope on A, B, Z channels. Should see clean square waves of equal amplitude with proper phase relationship.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Encoder option card (incremental TTL) | Schneider VW3A3401 | $385-485 | [AutomationDirect](https://www.automationdirect.com), [Galco](https://www.galco.com) |
| Encoder option card (sin/cos) | Schneider VW3A3402 | $545-685 | [Galco](https://www.galco.com), [AutomationDirect](https://www.automationdirect.com) |
| Encoder option card (EnDat absolute) | Schneider VW3A3404 | $685-845 | [Galco](https://www.galco.com) |
| Heidenhain ROD 426 incremental (1024 PPR) | Heidenhain 376857-04 | $785-985 | [Galco](https://www.galco.com), [Amazon](https://www.amazon.com) |
| BEI HS35 incremental (1024 PPR) | BEI HS35F-100-R2-SS-1024-ABZC-28V/V-EM18 | $385-485 | [Galco](https://www.galco.com), [AutomationDirect](https://www.automationdirect.com) |
| Encoder cable, shielded (per foot) | Belden 8451 | $5-10/ft | [AutomationDirect](https://www.automationdirect.com), [Amazon](https://www.amazon.com) |
| Dynamic brake resistor (10 ohm, 1.5kW) | Schneider VW3A7702 | $385-485 | [AutomationDirect](https://www.automationdirect.com), [Galco](https://www.galco.com) |
| Altivar ATV340 (closed loop, 7.5kW) | Schneider ATV340U75N4 | $2,400-3,200 | [Galco](https://www.galco.com), [AutomationDirect](https://www.automationdirect.com) |
| Oscilloscope (encoder waveform check) | Rigol DS1054Z | $385-485 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com) |

## When to call a controls engineer

Call senior controls support when:

- OSF only happens on specific motor speeds. Suggests a mechanical resonance interacting with the speed control loop — needs tuning by experienced engineer.
- The application is critical (web tension, synchronization, large fan) and you can't tolerate even brief overspeed events. Application-specific protection logic may need development.
- The drive is on a multi-axis line shaft or section control. Drive-to-drive synchronization configuration is complex.
- The motor is PMSM (permanent magnet synchronous). PM tuning is more sensitive than induction.

## FAQs

**My OSF only happens during fast deceleration. Why?**
Insufficient braking — when decel time is short, motor inertia keeps it spinning above setpoint briefly. Solution: increase decel time (parameter 3.20), or add dynamic brake resistor.

**Will increasing the overspeed factor (6.05) clear OSF?**
Temporarily, but it masks a real problem. If the drive is reporting 70 Hz on a 60 Hz application, something is wrong — find and fix it rather than raising the trip threshold.

**Can I run open-loop with a closed-loop drive (ATV340)?**
Yes — ATV340 supports both modes. Set parameter 5.00 to "Sensorless flux vector" instead of "Flux vector with feedback." But you lose the precision and torque control of closed-loop.

**Difference between OSF and SOF?**
OSF = overspeed (drive measured speed exceeded limit). SOF = speed feedback fault (drive can't read encoder at all). Different fault paths.

**My ATV320 doesn't have an encoder option. Why am I getting OSF?**
ATV320 is sensorless open-loop. OSF on ATV320 always points to motor model error — verify motor parameters and re-run auto-tune.

## Related guides

- [Schneider Altivar OCF Fault — Overcurrent Fix](/posts/schneider-altivar-fault-code-ocf)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
