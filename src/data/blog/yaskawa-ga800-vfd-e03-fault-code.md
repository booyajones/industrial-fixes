---
title: "Yaskawa GA800 E03 Fault - Causes & Fix"
description: "E03 on a Yaskawa GA800 means motor thermistor overheat or circuit fault. Most likely fix: let motor cool, check thermistor wiring."
pubDatetime: 2026-06-04T09:22:49Z
modDatetime: 2026-06-04T09:22:49Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Motor thermistor (PTC sensor)"
most_likely_cause: "Motor actually overheated"
---

## What this code means
The E03 fault on a Yaskawa GA800 VFD indicates a motor overheat or thermistor circuit fault. The drive has detected that the motor temperature protection input is signaling an overtemperature condition or that the thermistor circuit itself is open, shorted, or otherwise abnormal. This is not a drive power stage failure. The fault is responding to the motor temperature protective circuit, which can trip either because the motor has genuinely overheated or because the thermistor wiring or sensor has failed.

Yaskawa's GA800 documentation directs technicians to remove the fault cause before resetting. The drive will not restart until the condition is corrected and the fault is cleared. This fault protects the motor from thermal damage, so you must verify whether the motor is truly hot or whether the problem is in the thermistor circuit or drive configuration.

## Common Causes

- **Motor actually overheated** Overload, stalled rotor, excessive starts and stops, poor cooling, high ambient temperature, or blocked airflow cause the motor to overheat and trip the thermistor circuit.
- **Open or miswired thermistor circuit** Loose terminals, broken conductors, incorrect landing on the drive's thermistor input, or damaged wiring in the motor leads create an open circuit the drive reads as a fault.
- **Shorted or failing thermistor** The PTC or thermistor sensor embedded in the motor windings has failed internally and is sending a continuous fault signal to the drive.
- **Incorrect drive parameterization** Motor temperature input or protection function parameters are wrong after commissioning, replacement, or a drive initialization, causing the drive to misinterpret a valid circuit.
- **Cooling system failure** Failed motor fan, clogged cooling fins, or insufficient cabinet ventilation prevent the motor from dissipating heat and drive the thermistor to trip even when the drive is healthy.

## Step-by-Step Fix {#fix}

1. **Confirm the fault on the operator panel** and check if the motor itself is hot to the touch to determine whether this is a thermal or electrical fault.
2. **Inspect the motor and load mechanically** for overload, binding, seized bearings, jammed process equipment, or a failed cooling fan that would cause genuine overheating.
3. **Inspect the thermistor wiring** from the motor to the drive for opens, shorts, loose terminals, damaged insulation, incorrect shield grounding, or wrong terminal landing at the drive input.
4. **Measure continuity of the thermistor circuit** at both the motor and drive ends if accessible to confirm the sensor and wiring are intact and within the expected resistance range.
5. **Verify the drive configuration** for motor temperature input and protection function matches the installed motor and wiring setup, especially if the drive was recently replaced or reinitialized.
6. **Correct the root cause** by reducing load, restoring cooling airflow, repairing or replacing the motor fan, fixing damaged wiring, or replacing a failed thermistor before re-energizing.
7. **Reset the fault** using the keypad reset procedure or by cycling drive power only after the cause has been identified and corrected, per Yaskawa's fault reset guidance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor thermistor (PTC sensor) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e03-fault-code&k=Motor+thermistor+%28PTC+sensor%29&tag=errorcodefixes-20) \| Replacement winding temperature sensor if the original has failed or is reading incorrectly. |
| Thermistor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e03-fault-code&k=Thermistor+wiring+harness&tag=errorcodefixes-20) \| Cable assembly between motor and drive if existing wiring is damaged, shorted, or open. |
| Motor cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e03-fault-code&k=Motor+cooling+fan&tag=errorcodefixes-20) \| External or shaft-mounted fan if motor overheating is due to failed ventilation. |

## When to Call a Pro

Call a qualified electrician or motor technician if you cannot locate the thermistor wiring, if the motor continues to overheat after correcting obvious mechanical or cooling problems, or if you are unfamiliar with VFD parameter setup and motor protection configuration. An E03 fault that recurs immediately after reset often indicates internal motor damage or a persistent circuit fault that requires diagnostic equipment and motor testing. If the motor must be rewound or the thermistor replaced inside the motor housing, professional motor shop service is required.
