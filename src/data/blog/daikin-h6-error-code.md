---
title: "Daikin H6 Error Code — Indoor Fan Motor Lock Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: daikin-h6-error-code
featured: false
draft: false
tags:
  - daikin
  - mini-split
  - hvac
  - fan-motor
description: "Daikin H6 error code means the indoor fan motor is locked or its speed cannot be detected. Learn what causes it and how to fix it on Daikin mini-splits and VRV/VRF systems."
---

## Error Code: Daikin H6

**What it means:** The H6 error code on Daikin ductless mini-split systems — and on Daikin VRV/VRF commercial systems — indicates that the indoor unit's fan motor has locked up, stalled, or that the control board cannot detect the fan's speed signal from the Hall effect sensor. The indoor fan circulates air across the evaporator coil during cooling or the condenser coil during heating. When it fails to spin or spins at an incorrect speed, the system shuts down to prevent coil freeze-up or overheating.

This code applies to Daikin's wall-mount, floor console, ceiling cassette, and ducted indoor units across the FTX, RXS, FTXS, and VRV/VRF series. The specific cause depends on whether the motor is a standard single-phase induction motor with a run capacitor or a newer DC brushless (BLDC) direct-drive fan motor.

## Common Causes

- **Failed indoor fan motor** — The motor winding has developed an open circuit, a short, or seized bearings. On older units with AC induction motors, bearing failure is the most common mechanical cause. On newer BLDC direct-drive motors, winding or hall sensor failure is more common.
- **Failed run capacitor** — AC induction fan motors rely on a start/run capacitor to generate the phase shift needed for starting torque. A capacitor that has lost capacitance (common after 5–10 years) will cause the motor to hum but not spin — a classic H6 trigger.
- **Obstruction in the fan wheel or scroll** — A foreign object — a toy, insulation fragment, or accumulated ice — jammed in the blower wheel physically prevents the motor from spinning and causes the motor to lock up thermally.
- **Indoor PCB (control board) failure** — The indoor unit control board generates the fan drive signal and reads the speed feedback from the Hall sensor. If the board has failed, it may not drive the motor at all or may fail to read a valid speed signal, logging H6 even when the motor itself is fine.
- **Hall effect sensor wiring fault** — On BLDC motors, a broken wire or corroded connector in the Hall effect speed sensor harness will prevent the board from detecting fan rotation, logging H6 even if the motor is actually spinning.
- **Accumulated ice on the evaporator coil** — Severe ice buildup can extend into the fan scroll housing and physically jam the wheel. This is typically secondary to a low refrigerant or airflow problem, but it can trigger H6 directly.

## Step-by-Step Diagnosis {#step-by-step-fix}

1. **Power off, inspect the fan wheel for obstructions.** Turn the breaker off and open the front panel of the indoor unit. Visually inspect the blower wheel. Use a flashlight to check for any foreign objects jammed in the wheel or scroll. Manually rotate the fan wheel — it should spin freely with no grinding or resistance. If it won't spin by hand, there is either a mechanical obstruction or seized motor bearings.

2. **Check for ice buildup.** If the blower wheel is iced over, leave the unit off for several hours (or use a hair dryer at low heat with care) to defrost. Once defrosted, run the unit in fan-only mode for 10–15 minutes to confirm the error doesn't immediately return. Then investigate the root cause of the ice (low refrigerant, restricted airflow, dirty coil).

3. **Test the run capacitor (AC induction motors only).** On older Daikin units with a traditional capacitor-start motor, use a capacitance meter to test the run capacitor. Compare the measured capacitance to the value printed on the capacitor label. A reading more than 10% below the rated value indicates a failed capacitor that must be replaced.

4. **Check the fan motor winding resistance.** Disconnect the motor from the board and use a multimeter to measure resistance across each motor winding terminal pair. An open circuit (OL) on any winding indicates a failed motor. A reading of zero ohms indicates a short.

5. **Inspect the Hall sensor wiring harness.** On BLDC fan motors, trace the thin Hall sensor cable from the motor to the indoor PCB connector. Look for pinched, chafed, or corroded wires. Unplug the connector and check the pins for corrosion or bent contacts.

6. **Test the indoor PCB.** If the motor and capacitor check out, connect a known-good fan motor (from a parts unit or tested spare) and see if the H6 clears. If it does, the PCB is the problem. Replacing the indoor control board is the final step.

## How to Fix It

- **Foreign object obstruction:** Remove the obstruction and test. No parts needed.
- **Failed capacitor:** Replace the run capacitor — this is a low-cost, DIY-friendly fix on units with accessible capacitors.
- **Failed fan motor:** Replace the indoor blower motor with an OEM or compatible replacement. Match the motor's voltage, RPM, shaft size, and rotation direction exactly.
- **Hall sensor wiring:** Repair or replace the harness. Heat-shrink all repair splices.
- **Indoor PCB:** Replace the control board with an OEM Daikin PCB for your specific model number.

## Parts You May Need {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Daikin Indoor Fan Motor (BLDC or AC) | $100–$250 | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-daikin-h6-error-code&tag=errorcodefixes-20) |
| Run Capacitor (fan motor, various uF) | $8–$25 | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-daikin-h6-error-code&tag=errorcodefixes-20) |
| Daikin Indoor Control Board (PCB) | $120–$350 | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-daikin-h6-error-code&tag=errorcodefixes-20) |
| Capacitance Meter / Multimeter | $20–$60 | [Amazon](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-daikin-h6-error-code&tag=errorcodefixes-20) |

## When to Call a Technician

Replacing an indoor fan motor requires opening the indoor unit, removing the blower wheel assembly, and working with live 240V wiring. While a confident DIYer can handle this with proper safety precautions (power off, breaker locked out), most homeowners should have a licensed HVAC technician perform the repair. Board replacement in particular can be risky on VRV/VRF systems, where incorrect board installation can cause communication faults with the rest of the multi-zone system.

> **Pro tip:** On Daikin cassette units and ducted air handlers, H6 faults are frequently caused by a partially blocked return air filter that has been ignored for years. The motor isn't actually failed — it's working against so much airflow restriction that it overloads and triggers the overcurrent protection, which the board reads as a lock fault. Always check the filter before condemning the motor.

## Related Error Codes

- [Daikin J3 Error Code — Discharge Pipe Temperature Sensor Fault](/posts/daikin-j3-error-code/)
- [Daikin E7 Error Code — Outdoor Fan Motor Fault](/posts/daikin-e7-error-code/)
- [Daikin U4 Error Code — Communication Fault](/posts/daikin-u4-error-code/)
- [All Daikin Mini-Split Error Codes](/posts/daikin-mini-split-error-codes/)
