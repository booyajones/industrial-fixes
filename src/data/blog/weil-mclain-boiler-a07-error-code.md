---
title: "Weil-McLain A07 Error Code - Causes & Fix"
description: "A07 (E07) means flue gas sensor fault. The sensor or its wiring has failed. Most common fix: replace the flue gas temperature sensor."
pubDatetime: 2026-07-01T09:45:56Z
modDatetime: 2026-07-01T09:45:56Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - boiler
  - weil-mclain
money_part: "Flue gas temperature sensor (Weil-McLain)"
most_likely_cause: "Failed flue gas temperature sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect the sensor wiring at the control board for loose, corroded, or disengaged terminals"
  - "Check the sensor harness visually for pinched, cut, or damaged wires along its length"
part_price: "$40-90"
---

## Weil-McLain A07 Error Code — What It Means

The A07 or E07 error code on a Weil-McLain boiler indicates a flue gas sensor fault. The boiler's control module has detected an abnormality in the signal from the flue gas temperature sensor, typically a break in the circuit, a short circuit, or a temperature reading outside the valid operating range. This sensor is usually a thermistor or thermocouple located in the flue path or exhaust manifold that monitors the temperature of the combustion gases.

This is a high-urgency safety lockout. The boiler will stop firing immediately to prevent unmonitored combustion or overheating conditions. The system cannot resume normal operation until the fault is diagnosed and the lockout is reset.

## Before You Replace Anything

Some technicians replace the control board first, but a simple resistance check of the sensor with a multimeter (looking for open or zero ohms) identifies a failed sensor in minutes and costs far less than a board.

[Jump to Fix](#fix)

## Common Causes

- **Failed flue gas sensor (~60%)** The thermistor or thermocouple in the flue path has degraded internally and no longer provides a valid resistance signal.
- **Loose or corroded wiring (~20%)** The sensor wire connection at the control board or sensor harness has become loose, corroded, or disengaged.
- **Damaged wiring harness (~10%)** The harness connecting the sensor to the board is pinched, cut, or has an internal short circuit.
- **Control board input circuit fault (~7%)** The main control module's sensor input circuit is defective, though this is less common if the sensor checks out.
- **Erratic readings from flue blockage (~3%)** A severe flue blockage can cause the sensor to report impossible values that trigger the fault, though this more often causes other codes.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are the wires at the control board and sensor connector clean, tight, and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring connections are likely not the issue. Proceed to test the sensor resistance.<br><strong>No:</strong> Clean and reseat all connections, restore power, and reset the lockout. If the fault returns, test the sensor resistance.</div>
</details>

<details class="dtree"><summary>Does the sensor measure between 2,000 and 10,000 ohms at room temperature (consult your model manual for the exact spec)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is likely good. Check the harness for shorts or opens, or suspect the control board.<br><strong>No:</strong> The sensor is defective (open or shorted). Replace it and reset the lockout.</div>
</details>

<details class="dtree"><summary>After replacing the sensor, does the boiler complete a full startup cycle without the fault returning?</summary>
<div class="dtree-body"><strong>Yes:</strong> The repair is complete. Monitor the boiler for proper operation.<br><strong>No:</strong> The harness or control board may be at fault. Call a licensed technician to diagnose the board or wiring.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power and gas.** Switch off electrical power at the breaker and close the manual gas valve to the boiler.
2. **Open the control panel.** Remove the access cover to expose the main control board and sensor wiring.
3. **Inspect wiring connections.** Look for loose, corroded, or burned terminals at the control board and sensor connector. Clean and reseat any suspect connections.
4. **Disconnect the sensor.** Unplug or disconnect the two sensor wires from the control board terminals.
5. **Measure sensor resistance.** Use a multimeter set to ohms and measure across the two sensor terminals. Compare the reading to your model's specification (typically 2,000 to 10,000 ohms at room temperature). If the meter shows open (infinite) or zero ohms, the sensor is defective.
6. **Check the harness (if sensor is good).** Measure the resistance of the wiring harness from the board to the sensor to confirm it is not open or shorted.
7. **Replace the defective part.** Install a new flue gas sensor (or harness if that is the fault) and reconnect all wiring.
8. **Restore power and reset.** Turn on the breaker and gas supply, then reset the lockout by holding the reset button or cycling power. Verify the boiler runs through a complete startup cycle.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flue gas temperature sensor (Weil-McLain) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a07-error-code&k=Flue+gas+temperature+sensor+%28Weil-McLain%29&tag=errorcodefixes-20) \| Thermistor or thermocouple mounted in the flue path. Match your boiler model (Ultra, Aqua Balance, ECO, etc.). |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a07-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| If the harness is pinched, cut, or corroded and not repairable by cleaning. |

## When to Call a Pro

Call a licensed gas fitter or boiler technician for any work involving combustion components, gas lines, or flue systems. The A07 fault is a safety lockout related to combustion monitoring, and local codes typically require a licensed professional to diagnose and repair sensor or control board issues. If you are not comfortable working with electrical multimeters, wiring harnesses, or the boiler's internal components, have a technician perform the resistance checks and replacement. A technician can also access the contractor menu to review lockout history and confirm the fault, and will have the correct replacement sensor for your specific Weil-McLain model.

**Rough cost:** A pro service call runs about $200-400.

## See Also

- [Weil-McLain A114 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a114-error-code/)
- [Weil-McLain A67 Error - Causes & Fix](/posts/weil-mclain-boiler-a67-error-code/)
- [Weil-McLain A40 Error Code - Causes & Fix](/posts/weil-mclain-boiler-a40-error-code/)
- [Weil-McLain A54 Error - Causes & Fix](/posts/weil-mclain-boiler-a54-error-code/)
