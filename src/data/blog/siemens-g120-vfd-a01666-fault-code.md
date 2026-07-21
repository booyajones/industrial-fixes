---
title: "Siemens G120 VFD A01666 Fault - Causes & Fix"
description: "A01666 indicates an encoder or feedback signal issue on the Siemens G120 drive. Most often caused by wiring faults or encoder failure."
pubDatetime: 2026-07-19T07:35:09Z
modDatetime: 2026-07-19T07:35:09Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Incremental rotary encoder"
most_likely_cause: "Encoder cable fault or loose connection"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect encoder cable for physical damage, pinched insulation, or loose connectors at both the motor and drive ends"
  - "Check that encoder cable shields are properly grounded at one end only and not forming a ground loop"
  - "Review parameter settings in the drive to confirm encoder type, pulses per revolution, and signal polarity match the installed encoder"
part_price: "$150-400"
---

## Siemens G120 VFD A01666 Fault — What It Means

The A01666 fault on a Siemens G120 variable frequency drive signals a problem with the motor encoder or feedback system. This alarm typically appears when the drive cannot receive or interpret position or speed feedback from the encoder, which the system needs for accurate motor control in closed-loop applications. The fault can stem from wiring issues, encoder hardware failure, incorrect parameter settings, or signal interference.

Because the G120 relies on encoder feedback for precise speed and torque control, loss of this signal will prevent normal operation and trigger a protective shutdown. The fault requires systematic troubleshooting of the encoder circuit, beginning with the physical connections and moving through the encoder itself and the drive's input circuitry.

## Before You Replace Anything

Technicians sometimes replace the encoder itself when the real issue is a damaged or improperly shielded encoder cable. Always inspect and test the cable continuity and shielding first, and verify the connector pinout matches the drive's terminal assignments.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose encoder cable (~40%)** Breaks in the encoder cable conductors, poor connections at terminals, or damaged insulation allow signal loss or noise ingress that corrupts feedback.
- **Failed encoder (~25%)** The rotary encoder itself can fail due to bearing wear, moisture ingress, or electronic component failure inside the encoder housing.
- **Incorrect parameter configuration (~15%)** Mismatched encoder type settings, wrong pulses-per-revolution value, or inverted signal polarity in the drive parameters prevent proper signal interpretation.
- **Electromagnetic interference (~10%)** Routing encoder cables near high-current motor cables or lack of proper shielding introduces noise that the drive reads as a signal fault.
- **Drive encoder input card failure (~7%)** The input circuitry on the drive's encoder interface card can fail, preventing it from processing even a valid encoder signal.
- **Supply voltage to encoder out of range (~3%)** If the drive supplies power to the encoder, low or unstable voltage can cause erratic encoder output or complete signal loss.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the encoder cable show any visible damage, kinks, or loose connectors?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace or repair the encoder cable and retest the drive.<br><strong>No:</strong> Proceed to measure continuity and insulation resistance of the encoder cable with a multimeter.</div>
</details>

<details class="dtree"><summary>Do the drive parameters for encoder type and pulses per revolution match the encoder nameplate?</summary>
<div class="dtree-body"><strong>Yes:</strong> Move on to testing the encoder signal directly with an oscilloscope or the drive's diagnostic display.<br><strong>No:</strong> Correct the parameter settings to match the installed encoder specifications and clear the fault.</div>
</details>

<details class="dtree"><summary>Can you measure encoder output pulses with an oscilloscope while manually rotating the motor shaft?</summary>
<div class="dtree-body"><strong>Yes:</strong> The encoder is working; the problem is likely in the cable, parameters, or drive input card.<br><strong>No:</strong> The encoder itself has failed and needs replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the VFD and lock out** the main disconnect according to facility lockout-tagout procedures before beginning any work.
2. **Inspect the encoder cable** from end to end for physical damage, pinched sections, or signs of abrasion and moisture; check that connectors are firmly seated at both the motor encoder and the drive terminals.
3. **Verify encoder wiring** against the drive manual and encoder documentation, confirming that A, B, Z channels and power supply pins are correctly assigned and that cable shield is grounded at one end only.
4. **Check drive parameter settings** for encoder type (incremental or absolute), pulses per revolution, and signal polarity; consult your model's parameter list and compare with the encoder nameplate.
5. **Measure encoder supply voltage** at the encoder connector with a multimeter while the drive is powered; it should match the encoder's rated voltage (commonly 5 VDC or 24 VDC) within tolerance.
6. **Test encoder output signals** using an oscilloscope or the drive's built-in encoder diagnostics; manually rotate the motor shaft and observe for clean square-wave pulses on channels A and B.
7. **Replace the encoder or cable** if testing confirms hardware failure; make sure the replacement encoder matches the original pulses per revolution and supply voltage, then reconfigure parameters and run a test cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Incremental rotary encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01666-fault-code&k=Incremental+rotary+encoder&tag=errorcodefixes-20) \| Must match motor shaft size, pulses per revolution, and voltage rating of original; verify connector pinout. |
| Shielded encoder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a01666-fault-code&k=Shielded+encoder+cable&tag=errorcodefixes-20) \| Use cable designed for encoder applications with twisted pairs and proper shielding; route away from motor power cables. |

## When to Call a Pro

Call a qualified drives technician or industrial electrician if you are not trained in VFD diagnostics or if your facility safety rules require certified personnel for any work inside the drive enclosure. Professional help is also necessary when the fault persists after cable and parameter checks, when you need to verify the drive's encoder input card with specialized test equipment, or when the encoder is mounted in a hazardous location. Working inside energized VFD cabinets carries high-voltage shock risk, and improper encoder wiring can damage both the drive and the motor.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Siemens G120 A01590 Fault Code - Causes & Fix](/posts/siemens-g120-a01590-fault-code/)
- [Siemens Micromaster F0060 - Causes & Fix](/posts/siemens-micromaster-vfd-f0060-fault-code/)
- [Siemens Sinumerik Alarm 300204 — Causes & Fix](/posts/siemens-sinumerik-alarm-300204/)
- [Siemens G120 F01015 Fault - Causes & Fix](/posts/siemens-g120-vfd-f01015-fault-code/)
