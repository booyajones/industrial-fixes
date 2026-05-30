---
title: "Siemens Micromaster F0002 - Causes & Fix"
description: "Siemens Micromaster F0002 means DC-link overvoltage. Common causes: high supply voltage, fast deceleration, brake resistor failure. Step-by-step repair guide."
pubDatetime: 2026-05-28T09:11:08Z
modDatetime: 2026-05-28T09:11:08Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens Micromaster F0002 — What It Means

F0002 is a DC-link overvoltage fault on Siemens Micromaster drives (420/440 families). The drive has detected that the intermediate-circuit voltage has risen above its permitted limit and has tripped to protect the inverter stage. This happens when the DC bus capacitors absorb more voltage than the drive can safely handle.

The fault usually appears during deceleration or braking because the motor acts as a generator and pushes energy back into the drive's DC link. It can also occur if your incoming supply voltage is too high or if braking hardware (brake resistor or chopper) has failed or is improperly configured. The drive shuts down immediately to prevent damage to the power electronics.

[Jump to Fix](#fix)

## Common Causes

- **Incoming supply voltage too high** Mains voltage above the drive's rating directly raises the DC bus voltage and triggers the overvoltage trip.
- **Ramp-down time set too short** Fast deceleration forces the motor to regenerate energy faster than the drive can dissipate it, pushing DC-link voltage over the limit.
- **High load inertia during braking** Heavy or high-inertia loads (fans, centrifuges, flywheels) generate large amounts of regenerative energy when stopping.
- **Brake resistor disconnected, failed, or undersized** If the drive uses dynamic braking, a broken wire, burnt resistor, or incorrect resistance value leaves excess energy on the DC bus.
- **Brake chopper not enabled or faulty** The chopper circuit must be active and working to switch the brake resistor into the circuit during overvoltage events.
- **DC-link voltage controller disabled or misconfigured** Parameter P1240 and related settings control how the drive manages regenerative energy, and incorrect values can prevent proper voltage regulation.

## Step-by-Step Fix {#fix}

1. **Verify the fault code** by reading the display or parameter P0947 to confirm it is F0002 and not a different overvoltage alarm or DC-bus fault.
2. **Measure incoming AC line voltage** at the drive input terminals with a multimeter and compare it to the voltage range on the drive nameplate (typically 380–480 V for 400 V class drives). If supply voltage is above rating, correct the upstream electrical distribution or add a step-down transformer.
3. **Check when the fault occurs**. If it trips during deceleration or stopping, the motor is regenerating energy. Review the load type and inertia to confirm whether regenerative braking is expected.
4. **Increase the ramp-down time** (parameter P1121 or equivalent deceleration ramp) to slow the stop and reduce the rate of regenerative energy fed back into the DC link. Start by doubling the current ramp time and retest.
5. **Inspect braking hardware** if the drive has a brake resistor or brake chopper installed. Check all wiring connections, measure the resistor with an ohmmeter to verify it matches the specified value, and look for burn marks or physical damage. Confirm the brake chopper module is seated correctly and not faulted.
6. **Enable or verify the DC-link voltage controller** by setting parameter P1240 to the appropriate mode (consult your drive manual for the correct value for your model and application). This feature helps the drive manage overvoltage by dynamically adjusting motor speed during deceleration.
7. **Reset the fault** by cycling drive power or using the reset function, then run the motor through a full start and stop cycle under normal load to confirm F0002 does not reappear. Monitor the DC-link voltage (parameter r0026 or equivalent) during the test.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0002-fault-code&k=Siemens+Micromaster+brake+resistor&tag=errorcodefixes-20) \| Must match your drive model and power rating. Check the resistance value (ohms) and power rating (watts) in your drive's accessory table. Common cause of F0002 if failed or disconnected. |
| Siemens brake chopper module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0002-fault-code&k=Siemens+brake+chopper+module&tag=errorcodefixes-20) \| Required to switch the brake resistor into the circuit. Verify compatibility with your Micromaster 420 or 440 frame size. Not all drives have this installed from the factory. |
| Siemens Micromaster inverter power stage | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0002-fault-code&k=Siemens+Micromaster+inverter+power+stage&tag=errorcodefixes-20) \| Replacement if the overvoltage event has damaged the IGBT or DC bus capacitors. Usually requires factory or authorized repair. Check for burnt components or swollen capacitors before ordering. |

## When to Call a Pro

Call a qualified electrician or drive technician if you measure abnormal incoming supply voltage and cannot correct it yourself, if the brake resistor or chopper hardware is physically damaged or you are not comfortable working with high-voltage DC circuits, or if the fault persists after you have lengthened deceleration ramps and verified all braking components. Also call a professional if you see burnt components inside the drive, if the drive trips immediately on power-up before any motor movement, or if you are working with a high-power drive (above 5 HP) in a production environment where incorrect troubleshooting could cause expensive downtime or safety hazards. Regenerative applications and custom braking configurations often require load calculation and parameter tuning beyond basic field repair.
