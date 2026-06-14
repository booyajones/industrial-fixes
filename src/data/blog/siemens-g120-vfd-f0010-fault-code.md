---
title: "Siemens G120 F0010 Fault Code - Causes & Fix"
description: "Siemens G120 F0010 indicates a motor load short circuit or output fault. Most often caused by damaged motor cable or winding insulation."
pubDatetime: 2026-06-02T10:29:50Z
modDatetime: 2026-06-02T10:29:50Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Motor cable (shielded VFD-rated)"
most_likely_cause: "Motor winding short circuit"
---

## Siemens G120 F0010 Fault Code — What It Means

The F0010 fault code on a Siemens SINAMICS G120 variable frequency drive indicates a load short circuit or short-circuit-related condition on the drive output. This is a protective trip triggered when the drive detects a phase-to-phase short, phase-to-ground short, or other output-stage fault condition. The exact fault definition can vary slightly across G120 firmware families, so consult your specific drive manual for the precise mapping, but the indexed fault lists consistently associate this code with motor circuit short faults and earth faults rather than communication or control issues.

The drive shuts down to protect its power electronics from damage when it senses current flow outside normal motor load patterns. The fault may originate in the motor windings, the motor cable, the termination points, or in rare cases the drive's own output stage. Diagnosis requires isolating each component to determine whether the short is external (motor or cable) or internal to the drive hardware.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding short circuit** Insulation failure inside the motor creates a phase-to-phase or phase-to-ground short that the drive detects as a fault.
- **Damaged motor cable** Crushed, pinched, or degraded cable insulation allows current to leak between phases or to ground before reaching the motor.
- **Ground fault in motor or cable** Moisture ingress, contamination, or damaged insulation creates a path to ground that trips the drive's earth-fault protection.
- **Loose or corroded terminations** Poor connections at the drive output terminals or motor junction box can arc and create intermittent short-circuit conditions.
- **Incorrect motor data or sizing mismatch** Drive parameters that do not match the motor nameplate can cause the drive to misinterpret normal current draw as a fault condition.
- **Drive output stage failure** Internal damage to the IGBT power module or output electronics causes the drive to detect a fault even with the motor disconnected.

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and motor, lockout/tagout the supply, and wait for DC bus capacitors to discharge per the drive manual before any hands-on work.
2. **Visually inspect** the motor cable and motor junction box for burn marks, damaged insulation, moisture, contamination, or loose termination hardware.
3. **Disconnect the motor leads** from the drive output terminals (U, V, W) and test the motor cable for insulation resistance using a megohmmeter, checking phase-to-phase and phase-to-ground, and compare results to acceptable limits in your motor documentation.
4. **Test the motor windings** separately with the cable disconnected, checking for continuity between phases and measuring insulation resistance to ground to isolate motor internal faults.
5. **Inspect and re-torque** all termination points at the drive, cable junctions, and motor box, replacing any damaged lugs or connectors found during inspection.
6. **Verify motor nameplate data** matches the drive parameter settings for rated voltage, current, frequency, and motor type, and correct any mismatches in the drive parameter list.
7. **Restore power with the motor still disconnected** and attempt to clear the fault. If F0010 persists without a motor connected, the drive output stage is likely damaged and the drive requires service or replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0010-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation testing shows phase-to-phase or phase-to-ground leakage; use VFD-rated cable with proper shield grounding. |
| Motor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0010-fault-code&k=Motor+assembly&tag=errorcodefixes-20) \| Required if winding insulation has failed and resistance testing confirms internal short or ground fault. |
| Drive power module (IGBT section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0010-fault-code&k=Drive+power+module+%28IGBT+section%29&tag=errorcodefixes-20) \| Needed if the fault persists with motor disconnected, indicating internal drive output-stage failure. |
| Terminal lugs and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0010-fault-code&k=Terminal+lugs+and+connectors&tag=errorcodefixes-20) \| Replace any that show arcing, corrosion, or overheating damage at the drive or motor termination points. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage DC bus safety, if insulation testing reveals failures you cannot locate visually, or if the fault remains after disconnecting the motor (indicating internal drive damage). Drive output-stage repair or power-module replacement requires specialized knowledge of IGBT handling, firmware configuration, and safe work on energized industrial equipment. A technician with Siemens drive experience can also verify correct motor parameterization and perform load testing to confirm the repair before returning the system to production.

## See Also

- [Siemens SINAMICS G120 Fault F30021, Ground Fault Causes & Fix](/posts/siemens-sinamics-g120-fault-f30021/)
- [Siemens SINAMICS G120 F30003 Fault — DC Link Undervoltage Fix](/posts/siemens-sinamics-f30003-fault/)
- [Siemens Micromaster F0035 - Causes & Fix](/posts/siemens-micromaster-vfd-f0035-fault-code/)
- [Siemens Micromaster F0101 - Causes & Fix](/posts/siemens-micromaster-f0101-fault-code/)
