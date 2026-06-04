---
title: "Gree Mini Split U5 Error Code - Causes & Fix"
description: "U5 on a Gree mini split signals an outdoor unit current detection or power-supply fault. Fix by checking outdoor board connections first."
pubDatetime: 2026-05-31T08:07:50Z
modDatetime: 2026-05-31T08:07:50Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - gree
---

## Gree Mini Split U5 Error Code — What It Means

The U5 error code on a Gree mini split indicates a current detection or power-supply protection fault in the outdoor unit. This code is part of Gree's outdoor inverter malfunction group and means the outdoor PCB has detected a problem with current sensing, voltage supply, or the inverter module. It is not a refrigerant or airflow issue. The fault typically points to problems in the outdoor unit's power electronics, including the inverter board, IPM (Intelligent Power Module), current-sensing circuit, wiring connections, or the main power supply feeding the outdoor unit.

In real-world service, technicians most often find loose or corroded connectors, damaged wiring harnesses, failed current-detection components on the outdoor PCB, blown fuses, or defective inverter-stage parts. The code triggers when the board's protection circuits detect an abnormal current or voltage condition, shutting down operation to prevent damage to the compressor or power module.

[Jump to Fix](#fix)

## Common Causes

- **Outdoor PCB current-sensing circuit failure** A failed sensing resistor or related detection component on the outdoor board causes the system to misread load current and trip the U5 protection code.
- **Loose or corroded outdoor-unit connectors** Poor contact at board plugs, harness connectors, or compressor terminals creates intermittent circuits that the detection system flags as a fault.
- **Defective IPM or inverter power stage** A faulty Intelligent Power Module or its drive and feedback circuitry can produce abnormal current signatures that trigger the U5 code under load.
- **Power-supply instability or incorrect voltage** Weak incoming line voltage or a failing rectifier and DC bus inside the outdoor unit causes the protection circuit to activate.
- **Blown fuse or failed protection device** An open fuse or protection element on the outdoor PCB stops the current-detection circuit from operating correctly and generates the error.
- **Failed discrete components on the outdoor board** Technicians have documented cases where specific parts such as R901 and D902 on the outdoor PCB were the root cause of repeating U5 faults.

## Step-by-Step Fix {#fix}

1. **Confirm the U5 code is active** by checking the display or LED pattern on both the indoor and outdoor units, and note whether the fault is repeatable when you restart the system.
2. **Measure incoming line voltage** at the outdoor unit terminals to verify it is within the manufacturer's rated supply range before investigating board-level faults, since low or unstable voltage can mimic a PCB failure.
3. **Inspect and reseat all outdoor-board connectors**, including the main power harness, compressor terminals, and any inter-board plugs, looking for discoloration, loose pins, corrosion, or heat damage.
4. **Check the outdoor-unit fuse** and any other protection devices on the PCB to confirm they are intact, because an open fuse can disable the current-sensing circuit and cause the U5 code.
5. **Test the current-detection circuit** by following the board's sensing path and verifying the resistance and continuity of detection resistors and associated components rather than replacing the entire board immediately.
6. **Measure the DC bus voltage** across the IPM or main filter capacitor (a working bus typically reads around 335 VDC on 230 V systems) to rule out rectifier or supply-stage failures.
7. **Evaluate the IPM and gate-drive stage** if supply and sensing circuits check out, testing the Intelligent Power Module and its discharge network for faults, and replace the defective component or the entire outdoor PCB assembly if a specific part cannot be isolated.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor PCB assembly (inverter control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-u5-error-code&k=Outdoor+PCB+assembly+%28inverter+control+board%29&tag=errorcodefixes-20) \| Match by model and serial number. Required when current-sensing or power-stage components are integrated and not individually serviceable. |
| IPM (Intelligent Power Module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-u5-error-code&k=IPM+%28Intelligent+Power+Module%29&tag=errorcodefixes-20) \| Verify compatibility with your outdoor-unit model. Replaces the inverter power stage when testing isolates the IPM as the fault. |
| Wire harness (outdoor unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-gree-mini-split-u5-error-code&k=Wire+harness+%28outdoor+unit%29&tag=errorcodefixes-20) \| Order the correct harness set if you find melted insulation, broken conductors, or terminal damage that cannot be repaired by connector replacement alone. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live line voltage or if you lack a multimeter and the experience to safely test PCB circuits and high-voltage DC bus components. Component-level board repair requires schematic knowledge and the ability to identify and replace surface-mount parts such as sensing resistors and diodes. If you have verified incoming power and reseated all connectors but the U5 code persists, a technician with Gree-specific service documentation can isolate the failed sensing circuit, IPM, or board component and complete the repair safely. Professional diagnosis is especially important if the fault is intermittent or if you suspect a compressor or refrigerant-side issue that might produce abnormal electrical signatures.
