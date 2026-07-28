---
title: "Fujitsu Mini Split Won't Turn On - Causes & Fix"
description: "Usually caused by a communication fault between indoor and outdoor units (often E1 code). Check wiring connections and power first."
pubDatetime: 2026-06-11T11:45:49Z
modDatetime: 2026-06-11T11:45:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - fujitsu
  - symptom
---

## Fujitsu Mini Split Won't Turn On — What's Happening

When a Fujitsu mini split won't turn on, it's usually not a single problem. The most common fault tied to a no-start condition is a communication error between the indoor and outdoor units, often shown as an E1 code on systems that use that code family. If your unit shows a different pattern like E:EE, that indicates a separate communication or setup issue in older models, not the same fault as E1.

Fujitsu's troubleshooting guidance says to check wiring from the indoor unit to the outdoor condenser, look for connector problems, open cables, voltage-drop issues, or a defective control board. If the unit appears completely dead with no fault code at all, the manufacturer still directs technicians first to power, wiring, and control-board checks before replacing any components.

## Most Likely Causes

- **Loose or disconnected wiring between indoor and outdoor units** The interconnecting wiring harness or terminal connections at either the indoor or outdoor PCB are the most common point of failure in communication faults and no-start conditions.
- **Power supply problem to one or both units** Voltage drop, poor ground, tripped breaker, or loss of power to either the indoor or outdoor side will prevent the system from starting.
- **Loose or removed connector at the control board** Molex plugs or harness connectors at the indoor or outdoor PCB can work loose during installation or service, breaking the communication path.
- **Failed indoor control board** The indoor controller PCB can fail and prevent communication or power distribution to the rest of the system.
- **Failed outdoor control board** The outdoor unit's control board can fail, stopping all communication with the indoor unit and preventing compressor or fan operation.
- **Remote control or receiver circuit fault** Fujitsu's troubleshooting guide uses specific PCB connector voltage checks to separate a remote control failure from a controller board failure in no-start cases.
- **Sensor open or short circuit** Thermistor or other sensor faults can trigger protection modes that stop operation, depending on the model and sensor type involved.

## How to Diagnose and Fix {#fix}

1. Verify both indoor and outdoor units have supply power and that all breakers and disconnects are in the on position.
2. Power down the system at the disconnect or breaker, wait 60 seconds, then restore power and check if the unit starts.
3. Inspect all interconnecting wiring between the indoor and outdoor units for loose terminals, wrong connections, open cables, or damaged harnesses.
4. Check connector seating on both the indoor and outdoor PCBs and verify all molex plugs are fully seated and not removed or loose.
5. Measure 12 VDC at the indoor controller PCB connector CNC01 (12 V present indicates remote control failure, 0 V indicates controller PCB failure per Fujitsu's guide).
6. Check for voltage drop or poor grounding on the same circuit and verify no abnormal supply conditions are present.
7. Measure DC voltage between indoor fan motor wires (should see 150–380 V DC between red and black, 15 V DC between black and white per Fujitsu).
8. If power and wiring checks pass, isolate the failed control board by substitution, replacing the indoor or outdoor PCB that the voltage tests identified.

## Parts You Might Need

| Part | Notes |
|------|-------|
| Fujitsu indoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-wont-turn-on&k=Fujitsu+indoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Model-specific, verify part number from your indoor unit label |
| Fujitsu outdoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-wont-turn-on&k=Fujitsu+outdoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Model-specific, verify part number from your outdoor unit label |
| Interconnecting wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-wont-turn-on&k=Interconnecting+wiring+harness&tag=errorcodefixes-20) \| Pre-terminated indoor-to-outdoor communication cable |

## Related Error Codes

If your appliance also shows a code on the display, these match this problem:

- Fujitsu Mini Split E 01 error code
- Fujitsu Mini Split E 02 error code
- Fujitsu Mini Split E 03 error code
- Fujitsu Mini Split E 04 error code
- Fujitsu Mini Split E 05 error code
- Fujitsu Mini Split E 06 error code
- Fujitsu Mini Split E 07 error code
- Fujitsu Mini Split E 08 error code
- Fujitsu Mini Split E 09 error code
- Fujitsu Mini Split E 10 error code
- Fujitsu Mini Split E 11 error code
- Fujitsu Mini Split E 12 error code

## When to Call a Pro

Call a licensed HVAC technician if you see an E1 or communication fault code and you're not comfortable working with line-voltage wiring or PCB diagnostics. Technicians have the model-specific flowcharts, voltage test points, and board-substitution tools to isolate a failed control board from a wiring or sensor issue. If the system is completely dead with no display at all, a pro can trace power through both units and check for voltage drop or grounding faults that are hard to spot without a multimeter and the manufacturer's wiring diagrams.
