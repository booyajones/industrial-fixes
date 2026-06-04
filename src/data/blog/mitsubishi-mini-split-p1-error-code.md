---
title: "Mitsubishi Mini Split P1 Error - Causes & Fix"
description: "P1 on Mitsubishi mini splits typically signals a room temperature sensor or thermistor fault. Check sensor wiring and resistance first."
pubDatetime: 2026-05-31T00:49:23Z
modDatetime: 2026-05-31T00:49:23Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi Mini Split P1 Error — What It Means

The P1 error code on Mitsubishi mini split systems most commonly indicates a room temperature sensor or thermistor problem. The control board expects to receive a signal from the indoor temperature sensor, but either the sensor itself has failed, the wiring is loose or damaged, or the controller is configured to look for a sensor that is not installed. Because Mitsubishi uses different fault definitions across product lines, always verify your exact indoor unit model number and consult the specific service manual to confirm the P1 definition for your system.

In systems like the Ecodan heat pump, P1 specifically flags a mismatch between the sensor source selected in the controller menu and the physical sensor present. In other Mitsubishi mini splits, P1 points to a thermistor circuit fault, a broken sensor, or corroded connections. The system cannot operate in auto or heating mode without a valid room temperature reading, so the unit will stop or refuse to start until the sensor circuit is repaired.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect sensor configuration in the controller** The controller menu is set to read from a room sensor (such as TH1 or external thermistor) that is not physically installed or connected, triggering P1.
- **Loose or disconnected thermistor wiring** The sensor plug at the indoor unit board or along the harness has worked loose, corroded, or backed out of its connector.
- **Failed room temperature thermistor** The thermistor itself is shorted, open, or reading resistance values outside the acceptable range for the current temperature.
- **Damaged sensor cable or insulation** The wire insulation is pinched, chewed, or broken, causing intermittent opens or shorts that confuse the control board.
- **Faulty indoor control board sensor input** After verifying the sensor and wiring are good, the PCB sensor circuit itself may have failed and cannot read a valid signal.

## Step-by-Step Fix {#fix}

1. **Identify your exact model number** from the nameplate on the indoor unit and download the matching Mitsubishi service manual or error-code table to confirm the P1 definition for your product line.
2. **Turn off power** at the breaker or disconnect switch and wait two minutes before opening the indoor unit cover to access the control board and sensor connections.
3. **Inspect the thermistor connector** at the indoor PCB for loose pins, corrosion, or moisture, and trace the sensor wire back to the sensor itself to check for pinched or damaged insulation.
4. **Measure the room thermistor resistance** with a multimeter set to ohms, then compare the reading to the factory table (for example, Mitsubishi Mr. Slim sensors typically show 15 kΩ at 32°F, 9.6 kΩ at 50°F, 6.3 kΩ at 68°F, 4.3 kΩ at 86°F, and 3.0 kΩ at 104°F).
5. **Check the controller sensor-source setting** if your system has a configuration menu, and change the selection from an external sensor (TH1) to the main indoor thermistor (often labeled RC or internal) if no external sensor is installed.
6. **Replace the thermistor** if the resistance is open, shorted, or far outside the expected range for the room temperature, using the exact Mitsubishi part number for your model.
7. **Test the system** by restoring power, running a heating or cooling cycle, and confirming the display shows the correct room temperature without returning the P1 fault.
8. **Replace the indoor control board** only if the sensor tests good, the wiring is intact, and the P1 error persists after verifying all connections and settings.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Mitsubishi room temperature thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-p1-error-code&k=Mitsubishi+room+temperature+thermistor&tag=errorcodefixes-20) \| Match the part number to your exact indoor unit model, typically a two-wire sensor assembly. |
| Thermistor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-p1-error-code&k=Thermistor+wiring+harness&tag=errorcodefixes-20) \| Order if the cable insulation is damaged or the connector housing is cracked or corroded. |
| Indoor unit control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mini-split-p1-error-code&k=Indoor+unit+control+board+%28PCB%29&tag=errorcodefixes-20) \| Replace only after confirming the sensor and all wiring test within specification. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working inside the indoor unit with power off, if you do not own a multimeter or cannot interpret resistance tables, or if the P1 fault returns after you have verified the sensor resistance and all connections. A pro can cross-reference your exact Mitsubishi model number to the factory code definition, use specialized software to read additional fault history, and stock the correct OEM thermistor and control board for same-day repair. Also call if the system is under warranty, since DIY sensor replacement may void coverage.
