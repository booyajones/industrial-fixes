---
title: "Danfoss FC302 ALARM 22 - Causes & Fix"
description: "ALARM 22 on a Danfoss FC302 means the hoist mechanical brake did not release or the drive missed torque reference before timeout."
pubDatetime: 2026-05-29T09:43:54Z
modDatetime: 2026-05-29T09:43:54Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 ALARM 22 — What It Means

ALARM 22 on a Danfoss VLT AutomationDrive FC 302 is labeled 'Hoist mechanical brake.' The alarm trips when the drive does not reach the expected torque reference within the time set by the hoist or brake control parameters. This is a brake and load condition fault, not an electrical short, earth fault, or communication error.

The drive expects to see torque build up as the brake releases and the motor starts to lift or move the load. If the brake sticks, the load binds, or the torque ramp-up takes too long, the timeout expires and the drive shuts down to protect the hoist system.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical brake not releasing fully** The brake shoes or actuator are sticking, corroded, or contaminated so the brake does not open when commanded.
- **Brake coil or actuator failure** The brake coil has failed or is not receiving power, so the brake remains engaged even when the drive signals release.
- **Incorrect brake timing or torque ramp parameters** The timeout for reaching torque reference is set too short, or the torque ramp settings do not match the application load.
- **Excessive mechanical load or binding** The hoist load is too heavy, the sheave or cable is jammed, or another mechanical fault prevents the motor from developing torque quickly enough.
- **Faulty brake wiring or interposing relay** Loose connections, broken wires, or a failed relay in the brake control circuit prevent the brake from receiving the release command.

## Step-by-Step Fix {#fix}

1. **Verify the brake releases mechanically** by securing the load and checking that the brake shoes or disc open fully when power is applied to the brake coil.
2. **Inspect brake wiring and control relay** for loose terminals, broken wires, or a failed contactor that may block the release signal from reaching the brake actuator.
3. **Check the drive's hoist brake parameters** in the FC 302 programming menu and confirm the torque reference timeout and ramp settings match the load and brake type.
4. **Test the brake coil resistance and supply voltage** to confirm the actuator is energizing properly when the drive commands brake release.
5. **Inspect the hoist load path** for binding, damaged cables, worn sheaves, or any mechanical obstruction that would prevent free movement and slow torque buildup.
6. **Clear the alarm** from the drive display and perform a controlled start test to verify torque reaches reference before the timeout expires.
7. **Replace the mechanical brake assembly or actuator** if inspection reveals worn linings, seized pins, or a failed coil that cannot be repaired in the field.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hoist mechanical brake assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-22-fault-code&k=Hoist+mechanical+brake+assembly&tag=errorcodefixes-20) \| For worn or sticking brake shoes, liners, or actuator that will not release cleanly. |
| Brake coil or electromagnetic actuator | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-22-fault-code&k=Brake+coil+or+electromagnetic+actuator&tag=errorcodefixes-20) \| When the coil fails electrically and the brake does not open on command. |
| Brake control relay or contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-22-fault-code&k=Brake+control+relay+or+contactor&tag=errorcodefixes-20) \| If the interposing relay in the brake circuit is burned or has welded contacts. |

## When to Call a Pro

Call a qualified hoist technician or Danfoss-certified drive specialist if you cannot verify brake release, if the alarm persists after replacing the brake components, or if you are unfamiliar with hoist safety lockout and load-test procedures. Hoist applications involve fall hazards and require rigorous lockout-tagout discipline. A professional can also re-tune the drive's torque ramp and brake timing parameters to match your exact load profile and prevent nuisance trips.

## See Also

- [Danfoss FC302 ALARM 16 - Causes & Fix](/posts/danfoss-fc302-alarm-16-fault-code/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-alarm-32-fault-code/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC-302 Alarm 13 — DC Link Overvoltage Fix](/posts/danfoss-fc302-alarm-13/)
