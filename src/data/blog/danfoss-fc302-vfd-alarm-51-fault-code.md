---
title: "Danfoss FC302 Alarm 51 - Causes & Fix"
description: "Alarm 51 on Danfoss FC302 means AMA motor data check failed. Fix: verify motor voltage, current, power in parameters 1-20 to 1-25."
pubDatetime: 2026-06-04T09:14:06Z
modDatetime: 2026-06-04T09:14:06Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 programming cable or software"
---

## Danfoss FC302 Alarm 51 — What It Means

Alarm 51 on the Danfoss VLT AutomationDrive FC 302 indicates that the Automatic Motor Adaptation (AMA) procedure could not validate the motor's nominal electrical data. Specifically, the drive failed its check for Unom (motor rated voltage) and Inom (motor rated current). Danfoss identifies this fault as 'AMA check Unom and Inom' and attributes it to incorrect motor voltage, motor current, or motor power settings entered into the drive.

This alarm is almost always a configuration problem rather than a hardware failure. The drive cannot complete its self-tuning routine because the motor data you entered do not match the actual motor connected to it. The fix involves verifying and correcting the motor nameplate information in the drive's programming before running AMA again.

[Jump to Fix](#fix)

## Common Causes

- **Wrong motor voltage entered** The motor rated voltage in parameter 1-23 does not match the actual nameplate voltage on your motor.
- **Incorrect motor current setting** The motor rated current in parameter 1-24 is entered incorrectly or does not correspond to the motor's actual nameplate rating.
- **Motor power rating mismatch** The motor power entered in parameter 1-20 is wrong or inconsistent with the motor's actual power rating.
- **Nameplate data transcription error** Data from the motor nameplate was copied incorrectly into the drive during initial setup or commissioning.
- **AMA run without updating motor data** You ran Automatic Motor Adaptation after swapping motors but did not update parameters 1-20 through 1-25 with the new motor's specifications.
- **Motor incompatible with AMA procedure** The connected motor type or characteristics are not suitable for the drive's auto-tuning routine even though data entry is correct.

## Step-by-Step Fix {#fix}

1. **Locate the motor nameplate** on your connected motor and write down the exact values for rated voltage, rated current, rated power, rated frequency, and rated speed.
2. **Access parameters 1-20 through 1-25** on the FC302 front panel or via the programming software and compare each setting to your motor nameplate data.
3. **Correct any mismatches** by entering the exact motor nameplate values into the corresponding parameters (1-20 for motor power, 1-23 for motor voltage, 1-24 for motor current, and so on).
4. **Save the updated parameters** and power cycle the drive or reset the alarm to clear the fault code from memory.
5. **Rerun the Automatic Motor Adaptation** procedure from the drive's setup menu now that the motor data are correct.
6. **Monitor the AMA process** to confirm it completes without triggering Alarm 51 again.
7. **If the alarm persists after correct data entry**, double-check motor wiring and connections to confirm the motor is properly connected and that no wiring errors exist that would prevent AMA from reading correct electrical characteristics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 programming cable or software | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-51-fault-code&k=Danfoss+FC302+programming+cable+or+software&tag=errorcodefixes-20) \| For easier parameter editing if the keypad interface is difficult to use. |
| Motor nameplate label or documentation | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-51-fault-code&k=Motor+nameplate+label+or+documentation&tag=errorcodefixes-20) \| Replacement label if the original is damaged or illegible and you need the manufacturer's motor data. |

## When to Call a Pro

Call a qualified technician or control systems integrator if you have verified and corrected all motor data in parameters 1-20 to 1-25 and the alarm still appears after rerunning AMA. Persistent Alarm 51 after correct data entry may indicate a wiring problem, a motor issue that prevents adaptation, or an unusual drive configuration that requires deeper diagnostic tools. Also call a professional if you are unfamiliar with VFD programming or motor nameplate interpretation, since incorrect settings can damage both the drive and the motor.
