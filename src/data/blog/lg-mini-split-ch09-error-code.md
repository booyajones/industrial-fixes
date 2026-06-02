---
title: "LG Mini Split CH09 Error Code - Causes & Fix"
description: "CH09 means outdoor fan problem on most LG splits or indoor EEPROM error on Multi V. Check fan motor connections and spin resistance first."
pubDatetime: 2026-05-31T01:39:39Z
modDatetime: 2026-05-31T01:39:39Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - lg
---

## LG Mini Split CH09 Error Code — What It Means

CH09 is not a single universal fault across all LG mini split systems. On standard LG split air conditioners, CH09 indicates an outdoor unit fan problem. The outdoor fan motor is either unplugged, mechanically seized, electrically failed, or not receiving the correct drive signal from the outdoor PCB. On LG Multi V systems and some indoor unit contexts, CH09 is reported as an indoor unit EEPROM memory error, pointing to a failure in the control board's memory circuit or corrupted data.

Because the same code can mean two very different things depending on your system, the first step is to confirm whether you have a standard split or a Multi V setup and whether the fault is logged on the outdoor or indoor unit. For typical residential mini splits, treat CH09 as an outdoor fan circuit issue. For commercial or multi-zone Multi V installations, expect an indoor PCB memory fault.

[Jump to Fix](#fix)

## Common Causes

- **Outdoor fan motor unplugged or connector loose** The fan motor plug at the outdoor PCB or motor body is not fully seated, breaking the electrical circuit.
- **Fan motor mechanically seized** Bearings have failed or debris is blocking the fan, preventing it from spinning freely by hand.
- **Fan motor electrically failed** The motor windings are open or shorted, so it cannot run even when voltage is applied.
- **Faulty outdoor PCB or inverter control** The board is not sending the correct AC drive voltage to the fan motor, even though the motor itself is good.
- **Damaged wiring harness between PCB and fan motor** Wires are pinched, corroded, or cut, interrupting the signal or power to the motor.
- **Indoor EPROM or EEPROM failure (Multi V / indoor variant)** The memory IC on the indoor PCB is corrupted, damaged, or has lost its checksum, triggering a memory error instead of a fan fault.

## Step-by-Step Fix {#fix}

1. **Confirm your system type and fault location.** Check whether you have a standard LG split or a Multi V system, and read the service display or remote to see if the fault is logged on the outdoor or indoor unit.
2. **For split systems, inspect the outdoor fan motor connector.** Open the outdoor unit, locate the fan motor plug on the PCB, and push it firmly to reseat it. Check the harness for any visible damage or corrosion.
3. **Test the fan motor for mechanical freedom.** With power off, spin the outdoor fan blade by hand. It should rotate smoothly with no grinding, catching, or complete seizure. If it binds, the motor bearings or blade assembly is damaged.
4. **Measure the voltage supplied to the fan motor.** With the unit attempting to run, use a multimeter to check the AC voltage at the fan motor terminals. LG references show it can range from 120 V AC at low speed to 170 V AC at high speed. No voltage or wildly incorrect voltage points to a bad outdoor PCB.
5. **Replace the outdoor fan motor if it is electrically or mechanically bad.** If voltage is present but the motor will not run, or if it is seized and cannot be freed, swap in a new fan motor for your model.
6. **Replace the outdoor PCB if the motor is good but voltage is absent.** When the fan spins freely, tests electrically sound, but the board delivers no drive signal, the PCB or inverter module has failed.
7. **For Multi V / EEPROM variant, check the indoor PCB.** Verify the CN_OPTION connector is fully seated, inspect solder joints and the board for physical damage, and replace the indoor main PCB or EEPROM IC if memory corruption is confirmed. Run Auto Addressing after any PCB replacement if your platform requires it.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch09-error-code&k=Outdoor+fan+motor&tag=errorcodefixes-20) \| Match to your exact model number and voltage. Required when the motor is seized, shorted, or open. |
| Outdoor PCB / inverter control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch09-error-code&k=Outdoor+PCB+%2F+inverter+control+board&tag=errorcodefixes-20) \| Model-specific. Needed when the board fails to drive the fan motor despite a good motor. |
| Indoor main PCB or EEPROM PCB (Multi V) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch09-error-code&k=Indoor+main+PCB+or+EEPROM+PCB+%28Multi+V%29&tag=errorcodefixes-20) \| For the EEPROM memory variant of CH09. Confirm part number from your indoor unit label. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live AC voltage, if the fault persists after reseating connectors and verifying the fan spins freely, or if you need to replace a PCB and perform refrigerant-circuit commissioning or Auto Addressing. Multi V systems and memory-related faults require specialized diagnostic software and training. If your outdoor fan motor runs but CH09 still appears, or if you see the code on an indoor unit without clear guidance in your service manual, professional diagnosis will save time and prevent incorrect part replacement.
