---
title: "Mitsubishi P1 Error Code - Causes & Fix"
description: "P1 on Mitsubishi Ecodan heat pumps means a room sensor configuration mismatch. Check sensor source settings in the controller menu."
pubDatetime: 2026-05-31T08:52:34Z
modDatetime: 2026-05-31T08:52:34Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi P1 Error Code — What It Means

Mitsubishi uses different code definitions by product family, so P1 does not mean one thing across all units. On Ecodan hydronic heat pumps the code signals a room-temperature sensing or thermostat configuration problem in the control logic. The system is looking for a temperature input that is either missing or selected incorrectly in the controller settings. Some generic guides describe P1 as a power-supply voltage fault, but that interpretation is not manufacturer-confirmed for Ecodan and may apply to other Mitsubishi product lines. Always verify the exact meaning against your specific model's service documentation or Mitsubishi's official error-code lookup tool before diagnosing.

[Jump to Fix](#fix)

## Common Causes

- **Wrong room sensor source selected in controller** The unit is configured to read from TH1 thermistor when the installation actually uses the main RC or wireless controller as the room temperature source.
- **TH1 thermistor not fitted** The system expects a TH1 room sensor input but the thermistor was never installed or is disconnected.
- **Incorrect heating control mode** The controller is set to fixed flow temperature or weather compensation mode when the installation requires Auto adaptive or another mode for the sensor strategy to work correctly.
- **Sensor wiring fault** The thermistor or room controller cable is damaged, loose, or has corrosion at the connection terminals.
- **Wrong product-family interpretation** On non-Ecodan Mitsubishi models P1 may indicate a supply-voltage abnormality instead of a sensor fault, so always consult the specific model's error-code guide.

## Step-by-Step Fix {#fix}

1. **Confirm your exact model family** and look up P1 in the matching Mitsubishi service manual or online error-code tool, because code definitions vary by product line.
2. **Access the controller's initial settings menu** and navigate to the room sensor setting or sensor setting section to see which temperature input is currently selected.
3. **Check the heating control mode** to verify whether the system is in Auto adaptive, weather compensation, or fixed flow temperature mode, and confirm that mode matches the installation design.
4. **Change the room sensor source** if the controller shows TH1 but your installation uses the main RC or wireless controller as the room temperature input, then save and exit to the home screen.
5. **Verify TH1 thermistor installation** if the configuration requires it by inspecting the wiring connection at the controller and checking that the sensor is physically present and seated correctly.
6. **Test the live room temperature reading** on the home screen to confirm it changes normally when you alter room conditions or move a portable sensor, indicating the correct input is now active.
7. **Clear the fault code** and monitor for 24 hours to make sure the error does not return, and if it persists on a non-Ecodan model then check incoming supply voltage per that unit's service manual instead of sensor settings.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Mitsubishi TH1 room thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-p1-error-code&k=Mitsubishi+TH1+room+thermistor&tag=errorcodefixes-20) \| Required only if your controller is configured to use TH1 as the room temperature input and the sensor is missing or defective. |
| Mitsubishi wired room controller (main RC) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-p1-error-code&k=Mitsubishi+wired+room+controller+%28main+RC%29&tag=errorcodefixes-20) \| If the installation design calls for a wired controller as the temperature source and none is present or the unit is faulty. |
| Mitsubishi wireless room controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-p1-error-code&k=Mitsubishi+wireless+room+controller&tag=errorcodefixes-20) \| Alternative room temperature input if your system is configured for wireless control and the existing controller is not communicating. |

## When to Call a Pro

Call a qualified Mitsubishi installer if you are unsure which sensor configuration your system requires, if you cannot locate the initial settings menu on your controller, or if correcting the sensor source and heating mode does not clear the fault. Professional help is also necessary if your model documentation defines P1 as a voltage abnormality and you need to test incoming power supply, or if wiring inspection reveals damaged cables that require safe replacement and recommissioning of the heat pump.
