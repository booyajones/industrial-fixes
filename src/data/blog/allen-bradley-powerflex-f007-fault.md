---
title: "Allen-Bradley PowerFlex F007 Fault — Motor Overload Fix"
description: "PowerFlex F007 (Motor Overload) means the drive's internal I²t algorithm tripped because the integrated motor current exceeded the thermal limit set by..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f007-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - motor-overload
---
## Quick answer

PowerFlex F007 (Motor Overload) means the drive's internal I²t algorithm tripped because the integrated motor current exceeded the thermal limit set by parameter P035 (Motor OL Current). The most common real-world cause is not a bad drive or motor — it's that **P035 is set to the drive's rated FLA instead of the motor's nameplate FLA**, so the protection kicks in well before the motor is actually in distress. The second most common is a genuine mechanical load problem: worn bearings, a binding gearbox, a plugged conveyor, or a motor cooling fan that's lost airflow.

## What PowerFlex F007 means

The drive runs an inverse-time thermal model in software. It doesn't measure motor winding temperature directly (unless you have an external thermistor wired to a digital input or a 750-class with an option card) — it integrates current squared over time and decays that integral based on cooling time constants. When the integrated value crosses the limit set by P035, F007 trips.

The threshold isn't a single current value — it's a curve. At 150% of P035 the drive will trip in roughly 60 seconds. At 200% it trips in about 30 seconds. At 110% it might run for 30 minutes before tripping. The exact curve is in Rockwell publication 520-RM001 for the 525 and is broadly compatible with NEMA Class 10 overload protection.

On a PowerFlex 525 the relevant parameters are:
- **P035 Motor OL Current** — should be set to motor nameplate FLA, not drive FLA
- **A410 Motor OL Hertz** — frequency below which the OL curve is derated for reduced motor cooling (default 33 Hz)
- **A411 Motor OL Mode** — selects between standard NEMA and IEC curves, plus a "no derate" option for inverter-duty motors with separate cooling
- **A435 Motor OL Reset Level** — how cool the model has to get before allowing reset

On a 750-class drive the equivalents are parameters 47, 48, 49, with much finer control and the ability to bring in an external PTC thermistor via parameter 153.

The 4-class drives have a simpler curve and only the motor FLA parameter (P033 in their numbering). They're less granular but follow the same physics.

## Read the fault history first

Clearing F007 zeroes the drive's accumulated thermal model — you lose the current at trip and the elapsed time at overload. Pull the history first.

On a PowerFlex 525 with the 22-HIM-A3:

1. **Esc** to main menu, **Diagnostics**, **Enter**
2. **D361 Fault 1 Code** — most recent fault
3. **D362** through **D365** — older faults
4. Note the **motor current at trip** (the drive stores this alongside each fault code) and **drive temperature**

In Studio 5000 for a 755: Faults tab, Last Fault block shows fault code, output current at trip, output frequency at trip, and motor thermal capacity used. The thermal capacity reading is gold — it tells you whether the trip was sudden (capacity jumped from 50% to 100% in a few seconds, suggests jam or stall) or gradual (capacity climbed steadily over minutes, suggests sustained overload or undersized motor).

In CCW for a 525: **Drive → Faults & Alarms** shows the same data.

**Field insight:** when F007 trips and you read the fault history, also note the **output frequency at trip**. F007 below 20 Hz is almost always a low-speed cooling problem on a self-cooled (TEFC) motor — the fan on the back of the motor isn't moving enough air to dissipate the I²R losses, even though the current is well below rated FLA. The fix is not to tweak P035; it's to enable the low-speed derate (A410 Motor OL Hertz set correctly) or use a separately-cooled motor. I've watched plants chase mechanical problems for weeks on conveyors that ran at 8 Hz all shift because nobody set A410 to 33 Hz from its default of 33 Hz — wait, that's the default — except someone had set it to 5 Hz to "stop the nuisance trips" two years ago, and the motor was cooking itself slowly.

## Common causes (ranked by frequency)

1. **P035 Motor OL Current set incorrectly** — usually defaulted to drive FLA at commissioning and never changed to motor nameplate FLA. Smaller motor on a larger drive is the classic trap
2. **Mechanical load problem** — bearing failure, gearbox jam, conveyor blockage, pump cavitation, fan belt slipping
3. **Motor cooling fan blocked or failed** — TEFC fan covered in dust, fan blade cracked, fan shroud bent into the blade
4. **Sustained low-speed operation on a self-cooled motor without A410 set correctly** — motor runs but can't dissipate heat at the reduced fan RPM
5. **Single-phasing on the motor side** — one output phase open (cable damage, loose lug at motor) makes the other two pull 1.73× normal current to deliver the same torque
6. **Motor windings degraded** — insulation breakdown reduces effective impedance, motor draws higher current for the same load
7. **Wrong V/Hz curve for the application** — boost set too high (A484 Boost Select) puts excess current into the motor at low speed
8. **Process overload — the load actually exceeds motor rating** — common on retrofits where the operator pushed throughput beyond what the original motor was sized for

## Step-by-step diagnosis

Safety: F007 trips can happen because of a mechanical jam that's still binding. Before you turn the disconnect back on, verify the driven equipment is clear — rotate the shaft by hand if you can reach it. Lock and tag for any internal work. Wait the 5-minute discharge time before touching bus terminals.

1. **Pull the fault history before clearing.** D361 in particular — note the fault code, the **output current at trip**, and the **output frequency at trip**. If you see F007 at 4 A on a drive rated for 12 A, the parameter P035 is probably misconfigured. If you see F007 at 18 A on the same drive, you have a real overload.

2. **Verify P035 Motor OL Current against the motor nameplate.** Look at the motor's nameplate FLA — it's stamped on a plate on the motor housing. Set P035 to that exact value. A 5HP TEFC motor at 460V is typically 6.8–7.6 A; a 10HP is 13.2–14.0 A. If P035 was at the drive's default (often the drive's own FLA), this single change may resolve the fault entirely.

3. **Check the application against the trip frequency.** If the trip happened below 20 Hz on a TEFC motor, set parameter **A410 Motor OL Hertz** to 33 Hz (525 default) or 20 Hz for an inverter-duty motor, and verify **A411 Motor OL Mode** is set to **0 (Std NEMA)**. For motors with separate cooling (separately-ventilated blower-cooled or with a constant-speed cooling fan on a separate circuit), set A411 to **1 (No Derate)**.

4. **Rotate the driven equipment by hand with the drive off.** Lock and tag, uncouple if you can. Spin the shaft. If it binds, drags, or feels stiff in spots, you have a mechanical problem — bearings, alignment, gearbox, or a foreign object in the load. No amount of drive tuning will fix this.

5. **Inspect the motor cooling.** Pull the fan shroud cover. The TEFC fan should be clean, intact, and tight on the shaft. A fan caked in dust loses 30–50% of its airflow. A cracked fan blade unbalances and slips. A shroud bent against the fan blocks airflow entirely. Clean or replace.

6. **Measure motor lead current with a clamp meter during operation.** Use a true-RMS clamp on U, V, W output leads at the motor. All three should be within 5% of each other. Significant imbalance (over 10%) means a single-phasing or stator winding fault.

7. **Megger the motor.** With drive locked out and motor disconnected from drive output, use a 500V megohmmeter winding to ground. Above 100 MΩ at 25°C is healthy. Below 1 MΩ is degraded. Below 100 kΩ is failed — replace the motor.

8. **Look at the load curve.** Pull motor current at idle, at minimum speed, at full speed, and at full load. Plot or just note. A motor that draws 80% FLA at no-load is in trouble — either internally (bad bearings, dragged stator) or fighting an external load you didn't know about (mis-aligned coupling, dragging seal, plugged impeller).

9. **Tune V/Hz boost if applicable.** On a 525 in V/Hz mode, parameter **A484 Boost Select** raises the voltage at low speed to overcome stator IR drop. Too much boost (set above 7.5% on a standard motor) injects excess current at low speed and causes F007. Reduce boost one step and retest.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 525 replacement (5HP, 480V) | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO) |
| PowerFlex 525 internal cooling fan kit | 25-FAN1-B70 (frame B) | $85–$120 | [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| TEFC motor cooling fan (Baldor 5HP) | 36FN1004A02SP | $45–$75 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Replacement motor, 5HP TEFC 480V inverter-duty | Baldor EM3611T or equiv | $850–$1,250 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI) |
| Klein Tools clamp meter (true RMS) | CL800 | $180–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [AutomationDirect](https://www.automationdirect.com?aff=PLACEHOLDER-ADI) |
| 500V megohmmeter | Fluke 1587 FC | $720–$880 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Motor PTC thermistor (PTC type) | Various 130°C trip | $35–$95 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |
| 20-750-UFB-1 universal feedback option (755) | 20-750-UFB-1 | $380–$520 | [Galco](https://www.galco.com?aff=PLACEHOLDER-GALCO), [Wolf Automation](https://www.wolfautomation.com?aff=PLACEHOLDER-WOLF) |

If the drive's internal cooling fan has failed (you'll see F008 Heatsink Overtemp or a heatsink temp alarm preceding F007), replace the drive fan, not the drive — the 525 fans are field-replaceable on frames B and larger.

## When to call a controls engineer

Call senior support when: F007 trips persist after P035 is verified correct, mechanicals are checked, motor is meggered healthy, and cooling is confirmed; when you suspect the motor is undersized for the application (need to size up and retune the drive); when you're integrating a motor with external thermistor protection and need to wire it to a digital input or option card; or when the application is a low-speed high-torque load like a positive-displacement pump or extruder and you need to evaluate constant-torque vs. inverter-duty motor selection.

## FAQs

**My drive trips F007 every Monday morning but runs fine the rest of the week. Why?** Almost always a mechanical problem that's worse cold — grease stiffened over the weekend, condensation in the gearbox, a seal hardened from sitting. Run the equipment dry for a few minutes after the weekend or add a heater to the gearbox.

**Can I just raise P035 to stop F007?** Only if you've verified the motor nameplate FLA is higher than the current P035 setting. Raising P035 above motor nameplate FLA disables thermal protection and will burn the motor. Some plants do this anyway and pay for it in winding rewinds.

**How is F007 different from F064 (Drive Overload)?** F007 protects the *motor* based on integrated current vs. P035. F064 protects the *drive* IGBTs based on integrated current vs. drive rating. A small motor on a large drive can trip F007 while the drive is barely warm; a large motor on a small drive can trip F064 while the motor is fine.

**Should I add an external overload relay?** Generally no — the drive's protection is more sophisticated than a thermal overload relay because it's adjusted for speed (and therefore cooling). Adding an external OL relay between drive and motor causes harmonic-current nuisance trips. Use the drive's protection plus a motor thermistor if you want belt-and-suspenders coverage.

**Why does F007 take so long to clear?** The thermal model has a cooling time constant. Even with the drive stopped, the model decays at the rate the motor cools — which is slow on a stopped TEFC motor with no fan moving. Wait 5–10 minutes, or temporarily change A435 Motor OL Reset Level to allow earlier reset (not recommended for production use).

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
- [Allen-Bradley PowerFlex F029 Fault — Analog Loss Fix](/allen-bradley-powerflex-f029-fault/)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/allen-bradley-powerflex-f081-fault/)
