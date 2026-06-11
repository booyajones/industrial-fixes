---
title: "MRCOOL EH 60 Error Code - Causes & Fix"
description: "EH 60 means the indoor room temperature sensor (T1) is open or shorted. Most often caused by a failed sensor or loose connector."
pubDatetime: 2026-05-31T08:37:47Z
modDatetime: 2026-05-31T08:37:47Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mrcool
money_part: "Indoor room temperature sensor (T1 thermistor)"
---

## MRCOOL EH 60 Error Code — What It Means

The EH 60 error code on a MRCOOL mini-split indicates that the indoor unit is not receiving a valid signal from the indoor room temperature sensor, also called the T1 thermistor. This sensor measures the return air or room temperature at the indoor air handler. According to MRCOOL's official troubleshooting documentation, EH 60 means the T1 sensor is either in open circuit or has a short circuit, preventing the control board from reading the room temperature correctly.

When the sensor circuit fails, the system cannot regulate temperature properly and will display this fault code. The problem is usually in the sensor itself, the wiring harness that connects it to the control board, or occasionally the indoor PCB that reads the sensor signal.

[Jump to Fix](#fix)

## Common Causes

- **Failed T1 thermistor** The indoor room temperature sensor itself has failed internally, showing an open circuit or incorrect resistance when tested with a multimeter.
- **Loose or corroded connector** The plug connecting the T1 sensor to the indoor control board has worked loose, developed corrosion, or has poor contact.
- **Damaged sensor wiring** The wiring harness between the sensor and the indoor PCB is pinched, cut, frayed, or has broken strands causing intermittent or total loss of signal.
- **Faulty indoor control board** The indoor PCB is not reading the sensor correctly even though the sensor and wiring test good, often due to a failed circuit trace or component on the board.
- **Sensor voltage out of range** The sensor circuit voltage falls below 0.06 V or rises above 4.94 V, triggering the fault per manufacturer specifications for similar units.

## Step-by-Step Fix {#fix}

1. **Power off the system** at the breaker and wait at least two minutes, then restore power to perform a full reset and see if the code clears on its own.
2. **Locate the T1 sensor** inside the indoor air handler (usually clipped to the evaporator coil or return air path) and inspect the sensor body and connector for visible damage, corrosion, or loose seating.
3. **Check the wiring harness** that runs from the T1 sensor to the indoor control board, looking for pinched wires, cuts, fraying, or any signs of physical damage along the entire run.
4. **Disconnect the T1 sensor** from the control board and use a multimeter set to resistance (ohms) mode to measure across the sensor terminals, checking for an open reading which confirms sensor failure.
5. **Replace the T1 thermistor** if the resistance reading is open or obviously out of range, ensuring the new sensor is firmly seated and the connector clicks into place.
6. **Test the system** by restoring power and monitoring for at least one cooling or heating cycle to confirm the EH 60 code does not return.
7. **Evaluate the indoor PCB** if the sensor and wiring both test good but the code persists, as the control board may have a fault in the sensor input circuit and require replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor room temperature sensor (T1 thermistor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-60-error-code&k=Indoor+room+temperature+sensor+%28T1+thermistor%29&tag=errorcodefixes-20) \| Verify compatibility with your specific MRCOOL model and series before ordering. |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-60-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| Only needed if the original harness is cut, pinched, or has damaged connectors that cannot be repaired. |
| Indoor PCB / control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-60-error-code&k=Indoor+PCB+%2F+control+board&tag=errorcodefixes-20) \| Required if the sensor and wiring test good but the fault remains. Match the board part number to your indoor unit model. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with electrical components or multimeter testing, if the sensor and wiring appear intact but the code persists, or if you suspect the indoor control board needs replacement. Technicians have the proper tools to measure thermistor resistance accurately, access to OEM parts, and the experience to diagnose board-level faults. Professional diagnosis is also recommended if the unit is still under warranty, as DIY repairs may void coverage.
