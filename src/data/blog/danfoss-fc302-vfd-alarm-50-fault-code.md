---
title: "Danfoss FC302 Alarm 50 - Causes & Fix"
description: "Alarm 50 on a Danfoss FC302 VFD means AMA calibration failed. Usually caused by incorrect motor data or wiring problems."
pubDatetime: 2026-06-04T09:13:34Z
modDatetime: 2026-06-04T09:13:34Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control card"
---

## Danfoss FC302 Alarm 50 — What It Means

Alarm 50 on the Danfoss VLT AutomationDrive FC 302 means the Automatic Motor Adaptation (AMA) calibration failed. The drive tried to identify and tune itself to your motor but could not complete the process. This is different from a terminal 50 power supply warning. The drive is telling you it cannot finish the motor identification routine.

This alarm typically appears during commissioning or after a motor change when you attempt to run AMA. The drive needs accurate motor information and a good electrical connection to the motor in order to complete the tuning process. If those conditions are not met, the calibration stops and throws Alarm 50.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor nameplate data in parameters** Parameters 1-20 through 1-25 do not match the actual motor nameplate values, so the drive cannot complete the identification routine.
- **Loose or incorrect motor wiring** Connections at the drive output terminals or motor junction box are loose, corroded, or incorrectly phased, preventing AMA from reading the motor properly.
- **Motor circuit fault or open winding** The motor itself has a broken winding, high resistance, or internal fault that stops the calibration process.
- **Mechanically locked or improperly coupled motor** The motor shaft is jammed, heavily loaded, or the coupling prevents free rotation during the AMA test.
- **Drive control board issue** If all motor data and wiring are correct but AMA still fails repeatedly, the drive's internal control section may have a fault.

## Step-by-Step Fix {#fix}

1. **Stop the drive and acknowledge Alarm 50** on the control panel or keypad to clear the active fault state.
2. **Verify the motor nameplate** and compare every value (voltage, current, power, speed, frequency) against parameters 1-20 through 1-25 in the drive programming.
3. **Correct any mismatched motor data** in the drive parameters and save the changes before attempting AMA again.
4. **Inspect all motor wiring** from the drive output terminals to the motor junction box for tight connections, correct phase sequence (U-V-W), and any signs of damage or corrosion.
5. **Check that the motor shaft turns freely** by hand (with power off and the drive locked out) and that no mechanical binding or excessive load is present.
6. **Restart the AMA calibration** from the drive menu (typically parameter 1-29) and observe whether the process completes without returning Alarm 50.
7. **Contact Danfoss service or your supplier** if the alarm persists after confirming correct motor data and wiring, as the drive may require factory-level diagnostics or component replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-50-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Only if Danfoss service confirms internal drive fault after all field checks pass. |
| Motor terminal lugs and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-50-fault-code&k=Motor+terminal+lugs+and+connectors&tag=errorcodefixes-20) \| Replace corroded or damaged motor cable terminations found during wiring inspection. |

## When to Call a Pro

Call a qualified drive technician or Danfoss service if Alarm 50 returns after you have verified and corrected all motor nameplate data in parameters 1-20 through 1-25 and inspected the motor wiring for faults. Danfoss does not publish a deeper field repair procedure for this alarm and directs users to contact their supplier or service department when the fault persists. If you are not familiar with VFD programming or safe electrical work on industrial motor circuits, call a professional from the start to avoid damage to the drive or motor.

## See Also

- [Danfoss FC302 Alarm 42 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-42-fault-code/)
- [Danfoss FC302 VFD Alarm 28 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-28-fault-code/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC302 Alarm 40 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-40-fault-code/)
