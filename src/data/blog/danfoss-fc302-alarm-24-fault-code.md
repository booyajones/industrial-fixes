---
title: "Danfoss FC302 Alarm 24 - Causes & Fix"
description: "Alarm 24 on the Danfoss FC302 drive means Safe Stop is active. Learn how to check external safety circuits, reset interlocks, and clear this fault."
pubDatetime: 2026-05-29T09:45:04Z
modDatetime: 2026-05-29T09:45:04Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Safety relay"
most_likely_cause: "External E-stop or safety device is active"
---

## What this code means
Alarm 24 on the Danfoss VLT AutomationDrive FC 302 indicates that the Safe Stop function is active. This safety feature disables the drive's torque output whenever the safe-stop circuit is open or not satisfied. The drive is not reporting a motor, overload, or power section failure. Instead, it has detected that a required safety condition is not met, so it prevents operation to protect personnel and equipment.

In most cases, this alarm points to an external safety device or interlock in the safe-stop chain rather than an internal drive fault. The drive is doing its job by monitoring the safety inputs and halting operation when the circuit is interrupted. Your task is to verify the external safety chain, restore the closed loop, and reset the alarm once the safety condition is satisfied.

## Common Causes

- **External E-stop or safety device is active** An emergency stop button, safety gate switch, guard interlock, or other hardwired safety device in the safe-stop chain is open or not reset.
- **24 VDC control supply missing or interrupted** The control-side 24 VDC power feeding the safety circuit or interlock loop is absent, low, or cut off.
- **Wiring or terminal connection fault in the safety loop** Loose terminals, broken wires, incorrect terminal landing, or damaged insulation in the safe-stop input path has opened the circuit.
- **Safety relay contact not closed** A safety relay upstream of the drive's safe-stop input has not picked up, is faulted, or requires a manual reset.
- **Intentional safety lockout condition** The machine safety circuit is deliberately open due to maintenance mode, door interlock, or operator lockout, and the alarm is correct.

## Step-by-Step Fix {#fix}

1. Verify whether the safety condition is intentional by checking for open guard doors, active E-stops, maintenance locks, or operator lockout tags before troubleshooting further.
2. Check every external safety device in the chain including emergency stop buttons, guard interlocks, safety gate switches, and reset pushbuttons to confirm they are closed and latched.
3. Measure 24 VDC control supply at the drive's control terminals and verify the supply is present and stable at the safety circuit input and interlock loop as required by your wiring diagram.
4. Inspect the wiring and terminals in the safe-stop circuit for loose connections, broken conductors, incorrect wiring, corrosion, or damaged insulation and repair or re-land as needed.
5. Reset any safety relays or interlock devices that require manual reset, then clear Alarm 24 at the drive keypad or via the configured reset method.
6. If the alarm persists with the external safety loop confirmed closed, powered, and wired correctly, review the drive's safety input parameters and configuration against the installed safety option and wiring.
7. Test drive operation in a safe manner and monitor for recurrence of the alarm after confirming the safety circuit is intact and all devices are functioning.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-24-fault-code&k=Safety+relay&tag=errorcodefixes-20) \| Replace if the relay in the safe-stop chain is faulted, not picking up, or has damaged contacts. |
| Emergency stop button | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-24-fault-code&k=Emergency+stop+button&tag=errorcodefixes-20) \| Replace if the E-stop is mechanically stuck, will not reset, or has failed contacts in the safety loop. |
| Safety interlock switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-24-fault-code&k=Safety+interlock+switch&tag=errorcodefixes-20) \| Replace if a guard or gate switch is broken, misaligned, or has unreliable contact closure. |
| 24 VDC control power supply | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-24-fault-code&k=24+VDC+control+power+supply&tag=errorcodefixes-20) \| Replace if the control-side supply has failed and cannot deliver stable 24 VDC to the safety circuit. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained in industrial safety systems, cannot locate the open safety device after inspection, or if the alarm returns with the external safety circuit confirmed closed and powered. Do not bypass or jumper safety interlocks. If the drive's safety input configuration or internal control board is suspect after all external checks pass, a factory-trained service provider should verify parameters and inspect the drive's safety interface hardware to avoid compromising machine safety certification.
