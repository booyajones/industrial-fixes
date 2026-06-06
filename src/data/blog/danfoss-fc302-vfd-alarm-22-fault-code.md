---
title: "Danfoss FC302 Alarm 22 - Hoist Brake Fault Fix"
description: "Alarm 22 on Danfoss FC302 means hoist mechanical brake did not release or feedback timeout. Check brake operation and timing parameters."
pubDatetime: 2026-06-02T10:46:37Z
modDatetime: 2026-06-02T10:46:37Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 22 — What It Means

Alarm 22 on a Danfoss VLT AutomationDrive FC 302 signals a hoist mechanical brake fault. The alarm includes a subcode that tells you which brake condition failed. Subcode 0 means the drive did not reach the required torque reference before the timeout set in parameter 2-27 Torque Ramp Up Time. Subcode 1 means the expected brake feedback signal was not received before the timeout controlled by parameter 2-23 Activate Brake Delay and parameter 2-25 Brake Release Time.

This fault points directly to the hoist brake system rather than the motor or power stage. The drive is monitoring both the mechanical release of the brake and the electrical feedback that confirms the brake has opened. When either condition times out, the drive trips to prevent unsafe hoist operation.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical brake not releasing** The brake assembly is stuck, corroded, or releasing too slowly for the drive's timeout window.
- **Brake feedback circuit failure** The feedback switch or contact does not change state or send the expected signal to the drive when the brake releases.
- **Incorrect brake timing parameters** Parameters 2-23, 2-25, or 2-27 are set too short for the actual brake hardware response time.
- **Brake coil or contactor fault** The brake release coil is not energizing or the brake contactor is failing to pull in when commanded.
- **Wiring or terminal problems** Loose connections, broken wires, or corroded terminals in the brake control or feedback circuit prevent proper operation.

## Step-by-Step Fix {#fix}

1. Read the alarm subcode on the drive display or in diagnostics to determine whether the fault is torque timeout (subcode 0) or brake feedback timeout (subcode 1).
2. Verify mechanical brake release by manually checking that the hoist moves freely when the brake is commanded open and inspect the brake assembly for sticking, wear, or damage.
3. Check brake feedback wiring and contacts using a multimeter to confirm the feedback circuit changes state cleanly when the brake releases and sets.
4. Review and adjust brake timing parameters in the drive: increase parameter 2-27 Torque Ramp Up Time if subcode is 0, or increase parameter 2-23 Activate Brake Delay and parameter 2-25 Brake Release Time if subcode is 1.
5. Test brake coil and contactor operation by measuring voltage at the brake coil terminals when the drive commands brake release and verifying the contactor pulls in.
6. Run a controlled test cycle with the adjusted parameters and no load to confirm the brake releases before torque builds and feedback arrives within the timeout window.
7. Replace failed brake components (coil, contactor, feedback switch, or mechanical assembly) if inspection and testing reveal hardware that does not operate reliably.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hoist mechanical brake assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-22-fault-code&k=Hoist+mechanical+brake+assembly&tag=errorcodefixes-20) \| For the motor or load side brake mechanism if worn or sticking. |
| Brake feedback switch or contact | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-22-fault-code&k=Brake+feedback+switch+or+contact&tag=errorcodefixes-20) \| Replaces failed feedback sensor or auxiliary contact on the brake contactor. |
| Brake release coil or brake contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-22-fault-code&k=Brake+release+coil+or+brake+contactor&tag=errorcodefixes-20) \| For electrically actuated brakes that do not energize or release when commanded. |

## When to Call a Pro

Call a qualified hoist or VFD technician if you are not trained in hoist brake systems or if the alarm persists after you have verified wiring and adjusted parameters. Hoist brake faults involve load-holding safety and require precise mechanical and electrical integration. A technician with FC 302 and hoist experience can perform load tests, measure brake torque, verify feedback logic, and certify the system meets local lifting equipment codes before returning the hoist to service.

## See Also

- [Danfoss FC302 ALARM 27 - Causes & Fix](/posts/danfoss-fc302-alarm-27-fault-code/)
- [Danfoss FC302 Alarm 40 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-40-fault-code/)
- [Danfoss FC302 ALARM 16 - Causes & Fix](/posts/danfoss-fc302-alarm-16-fault-code/)
- [Danfoss FC302 ALARM 25 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-25-fault-code/)
