---
title: "Rheem RTGH-95DVLN Condensing Tankless Water Heater Error Codes"
description: "Complete error code reference for the Rheem RTGH-95DVLN condensing tankless water heater, covering all fault codes, secondary heat exchanger issues, condensate drain problems, and ignition failures. Written for homeowners and plumbing technicians."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Rheem RTGH-95DVLN is Rheem's flagship condensing tankless water heater, a natural gas indoor direct vent unit rated at 9.5 GPM maximum flow and up to 199,000 BTU/hr input. It's a condensing unit, which means it has both a primary and secondary heat exchanger, a condensate drain system, and a flue gas temperature well below 120°F at the exhaust termination. When a fault occurs, the unit displays a two-digit error code on its front panel and stops firing. This guide covers every code the RTGH-95DVLN generates and how to resolve each one.

## What Does a Rheem RTGH-95DVLN Error Code Mean?

Error codes on the RTGH-95DVLN appear as two-digit numbers on the LED display on the unit's front panel. When an error code is active, the unit shuts down and displays the code until either the fault clears automatically, the user resets it, or the underlying problem is repaired.

The unit uses the same fault code system as most Rheem/Paloma condensing tankless units, so if you've worked on any Rheem RTGH or RTG series unit, the codes will look familiar.

### Complete Error Code Reference

| Code | Fault Description | Reset Type |
|------|-----------------|------------|
| 00 | Normal operation, no fault |, |
| 03 | Domestic hot water demand too low to ignite (below minimum flow rate) | Auto (increases flow) |
| 05 | Abnormal water pressure (above maximum inlet pressure) | Auto |
| 10 | Exhaust vent blockage detected or insufficient combustion air | Manual |
| 11 | Ignition failure, could not confirm flame during startup attempt | Manual |
| 12 | Flame extinguishment during operation | Manual |
| 14 | Thermal fuse or overheat cutoff device open | Manual (after repair) |
| 16 | Outgoing water temperature exceeded maximum limit | Auto |
| 24 | Secondary heat exchanger outlet temperature sensor failure | Auto |
| 29 | Condensate drain sensor error or condensate system backup | Manual |
| 31 | Inlet cold water temperature sensor failure | Auto |
| 32 | Outlet hot water temperature sensor failure | Auto |
| 33 | Secondary heat exchanger temperature sensor failure | Auto |
| 34 | Ambient temperature sensor failure | Auto |
| 38 | Freeze protection circuit fault | Auto |
| 52 | Modulating gas valve drive circuit failure | Manual |
| 61 | Combustion fan motor failure or incorrect RPM | Manual |
| 65 | Water flow control valve failure | Auto |
| 66 | Bypass valve failure (on units with built-in mixing valve) | Manual |
| 71 | Gas valve circuit failure, valve drive abnormal | Manual |
| 72 | Flame sensing circuit failure, control board issue | Manual |
| 76 | Remote controller communication error | Auto |
| 79 | Inlet water temperature too high (recirculation system issue) | Auto |
| 89 | Gas type mismatch, unit configured for different gas type than supplied | Manual |

### Secondary Heat Exchanger and Condensate Codes (24, 29, 33)

The RTGH-95DVLN's condensing operation is what separates it from standard tankless units. Hot flue gases pass through a stainless steel primary heat exchanger, then through a secondary heat exchanger where additional heat is extracted, dropping flue gas temperatures low enough that water vapor in the exhaust condenses. This condensate (acidic water at pH 3–5) drains out the bottom of the unit through a trap.

**Code 24 (secondary HX outlet sensor failure):** The temperature sensor monitoring the secondary heat exchanger outlet has gone open-circuit or shorted. This sensor is critical, the secondary heat exchanger can develop lime scale buildup in hard water areas, and the sensor detects if heat transfer is degraded. The sensor is an NTC thermistor; Rheem part **RTG20009B** covers this sensor on RTGH-series units.

**Code 29 (condensate drain fault):** This is one of the most common codes on the RTGH-95DVLN in cold climates or installations that weren't drained properly. The condensate drain system includes a trap (must always have water in it, the trap seal prevents flue gas from entering the room) and, on some installations, a condensate pump. Code 29 appears when:
- The condensate drain is frozen (common in units installed near exterior walls in cold climates)
- The condensate drain is blocked with algae, mineral deposits, or debris
- The condensate level sensor detects the trap is full and not draining
- The condensate pump (if installed) has failed

Never bypass the condensate drain sensor, the RTGH-95DVLN produces roughly 1–3 quarts of condensate per hour at full fire rate. A blocked drain will eventually overflow into the unit and cause internal corrosion.

**Code 33 (secondary HX temperature sensor failure):** Similar to code 24 but on a different sensor location. Both sensors must be functioning for the unit to operate safely, the secondary heat exchanger can reach damaging temperatures without proper sensor feedback.

## How to Fix It

### For Code 11 (Ignition Failure)

1. Verify gas is flowing: light a gas burner at the range or confirm another gas appliance is working.
2. Check gas supply pressure. Natural gas should be 5–10.5 in WC at the unit inlet. Measure at the test port on the gas valve with a manometer during a call for hot water (dynamic pressure).
3. Check water flow: the RTGH-95DVLN requires a minimum of 0.75 GPM to initiate a firing sequence. Run the hot water tap fully open. If flow is low, check the inlet cold water filter screen at the unit's water inlet, scale and debris clog these quickly.
4. Check incoming cold water temperature sensor (code 31), if it's reading incorrectly, the flow sensor may not be getting the correct activation signal.
5. Inspect the air intake termination and exhaust termination for blockage. The RTGH-95DVLN uses a 3-inch PVC or CPVC concentric vent system; ice, bird nests, or improper termination slope can block the intake.
6. Access the burner compartment (requires removing the front panel) and inspect the igniter for carbon deposits. Clean the igniter electrode and the flame rod with fine-grit sandpaper if visibly fouled.

### For Code 12 (Flame Extinguishment)

1. Check dynamic gas supply pressure while the unit is firing. Gas pressure that looks fine at rest may drop below 4 in WC during peak demand on undersized supply lines.
2. Inspect the venting system for any section that might allow recirculation, exhaust gases re-entering the intake causes oxygen depletion and flameout. Minimum 12-inch separation between intake and exhaust terminations is required.
3. Check the combustion fan operation: a fan running at reduced speed will cause a lean mixture that extinguishes easily.
4. Inspect the flame rod: carbon buildup or a cracked ceramic insulator causes intermittent flame signal loss.

### For Code 29 (Condensate Drain Fault)

1. Locate the condensate drain outlet, a small pipe at the bottom of the unit that leads to a trap and then to a drain.
2. Visually inspect the trap for blockage. The RTGH-95DVLN's built-in trap should contain water (it's a water seal). Empty or clogged means drainage failure.
3. If the drain line exits through an exterior wall, check for freezing at the termination. Condensate drain lines in cold climates must be insulated or routed to interior drains only.
4. Flush the condensate drain and trap with hot water to clear mineral deposits. Some installations also benefit from a quarterly biological drain cleaner tablet to prevent algae.
5. Check the condensate overflow sensor: locate the sensor in the condensate collection area (typically a float switch or resistance probe). If the drain is clear but code 29 persists, the sensor may have failed.
6. If a condensate pump is installed, verify it's plugged in and operating. Test by manually tripping the float switch, the pump should activate immediately.

### For Code 16 (Outlet Temperature Exceeded Maximum)

1. Check the temperature setpoint on the unit. If someone set the unit to 140°F and demand is low, the unit can hit its 167°F high-limit.
2. Check whether the recirculation system is short-cycling hot water back to the inlet (code 79 is the specific recirculation fault; code 16 can result from the same root cause).
3. Inspect the outlet temperature sensor (code 32), a shorted sensor can cause the controller to think water is cooler than it is and continue heating.
4. For persistent code 16, descale the secondary heat exchanger: connect a pump with descaling solution (white vinegar or commercial descaler) to the cold inlet service valve and circulate for 45 minutes. Scale on the heat exchanger restricts water flow, allowing outlet temperatures to spike.

### For Code 61 (Combustion Fan Fault)

1. On startup, the RTGH-95DVLN combustion fan runs a pre-purge cycle. Listen for the fan spin-up, a failed fan motor won't spin at all.
2. If the fan runs but code 61 persists, the fan speed sensor (hall sensor on the fan assembly) may be faulty. Access the fan by removing the front panel and combustion cover; inspect the sensor connector for corrosion.
3. Check the combustion air inlet for restriction, the unit requires adequate makeup air. In tightly sealed utility rooms, insufficient combustion air causes the fan to work harder without reaching required RPM.
4. Rheem combustion fan replacement: part **AP15516-1** covers the combustion air blower assembly for RTGH-series units.

### For Code 52 and 71 (Gas Valve Faults)

1. Code 52 means the modulating valve drive circuit failed to respond. Code 71 means the main gas valve solenoid circuit is abnormal.
2. Check the gas valve wiring harness for loose connectors. The gas valve on the RTGH-95DVLN has both a solenoid connector and a modulating control connector.
3. Measure 24VAC at the gas valve solenoid terminals during a call for hot water. Presence of voltage with no valve opening confirms valve failure.
4. Gas valve replacement on a condensing tankless unit requires a licensed plumber, gas valve work falls under gas code in most jurisdictions.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Rheem Tankless Water Heater Temperature Sensor RTG20009B](https://www.amazon.com/s?ascsubtag=ecf-rheem-rtgh-95dvln-error-codes&k=Rheem+Tankless+Water+Heater+Temperature+Sensor+RTG20009B&tag=errorcodefixes-20) | Secondary HX and outlet sensors; codes 24, 32, 33 | $20–$45 |
| [Condensate Neutralizer Refill Kit](https://www.amazon.com/s?ascsubtag=ecf-rheem-rtgh-95dvln-error-codes&k=condensate+neutralizer+refill+media+tankless&tag=errorcodefixes-20) | Required if condensate drain is acidic; neutralizes pH before drain | $15–$35 |
| [Tankless Water Heater Descaler Flush Kit](https://www.amazon.com/s?ascsubtag=ecf-rheem-rtgh-95dvln-error-codes&k=tankless+water+heater+descaler+flush+pump+kit&tag=errorcodefixes-20) | Removes scale from secondary heat exchanger; prevents codes 16, 29, 33 | $30–$60 |
| [Rheem Combustion Fan AP15516-1](https://www.amazon.com/s?ascsubtag=ecf-rheem-rtgh-95dvln-error-codes&k=Rheem+RTGH+combustion+fan+blower+AP15516&tag=errorcodefixes-20) | Replace on code 61; inspect before condemning, check wiring first | $80–$175 |
| [Condensate Pump for Tankless Water Heater](https://www.amazon.com/s?ascsubtag=ecf-rheem-rtgh-95dvln-error-codes&k=condensate+pump+tankless+water+heater&tag=errorcodefixes-20) | Required when gravity drain to floor drain isn't possible; code 29 prevention | $35–$80 |
| [Rheem Igniter Electrode Kit](https://www.amazon.com/s?ascsubtag=ecf-rheem-rtgh-95dvln-error-codes&k=Rheem+RTGH+igniter+electrode+kit+tankless&tag=errorcodefixes-20) | Replace on code 11 if electrode is fouled or gap is incorrect | $20–$50 |

## When to Call a Pro

Several RTGH-95DVLN faults require a licensed plumber or HVAC/gas technician:

- **Code 52 or 71 (gas valve faults).** Gas valve work requires a licensed contractor in most states. An incorrect gas valve replacement can create a dangerous situation.
- **Code 11 or 12 with low gas pressure confirmed.** Undersized gas supply piping, regulator issues, or gas meter capacity problems require a licensed gas fitter.
- **Code 14 (thermal fuse).** The fuse must be replaced, but more importantly, the root cause (scale, restricted flow, sensor failure) must be diagnosed and repaired first.
- **Any venting issues.** Incorrect PVC vent sizing, slope, or termination on a condensing unit can create CO exposure risk. Have a qualified technician inspect the venting.
- **Persistent code 29 after drain clearing.** If the condensate drain keeps blocking despite regular maintenance, the installation may have a routing issue that requires a plumber to redesign.

Inlet filter cleaning, sensor replacement, condensate drain maintenance, and igniter inspection are manageable DIY repairs with basic mechanical aptitude.

## Frequently Asked Questions

**Q: The RTGH-95DVLN shows code 29 every winter but works fine in summer. What's happening?**
A: Your condensate drain is freezing at the exit point, almost certainly because the drain line runs through or exits near an exterior wall. The condensate exits the unit at close to 50–60°F but can freeze in the drain line if it runs through a cold attic, crawl space, or exterior penetration. The fix is rerouting the condensate to an interior drain or fully insulating the drain line run. A condensate pump that discharges into an interior drain eliminates this problem entirely.

**Q: How do I reset error code 11 on my Rheem RTGH-95DVLN?**
A: Press the temperature UP button on the front panel. On most RTGH revisions, this serves as the reset button. Alternatively, turn the unit off at the power switch, wait 30 seconds, then turn it back on. If the fault reappears immediately, the root cause hasn't been fixed, don't just keep resetting.

**Q: The unit fires and heats water but code 16 keeps flashing as an alert (not a shutdown). Is it safe to use?**
A: Code 16 as a non-shutdown alert (some firmware revisions log it as informational if the outlet temperature briefly exceeded the threshold) is a warning. The unit is getting hotter than intended. Turn down the temperature setpoint to 120°F if it's set higher, check for hot water recirculation sending hot water back to the inlet (which reduces the unit's ability to control outlet temperature), and plan a descaling service soon. Continuing to operate with code 16 appearing regularly will shorten the heat exchanger life.

**Q: My RTGH-95DVLN is brand new and shows code 03 on first start. Is it defective?**
A: Code 03 means the water flow rate is below the minimum threshold required to fire (typically 0.75 GPM). This often happens on new installations where the service technician is testing the unit with a partially opened tap, or where a pressure-reducing valve was set too low. Open a hot water tap fully and confirm flow, the code should clear and the unit should fire. If it still won't fire at full open-tap flow, check that both isolation valves on the cold inlet and hot outlet are fully open.
