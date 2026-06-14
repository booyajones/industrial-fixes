---
title: "Danfoss FC302 ALARM 28 - Causes & Fix"
description: "Danfoss FC302 ALARM 28 (Brake Check) means the drive detected a fault in the brake resistor circuit. Learn causes and repair steps."
pubDatetime: 2026-05-29T09:47:05Z
modDatetime: 2026-05-29T09:47:05Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss brake resistor"
most_likely_cause: "Brake resistor not connected"
---

## Danfoss FC302 ALARM 28 — What It Means

ALARM 28 on the Danfoss FC302 drive indicates a brake check failure. The drive's internal brake-check function has detected that the brake resistor or brake circuit is not behaving as expected. This alarm is linked to parameter 2-15 (Brake Check) and typically appears when the brake resistor is missing, disconnected, or faulty. The drive uses the brake resistor to dissipate excess energy during deceleration or overhauling loads, and without a working brake circuit, safe operation cannot be guaranteed.

[Jump to Fix](#fix)

## Common Causes

- **Brake resistor not connected** The brake resistor wiring is loose, disconnected, or not terminated at the drive's brake terminals.
- **Defective brake resistor** The brake resistor has failed open-circuit or otherwise does not meet electrical requirements.
- **Brake-check parameter enabled without hardware** Parameter 2-15 Brake Check is enabled but no brake resistor is physically installed on the system.
- **Damaged wiring or terminals** The brake resistor wiring or terminals are damaged, overheated, or corroded.
- **Internal drive brake circuit fault** After verifying external wiring and resistor, the drive's internal brake chopper or monitoring circuit may have failed.

## Step-by-Step Fix {#fix}

1. De-energize the drive and wait for DC bus discharge. Disconnect line power and allow capacitors to fully discharge before opening the unit or accessing power terminals.
2. Inspect the brake resistor wiring at both the drive and resistor. Look for loose connections, damage, overheating, or incorrect termination at the brake terminals.
3. Verify a brake resistor is installed. If parameter 2-15 Brake Check is enabled but no resistor is present, the alarm is expected and the parameter setting must match your hardware.
4. Check parameter 2-15 Brake Check. Confirm it is configured correctly for your application and matches whether a brake resistor is actually installed.
5. Measure the brake resistor electrically if you suspect failure. An open circuit or abnormal resistance reading indicates the resistor needs replacement.
6. Repair or replace the brake resistor and wiring. Replace any damaged, open, or heat-damaged resistor and fix any faulty connections or wiring.
7. Clear the alarm and retest the drive. After correcting the wiring or hardware condition, reset the fault and verify normal operation under load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-28-fault-code&k=Danfoss+brake+resistor&tag=errorcodefixes-20) \| Match to your FC302 frame size and braking power requirements. |
| Brake resistor terminals and wiring | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-28-fault-code&k=Brake+resistor+terminals+and+wiring&tag=errorcodefixes-20) \| Replace if overheated, corroded, or damaged during inspection. |

## When to Call a Pro

Call a qualified drive technician if the alarm persists after you have verified the brake resistor is installed, wired correctly, and tests good electrically. A continuing ALARM 28 after external components are confirmed suggests an internal drive fault in the brake chopper or monitoring circuit, which requires factory-trained service and may involve power section replacement. Also call a professional if you are not comfortable working with high-voltage DC bus circuits or if your facility does not have lockout procedures for VFD service.

## See Also

- [Danfoss FC301 Fault AL 14 — Ground Fault Causes & Fix](/posts/danfoss-fc301-fault-al-14/)
- [Danfoss FC302 ALARM 33 - Causes & Fix](/posts/danfoss-fc302-alarm-33-fault-code/)
- [Danfoss FC302 Alarm 39 - Causes & Fix](/posts/danfoss-fc302-alarm-39-fault-code/)
- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/posts/danfoss-fc302-alarm-13/)
