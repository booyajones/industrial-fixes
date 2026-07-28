---
title: "Danfoss FC302 ALARM 35 - Causes & Fix"
description: "ALARM 35 on a Danfoss FC302 means an option fault. Learn the 5 most common causes and the step-by-step repair procedure."
pubDatetime: 2026-05-29T09:50:09Z
modDatetime: 2026-05-29T09:50:09Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss VLT Sensor Input Option module"
most_likely_cause: "Incorrectly seated or loose option module"
---

## What this code means
ALARM 35 on a Danfoss VLT FC302 indicates an option fault, meaning the drive has detected a problem with an installed accessory module or option card, not a motor or mains power issue. This fault is tied specifically to optional add-on components such as the Sensor Input Option, Programmable I/O Option, or other interface modules fitted to the drive's control section.

The alarm typically appears when the drive cannot communicate with the option module during power-up, detects an initialization failure, or finds incompatibility between the option and the drive configuration. Because this is an option-specific fault, the motor and process equipment are usually not the root cause unless the option itself is a sensor interface monitoring that process.

## Common Causes

- **Incorrectly seated or loose option module** The accessory card is not fully inserted into its slot, or the connector is partially detached, preventing communication with the drive.
- **Failed or damaged option card** The option module itself has failed due to age, electrical stress, or physical damage such as bent pins or corrosion on the connector.
- **Power-up or initialization problem** The option module does not initialize correctly when the drive powers on, often due to intermittent supply voltage or internal option firmware issues.
- **Communication fault between option and drive** The internal data bus or wiring between the option card and the drive's control board is interrupted or corrupted.
- **Incompatible or misconfigured option** The installed option module is not compatible with the FC302 model or firmware version, or drive parameters are set incorrectly for the installed option type.

## Step-by-Step Fix {#fix}

1. **Safely power down** the FC302 drive following lockout/tagout procedures and allow at least five minutes for internal capacitors to discharge before opening the drive enclosure.
2. **Identify the installed option module** by inspecting the control section and recording the option card part number and type (such as Sensor Input Option or Programmable I/O Option).
3. **Remove and reseat the option module** by carefully pulling it from its slot, inspecting the connector for bent pins, corrosion, or debris, then firmly reinserting it until it locks into place.
4. **Inspect all cables and connectors** associated with the option card, checking for loose wiring, damaged insulation, or poor terminal connections, and tighten or replace as needed.
5. **Restore power and clear the alarm** through the drive's control panel, then monitor the display during startup to see if ALARM 35 reappears immediately or after a delay.
6. **Verify option compatibility** by cross-referencing the option card part number with the FC302 model and firmware version in the Danfoss instruction manual or programming guide.
7. **Swap in a known-good option module** if the alarm persists after reseating and inspection, or contact Danfoss technical support if no spare module is available for testing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss VLT Sensor Input Option module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-35-fault-code&k=Danfoss+VLT+Sensor+Input+Option+module&tag=errorcodefixes-20) \| Replacement option card for sensor interface functions, verify part number matches your FC302 model. |
| Danfoss VLT Programmable I/O Option module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-35-fault-code&k=Danfoss+VLT+Programmable+I%2FO+Option+module&tag=errorcodefixes-20) \| Replacement programmable input/output option card, confirm compatibility with drive firmware version. |
| FC302 control board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-35-fault-code&k=FC302+control+board+assembly&tag=errorcodefixes-20) \| Required only if the option interface circuitry on the main control board is damaged, confirm by substitution testing first. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss-authorized service provider if reseating the option module and inspecting connectors does not clear ALARM 35, if you do not have a spare option card for substitution testing, or if the alarm returns immediately after each power cycle. Also seek professional help if you are not trained in lockout/tagout procedures or working inside energized VFD enclosures, or if the drive shows additional alarms or erratic behavior that suggests damage to the control board or internal data bus.
