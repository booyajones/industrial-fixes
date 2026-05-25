---
title: "Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-24T21:00:00Z
modDatetime: 2026-04-24T21:00:00Z
slug: yaskawa-a1000-oc-fault-code
featured: false
draft: false
tags:
  - yaskawa
  - vfd
  - industrial
  - overcurrent
  - fault-codes
description: "Yaskawa A1000 OC fault code means overcurrent — the drive detected output current exceeding 200% of rated current. Here's how to diagnose the motor, load, and drive parameters causing it."
---

## Error Code: Yaskawa A1000 OC (Overcurrent)

**What it means:** The OC fault on the Yaskawa A1000 variable frequency drive indicates the output current exceeded 200% of the drive's rated current. The A1000's hardware current sensors detected a current surge large enough to require immediate shutdown to protect both the drive's IGBT output transistors and the connected motor. OC is distinct from OL1 (motor overload, sustained high current) and OL2 (drive overload) — OC is an instantaneous peak current trip, not a thermal event.

The A1000 is Yaskawa's premium industrial VFD, used in demanding applications including pumps, fans, compressors, conveyors, hoists, and HVAC systems. Drives range from fractional HP to several hundred HP. The OC fault is one of the most common faults on any VFD and is often resolvable through parameter adjustment or mechanical inspection.

## When the OC Fault Occurs

The A1000 differentiates between:

- **OC during acceleration** — The most common scenario. Current spikes as the drive ramps motor frequency. Usually caused by too-fast acceleration time (C1-01), excessive load inertia, or a motor winding problem.
- **OC during constant speed** — Indicates a sudden load change or mechanical shock. Check for binding, jamming, or load impact events in the driven equipment.
- **OC during deceleration** — The motor is regenerating into the drive faster than the drive can handle. Increase deceleration time (C1-02) or add a dynamic braking resistor.
- **OC at start** — Immediate trip at the moment the drive outputs power. Strong indicator of a shorted motor winding or output short circuit.

## Common Causes

- **Acceleration ramp too fast** — Parameter C1-01 (acceleration time) set too short for the load's inertia. The motor tries to accelerate faster than the current limit allows, causing a current spike.
- **Motor winding fault** — Shorted turns in the motor winding create an extremely low impedance path, producing high current even at low voltage. A megohm test and winding resistance check will confirm.
- **Output wiring fault** — A short circuit between two output phases (U, V, W terminals), or phase-to-ground fault on the motor cable. The A1000 trips OC within microseconds of detecting this.
- **Load jam or mechanical lockup** — If the driven equipment suddenly seizes (pump cavitation, conveyor jam, etc.), the motor draws locked-rotor current, tripping OC.
- **Drive output IGBT failure** — A failed IGBT module in the output stage can cause OC at startup or intermittently. This is a drive hardware failure requiring service or replacement.
- **Motor too small for load** — The motor's service factor is exceeded by the actual load torque, resulting in continuous high current that eventually peaks above the OC threshold.
- **Incorrect motor parameters** — If E2-01 (motor rated current) is set too high, the drive's current limit function doesn't activate soon enough to prevent an OC trip.

## Step-by-Step Fix {#step-by-step-fix}

1. **Record when the OC occurs.** Press the ENTER key to clear the fault (or power cycle). Watch the drive display — does OC trip immediately at power application, during acceleration, at a specific speed, or under load? This timing is the most important diagnostic clue.

2. **Check the fault history.** Navigate to U2-01 (last fault) through U2-10 (fault history) in the monitor parameter group. Review the output current value at the time of fault (U2-06) — this tells you if you're seeing a true overcurrent event or a nuisance trip near the threshold.

3. **Increase acceleration time if OC occurs during ramp-up.** Navigate to C1-01 (accel time 1). Double the current value and retry. If the fault clears, the original ramp was too aggressive for the load inertia. Find the minimum stable accel time through trial and increase it 20–30% beyond that for margin.

4. **Verify motor parameters.** Check E2-01 (motor rated current) against the motor nameplate full-load amps. An incorrect E2-01 can cause the drive to allow too much current before protecting the motor. For vector control modes (CLV, OLV), also verify E2-04 (motor rated RPM) and E2-05 (motor pole count).

5. **Test the motor and output wiring for faults.** Disconnect the motor cable at the A1000 output terminals (U, V, W). With a 500V or 1000V megohm tester:
   - Test each phase (U, V, W) to ground — should read >1 MΩ (ideally >100 MΩ on a healthy motor)
   - Test each phase to the other phases — should read >1 MΩ
   - Readings below 1 MΩ indicate winding insulation breakdown; below 100 kΩ = motor needs replacement
   
   If megohm tests pass, measure winding resistance with a precision ohmmeter between U-V, V-W, and W-U. All three readings should be equal within ±5%.

6. **Inspect for mechanical jams.** Disconnect the motor from the driven load. If you can rotate the motor shaft freely by hand but not under load, the problem is in the driven equipment. Inspect for jams, seized bearings, or foreign material.

7. **Check for output transistor failure.** With the drive de-energized and motor disconnected, use a multimeter in diode test mode to check the output IGBT modules. Test from each output phase (U, V, W) to the DC bus positive and negative. A failed IGBT often shows a low forward voltage or zero resistance in one direction. This test requires familiarity with power electronics — consult Yaskawa's A1000 technical manual for the specific test procedure.

8. **Review torque boost and current limit settings.** Parameter C6-01 (torque boost) and L3-02 (stall prevention current level during acceleration). Excessive torque boost for the application can push starting current above OC threshold. Reduce C6-01 toward 0% and increase L3-02 if currently set too low.

## Parts Often Needed {#parts-often-needed}

| Part | Part Number | Typical Cost | Where to Buy |
|------|-------------|--------------|--------------|
| IGBT output module (drive-size dependent) | Varies by HP | $200–$800 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-oc-fault-code&k=Yaskawa+A1000+IGBT+module+replacement&tag=errorcodefixes-20) \| Yaskawa distributor |
| Control board (if parameter corruption) | ETC615018-S3xxx | $350–$600 | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-yaskawa-a1000-oc-fault-code&tag=errorcodefixes-20) \| Yaskawa distributor |
| Dynamic braking resistor (for OC on decel) | ERF150W series | $80–$300 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-oc-fault-code&k=Yaskawa+A1000+braking+resistor&tag=errorcodefixes-20) \| Automation supply |
| Output choke/line reactor | LR3020-MH series | $80–$200 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-oc-fault-code&k=Yaskawa+output+line+reactor+3-phase&tag=errorcodefixes-20) \| Automation supply |

## When to Call a Professional

If OC persists after adjusting acceleration time and confirming motor winding integrity, the issue is likely in the drive's output stage or requires sophisticated parameter tuning for the application. Yaskawa A1000 drives are complex — improper parameter changes can damage the motor or drive, or create safety hazards in industrial equipment. A Yaskawa-certified service technician or authorized distributor can connect a laptop with DriveWizard Plus software to capture real-time waveforms and diagnose the root cause of persistent OC faults.

> **Pro tip:** On Yaskawa A1000 drives, the OC protection threshold can be temporarily adjusted using L3-06 (stall prevention limit during acceleration). Setting this to a higher value (e.g., 180% instead of 150%) allows the drive to push through brief current spikes during acceleration without tripping — useful for high-inertia loads like fans and centrifuges. However, increasing this value increases stress on the IGBT modules and motor insulation, so use conservatively and only when the application genuinely requires it.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
- [Yaskawa Sigma-7 SGD7S Servo Drive Alarm Codes — Diagnosis & Fix](/posts/yaskawa-sigma7-sgd7s-alarm-codes/)

## See Also

- [Yaskawa VFD Fault GF — Causes & Fix](/posts/yaskawa-vfd-fault-gf/)
- [Yaskawa VFD Fault BB — Causes & Fix](/posts/yaskawa-vfd-fault-bb/)
- [Yaskawa VFD Fault CF — Causes & Fix](/posts/yaskawa-vfd-fault-cf/)
- [Yaskawa A1000 Complete Guide - Fault Codes, Parameters, and Commissioning](/posts/yaskawa-a1000-complete-guide/)
