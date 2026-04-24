---
title: "ABB VFD Fault 2201 — Overcurrent Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: abb-vfd-fault-2201-overcurrent
featured: false
draft: false
tags:
  - electrical
  - vfd
  - abb
  - overcurrent
description: "ABB VFD fault 2201 means overcurrent during acceleration on ACS550, ACS310, and ACS355 drives — here's how to diagnose and fix it."
---

## Error Code: ABB VFD Fault 2201

**What it means:** Fault 2201 (OVERCURRENT) on ABB ACS550, ACS310, and ACS355 variable frequency drives indicates that the drive's output current exceeded the overcurrent trip limit — typically 3.0–3.5 times the drive's rated output current — during acceleration, deceleration, or steady-state operation. The drive shuts down immediately to protect its IGBT output stage from destruction.

ABB drives display the fault as F-2201 on the control panel LED display (or via the CDP/ACS panel on units with integral displays). The fault is logged in the drive's fault history (accessible via Parameter Group 15 on ACS550, or the Fault Logger on ACS310/355).

Fault 2201 is nearly always caused by something external to the drive — the motor, its load, or the wiring between them. The drive itself is rarely the root cause.

## Common Causes

- **Acceleration ramp too short for the connected load** — The most common cause. The drive tries to ramp the motor from 0 to full speed faster than the motor can follow, causing current to spike above the trip threshold. This is a parameter setting issue, not a hardware failure.
- **Motor or load has seized** — A jammed pump, fan, conveyor, or compressor causes locked-rotor current that immediately trips overcurrent.
- **Motor winding fault (shorted turns or phase-to-ground)** — A motor with degraded insulation draws excessive current as the drive increases voltage during acceleration. The fault often occurs at the same speed point in every acceleration cycle.
- **Output cable too long** — Long motor cables (especially over 100 meters without output reactors) cause capacitive charging current spikes that appear as overcurrent to the drive. ABB recommends output reactors or dV/dt filters on cable runs exceeding the drive's rated maximum.
- **Missing or undersized output reactor** — Without a reactor on a long cable run, reflected voltage waves damage motor insulation and cause capacitive current spikes.
- **Drive undersized for the load** — If the motor nameplate FLA exceeds the drive's rated output current, the drive will trip on overcurrent under normal load conditions.

## Step-by-Step Fix {#step-by-step-fix}

1. **Read the fault history before clearing.** On ACS550, navigate to Parameter Group 15 (Fault Logger). Note: the time of the fault, the output current at the time of trip (available in the fault data on most ACS550 firmware versions), and the output frequency at which the fault occurred. A fault that consistently happens at 10–15 Hz during acceleration points to ramp time. A fault that happens at steady state points to load or motor issues.

2. **Increase the acceleration ramp time.** On ACS550: Parameter 2202 (Acceleration Time 1). On ACS310/355: Parameter 2202 is the same. Increase from the current value by 50% and test. For high-inertia loads (large fans, centrifuges, flywheels), ramp times of 10–60 seconds are normal. The drive should never fault on overcurrent during a properly sized acceleration ramp.

3. **Check the load for mechanical binding.** Lock out/tag out the drive. Manually rotate the driven equipment. A pump, fan, or conveyor that won't turn freely has a mechanical problem. Do not attempt to run through a mechanical bind — you will damage the motor or the driven equipment.

4. **Measure motor insulation resistance.** Disconnect the motor leads from the drive output terminals. Using a 500V or 1000V megohmmeter, measure insulation resistance from each phase lead to ground (motor frame). Healthy motors read 100 MΩ or higher. A reading below 1 MΩ indicates degraded insulation — the motor needs rewinding or replacement before the drive should be reconnected.

5. **Verify cable length and check for output reactors.** Measure the total cable length from drive to motor. ABB's application guidelines for ACS550 recommend output reactors for cable lengths exceeding 100m at 400V or 50m at 690V. If cable length is marginal and no reactor is installed, add an ABB output reactor rated for the drive's current.

6. **Verify drive sizing.** Confirm the drive's rated output current (from the drive nameplate or Parameter 9906 — Motor Nominal Current on ACS550) is greater than or equal to the motor's nameplate full-load amps. If the drive is undersized, it must be replaced with a larger unit.

7. **Check current limit parameter.** On ACS550: Parameter 2003 (Maximum Current) should be set to 100–120% of motor FLA, not to 300%. If someone previously set Maximum Current too low as a "protection" measure, it may cause nuisance overcurrent trips at normal operating loads.

8. **Clear the fault and test.** Press the Stop/Reset button on the ACS550 panel, or navigate to the Fault Reset parameter. Run the drive on the panel (Local control) for a test start before returning to automatic operation. Monitor output current (Parameter 0104 on ACS550) during the full acceleration ramp.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| ABB Output Reactor (dV/dt filter) | NOCH0100-61 (varies by A rating) | $80–$350 | [Amazon](https://www.amazon.com/s?k=NOCH0100-61+%28varies+by+A+rating%29+ABB+Output+Reactor+%28dV%2Fdt+filter%29&tag=errorcodefixes-20) \| ABB distributor / Automation Direct |
| Motor (if insulation failed) | Match frame/HP/voltage | $200–$2000+ | [Amazon](https://www.amazon.com/s?k=Match+frame%2FHP%2Fvoltage+Motor+%28if+insulation+failed%29&tag=errorcodefixes-20) \| Grainger / motor repair shop |
| Replacement ACS355 Drive | ACS355-03E-07A3-4 (varies) | $500–$1200 | [Amazon](https://www.amazon.com/s?k=ACS355-03E-07A3-4+%28varies%29+Replacement+ACS355+Drive&tag=errorcodefixes-20) \| ABB distributor |
## When to Call a Professional

If fault 2201 appears during steady-state operation (not during acceleration) and the motor megger test is clean, the fault may originate from a load transient — a conveyor jam, pump cavitation, or compressor valve failure. These transient events require a power quality recorder or scope to catch in the act. An ABB-certified drive technician can set up the drive's built-in data logging (Fault Logger with pre-fault capture on ACS550 firmware versions that support it) to capture the waveform at the moment of trip. This data often pinpoints the exact cause within one site visit.

> **Pro tip:** ABB ACS550 drives log the output current at the time of each fault in the fault history. If your 2201 faults consistently show output current at exactly 150% of motor FLA, someone set the overcurrent threshold too low. If they show 300%+ of FLA, the motor is seeing true overcurrent from a mechanical or insulation event. The number in the fault log tells you which direction to troubleshoot.
