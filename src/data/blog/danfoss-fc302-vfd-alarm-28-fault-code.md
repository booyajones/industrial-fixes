---
title: "Danfoss FC302 VFD Alarm 28 - Causes & Fix"
description: "Alarm 28 means brake resistor not connected or failed. Check parameter 2-15, inspect wiring, and test resistor continuity."
pubDatetime: 2026-06-04T09:10:06Z
modDatetime: 2026-06-04T09:10:06Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss brake resistor (match your FC 302 frame size and power)"
most_likely_cause: "Brake resistor disconnected or missing"
---

## Danfoss FC302 VFD Alarm 28 — What It Means

Alarm 28 on a Danfoss FC 302 VFD is a 'Brake check failed' warning. The drive's brake-resistor supervision has detected that the external brake resistor is either not connected or not working. The FC 302 monitors the braking circuit during operation, and when this check fails, the drive cannot safely dissipate regenerative energy from the motor during deceleration or overhauling loads.

This alarm is directly tied to parameter 2-15 (Brake Check) and the physical brake-resistor circuit. The drive expects to see specific electrical behavior from the brake resistor when braking is demanded. If the circuit is open, the resistor has failed internally, or the brake-check setting does not match the installed hardware, Alarm 28 will trigger and the drive may limit braking performance or shut down to protect itself.

[Jump to Fix](#fix)

## Common Causes

- **Brake resistor disconnected or missing** The external brake resistor is not landed at the drive's brake terminals or has been removed.
- **Open or failed brake resistor element** The resistor assembly has failed internally, creating an open circuit that the drive detects during the brake check.
- **Loose or damaged brake wiring** Connections between the drive brake terminals and the resistor are loose, corroded, or broken, interrupting the circuit.
- **Incorrect parameter 2-15 Brake Check setting** The brake-check configuration does not match the installed brake hardware, causing the drive to flag a failure even when the resistor is present.
- **Drive brake-chopper or monitoring circuit fault** If the resistor and wiring are verified good, the drive's internal brake-detection or chopper circuitry may have failed.

## Step-by-Step Fix {#fix}

1. **Remove all power** to the FC 302 and wait for DC bus capacitors to discharge before touching any brake-circuit terminals or wiring.
2. **Check parameter 2-15 (Brake Check)** in the drive programming and confirm it is set correctly for your installed brake resistor and application.
3. **Inspect all brake-resistor wiring** from the drive brake terminals to the resistor assembly for loose connections, broken strands, corrosion, or incorrect landing.
4. **Verify the brake resistor is physically connected** and that it matches the specifications required by the FC 302 brake option or chopper circuit.
5. **Measure the brake-resistor circuit** with a multimeter (power removed) to check for continuity and expected resistance. An open reading confirms a disconnected or failed resistor.
6. **Replace the brake resistor assembly** if the circuit is open or the resistor tests out of range. Reconnect all wiring securely and restore power to test.
7. **If the alarm persists** with a verified good resistor and wiring, contact Danfoss service or a qualified VFD technician to diagnose the drive's internal brake-chopper or monitoring circuitry.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss brake resistor (match your FC 302 frame size and power) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-28-fault-code&k=Danfoss+brake+resistor+%28match+your+FC+302+frame+size+and+power%29&tag=errorcodefixes-20) \| Primary replacement when Alarm 28 indicates resistor failure or open circuit. |
| Brake-circuit wiring and terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-28-fault-code&k=Brake-circuit+wiring+and+terminals&tag=errorcodefixes-20) \| Replace any damaged, corroded, or undersized conductors in the brake path. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss service if you have verified the brake resistor is connected, measures the correct resistance, all wiring is intact, and parameter 2-15 is set correctly but Alarm 28 still appears. At that point the fault is likely inside the drive's brake-chopper or monitoring circuit, which requires specialized test equipment and knowledge of high-voltage DC circuits. Also call a pro if you are unfamiliar with VFD safety procedures, working around high DC bus voltages, or configuring brake parameters for regenerative applications.

## See Also

- [Danfoss FC302 Alarm 47 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-47-fault-code/)
- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss FC302 Alarm 14 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-14-fault-code/)
- [Danfoss VFD Fault UL — Causes & Fix](/posts/danfoss-vfd-fault-ul/)
