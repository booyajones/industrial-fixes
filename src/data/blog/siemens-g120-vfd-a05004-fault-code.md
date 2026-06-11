---
title: "Siemens G120 A05004 Fault - Causes & Fix"
description: "A05004 warns that the G120's rectifier is overheating. Check cooling fans, verify all three supply phases, and reduce load to prevent shutdown."
pubDatetime: 2026-06-01T11:33:24Z
modDatetime: 2026-06-01T11:33:24Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - vfd
  - siemens
money_part: "Siemens G120 cooling fan assembly"
---

## Siemens G120 A05004 Fault — What It Means

A05004 is an alarm (not yet a trip fault) indicating that the incoming rectifier section of your Siemens SINAMICS G120 variable frequency drive has reached its overtemperature threshold. The rectifier converts incoming three-phase AC power to DC for the inverter stage, and elevated temperature means something is forcing it to work harder than its thermal design allows or cooling has been compromised. Siemens documentation notes that if the rectifier temperature climbs another 5 K from this point, the drive will escalate to fault F30037 and shut down to protect itself.

Because this is an alarm rather than a fault, the drive may still be running when you see A05004, giving you a window to diagnose and correct the issue before a full trip occurs. The root cause is almost always thermal: either the environment around the drive is too hot, cooling air is blocked or the fan has failed, the load profile is exceeding the drive's duty-cycle rating, one of the three incoming line phases is missing (forcing the remaining rectifier arms to carry extra current), or an internal rectifier component has degraded and is generating excess heat.

[Jump to Fix](#fix)

## Common Causes

- **Blocked airflow or high ambient temperature** Dust accumulation on heatsinks, obstructed vents, or an enclosure temperature above the drive's rated limit will prevent the rectifier from shedding heat.
- **Cooling fan failure** If the internal or external cooling fan has stopped or is running slowly, the rectifier cannot maintain safe operating temperature under load.
- **Missing incoming line phase** Loss of one phase at the supply (due to a blown fuse, loose connection, or contactor issue) forces the remaining rectifier diodes to carry the full load current, generating excess heat.
- **Excessive load or duty cycle** Running the drive continuously at or above its rated output, or cycling the motor too frequently, can thermally overload the rectifier section.
- **Defective rectifier arm** A failing diode or bridge component inside the power module will exhibit higher on-state voltage drop and heat generation even under normal load.

## Step-by-Step Fix {#fix}

1. {'lead': 'Acknowledge the alarm and record the ambient temperature', 'text': "Use the drive's keypad or software interface to clear the A05004 alarm, then measure the temperature of the air entering the drive and compare it to the operating limits in your G120 manual (typically 0–40 °C for most frame sizes)."}
2. {'lead': 'Inspect and restore cooling airflow', 'text': 'Power down the drive, open the enclosure if applicable, and check for dust buildup on heatsinks, blocked intake or exhaust vents, and proper spacing around the drive. Clean all surfaces with compressed air and verify that no obstructions remain.'}
3. {'lead': 'Test the cooling fan', 'text': 'With power restored, listen and visually confirm that the internal cooling fan is spinning at full speed. If the fan is silent, intermittent, or running slowly, replace the fan assembly before returning the drive to service.'}
4. {'lead': 'Verify all three incoming line phases', 'text': "Use a multimeter or phase-rotation meter at the drive's supply terminals to confirm balanced three-phase voltage on L1, L2, and L3. Check upstream fuses, contactors, and disconnect switches for any loose, burned, or open connections and repair as needed."}
5. {'lead': 'Review the load profile and duty cycle', 'text': "Compare the motor nameplate current and the application's run/stop pattern against the drive's continuous and overload ratings. If the drive is undersized or the duty cycle is too aggressive, either reduce the load or upgrade to a larger frame size."}
6. {'lead': 'Monitor rectifier temperature after restart', 'text': "Return the drive to normal operation and use the drive's parameter monitoring (often visible via the keypad or commissioning software) to watch the rectifier temperature in real time. If temperature climbs rapidly or the alarm reappears within minutes despite good cooling and balanced supply, suspect an internal rectifier defect."}
7. {'lead': 'Replace the power module if hardware fault is confirmed', 'text': 'If all external factors are correct but the alarm persists, the incoming rectifier section has likely degraded. Contact Siemens or an authorized service center to order and install a replacement power module matched to your G120 frame size and voltage rating.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05004-fault-code&k=Siemens+G120+cooling+fan+assembly&tag=errorcodefixes-20) \| Match the fan part number to your specific power module frame size and enclosure type. |
| Siemens G120 power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05004-fault-code&k=Siemens+G120+power+module&tag=errorcodefixes-20) \| Order by frame size (PM240, PM250, etc.) and voltage rating if internal rectifier damage is confirmed. |

## When to Call a Pro

Call a qualified electrician or drive technician if you are not comfortable working inside energized industrial electrical equipment, if you cannot safely verify three-phase supply voltage, or if the alarm returns immediately after you have confirmed good cooling and balanced line phases. Replacing a power module requires proper ESD precautions, correct torque on DC-bus and AC supply terminals, and verification of all parameter settings afterward. If your process cannot tolerate downtime for trial-and-error diagnosis, a Siemens-certified service partner with thermal imaging and power-quality test equipment can isolate the root cause in a single visit and carry the correct replacement module on the truck.

## See Also

- [Siemens Micromaster F0001 - Causes & Fix](/posts/siemens-micromaster-vfd-f0001-fault-code/)
- [Siemens Micromaster F0052 - Causes & Fix](/posts/siemens-micromaster-f0052-fault-code/)
- [Siemens G120 F0004 - Causes & Fix](/posts/siemens-g120-vfd-f0004-fault-code/)
- [Siemens Micromaster F0085 - Causes & Fix](/posts/siemens-micromaster-vfd-f0085-fault-code/)
