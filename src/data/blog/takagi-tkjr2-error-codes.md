---
title: "Takagi TK-Jr2 Error Codes - What It Means and How to Fix It"
description: "Takagi TK-Jr2 tankless water heaters use numeric codes like 11, 12, 14, 16, 31, 52, 61, and 91 to report ignition, sensor, gas valve, fan, and exhaust faults. This guide explains every major TK-Jr2 code and the repair steps that usually fix it."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Takagi TK-Jr2 is a popular residential natural gas or propane tankless water heater with a 140,000 BTU input rating, capable of producing 5.8 GPM of hot water. It's known for reliability, but when a fault code appears on the digital display, the numeric codes can seem cryptic. Unlike other brands that use letter codes (E1, E2), Takagi uses a 2-digit numeric fault code system with distinct codes for every failure mode.

This guide is the most complete reference available for TK-Jr2 fault codes - covering all 15 primary codes, what each one means at the component level, and how to diagnose and fix each one. Whether you're a homeowner running a basic check or an HVAC/plumbing technician on a service call, this covers everything.

## What Does Takagi TK-Jr2 Error Codes Mean?

The TK-Jr2 control board monitors the entire operating cycle: flow detection, pre-purge, ignition sequence, flame verification, water temperature, combustion air, and heat exchanger temperature. When the board detects an out-of-spec condition, it shuts the unit down, displays the fault code, and stores it in the fault history.

The TK-Jr2's fault history can hold the last 3 fault codes. To retrieve the fault history, press and hold the "Set" button on the remote control for 5 seconds - the display cycles through the last 3 stored codes. This is invaluable for diagnosing intermittent faults.

### Takagi TK-Jr2 Complete Fault Code Reference

**Code 11 - Ignition Failure**
The unit attempted to ignite 3 times and did not detect a flame signal within the trial-for-ignition period.

Causes:
- Failed igniter (Part # 100013730 for TK-Jr2 compatible igniter assembly)
- Dirty or failed flame rod sensor
- Low gas pressure (should be 3.5-10.5 inches w.c. natural gas; 8.0-14.0 inches w.c. propane)
- Air in the gas line (initial installation or after supply interruption)
- Closed or partially open gas supply valve

**Code 12 - Flame Loss During Operation**
The unit ignited but the flame sensor lost the signal during a hot water draw.

Causes:
- Dirty flame sensor rod - the most common cause
- Gas pressure drop during operation (another large gas appliance activating)
- Failed gas valve (intermittent closure)
- Combustion air problem in a confined installation

**Code 14 - Thermal Fuse Blown**
A thermal fuse on the gas valve or heat exchanger assembly has opened. This is a one-shot safety device. Unlike a resettable high-limit switch, the thermal fuse must be replaced once it trips.

Causes:
- Dry fire (unit operated without adequate water flow)
- Combustion gas recirculation overheating the unit body
- Failed temperature sensor causing over-firing
- Part number for Takagi TK-Jr2 thermal fuse: **TK-Jr2-THERMO** (compatible: 10A 250V 139°C rated thermal fuse)

**Code 16 - Outlet Water Temperature Too High**
The outlet thermistor detected water temperature exceeding 185°F (85°C).

Causes:
- Very low flow rate with maximum temperature setpoint
- Failed thermistor reading low (causing board to over-fire)
- Scale buildup in heat exchanger creating hot spots
- Failed gas valve stuck partially open at full gas rate

**Code 31 - Inlet Water Temperature Sensor Failure**
The cold water inlet temperature sensor (NTC thermistor) is reading outside its normal range.

Causes:
- Failed inlet thermistor (open or shorted)
- Loose connector on control board
- Wiring damage between sensor and board

**Code 32 - Outlet Water Temperature Sensor Failure**
The hot water outlet temperature sensor is reporting an out-of-range value.

Causes:
- Failed outlet thermistor
- Scale encasing the sensor reducing thermal contact
- Loose or corroded connector

**Code 33 - Combustion Air Temperature Sensor Failure**
The combustion air temperature sensor (used by the TK-Jr2 to monitor intake air) is faulty.

Causes:
- Failed combustion air sensor
- Connector damage

**Code 52 - Modulating Gas Valve Fault**
The proportional modulating gas valve is not responding correctly to control signals. The TK-Jr2 uses a modulating gas valve that adjusts BTU output based on demand. This is a higher-value component than a simple on/off valve.

Causes:
- Failed gas valve modulating coil
- Control board failure (gas valve command circuit)
- Wiring fault between board and valve
- Valve stuck in fixed position (mechanical failure)

**Code 61 - Fan Motor Failure**
The combustion air fan is not running or not reaching commanded speed. The TK-Jr2 uses fan speed monitoring (tachometer signal) to verify safe combustion air flow.

Causes:
- Failed fan motor (Part # 100013732 for TK-Jr2 compatible fan)
- Blocked flue or air intake
- Fan blade obstructed by debris
- Tachometer signal wire failure

**Code 65 - Water Flow Control Valve Fault**
The water flow control valve (water volume control) is not responding correctly. The TK-Jr2 has an internal water control valve that regulates flow to prevent thermal shock and modulate output.

Causes:
- Failed water control valve
- Debris in valve mechanism
- Failed valve control motor
- Wiring fault

**Code 72 - Flame Signal Without Gas Valve Command**
The flame sensor is detecting a flame when the control board has not commanded the gas valve to open. This is a gas valve safety fault.

Causes:
- Leaking gas valve (gas passing through closed valve)
- Faulty flame sensor generating false signal
- Electrical interference on the flame sense circuit

⚠️ Code 72 indicates a potential gas leak through the valve. If this code appears, verify no gas odor before restarting. Call a licensed plumber to inspect the gas valve.

**Code 76 - Communication Error Between Controller and Unit**
The remote controller (if installed) has lost communication with the main unit.

Causes:
- Damaged communication wiring between remote and unit
- Failed remote controller
- Failed control board communication circuit
- Wiring polarity reversed during installation

**Code 91 - Exhaust Overtemperature**
The exhaust temperature sensor detected flue gas temperatures above the safe limit. This indicates incomplete heat transfer - the combustion gases are leaving the unit too hot.

Causes:
- Scale buildup in heat exchanger severely reducing thermal transfer
- Heat exchanger partially blocked
- Incorrect gas pressure (over-pressurized, resulting in excess combustion)
- Cold climate condensate drain blockage affecting flue

**Code 93 - Condensate Neutralizer / Drain Fault (Condensing Models)**
On condensing TK-Jr2 models, the condensate system has a fault.

Causes:
- Blocked condensate drain
- Frozen condensate line in cold weather
- Failed condensate pump (if installed)
- Failed drain monitoring switch

**Code 99 - False Flame Signal at Startup / Fan Preignition Error**
Before the ignition sequence starts, the board checks that no flame is present. Code 99 means the flame sensor detected a signal before ignition - suggesting a false reading or a genuinely abnormal pre-existing flame.

Causes:
- Dirty flame sensor generating a false signal at room temperature
- Flame sensor wire shorted to chassis
- Failed control board

## How to Fix It

**Step 1: Retrieve fault history before resetting.**
Press and hold the Set button on the TK-Jr2 remote for 5 seconds. Record all 3 stored codes. A sequence like Code 11 → Code 12 → Code 11 tells you the unit attempted ignition, briefly achieved flame, then lost it repeatedly - pointing to a gas supply or flame sensor issue rather than a complete igniter failure.

**Step 2: For Code 11 (ignition failure), test igniter and flame sensor first.**
Shut off gas and power. Access the burner chamber (remove the front cover, typically 4 screws). The igniter assembly is a spark electrode positioned approximately 3-5mm from the grounding surface. Check for visible damage - a cracked ceramic insulator means replacement is needed. The igniter part # for the TK-Jr2 is **100013730** (or compatible cross-reference). For the flame sensor, clean the rod tip with steel wool and re-test.

**Step 3: For Code 12, check gas pressure at the manifold.**
While the unit is running (if it can sustain a brief run), measure gas manifold pressure with a U-tube manometer or digital pressure gauge at the test port on the gas valve. For natural gas, manifold pressure at maximum firing should be 3.0-3.5 inches w.c. If pressure drops below 2.5 inches w.c. during operation, the issue is upstream gas supply, not the unit itself.

**Step 4: For Code 14 (thermal fuse), find the root cause before replacing.**
The thermal fuse (located on the gas valve or heat exchanger body, depending on exact assembly year) blew for a reason. Check:
- Were there any Code 31/32 faults before Code 14? A failed temperature sensor could have caused over-firing.
- Is the heat exchanger heavily scaled? Scale reduces water flow, raising heat exchanger body temperature.
Replace the thermal fuse (generic 139°C 10A 250V fuse from any electronics supplier), and then address the root cause.

**Step 5: For Code 52 (gas valve fault), test the modulating coil.**
The modulating gas valve on the TK-Jr2 has a proportional coil that the control board drives with a variable current. Disconnect the valve wiring connector and measure resistance across the modulating coil terminals. Expected resistance: 25-35 ohms for typical Takagi modulating valves. An open circuit confirms coil failure. A reading within range suggests the fault is in the board's drive circuit.

**Step 6: For Code 61 (fan failure), inspect flue first.**
Remove the flue pipe from the unit and check for obstructions at the termination cap. Also inspect the air intake (many TK-Jr2 models have a direct-vent configuration with separate intake and exhaust). Spin the fan blade by hand - it should turn freely. Any resistance suggests bearing failure. If the fan spins freely and the flue is clear but Code 61 persists, the fan motor itself needs replacement (Part # 100013732 or equivalent).

**Step 7: For Code 91 (exhaust overtemperature), perform heat exchanger service.**
Code 91 on a TK-Jr2 that's been in service for 3+ years in a hard water area almost always means significant scale on the heat exchanger. The descaling procedure: isolate the water supply at the service valves (most TK-Jr2 installations include a flushing port), connect a submersible pump to the cold inlet service port, and circulate 3 gallons of undiluted white vinegar for 45 minutes. Flush with clean water. Vinegar descaling resolves Code 91 in the majority of cases without heat exchanger replacement.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [Takagi TK-Jr2 Igniter Assembly (Part # 100013730)](https://www.amazon.com/s?i=industrial&k=Takagi+TK-Jr2+igniter+assembly+100013730&tag=errorcodefixes-20) | Replaces failed spark igniter causing Code 11 | $25-$50 |
| [Flame Sensor Rod (Takagi Compatible)](https://www.amazon.com/dp/B0CZ7M9V4D?tag=errorcodefixes-20) | Replaces corroded flame sensor causing Code 12 or 99 | $12-$25 |
| [TK-Jr2 Fan Motor Assembly (Part # 100013732)](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | Replaces failed combustion fan causing Code 61 | $85-$150 |
| [Thermal Fuse 139°C 10A (Universal)](https://www.amazon.com/s?i=industrial&k=thermal+fuse+139c+10a+250v+replacement&tag=errorcodefixes-20) | Replaces blown thermal fuse causing Code 14 | $5-$12 |
| [NTC Thermistor (Inlet or Outlet)](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) | Replaces failed temperature sensor causing Code 31 or 32 | $12-$25 |
| [Modulating Gas Valve (Takagi TK-Jr2)](https://www.amazon.com/dp/B0015KAHHA?tag=errorcodefixes-20) | Replaces failed modulating valve causing Code 52 | $180-$320 |
| [Takagi TK-Jr2 Control Board](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) | Replaces failed main PCB | $200-$380 |
| [Tankless Flush Kit (Descaling)](https://www.amazon.com/s?i=industrial&k=tankless+water+heater+flush+descale+kit&tag=errorcodefixes-20) | Annual maintenance for hard water - prevents Code 91 and heat exchanger damage | $28-$55 |

## When to Call a Pro

The Takagi TK-Jr2 is a professional-grade appliance, and several faults require licensed technician involvement:

- **Code 52 (gas valve)**: Modulating gas valve replacement requires leak testing and manifold pressure adjustment after installation.
- **Code 72 (flame without command)**: This is a potential gas leak situation. Have a licensed plumber inspect the valve before any restart.
- **Code 14 (thermal fuse) with suspected heat exchanger damage**: If descaling doesn't resolve underlying overtemperature conditions, heat exchanger replacement requires a plumber.
- **Code 91 that returns within 6 months of descaling**: This suggests the heat exchanger is failing and approaching end of life - get a professional evaluation.
- **Any time you smell gas**: Do not reset the unit. Shut off gas, ventilate, and call the gas company.

## Frequently Asked Questions

**Q: My TK-Jr2 shows Code 11 only on the first call for hot water each day, then works fine after one reset. What causes this?**
A: Morning ignition failures that clear after a reset usually point to one of two things: (1) overnight condensation on the flame sensor rod - the moisture briefly disrupts the flame signal on first ignition, then burns off; (2) air that slowly migrates into the gas line overnight, requiring one purge cycle to clear. Clean the flame sensor rod thoroughly and see if the morning Code 11 disappears.

**Q: Code 12 appears when I run the dishwasher and the shower simultaneously. Is the TK-Jr2 undersized?**
A: Not necessarily undersized, but likely experiencing a gas pressure drop. Running multiple gas appliances simultaneously (dishwasher's gas dryer nearby, gas range, etc.) can temporarily drop manifold pressure below the Code 12 threshold. Have a plumber measure dynamic gas pressure (with all appliances running) at the meter and at the TK-Jr2 inlet. If pressure drops significantly under load, a larger gas supply line may be needed.

**Q: The Code 91 keeps coming back 3 months after descaling. Is it time to replace the unit?**
A: Code 91 returning quickly after descaling suggests either very hard water is re-scaling the unit rapidly (consider a water softener or a whole-house scale inhibitor), or the heat exchanger has physical damage - corroded fins, a partial blockage that vinegar can't dissolve, or a collapsed tube. A plumber can perform a visual inspection after removal. If the unit is 10+ years old, replacement is often more economical than heat exchanger replacement.

**Q: How do I access the fault history if I don't have the remote controller?**
A: On the TK-Jr2, the remote controller is standard equipment but may have been misplaced. Takagi sells replacement remotes. In the absence of a remote, fault codes are only accessible on the display as the current active code. If the fault code clears before you see it, have a plumber connect a diagnostic tool, or call Takagi technical support (1-888-882-5244) for guidance on reading fault memory from the board directly.

**Q: Can I use a generic NTC thermistor to replace the TK-Jr2 inlet sensor?**
A: Yes, with the correct specifications. The TK-Jr2 uses 10kΩ NTC thermistors with a standard B-constant. Measure the resistance of your failed sensor at room temperature - a good one reads approximately 10,000 ohms at 77°F. Match the replacement to the same connector type and mounting bracket. Many generic HVAC thermistors with 2-pin connectors are direct replacements and cost significantly less than OEM parts.
