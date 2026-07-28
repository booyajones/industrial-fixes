---
title: "Danfoss FC302 Alarm 52 - AMA Low Inom Causes & Fix"
description: "Alarm 52 means motor current is too low during Automatic Motor Adaptation. Check parameter 1-24 Motor Current against nameplate data."
pubDatetime: 2026-06-04T09:15:01Z
modDatetime: 2026-06-04T09:15:01Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss VLT programming software (MCT 10)"
most_likely_cause: "Incorrect parameter 1-24 Motor Current entry"
---

## What this code means
Alarm 52 on the Danfoss VLT AutomationDrive FC 302 is labeled "AMA low Inom." This fault occurs specifically during the Automatic Motor Adaptation (AMA) procedure, not during normal drive operation. The drive has detected that the motor current is too low for the adaptation routine to complete successfully. This is almost always a configuration issue rather than a hardware failure. The drive cannot complete AMA because the current value does not match what the adaptation algorithm expects based on the parameters you entered.

## Common Causes

- **Incorrect parameter 1-24 Motor Current entry** The motor current value entered in parameter 1-24 does not match the actual motor nameplate current rating, causing AMA to fail.
- **Wrong motor nameplate data in setup parameters** Other motor setup parameters (voltage, power, frequency) are incorrect, which throws off the AMA current expectations.
- **Motor genuinely too small for drive** The connected motor current is far below the range the drive expects for AMA, making automatic adaptation unsuitable for this pairing.
- **Motor wiring or terminal problem** Loose connections, missing phase, or incorrect wiring configuration can cause the drive to measure current lower than expected during AMA.
- **AMA attempted on unsuitable motor type** The motor is not compatible with AMA (special winding, unusual construction), so the routine cannot measure current properly.
- **Motor disconnected or not coupled** The motor is not mechanically or electrically connected as expected, so the drive sees very low or zero current during the adaptation test.

## Step-by-Step Fix {#fix}

1. {'lead': 'Confirm the alarm occurs during AMA only.', 'text': 'Verify that Alarm 52 appears when you run Automatic Motor Adaptation, not during normal drive operation, to confirm the diagnosis.'}
2. {'lead': 'Locate the motor nameplate.', 'text': 'Read the motor nameplate and write down the rated current (full-load amps), voltage, frequency, power, and speed.'}
3. {'lead': 'Check parameter 1-24 Motor Current.', 'text': 'Navigate to parameter 1-24 in the drive menu and compare the entered value to the nameplate rated current, then correct if wrong.'}
4. {'lead': 'Verify all motor setup parameters.', 'text': 'Inspect the other motor data parameters (voltage, power, frequency) and correct any that do not match the motor nameplate exactly.'}
5. {'lead': 'Inspect motor wiring and terminals.', 'text': 'Check that all three phases are tightly connected at the drive output and motor terminal box, and confirm correct phase sequence.'}
6. {'lead': 'Re-run AMA after corrections.', 'text': 'Reset the alarm, save corrected parameters, and initiate AMA again to see if the drive completes adaptation without fault.'}
7. {'lead': 'Use manual commissioning if AMA still fails.', 'text': 'If the motor is unsuitable for AMA or the fault persists with correct data, skip AMA and commission the drive using manual motor parameter entry instead.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss VLT programming software (MCT 10) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-52-fault-code&k=Danfoss+VLT+programming+software+%28MCT+10%29&tag=errorcodefixes-20) \| Optional PC tool for easier parameter entry and backup of drive settings during commissioning. |
| Motor nameplate data label | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-52-fault-code&k=Motor+nameplate+data+label&tag=errorcodefixes-20) \| Not a part to buy, but photograph or record all motor nameplate data before making any parameter changes. |

## When to Call a Pro

Call a qualified drive technician or motor specialist if you have verified all motor nameplate data matches the drive parameters and the alarm still appears during AMA. Also get help if you are unsure which motor parameters to enter, if the motor has unusual construction (special windings, high-slip design), or if the drive and motor sizes seem mismatched. A technician can measure actual motor current with a clamp meter during a manual start, confirm the motor is wired correctly, and choose the best commissioning method for your application. Because Alarm 52 is configuration-related and not a hardware fault, professional help usually means getting the setup right rather than replacing parts.
