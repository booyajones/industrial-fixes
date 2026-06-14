---
title: "Yaskawa GA800 E21 Fault Code - Causes & Fix"
description: "E21 is not a standard GA800 fault code. Verify the exact display and check your technical manual for the real code shown on the keypad."
pubDatetime: 2026-06-05T09:55:49Z
modDatetime: 2026-06-05T09:55:49Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor thermistor or PTC temperature sensor"
most_likely_cause: "Misread or misidentified display code"
---

## Yaskawa GA800 E21 Fault Code — What It Means

E21 does not appear in Yaskawa's documented GA800 fault or alarm tables. The code you see on the keypad display may be misread or may actually be a different alarm such as oH3 (motor overheat from PTC input) or another fault. The GA800 uses specific alphanumeric codes for faults and alarms, and E21 is not among them according to available technical documentation. Before attempting any repair, confirm the exact characters shown on the drive's display and whether it is labeled as a fault or alarm.

If the actual code is oH3 or another motor-temperature alarm, the cause is typically a defective thermistor wiring circuit or incorrect wiring to the motor temperature detection input. For any unconfirmed code, record the drive's model number, specification number, serial number, and the exact displayed code, then consult the GA800 technical manual or contact Yaskawa support to identify the true fault and its meaning.

[Jump to Fix](#fix)

## Common Causes

- **Misread or misidentified display code** The characters on the keypad may look like E21 but are actually a different fault, alarm, or parameter value.
- **Defective motor thermistor wiring (if code is oH3 or similar)** Open, shorted, or corroded wiring to the motor's PTC or thermistor temperature sensor triggers a motor overheat alarm.
- **Incorrect temperature sensor wiring** Wrong terminal connections or polarity on the motor temperature input cause false temperature fault readings.
- **Failed or damaged thermistor in the motor** A motor-mounted PTC or thermistor that has failed open or short will signal an overheat condition even when the motor is cool.
- **Control board misreading inputs** A faulty control board on the GA800 may generate spurious fault codes or display characters that do not match the actual alarm state.
- **Parameter or monitor value mistaken for a fault** The display may be showing a parameter number or monitor reading rather than an active fault code.

## Step-by-Step Fix {#fix}

1. Verify the exact code on the keypad display and write down every character, noting whether the drive labels it as a fault, alarm, or parameter.
2. Record the drive model, specification number, and serial number from the nameplate before cycling power or resetting the drive.
3. Consult the GA800 technical manual fault and alarm tables to match the exact displayed code and identify its documented meaning.
4. Inspect motor thermistor and PTC wiring if the code is temperature-related, checking for open circuits, shorts, loose terminals, or corroded connections at both the motor and drive ends.
5. Measure resistance across the thermistor or PTC sensor with the motor cool and compare to the motor manufacturer's specification to confirm the sensor is not open or shorted.
6. Correct any wiring errors or replace damaged thermistor cable and reconnect to the proper terminals on the GA800.
7. Contact Yaskawa technical support with your recorded drive information and exact fault code if the code remains unidentified or the fault persists after wiring correction.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor thermistor or PTC temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e21-fault-code&k=Motor+thermistor+or+PTC+temperature+sensor&tag=errorcodefixes-20) \| Match to your motor manufacturer's specification and connector type. |
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e21-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Field-replaceable assembly for the GA800, verify model and spec number before ordering. |
| Yaskawa GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e21-fault-code&k=Yaskawa+GA800+cooling+fan&tag=errorcodefixes-20) \| Field-replaceable assembly, consult GA800 maintenance documentation for compatibility. |

## When to Call a Pro

Call a qualified drives technician or contact Yaskawa support if you cannot confirm the exact fault code from the technical manual, if the code persists after correcting external wiring, or if you are not trained to work safely on live industrial motor drives. The GA800 maintenance documentation limits deep field repair to fan and control board replacement, so internal component-level troubleshooting or board-level diagnostics require factory support or an authorized Yaskawa service center. Do not attempt repairs on energized high-voltage equipment without proper lockout and electrical safety training.
