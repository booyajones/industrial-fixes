---
title: "Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix"
description: "PowerFlex F004 (Undervoltage) means the DC bus dropped below the drive's minimum threshold while running — about 310 VDC on a 480V-class PowerFlex 525,..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f004-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - undervoltage
---
## Quick answer

PowerFlex F004 (Undervoltage) means the DC bus dropped below the drive's minimum threshold while running — about 310 VDC on a 480V-class PowerFlex 525, roughly 200 VDC on a 240V-class. The single most common cause I see in the field is a sagging branch circuit during inrush of a nearby load (another VFD soft-starting, a large air compressor kicking on, a welder striking), not a problem with the drive itself.

## What PowerFlex F004 means

The drive doesn't measure line voltage directly to declare undervoltage — it measures the DC bus after the diode bridge and bus capacitors. On a PowerFlex 525, the bus normally floats around 650–680 VDC when fed from a healthy 480V three-phase supply (line × 1.414, minus diode drop, minus loaded sag). The drive trips F004 when bus voltage drops below the undervoltage threshold for more than roughly 0.5 seconds while the drive is in a Run state. Below that, the drive cannot guarantee enough gate-drive headroom or clean PWM output, and the IGBTs would commutate into a saturated state — exactly the condition that smokes them.

Three things make F004 confusing: first, the trip happens after the bus has already recovered, so by the time you walk to the drive your fluke shows nominal line voltage. Second, the drive doesn't tell you which phase sagged unless you read the right diagnostic parameter. Third, F004 can be triggered by a problem on the line side (utility, branch fuse, contactor), the drive side (bus capacitor aging, pre-charge resistor open, SCR/diode failure on 750-class), or the load side (massive load step that pulls the bus down faster than the line can backfill it).

The PowerFlex 4-class drives use the same logic but with a coarser threshold and no granular fault history. The 750-class (753, 755) adds three extra diagnostic words including peak inverse bus voltage and pre-charge state at trip — use those when you have them.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a 2-hour parts-swap fishing trip. **Do not clear the fault before you read the history.** Clearing wipes the diagnostic record on every PowerFlex series.

On a PowerFlex 525 with a 22-HIM-A3 or A6 keypad:

1. From the run screen, press **Esc** until you reach the main menu
2. Arrow to **Diagnostics** and press **Enter**
3. Select **Fault 1 Code** — this is parameter **D361**, the most recent fault
4. **D362** is the second-most-recent, **D363** the third, **D364** fourth, **D365** fifth (oldest of the five)
5. Each of those fault-code parameters has its own paired bus-voltage and status-word parameters stored in adjacent slots — so D361's trip has its own bus-voltage-at-trip record, D362's trip has its own, and so on. On the 525 you read bus volts at trip via parameter **B005 Last Stop Source** combined with the fault log; on the 750-class the fault history exposes them directly.

In Studio 5000 with a PowerFlex 755 on EtherNet/IP, expand the drive in the I/O tree, right-click, **Properties → Drive → Faults**. CCW (Connected Components Workbench) for the 525: connect via USB, go to **Drive → Faults & Alarms**. The dialog shows fault code, time since power-up, and bus voltage at the moment of trip.

**Field insight — the one thing that traps everyone on F004:** the trip happens *after* the line voltage has already recovered. The drive logs the fault based on a 250–400 millisecond dip you will never see on a handheld DMM, even in Min/Max mode (most fluke 87Vs sample at 100ms). If the fault history shows F004 with a bus voltage at trip below 310 VDC but your standing measurement at the input terminals shows nominal 480, you are chasing a transient — put a power quality recorder (Fluke 1748 or Dranetz HDPQ) on the branch for 24 hours and look for sags coincident with the trip.

## Common causes (ranked by frequency)

1. **Line voltage sag from a coincident load** — another VFD on the same branch starting at full load, a large motor across-the-line start, welder duty cycle, utility sag from a fault clearing somewhere upstream
2. **Loose terminal on the drive input** — L1, L2, or L3 lug not torqued to spec (the 525 frame-B spec is 1.5 Nm / 13 in-lb). A loose connection makes a high-impedance phase that drops voltage under load
3. **Blown branch fuse or open contactor pole** — drive runs on two phases for a few cycles before the bus sags far enough to trip; you'll see a much lower bus voltage in the history than a sag would produce
4. **Pre-charge resistor open or pre-charge relay welded** — drive starts on the pre-charge path and never transitions to the main bus, so as soon as load increases the bus collapses
5. **Aged bus capacitors** — drives older than 7–10 years in high-ambient cabinets (above 40°C) lose capacitance, can't ride through a normal sag they handled when new
6. **Undersized branch circuit** — the wire run is technically code-compliant but the voltage drop at full motor current pulls the drive into trip range during acceleration

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time (5 minutes minimum on a PowerFlex 525, longer on 753/755 frames 3 and up), and verify zero energy at the DC bus terminals (DC+ and DC-) with a CAT-IV meter. The bus caps hold lethal voltage long after the input is dead. Stay outside the NFPA 70E arc-flash boundary marked on the cabinet label until you've confirmed de-energization.

1. **Pull the fault history before clearing.** Read D361 through D365 on a PowerFlex 525, or the Faults tab in Studio 5000 / CCW. Write down the fault code, the bus voltage at trip, and any precedent alarms. A trip from 310 VDC tells a different story than a trip from 180 VDC.

2. **Check input voltage at the drive terminals — both standing and during the next start cycle.** Use a true-RMS meter on L1-L2, L2-L3, L3-L1. Standing voltage should be within ±10% of nameplate (432–528 VAC for a 480V drive per parameter P031 Motor NP Voltage class). Imbalance between phases over 3% will eventually cause F004 even if the average looks fine.

3. **Hunt the loose connection.** Power off, verify dead, then check torque on every input lug (L1/L2/L3), output lug (U/V/W or T1/T2/T3), and ground. Use a calibrated torque screwdriver — Allen-Bradley publishes the spec on the back of the drive cover. A discolored lug or melted insulation around a terminal is a smoking gun.

4. **Verify the branch fuses and upstream disconnect.** A single-phased input is the classic F004 producer. Pull each fuse and check continuity. Replace as a matched set (same I²t rating, same brand) — don't mix Bussmann FRS-R with Mersen AJT.

5. **Compare the fault to operating conditions.** Was the drive accelerating a high-inertia load? Was a second piece of equipment starting at the same time? Walk the panel and the surrounding equipment. The fault timestamp from Studio 5000 or CCW lined up against a process trend almost always reveals the coincident event.

6. **Megger the motor and motor leads — but only if you suspect load-side trouble pulled the bus down.** Disconnect U/V/W from the drive output terminals. Use a 500V megohmmeter motor lead to ground. Anything below 1 megohm at 25°C is a problem; below 100 kΩ and you have a ground fault that will drag the bus down on every start.

7. **Set up a power quality monitor** if standing measurements and connections check out. A Fluke 1748 or 1735 on the drive input for 24–72 hours will capture the sag that's tripping you. Trigger threshold: 10% below nominal for 100ms or more.

8. **Check pre-charge on older drives.** On a PowerFlex 525 over 5 years old, listen for the pre-charge relay click on power-up and watch bus voltage ramp on a meter. If the bus ramps slowly and stays low (under 600 VDC on 480V class), the pre-charge resistor is open or the bypass relay has a stuck contact — replace the drive, this is not field-repairable.

9. **Verify parameter P031 Motor NP Voltage matches the supply class.** A 480V-class drive parameterized for 380V will trip F004 at startup every time. This sounds dumb. I've seen it on three commissioning calls in the last year.

## Parts that may need replacement

PowerFlex 525 drives are sold as complete units — Allen-Bradley does not sell power stages, bus capacitors, or pre-charge boards as separate field parts. If the fault history shows F004 with a bus voltage at trip below 200 VDC on a 480V-class drive *and* your input voltage is verified good *and* there's no loose connection, you are replacing the drive.

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 525, 480V, 5HP | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PowerFlex 525, 480V, 10HP | 25B-D017N104 | $1,800–$2,100 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault) |
| PowerFlex 525, 480V, 20HP | 25B-D030N104 | $2,600–$3,100 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Wolf Automation](https://www.wolfautomation.com) |
| 22-HIM-A3 LCD keypad | 22-HIM-A3 | $185–$240 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Bussmann FRS-R-30 input fuse (480V) | FRS-R-30 | $14–$22 each | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Phoenix Contact terminal torque screwdriver | 1212597 | $190–$240 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault) |
| Fluke 1748 power quality logger | FLUKE-1748/BASIC | $7,400–$8,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f004-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

For 753/755 drives the same rule applies for the power module, but the **control board (20-750-S1)**, **EtherNet/IP option (20-750-ENETR)**, and **24VDC aux power supply (20-750-APS)** are user-replaceable.

## When to call a controls engineer

Call for senior support when: the fault history shows multiple F004 events with bus voltages spread across a wide range (suggests a power quality problem outside the panel); a power quality monitor logged transients but the utility denies anything upstream; you have a 750-class drive on a regenerative bus tie or common-bus configuration and the undervoltage is appearing on only one inverter; or when the F004 happens only on cold mornings (capacitor temperature dependency, drive is at end of life).

## FAQs

**Can I just clear F004 and keep running?** You can, and the drive will let you, but you've now lost the bus voltage at trip and the precedent fault data. If it trips again, you're starting from zero. Always pull D361–D365 first.

**Will an undersized transformer cause F004?** Yes, especially during acceleration of a high-inertia load. The transformer's source impedance combined with motor inrush can sag the bus enough to trip. Check kVA capacity: a 480V VFD pulls roughly 1.25× the motor HP in input kVA at full load.

**My drive trips F004 only during a thunderstorm. Why?** Utility sags caused by lightning faults clearing on the distribution feeder. The sag is typically 100–200 milliseconds — long enough to trip F004, short enough that your lights don't even flicker. Install a line reactor (5% impedance) and consider parameter A436 (Bus Reg Mode) set to Enable.

**Difference between F004 and F003 (Power Loss)?** F003 means the drive lost input power entirely (all three phases gone, or bus collapsed completely). F004 means the bus dropped below threshold but power was still present. F003 is a harder fault and usually means a contactor opened or fuses blew.

**Should I add a UPS in front of the VFD?** Almost never. The drive's bus capacitors *are* a small UPS. What you actually need is either a line reactor for impedance, an isolation transformer for clean power, or a true online double-conversion UPS sized for the full VFD load (which is huge). Most plants solve this with a 5% line reactor for a few hundred dollars.

## Related guides

- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
- [Allen-Bradley PowerFlex F007 Fault — Motor Overload Fix](/allen-bradley-powerflex-f007-fault/)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/allen-bradley-powerflex-f012-fault/)
- [Allen-Bradley PowerFlex F029 Fault — Analog Loss Fix](/allen-bradley-powerflex-f029-fault/)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/allen-bradley-powerflex-f081-fault/)
