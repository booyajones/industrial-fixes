---
title: "ABB ACS580 A2B1 Fault Code - Causes & Fix"
description: "ABB ACS580 A2B1 (Overcurrent) means output current exceeded the internal fault limit. Learn causes, diagnostic steps, and repairs."
pubDatetime: 2026-05-26T21:47:31Z
modDatetime: 2026-05-26T21:47:31Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "Motor cable (shielded VFD-rated)"
most_likely_cause: "Mechanical overload or jammed load"
---

## What this code means
The A2B1 fault on an ABB ACS580 drive indicates an overcurrent condition. The drive has detected that output current to the motor exceeded its internal fault limit and shut down to protect itself. This fault code appears with auxiliary code 2310 in the event log.

Although the primary meaning is overcurrent, ABB notes that A2B1 can also be triggered by an earth fault or a missing motor phase. The fault may occur during startup, acceleration, or steady-state operation depending on the root cause. The drive will not restart until you clear the fault and address the underlying problem.

## Common Causes

- **Mechanical overload or jammed load** The driven machine is binding, seized, or drawing excessive torque that forces the motor current beyond the fault threshold.
- **Acceleration ramp too fast** The drive ramps up speed too quickly and the motor current spikes during startup or speed changes, triggering the overcurrent limit.
- **Motor cable or motor short circuit** Damaged insulation, a shorted turn, or a phase-to-phase fault in the motor windings or cable causes excessive current flow.
- **Earth fault in motor or cable** A phase conductor is leaking current to ground through damaged insulation or a wet motor, tripping the overcurrent protection.
- **Missing motor phase or wiring error** A loose connection, broken wire, or incorrect delta/star termination causes unbalanced current and fault detection.
- **Power factor correction capacitors on motor cable** Capacitors or surge absorbers installed between the drive output and motor create current transients that the drive interprets as overcurrent.

## Step-by-Step Fix {#fix}

1. **Read the fault code and auxiliary code** from the drive keypad or event log to confirm A2B1 with auxiliary code 2310, then reset the drive and note whether the fault recurs immediately or only under load.
2. **Inspect the driven load** for mechanical binding, jammed parts, or excessive friction by manually rotating the shaft (power off and locked out) and checking for abnormal resistance or foreign objects.
3. **Review and lengthen the acceleration ramp time** in the drive parameters if the fault occurs during startup, giving the motor more time to reach target speed and reducing inrush current.
4. **Verify motor nameplate data** against the drive startup parameters (voltage, frequency, rated current, power) and correct any mismatches that would cause the drive to deliver incorrect current.
5. **Check motor wiring and connections** at both the drive output terminals and motor terminal box for tight connections, correct phase sequence, proper delta or star configuration, and any signs of arcing or corrosion.
6. **Measure motor and cable insulation resistance** to ground using a megohmmeter (power off, drive disconnected) and inspect the motor cable for physical damage, cuts, or moisture that could cause a short or earth fault.
7. **Remove any power factor correction capacitors or surge absorbers** from the motor cable if present, as ABB explicitly prohibits these components between the drive output and motor, then test-run the drive and monitor current on all three phases during acceleration and loaded operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b1-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation is damaged, conductors are shorted, or resistance-to-ground is low. |
| Motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b1-fault-code&k=Motor&tag=errorcodefixes-20) \| Required if windings are shorted, insulation has failed, or internal fault is confirmed by testing. |
| Motor terminal connectors and lugs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a2b1-fault-code&k=Motor+terminal+connectors+and+lugs&tag=errorcodefixes-20) \| Replace any corroded, burned, or loose terminals found during wiring inspection. |

## When to Call a Pro

Contact ABB service or a qualified drive technician if the A2B1 fault persists after you have verified the load, corrected the ramp settings, checked all wiring, confirmed motor parameters, and ruled out external shorts or ground faults. Repeated overcurrent trips that occur with no mechanical overload or wiring issue may indicate internal drive damage to the IGBT modules or current sensors that require factory-level diagnostics and repair. ABB's troubleshooting guide directs users to contact service when standard checks do not resolve the fault.
