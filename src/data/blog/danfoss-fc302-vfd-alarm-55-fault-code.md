---
title: "Danfoss FC302 Alarm 55 - Causes & Fix"
description: "Alarm 55 on a Danfoss FC302 VFD means AMA parameter out of range. Fix by verifying motor nameplate data matches drive settings."
pubDatetime: 2026-06-04T09:17:27Z
modDatetime: 2026-06-04T09:17:27Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 55 — What It Means

Alarm 55 on a Danfoss VLT AutomationDrive FC 302 means "AMA parameter out of range." AMA stands for Automatic Motor Adaptation, the drive's auto-tuning routine. This alarm appears when the motor data you entered for the AMA routine fall outside the acceptable range the drive can work with, so the drive will not complete auto-tuning.

This is a configuration and motor data validity alarm, not a hardware power-stage failure. The drive is telling you that the motor nameplate values programmed into the motor parameter set do not match what the AMA routine can accept for that drive size. The most common fix is to double-check the motor nameplate against the values you entered and correct any mismatches.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor nameplate data entered** You entered motor voltage, current, power, or speed values that do not match the motor nameplate or are outside the range the AMA routine supports.
- **Motor rating outside AMA's supported range** The motor is too large or too small for the drive size, creating a mismatch that prevents the auto-tune routine from running properly.
- **Wrong motor connection method** You selected delta or wye configuration in the drive parameters that does not match the actual motor wiring, making the programmed data invalid for adaptation.
- **Improper motor wiring** Motor leads are miswired or a phase is open or shorted, leading to invalid parameter conditions when the drive attempts to validate the setup.
- **Parameter set corruption or previous bad AMA run** A prior incomplete or failed AMA attempt left the drive in a state where the motor parameters are now out of range and the drive will not retry until you correct the values.

## Step-by-Step Fix {#fix}

1. **Compare motor nameplate to drive parameters.** Read the voltage, current, power, frequency, and speed from the motor nameplate and compare each value to the motor parameter set in the drive (typically parameters 1-20 through 1-29). Correct any mismatches.
2. **Check motor size against drive rating.** Confirm the motor horsepower or kilowatt rating falls within the range the drive model can handle. Consult the FC 302 installation guide for the min and max motor sizes your drive frame supports for AMA.
3. **Verify motor wiring and connection method.** Inspect the motor terminal box to confirm the wiring matches the delta or wye configuration you selected in the drive. Look for loose connections, swapped phases, or damaged leads.
4. **Correct the motor parameter values.** Enter the accurate nameplate data into the drive and set the motor connection type to match the actual wiring. Save the changes.
5. **Power-cycle the drive.** Disconnect mains power, wait 30 seconds, and re-energize the drive to clear any internal state left from the previous alarm.
6. **Rerun AMA.** Navigate to the AMA menu in the drive and start the Automatic Motor Adaptation routine. The drive should now accept the corrected parameters and complete auto-tuning.
7. **If the alarm persists, recheck motor and drive pairing.** Double-check that the motor is compatible with the drive size and that all nameplate data are entered correctly. If the alarm continues after verified data and correct wiring, consult the FC 302 design guide or contact Danfoss technical support, because Alarm 55 is a setup validation issue rather than a failed power component.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor terminal leads and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-55-fault-code&k=Motor+terminal+leads+and+connectors&tag=errorcodefixes-20) \| Replace if damaged, corroded, or causing intermittent connection that invalidates motor data during AMA. |
| Motor nameplate label or datasheet | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-55-fault-code&k=Motor+nameplate+label+or+datasheet&tag=errorcodefixes-20) \| Obtain from the motor manufacturer if the original nameplate is missing or unreadable, so you can enter accurate motor parameters. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are unsure how to read the motor nameplate or navigate the FC 302 parameter menus, or if the alarm returns after you have verified all motor data and wiring. Because Alarm 55 is a configuration and motor-data validation issue rather than a hardware fault, a technician will use Danfoss software tools to inspect the full parameter set and confirm the motor and drive are correctly paired. If the drive continues to reject AMA with correct data, the technician will check for deeper wiring faults or consult Danfoss support for factory assistance.
