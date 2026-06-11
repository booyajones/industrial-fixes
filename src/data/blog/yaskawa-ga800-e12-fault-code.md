---
title: "Yaskawa GA800 E12 Fault Code - Causes & Fix"
description: "Yaskawa GA800 E12 (Er-12) is a current detection error. Learn the real causes, step-by-step diagnostics, and repair actions."
pubDatetime: 2026-05-30T12:27:14Z
modDatetime: 2026-05-30T12:27:14Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor output cable / leads"
---

## Yaskawa GA800 E12 Fault Code — What It Means

The Er-12 fault on a Yaskawa GA800 variable frequency drive means the drive is not seeing a valid output current feedback signal, or the sensed current is outside the expected range for the operating condition. The drive's current measurement circuit has detected a problem, which typically points to a fault in the motor wiring or an internal drive issue.

In practical terms, the drive either cannot measure the current flowing to the motor or the current pattern does not match what the drive expects during normal operation. This fault is linked to current detection signal problems and can occur during startup, auto-tuning, or under load.

[Jump to Fix](#fix)

## Common Causes

- **Open phase or missing motor lead** One of the output phases (U/T1, V/T2, or W/T3) is disconnected, broken, or not making contact at the drive or motor terminal.
- **Loose or damaged motor wiring** Motor cable terminations are loose, insulation is damaged, or conductors are swapped, creating an abnormal current pattern the drive flags as an error.
- **Output short circuit or wiring fault** A shorted motor lead, grounded output conductor, or internal motor fault causes current to exceed the drive's rating or expected range.
- **Contactor open or not making contact** If a magnetic contactor exists between the drive and motor, it may be open or failing to close one phase properly during operation.
- **Motor disconnected during auto-tuning** The drive attempted to measure motor parameters while the motor was not connected or while a contactor was open.
- **Failed current detection circuitry in the drive** When external wiring and the motor test good, the drive's internal current measurement circuit has failed and the drive itself needs repair or replacement.

## Step-by-Step Fix {#fix}

1. **Record the exact fault display** and confirm it reads Er-12 on the GA800 panel, not a similar code from a different Yaskawa drive family.
2. **Inspect the motor output wiring** from the GA800 terminals U/T1, V/T2, and W/T3 all the way to the motor, looking for opens, loose terminations, damaged insulation, or swapped conductors.
3. **Verify all three motor phases are present** and the motor is actually connected at the time the fault occurs, especially if the drive was running an auto-tune routine.
4. **Check for shorted motor leads or grounded output conductors** if the fault occurred under load or if current was high before the trip.
5. **Test any magnetic contactor or output switching device** between the drive and motor to confirm it is closed and making good contact on all three phases.
6. **Perform a basic motor resistance check** (drive disconnected and locked out) to rule out a shorted or open motor winding before suspecting the drive.
7. **Reset the drive only after correcting the cause** by clearing the fault condition first, then use the drive's reset function to attempt a restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor output cable / leads | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e12-fault-code&k=Motor+output+cable+%2F+leads&tag=errorcodefixes-20) \| Replace if any phase conductor is broken, damaged, or has failed insulation. |
| Yaskawa GA800 drive (power section) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e12-fault-code&k=Yaskawa+GA800+drive+%28power+section%29&tag=errorcodefixes-20) \| Replace when external wiring and motor test good but Er-12 persists, indicating internal current detection failure. |
| Magnetic contactor (if used) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e12-fault-code&k=Magnetic+contactor+%28if+used%29&tag=errorcodefixes-20) \| Replace if contacts are pitted, stuck, or not closing all three phases reliably. |

## When to Call a Pro

Call a qualified technician or contact Yaskawa technical support if you have verified all motor wiring, tested the motor, and checked any contactors but the Er-12 fault continues to appear. Persistent faults after external wiring checks usually indicate an internal drive failure in the current detection circuit, which requires drive-level repair or replacement. Also call a pro if you are not comfortable working with live high-voltage VFD circuits or if your facility does not allow field troubleshooting of drive internals.

## See Also

- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa GA800 oC Fault — Overcurrent Fix](/posts/yaskawa-ga800-error-oc/)
- [Yaskawa A1000 Complete Guide - Fault Codes, Parameters, and Commissioning](/posts/yaskawa-a1000-complete-guide/)
- [Yaskawa GA800 E03 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e03-fault-code/)
