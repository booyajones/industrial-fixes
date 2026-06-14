---
title: "Fujitsu E:73 Error Code - Causes & Fix"
description: "E:73 means the outdoor coil temperature sensor circuit is open, shorted, or out of range. Most often it's a loose connector or bad sensor."
pubDatetime: 2026-05-31T01:15:46Z
modDatetime: 2026-05-31T01:15:46Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Outdoor heat exchanger temperature thermistor"
most_likely_cause: "Open or shorted thermistor"
---

## Fujitsu E:73 Error Code — What It Means

E:73 on a Fujitsu mini-split is an outdoor unit heat exchanger temperature thermistor error. The thermistor is the temperature sensor attached to the outdoor coil that tells the control board how hot or cold the coil is running. When you see this code, the outdoor controller has detected that the sensor circuit is open, shorted, miswired, or reading a value outside normal range.

This fault stops the system from running safely because the board can't monitor coil temperature to prevent freeze-ups or overheating. The code usually points to a failed sensor, a loose or corroded connector at the outdoor board, or damaged wiring between the sensor and the board. In some cases the sensor and wiring test fine but the outdoor controller board itself has a bad input circuit and needs replacement.

[Jump to Fix](#fix)

## Common Causes

- **Open or shorted thermistor** The heat exchanger temperature sensor itself has failed internally and reads infinite resistance (open) or near-zero resistance (shorted).
- **Loose or removed connector** The sensor connector at the outdoor PCB has backed out, corroded, or was left unplugged during earlier service work.
- **Damaged thermistor wiring** The wire harness running from the outdoor coil sensor to the control board has a break, chafe, or cut that opens the circuit.
- **Miswired or incorrect sensor connection** The thermistor connector was plugged into the wrong header on the outdoor board, or pins are bent or pushed back in the housing.
- **Defective outdoor controller PCB** The outdoor main board has a failed sensor input circuit and reads the thermistor incorrectly even when the sensor and wiring test good.

## Step-by-Step Fix {#fix}

1. **Power off the system** at the circuit breaker and the outdoor disconnect, then remove the outdoor unit cover to access the control board and sensor wiring.
2. **Inspect the thermistor connector** at the outdoor PCB for looseness, corrosion, pushed-back pins, or damage, and verify it is seated firmly in the correct header.
3. **Trace the thermistor harness** from the outdoor coil back to the board and check for cuts, chafes, pinches, or breaks in the wire insulation.
4. **Disconnect the thermistor connector** and use a multimeter to measure the resistance across the sensor leads, then compare the reading to Fujitsu's thermistor characteristics table for the ambient temperature (consult your model's service manual for the table).
5. **Check for open or short** by confirming the resistance is neither infinite (open) nor near-zero (shorted), and verify the harness wiring shows continuity from sensor to board with the sensor unplugged.
6. **Replace the outdoor heat exchanger thermistor** if it reads open, shorted, or out of spec, or replace the thermistor harness if you found a wire break or damaged connector.
7. **Replace the outdoor controller PCB** if the sensor and all wiring test correctly but the E:73 code persists after reconnecting and powering up.
8. **Restore power and run a test cycle** to confirm the error clears and the outdoor unit regulates coil temperature normally without faulting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor heat exchanger temperature thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-73-error-code&k=Outdoor+heat+exchanger+temperature+thermistor&tag=errorcodefixes-20) \| The coil-mounted sensor. Verify your model and serial number to get the correct thermistor for your outdoor unit. |
| Outdoor controller PCB / main board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-73-error-code&k=Outdoor+controller+PCB+%2F+main+board&tag=errorcodefixes-20) \| Required only if sensor and wiring test good but fault remains. Confirm board part number from the label on your existing PCB. |
| Thermistor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-73-error-code&k=Thermistor+wiring+harness&tag=errorcodefixes-20) \| Needed if the wire between sensor and board is cut, chafed, or the connector housing is cracked. |

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working inside energized equipment, if you do not have a multimeter and the thermistor resistance table for your model, or if the code returns after you have verified the sensor and wiring. Refrigerant-side work is not required for this repair, but misdiagnosing a board or sensor can waste money on unnecessary parts. A pro can compare live resistance readings to the factory table, check board input voltages, and confirm the repair with a full system checkout.
