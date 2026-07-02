---
title: "Danfoss FC302 AL-136 Fault - Causes & Fix"
description: "AL-136 is not a valid FC302 code. The likely code is Alarm 13 (overcurrent). Most common fix: verify motor parameter 1-24 matches motor rating."
pubDatetime: 2026-06-25T09:24:13Z
modDatetime: 2026-06-25T09:24:13Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 power card / IGBT module"
most_likely_cause: "Incorrect motor nominal current setting in parameter 1-24"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify parameter 1-24 (motor nominal current) matches the actual motor nameplate rating exactly"
  - "Inspect all motor cable connections for loose or corroded terminals"
  - "Check that all cooling vents and fans are clear and operating"
part_price: "$600-1,800"
no_buy_pct: "65%"
---

## Danfoss FC302 AL-136 Fault — What It Means

No fault code AL-136 exists in Danfoss FC302 documentation. The drive uses numeric alarm identifiers like Alarm 13, Alarm 14, and Alarm 4. The most probable match is Alarm 13, which indicates output current exceeding safe operating thresholds during normal operation or acceleration. This fault triggers when current builds beyond the drive's rated capacity (typically 150–160% of nominal current sustained for several seconds), protecting the drive from thermal overload and IGBT damage. The fault is not an instantaneous short circuit but rather a gradual current buildup that exceeds safe limits.

Alarm 13 protects the drive hardware by shutting down before heat damages the inverter module. The drive monitors current through internal sensors and compares it against parameter settings. When the threshold is crossed for too long, the alarm latches and stops the motor. The fault can originate from mechanical issues on the motor side, incorrect parameter configuration, or internal drive component failure.

## Before You Replace Anything

Technicians often replace the entire inverter power module when Alarm 13 appears, but most cases stem from wrong parameter 1-24 settings or mechanical motor overload. Always disconnect the motor and run the drive unloaded first to isolate whether the fault is in the drive or the motor circuit.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor parameter 1-24 (~35%)** Motor nominal current setting does not match the actual motor nameplate current, causing the drive to trip on normal load.
- **Mechanical overload on motor shaft (~25%)** Jammed pump, seized bearing, or blocked load forces the motor to draw excessive current during acceleration or running.
- **Loose or corroded motor cable connections (~15%)** High resistance at connection points creates voltage drop and current spikes that exceed drive limits.
- **Partial short in motor windings (~10%)** Insulation degradation allows turn-to-turn or phase-to-ground faults that increase current draw.
- **Insufficient cooling airflow (~8%)** Blocked vents or failed cooling fan cause thermal stress that lowers the drive's current-handling capacity.
- **Aging or damaged IGBT modules (~7%)** Internal drive components fail to regulate current properly, triggering false overcurrent alarms or allowing real overcurrent conditions.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display Alarm 13 (not AL-136) on the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> Proceed with Alarm 13 diagnostics below.<br><strong>No:</strong> Check your drive model documentation for the exact code displayed, as AL-136 does not exist in FC302 manuals.</div>
</details>

<details class="dtree"><summary>Does Alarm 13 clear when you disconnect the motor cables and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is in the motor, motor cables, or mechanical load. Inspect motor connections, test winding insulation, and check for mechanical binding.<br><strong>No:</strong> The fault is internal to the drive. Check for failed IGBTs, current sensors, or internal wiring damage.</div>
</details>

<details class="dtree"><summary>Does parameter 1-24 (motor nominal current) exactly match the motor nameplate current rating?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter is correct. Move to mechanical and motor insulation testing.<br><strong>No:</strong> Set parameter 1-24 to the exact nameplate current and reset the alarm. This fixes most Alarm 13 cases.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the disconnect. Wait at least five minutes for capacitors to discharge before opening the enclosure.
2. **Check parameter 1-24** on the keypad. Compare the value to the motor nameplate nominal current. If they do not match exactly, enter the correct current value and save.
3. **Verify all motor data parameters** (120–125 in some firmware versions) match the motor nameplate for voltage, frequency, speed, and power factor.
4. **Disconnect the motor cables** at the drive output terminals. Power up the drive and attempt to run it unloaded at low speed. If Alarm 13 persists, the drive has an internal fault (proceed to step 7).
5. **Inspect motor wiring and connections** if the drive runs unloaded without fault. Tighten all terminals, clean any corrosion, and verify continuity from drive outputs to motor windings.
6. **Perform a megohm insulation test** on the motor windings to ground. Readings below 2 megohms indicate insulation failure requiring motor repair or replacement.
7. **Check cooling and internal components** if the drive faults while unloaded. Verify all fans operate, clean blocked vents, and inspect for damaged current sensors or IGBT modules. Log extended alarm data in parameter 15-32 for diagnostic codes.
8. **Reset the alarm** by pressing the Reset button or cycling power. Reconnect the motor and run a test cycle under normal load. Monitor current on the display during acceleration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 power card / IGBT module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-136-fault-code&k=Danfoss+FC302+power+card+%2F+IGBT+module&tag=errorcodefixes-20) \| Order by drive frame size and voltage rating stamped on the module cover. |
| Danfoss FC302 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-136-fault-code&k=Danfoss+FC302+control+board&tag=errorcodefixes-20) \| Required if current sensor circuits have failed, less common than power module failures. |
| Drive cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-136-fault-code&k=Drive+cooling+fan+assembly&tag=errorcodefixes-20) \| Match the part number on the fan housing, varies by drive frame size. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if the alarm persists after you have verified parameter 1-24 and checked motor connections. Internal drive faults require high-voltage diagnostic tools, IGBT module testing, and current sensor calibration that are not safe for untrained personnel. Also call a pro if motor insulation testing shows readings below 2 megohms, as motor rewind or replacement requires specialized equipment. If the motor is mechanically jammed or you suspect bearing failure, a motor shop or mechanical technician should inspect the shaft and bearings before you restart the drive. Do not attempt to replace IGBT modules or control boards without proper training in handling high-voltage DC bus capacitors and electrostatic-sensitive components.

**Rough cost:** A pro service call runs about $150-400 for parameter adjustment and diagnostics, $800-2,500 if IGBT module replacement is needed.

## See Also

- [Danfoss FC302 AL-76 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-76-fault-code/)
- [Danfoss FC302 VFD AL-106 - Causes & Fix](/posts/danfoss-fc302-vfd-al-106-fault-code/)
- [Danfoss FC302 W66 - Causes & Fix](/posts/danfoss-fc302-vfd-al-66-fault-code/)
- [Danfoss FC302 Alarm 43 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-43-fault-code/)
