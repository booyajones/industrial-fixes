---
title: "Fujitsu E:37 Error Code - Causes & Fix"
description: "E:37 on Fujitsu mini-splits likely indicates a room-air thermistor short. Most common fix: replace the return-air thermistor sensor."
pubDatetime: 2026-05-31T01:06:50Z
modDatetime: 2026-05-31T01:06:50Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu E:37 Error Code — What It Means

The E:37 code on Fujitsu mini-split systems is not consistently documented across all public manuals, but it closely resembles the E3 or E03 fault, which signals a shorted return-air (room-air) thermistor. The indoor unit cannot read valid room temperature because the sensor circuit is sending an invalid signal. This prevents the system from controlling heating or cooling properly, so the unit shuts down to protect itself. If your display shows E:37 and not E3, verify the exact code format on your wired remote or indoor LED, as Fujitsu uses different code families depending on the controller and model year.

[Jump to Fix](#fix)

## Common Causes

- **Shorted return-air thermistor** The temperature sensor on the indoor coil or in the return-air stream has failed internally or is reading zero resistance due to a short circuit.
- **Damaged sensor wiring or harness** The wire running from the thermistor to the indoor control board is pinched, cut, or shorted against metal, causing a false short reading.
- **Loose or corroded sensor connector** The plug at the thermistor or at the indoor PCB is not fully seated, or corrosion on the pins is creating an intermittent short.
- **Indoor control board fault** The main PCB itself has a failed input circuit that incorrectly reads the thermistor signal as shorted even when the sensor is good.

## Step-by-Step Fix {#fix}

1. **Verify the exact error code** by checking both the indoor unit LED display and any wired or wireless remote, and note your indoor unit model number to confirm the fault definition.
2. **Power off the system** at the breaker or disconnect switch and wait 60 seconds to clear any transient faults before beginning inspection.
3. **Access the indoor unit** by removing the front cover and filter, then locate the return-air thermistor (a small bead sensor with two thin wires, usually clipped to the evaporator coil or tucked in the return-air stream).
4. **Inspect the sensor connector and wiring** for obvious damage, loose seating, corrosion, or pinch points, and reseat the connector firmly at both the sensor and the indoor control board.
5. **Measure the thermistor resistance** by unplugging it from the board and using a multimeter set to ohms, then compare the reading at room temperature against your model's thermistor table (consult your service manual for the exact curve).
6. **Check for 5 V at the sensor input** on the main PCB with the sensor unplugged (if your model uses this diagnostic method). If 5 V is present, the sensor or harness is likely at fault. If not, suspect the control board.
7. **Replace the failed component** (thermistor, harness, or indoor PCB), restore power, and confirm the error clears and the unit resumes normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fujitsu return-air thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-37-error-code&k=Fujitsu+return-air+thermistor&tag=errorcodefixes-20) \| Match the part number printed on your original sensor or in your model's service parts list. |
| Indoor control board (main PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-37-error-code&k=Indoor+control+board+%28main+PCB%29&tag=errorcodefixes-20) \| Only if the thermistor and wiring test correctly and the board shows no sensor voltage or fails the conduction test. |

## When to Call a Pro

If you are not comfortable working inside the indoor unit, measuring resistance with a multimeter, or interpreting your model's thermistor resistance table, call a qualified HVAC technician. Also call a pro if the sensor and wiring check out but the fault persists, since diagnosing a control board fault requires specialized tools and an understanding of your specific Fujitsu model's circuitry. If your code is truly E:37 and not E3, a technician with access to Fujitsu's full service literature can confirm the exact fault definition for your controller type.
