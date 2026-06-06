---
title: "Daikin U2 Error Code - Causes & Fix"
description: "U2 means power supply failure or voltage drop. Most common fix: verify incoming power, then replace outdoor PCB if supply is good."
pubDatetime: 2026-05-31T08:57:01Z
modDatetime: 2026-05-31T08:57:01Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - daikin
---

## Daikin U2 Error Code — What It Means

The U2 code on a Daikin heat pump signals a malfunction of the power supply or an instantaneous power failure. The control system has detected that incoming power is missing, unstable, or dropped out long enough to register a protection fault. This is fundamentally a power, supply, or wiring alarm, not a compressor or refrigerant issue. Daikin's fault-code chart lists the underlying categories as abnormal power supply voltage, instantaneous power failure, and defective main circuit wiring between the indoor and outdoor unit.

[Jump to Fix](#fix)

## Common Causes

- **Low or missing supply voltage** The outdoor unit is not receiving proper power due to a utility issue, tripped breaker, failed disconnect, or upstream wiring problem.
- **Momentary power interruption** A voltage dip or brief outage lasting long enough for the control board to trip the U2 protection fault.
- **Defective main circuit wiring** Loose terminals, damaged conductors, or incorrect field wiring between the indoor and outdoor sections.
- **Outdoor PCB failure** The outdoor main control board is not properly distributing power internally even when supply voltage is present at the unit.
- **Power-section failure on the board** Internal fuses, PFC section, or power conversion components on the PCB have failed, preventing the board from energizing the system.
- **Condenser fan motor fault** A damaged or failed fan motor can contribute to the overall fault condition and may need replacement alongside the board.

## Step-by-Step Fix {#fix}

1. Turn off power at the breaker and outdoor disconnect, then visually inspect the disconnect, breaker panel, and outdoor unit for signs of damage or tripped protection devices.
2. Restore power and measure incoming line voltage at the outdoor disconnect and at the outdoor unit terminals using a multimeter to confirm proper supply voltage is reaching the unit.
3. Observe voltage while the unit attempts to start to check for voltage sag or dropout during operation, since U2 includes instantaneous power failure detection.
4. Inspect all field wiring and terminations between the indoor and outdoor units, looking for loose lugs, burned terminals, broken wires, or incorrect phase connections.
5. Check internal fuses and board power distribution by removing the outdoor unit service panel and testing for output from the PCB power sections when input supply is confirmed good.
6. Test the condenser fan motor and verify its harness and connector integrity if the board and supply voltage check out but the fan circuit is implicated.
7. Replace the outdoor main control board if proper input voltage is present but the board is not distributing power internally, then reassemble, restore power, and verify the unit runs normally and the fault clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-u2-error-code&k=Outdoor+main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match the part number on your existing board or consult your model's service manual for the correct replacement. |
| Condenser fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-u2-error-code&k=Condenser+fan+motor&tag=errorcodefixes-20) \| Often replaced together with the PCB in documented field repairs when the motor is damaged or contributing to the fault. |
| Main circuit wiring harness or terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-heat-pump-u2-error-code&k=Main+circuit+wiring+harness+or+terminals&tag=errorcodefixes-20) \| Repair or replace damaged conductors, connectors, or terminal lugs between indoor and outdoor units as needed. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with line voltage or if you cannot confirm proper supply voltage at the outdoor unit. If voltage is present and correct but the unit still shows U2, the outdoor PCB or internal power-section components likely need diagnosis and replacement, which requires technical training and proper tools. Because U2 is a power-supply fault, misdiagnosis or improper wiring repair can create safety hazards or further damage the system.

## See Also

- [Daikin C4 Error Code - Causes & Fix](/posts/daikin-heat-pump-c4-error-code/)
- [Daikin U0 Error Code - Causes & Fix](/posts/daikin-heat-pump-u0-error-code/)
- [Daikin VRV System Error Codes: Complete Guide](/posts/daikin-vrv-error-codes/)
- [Daikin Chiller Fault Codes — Complete Troubleshooting Guide](/posts/daikin-chiller-fault-codes/)
