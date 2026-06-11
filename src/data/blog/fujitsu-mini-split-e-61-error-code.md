---
title: "Fujitsu E:61 Error Code - Causes & Fix"
description: "E:61 means a faulty indoor room temperature sensor circuit. Most common fix: reseat the sensor connector or replace the thermistor."
pubDatetime: 2026-05-31T01:12:56Z
modDatetime: 2026-05-31T01:12:56Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - fujitsu
money_part: "Room temperature thermistor (10 kΩ at 25°C)"
---

## Fujitsu E:61 Error Code — What It Means

E:61 on a Fujitsu mini-split indicates a fault in the indoor unit's room temperature sensing circuit. The system has detected that the room thermistor (temperature sensor) is reading out of range, disconnected, open, shorted, or the signal path between the sensor and the indoor control board is broken. This is an electrical sensor problem, not a refrigerant or compressor issue. The fault prevents the unit from accurately reading room temperature, so the system cannot maintain the setpoint and will shut down or refuse to start.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded sensor connector** The plug at the indoor PCB or at the sensor body has backed out, oxidized, or lost contact due to vibration or moisture.
- **Failed room thermistor** The thermistor itself has drifted out of tolerance, opened internally, or shorted from age or moisture exposure.
- **Broken or damaged sensor wiring** The harness between the sensor and the board has been pinched, cut, or corroded, creating an open or intermittent connection.
- **Shorted sensor circuit** Damaged insulation or moisture in the connector has caused the sensor leads to short together or to ground.
- **Indoor control board fault** The board is not supplying the correct reference voltage to the sensor or cannot read the sensor signal correctly even when the sensor is good.

## Step-by-Step Fix {#fix}

1. **Power off the indoor unit** at the breaker or disconnect before touching any sensor wiring or connectors to avoid shock or board damage.
2. **Locate the room temperature sensor** on the indoor unit (usually clipped near the return air inlet or mounted on the evaporator housing) and trace its wire to the indoor control board connector.
3. **Inspect both ends of the sensor connector** for loose pins, corrosion, moisture, or backed-out terminals, then unplug and firmly reseat the connector at the board and sensor.
4. **Measure the thermistor resistance** with a multimeter across the sensor leads (disconnect the sensor from the board first), then compare the reading to the expected value for your model (typically 10 kΩ at 25°C for Fujitsu room sensors).
5. **Wiggle-test the sensor harness** while watching the resistance reading to reveal intermittent opens or shorts caused by broken internal conductors or damaged insulation.
6. **Check the board-side sensor supply voltage** at the unplugged sensor connector (power the unit back on briefly), looking for approximately 5 V DC at the board side of the plug.
7. **Replace the failed component**: if the sensor is open, shorted, or out of tolerance, install a new room thermistor. If the sensor tests good but the board supply voltage is missing or incorrect, replace the indoor control board.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Room temperature thermistor (10 kΩ at 25°C) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-61-error-code&k=Room+temperature+thermistor+%2810+k%CE%A9+at+25%C2%B0C%29&tag=errorcodefixes-20) \| Match the part number for your specific Fujitsu model and confirm resistance spec. |
| Sensor wiring harness or connector terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-61-error-code&k=Sensor+wiring+harness+or+connector+terminals&tag=errorcodefixes-20) \| Use if the plug or wire is damaged and cannot be repaired. |
| Indoor control PCB / main board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-61-error-code&k=Indoor+control+PCB+%2F+main+board&tag=errorcodefixes-20) \| Required only if the sensor and wiring test good but the board does not supply 5 V or read the sensor correctly. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with live voltage, measuring thermistor resistance, or opening the indoor unit cabinet. A pro can quickly test the sensor circuit, verify board voltages, and confirm the correct replacement part number for your specific Fujitsu model. If you have already replaced the sensor and the error persists, the indoor board is likely at fault and should be diagnosed and replaced by a qualified technician to avoid further damage or warranty issues.
