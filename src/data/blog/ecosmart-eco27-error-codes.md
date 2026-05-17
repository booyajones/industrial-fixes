---
title: "EcoSmart ECO 27 Error Codes - What It Means and How to Fix It"
description: "EcoSmart ECO 27 electric tankless water heaters use E1, E2, E3, E4, and Err codes to report flow, sensor, heating element, and thermal cutoff faults. This guide shows what each code means and the parts most likely to fix it."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The EcoSmart ECO 27 is a self-modulating electric tankless water heater rated at 27 kilowatts - one of the most powerful residential electric tankless units available. It can handle two simultaneous showers in most U.S. climates. When the ECO 27 throws an error code, the digital display shows a code that tells you exactly what the self-modulating control module detected. This guide covers every error code, what causes it, and how to fix it.

## What Does EcoSmart ECO 27 Error Codes Mean?

The ECO 27 uses EcoSmart's IQ digital control system. The control module continuously monitors water temperature at the inlet and outlet sensors, flow rate through the flow sensor, and heating element health via current monitoring. When any parameter falls outside safe operating bounds, the unit shuts off and displays an error code on the LED display.

The ECO 27 draws up to 112.5 amps at 240VAC (four 6,750-watt heating elements). This is why electrical faults are common - the unit needs a properly wired 240V service with the correct wire gauge (4 AWG copper minimum for most installations) and dedicated breakers.

### EcoSmart ECO 27 Error Code Reference

**E1 - No Flow / Minimum Flow Not Met**
The unit powered on and a hot water tap was opened, but the flow sensor did not detect enough water flow to safely activate the heating elements. The ECO 27 requires a minimum of 0.3 gallons per minute (GPM) to activate.

Causes:
- Partially closed inlet water valve
- Clogged inlet screen filter (common after installation in areas with sediment)
- Failed flow sensor (paddle-wheel or magnetic turbine type)
- Very low household water pressure
- Debris or scale buildup on the flow sensor paddle

**E2 - Outlet Water Temperature Too High / Overtemperature**
The outlet thermistor detected water temperature above the safe limit (the ECO 27's maximum setpoint is 140°F / 60°C, but the safety shutoff triggers significantly above that - typically around 160°F+).

Causes:
- Failed or stuck-open heating element (element energized without control signal)
- Failed outlet temperature sensor sending incorrect (low) reading that causes over-heating
- Unit set to maximum temperature with very low flow rate
- Scaled heating elements with hot spots

**E3 - Cold Water Inlet Sensor Fault / Inlet Temperature Error**
The inlet temperature sensor (thermistor) is reading out of range or has failed. The control module uses this reading to calculate how much power to apply to reach the target temperature.

Causes:
- Failed inlet thermistor
- Loose thermistor connector on control module
- Extreme incoming water temperature (below 35°F / inlet freezing)
- Wiring damage near the inlet sensor

**E4 - Outlet Temperature Sensor Fault**
The outlet thermistor is reading out of range. The control module cannot verify the water is being heated correctly.

Causes:
- Failed outlet thermistor
- Loose connector
- Physical damage to the sensor from scale buildup or calcium deposits

**Err - General System Error / Control Module Fault**
A catch-all code that means the control board detected an internal fault it cannot categorize into a specific code. This often follows an electrical event.

Causes:
- Power surge or voltage spike to the unit
- Failed control module
- Loose or corroded power connections inside the unit
- Partial heating element failure causing current imbalance

**No Display / Unit Dead**
Not technically an error code, but commonly reported. If the LED display is blank when the unit is powered and a tap is opened, the issue is typically:
- Tripped thermal cutoff (TCO) - this is a one-shot manual-reset safety device
- Tripped circuit breakers (check both breakers if on a double-pole breaker panel)
- Failed control module
- No power from the panel

### Understanding the Thermal Cutoff (TCO)

The ECO 27 has a thermal cutoff device on each heating element. If any element overheats - typically from running dry, scale buildup, or a failed element - the TCO trips and cuts power to that element permanently. A tripped TCO shows either as an "Err" code or as the unit running with reduced output (only some elements firing).

The ECO 27's heating elements are EcoSmart part # ECO27 (sold as a replacement element kit). They are 240V, 6,750W, and threaded into the water chamber. The elements are designed to be user-replaceable.

## How to Fix It

**Step 1: Power down at the breaker panel before opening the unit.**
The ECO 27 draws over 100 amps. Always turn off both circuit breakers feeding the unit before removing the cover. Verify power is off with a non-contact voltage tester at the terminals inside the unit.

**Step 2: For E1 (no flow), clean the inlet screen filter.**
The inlet screen is located on the cold water inlet connection (right side of unit, looking at the front). Turn off the cold water supply valve. Using pliers or a filter removal tool, unscrew the inlet connection fitting and pull out the mesh screen. Rinse it under running water until clean. Reinstall, restore water, and test. If the E1 persists, locate the flow sensor - it's mounted in the water pathway inside the unit and has two wires connecting to the control board. Disconnect the wires and measure sensor resistance: paddle-type flow sensors on the ECO 27 typically read 2-10 ohms when the paddle moves freely. Check for debris on the paddle wheel.

**Step 3: For E2 (overtemperature), check flow rate first.**
The most common cause of E2 on the ECO 27 is too-low flow rate at high temperature setpoint. Run a hot tap and time how long it takes to fill a 1-gallon container. If it takes more than 3 minutes, your flow is below the minimum for the temperature setting. Lower the setpoint or increase the tap flow. If flow is adequate and E2 persists, the outlet thermistor may need replacement - it clips onto the outlet pipe inside the unit.

**Step 4: For E3 or E4 (sensor faults), test the thermistors.**
The inlet and outlet thermistors on the ECO 27 are NTC (negative temperature coefficient) sensors. At room temperature (70°F / 21°C), they should read approximately 12,000-14,000 ohms. An open circuit (OL) or a very low reading (under 500 ohms) confirms a failed sensor. The sensors clip onto their respective water pipes inside the unit and are connected by 2-pin connectors to the control board. Replacement sensors are available (EcoSmart part # ECO-SENSOR) and simply clip on.

**Step 5: For Err or blank display, check the thermal cutoffs.**
Each heating element has a thermal cutoff mounted on it. The TCO is a small disc-shaped device with two terminals (Part # ECO-TCO or generic 2-wire 140°C TCO). Test continuity across the TCO with a multimeter - a good TCO reads 0 ohms (closed circuit). An open circuit (OL) means the TCO has tripped and the element is disabled. Replace the TCO if it has tripped, but also investigate why it tripped - scale buildup on the element causes hot spots that trigger the TCO.

**Step 6: Descale the heating elements.**
In hard water areas, calcium carbonate builds up on the heating elements and the inner walls of the water chamber. EcoSmart recommends annual descaling with white vinegar flush for hard water conditions. Connect a submersible pump and pump 4 gallons of undiluted white vinegar through the unit in a closed loop for 45-60 minutes, then flush with fresh water. This removes scale that causes E2 codes, TCO trips, and element failure.

**Step 7: For persistent Err codes, inspect power connections.**
Remove the cover and visually inspect all wire connections at the terminal block. Loose or arced connections on a 100+ amp circuit will cause the control board to detect current anomalies. Look for melting, discoloration, or burning at the lugs. Re-torque all connections to spec (typically 20-30 in-lb for the element terminals, 45 in-lb for the main input terminals).

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [EcoSmart ECO 27 Heating Element (Part # ECO27-ELEMENT)](https://www.amazon.com/s?ascsubtag=ecf-ecosmart-eco27-error-codes&k=EcoSmart+ECO+27+heating+element+replacement&tag=errorcodefixes-20) | Replaces burned-out or scaled 6,750W heating element | $30-$55 per element |
| [EcoSmart Flow Sensor (Part # ECO-FLOW-SENSOR)](https://www.amazon.com/s?ascsubtag=ecf-ecosmart-eco27-error-codes&k=EcoSmart+tankless+flow+sensor+replacement&tag=errorcodefixes-20) | Replaces failed flow sensor causing E1 error | $20-$40 |
| [EcoSmart Thermal Cutoff (TCO)](https://www.amazon.com/s?ascsubtag=ecf-ecosmart-eco27-error-codes&k=EcoSmart+ECO+thermal+cutoff+TCO+replacement&tag=errorcodefixes-20) | Replaces tripped thermal cutoff on heating element | $8-$18 |
| [NTC Temperature Sensor (Inlet or Outlet)](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-ecosmart-eco27-error-codes&tag=errorcodefixes-20) | Replaces failed thermistor causing E3 or E4 codes | $12-$25 |
| [EcoSmart Control Module / Board](https://www.amazon.com/s?ascsubtag=ecf-ecosmart-eco27-error-codes&k=EcoSmart+ECO+27+control+module+board&tag=errorcodefixes-20) | Replaces failed control board causing Err or blank display | $60-$120 |
| [Inlet Screen Filter](https://www.amazon.com/s?ascsubtag=ecf-ecosmart-eco27-error-codes&k=tankless+water+heater+inlet+filter+screen&tag=errorcodefixes-20) | Replaces clogged inlet filter causing E1 fault | $5-$12 |
| [Tankless Descaling Kit (Vinegar Flush System)](https://www.amazon.com/s?ascsubtag=ecf-ecosmart-eco27-error-codes&k=tankless+water+heater+descaling+flush+kit&tag=errorcodefixes-20) | Annual maintenance to prevent scale-related faults and element failure | $25-$50 |

## When to Call a Pro

The ECO 27 is a DIY-friendly appliance in terms of part replacement - EcoSmart designed it specifically for homeowner maintenance. However, call a licensed plumber or electrician for:

- **Any electrical work inside the panel**: Adding circuits, upgrading wire gauge, or replacing breakers must be done by a licensed electrician.
- **Water supply work**: If the E1 fault traces to low household water pressure (under 30 PSI), diagnosing and fixing pressure issues is plumbing work.
- **Persistent Err codes after board and TCO replacement**: This may indicate a wiring problem in the home's supply circuit that requires electrical diagnosis.
- **No hot water in a single-family home serving more than 2 bathrooms**: The ECO 27 may be undersized for the load. A plumber can calculate demand and spec the correct unit.

If you're uncomfortable working around 240VAC systems with over 100 amps, have a professional handle the repair.

## Frequently Asked Questions

**Q: My ECO 27 shows E1 only when I run two fixtures at the same time. Is this normal?**
A: Not quite normal, but it suggests marginal flow. The ECO 27 requires 0.3 GPM minimum across the entire unit (not per outlet). If running two fixtures simultaneously pushes flow too high for the unit to maintain setpoint, it shouldn't E1 - it should just deliver warm rather than hot water. If E1 appears, check whether the flow sensor paddle is partially stuck or worn. Also verify your household pressure doesn't drop significantly under simultaneous demand.

**Q: I replaced the heating elements but still get Err codes. What should I check?**
A: After element replacement, verify the TCOs on each new element are good (continuity test). Also confirm all element terminal connections are tight. An Err code after element replacement sometimes traces to a loose element-to-chamber seal causing a small water leak onto the control board. Finally, check that you didn't accidentally reverse the inlet and outlet connections during reassembly.

**Q: The ECO 27 worked fine for 3 years, then started showing E2 in winter. Why?**
A: Cold inlet water temperature is the likely cause. In winter, groundwater can be 35-45°F. The ECO 27 must add more heat to reach your setpoint, which means it's running at full power with every element active. At low flow rates, this can result in actual outlet overtemperature even with correct temperature settings. Lower your setpoint in winter or slightly increase your tap flow rate. Also consider whether scale has accumulated on the elements - three years of hard water leaves significant calcium deposits.

**Q: How do I know which heating element failed?**
A: With power off and the unit open, disconnect each element's terminals individually and test resistance across the element terminals. A working 6,750W / 240V element reads approximately 8.5 ohms (calculated from P=V²/R). An open circuit (OL) means a failed element. A reading of 0 ohms (dead short) means the element shorted and likely tripped a breaker.
