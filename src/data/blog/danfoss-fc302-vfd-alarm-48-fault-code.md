---
title: "Danfoss FC302 Alarm 48 - Causes & Fix"
description: "Alarm 48 on Danfoss FC302 means the 1.8 V control-card supply is out of spec. Most often a defective control card is the fix."
pubDatetime: 2026-06-03T10:53:14Z
modDatetime: 2026-06-03T10:53:14Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 control card (control PCB)"
---

## Danfoss FC302 Alarm 48 — What It Means

Alarm 48 (WARNING 48, 1.8 V supply low) on a Danfoss VLT FC 302 indicates that the drive has detected the 1.8 V DC supply on the control card is outside allowable limits. This is an internal electronics problem, not a motor or load issue. Danfoss troubleshooting points directly to the control card as the primary suspect, with option card overvoltage as a secondary contributor if an option card is installed.

The 1.8 V rail powers critical control-card circuitry. When it drops or becomes unstable, the drive cannot safely regulate itself and throws this warning. Field repair focuses on replacing the control card rather than component-level board repair, because the 1.8 V supply circuitry is integrated into the card assembly.

[Jump to Fix](#fix)

## Common Causes

- **Defective control card** The 1.8 V supply circuit on the control card has failed or degraded, and Danfoss identifies this as the primary cause for Alarm 48.
- **Option card overvoltage** An installed option card feeding abnormal voltage back to the control card can pull the 1.8 V rail out of spec.
- **Loose or corroded control-card connector** Poor contact at the control-card connector can interrupt the 1.8 V supply path and trigger the low-voltage alarm.
- **Contamination or moisture on the control card** Dust, conductive debris, or humidity can create leakage paths that load down the 1.8 V rail below threshold.
- **Internal power-supply fault** A fault in the drive's internal DC supply section that feeds the control card can starve the 1.8 V regulator.

## Step-by-Step Fix {#fix}

1. **Disconnect all power** to the VFD and follow lockout/tagout procedures before opening any covers or touching internal components.
2. **Open the drive enclosure** and locate the control card (the main logic board, typically mounted in the upper section of the FC 302).
3. **Inspect the control card and connectors** for obvious damage, burn marks, corrosion, loose ribbon cables, or contamination on the board surface.
4. **Check for installed option cards** and verify connections. If an option card is present, remove it temporarily and attempt to clear the alarm to rule out option-card overvoltage.
5. **Measure the 1.8 V supply** at the control-card test points (if accessible and you have the technical datasheet). If the reading is significantly below 1.8 V, the control card is defective.
6. **Replace the control card** with a genuine Danfoss FC 302 control PCB. Transfer any configuration backup or re-program drive parameters after installation.
7. **Power up the drive** and monitor for Alarm 48. If the fault clears and the 1.8 V supply is stable, the repair is complete. If the alarm persists, inspect the main power-supply section and contact Danfoss technical support for deeper diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 control card (control PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-48-fault-code&k=Danfoss+FC+302+control+card+%28control+PCB%29&tag=errorcodefixes-20) \| Main logic board for the FC 302. Verify your exact drive model and firmware revision before ordering. |
| Option card (if installed) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-48-fault-code&k=Option+card+%28if+installed%29&tag=errorcodefixes-20) \| Only if the installed option card is found defective or causing overvoltage during testing. |

## When to Call a Pro

Call a qualified VFD technician or contact Danfoss technical support if you are not comfortable working inside energized or recently de-energized industrial drives, if you do not have the tools to measure low-voltage DC supplies safely, or if replacing the control card does not clear Alarm 48. Control-card replacement requires proper ESD handling, parameter backup, and sometimes firmware/configuration tools. If the drive is under warranty or part of a critical process line, professional service ensures you preserve warranty coverage and minimize downtime.

## See Also

- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-alarm-32-fault-code/)
- [Danfoss FC302 Alarm 40 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-40-fault-code/)
- [Danfoss AKC Controller Fault Codes - Complete Guide](/posts/danfoss-akc-controller-fault/)
- [Danfoss FC302 VFD Alarm 28 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-28-fault-code/)
