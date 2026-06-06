---
title: "Danfoss FC302 Alarm 58 - Causes & Fix"
description: "Alarm 58 on a Danfoss FC302 VFD means AMA internal fault. The drive's Automatic Motor Adaptation failed internally. Contact Danfoss support."
pubDatetime: 2026-06-04T09:19:28Z
modDatetime: 2026-06-04T09:19:28Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 58 — What It Means

Alarm 58 on the Danfoss VLT AutomationDrive FC 302 is listed as **AMA Internal Fault**. AMA stands for Automatic Motor Adaptation, a routine the drive runs to learn motor parameters. This alarm means the adaptation procedure could not complete because of an internal fault inside the drive itself, not a simple motor overload or wiring problem. Danfoss groups Alarm 58 with other AMA failure codes (50 through 58) and treats it as a drive-side electronics issue rather than a field-adjustable fault.

Unlike many other alarms, Danfoss does not provide detailed field troubleshooting for Alarm 58. The manufacturer's official instruction is to contact your Danfoss supplier or authorized service center. This indicates the fault involves internal drive electronics or the control card, and field repair is not recommended without factory guidance.

[Jump to Fix](#fix)

## Common Causes

- **AMA routine triggered an internal drive fault** The Automatic Motor Adaptation process failed because of a problem inside the VFD hardware, not the motor or wiring.
- **Incorrect motor parameters entered for AMA** If motor nameplate data was entered wrong or the motor is unsuitable for adaptation, the drive may abort with an internal error.
- **Control card or internal electronics failure** The drive's internal control board or power section may have developed a fault that prevents AMA from completing.
- **Repeated AMA restart attempts** Running AMA multiple times without fixing the underlying issue can stress the drive and trigger internal protection.

## Step-by-Step Fix {#fix}

1. **Confirm the exact alarm number** on the FC 302 display and verify it is Alarm 58, not another code in the 50–58 AMA failure group.
2. **Stop any further AMA restart attempts.** Danfoss warns that repeated AMA runs can overheat the motor and stress the drive, especially for nearby alarms in this group.
3. **Record the alarm details** including any trip history, motor nameplate data entered in parameters, and the context in which AMA was started (commissioning or routine operation).
4. **Check motor parameter setup** in the drive's configuration menu and compare the entered nameplate values (voltage, current, speed, power) with the actual motor plate to confirm accuracy.
5. **Power down the drive completely** and inspect control card seating, connections, and any visible signs of component damage or overheating on internal boards if you have access.
6. **Contact your Danfoss supplier or authorized service center** with the recorded alarm information. Danfoss's official action for Alarm 58 is to escalate to factory support rather than attempt field repair.
7. **Follow supplier instructions** for any firmware updates, parameter resets, or component replacement they recommend based on drive diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-58-fault-code&k=Danfoss+FC+302+control+card&tag=errorcodefixes-20) \| Likely suspect for AMA internal faults, but confirm part number with Danfoss service before ordering. |
| Danfoss FC 302 power section | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-58-fault-code&k=Danfoss+FC+302+power+section&tag=errorcodefixes-20) \| May be involved in internal AMA failures. Consult Danfoss supplier to verify the exact failing module for your frame size. |

## When to Call a Pro

Call a Danfoss authorized service technician or your drive supplier immediately for Alarm 58. This is an internal drive fault that Danfoss does not publish detailed field repair procedures for, and the manufacturer explicitly directs users to contact support rather than attempt troubleshooting on their own. A qualified VFD technician with Danfoss training can run diagnostic routines, check internal hardware, and access service bulletins not available to general users. Attempting to swap control cards or power modules without proper guidance risks further damage and may void warranty coverage.
