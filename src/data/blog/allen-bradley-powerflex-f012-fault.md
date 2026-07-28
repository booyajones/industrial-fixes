---
title: "Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix"
description: "PowerFlex F012 (Hardware Overcurrent) is a hard-tripped, microsecond-scale current fault detected by the gate driver circuitry, not by software. It means..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f012-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - hw-overcurrent
---
## Quick answer

PowerFlex F012 (Hardware Overcurrent) is a hard-tripped, microsecond-scale current fault detected by the gate driver circuitry, not by software. It means the IGBT current exceeded roughly 220–250% of drive rating instantaneously. The most common causes are a phase-to-phase short on the motor cable, a ground fault on the motor side, a shorted IGBT in the drive's power module, or a hard mechanical jam that produces a violent current step. **Do not press reset and try again** — F012 can indicate a destroyed power stage, and a second start may eject debris from the drive.

## What PowerFlex F012 means

F012 is fundamentally different from F006 (motor stall) or F007 (motor overload). F006 and F007 are software faults — the drive's processor saw a problem developing and chose to trip. F012 is a hardware fault — the IGBT gate driver chips saw an instantaneous overcurrent (desat detect or shunt current sensor) and shut the IGBTs off in microseconds to prevent destruction. By the time the drive's processor logs F012, the event is already over.

The 525-series uses integrated power modules with current shunts on the lower IGBTs of each phase. The threshold is roughly 220% of the drive's continuous current rating for a microsecond-scale trip. The 750-series uses similar integrated drivers but adds desaturation detection on the IGBT VCE — if the IGBT can't pull its collector below saturation voltage at the commanded current, the driver assumes a short and trips.

Because F012 is hardware-level, the fault can be triggered by:
- A real short on the motor side (the drive correctly protects itself)
- A failed IGBT (the drive's own power stage shorted, and the driver detects it)
- A current sensor failure (rare but happens — sensor reports phantom overcurrent)
- Severe noise or EMI coupling into the gate driver circuit (uncommon but possible with damaged drive ground)

Knowing which one of these you have before you reset matters. A drive with a shorted IGBT will trip F012 immediately on any subsequent start, often violently — bus capacitors dumping through the shorted phase. **Verify the power stage is healthy with a diode check before resetting.**

## Read the fault history first

Capture the diagnostic record before clearing. F012's fault history is particularly important because it tells you whether the trip was during accel (suggests a phase short on startup current), during run at speed (suggests motor cable degradation or load step), or during decel (suggests a brake chopper IGBT short or a regen overshoot).

PowerFlex 525 with 22-HIM-A3:

1. **Esc** → **Diagnostics** → **Enter**
2. **D361 Fault 1 Code** — write down code, output current at trip, output frequency at trip, bus voltage at trip
3. **D362** through **D365** — older faults. F012 preceded by F005 (overvoltage) suggests brake chopper issue. F012 preceded by F029 (analog loss) and a sudden speed reference jump suggests a load-side current step. F012 standalone with no precedent often means hardware failure.

In Studio 5000 for a 755: Faults tab, Last Fault block. Note **Peak Inverter Current** in parameter 9.

In CCW for a 525: **Drive → Faults & Alarms**.

**Field insight on diode-check before reset:** before you ever press reset on an F012, do a static diode check on the drive's power stage with the drive locked out. Power off, verify dead, wait 5 minutes for bus discharge, verify zero volts at DC bus terminals. With the motor leads disconnected from U/V/W output, use a digital multimeter in diode-check mode. Probe DC+ (red) to U (black), then V, then W — you should read open or very high (the IGBT body diodes are reverse-biased this way). Reverse polarity (red to U, V, W; black to DC+) — you should read 0.3–0.6 V (the body diodes forward-biased). Repeat from DC- to U/V/W: red to DC-, black to U/V/W reads 0.3–0.6 V; reversed reads open. A 0 V reading in either direction on any leg means a shorted IGBT — do not reset, replace the drive. A 0.2 V reading suggests partial damage. I have seen techs press reset on a drive with a shorted lower IGBT and the resulting short across the bus turned the drive into a small explosion when the soft-charge resistor couldn't limit the inrush. The 4-amp inline DMM check takes 90 seconds and is the difference between a drive replacement and a drive replacement plus a panel rebuild.

## Common causes (ranked by frequency)

1. **Motor cable short to ground** — common after a recent cable pull, after a forklift hit, or in wet environments. The fault often presents as F012 during acceleration when the inrush current is highest
2. **Motor cable phase-to-phase short** — pinched cable, rodent damage, abrasion against a sharp edge
3. **Shorted IGBT in the drive power module** — the drive's own power stage failed. Common after a previous violent event (lightning, line transient, brake resistor failure with bus overvoltage)
4. **Severe load step** — a high-inertia load suddenly coupling (clutch engagement), a jammed conveyor breaking free, a centrifuge unbalance event
5. **Motor stator-to-stator winding short** — usually develops after a previous insulation failure; megger reading will show it
6. **Brake chopper IGBT short** (drives with internal chopper) — bus regen energy unable to be dissipated, with a side effect of overcurrent on the brake leg
7. **Drive gate driver failure** — rare; usually shows up as inability to reset to a healthy state even with motor disconnected

## Step-by-step diagnosis

Safety paramount on F012: the drive may have a shorted IGBT, which means the bus capacitors could discharge into a shorted phase the instant you reapply power. Lock and tag, verify zero energy at the DC bus terminals, wait the full 5-minute discharge time, and verify with a meter on both polarities. Stay outside the arc-flash boundary. If you smell ozone, see soot at the motor terminal box, or see scorching around the drive terminals, treat the system as energized until proven otherwise.

1. **Pull the fault history before clearing.** D361–D365. Record the output current at trip, frequency at trip, and any precedent faults.

2. **Do not reset and retry.** F012 is unlike F004 or F029 — pressing reset when an IGBT is shorted will produce a violent bus discharge. Diagnose first.

3. **Lock out and verify dead.** Disconnect, verify zero at L1-L2, L2-L3, L3-L1 input. Wait 5 minutes. Verify zero at DC+ to DC-. Stay outside the arc-flash boundary until verified.

4. **Do the diode check on the power stage** (see the field insight above). DMM in diode mode, probe DC+ and DC- to each output U/V/W in both polarities. Any 0V reading on any leg means shorted IGBT — drive replacement. Document which leg shorted (helpful for warranty claims and trending).

5. **Disconnect the motor leads from U/V/W and inspect them.** Visually check the full length of the cable from the drive output to the motor terminal box. Look for crushed sections, abrasion through the jacket, signs of rodent damage. At the motor end, open the terminal box and look for scorching, water intrusion, or insulation breakdown.

6. **Megger the motor cable to ground.** With cable disconnected at both ends, 500V megohmmeter from each conductor to ground. Above 100 MΩ at 25°C: healthy. Below 1 MΩ: degraded, find and replace. Below 100 kΩ: failed, definitely the cause.

7. **Megger the motor windings to ground.** With cable disconnected from motor, 500V megohmmeter from each motor lead to motor frame. Same thresholds. Replace the motor if below 1 MΩ. Heart-broken note: a motor that meggers OK cold but trips F012 hot often has a temperature-dependent insulation failure that won't show up on a cold megger test — run a soak test if you can.

8. **Resistance-check the motor windings phase-to-phase.** With cable disconnected at motor, low-resistance ohmmeter (or four-wire micro-ohmmeter) lead-to-lead on motor terminals. The three readings (U-V, V-W, U-W) should be within 5% of each other. A reading 30% lower than the other two indicates a shorted turn in that phase — replace the motor.

9. **Check the mechanical load.** Lock and tag, uncouple if possible, rotate the driven equipment by hand. If a sudden jam happened, you'll feel it; you may also see broken components in a gearbox, a sheared coupling, or a foreign object in a conveyor.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 525, 480V, 5HP | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault) |
| PowerFlex 525, 480V, 10HP | 25B-D017N104 | $1,800–$2,100 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault) |
| PowerFlex 525, 480V, 20HP | 25B-D030N104 | $2,600–$3,100 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PowerFlex 753, 480V, 25HP | 20F11ND022AA0NNNNN | $3,800–$4,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault) |
| Replacement motor, 10HP TEFC 480V inverter-duty | Baldor ECP3770T-4 or equiv | $1,400–$1,900 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault) |
| VFD-rated motor cable, 4-conductor 10AWG | Belden 29504 or equiv | $4.50–$7/ft | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| 500V megohmmeter | Fluke 1587 FC | $720–$880 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Klein digital multimeter w/ diode | MM700 | $145–$195 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault) |
| Cable lug crimping tool | Burndy Y750 | $390–$520 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f012-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

PowerFlex 525 power stages are not separately replaceable — if the diode check shows a shorted IGBT, the whole drive is replaced. PowerFlex 753 and 755 have field-replaceable power modules on frame 3 and larger (catalog 20-PF7-PWR-xxxx), but the swap requires a controls engineer and Rockwell-trained tech for warranty.

## When to call a controls engineer

Call for senior support when: the diode check shows a healthy power stage but F012 trips again on first start (suggests current sensor or driver issue, requires drive replacement under warranty); when you have an F012 on a regenerative or common-bus configuration (the energy paths are complex and may need engineering analysis); when the same drive has tripped F012 twice in a short period after replacement (suggests an upstream root cause — load, cable, or grounding); or when the application is a critical-process drive and you need a root-cause report for the customer or for warranty.

## FAQs

**Can I reset F012 and just try again?** Not until you've done the diode check on the power stage. Resetting with a shorted IGBT can produce a violent bus discharge. Diode check first, then reset only if the power stage is healthy.

**My drive trips F012 the instant I press Start. What does that mean?** Almost certainly a shorted IGBT or a hard short on the motor side. Power off, lock out, do the diode check. If the diode check is clean, megger the motor cable.

**Why does F012 only happen during accel?** Acceleration current is the highest current the drive ever delivers — typically 150% of motor FLA for the duration of accel. A marginal motor insulation defect, a borderline cable, or a partial winding short will trip F012 only when current is highest. Megger cold and hot if you can.

**Will adding a line reactor or output filter help?** A line reactor protects the diode bridge from line-side transients but does nothing for motor-side F012. An output filter (dV/dt reactor or sine wave filter) reduces voltage stress on motor insulation and can prevent long-term degradation — worth installing on motor leads longer than 200 ft, but it won't fix an active short.

**What's the difference between F012 and F013 (Ground Fault)?** F012 is instantaneous IGBT-level overcurrent regardless of where the current goes. F013 is specifically a ground current detected by the drive's residual current sensing (a sum-of-three-phases reading that should equal zero in a healthy system). A motor cable short to ground will often trip F013 first; a stator-to-stator short will trip F012 first.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex F007 Fault — Motor Overload Fix](/allen-bradley-powerflex-f007-fault/)
- [Allen-Bradley PowerFlex F029 Fault — Analog Loss Fix](/allen-bradley-powerflex-f029-fault/)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/allen-bradley-powerflex-f081-fault/)
