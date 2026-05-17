---
title: "EcoSmart ECO 36 Error Codes - What It Means and How to Fix It"
description: "EcoSmart ECO 36 electric tankless water heaters use the same core fault architecture as the ECO 27, but the higher-capacity unit has different flow, amperage, and heating element considerations. This guide explains each code and the repair steps that make sense on the 36kW platform."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The EcoSmart ECO 36 is the top of the EcoSmart residential electric tankless line, rated at 36 kilowatts. It draws up to 150 amps at 240VAC and is designed for homes in cold climates where groundwater temperatures can drop below 40°F, making a lower-capacity unit insufficient for simultaneous hot water demand. Because it shares the same IQ digital control architecture as the ECO 27, its error codes are identical - but the diagnostic steps differ in a few key areas due to the ECO 36's higher power draw, larger heating elements, and three-phase wiring in some installations.

## What Does EcoSmart ECO 36 Error Codes Mean?

The ECO 36 runs the same IQ self-modulating control system as the ECO 27. It monitors inlet temperature, outlet temperature, and flow rate continuously. When any reading falls outside operating parameters, it shuts down and displays a fault code. The core difference from the ECO 27 is scale:

- **ECO 27**: 27 kW / 4 heating elements / 112.5A draw / 4 AWG wire minimum
- **ECO 36**: 36 kW / 4 heating elements (larger, higher-wattage) / 150A draw / typically requires 2 AWG copper or 1 AWG aluminum; some installations use two separate 200A panels

The ECO 36 also has a higher minimum flow requirement - approximately 0.5 GPM to activate, versus 0.3 GPM for the ECO 27. This matters for E1 diagnosis.

### EcoSmart ECO 36 Error Code Reference

**E1 - No Flow / Minimum Flow Not Met**
Same architecture as ECO 27, but the activation threshold is higher (0.5 GPM vs. 0.3 GPM). Low-flow faucet aerators that work fine with the ECO 27 may cause persistent E1 faults on the ECO 36.

Causes:
- Inlet screen filter clogged with sediment
- Failed flow sensor paddle wheel
- Low-flow aerators or fixtures below 0.5 GPM
- Partially closed water supply valve
- Low household water pressure (below 30 PSI)

**E2 - Outlet Overtemperature**
The outlet thermistor detected temperature above the safe limit. On the ECO 36, this is more likely than on the ECO 27 when flow rate is marginal relative to temperature setpoint, because the higher wattage means more heat is delivered per gallon.

Causes:
- Very low flow rate with high temperature setpoint
- Failed or stuck heating element
- Failed outlet thermistor (false low reading causing board to overheat water)
- Severe scale on heating elements causing uneven heat distribution

**E3 - Inlet Temperature Sensor Fault**
The inlet thermistor is reading out of range. Diagnostics are identical to ECO 27.

Causes:
- Failed inlet NTC thermistor
- Loose or corroded connector on control board
- Extreme cold inlet water triggering threshold (below 35°F)

**E4 - Outlet Temperature Sensor Fault**
The outlet thermistor is reading out of range. Diagnostics are identical to ECO 27.

Causes:
- Failed outlet NTC thermistor
- Physical damage from scale or calcium deposits on sensor

**Err - General Control Module Fault**
Same as ECO 27, but on the ECO 36 this code has an additional common cause: the higher current draw (150A) is more likely to cause connection issues at the terminal block, especially if the installer did not use the correct wire gauge or torqued connections improperly.

Causes:
- Power surge or voltage spike
- Loose power connections at the 150A terminal block
- Failed control module
- Tripped thermal cutoffs on heating elements

**No Display / Dead Unit**
More common on the ECO 36 than on smaller EcoSmart units, because:
- Two separate circuit breakers (or a 200A service) are often required - if one trips, the unit gets partial power and the display may behave erratically
- The higher load means breaker trips are more common during demand peaks

### Key Difference from ECO 27: Higher Element Wattage

The ECO 36 heating elements are 9,000W each (at 240VAC), compared to 6,750W on the ECO 27. This means:

- Expected resistance of a good ECO 36 element: approximately **6.4 ohms** (R = V²/P = 57,600/9,000)
- Compared to ECO 27: approximately 8.5 ohms

When testing ECO 36 elements with a multimeter, expect a lower resistance reading. Anything below 4 ohms suggests a partial short; OL (open circuit) confirms failure.

ECO 36 replacement elements are a different part number: **ECO36-ELEMENT** - do not substitute ECO 27 elements, which are a different wattage and will cause overtemperature faults.

## How to Fix It

**Step 1: Cut power at BOTH breakers before opening the unit.**
The ECO 36 requires 150A service and may be on two separate 60A or 80A double-pole breakers. Verify both are off. Use a non-contact voltage tester at every terminal inside the unit before touching anything.

**Step 2: For E1 (no flow), check flow rate at the fixture first.**
Fill a 1-gallon container with cold water from the tap you're testing. Time it. If it takes more than 2 minutes (under 0.5 GPM), your fixture or aerator is the problem - not the ECO 36. Replace low-flow aerators with 1.5 GPM or higher models on fixtures feeding the unit. If flow is adequate, clean the inlet screen and inspect the flow sensor as described in the ECO 27 guide above.

**Step 3: For E2 (overtemperature), calculate whether the ECO 36 is being asked to do too much.**
At 40°F inlet temperature with a 120°F setpoint, the ECO 36 needs to raise water temperature 80°F. At 2.0 GPM, that requires 26.6 kW. The ECO 36 can supply this. At 1.0 GPM, the unit modulates down and E2 should not occur. If E2 appears at normal flow rates, suspect the outlet thermistor.

**Step 4: For ECO 36-specific Err codes, check the terminal block carefully.**
The ECO 36's 150A terminal block must have wires torqued to 45-50 in-lb minimum. Over years of thermal cycling (the unit heats up and cools down with each use), connections loosen. Use a torque screwdriver to check all connections - loose connections at this amperage cause arcing, which generates an Err code and will eventually burn the terminal block.

**Step 5: Descaling protocol - more critical on the ECO 36.**
Because each ECO 36 element delivers 9,000W, scale buildup creates more severe hot spots than on the lower-wattage ECO 27 elements. EcoSmart recommends annual descaling for any water supply above 7 GPG hardness. Use a tankless water heater flushing kit: connect a submersible pump to the cold inlet isolation valve and route the outlet back to the pump reservoir (a 5-gallon bucket works). Circulate 4 gallons of undiluted white vinegar for 60 minutes.

**Step 6: For dead display after an Err code, check thermal cutoffs.**
Each element has a one-shot thermal cutoff (TCO). If any TCO has tripped, that element is disabled. The ECO 36 will typically still operate with one disabled element but at reduced capacity (27 kW instead of 36 kW). Test each TCO for continuity. Replace any open TCO and also replace the element it was on - a TCO doesn't trip without a reason. Part number for ECO 36 TCO: compatible with generic 250V/15A 140°C auto-reset or manual-reset TCOs.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [EcoSmart ECO 36 Heating Element (Part # ECO36-ELEMENT, 9,000W)](https://www.amazon.com/s?i=industrial&k=EcoSmart+ECO+36+heating+element+9000w+replacement&tag=errorcodefixes-20) | Replaces failed 9,000W heating element - do NOT substitute ECO 27 elements | $40-$70 per element |
| [EcoSmart Flow Sensor](https://www.amazon.com/s?i=industrial&k=EcoSmart+ECO+36+flow+sensor&tag=errorcodefixes-20) | Replaces failed flow sensor causing persistent E1 fault | $20-$40 |
| [Thermal Cutoff (TCO) 140°C](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+thermal+cutoff+140c&tag=errorcodefixes-20) | Replaces tripped thermal safety on heating element | $8-$18 |
| [NTC Thermistor Sensor (10kΩ)](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+NTC+thermistor+10k&tag=errorcodefixes-20) | Replaces E3 or E4 inlet/outlet temperature sensor | $12-$25 |
| [EcoSmart Control Module](https://www.amazon.com/s?i=industrial&k=EcoSmart+ECO+36+control+module+board&tag=errorcodefixes-20) | Replaces failed control board on ECO 36 | $65-$130 |
| [Tankless Descaling Flush Kit](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+flush+kit+descale&tag=errorcodefixes-20) | Annual maintenance kit for hard water - prevents element failure and E2 codes | $28-$55 |

## When to Call a Pro

The ECO 36's 150A service requirement puts it in a different league from standard appliance repairs. Call a licensed electrician for:

- **Panel upgrades**: Many homes need a panel upgrade or subpanel to accommodate the 150A ECO 36 service.
- **Wire gauge issues**: Undersized wiring to the unit (anything smaller than 2 AWG copper for a 150A circuit) is a fire risk and must be corrected before the ECO 36 will work reliably.
- **Persistent arcing at terminal block**: Arcing at 150A requires panel-level diagnosis.

For water supply work or if the unit needs to be removed for access, call a licensed plumber.

## Frequently Asked Questions

**Q: What's the main functional difference between the ECO 27 and ECO 36 for error code diagnosis?**
A: The error codes are the same, but E1 and E2 require slightly different thresholds to trigger. The ECO 36's higher minimum flow (0.5 GPM vs. 0.3 GPM) means more fixtures and aerators can trigger E1. The higher wattage means E2 can occur at slightly higher flow rates than on the ECO 27 if the outlet thermistor is marginal. When in doubt on E2, test the outlet thermistor before changing the temperature setpoint.

**Q: My ECO 36 suddenly started delivering warm water instead of hot. No error code is displayed. What's wrong?**
A: This is the classic symptom of one or more failed heating elements or tripped TCOs. The unit still runs (and thus shows no error code) but at reduced capacity. With one 9,000W element down, you have 27 kW - equivalent to an ECO 27. With two elements down, you have 18 kW, which will struggle in cold climates. Test all four elements and TCOs individually.

**Q: The ECO 36 trips a breaker when multiple showers run simultaneously. Is this a unit fault?**
A: Not necessarily - it may be a correctly functioning breaker protecting an undersized circuit. The ECO 36 draws up to 150A. Verify the breakers feeding the unit are rated for continuous 150A service and that the wire gauge matches. Do not replace breakers with higher-amperage units to stop the tripping - investigate the wire gauge first.

**Q: How often should I descale the ECO 36 compared to the ECO 27?**
A: Same interval if your water hardness is the same, but the consequences of skipping descaling are worse on the ECO 36. Higher element wattage means scale-induced hot spots are more extreme, TCOs trip more readily, and elements fail faster. In areas above 10 GPG water hardness, descale every 6 months rather than annually.
