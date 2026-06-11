---
title: "Danfoss FC302 ALARM 16 - Causes & Fix"
description: "ALARM 16 on a Danfoss FC302 VLT drive signals a line-to-line short circuit in the motor or motor cable. Step-by-step repair guide."
pubDatetime: 2026-05-29T09:41:07Z
modDatetime: 2026-05-29T09:41:07Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor cable (shielded VFD-rated)"
---

## Danfoss FC302 ALARM 16 — What It Means

ALARM 16 on the Danfoss VLT AutomationDrive FC 302 (and FC 301) means the drive has detected a short circuit between output phases on the motor side. The drive trips to protect its power section from damage caused by phase-to-phase contact in the motor winding or motor cabling.

This fault does not point to an overload or ground fault. It specifically indicates that two or more output phases are shorted together, either in the motor cable insulation, inside the motor windings, or in rare cases within the drive's own inverter section.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable insulation** Cuts, crushing, or abrasion in the motor cable allow phase conductors to touch, creating a phase-to-phase short.
- **Shorted motor winding** Internal insulation failure inside the motor causes windings to short together.
- **Loose or burnt motor terminal connections** Arcing or heat at the motor terminal box can carbonize insulation and bridge phases.
- **Contaminated motor terminal box** Water, metal debris, or conductive dust inside the motor junction box creates a path between phases.
- **Drive power section fault** If the alarm persists with the motor disconnected, the drive's internal inverter or IGBT section may have failed.

## Step-by-Step Fix {#fix}

1. **Lock out and isolate all power** to the drive before beginning any inspection or testing, because hazardous voltage remains inside the drive even after mains are removed.
2. **Disconnect the motor leads** from the drive output terminals (U, V, W) and clear the alarm. Attempt a no-load power-up to see if ALARM 16 reappears.
3. **If the alarm clears with the motor disconnected**, inspect the motor cable for visible damage, pinch points, cuts, or burnt spots. Test the cable with a multimeter on resistance mode to check for continuity between phases (should be open circuit).
4. **Test motor winding insulation** using a megohmmeter. Measure phase-to-phase resistance and phase-to-ground resistance. Low readings indicate winding or insulation failure inside the motor.
5. **If the motor and cable test good**, the fault is likely internal to the drive. Inspect the drive's power board and inverter section for burn marks, swollen components, or signs of IGBT failure.
6. **Replace the damaged component** identified (motor cable, motor, or drive power section) and reassemble all connections securely.
7. **Reconnect the motor**, restore power under controlled conditions, and perform a test run to confirm ALARM 16 does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-16-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Replace if insulation is damaged or phase-to-phase short is found in the cable. |
| Three-phase motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-16-fault-code&k=Three-phase+motor&tag=errorcodefixes-20) \| Required if winding insulation has failed or internal short is confirmed by megohmmeter test. |
| Drive power board / inverter section | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-16-fault-code&k=Drive+power+board+%2F+inverter+section&tag=errorcodefixes-20) \| Needed if ALARM 16 persists with motor disconnected. Often replaced as a complete assembly. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not trained in high-voltage troubleshooting or do not have the tools to perform insulation testing. Internal drive faults require board-level diagnostics and parts that are typically available only through Danfoss service channels. If you have replaced the motor cable and motor but the alarm continues, the drive's power section likely needs professional repair or replacement.

## See Also

- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
- [Danfoss FC302 Alarm 21 - Causes & Fix](/posts/danfoss-fc302-alarm-21-fault-code/)
- [Danfoss AKC Controller Fault Codes - Complete Guide](/posts/danfoss-akc-controller-fault/)
- [Danfoss FC302 Alarm 17 - Causes & Fix](/posts/danfoss-fc302-alarm-17-fault-code/)
