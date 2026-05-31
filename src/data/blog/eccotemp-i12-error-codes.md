---
title: "Eccotemp i12 Error Codes - What It Means and How to Fix It"
description: "Eccotemp i12 indoor tankless water heaters use E1 through E9 codes to report ignition, flame, temperature, flow, and fan faults. This guide explains what each code usually means and how to diagnose the likely failed part."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The Eccotemp i12 is a natural gas or propane indoor tankless water heater that produces up to 3.1 gallons per minute, making it suitable for a bathroom addition, a small cabin, or as a supplemental unit. Like all gas tankless water heaters, the i12 has a sophisticated ignition and safety system that monitors flame, temperature, water flow, and gas pressure. When something goes wrong, the digital display shows an error code. This guide covers every code the i12 can display, what the control board is detecting, and how to diagnose and fix each fault.

## What Does Eccotemp i12 Error Codes Mean?

The Eccotemp i12 control board monitors the entire combustion cycle: water flow activates the flow sensor, which triggers the ignition sequence. The gas valve opens, the igniter fires, and the flame sensor verifies combustion. Temperature sensors at the inlet and outlet monitor water temperature throughout the heat cycle. If any step fails or goes out of bounds, the unit shuts down and displays an error code on the LED panel.

The i12 runs on a standard 110-120VAC power supply (unlike electric tankless units, it only uses electricity for ignition, controls, and the fan). The typical setup uses D-cell batteries as the primary ignition power source on some models, while others use an AC adapter - verify yours before troubleshooting electrical faults.

### Eccotemp i12 Error Code Reference

**E1 - Ignition Failure / No Ignition**
The control board initiated the ignition sequence - the flow sensor detected water, the gas valve opened, and the igniter activated - but the flame sensor did not confirm ignition within the trial-for-ignition window. After typically 3 attempts, the board locks out and displays E1.

Causes:
- Depleted or weak batteries (on battery-ignition models)
- Failed igniter electrode (cracked ceramic, fouled tip, incorrect gap)
- Low gas pressure (supply pressure should be 3.5-7 inches w.c. for natural gas, 8-11 inches w.c. for propane)
- Closed gas supply valve or empty propane tank
- Gas line air purge needed (after initial installation or if gas supply was interrupted)
- Blocked burner orifice

**E2 - Flame Loss / Flame Sensor Fault**
The unit successfully ignited - E1 didn't occur - but the flame sensor lost the flame signal during operation. The unit shuts off and displays E2.

Causes:
- Dirty or corroded flame sensor rod
- Flame sensor lead wire damage or loose connection
- Combustion air issue - insufficient fresh air supply for indoor installation
- Gas pressure fluctuation during operation (pressure drops when another gas appliance activates)
- Wind or draft interference (even indoor units can be affected by strong drafts)
- Failed flame sensor

**E3 - Overtemperature Shutdown / High Outlet Temperature**
The water temperature sensor detected an outlet temperature above the unit's safety limit (typically 167°F / 75°C maximum, with safety shutoff above that threshold).

Causes:
- Very low water flow rate with high temperature setpoint
- Failed or stuck-open gas valve (excessive gas flow)
- Failed outlet temperature sensor (reading low, causing the board to over-fire)
- Scale or mineral buildup in the heat exchanger reducing flow velocity

**E4 - Inlet or Outlet Water Temperature Sensor Fault**
One of the water temperature sensors (NTC thermistors) is reading outside its expected range.

Causes:
- Failed thermistor (open or shorted)
- Loose sensor connector on the control board
- Physical damage to sensor from impact or scale

**E5 - Overheating Protection / Heat Exchanger Overheat**
The heat exchanger temperature exceeded the safe limit. This is distinct from E3 (water outlet temperature) - E5 is the heat exchanger body temperature itself.

Causes:
- Blocked water flow through heat exchanger (scale, sediment, or partially closed valve)
- Combustion issue causing excess heat output
- Failed cooling fan (if unit has a cooling fan)

**E6 - Water Temperature Sensor Short Circuit**
A water temperature sensor has shorted (reading abnormally low resistance, indicating a short to ground or a failed sensor).

Causes:
- Failed NTC thermistor (shorted element)
- Water intrusion into sensor connector
- Damaged wiring

**E7 - Fan Motor Fault (Duct/Indoor Models)**
The flue fan or combustion air fan is not running at the commanded speed or has failed to start.

Causes:
- Failed fan motor
- Blocked flue or exhaust vent
- Fan blade obstructed
- Failed fan control circuit on the control board

**E8 - Dry Fire Protection / Low Water Flow**
Similar to E1 but specific to water flow during operation - the unit started successfully but the flow sensor detected a drop in flow below the minimum threshold during a hot water draw.

Causes:
- Flow sensor partially clogged with debris
- Supply water pressure dropping during operation
- Partially closed inlet filter clogged
- Failed flow sensor

**E9 - Flame Failure After Ignition**
The unit lit, but lost flame within a very short period - faster than the normal E2 detection window. This often indicates an immediate flame extinguishment at or near ignition.

Causes:
- Gas pressure issues (too low for stable combustion)
- Igniter and flame sensor too close together causing "flash" ignition without sustained flame
- Burner assembly issue
- Moisture or contamination in the gas line

## How to Fix It

**Step 1: For E1 (ignition failure), start with the gas supply and batteries.**
Check that the gas supply valve at the wall is fully open. If this is a propane installation, verify the tank is not empty - even with a full gauge, regulator failure can cut supply. On battery-powered ignition models, replace the D-cell batteries even if the display lights up - ignition circuits need full voltage (1.5V per cell), and partially depleted batteries can power the display but fail during the high-draw ignition spark. Fresh batteries resolve E1 on battery-ignition i12 models more often than any other fix.

**Step 2: Purge air from the gas line.**
After the gas supply has been off (new installation, tank swap, interrupted supply), air in the gas line prevents ignition. Open a hot water tap at the unit. Attempt ignition 5-7 times in quick succession - each attempt pushes more air out of the line. After 5-7 attempts, if the unit still shows E1, the line may need more purging time or the gas pressure needs to be verified.

**Step 3: For E2 (flame loss), clean the flame sensor.**
Locate the flame sensor rod inside the burner assembly - it's a single metal probe with a ceramic insulator, positioned to sit within the burner flame. Shut off gas and power. Remove the burner access panel (usually 2-4 screws on the i12). Clean the flame sensor tip with fine steel wool or emery cloth. Reinstall and test. If the flame sensor connector at the control board is corroded, clean it with electrical contact cleaner.

**Step 4: For E2 related to combustion air, check the installation space.**
The i12 is an indoor unit but still requires adequate combustion air. A small, sealed utility closet without ventilation can starve the unit of oxygen, causing unstable combustion and E2 faults. Check that the installation space meets Eccotemp's minimum cubic footage requirements (typically 150 cubic feet per 1,000 BTU/hr input) or has a fresh air duct.

**Step 5: For E3 or E8 (temperature or flow issues), inspect the inline filter.**
The Eccotemp i12 has an inline cold water filter at the inlet connection. Remove and clean this filter annually or whenever E3 or E8 appears without an obvious cause. In areas with high sediment content, the filter can clog within months. Also verify the heat exchanger hasn't scaled - remove and visually inspect if the unit is more than 2 years old in hard water service.

**Step 6: Test the gas valve.**
The Eccotemp i12 uses a solenoid-activated gas valve. With the unit showing E1 or E9 and the gas supply confirmed, listen carefully during an ignition attempt: you should hear a faint click from the gas valve opening. No click may indicate a failed valve solenoid. Measure 12VDC across the solenoid terminals during an ignition attempt - if voltage is present but the valve doesn't click, the solenoid has failed.

**Step 7: For E7 (fan fault), check the flue pipe.**
The i12's combustion fan can fail to reach speed if the flue is obstructed. Inspect the entire flue run (typically 2-3 inch PVC or stainless flex) for kinks, obstructions, birds' nests (at the exterior termination), or ice blockage in winter. Also verify the fan spins freely by hand with power disconnected - stiff bearings are an early sign of fan motor failure.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Eccotemp i12 Igniter Electrode](https://www.amazon.com/s?ascsubtag=ecf-eccotemp-i12-error-codes&k=Eccotemp+i12+igniter+electrode+replacement&tag=errorcodefixes-20) | Replaces cracked or fouled igniter causing E1 fault | $15-$28 |
| [Flame Sensor Rod (Universal Gas)](https://www.amazon.com/s?k=Flame+Sensor+Rod+%28Universal+Gas%29&tag=errorcodefixes-20) | Replaces corroded flame sensor causing E2 fault | $10-$20 |
| [Gas Valve Solenoid (12V)](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-eccotemp-i12-error-codes&tag=errorcodefixes-20) | Replaces failed gas valve on Eccotemp i12 | $35-$65 |
| [Flow Sensor (Paddle Type)](https://www.amazon.com/s?ascsubtag=ecf-eccotemp-i12-error-codes&k=Eccotemp+flow+sensor+paddle+water+heater&tag=errorcodefixes-20) | Replaces failed flow sensor causing E1 or E8 fault | $18-$35 |
| [NTC Temperature Sensor](https://www.amazon.com/dp/B09FFFPF5L?ascsubtag=ecf-eccotemp-i12-error-codes&tag=errorcodefixes-20) | Replaces failed water temperature sensor causing E4 or E6 | $10-$22 |
| [Eccotemp i12 Control Board](https://www.amazon.com/s?k=Eccotemp+i12+Control+Board&tag=errorcodefixes-20) | Replaces failed main control board when multiple codes persist | $55-$95 |
| [D-Cell Batteries (8-pack)](https://www.amazon.com/s?ascsubtag=ecf-eccotemp-i12-error-codes&k=D+cell+batteries+alkaline+8+pack&tag=errorcodefixes-20) | Powers ignition circuit - replace when E1 code appears first | $12-$18 |

## When to Call a Pro

The Eccotemp i12 is a relatively approachable gas appliance for DIY diagnosis, but some situations require a licensed plumber or gas technician:

- **Gas valve replacement**: Any work on the gas valve requires pressure testing after reassembly to confirm there are no leaks.
- **Persistent E1 after battery and igniter replacement**: This may indicate low gas pressure at the appliance, which requires a manometer test of manifold pressure - a technician's job.
- **E3 or heat exchanger faults on a unit over 5 years old**: Descaling or heat exchanger replacement is best done by someone with the correct tools and chemicals.
- **Any smell of gas**: If you smell gas, turn off the supply, ventilate, and call your gas company before any other action.

## Frequently Asked Questions

**Q: My Eccotemp i12 shows E1 after sitting unused all summer. Is this normal?**
A: Very common. Air infiltrates the gas line when the unit isn't used for months. Follow the purge procedure in Step 2 above - attempt ignition repeatedly to push air out. If E1 persists after 10 attempts, check that the gas valve at the wall wasn't accidentally shut off. Also replace the batteries on battery-ignition models regardless - batteries degrade in storage.

**Q: The i12 ignites fine but shows E2 after about 5 minutes of operation. What causes mid-run flame loss?**
A: Mid-run E2 almost always points to a combustion air problem or a gas pressure fluctuation. Time it - if the failure is exactly predictable (always at minute 5), it suggests the unit is depleting the oxygen in an enclosed space. If the timing is random, check whether other gas appliances in the home (HVAC, dryer) are activating around the same time as E2 occurs, which could be dropping your gas pressure.

**Q: How do I reset the Eccotemp i12 after an error code?**
A: Turn off the hot water tap to stop the call for hot water. Wait 30-60 seconds. The display should clear. Turn the tap back on. If the error returns immediately, the underlying fault hasn't been resolved. If the unit operates normally after the reset, the fault may have been transient (momentary pressure fluctuation, brief air in gas line).

**Q: The i12 shows E3 only in winter. In summer it works perfectly. What gives?**
A: In winter, incoming cold water requires more heat to reach setpoint. At low flow rates, the unit applies maximum BTU output. If your temperature setpoint is near maximum (120-140°F) and winter flow rates are even slightly lower than summer (due to pipe pressure differences), the outlet temperature can spike above the E3 threshold. Lower your temperature setpoint by 10°F in winter, or run slightly higher flow rate at the fixture.
