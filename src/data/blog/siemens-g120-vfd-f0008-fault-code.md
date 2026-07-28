---
title: "Siemens G120 F0008 Fault - Causes & Fix"
description: "F0008 on a Siemens G120 VFD means DC link undervoltage. Check incoming AC supply voltage and input wiring before replacing rectifier."
pubDatetime: 2026-06-02T10:29:05Z
modDatetime: 2026-06-02T10:29:05Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 input rectifier module"
most_likely_cause: "Incoming AC supply undervoltage or line dip"
---

## What this code means
F0008 is a DC link undervoltage fault on the Siemens SINAMICS G120 variable frequency drive. The drive has detected that the internal DC bus voltage has dropped below the minimum threshold required for safe operation and has tripped to protect the power stage. This fault stops the drive immediately because the rectifier cannot maintain the voltage needed to synthesize clean AC output to the motor.

The DC link is the capacitor bank between the input rectifier and the output inverter. When the incoming three-phase AC is converted to DC, that voltage must stay within a defined window. If it falls too low due to supply problems or internal component failure, the drive shuts down and logs F0008. The fault can occur at startup, during acceleration, or randomly during a run if the supply sags or a component fails.

## Common Causes

- **Incoming AC supply undervoltage or line dip** The facility supply voltage is too low or a momentary sag occurs while the drive is running, starving the rectifier of energy to charge the DC link.
- **Loose or corroded input power terminals** Poor connections at the drive input terminals or at upstream disconnects and contactors create high resistance that drops voltage before it reaches the rectifier.
- **Blown fuse or tripped upstream breaker** A single missing phase or weak supply path prevents the rectifier from producing full DC bus voltage.
- **Failed input rectifier or power module** Internal diodes or the integrated power stage cannot convert AC to DC properly even when correct line voltage is present.
- **Damaged line reactor or input filter** External inductors or EMI filters with internal opens or short circuits disrupt the AC path to the drive.
- **Incorrect supply voltage parameter setting** The drive is configured for a different line voltage than what is actually connected, causing the undervoltage trip threshold to be misapplied.

## Step-by-Step Fix {#fix}

1. {'lead': '**Lock out and verify zero energy** on all incoming power.', 'text': 'Open the disconnect or breaker feeding the drive, verify lockout/tagout, and use a multimeter to confirm zero voltage at the drive input terminals before opening the enclosure.'}
2. {'lead': '**Measure the incoming line voltage** at the drive input terminals.', 'text': "With power restored but the drive still faulted, measure L1–L2, L2–L3, and L3–L1 voltage and compare each to the drive's nameplate input rating and parameter settings to confirm the supply is within tolerance."}
3. {'lead': '**Inspect all upstream power components** for damage or looseness.', 'text': 'Check fuses, contactors, disconnect terminals, and any line reactors or filters for signs of heat, corrosion, loose bolts, or blown fuses that would reduce or interrupt the supply.'}
4. {'lead': "**Review the drive's fault history buffer** using the keypad or connected software.", 'text': 'Navigate to the diagnostic or fault-log parameters and note whether F0008 appears during start, acceleration, or at random to help narrow the trigger condition.'}
5. {'lead': "**Check the drive's line-voltage parameter** setting against the actual supply.", 'text': 'Verify that the parameter for expected input voltage matches your facility supply to rule out a configuration mismatch triggering false undervoltage trips.'}
6. {'lead': '**Test the DC bus voltage directly** if your model provides test points or a parameter display.', 'text': 'With the drive powered and not running, observe the DC link voltage reading to see if it is significantly below the expected rectified value for your AC input.'}
7. {'lead': '**Replace the input rectifier or power module** if external supply and wiring are correct.', 'text': 'When correct line voltage is present, wiring is tight, and the DC link still cannot charge, the internal rectifier or integrated power stage has failed and must be replaced by a qualified technician or sent for factory repair.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 input rectifier module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0008-fault-code&k=Siemens+G120+input+rectifier+module&tag=errorcodefixes-20) \| Order by drive frame size and voltage rating if your model uses a replaceable rectifier block. |
| Siemens G120 power module (CU240 or PM240) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0008-fault-code&k=Siemens+G120+power+module+%28CU240+or+PM240%29&tag=errorcodefixes-20) \| Required when the integrated power stage is faulty and the rectifier is not sold separately. |
| Input line fuses | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0008-fault-code&k=Input+line+fuses&tag=errorcodefixes-20) \| Match the fuse type and amperage specified on the drive nameplate or input wiring diagram. |

## When to Call a Pro

Call a qualified drives technician or Siemens-certified service partner if you measure correct incoming voltage and tight connections but the DC link still trips low, if you are uncomfortable working inside energized industrial control cabinets, or if your drive has no external fault-reset capability and requires laptop-based diagnostics. Replacing the input rectifier or power module requires matching the exact frame size and firmware revision, and many G120 configurations need parameter backup and commissioning software to restore full operation after a hardware swap.
