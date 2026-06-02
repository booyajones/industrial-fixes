---
title: "ABB ACS580 A2B1 Fault Code - Causes & Fix"
description: "A2B1 means overcurrent on your ABB ACS580 VFD. Usually caused by overload, short ramps, or wiring faults. Check load and motor cables first."
pubDatetime: 2026-05-31T11:07:51Z
modDatetime: 2026-05-31T11:07:51Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 A2B1 Fault Code — What It Means

The A2B1 fault (auxiliary code 2310) on an ABB ACS580 variable frequency drive indicates overcurrent. The drive has detected that output current exceeded its internal fault limit. This fault can signal a true overload condition, but ABB also notes it may be triggered by an earth fault in the motor or cable, or by a phase loss in the motor leads. The drive shuts down to protect itself and the motor from damage.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical overload on the motor or driven equipment** The load is jammed, binding, or operating above the motor's rated torque, forcing excessive current draw.
- **Acceleration ramp set too short** The drive tries to spin the motor up too quickly, demanding more current than the system can safely supply during the ramp.
- **Earth fault or insulation breakdown in motor or cable** ABB explicitly lists earth faults as a common cause of A2B1, where current leaks to ground through damaged insulation.
- **Output phase loss or loose motor lead** A broken or poorly terminated conductor between the drive and motor causes unbalanced currents that trip the overcurrent limit.
- **Short circuit in motor cable or motor windings** A hard short between phases or turns in the motor forces instantaneous high current and triggers the fault.
- **Power factor correction capacitors installed in motor circuit** ABB warns that capacitors or surge absorbers on the motor cable can interfere with drive operation and cause current-related faults.

## Step-by-Step Fix {#fix}

1. {'lead': 'Check the load for mechanical binding or overload.', 'text': 'Disconnect the motor from the driven machine if possible and verify the machine turns freely by hand; if it is jammed or requires excessive force, resolve the mechanical issue before restarting the drive.'}
2. {'lead': 'Inspect all motor cable terminations and wiring.', 'text': 'Look for loose or corroded terminals at both the drive output and the motor junction box, verify all three phases are securely landed, and check for any visible damage to the cable jacket or conductors.'}
3. {'lead': 'Test motor and cable insulation resistance to ground.', 'text': 'Use a megohmmeter to measure insulation resistance between each motor phase and ground with the motor disconnected from the drive; low readings indicate an earth fault that must be repaired.'}
4. {'lead': 'Review and lengthen the acceleration time parameter.', 'text': "Access the drive's ramp settings and increase the acceleration time to allow the motor to start more gradually, reducing inrush current."}
5. {'lead': 'Check for short circuits in motor cable and motor windings.', 'text': 'Measure phase-to-phase resistance at the motor terminals with the drive disconnected; identical low readings are normal, but a very low or zero reading may indicate a short that requires motor or cable replacement.'}
6. {'lead': 'Verify no power factor correction devices are installed.', 'text': 'Remove any capacitors, surge absorbers, or RC snubbers from the motor circuit, as ABB documentation cautions these components can cause faults with VFD operation.'}
7. {'lead': 'Confirm drive current settings match motor nameplate.', 'text': "Compare the drive's configured motor current and overload parameters to the values on the motor nameplate; adjust if undersized or incorrectly entered during commissioning."}

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b1-fault-code&k=VFD-rated+motor+cable&tag=errorcodefixes-20) \| Use shielded cable rated for variable frequency drive output if the existing cable shows damage or fails insulation testing. |
| Motor terminal blocks and lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b1-fault-code&k=Motor+terminal+blocks+and+lugs&tag=errorcodefixes-20) \| Replace corroded or burned terminals; match wire gauge and torque to manufacturer specifications. |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a2b1-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Required if insulation or winding tests indicate internal motor failure; consider professional rewind for large motors. |

## When to Call a Pro

Call an electrician or ABB-certified technician if you have confirmed the load is not overloaded and all wiring tests pass but the A2B1 fault returns immediately on restart. Persistent faults after load and cable checks may indicate a failed drive output stage or incorrect parameter configuration that requires diagnostic software and factory training. ABB recommends contacting your local ABB service representative if the fault cannot be resolved by field inspection of the motor and cable.
