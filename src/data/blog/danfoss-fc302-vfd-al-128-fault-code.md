---
title: "Danfoss FC302 AL-128 - Causes & Fix"
description: "AL-128 is not a real Danfoss fault code. Technicians mislabel Alarm 13 (Overcurrent) from motor thermal protection. Check parameter 128 setting first."
pubDatetime: 2026-06-25T09:18:09Z
modDatetime: 2026-06-25T09:18:09Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 inverter board (power card)"
most_likely_cause: "Parameter 128 (Motor Thermal Protection) set too low"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the LCP display for the exact alarm number (13, 14, or 38), not AL-128"
  - "Review parameter 128 value and compare to motor nameplate full-load amperage"
  - "Power off and check all motor terminal connections for corrosion or looseness"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-128 — What It Means

The label AL-128 does not exist in the Danfoss FC302 alarm list. Parameter 128 is Motor Thermal Protection, a setting you program, not a fault code. When technicians say AL-128, they usually mean Alarm 13 (Overcurrent) triggered because parameter 128 is set too low or the motor thermal model detects an overload. The drive trips to prevent motor damage when it calculates the motor has exceeded its thermal limit based on current and time.

Alarm 13 appears when motor current exceeds the rated value, often due to incorrect thermal settings in parameter 128, a real mechanical overload on the shaft, or winding faults. If parameter 128 is programmed below the motor's actual rating (for example 80 percent of nameplate), the drive will trip under normal load thinking the motor is overheating.

## Before You Replace Anything

Technicians often replace the IGBT inverter board when Alarm 13 appears, but the real cause is usually parameter 128 set incorrectly or a motor cable fault. Always disconnect the motor and run unloaded first to isolate the drive from the motor.

[Jump to Fix](#fix)

## Common Causes

- **Parameter 128 set too low (~40%)** Motor Thermal Protection programmed below the motor's actual nameplate rating causes the drive to trip Alarm 13 under normal load because it calculates false overheating.
- **Mechanical overload on motor shaft (~25%)** Jammed pump, binding fan blades, or seized bearings force the motor to draw excess current past the thermal limit, triggering Alarm 13.
- **Loose or corroded motor cable connections (~15%)** High resistance at terminals or cable joints creates current spikes that the drive interprets as overcurrent, tripping Alarm 13.
- **Motor winding insulation failure (~10%)** Partial short or degraded winding insulation raises current draw above the thermal protection threshold and triggers Alarm 13.
- **Input voltage sag or phase imbalance (~5%)** Undervoltage or phase imbalance greater than 3 percent forces the drive to draw more current to maintain torque, tripping the thermal model.
- **Failed IGBT modules or current sensor (~5%)** Aging IGBT modules or damaged current shunt on the inverter board lose current regulation and report false overcurrent to the controller.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP display Alarm 13, Alarm 14, or a different number?</summary>
<div class="dtree-body"><strong>Yes:</strong> You have a real Danfoss alarm code. Proceed with the steps below to diagnose the motor thermal trip.<br><strong>No:</strong> If the display shows a different alarm or no alarm, consult the FC302 manual alarm list for the correct troubleshooting procedure.</div>
</details>

<details class="dtree"><summary>Is parameter 128 value equal to or greater than motor nameplate full-load amperage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter is correct. The fault is likely a real motor overload, cable issue, or winding fault. Continue to step 3.<br><strong>No:</strong> Increase parameter 128 to match motor nameplate FLA. Reset the alarm and test under load. If the alarm clears, the setting was the cause.</div>
</details>

<details class="dtree"><summary>Does Alarm 13 still appear with the motor disconnected and drive running unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive has internal component failure (IGBT modules or current sensor). Replace the inverter board or contact Danfoss service.<br><strong>No:</strong> The fault is motor-side or cable-side. Inspect motor windings, cable continuity, and all terminal connections for damage or high resistance.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off and check the exact alarm number** on the LCP display. AL-128 is not a valid code. Look for Alarm 13, Alarm 14, or Alarm 38 in the alarm history.
2. **Review parameter 128 setting** in the drive menu. Compare the programmed value to the motor nameplate full-load amperage. If parameter 128 is below nameplate FLA, increase it to match or slightly above the motor rating.
3. **Disconnect the motor** from the drive output terminals. Power on the drive and run at low speed without load. If Alarm 13 persists, the drive has internal hardware failure (IGBT or current sensor). If the alarm clears, the problem is motor or cable.
4. **Inspect motor cable and terminals** with power off. Check continuity from drive output to motor and measure winding resistance to ground with a megohmmeter. Winding resistance should be greater than 1 megohm to ground. Tighten all terminals and clean corrosion.
5. **Check input power quality** at the drive input terminals. Measure all three phases for voltage balance. Phase imbalance greater than 3 percent will cause overcurrent trips. Verify input fuses and contactors are not blown or degraded.
6. **Test motor under no mechanical load** by disconnecting the pump or fan from the motor shaft. Run the motor at low speed. If Alarm 13 clears, the mechanical load is seized or binding. Inspect bearings, couplings, and driven equipment for jams.
7. **Replace the inverter board** if the alarm appears with motor disconnected and all parameters correct. Aging IGBT modules lose current regulation and cannot be repaired. Order the replacement board by the FC302 model and serial number on the drive nameplate.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 inverter board (power card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-128-fault-code&k=Danfoss+FC302+inverter+board+%28power+card%29&tag=errorcodefixes-20) \| Match by drive frame size and voltage rating on nameplate. Contact Danfoss or authorized distributor for the exact part number. |
| Motor winding insulation test kit (megohmmeter) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-128-fault-code&k=Motor+winding+insulation+test+kit+%28megohmmeter%29&tag=errorcodefixes-20) \| 500V or 1000V insulation tester to measure winding resistance to ground before replacing motor. |

## When to Call a Pro

Call a qualified technician if the alarm persists after correcting parameter 128 and inspecting motor cables. VFD repair requires high-voltage experience and specialized diagnostic tools to measure IGBT gate voltage, current shunt calibration, and thermal model calculations. If motor winding insulation tests below 1 megohm to ground, the motor needs professional rewind or replacement. Do not attempt to open the drive enclosure or test IGBTs without lockout/tagout and arc-flash PPE. Incorrect parameter programming or wiring can damage the drive permanently or cause motor fires.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
- [Danfoss FC302 AL-88 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-88-fault-code/)
- [Danfoss FC302 VFD Alarm 46 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-46-fault-code/)
- [Danfoss FC302 Alarm 14 - Causes & Fix](/posts/danfoss-fc302-alarm-14-fault-code/)
