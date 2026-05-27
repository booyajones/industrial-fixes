---
title: "Siemens SINAMICS G120 F30001 Fault — Power Module Overcurrent Fix"
description: "Siemens SINAMICS G120 F30001 (Power Module Overcurrent) means the hardware-level overcurrent comparator inside the Power Module fired before the firmware's..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: siemens-sinamics-f30001-fault
featured: false
draft: false
tags:
  - siemens
  - vfd
  - industrial-maintenance
  - drives
  - power-module-overcurrent
---
## Quick answer

Siemens SINAMICS G120 F30001 (Power Module Overcurrent) means the hardware-level overcurrent comparator inside the Power Module fired before the firmware's current-limit logic could throttle output — peak phase current exceeded approximately 2.0× the Power Module's rated short-time current for more than a few microseconds. In the field this is almost always a load-side problem: shorted motor lead, stalled motor under a load step, or an output-side ground fault. The drive itself is rarely the failure point on F30001.

## What F30001 means

The G120 (and the closely related G110, G130, and S120 platforms) splits the drive into a Control Unit (CU240E-2 PN, CU250S-2, etc.) and a Power Module (PM240-2, PM250, PM340). The Power Module has its own current-sensing Hall transducers on each output phase feeding both the firmware's current regulator and an independent hardware comparator. The hardware comparator's trip point is set in factory firmware to roughly 200% of Power Module rated current. When any phase exceeds that for the debounce window (typically 2–8 µs depending on Power Module size), the comparator commands an immediate IGBT shutdown and the firmware logs F30001.

This is a Power Module-side fault, not a Control Unit-side fault. The Control Unit's regulator wasn't fast enough to prevent it, and that's by design — the hardware protection is the last line of defense before IGBT failure. F30001 is the "fast" overcurrent; the slower regulator-managed overcurrents throw F07900 series codes instead.

The fault code F30001 is consistent across SINAMICS platforms. On the G120 you read it via the BOP-2 basic operator panel, the IOP-2 intelligent operator panel, or through STARTER/Startdrive/TIA Portal connected via PROFINET. On S120 systems with multi-axis configurations, F30001 includes a drive object (DO) identifier indicating which axis tripped.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from chasing parts. **Do not clear the fault before you read the history.** Siemens stores a richer fault history than many drive platforms, but only if you read it before clearing.

Open STARTER (legacy) or TIA Portal with Startdrive (current). Connect to the drive via PROFINET or USB. Navigate to the drive object → Diagnostics → Faults and alarms. The history shows up to 64 entries on a G120 CU240E-2.

For each F30001 entry record:

- **r0945 (FaultNumber)** — the fault code itself, 8 entries indexed 0–7
- **r0947 (FaultNumberOlder)** — older fault buffer
- **r0948 (FaultTime)** — timestamp at trip (seconds since drive boot or RTC if equipped)
- **r0949 (FaultValue)** — supplemental fault value, on F30001 this encodes which phase tripped
- **r2122 (Alarm history)** — pre-fault alarm sequence, often shows current-limit alarms before the trip

On a BOP-2 keypad you can navigate parameter r0945 directly. Push the **Fn** key, select **Fault and Alarm Memory**, scroll through.

**Field insight on F30001:** the r0949 value tells you which phase tripped. A consistent r0949 value across multiple events means the fault is on a specific phase — chase that phase's wiring and motor connection. A randomly varying r0949 means the fault is symmetric across phases — usually a stall, a load step, or a configuration problem. Pull r0949 every time.

## Common causes (ranked by frequency)

1. **Motor stall under sudden load** — pump suddenly sucks debris, conveyor hits a jam, grinder bites into oversized material. Current spikes faster than the firmware regulator can drop output frequency.
2. **Phase-to-phase short in motor leads** — chafed cable, water in the J-box, shorted disconnect downstream of the drive.
3. **Phase-to-ground fault on output** — motor winding insulation failure to frame, water in motor, damaged cable to ground.
4. **Acceleration ramp too aggressive** — **p1120 Ramp-up time** set too short for the load inertia. Drive tries to accelerate faster than the motor can develop torque without saturating, hits current limit, then trips F30001.
5. **Motor parameters mismatched** — wrong motor rated current in p305, wrong nameplate frequency in p310, wrong stator resistance in p350. Drive's torque control is fighting the actual motor characteristics.
6. **Power Module undersized for the application** — drive is one frame size too small for actual motor inrush demands during high-inertia starts.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time (minimum 5 minutes for G120 PM240-2 frames, longer for larger Power Modules), and verify zero DC link energy at the DC link terminals. The G120 DC link voltage is in the 540–680 VDC range during operation and discharges slowly.

1. **Read r0945, r0947, r0949 before clearing.** Capture all values. Note the phase indicated by r0949 — this drives your inspection.

2. **Megger the motor and output cable.** Disconnect U2, V2, W2 from the Power Module output. Use a 500V megohmmeter (1000V if rated). Test U-V, V-W, U-W, and each phase to ground. Healthy: above 100 MΩ at 25°C. Below 1 MΩ phase-to-phase = your fault. Below 1 MΩ phase-to-ground = ground fault.

3. **Walk the cable run.** With leads disconnected, inspect every conduit body, every cable tray transition, every strain relief. F30001 is overwhelmingly cable-side or motor-side in origin.

4. **Verify the motor matches drive configuration.** In STARTER/Startdrive, open the drive's motor configuration page. Confirm: **p304 Motor rated voltage**, **p305 Motor rated current**, **p307 Motor rated power**, **p308 Motor rated cos φ**, **p310 Motor rated frequency**, **p311 Motor rated speed** all match the motor nameplate. A drive parameterized for a 5kW motor driving a 7.5kW motor will hit current limit and trip F30001 on every start.

5. **Run motor data identification.** With motor connected and the system safe to spin slowly, command **p1910 = 1** (motor identification at standstill). The drive injects test signals, measures stator resistance, leakage inductance, and main inductance. This calibrates the torque controller to the actual motor. Without identification, the regulator can miscalculate during accel and trip F30001.

6. **Check ramp times.** **p1120 Ramp-up time** and **p1121 Ramp-down time** must allow the load inertia to follow the speed reference without exceeding the drive's current limit. Start with values 2–3× longer than your target and reduce until you hit comfortable acceleration. For high-inertia loads (large fans, centrifuges), p1120 of 30–60 seconds is normal.

7. **Verify current limit and torque limit parameters.** **p640 Current limit** sets the peak current limit, usually 150–200% of motor rated current. If a user dropped this below motor inrush requirements, F30001 will trip during normal starts. Default is 1.5× p305.

8. **Inspect the Power Module externally.** Look for: visible damage at output terminals, scorch marks at the DC link bus, swollen capacitors visible through air-intake louvers, contamination on the heatsink. A failed Power Module sometimes shows visible damage; an internal IGBT failure may not.

> **Field knowledge nugget:** On SINAMICS G120 systems with PM240-2 Power Modules driving submersible pumps or motors in high-humidity environments — wastewater pump stations, food-processing washdown areas — F30001 trips that happen specifically after a wet-weather event or after a CIP cycle are almost always motor winding moisture intrusion, not a drive problem. The motor insulation hasn't fully failed, but moisture provides a partial phase-to-ground path that pulls current sharply during the PWM voltage steps. Megger results may show 5–20 MΩ — not zero, but well below healthy. The fix is to dry the motor (a 24-hour bake at low voltage with the rotor locked, or a proper oven dry), then re-megger. On a submersible pump at a Riverside CA wastewater plant I dried six pumps over a weekend; all six came back to >500 MΩ and no F30001 in the following two years. Drying is cheaper than a new motor — try it before condemning.

## Parts that may need replacement

SINAMICS G120 Power Modules and Control Units are sold separately. Identify your part numbers from the drive nameplate (PM240-2 6SL3210-1PE21-8UL0 format).

| Part | Order Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PM240-2 Power Module, 7.5kW, 400V | 6SL3210-1PE22-8UL0 | $1,200–$1,600 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault) |
| PM240-2 Power Module, 15kW, 400V | 6SL3210-1PE24-5UL0 | $1,900–$2,400 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault), [Wolf Automation](https://www.wolfautomation.com) |
| CU240E-2 PN Control Unit | 6SL3244-0BB12-1PA1 | $480–$640 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault) |
| BOP-2 Basic Operator Panel | 6SL3255-0AA00-4CA1 | $185–$245 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault) |
| IOP-2 Intelligent Operator Panel | 6SL3255-0AA00-4JA2 | $480–$620 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault) |
| Output choke (3.5%, frame FSC) | 6SL3203-0CD22-2AA0 | $380–$520 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault) |
| dV/dt filter for long motor cables | 6SL3000-2DE38-4AA0 | $1,400–$1,900 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30001-fault), [Wolf Automation](https://www.wolfautomation.com) |

## When to call Siemens or a controls engineer

Call senior support when: F30001 recurs after motor and cable have been verified good via megger and motor data identification has been run successfully; the drive is a multi-axis S120 in a coordinated motion application (synchronization issues can produce F30001 on one axis); you need to update Power Module firmware to support a newer motor identification routine; or when F30001 only appears under specific process conditions you cannot reproduce on a service call.

## FAQs

**What does F30002 mean compared to F30001?** F30002 is DC Link Overvoltage — bus voltage exceeded its trip threshold, typically from regenerative braking energy or a line transient. F30001 is the AC-side overcurrent on the output. Different protections, different physical phenomena. They occasionally appear together when a bad decel triggers overvoltage that then collapses to an overcurrent on the next accel attempt.

**Can I disable the current limit to get past F30001?** No, and Siemens does not allow it. p640 has a minimum value tied to Power Module rating; the hardware comparator is not user-adjustable on any SINAMICS platform. The fault is hardware protection. Bypassing it means destroyed IGBTs.

**Why does motor identification matter so much?** Siemens drives use sensorless vector control by default on G120, which requires accurate knowledge of motor electrical parameters (stator resistance, leakage inductance, main inductance) to estimate flux and torque. Without identification, the regulator's internal model diverges from reality and current control becomes sloppy. Sloppy current control + a load step = F30001.

**My drive was working fine, threw F30001 once, cleared, runs fine now. Should I worry?** Maybe. Pull r0949 and look at what phase tripped. Single isolated F30001s can be one-shot events from a momentary load condition. But three F30001s in a week with consistent r0949 values means you have a real fault developing. Don't ignore it.

**What's the difference between F30001 on G120 and F30001 on S120?** Same code, same root logic, but S120 systems have more granular diagnostics through the Control Unit (CU320-2 PN) and richer trace data via STARTER. On S120, also check r0050 (faults present) and the trace buffer for current and voltage waveforms at the time of trip. The S120's diagnostic depth is one of its main advantages over G120.

## Related guides

- [Siemens SINAMICS F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault)
- [Siemens SINAMICS F30003 Fault — DC Link Undervoltage Fix](/posts/siemens-sinamics-f30003-fault)
- [Siemens SINAMICS F30021 Fault — Ground Fault Fix](/posts/siemens-sinamics-f30021-fault)

## See Also

- [Siemens Sinumerik Alarm 25201 — Causes & Fix](/posts/siemens-sinumerik-alarm-25201/)
- [Siemens Sinumerik Alarm 380500 — Causes & Fix](/posts/siemens-sinumerik-alarm-380500/)
- [Siemens SINAMICS G120 F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault/)
- [Siemens SINAMICS G120 Fault F30021, Ground Fault Causes & Fix](/posts/siemens-sinamics-g120-fault-f30021/)
