---
title: "Carrier Heat Pump E14 Error Code - Causes & Fix"
description: "E14 means tank temperature sensor fault on many Carrier heat pumps. Most common fix: check the sensor connector and replace sensor if damaged."
pubDatetime: 2026-05-31T14:51:23Z
modDatetime: 2026-05-31T14:51:23Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - carrier
money_part: "Tank temperature sensor / thermistor"
---

## Carrier Heat Pump E14 Error Code — What It Means

The E14 error code on Carrier heat pumps typically indicates a tank temperature sensor or thermistor fault, though the exact meaning can vary by model family and control platform. The unit is detecting an open circuit, short, disconnection, or out-of-range signal from the temperature sensor input. This prevents the system from accurately monitoring operating temperature and can shut down heating or cooling operation until the fault is corrected. Always confirm the code definition in your specific model's technical documentation, as Carrier uses different fault tables across product lines.

[Jump to Fix](#fix)

## Common Causes

- **Loose or disconnected sensor plug** The temperature sensor connector has backed out, become unseated, or was not fully engaged during previous service.
- **Damaged sensor wiring** The harness between the sensor and control board has been pinched, cut, abraded, or has developed a break in one or both wires.
- **Failed thermistor** The temperature sensor itself has failed internally, reading open circuit, shorted, or drifted significantly out of its normal resistance range.
- **Corrosion at connector terminals** Moisture intrusion or age has caused oxidation on the pins or socket, creating intermittent or high-resistance contact.
- **Control board sensor circuit fault** The PCB input for the sensor has failed even though the sensor and wiring test correctly, requiring board-level diagnosis or replacement.

## Step-by-Step Fix {#fix}

1. **Verify the code definition** for your exact Carrier model by consulting the technical manual or wiring diagram, as E14 may have different meanings across product families.
2. **Power off the unit** at the breaker and remove the access panel to reach the indoor or outdoor electronics compartment where the control board and sensor connections are located.
3. **Locate the tank temperature sensor connector** using the wiring diagram and inspect the plug and socket for looseness, corrosion, or physical damage, then disconnect and reconnect firmly.
4. **Measure sensor resistance** with a multimeter across the sensor terminals after unplugging it, looking for a reading near 5 kΩ at room temperature (the cited platform used a ±1.5 kΩ tolerance, but consult your model's spec).
5. **Replace the temperature sensor** if it reads open, shorted, or far outside the expected range, or if the sensor body shows physical damage or a cracked housing.
6. **Check control board sensor supply** if the sensor tests good but the code persists, measuring for the expected reference voltage (5 V in the cited example) and confirming continuity on both sensor wires back to the PCB.
7. **Restore power and test** by turning the breaker back on, restarting the heat pump, and confirming that E14 clears and the unit resumes normal heating or cooling operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Tank temperature sensor / thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-heat-pump-e14-error-code&k=Tank+temperature+sensor+%2F+thermistor&tag=errorcodefixes-20) \| Match the connector type and resistance spec to your Carrier model and control board platform. |
| Main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-heat-pump-e14-error-code&k=Main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Only if sensor and wiring test correctly but the E14 fault remains after replacement. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with line-voltage electrical components or if the error code definition does not match the tank sensor fault described here. A pro should also diagnose the system if the sensor tests within spec, the wiring shows continuity, but the E14 code will not clear, as this points to a control board issue requiring board-level testing and possibly refrigerant-side work. Professional service is also recommended if your heat pump is under warranty, since DIY sensor replacement may void coverage on some Carrier models.

## See Also

- [Carrier 23 Error Code — Draft Safeguard Switch Fault](/posts/carrier-23-error-code/)
- [Carrier 59TN6 Furnace Problems & Error Codes](/posts/carrier-59tn6-furnace-gas-residential-problems/)
- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier Error Code 34 - Ignition Proving Failure Fix](/posts/carrier-furnace-34-error-code/)
