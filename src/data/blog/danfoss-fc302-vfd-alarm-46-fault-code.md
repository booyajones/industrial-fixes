---
title: "Danfoss FC302 VFD Alarm 46 - Causes & Fix"
description: "Alarm 46 means power card supply voltage is out of range. Most often caused by a defective heat sink fan or clogged filters."
pubDatetime: 2026-06-03T10:52:04Z
modDatetime: 2026-06-03T10:52:04Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 heat sink fan"
most_likely_cause: "Defective heat sink fan"
---

## Danfoss FC302 VFD Alarm 46 — What It Means

Alarm 46 on the Danfoss VLT FC 302 means the internal power supply voltages on the power card are out of acceptable range. The drive monitors 24 V, 5 V, and ±18 V rails (or only 24 V and 5 V if powered by the optional 24 V DC supply). This alarm indicates the switch-mode power supply on the power card is not producing one or more of these rails within tolerance.

This is typically caused by an internal supply generation problem or a heat-related issue affecting the supply section, not by motor overload or output faults. Danfoss specifically calls out defective heat sink fans as a common contributor to this alarm.

[Jump to Fix](#fix)

## Common Causes

- **Defective heat sink fan** A failed or slowing fan causes overheating that pushes internal supply voltages out of range.
- **Clogged air filters** Blocked filters restrict cooling airflow and overheat the power card supply section.
- **High ambient temperature** Operating outside the rated temperature range stresses the internal power supply rails.
- **Defective power card** The switch-mode power supply section on the card itself has failed and cannot maintain voltage rails.
- **Defective control card or option card** A faulty control or add-on option card can load the monitored supplies beyond tolerance.
- **Missing or improper 24 V DC supply** If the drive uses the 24 V DC supply option, a weak or absent external supply triggers the alarm.

## Step-by-Step Fix {#fix}

1. **Power down the drive safely** and follow lockout/tagout procedures before opening the enclosure.
2. **Check the heat sink fan** by inspecting for rotation and listening for unusual noise, and replace the fan if it is not running or shows weak airflow.
3. **Inspect and clean air filters** to remove dust and debris that block cooling airflow through the drive.
4. **Verify ambient temperature** is within the drive's rated operating range and improve ventilation or enclosure cooling if necessary.
5. **Check the 24 V DC supply if equipped** by measuring the external supply voltage and confirming it is stable and within specification.
6. **Remove option cards one at a time** if installed, power up after each removal, and check if the alarm clears to isolate a faulty option.
7. **Replace the control card or power card** if all external causes are ruled out and the alarm persists, as the internal supply section has likely failed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 heat sink fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-46-fault-code&k=Danfoss+FC+302+heat+sink+fan&tag=errorcodefixes-20) \| Match the fan voltage and connector type to your specific frame size. |
| Danfoss FC 302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-46-fault-code&k=Danfoss+FC+302+power+card&tag=errorcodefixes-20) \| Order by drive frame size and voltage rating, typically requires factory or distributor support. |
| Danfoss FC 302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-46-fault-code&k=Danfoss+FC+302+control+card&tag=errorcodefixes-20) \| Confirm firmware version compatibility before ordering. |
| Air intake filter for Danfoss FC 302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-46-fault-code&k=Air+intake+filter+for+Danfoss+FC+302&tag=errorcodefixes-20) \| Check part number for your specific enclosure and mounting style. |

## When to Call a Pro

Call a qualified industrial electrician or VFD service technician if you are not trained in high-voltage equipment, if the alarm persists after cleaning filters and verifying the fan, or if you need to replace the power card or control card. Work inside the drive enclosure exposes you to lethal voltage even when input power is off, due to charged DC bus capacitors. Professional service includes proper discharge procedures, firmware backup, parameter transfer, and verification of internal supply rails with precision test equipment.

## See Also

- [Danfoss FC302 Alarm 14 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-14-fault-code/)
- [Danfoss FC302 VFD Alarm 29 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-29-fault-code/)
- [Danfoss FC302 ALARM 37 - Causes & Fix](/posts/danfoss-fc302-alarm-37-fault-code/)
- [Danfoss FC302 Alarm 58 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-58-fault-code/)
