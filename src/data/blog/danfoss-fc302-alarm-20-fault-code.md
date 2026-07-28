---
title: "Danfoss FC302 Alarm 20 - Causes & Fix"
description: "Danfoss FC302 Alarm 20 (Temp. input error) means the drive cannot read the configured temperature sensor. Fix wiring and sensor issues."
pubDatetime: 2026-05-29T09:42:55Z
modDatetime: 2026-05-29T09:42:55Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Motor thermistor or PTC temperature sensor"
most_likely_cause: "Open or loose thermistor wiring"
---

## What this code means
Alarm 20 on the Danfoss FC302 is a "Temp. input error." The drive has detected that the configured temperature sensor input is missing, open, or otherwise invalid. Danfoss states that this fault typically means the temperature sensor is not connected or not communicating properly with the drive.

The FC302 monitors motor or external temperature sensors to protect equipment from overheating. When the drive cannot see a valid signal on the configured temperature input (usually terminal 53 or 54), it raises Alarm 20 and may shut down or limit operation to prevent damage. The fault does not mean the motor is hot, it means the drive cannot verify temperature at all.

## Common Causes

- **Open or loose thermistor wiring** The most common cause is a broken wire, loose screw terminal, or poor connection at the drive or motor terminal box.
- **Terminal configuration mismatch** The drive is configured to read a sensor on terminal 53 or 54, but the field wiring or terminal setup does not match that parameter setting.
- **Wrong input type or parameter setup** The analog input is configured for the wrong sensor type (PTC vs. PT100 vs. voltage) or the temperature source parameter does not match the physical installation.
- **Failed thermistor or temperature sensor** The motor thermistor or external thermal protection device has failed open or degraded and no longer presents a valid resistance to the drive.
- **Drive input circuit failure** Less commonly, the temperature input circuit or control card in the drive itself has failed, even though field wiring and sensor test correctly.

## Step-by-Step Fix {#fix}

1. Lock out power to the drive and follow all Danfoss safety precautions before opening the enclosure or touching terminals.
2. Check the drive parameters to confirm which temperature input is enabled and which terminal (53 or 54) is configured for the sensor type you have installed.
3. Inspect the sensor wiring at both the drive terminals and the motor or external sensor, looking for loose screws, broken conductors, or incorrect wire landing.
4. Disconnect the sensor cable at the drive and measure resistance across the thermistor leads with a multimeter to verify the sensor is not open-circuit (a good thermistor will show a finite resistance, typically a few hundred to a few thousand ohms depending on type and temperature).
5. If the sensor reads open or infinite resistance, replace the thermistor or temperature sensor and verify continuity of the new installation.
6. If the sensor and wiring test good, review the analog input configuration in the drive programming to confirm the input type matches the physical sensor (consult your model's parameter table for exact analog input and temperature source settings).
7. If all field wiring, sensor, and parameters are verified correct and the alarm persists, suspect the drive's temperature input circuit and consult Danfoss service or replace the control card only after confirming all external factors.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor thermistor or PTC temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-20-fault-code&k=Motor+thermistor+or+PTC+temperature+sensor&tag=errorcodefixes-20) \| Replace if sensor tests open or infinite resistance. |
| Temperature sensor cable (shielded twisted pair) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-20-fault-code&k=Temperature+sensor+cable+%28shielded+twisted+pair%29&tag=errorcodefixes-20) \| Use if original cable is damaged or shows intermittent continuity. |
| Danfoss FC302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-20-fault-code&k=Danfoss+FC302+control+card&tag=errorcodefixes-20) \| Required only if sensor and wiring test good but alarm persists, indicating internal input circuit failure. |

## When to Call a Pro

Call a qualified technician or Danfoss service if you are not familiar with VFD parameter programming, if you cannot safely lock out power and verify zero voltage, or if the alarm returns after you have confirmed good sensor resistance and correct wiring. Also call for help if the drive is part of a coordinated system (building HVAC, process line, or fire-pump setup) where incorrect parameter changes could create safety or production issues. If you have replaced the sensor and verified all wiring but Alarm 20 persists, the drive's internal temperature input circuit may be faulty and will require factory-trained diagnostics or control card replacement.
