---
title: "Allen-Bradley PowerFlex F070 Fault — Power Unit Fault Fix"
description: "PowerFlex F070 (Power Unit Fault) is the drive telling you its internal hardware self-diagnostics caught something the control board can't recover from — a..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f070-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - power-unit-fault
---
## Quick answer

PowerFlex F070 (Power Unit Fault) is the drive telling you its internal hardware self-diagnostics caught something the control board can't recover from — a power-stage feedback signal out of range, a gate-driver fault that didn't fit the F063 desat signature, or a power-supply rail on the gate-drive ASIC that's drooping. F070 is the most "drive-side" of the major PowerFlex fault codes; about 70% of the time it's a real hardware failure inside the drive enclosure, and about 30% of the time it's an EMI, grounding, or external power problem that has corrupted the diagnostic feedback path.

## What PowerFlex F070 means

The PowerFlex control board runs a periodic self-check on every power-stage feedback signal: current sensor outputs, gate-drive ready signals, IGBT temperature feedback, internal +5V and +15V rails feeding the gate-drive ASICs, and DC-bus voltage sense. F070 fires when one of those internal checks falls outside the expected window long enough for the firmware to call it a hardware fault rather than a transient.

The fault doesn't tell you *which* internal subsystem tripped — that's the frustrating part. On a PowerFlex 525 you get F070 and a bus voltage at trip; that's it. On a 753/755 the fault buffer is richer and exposes subcode information that points to which power-stage feedback channel failed. In Studio 5000 you can read this via the **Drive Faults** tab; the subcode (sometimes called the "auxiliary fault code") is the differentiator between, say, a current sensor failure and a gate-drive supply failure.

Critically: F070 is not the same as F012 (HW Overcurrent) or F063 (Phase Short). Those two are *external* fault detectors — they reflect what's happening on the motor side. F070 is the drive's *internal* watchdog. When F070 fires repeatedly with no external cause, the drive has a real problem.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a wild parts swap. **Do not clear the fault before you read the history.** Clearing wipes the diagnostic record on every PowerFlex series.

On a PowerFlex 525 with a 22-HIM-A3 keypad:

1. From the run screen, press **Esc** until you reach the main menu
2. Arrow to **Diagnostics** and press **Enter**
3. Select **Fault 1 Code** — parameter **D361** (most recent)
4. Read **D362** through **D365** for the four older faults
5. Note any precedent faults — was there an F012, F063, or F081 right before the F070? That changes the diagnosis significantly

On a PowerFlex 755 in Studio 5000: expand the drive in the I/O tree, right-click, **Properties → Drive → Faults**. Look for the subcode field next to each F070 entry. Common subcodes include current sensor channel U/V/W out of zero range at power-up, gate driver supply low, and bus sense out of range — but Rockwell publication 750-RM002 is the authoritative subcode table.

**Field insight on F070:** the precedent fault matters more than the F070 itself. An F070 immediately following an F012 is usually the drive saying "I just lost a power-stage channel as a side effect of that overcurrent" — that's a real hardware failure. An F070 with no precedent is more often a one-shot diagnostic glitch from EMI, a poor ground, or a momentary control-power dip. Don't replace a drive on a single isolated F070 unless you can also confirm it on power cycle.

## Common causes (ranked by frequency)

1. **Current sensor failure inside the drive** — the Hall-effect or shunt-based output current sensors drift out of zero range or fail entirely. Most common F070 root cause on drives 8+ years old.
2. **Gate-drive supply rail failure** — the small DC-DC converters that feed the gate-drive ASICs lose regulation. Often shows up as a one-leg-only failure.
3. **EMI corruption of feedback signals** — drive panel grounding has degraded, or a nearby contactor is dumping transients on the shared 24VDC control bus, and the firmware sees a momentary out-of-range condition.
4. **Bus voltage sense fault** — the bus voltage divider network or its ADC channel drifted. Usually a precursor to bigger problems.
5. **Power-stage thermal sensor failure** — the IGBT temperature feedback fails open and the firmware can't validate thermal operation.
6. **Control board / power board interconnect** — ribbon cable or board-to-board connector with a marginal pin, exacerbated by panel vibration or temperature cycling.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time (5 minutes minimum on a PowerFlex 525, longer on 753/755 frames 3 and up), and verify zero energy at the DC bus terminals with a CAT-IV meter. Bus caps stay lethal for many minutes after the input is dead.

1. **Read the fault history first.** Record F070 occurrences, all subcode data on a 755, and any precedent faults. Look for patterns: does F070 happen only at power-up, only at start, only at full load, only on a specific day? Patterns isolate root cause.

2. **Power-cycle the drive and watch.** Drop control power, wait 5 minutes, restore power. Watch the boot sequence. If the drive boots clean and runs without F070, you may have a one-shot EMI event. If it throws F070 immediately on power-up, you have a real hardware issue and the drive is likely toast.

3. **Verify panel grounding.** This is the single most common external cause of phantom F070s. Confirm: drive ground lug is bonded to the panel sub-plate with copper bus or a green-yellow conductor of adequate gauge; sub-plate is bonded to the enclosure; enclosure is bonded to building ground via the equipment grounding conductor; motor frame ground is brought back to the drive ground lug, not "anywhere convenient." A floating or high-impedance ground will absolutely produce intermittent F070.

4. **Inspect the drive enclosure interior.** Look for: blown vents, scorch marks, swollen capacitors visible through the air-intake louvers (on 525 and smaller 755 frames), discoloration on the heatsink fan housing, contamination (dust, oil mist, conductive debris) coating the control board. Any of these is bad news.

5. **Check ambient and internal temperature trend.** Pull parameter **U101 Heatsink Temp** on a 525. Normal at idle in a 25°C panel is 30–45°C. Idle heatsink temps above 60°C with no load suggest a fan problem or contamination. Heatsink running hot fries gate-drive supplies, which throws F070 weeks later.

6. **Verify control power supply quality.** The 24VDC control supply feeding the drive's logic side should be within ±5% of nominal. Dirty 24VDC from a marginal panel power supply can cause F070 on otherwise healthy drives. Meter the supply with a scope if you have one; look for ripple over 200 mV peak-to-peak.

7. **Inspect ribbon cables and internal connectors.** On a 755 frame 3+ you can pull the front cover and access the ribbon cable between the control board and power board. Re-seat it. If the drive has been on a vibrating platform (compressor skid, large fan deck), connector pin retention degrades over time.

8. **Cycle test the drive uncoupled.** If you can disconnect the motor and run the drive into open circuit at low frequency (1 Hz, no motor connected), the drive should run without F070 indefinitely. If it throws F070 with no motor connected, the problem is unambiguously inside the drive.

> **Field knowledge nugget:** On PowerFlex 525 drives in food-and-beverage panels — bottling lines, dairy CIP rooms, anywhere with washdown — F070 trips often trace to humidity infiltration through the air intake. The board has a conformal coating but the heatsink fan pulls atmospheric moisture across the gate-drive ASIC area. Over time the moisture leaves an ionic residue on the PCB that creates micro-leakage paths in the gate-drive supply circuit. The drive runs fine until ambient humidity spikes (a steam clean, a hot afternoon), then throws F070. I have replaced eight 525s on a single Wisconsin dairy plant for this exact reason. Fix is an enclosure with a NEMA 12 rating minimum, vortex cooler if the ambient is hot, and a regular schedule to wipe down the panel interior. The drive's IP rating does not protect against the panel's IP rating being violated.

## Parts that may need replacement

PowerFlex 525 drives are sold as complete units — internal failure means replace the drive. PowerFlex 753/755 drives are modular and certain boards are field-replaceable.

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 525, 480V, 5HP | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault) |
| PowerFlex 525, 480V, 10HP | 25B-D017N104 | $1,800–$2,100 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault) |
| PF 755 Main Control Board | 20-750-S1 | $1,200–$1,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PF 755 24VDC Aux Power Supply | 20-750-APS | $480–$650 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PF 755 Heatsink Fan (frame 3) | 20-750-FAN3-F | $145–$220 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault) |
| 22-HIM-A3 LCD keypad | 22-HIM-A3 | $185–$240 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Vortex panel cooler (small) | EXAIR 4815 | $480–$580 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f070-fault) |

For 755 drives, swap the **Main Control Board (20-750-S1)** first if the subcode points to a control-side fault. If the subcode points to power-stage feedback (current sensor, gate driver), the power module is the part — that's not field-replaceable below frame 4. Frame 4+ power modules can be replaced as units but require Rockwell-trained service.

## When to call Rockwell or a controls engineer

Call for senior support when: F070 returns after a drive replacement (suggests an upstream power quality or grounding issue you haven't found); the 755 subcode points to power-stage hardware and the drive is under warranty (Rockwell warranty repair); multiple drives in the same panel start throwing F070 in close succession (common cause — usually grounding, panel power, or harmonics from a regenerative source); or when the F070 only happens during a specific upstream event you can't isolate from on-site evidence.

## FAQs

**Why does F070 not tell me what failed?** Because the firmware can't always know. The fault is a "diagnostic check failed" condition; the specific check that failed is in the subcode on 755 drives, but on the 525 the firmware budget didn't include surfacing that detail. Rockwell's design choice was to err on the side of "stop running, alert the operator" rather than try to differentiate failures it can't reliably diagnose.

**Can a bad EtherNet/IP card cause F070?** Indirectly, yes. If the EtherNet/IP option (20-750-ENETR on a 755) is consuming control power abnormally or generating noise on the internal communication bus, the firmware can see it as a power-stage feedback anomaly. Rare but documented. Try removing the comm card and running standalone if you suspect this.

**Will a line reactor fix recurring F070?** Only if your F070s correlate with line transients (utility sags, capacitor switching, neighboring large loads). A 5% line reactor flattens the input current waveform and protects the input diode bridge from voltage spikes. It does not fix internal drive faults — those need drive replacement.

**Drive is out of warranty. Repair or replace?** Get a quote from Rockwell or an authorized repair house, but for 525s the math almost never works — repair cost approaches new-drive cost, and the repair is often a power-stage swap that doesn't address the upstream condition that killed the original. For 753/755 in frames 3+, refurbishment can pencil out if the rest of the drive is sound.

**Is F070 ever a software issue?** Very rarely. There's been one notable firmware revision on the 525 (firmware 5.001) that produced spurious F070s on power-up; updating to 5.002 or later resolved it. Check **Parameter D001 Drive Firmware** rev and consult Rockwell knowledgebase Tech Note QA52234 for known firmware issues.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/posts/allen-bradley-powerflex-f004-fault)
- [Allen-Bradley PowerFlex F063 Fault — Phase Short Fix](/posts/allen-bradley-powerflex-f063-fault)
- [Allen-Bradley PowerFlex F091 Fault — Encoder Loss Fix](/posts/allen-bradley-powerflex-f091-fault)
