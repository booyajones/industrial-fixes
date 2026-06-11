---
title: "Fujitsu E:77 Error - Causes & Fix"
description: "E:77 means outdoor unit heat sink thermistor error. Usually a failed sensor, loose connector, or bad inverter PCB. Pro diagnosis required."
pubDatetime: 2026-05-31T01:16:58Z
modDatetime: 2026-05-31T01:16:58Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Outdoor unit heat sink thermistor"
---

## Fujitsu E:77 Error — What It Means

Code E:77 on a Fujitsu mini-split indicates a heat sink thermistor error in the outdoor unit. The thermistor monitors the temperature of the inverter or IPM heat sink. When the control board sees an invalid, open, shorted, or out-of-range signal from this sensor, it throws the E:77 fault and shuts down the system to protect the inverter electronics. This is not a fan motor problem. It is a sensor or circuit issue tied specifically to the outdoor inverter section.

[Jump to Fix](#fix)

## Common Causes

- **Failed heat sink thermistor** The thermistor itself has failed and is reading open, shorted, or out of range.
- **Loose or damaged thermistor connector** The connector between the thermistor and the outdoor PCB is loose, corroded, or the wiring is damaged.
- **Open or miswired thermistor cable** The harness from the heat sink sensor to the board has an open circuit or was reconnected incorrectly during prior service.
- **Defective outdoor inverter PCB** The main or inverter board is reading the sensor signal incorrectly even though the thermistor and wiring are good.
- **Overheating inverter section** Blocked airflow, dirty condenser coils, or another fault causes abnormal heat sink temperatures that push the thermistor reading out of normal range.

## Step-by-Step Fix {#fix}

1. **Kill power at the breaker** and lock it out. Wait five minutes for capacitors to discharge. Fujitsu service docs warn of high voltage inside outdoor unit covers.
2. **Remove the outdoor unit service panel** and locate the inverter PCB and heat sink thermistor. The thermistor is usually mounted on or near the large aluminum heat sink attached to the inverter module.
3. **Inspect the thermistor connector and harness** for loose plugs, corrosion, damaged insulation, or pinched wires. Reseat the connector firmly and check for visual damage.
4. **Check thermistor resistance** with a multimeter. Disconnect the thermistor from the board, measure resistance across the sensor leads, and compare to the resistance table in your model's service manual. If it reads open, shorted, or wildly out of spec at room temperature, replace the thermistor.
5. **Test for continuity** in the thermistor harness from the sensor plug to the PCB connector. An open wire will cause the fault even if the sensor is good.
6. **If wiring and thermistor test good, suspect the outdoor inverter PCB.** Consult the service manual for your model. Board-level faults require PCB replacement.
7. **Reassemble, restore power, and run a test cycle.** Clear the error by power-cycling the unit. Monitor for 15 minutes to confirm the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor unit heat sink thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-77-error-code&k=Outdoor+unit+heat+sink+thermistor&tag=errorcodefixes-20) \| Match by model number. Mounts on or near the inverter heat sink. |
| Outdoor inverter PCB (main control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-77-error-code&k=Outdoor+inverter+PCB+%28main+control+board%29&tag=errorcodefixes-20) \| Required if thermistor and wiring test good but fault persists. Verify exact board part number for your outdoor unit. |
| Thermistor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-77-error-code&k=Thermistor+wiring+harness&tag=errorcodefixes-20) \| Only if the cable between sensor and PCB is damaged or has an open circuit. |

## When to Call a Pro

E:77 requires opening the outdoor unit and working around high-voltage inverter components. If you are not EPA-certified, lack a multimeter and service manual, or are uncomfortable diagnosing sensor circuits and replacing PCBs, call a licensed HVAC technician. Misdiagnosis can lead to expensive part swaps. Inverter boards cost several hundred dollars and thermistor faults can mimic board faults if wiring checks are skipped. A qualified tech has the resistance tables, safety training, and tools to isolate the fault quickly.
