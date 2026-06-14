---
title: "ABB ACS580 A7EE Fault - Causes & Fix"
description: "A7EE on the ABB ACS580 means panel loss. The drive lost communication with the control panel or PC tool. Follow this repair guide."
pubDatetime: 2026-05-27T10:36:06Z
modDatetime: 2026-05-27T10:36:06Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control panel (keypad assembly)"
most_likely_cause: "Loose or unplugged control panel cable"
---

## ABB ACS580 A7EE Fault — What It Means

The A7EE fault code on an ABB ACS580 drive indicates panel loss. This means the drive has detected that the control panel or PC tool selected as the active control location has stopped communicating with the drive. This is not a motor or power problem. It is a communication interruption between the drive and the local HMI or computer interface.

[Jump to Fix](#fix)

## Common Causes

- **Loose or unplugged control panel cable** The connector between the panel and the drive has come loose or been disconnected.
- **Faulty panel mounting dock or adapter** If the panel mounts on a separate platform or base, the connection interface at that dock may have failed.
- **PC tool communication lost** Drive Composer or another PC tool was the active control location and the connection dropped.
- **Intermittent control board supply issue** A power or communication problem on the control board can cause repeated panel communication faults.
- **Damaged panel connector or control board port** Bent pins, contamination, or physical damage at the connection point prevents reliable communication.

## Step-by-Step Fix {#fix}

1. {'text': 'Check which device is the active control location. Confirm whether the fault refers to the local control panel or a connected PC tool.'}
2. {'text': 'Inspect the control panel connector at the drive. Remove and reseat the cable firmly, checking for bent pins, dirt, or poor retention.'}
3. {'text': 'Verify the mounting platform or dock connection if the panel is installed remotely. Reseat the panel in its base and confirm the dock contacts are clean.'}
4. {'text': 'Test PC tool connection if Drive Composer or another program is active. Open the software and verify the link to the drive is established.'}
5. {'text': 'Check parameter 95.04 (Control board supply) if panel communication problems persist. Look for anomalies in the control board voltage or supply status.'}
6. {'text': 'Reboot the control unit or cycle power to the drive. Many temporary panel-loss conditions clear after a full reset.'}
7. {'text': 'Replace the panel or control board if reseating and rebooting do not restore communication. Contact ABB service if the fault returns immediately after a successful reset.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control panel (keypad assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a7ee-fault-code&k=ABB+ACS580+control+panel+%28keypad+assembly%29&tag=errorcodefixes-20) \| Replacement HMI for drives with damaged or unresponsive panels. |
| Control panel cable and connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a7ee-fault-code&k=Control+panel+cable+and+connector&tag=errorcodefixes-20) \| Cable that links the panel to the drive's control board. |
| Panel mounting platform or dock | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a7ee-fault-code&k=Panel+mounting+platform+or+dock&tag=errorcodefixes-20) \| For remote installations where the panel plugs into a separate base. |
| ACS580 control board (control unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a7ee-fault-code&k=ACS580+control+board+%28control+unit%29&tag=errorcodefixes-20) \| Main logic board if panel supply or communication hardware has failed. |

## When to Call a Pro

Call a qualified drive technician or ABB service if the A7EE fault persists after reseating all connections and cycling power. If the panel drops out immediately after clearing the fault, the control board, panel hardware, or internal communication path likely has a defect that requires factory diagnostics. Also contact a professional if you are not familiar with parameter navigation or PC tool setup, or if your drive is still under warranty and you need to preserve support coverage.

## See Also

- [ABB ACS550 EFB 1 Fault - Causes & Fix](/posts/abb-acs550-efb-1-fault-code/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS550 EFB2 Fault Code - Causes & Fix](/posts/abb-acs550-efb2-fault-code/)
- [ABB ACS580 A2B4 Fault Code - Causes & Fix](/posts/abb-acs580-a2b4-fault-code/)
