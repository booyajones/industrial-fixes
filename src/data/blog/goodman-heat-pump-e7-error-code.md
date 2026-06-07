---
title: "Goodman Heat Pump E7 Error Code - Causes & Fix"
description: "E7 on a Goodman heat pump likely signals an outdoor fan motor fault. Check fan motor wiring and operation first, then the control board."
pubDatetime: 2026-05-31T09:07:14Z
modDatetime: 2026-05-31T09:07:14Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - goodman
---

## Goodman Heat Pump E7 Error Code — What It Means

The E7 error code on Goodman heat pumps is most commonly associated with an outdoor fan motor fault, though the exact definition varies by model and platform. On some systems, E7 may instead indicate a communication error between the indoor and outdoor units, a mode conflict in multi-zone setups, or a control board issue. Because Goodman uses different control platforms across its product lines, you should verify the code meaning in your unit's specific service manual or on the label inside the outdoor unit's control panel. The outdoor fan motor interpretation is the most widely cited for Goodman, but always cross-reference with your model documentation before beginning repairs.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor fan motor** The motor may be seized, open-winding, shorted, or drawing abnormal current, preventing the outdoor coil from receiving airflow.
- **Loose or damaged wiring to the fan motor** Corroded terminals, loose connectors, pinched wires, or burned contacts at the motor or control board interrupt the command or feedback signal.
- **Faulty outdoor control board** The board may fail to send the correct voltage or PWM signal to the fan motor, or it may misinterpret feedback and log a fault even when the motor is functional.
- **Communication wiring fault (if E7 is a comm error on your model)** Damaged, disconnected, or miswired communication cables between indoor and outdoor units prevent the boards from synchronizing mode and status.
- **Power supply interruption or voltage sag** Low line voltage, a tripped breaker, or a blown fuse can starve the outdoor unit and trigger a fault before the motor even attempts to start.
- **Mode conflict in multi-zone systems** If one indoor head calls for heat while another calls for cool, the outdoor unit may lock out with an E7 communication or mode error.

## Step-by-Step Fix {#fix}

1. **Verify the code meaning** by locating your heat pump's model and serial number on the outdoor unit nameplate, then consulting the service manual or the diagnostic label inside the control box cover to confirm whether E7 is a fan-motor fault, communication fault, or another error on your exact platform.
2. **Power down the system** at the outdoor disconnect and the indoor breaker, wait 60 seconds, then restore power and observe whether the fault clears or reappears immediately, which helps distinguish a latched error from a recurring hardware problem.
3. **Inspect all wiring and connections** at the outdoor fan motor, the outdoor control board terminal block, and the communication harness between indoor and outdoor units for loose, corroded, burned, or pinched conductors, tightening or replacing any damaged wires or terminals.
4. **Test the outdoor fan motor** by checking for mechanical binding (spin the blade by hand with power off), measuring winding resistance if accessible, and verifying that the motor receives the correct voltage or PWM signal from the board when the unit attempts to run.
5. **Check communication wiring end-to-end** if your model uses E7 as a comm fault by tracing the low-voltage control cable from the indoor air handler to the outdoor unit, confirming polarity, inspecting for breaks or shorts, and reseating all plug connections.
6. **Evaluate the outdoor control board** by looking for visible damage such as burned traces, swollen capacitors, or corrosion, and by verifying that the board outputs the proper command voltage to the fan motor and receives valid feedback when the motor is known-good.
7. **Replace the failed component** once isolated, whether fan motor, control board, or communication harness, and clear any stored fault codes per the service manual procedure before returning the system to normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-heat-pump-e7-error-code&k=Outdoor+fan+motor&tag=errorcodefixes-20) \| Match voltage, RPM, and shaft diameter to the nameplate on your existing motor. |
| Outdoor control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-heat-pump-e7-error-code&k=Outdoor+control+board&tag=errorcodefixes-20) \| Order by the board part number printed on the board itself or listed in your model's parts breakdown. |
| Communication wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-heat-pump-e7-error-code&k=Communication+wiring+harness&tag=errorcodefixes-20) \| Use the correct conductor gauge and length specified for your indoor-outdoor distance. |
| Fan motor run capacitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-goodman-heat-pump-e7-error-code&k=Fan+motor+run+capacitor&tag=errorcodefixes-20) \| If the motor hums but does not spin, verify and replace the capacitor with the same µF and voltage rating. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working with line voltage, if you cannot safely access the outdoor unit's electrical compartment, or if basic wiring and power-cycle checks do not resolve the fault. A technician has the model-specific service literature, metering tools to test motor windings and board outputs accurately, and the refrigerant-handling certification required if fan-motor replacement involves disturbing refrigerant lines. Professional diagnosis is also recommended when the code meaning is ambiguous or when the unit cycles through multiple error codes, since those patterns often point to a failing inverter board or compressor-control issue that requires specialized troubleshooting.

## See Also

- [Goodman Furnace 3 Flashes — Pressure Switch Open Fix](/posts/goodman-furnace-3-flashes/)
- [Goodman Heat Pump Error Codes - What It Means and How to Fix It](/posts/goodman-heat-pump-error-codes/)
- [Goodman GVZC18 Heat Pump Error Codes: iQ Drive Fault Diagnostics](/posts/goodman-gvzc18-heat-pump-error-codes/)
- [Goodman Furnace Blowing Cold Air - Causes & Fix](/posts/goodman-furnace-blowing-cold-air/)
