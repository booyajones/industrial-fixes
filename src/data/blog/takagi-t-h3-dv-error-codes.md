---
title: "Takagi T-H3-DV Tankless Water Heater Error Codes - Indoor Direct Vent Fault Guide"
description: "Complete fault code guide for the Takagi T-H3-DV indoor condensing tankless water heater, covering error codes 11, 12, 14, 16, 31, 32, 33, 52, 61, 65, 72, 76, 91, 93, and 99. Includes diagnosis steps, replacement parts, and when to call a plumber."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Takagi T-H3-DV is Takagi's high-capacity indoor direct vent condensing tankless water heater, rated at 199,000 BTU/hr with an energy factor of 0.93 or higher. It's common in commercial light applications and whole-house installations in cold climates. When something goes wrong, the T-H3-DV displays a two-digit error code on its front panel LED display. This guide covers all the fault codes you're likely to see, what each one means mechanically, and how to diagnose and fix it.

## What Does a Takagi T-H3-DV Error Code Mean?

Error codes on the T-H3-DV appear on the front panel digital display when the unit fails to ignite, loses flame, detects an abnormal sensor reading, or receives an alert from one of its safety circuits. The unit also has indicator LEDs for power, operation, and error status.

When a fault occurs, the unit stops firing, displays the error code, and waits. Some codes require a manual reset (press the Reset button on the front panel); others automatically retry after the fault condition clears.

### Complete Error Code Reference

| Code | Fault Description | Reset Type |
|------|-----------------|------------|
| 11 | No ignition, unit tried to light but couldn't detect flame | Manual |
| 12 | Flame failure, flame was established but extinguished mid-cycle | Manual |
| 14 | Thermal fuse blown, overheat protection activated | Manual (after repair) |
| 16 | Overheating, heat exchanger exceeded maximum temperature | Automatic |
| 31 | Inlet water temperature sensor fault (open or shorted) | Automatic |
| 32 | Outgoing water temperature sensor fault | Automatic |
| 33 | Heat exchanger outlet temperature sensor fault | Automatic |
| 52 | Modulating gas valve failure, valve stuck or unable to modulate | Manual |
| 61 | Combustion fan fault, fan not reaching required speed | Manual |
| 65 | Water flow control valve fault | Automatic |
| 72 | Flame detection circuit fault (miswire or control board issue) | Manual |
| 76 | Communication error between remote controller and unit | Automatic |
| 91 | Exhaust temperature exceeded limit | Manual |
| 93 | Neutralizer maintenance required, condensate neutralizer cartridge needs service | Automatic (reminder) |
| 99 | Fan motor fault or blocked flue | Manual |

### Code 11 and 12: Ignition and Flame Failures

Error 11 means the unit opened the gas valve and activated the igniter but never confirmed flame via the flame rod. Error 12 means the unit established flame but it went out before the call for hot water ended. These are the two most common Takagi service calls.

**Most frequent causes for codes 11 and 12:**
- Low gas supply pressure (below 5 in WC for natural gas, below 11 in WC for propane)
- Air in the gas line after new installation or service work
- Fouled or misdirected igniter
- Failed flame rod or ceramic insulator cracked
- Scale buildup on the heat exchanger restricting flow (insufficient water flow prevents ignition permissive)
- Blocked venting causing negative draft that blows out flame

On the T-H3-DV, minimum incoming water flow for ignition is typically 0.75 GPM. If flow is below this threshold, the unit will not fire at all, this can manifest as code 11 even when gas supply is fine.

### Code 16 and 91: Overheating Faults

Code 16 indicates the heat exchanger outlet temperature exceeded the unit's safety limit, typically 203°F. This triggers an automatic safety shutdown. Common causes: scale buildup inside the heat exchanger tubes restricting flow and concentrating heat, a partial blockage in the hot water distribution lines, or the unit being significantly undersized for the hot water demand.

Code 91 is specifically the exhaust temperature exceeding its limit, a separate thermocouple monitors the flue gas temperature. High exhaust temperature with normal heat exchanger temperature often points to incomplete combustion (incorrect gas-to-air ratio, fouled burner) or a restriction in the venting system.

### Code 93: Condensate Neutralizer

The T-H3-DV is a condensing unit, it extracts so much heat from combustion gases that the flue gases condense into acidic water (pH 3–5) before exiting. This condensate must pass through a neutralizer cartridge (filled with limestone chips) before draining to prevent drain pipe damage. Code 93 is not a system fault, it's a maintenance reminder that the neutralizer needs to be inspected and the limestone media replaced. The T-H3-DV typically generates this code based on runtime hours. Ignoring it eventually leads to exhausted neutralizer media and acidic condensate damaging copper drain lines.

## How to Fix It

### For Code 11 (No Ignition)

1. Check gas supply: turn on a gas burner elsewhere in the house and confirm gas is flowing. If no gas anywhere, contact your utility.
2. Check gas pressure: ideally measure with a manometer at the unit's gas inlet test port. Natural gas should read 5–10.5 in WC, propane 11–14 in WC. Low pressure under load means undersized gas line or pressure regulator issue.
3. Check water flow: run the hot water tap fully open and confirm you're getting at least 0.75 GPM. If flow is low, check for partially closed shutoff valves, a clogged inlet filter screen on the unit, or low whole-house water pressure.
4. Clean the inlet filter: the T-H3-DV has a stainless mesh filter at the cold water inlet fitting. Remove the inlet connection and pull the filter screen, a clogged screen restricts flow below the ignition minimum.
5. Check venting: inspect the intake and exhaust terminations for blockage (bird nests, ice, debris). The T-H3-DV uses a concentric vent, the outer ring is intake air, the inner pipe is exhaust.
6. If gas and water pressure are confirmed good and ignition still fails: remove the burner access panel and inspect the igniter electrode gap (should be 3.5–4mm on the T-H3-DV). Clean carbon deposits from the flame rod with fine sandpaper.
7. Press Reset on the front panel and retry.

### For Code 12 (Flame Failure)

1. Check for drafts at the installation location, a T-H3-DV near an opening or in a space with significant negative pressure can experience draft-induced flameouts.
2. Check gas supply pressure while the unit is firing (dynamic pressure). A pressure that's fine at rest but drops under load indicates a capacity-limited gas supply.
3. Inspect the flame rod: a cracked porcelain insulator on the flame rod causes erratic flame detection. Visual inspection with the burner cover removed, cracks in the white ceramic insulator are typically visible.
4. Clean scale from the heat exchanger: if the unit runs for 10–20 seconds then shuts on code 12, scale-induced reduced water flow may be causing the flow sensor to drop below the minimum operating threshold mid-cycle. Flush the heat exchanger with a descaling solution.

### For Code 14 (Thermal Fuse Blown)

1. Code 14 means the unit hit a severe overtemp condition that blew the thermal fuse, a one-time safety device. The fuse cannot be reset; it must be replaced.
2. Before replacing the fuse, find out why it blew. Common causes: scale-clogged heat exchanger with severely restricted water flow, a failed temperature sensor that allowed the unit to fire beyond its normal limits, or a blocked flue that caused heat to back up into the unit.
3. Takagi thermal fuse part number varies by production year; the fuse is typically a 167°F or 195°F (75°C or 90°C) axial-lead fuse located on or near the heat exchanger housing.
4. Flush and descale the heat exchanger before putting the unit back in service.

### For Code 61 (Combustion Fan Fault)

1. The T-H3-DV has a combustion fan that pre-purges the combustion chamber before ignition and maintains airflow during firing. Code 61 means the fan speed sensor (hall effect sensor) isn't confirming the fan reached the required RPM.
2. Remove the front panel and listen for the fan during a call for hot water, you should hear it spin up before the igniter fires. No sound means the fan motor has failed.
3. If the fan spins but code 61 persists, the hall effect sensor on the fan or the sensor wiring may have failed.
4. Check the combustion air intake for blockage, a partially blocked intake forces the fan to work harder, and if it can't reach speed, the unit won't fire.
5. Fan motor replacement is a field-serviceable part. Takagi part **100004490** covers the combustion fan assembly on several T-series units.

### For Code 91 (Exhaust Temperature High) / Code 99 (Fan or Flue Fault)

1. Inspect the exhaust vent termination for blockage. Condensing units can accumulate ice at the exhaust termination in very cold climates.
2. Inspect the entire vent run for partial blockage, sagging sections that collect water, or incorrect slope. The exhaust vent should slope back toward the unit at 1/4 inch per foot to allow condensate to drain.
3. Check the combustion fan operation, a failing fan that runs at low speed will cause incomplete combustion and high exhaust temperatures.
4. If flue gas CO levels are high (requires a combustion analyzer), the burner or gas valve may need service.

### For Code 93 (Neutralizer Maintenance)

1. Locate the condensate drain outlet at the bottom of the unit.
2. Remove the neutralizer cartridge housing (typically secured with two screws or a quick-connect fitting below the unit).
3. Empty the exhausted limestone media and refill with fresh neutralizer media. Takagi sells replacement cartridges; generic condensate neutralizer refill limestone chips also work.
4. Reset the maintenance reminder: hold the temperature Up and Down buttons simultaneously for 5 seconds while the unit is in standby (specific reset procedure may vary by unit revision, consult the installation manual Section 6).

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Takagi Igniter Electrode for T-Series](https://www.amazon.com/s?ascsubtag=ecf-takagi-t-h3-dv-error-codes&k=Takagi+tankless+water+heater+igniter+electrode&tag=errorcodefixes-20) | Replace if cracked or misfiring; code 11 won't clear with bad igniter | $20–$50 |
| [Takagi Flame Rod Sensor](https://www.amazon.com/s?ascsubtag=ecf-takagi-t-h3-dv-error-codes&k=Takagi+flame+rod+sensor+tankless&tag=errorcodefixes-20) | Cracked porcelain insulator causes code 12 flameouts mid-cycle | $20–$45 |
| [Condensate Neutralizer Refill Media](https://www.amazon.com/s?ascsubtag=ecf-takagi-t-h3-dv-error-codes&k=condensate+neutralizer+media+limestone+tankless&tag=errorcodefixes-20) | Required for code 93 maintenance reminder; replace every 1–2 years | $15–$35 |
| [Takagi Combustion Fan Motor 100004490](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-takagi-t-h3-dv-error-codes&tag=errorcodefixes-20) | Required for code 61 (fan fault) or code 99 (blocked flue/fan) | $80–$180 |
| [Descaler Flush Kit for Tankless Water Heater](https://www.amazon.com/s?ascsubtag=ecf-takagi-t-h3-dv-error-codes&k=tankless+water+heater+descaler+flush+kit&tag=errorcodefixes-20) | Removes scale from heat exchanger causing codes 11, 16, reduced flow | $30–$60 |
| [Manometer Gas Pressure Test Kit](https://www.amazon.com/s?ascsubtag=ecf-takagi-t-h3-dv-error-codes&k=manometer+gas+pressure+test+HVAC&tag=errorcodefixes-20) | Measure dynamic gas supply pressure to diagnose code 11 gas issues | $25–$65 |

## When to Call a Pro

Some T-H3-DV faults require a licensed plumber or HVAC technician:

- **Code 11 or 12 with confirmed low gas pressure.** Undersized gas lines, incorrect regulator sizing, or gas meter capacity issues require a licensed gas fitter or your utility company.
- **Code 14 (thermal fuse).** Before replacing the fuse, you must confirm why it blew, a tech with a combustion analyzer and water pressure diagnostic tools can find the root cause. Replacing the fuse without fixing the underlying problem will blow the fuse again.
- **Gas valve replacement (code 52).** A modulating gas valve on a high-BTU commercial-grade unit like the T-H3-DV should be installed by a licensed professional.
- **Venting system issues.** Incorrect vent sizing, insufficient makeup air, or negative building pressure issues require an experienced tech to diagnose and correct.
- **Any fault that involves combustion gas analysis.** CO levels in flue gas must be checked with a calibrated analyzer, not DIY equipment.

Inlet filter cleaning, neutralizer cartridge replacement, igniter inspection, and descaling are reasonable DIY tasks.

## Frequently Asked Questions

**Q: My Takagi T-H3-DV shows code 11 only in the morning when the hot water hasn't been used overnight. Works fine after the first use. What's happening?**
A: This is almost certainly air accumulating in the gas line overnight as the system cools. When the unit sits for hours, small amounts of air can migrate back through the gas supply pipe, especially in installations where the unit is slightly above the gas meter elevation. The first ignition attempt fails on code 11 because it's purging air; subsequent attempts succeed. It's not dangerous but it is irritating. Check that all gas line unions are tight and properly sealed. If it persists, a gas contractor can install a better-quality check valve upstream.

**Q: The T-H3-DV runs fine alone but shows code 11 when my dishwasher or laundry is also running hot water. Is it undersized?**
A: Possibly. The T-H3-DV is rated at 199,000 BTU/hr but peak simultaneous demand may exceed its capacity, especially in colder climates where incoming water temperature is lower (requires more BTUs to reach setpoint). More likely, though, the simultaneous demand is dropping gas supply pressure below the ignition minimum. Have a gas contractor measure dynamic gas pressure under peak demand, this is a common diagnosis for multi-fixture code 11 issues.

**Q: Code 16 keeps coming back every few months. I descaled once. What am I missing?**
A: Scale is a recurring problem in hard water areas. A single descale flush won't solve it permanently if the root cause (hard water) isn't addressed. Install a whole-house water softener or at minimum a dedicated scale-inhibiting filter (polyphosphate or TAC media) on the cold water inlet to the tankless unit. The T-H3-DV's heat exchanger is stainless steel with small channels, even moderate hardness water will build scale faster than most homeowners expect.

**Q: What does the T-H3-DV error code 76 mean? My remote controller shows it occasionally.**
A: Code 76 is a communication error between the optional remote controller (RC-7001 or similar) and the main unit. Most commonly caused by a loose connection at the remote controller wiring terminals, running the remote control wire in the same conduit as line voltage wiring (induces interference), or a failed remote controller. If you don't use the remote controller, simply disconnecting it at the unit should clear the code.
