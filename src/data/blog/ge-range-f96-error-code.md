---
title: "GE Range F96 Error Code - Causes & Fix"
description: "F96 means the upper oven cooling fan speed is too low. Usually caused by a failed fan motor, bad sensor, or wiring issue."
pubDatetime: 2026-05-31T06:42:01Z
modDatetime: 2026-05-31T06:42:01Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - appliance
  - oven
  - ge
---

## GE Range F96 Error Code — What It Means

The F96 error code on GE wall ovens and double ovens indicates that the upper oven cooling fan speed has dropped below the minimum threshold for about 30 seconds. The control board monitors fan speed through a sensor or Hall-effect device mounted on the fan assembly. When the fan does not spin fast enough or the control does not receive the expected feedback signal, the oven throws F96 and may shut down to prevent overheating. This is not a generic oven fault. It points specifically to a problem in the upper cooling fan circuit, either mechanical or electrical.

[Jump to Fix](#fix)

## Common Causes

- **Failed upper cooling fan motor** The blower motor itself has worn bearings, a burned winding, or has seized and cannot reach operating speed.
- **Bad fan speed sensor or Hall sensor** The sensor board mounted on the fan assembly no longer generates the pulse signal the control expects, even when the fan spins.
- **Obstructed or binding fan rotation** Debris, grease buildup, or a warped blade prevents the fan from spinning freely and reaching minimum RPM.
- **Loose or damaged wiring and connectors** A corroded pin, broken wire, or loose harness connection interrupts the feedback or power signal between the fan and control board.
- **Faulty FAD or main control board** The fan-drive board or machine control does not correctly send the drive signal or interpret the sensor feedback, even when the fan and sensor are good.

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the breaker and verify zero voltage with a multimeter before opening any panels.
2. **Access the upper cooling fan** by removing the oven's rear or top service panel, depending on your model, and locate the fan assembly mounted near the upper oven cavity.
3. **Inspect the fan for physical obstruction**, binding, or debris that would prevent free rotation, and manually spin the blade to confirm smooth movement.
4. **Check the wiring harness and connectors** at the fan motor and sensor for corrosion, loose pins, or damaged insulation, and reseat all connections firmly.
5. **Measure the fan control signal** at the FAD board connector if your model uses one, looking for a 5 V pulse between Pin 1 and Pin 2 or Pin 2 and Pin 3 as specified in GE service literature.
6. **Test the fan motor and sensor** by applying power and observing whether the fan starts and ramps to speed, then use a multimeter to confirm the sensor is generating a pulse or AC waveform at its output during rotation.
7. **Replace the cooling fan assembly** if the motor is seized or the sensor gives no signal, or replace the FAD or main control board if the fan and sensor check good but the fault persists.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Upper cooling fan / blower motor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f96-error-code&k=Upper+cooling+fan+%2F+blower+motor+assembly&tag=errorcodefixes-20) \| Match your model number. Some include the sensor board, others require separate transfer of the Hall sensor or mounting bracket. |
| Fan speed sensor / Hall-effect sensor board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f96-error-code&k=Fan+speed+sensor+%2F+Hall-effect+sensor+board&tag=errorcodefixes-20) \| Order separately if your fan assembly does not include it integrated. Verify connector type and mounting tabs. |
| FAD board or fan-drive control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f96-error-code&k=FAD+board+or+fan-drive+control+board&tag=errorcodefixes-20) \| Used on certain GE models to regulate fan speed. Consult your wiring diagram to confirm if your oven uses this board. |
| Main electronic control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-ge-range-f96-error-code&k=Main+electronic+control+board&tag=errorcodefixes-20) \| Replace if all fan components and wiring test good but the F96 fault remains after fan replacement. |

## When to Call a Pro

Call a qualified appliance technician if you are uncomfortable working inside a 240 V appliance, if access to the upper fan requires disassembly of gas or high-voltage components you cannot isolate safely, or if you have replaced the fan assembly and checked all connectors but the F96 code returns. Diagnosing control-board faults and tracing low-voltage sensor signals requires a multimeter and familiarity with your model's wiring schematic. A technician has model-specific service manuals, the correct OEM parts cross-references, and the tools to test pulse signals and board outputs accurately.
