---
title: "Danfoss FC302 ALARM 20 - Causes & Fix"
description: "ALARM 20 means temperature input error: the sensor is not connected or wired correctly. Check wiring and sensor connection first."
pubDatetime: 2026-06-02T10:45:56Z
modDatetime: 2026-06-02T10:45:56Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 ALARM 20 — What It Means

ALARM 20 on a Danfoss FC302 VFD indicates a temperature input error. The drive has detected that it cannot read a valid signal from the temperature sensor circuit. This is not an overtemperature condition, but rather a problem with the sensor input itself. The drive expects a temperature sensor to be connected to a specific input terminal, and it is either missing, disconnected, wired incorrectly, or the input circuit is faulty.

Danfoss documentation describes this alarm as 'Temp. input error. The temperature sensor is not connected.' The fault is raised when the drive cannot see the expected sensor connection or signal state on the configured temperature input. Until the input reads correctly, the drive will not clear the alarm.

[Jump to Fix](#fix)

## Common Causes

- **Temperature sensor not wired or disconnected** The sensor is not connected to the expected input terminal, or the connection has come loose or open.
- **Incorrect wiring to temperature input terminals** The sensor leads are landed on the wrong terminals or the polarity or circuit is wired incorrectly for the configured input type.
- **Wrong parameter setup for temperature function** The drive is configured to expect a thermistor or temperature sensor on a specific analog or thermistor input, but the field wiring does not match that configuration.
- **Failed temperature sensor or damaged cable** The sensor itself has failed open or the field cable has broken conductors, corrosion, or physical damage.
- **Faulty control card or input circuitry** If wiring and sensor test good but the alarm persists, the drive's internal input circuit or control card is likely defective.

## Step-by-Step Fix {#fix}

1. **Identify the configured temperature input** by reviewing the drive parameters to confirm which input terminal and sensor type (thermistor, PTC, etc.) the drive expects.
2. **Inspect the sensor wiring and terminals** at both the drive input and the sensor itself for loose connections, broken wires, corrosion, or incorrect landing on the terminal block.
3. **Check the sensor type and termination** against the drive configuration to make sure the correct thermistor or temperature device is connected where the drive expects it.
4. **Remove the external sensor wiring** from the relevant input terminals and observe whether the alarm clears or changes state when the drive is powered.
5. **If the alarm clears with wiring removed**, repair or replace the field sensor, cable, or terminations and reconnect.
6. **If the alarm does not clear**, suspect the drive's internal input circuit or control card and plan for control-card replacement or factory service.
7. **Reset the alarm** after repair and verify normal operation with the motor running under load and the temperature input reading stable in the drive display or parameter readout.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Temperature sensor (thermistor or PTC) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-20-fault-code&k=Temperature+sensor+%28thermistor+or+PTC%29&tag=errorcodefixes-20) \| Match the sensor type (resistance curve and connector) to the FC302 input configuration. |
| Sensor cable and terminal connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-20-fault-code&k=Sensor+cable+and+terminal+connectors&tag=errorcodefixes-20) \| Use shielded cable rated for the environment if replacing field wiring to the temperature input. |
| FC302 control card / control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-20-fault-code&k=FC302+control+card+%2F+control+PCB&tag=errorcodefixes-20) \| Required if the alarm persists with field wiring removed and the input circuit is confirmed faulty. |

## When to Call a Pro

Call a qualified technician or VFD specialist if you are not comfortable working with low-voltage control wiring or interpreting drive parameters. If the alarm remains after you have verified and reconnected the sensor wiring, the fault is likely inside the drive and requires control-card diagnosis or replacement. Industrial VFD repairs often involve both electrical troubleshooting and parameter programming, and incorrect changes can affect motor protection or process safety. Professional service is recommended any time the control card is suspect or when the drive serves a critical or high-value application.
