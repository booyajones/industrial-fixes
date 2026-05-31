---
title: "Danfoss FC302 ALARM 18 - Causes & Fix"
description: "ALARM 18 on the Danfoss FC302 means start failure: the motor did not reach required speed in time. Repair guide with causes and steps."
pubDatetime: 2026-05-29T09:42:19Z
modDatetime: 2026-05-29T09:42:19Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 ALARM 18 — What It Means

ALARM 18 on a Danfoss VLT FC 302 means Start Failure. The drive commanded a start, but the motor speed did not increase to the required threshold within the allowed start time. The FC 302 expects the motor to accelerate past the configured Compressor Start Max Speed within the configured Compressor Start Max Time to Trip. If it does not, the drive trips with Alarm 18.

This alarm is almost always caused by a mechanical problem preventing normal acceleration, or by start-time parameters that are too strict for the actual application. It is not typically a sign of failed drive electronics.

[Jump to Fix](#fix)

## Common Causes

- **Motor or compressor mechanically blocked or stuck** The shaft cannot rotate freely, so the motor cannot accelerate to the target speed in time.
- **Excessive load or process binding** The compressor is not unloading properly during startup, or the driven load is too heavy for normal acceleration.
- **Compressor Start Max Speed set too high** Parameter 1-78 is set above the speed the motor can realistically reach during startup.
- **Compressor Start Max Time to Trip set too short** Parameter 1-79 does not allow enough time for the motor to complete its normal ramp-up.

## Step-by-Step Fix {#fix}

1. **Disconnect power and lock out** the VLT FC 302 and motor circuit per NFPA 70E before any hands-on inspection.
2. **Inspect the motor shaft and compressor** to confirm the machine rotates freely by hand or approved mechanical methods, checking for seized bearings, stuck valves, or coupling damage.
3. **Review parameter 1-78 (Compressor Start Max Speed)** on the drive display and compare it to the motor's actual speed during a normal startup to verify the target is achievable.
4. **Review parameter 1-79 (Compressor Start Max Time to Trip)** and increase it if the motor needs more time to reach the target speed under normal load conditions.
5. **Clear the alarm** by cycling drive power or using the reset function, then attempt a test start and monitor actual motor speed against the programmed thresholds.
6. **If the alarm persists after parameter adjustment**, check motor and load sizing, verify the compressor unloader or inlet valve operates correctly, and inspect couplings, belts, or gearboxes for binding.
7. **Document the final parameter settings** and the motor's startup profile so future alarms can be diagnosed quickly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (AC induction or PM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-18-fault-code&k=Motor+%28AC+induction+or+PM%29&tag=errorcodefixes-20) \| Replace if windings are shorted or bearings seized beyond repair. |
| Compressor (reciprocating, screw, or scroll) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-18-fault-code&k=Compressor+%28reciprocating%2C+screw%2C+or+scroll%29&tag=errorcodefixes-20) \| Replace or rebuild if internal damage prevents normal startup acceleration. |
| Motor bearings or coupling | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-18-fault-code&k=Motor+bearings+or+coupling&tag=errorcodefixes-20) \| Replace if worn or binding, preventing free shaft rotation. |

## When to Call a Pro

Call a qualified VFD or compressor technician if you cannot safely rotate the motor by hand, if parameter adjustments do not clear the alarm after verifying the machine is mechanically free, or if you lack the tools to measure actual motor speed during startup. Also call a pro if the compressor shows signs of internal damage (unusual noise, locked rotor, or oil contamination) or if the drive continues to trip on ALARM 18 after confirming correct parameters and a freely rotating load. This alarm usually points to a mechanical or application issue rather than a failed drive component, so expert diagnosis of the motor and driven equipment is often required.

## See Also

- [Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix](/posts/danfoss-fc301-fault-al-14/)
- [Danfoss FC302 Alarm AL 29 — Causes & Fix](/posts/danfoss-fc302-fault-al-29/)
- [Danfoss AKC Controller Fault Codes - Complete Guide](/posts/danfoss-akc-controller-fault/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
