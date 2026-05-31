---
title: "Honeywell Thermostat E1 Error Code — Sensor Fault Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: honeywell-thermostat-e1-error-code-sensor-fault
featured: false
draft: false
tags:
  - hvac
  - honeywell
  - thermostat
  - sensor-fault
description: "Honeywell thermostat E1 error code means an internal sensor fault on T6, T9, and T10 Pro series — here's what it means and how to fix it."
---

## Error Code: Honeywell Thermostat E1

**What it means:** The E1 error code on Honeywell T-series thermostats (T6 Pro, T9, T10 Pro, and related models) indicates an internal temperature sensor fault. The thermostat's onboard NTC thermistor — the sensor that reads room temperature — has failed, gone out of range, or is reading implausible values. When E1 appears, the thermostat can no longer measure ambient temperature accurately and will not control heating or cooling reliably.

On the T6 Pro (TH6320U2008 / TH6220U2000), E1 appears as a static error on the main display. On the T9 and T10 Pro (with HomeKit/Smart Room Sensor support), E1 may also appear in the Honeywell Home app as a device alert.

Unlike external sensor errors (which can sometimes be resolved by repositioning a remote sensor), E1 is an internal hardware fault. The thermistor is integrated into the thermostat's PCB and is not user-serviceable.

## Common Causes

- **Failed internal NTC thermistor** — The most common cause. The thermistor's resistance drifts outside the valid range (typically 10 kΩ at 25°C for Honeywell units), and the firmware flags it as a fault.
- **Water or humidity damage** — Condensation, a nearby humidifier, or a leaking HVAC system can corrode the thermostat's PCB and cause the sensor to fail.
- **Extreme temperature exposure** — Installing a thermostat in direct sunlight, near an exterior wall, or close to a heat register can cause the sensor to read out of range.
- **Firmware corruption (rare)** — On the T9 and T10 Pro, a failed OTA firmware update can occasionally produce sensor-related errors. A factory reset may resolve this before condemning the hardware.
- **Age and normal component wear** — Thermostats have a typical service life of 10–15 years. An E1 fault on an older unit is often a sign of end-of-life.

## Step-by-Step Fix {#step-by-step-fix}

1. **Perform a soft reset first.** On the T6 Pro: press and hold the Menu button for 5 seconds until "Reset" appears, then select "Factory Reset." On the T9/T10 Pro: go to Settings → Reset → Factory Reset. This clears any firmware glitch before you declare the hardware dead.

2. **Remove the thermostat from the wall plate and inspect for moisture.** Pull the thermostat body off its wall plate (it snaps off without tools on all T-series models). Look at the back of the thermostat and the wall plate for signs of water staining, corrosion on terminals, or condensation. If moisture is present, dry it out with compressed air, address the source of moisture, and re-evaluate.

3. **Check the installation location.** Is the thermostat in direct sunlight at any point in the day? Is it on an exterior wall where it might read outdoor cold? Is it within 3 feet of a supply air register blowing hot or cold air directly at it? Any of these will cause temperature reading errors. Relocate if possible — though a true E1 internal fault won't be resolved by relocation alone.

4. **Verify the thermostat hasn't been mis-wired.** On a T6 Pro with a C-wire, confirm the C terminal is providing a stable 24VAC common. A floating C terminal can cause erratic behavior including sensor errors on some firmware versions.

5. **On T9/T10 Pro: check for a pending firmware update.** Open the Honeywell Home app, go to the thermostat settings, and check for available updates. Apply any pending updates and allow the unit to reboot. Check if E1 clears.

6. **If E1 persists after reset and inspection: replace the thermostat.** The internal sensor is not a serviceable component. The Honeywell T6 Pro (TH6320U2008) is the direct OEM replacement for most installations using the same 2H/2C wiring. It runs about $75 and installs in 20 minutes.

7. **Document your wiring before removal.** Take a clear photo of your existing wiring terminals before pulling the thermostat. T-series models label terminals R, C, Y, Y2, W, W2, G, O/B — photograph these before disconnecting. An incorrectly re-wired thermostat will not work even if the hardware is perfect.

8. **Register the new thermostat.** Honeywell's app-connected thermostats (T9, T10 Pro) require re-registration in the Honeywell Home app after replacement. Have your Wi-Fi password ready and allow 10 minutes for the setup process.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Honeywell T6 Pro Thermostat | TH6320U2008 | $70–$85 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-thermostat-e1-error-code-sensor-fault&k=TH6320U2008+Honeywell+T6+Pro+Thermostat&tag=errorcodefixes-20) \| Amazon / Home Depot |
| Honeywell T9 Smart Thermostat | RTH9585WF | $130–$160 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-thermostat-e1-error-code-sensor-fault&k=RTH9585WF+Honeywell+T9+Smart+Thermostat&tag=errorcodefixes-20) \| Amazon / Best Buy |
| Honeywell T10 Pro Thermostat | THX321WFS | $150–$190 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-thermostat-e1-error-code-sensor-fault&k=THX321WFS+Honeywell+T10+Pro+Thermostat&tag=errorcodefixes-20) \| Amazon / Home Depot |
| Smart Room Sensor (T9/T10) | RCHTSENSOR-1PK | $28–$35 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-honeywell-thermostat-e1-error-code-sensor-fault&k=RCHTSENSOR-1PK+Smart+Room+Sensor+%28T9%2FT10%29&tag=errorcodefixes-20) \| Amazon |
## When to Call a Professional

If you're not comfortable with low-voltage thermostat wiring — specifically identifying and labeling your R, C, Y, W, G, and O/B wires — call an HVAC technician to handle the replacement. A mis-wired thermostat can damage the control board on your air handler or furnace (particularly if the R and C terminals are shorted). If your system uses proprietary wiring (Carrier Infinity, Lennox iComfort, or Trane ComfortLink), a standard Honeywell thermostat is not a compatible replacement and you'll need the same-brand smart thermostat from an authorized dealer.

> **Pro tip:** If your T6 Pro shows E1 only when the furnace runs and clears when the system is idle, check whether the thermostat is mounted directly to drywall over a cold exterior wall cavity. The temperature differential between a running system and an idle one can push a marginally functioning thermistor in and out of range. Add a thin foam gasket behind the wall plate as an insulating barrier — this solves roughly 10% of T6 Pro E1 calls.
