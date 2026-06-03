---
title: "Siemens G120 F0015 Fault - Causes & Fix"
description: "F0015 means motor temperature signal lost or open-circuit. Check motor thermistor wiring and sensor connections at motor and drive."
pubDatetime: 2026-06-01T11:40:38Z
modDatetime: 2026-06-01T11:40:38Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F0015 Fault — What It Means

Fault code F0015 on a Siemens SINAMICS G120 variable frequency drive indicates a motor temperature monitoring fault. The drive has detected that the motor temperature sensor signal is lost or open-circuit, so it cannot reliably monitor motor thermal protection. This fault is specific to the motor temperature sensing circuit and its parameterization, not the drive's internal temperature. The drive shuts down to protect the motor because it no longer has feedback from the thermal sensor.

[Jump to Fix](#fix)

## Common Causes

- **Open or broken motor thermistor wiring** The temperature sensor cable between the motor and drive has a break, cut, or open conductor that interrupts the signal path.
- **Loose or corroded terminals** The temperature input terminals at the motor junction box or drive input block are loose, corroded, or making poor contact.
- **Failed motor temperature sensor** The thermistor or temperature sensor embedded in the motor windings has failed open and no longer provides a valid signal.
- **Incorrect drive parameterization** The drive is configured to expect a temperature sensor type that does not match the actual motor sensor or thermal model, so it reads the feedback as invalid.
- **Damaged cable or connector** The temperature sensor cable or connector has been crushed, pinched, or physically damaged, causing intermittent or total signal loss.
- **Drive control unit input circuit fault** Less commonly, the temperature input circuit on the drive control unit itself has failed, though this is rare and only suspect after verifying the sensor and wiring.

## Step-by-Step Fix {#fix}

1. **Shut down and lock out power** to the drive safely before beginning any work on the motor temperature circuit.
2. **Identify the motor temperature sensor type** from the motor nameplate or documentation and verify the drive parameters are configured for that sensor or thermal model.
3. **Inspect the sensor wiring** from the motor terminal box to the drive temperature input terminals for visible damage, loose connections, crushed cable, or corrosion at all connection points.
4. **Measure continuity** of the sensor circuit at both the motor side and drive side to confirm the sensing element is not open and the cable is intact.
5. **Compare drive motor data parameters** (such as motor connection type and thermal protection settings) to the actual motor nameplate and application setup to make sure correct configuration.
6. **Repair or replace** any defective sensor, damaged cable, or faulty connector assembly you find during testing.
7. **Clear the fault** and run the motor under load to confirm stable temperature feedback and verify the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor temperature sensor (thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0015-fault-code&k=Motor+temperature+sensor+%28thermistor%29&tag=errorcodefixes-20) \| Match the sensor type (PTC, NTC, or PT100) to your motor and drive model. |
| Shielded thermistor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0015-fault-code&k=Shielded+thermistor+cable&tag=errorcodefixes-20) \| Use proper motor-rated temperature sensor cable with shielding to prevent interference. |
| Terminal blocks or connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f0015-fault-code&k=Terminal+blocks+or+connectors&tag=errorcodefixes-20) \| Replace corroded or damaged terminals at the motor junction box or drive input. |

## When to Call a Pro

Call a qualified industrial electrician or controls technician if you are not trained in variable frequency drive systems, if you cannot safely lock out and test the motor circuit, or if the fault persists after verifying and replacing the sensor and wiring. If the sensor circuit tests good at both ends but the drive still reports F0015, the drive control unit may need factory service or replacement by a Siemens-authorized technician. Industrial VFD work involves lethal voltages and specialized diagnostic equipment, so professional support is recommended for complex faults or systems critical to production.
