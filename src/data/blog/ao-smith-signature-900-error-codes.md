---
title: "A.O. Smith Signature 900 Tankless Water Heater Error Codes - Full Fault Guide"
description: "Complete fault code guide for the A.O. Smith Signature 900 condensing tankless water heater, covering error codes E01 through E09, gas valve faults, heat exchanger issues, flow sensor failures, and step-by-step diagnosis. Written for homeowners and plumbing technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The A.O. Smith Signature 900 is A.O. Smith's premium condensing tankless water heater line, available in 140,000–199,000 BTU configurations for whole-house applications. It's a condensing unit with both primary and secondary heat exchangers, a stainless steel condensate management system, and A.O. Smith's modulating gas valve that adjusts firing rate in real time based on incoming water temperature and flow rate. Fault codes appear on the digital display as E-series codes followed by a number. This guide covers E01 through E09, the full range of faults on the Signature 900 platform.

## What Does an A.O. Smith Signature 900 Error Code Mean?

When the Signature 900 detects a fault, it shuts down, displays an E-code on the front panel LED display, and holds that code until either the condition clears (for auto-reset faults) or a manual reset is performed. The unit also has colored indicator LEDs: green for normal operation, yellow for minor alerts, and red for faults that have shut the unit down.

All E-codes have a specific origin, a sensor, a safety circuit, or a component that reported an out-of-range value. Understanding which component each code maps to makes diagnosis fast.

### Complete Error Code Reference

| Code | Fault Description | Reset Type |
|------|-----------------|------------|
| E01 | Ignition failure, no flame confirmed during startup | Manual |
| E02 | False flame detected, flame signal present when gas valve is closed | Manual |
| E03 | Gas supply or combustion fault, flame established but unstable | Manual |
| E04 | High temperature limit exceeded, heat exchanger overheated | Manual |
| E05 | Outlet water temperature sensor fault | Auto |
| E06 | Inlet water temperature sensor fault | Auto |
| E07 | Secondary heat exchanger temperature sensor fault | Auto |
| E08 | Heat exchanger outlet temperature sensor fault | Auto |
| E09 | Gas valve failure, valve not responding to modulation commands | Manual |

### Code E01: Ignition Failure

E01 is the most common fault on the Signature 900. It means the unit opened the gas valve and activated the igniter but never received a flame signal from the flame rod within the allowed startup window. The unit will attempt ignition 3 times before locking out on E01.

**Root causes (in order of frequency):**
1. Gas supply interruption or low gas pressure
2. Water flow below minimum threshold (0.75 GPM), unit won't fire without sufficient flow
3. Fouled or misdirected igniter electrode
4. Failed flame rod or cracked porcelain insulator
5. Blocked combustion air intake
6. Defective control board (rare)

On the Signature 900, the minimum water flow for ignition can be viewed in the diagnostic menu. Hold the Up and Down buttons simultaneously for 3 seconds to enter service mode, this displays current sensor values including flow rate.

### Code E02: False Flame

E02 is unusual, it means the control board's flame detection circuit is seeing a flame signal when the gas valve should be closed. This can mean:
- The flame rod is shorted to ground (check insulator)
- There's a leak in the gas valve body allowing uncontrolled flame
- The control board's flame sensing circuit has failed

Do not ignore E02. A confirmed flame rod short is usually harmless (just replace the rod), but a leaking gas valve is a safety issue that requires immediate professional service.

### Code E03: Unstable Combustion

E03 fires when the unit establishes a flame but the flame signal is intermittent or drops out unexpectedly. This is the "almost-working" fault, the unit gets gas and ignites but can't sustain reliable combustion.

**Common causes:**
- Low dynamic gas pressure (fine at rest, drops under firing load)
- Partially fouled burner ports causing uneven flame distribution
- Combustion air restriction
- Wind-related interference at the vent termination (common in installations where the exhaust terminal is in a high-wind location)

### Codes E05–E08: Sensor Faults

The Signature 900 monitors water temperature at four points: the cold water inlet (E06), the hot water outlet (E05), the secondary heat exchanger (E07), and the primary heat exchanger outlet (E08). All four sensors are NTC thermistors. A sensor that has failed open will read –40°F or a similar extreme cold value; a shorted sensor reads 250°F or higher.

The Signature 900's diagnostic mode (hold Up + Down for 3 seconds) displays live sensor temperatures. If a sensor shows –40 or 250 when at room temperature, it has failed.

A.O. Smith Signature 900 temperature sensors are 10k NTC thermistors. Part number **100109748** covers the outlet and inlet sensors; part number **100109749** covers the heat exchanger sensors, verify against your specific model's parts list.

### Code E04: High Temperature Limit

E04 means the primary heat exchanger outlet temperature exceeded the safety cutout (typically 203°F). This is the "something is very wrong with water flow or heat exchange" code. Root causes:

- **Scale buildup on heat exchanger:** In hard water areas, calcium and magnesium carbonate deposits insulate the heat exchanger, restricting flow and causing local overheating. Scale is the #1 cause of E04 on units over 3 years old in hard water regions.
- **Closed or partially closed shutoff valves:** Even a partially closed service valve restricts flow enough to cause overheating at high fire rate.
- **Failed flow sensor:** The Signature 900 adjusts firing rate based on flow, a flow sensor reading too high will cause the unit to fire harder than the actual flow can handle.
- **Undersized unit for demand:** Asking a 140K BTU unit to produce 120°F water from 35°F inlet at 3+ GPM simultaneously will push it toward its thermal limits.

### Code E09: Gas Valve Failure

E09 specifically means the control board sent a modulation command to the gas valve's stepper motor and received no response or an incorrect response. The Signature 900 uses a modulating gas valve, it doesn't just open and close, it continuously adjusts gas flow to modulate BTU output.

E09 can also appear if:
- The gas valve wiring harness has a broken pin or loose connector
- The control board's gas valve driver circuit has failed
- The valve's stepper motor has mechanically failed

Before condemning the gas valve, inspect and reseat the harness connector at both the valve and the board. E09 caused by a loose connector is a frustratingly common service call.

## How to Fix It

### For E01 (Ignition Failure)

1. Check gas supply: confirm other gas appliances work. If gas service is out, wait for restoration.
2. Check minimum flow: open a hot water tap fully and confirm flow exceeds 0.75 GPM. If you have a shower head rated below 1.5 GPM, it may be marginal for ignition.
3. Clean the inlet water filter: remove the cold water inlet line and pull the filter screen. Rinse under running water and reinstall.
4. Check the combustion air intake for blockage: the Signature 900 draws combustion air through its intake pipe (typically 3-inch PVC). Check the termination cap for bird nests or debris.
5. Access the burner compartment (front panel removal) and visually inspect the igniter electrode: look for carbon fouling or a cracked porcelain insulator. The electrode gap should be 3.5–4mm.
6. Test flame rod: remove the flame rod connector at the control board. With the connector disconnected, measure resistance from the flame rod terminal to unit ground. Infinity (open circuit) is correct. Any resistance reading means the rod is shorted, replace it.
7. Press Reset (the button on the front panel, or cycle power) and retry.

### For E03 (Unstable Combustion)

1. Check dynamic gas pressure while unit is firing: connect a manometer to the gas inlet test port. Natural gas should maintain 5–10.5 in WC under firing load. Pressure drop to below 4 in WC during firing indicates a supply problem.
2. Check venting for recirculation: run the unit and hold your hand near the intake termination. You shouldn't feel warm air coming out of the intake (exhaust recirculation). Verify the separation between intake and exhaust terminations meets code (minimum 12 inches on most installations).
3. Inspect burner ports for fouling: fine debris or insect residue can partially block burner ports causing uneven combustion. Burner cleaning requires removing the burner assembly, a job for a qualified tech.

### For E04 (High Temperature Limit)

1. Check all water supply valves to the unit are fully open.
2. Check inlet water pressure: should be 15–150 PSI. Low pressure means low flow means overheating.
3. Descale the heat exchanger: this is the most impactful maintenance action for E04. Connect a descaling pump kit to the service ports (cold inlet service valve and hot outlet service valve). Circulate white vinegar or commercial descaler (Calci-Free or equivalent) for 45–60 minutes, flush with clean water.
4. After descaling, check if flow rate through the unit has improved, you should notice a measurable increase.

### For E05–E08 (Sensor Faults)

1. Enter diagnostic mode (hold Up + Down for 3 seconds) and read the live temperature values.
2. Identify the out-of-range sensor (showing –40°F or 250°F at room temperature).
3. Locate and disconnect the sensor.
4. Measure resistance: approximately 10,000 ohms at 77°F is correct. Replace if open or shorted.
5. Restore power and confirm the fault clears.

### For E09 (Gas Valve Failure)

1. Turn off the unit and disconnect power.
2. Locate the gas valve harness connector at the bottom of the gas valve. Disconnect and reconnect firmly.
3. Inspect each pin in the connector for corrosion or pushed-back position.
4. Restore power and test.
5. If E09 persists after reseating the connector, the gas valve stepper motor or the control board driver circuit has failed. Contact a licensed plumber for gas valve replacement.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [A.O. Smith Tankless Temperature Sensor 100109748](https://www.amazon.com/s?ascsubtag=ecf-ao-smith-signature-900-error-codes&k=A.O.+Smith+Tankless+Temperature+Sensor+100109748&tag=errorcodefixes-20) | Inlet and outlet sensors; codes E05, E06, 10k NTC thermistor | $20–$45 |
| [A.O. Smith Heat Exchanger Sensor 100109749](https://www.amazon.com/s?ascsubtag=ecf-ao-smith-signature-900-error-codes&k=AO+Smith+100109749+heat+exchanger+sensor&tag=errorcodefixes-20) | Secondary and primary HX sensors; codes E07, E08 | $20–$45 |
| [Tankless Descaler Flush Pump Kit](https://www.amazon.com/s?ascsubtag=ecf-ao-smith-signature-900-error-codes&k=tankless+water+heater+descaler+flush+pump+kit+vinegar&tag=errorcodefixes-20) | Critical for E04 faults in hard water areas; flush annually | $30–$65 |
| [Igniter Electrode for AO Smith Tankless](https://www.amazon.com/s?ascsubtag=ecf-ao-smith-signature-900-error-codes&k=AO+Smith+tankless+water+heater+igniter+electrode&tag=errorcodefixes-20) | Replace on persistent E01; check gap and ceramic insulator | $20–$50 |
| [Flame Rod Sensor for Tankless Water Heater](https://www.amazon.com/s?ascsubtag=ecf-ao-smith-signature-900-error-codes&k=tankless+water+heater+flame+rod+sensor&tag=errorcodefixes-20) | Required for E01 or E02; shorted rod causes both fault types | $15–$35 |
| [Water Heater Inlet Filter Screen](https://www.amazon.com/s?ascsubtag=ecf-ao-smith-signature-900-error-codes&k=tankless+water+heater+inlet+filter+screen&tag=errorcodefixes-20) | Clogged inlet filter causes E01 from low flow; clean or replace annually | $10–$20 |

## When to Call a Pro

Certain Signature 900 faults must be handled by a licensed professional:

- **Code E09 with confirmed gas valve failure.** Gas valve replacement on a condensing tankless unit is a licensed plumber's job in most jurisdictions. An incorrect replacement or improper installation creates safety risk.
- **Code E02 with any possibility of gas valve leakage.** Do not operate the unit if you suspect a leaking gas valve. Shut off the gas supply and call for service immediately.
- **Code E01 with confirmed low gas supply pressure.** If your gas line can't supply adequate pressure under firing conditions, you need a licensed gas fitter to assess the supply pipe sizing or regulator.
- **Code E04 that recurs quickly after descaling.** If the heat exchanger is scaling faster than annual maintenance cycles can handle, a plumber can install a scale inhibitor or water softener to address the root cause.
- **Any combustion gas analysis.** CO levels in flue gas require a calibrated combustion analyzer, not DIY equipment.

Sensor replacement, inlet filter cleaning, descaling, and igniter service are appropriate for a mechanically confident homeowner or general plumbing technician.

## Frequently Asked Questions

**Q: My A.O. Smith Signature 900 shows E01 only during simultaneous hot water demand, like shower plus dishwasher. Why?**
A: Two most likely causes: (1) simultaneous demand is dropping gas supply pressure below the ignition minimum, measure dynamic pressure at the unit while firing, and (2) simultaneous demand exceeds the unit's rated capacity, causing the unit to reduce flow sensing which dips below the minimum ignition threshold. A gas contractor can assess supply pressure; if the unit is legitimately undersized, a second unit or a buffer tank may be the answer.

**Q: How do I descale my A.O. Smith Signature 900 at home?**
A: You need two things: a small submersible pump and several gallons of white vinegar (or commercial descaler). Connect the pump discharge to the unit's cold inlet service valve with a hose, and connect the hot outlet service valve to a bucket or hose that drains back to the same bucket. Fill the bucket with vinegar, plug in the pump, and let it circulate for 45–60 minutes. Flush with clean water for 10 minutes, then disconnect. The service valves are pre-installed on the Signature 900 for exactly this purpose, no tools required except hose connections.

**Q: Code E07 appeared after a power outage. The unit runs but the E07 light stays on. Should I be concerned?**
A: Code E07 (secondary heat exchanger sensor fault) that appeared after a power outage sometimes indicates a loose sensor connector that was disturbed. Turn off the unit and check the sensor wiring at the secondary heat exchanger, it's typically a push-in connector near the bottom of the unit. Reseat it, restore power, and see if the fault clears. If the code returns, measure resistance at the sensor per the diagnostic steps above.

**Q: What's the annual maintenance schedule for the Signature 900?**
A: A.O. Smith recommends: (1) Annual descale in hard water areas (above 6 grains per gallon hardness), every 2 years otherwise. (2) Annual inlet filter screen inspection and cleaning. (3) Annual condensate drain and trap inspection, check that the trap has water in it and the drain line is clear. (4) Annual visual inspection of venting terminations for obstruction. (5) Every 3 years, check the anode rod if the unit has one (some Signature 900 configurations include an indirect storage tank, those have an anode rod).
