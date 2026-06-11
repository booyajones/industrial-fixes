---
title: "Danfoss FC302 ALARM 27 - Causes & Fix"
description: "ALARM 27 on a Danfoss FC302 means brake chopper fault. Learn the exact causes, step-by-step diagnostics, and repair."
pubDatetime: 2026-05-29T09:46:40Z
modDatetime: 2026-05-29T09:46:40Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Brake resistor (matched to FC 302 model and application)"
---

## Danfoss FC302 ALARM 27 — What It Means

ALARM 27 on a Danfoss VLT AutomationDrive FC 302 indicates a brake chopper fault or brake IGBT fault. The drive monitors the internal brake transistor (IGBT) and raises this alarm when the braking circuit reports a problem. This is an internal drive fault, not a motor overload or a terminal 27 I/O issue.

The brake chopper is the circuit that dissipates energy during motor deceleration through an external brake resistor. When the drive detects that this chopper or its IGBT has failed, it shuts down and logs Alarm 27. The fault can originate from external resistor problems or from a failed internal brake stage.

[Jump to Fix](#fix)

## Common Causes

- **Brake resistor failure or miswiring** A shorted, open, incorrectly sized, or miswired brake resistor can force the chopper into a fault condition.
- **Failed brake chopper or IGBT** The internal braking transistor (IGBT) has failed and the drive's monitoring logic detects the fault.
- **Excessive braking duty** Repeated or heavy deceleration cycles can over-stress the brake chopper if the resistor and duty cycle are not matched to the application.
- **Damaged brake resistor wiring** Loose terminals, damaged cables, or poor connections at the brake terminals can interrupt or short the brake circuit.
- **Control or power-stage damage** Internal damage to the drive's brake circuit or power section can trigger the fault and may require replacement of the power board or entire drive.

## Step-by-Step Fix {#fix}

1. Shut down the motor and disconnect AC mains and any DC-link or remote backup supplies, then lock out and wait for capacitors to fully discharge before touching the drive.
2. Inspect the brake resistor visually for damage, overheating, loose terminals, and incorrect connections at the brake terminals on the drive.
3. Verify the brake resistor specifications match the drive's requirements and confirm the installation has not exceeded the resistor's duty rating or power limits.
4. Measure the brake resistor and wiring for continuity and resistance with power removed to confirm there is no open circuit, short, or abnormal resistance value.
5. Check all brake circuit wiring for damage, secure all terminals, and correct any miswiring or loose connections before attempting a reset.
6. If the brake resistor and wiring test good, suspect the drive's internal brake IGBT or brake chopper stage and consult the service manual or Danfoss support for internal diagnostics.
7. Replace the failed brake resistor if damaged, or replace the brake chopper/power section or entire drive if the internal brake circuit has failed and is not field-repairable.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Brake resistor (matched to FC 302 model and application) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-27-fault-code&k=Brake+resistor+%28matched+to+FC+302+model+and+application%29&tag=errorcodefixes-20) \| Replace if open, shorted, overheated, or damaged. Confirm ohmic value and power rating from drive manual. |
| Brake chopper / power section for FC 302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-27-fault-code&k=Brake+chopper+%2F+power+section+for+FC+302&tag=errorcodefixes-20) \| Required if internal brake IGBT has failed. May be sold as power board or complete power stage depending on model. |
| Danfoss VLT AutomationDrive FC 302 (complete drive) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-27-fault-code&k=Danfoss+VLT+AutomationDrive+FC+302+%28complete+drive%29&tag=errorcodefixes-20) \| Needed if brake stage is not separately replaceable or if multiple internal faults are present. |

## When to Call a Pro

Call a qualified technician or VFD specialist if the brake resistor and wiring check good but Alarm 27 persists, if you are not trained to safely discharge and work inside the drive, or if internal brake chopper replacement is required. Brake IGBT and power-stage faults require experience with drive internals and access to service documentation. Danfoss technical support or an authorized service center can diagnose internal faults and determine if the power section is field-replaceable or if the entire drive must be replaced.

## See Also

- [Danfoss FC302 ALARM 35 - Causes & Fix](/posts/danfoss-fc302-alarm-35-fault-code/)
- [Danfoss FC302 Alarm 34 - Causes & Fix](/posts/danfoss-fc302-alarm-34-fault-code/)
- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC302 Alarm 17 - Causes & Fix](/posts/danfoss-fc302-alarm-17-fault-code/)
