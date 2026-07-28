---
title: "Siemens Micromaster F0071 - Causes & Fix"
description: "F0071 means USS setpoint fault: the drive lost communication with its USS master. Check the master device and wiring first."
pubDatetime: 2026-06-02T10:38:55Z
modDatetime: 2026-06-02T10:38:55Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens USS master or BOP-link master"
most_likely_cause: "Master device not sending telegrams"
---

## What this code means
F0071 on a Siemens Micromaster is a USS (BOP-link) setpoint fault. The drive did not receive valid setpoint data from the USS master during the telegram off time, so it tripped on OFF2. This is a communication or setpoint-loss fault on the USS link, not a motor overload or power-stage problem. The drive was expecting cyclic USS communication and stopped getting it in time, so the setpoint source was effectively lost.

Siemens documents this fault as 'No setpoint values from USS during telegram off time' and lists the remedy as 'Check USS master.' The fault occurs when the drive is configured to receive its control setpoint over the USS communication link (often from a PLC, HMI, or BOP-link master) and that data stream stops arriving.

## Common Causes

- **Master device not sending telegrams** The PLC, HMI, BOP-link master, or other USS master is offline, powered off, or not transmitting telegrams on time.
- **Loose or damaged communications wiring** The wiring or connectors on the USS link or BOP-link path are loose, broken, corroded, or miswired.
- **Wrong master or drive configuration** The master is not addressing the drive correctly, not enabled, or the drive is not configured to expect USS setpoint data.
- **Failed communications board or interface** The interface board or communications module on the drive or master has failed or is not seated correctly.
- **Incorrect USS protocol settings** Baud rate, address, or telegram format settings do not match between the master and the drive.

## Step-by-Step Fix {#fix}

1. **Confirm the fault code** on the drive display and verify that it is F0071.
2. **Identify the active control source** and confirm the drive is configured to receive setpoint data over USS or BOP-link.
3. **Check the master device first** (PLC, HMI, or BOP-link master) because Siemens explicitly lists 'Check USS master' as the remedy. Verify the master is powered, online, and actively sending telegrams.
4. **Inspect all communications wiring and connectors** on the USS or BOP-link path for looseness, damage, incorrect pinout, or missing termination.
5. **Check the communications board or interface** if the installation uses one. Reseat or replace the board if needed.
6. **Verify USS protocol settings** on both the master and the drive, including baud rate, device address, and telegram format, and correct any mismatches.
7. **Clear the fault** after the communications issue is corrected by power cycling the drive, pressing the reset key on the BOP or AOP, or using a digital input reset if configured. If the fault returns, substitute the master or interface hardware to isolate a failed component.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens USS master or BOP-link master | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0071-fault-code&k=Siemens+USS+master+or+BOP-link+master&tag=errorcodefixes-20) \| If the master device is proven faulty or not transmitting correctly. |
| Siemens Micromaster communications board or interface module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0071-fault-code&k=Siemens+Micromaster+communications+board+or+interface+module&tag=errorcodefixes-20) \| If the communications board is damaged, unseated, or failed. Match the board to your exact drive model. |
| USS communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0071-fault-code&k=USS+communication+cable&tag=errorcodefixes-20) \| Shielded twisted-pair cable for the USS link, if the existing cable is damaged or does not meet the wiring specification. |

## When to Call a Pro

Call a qualified technician or automation specialist if you are not familiar with industrial communication protocols or if the fault persists after verifying wiring, master status, and communications board condition. F0071 is a communication fault, so troubleshooting requires understanding the USS protocol, the master device configuration, and the drive's control source settings. If the master is part of a larger PLC or SCADA system, involve the system integrator or controls engineer to diagnose the master side of the link.
