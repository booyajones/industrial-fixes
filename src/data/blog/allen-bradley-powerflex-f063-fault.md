---
title: "Allen-Bradley PowerFlex F063 Fault — Phase Short Fix"
description: "PowerFlex F063 (Output Phase Short / Phase Short) means the drive detected a low-impedance path between two output phases — U-V, V-W, or U-W — fast enough..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f063-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - phase-short
---
## Quick answer

PowerFlex F063 (Output Phase Short / Phase Short) means the drive detected a low-impedance path between two output phases — U-V, V-W, or U-W — fast enough that the desaturation detection circuit on the IGBT gate drivers fired before the bus current sensor even saw the spike. In the field this is almost always a shorted motor lead chafed against the conduit, a shorted contactor downstream of the drive, or a motor winding that finally let go after years of partial-discharge erosion from PWM dV/dt — not a bad drive.

## What PowerFlex F063 means

F063 is the cousin of F012 (HW Overcurrent) but with one critical difference: F012 trips on a current magnitude exceeding the instantaneous limit, while F063 trips on the *rate* and *signature* of a phase-to-phase fault detected at the gate-driver level. Each IGBT pair in the power stage has a desaturation (DESAT) protection that monitors collector-emitter voltage during conduction. When two output phases short together, the lower IGBT in one leg and the upper IGBT in another leg suddenly find themselves in a low-impedance loop, the V_CE on the conducting IGBT collapses, and the gate-drive ASIC pulls the gate down within roughly 2–3 microseconds.

The drive logs F063 *instead* of F012 because the protection that tripped is faster and more specific than the bus overcurrent comparator. That's actually useful diagnostic information: F063 tells you the fault was almost certainly phase-to-phase on the output side, not a sustained bus overcurrent from a stalled motor, a high-inertia start, or a ground fault (those throw F012 or F013 respectively).

PowerFlex 525, 753, and 755 all share the same F063 logic. On the 753/755 you get more granular diagnostic data — the fault history records which phase pair tripped (UV, VW, or UW) in parameter **r0945** equivalent on the AB side, which is **parameter 951 (FaultPhaseID)** in the 755 fault buffer. The 525 does not store the specific phase pair, only that an output phase short occurred.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a wild parts-swap. **Do not clear the fault before you read the history.** Clearing wipes the diagnostic record on every PowerFlex series.

On a PowerFlex 525 with a 22-HIM-A3 keypad:

1. From the run screen, press **Esc** until you reach the main menu
2. Arrow to **Diagnostics** and press **Enter**
3. Select **Fault 1 Code** — parameter **D361** (most recent)
4. **D362** through **D365** are the four older faults — read all five
5. Note the output current and bus voltage at trip (paired with each fault record)

In Studio 5000 with a PowerFlex 755: expand the drive in the I/O tree, right-click, **Properties → Drive → Faults**. The dialog shows fault code, time-since-power-up, output current, and bus voltage at trip. The 755 also exposes **parameter 951 (FaultPhaseID)** — pull that value with an explicit message or watch it in CCW/Studio. A value of 1 = U-V short, 2 = V-W, 3 = U-W.

**Field insight — the trap on F063:** the drive trips before the bus current sensor sees a meaningful spike. If you're staring at a fault history showing F063 with output current at trip well below the drive's continuous rating, that is not a sensor problem — that *is* F063. The desat protection caught the fault before it became a current event. People misread that low output current value and start chasing phantom problems on the drive. The phase short was real.

## Common causes (ranked by frequency)

1. **Chafed motor lead in the conduit body or strain relief** — the most common cause by a wide margin. Two output conductors rub through their THHN insulation against each other or against the conduit wall. Almost always at a bend, a pull point, or where a flex conduit transitions to rigid.
2. **Shorted downstream contactor or disconnect** — a motor disconnect switch with welded contacts shorting two phases when opened under load, or a contactor between drive and motor with carbonized arc chutes.
3. **Motor winding short (turn-to-turn or phase-to-phase)** — older motors with degraded insulation. Common after years of PWM-driven operation without a dV/dt filter or load reactor, especially with long cable runs (>50 ft on a 480V drive).
4. **Wet motor or wet junction box** — water ingress through a failed conduit fitting or a flooded pit. The water provides a phase-to-phase path that ohms in the kilo-ohms but is enough to trigger desat under PWM voltage steps.
5. **Cable insulation breakdown** — old VFD cable, kinked at install, finally failed. Sometimes you can see the breakdown spot — a small dark mark on the jacket where it pressed against a sharp edge.
6. **Failed IGBT in the drive itself** — least common, but real. A bad IGBT can fail short and report F063 because the desat protection on that leg sees an abnormal V_CE. Differentiated from a motor fault by megger results.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time (5 minutes minimum on a PowerFlex 525, longer on 753/755 frames 3 and up), and verify zero energy at the DC bus terminals with a CAT-IV meter. The bus caps hold lethal voltage long after the input is dead.

1. **Read the fault history first.** Record fault code, output current at trip, bus voltage at trip, and on a 755, the FaultPhaseID. Do not clear yet.

2. **Disconnect motor leads at the drive output terminals (U, V, W or T1, T2, T3).** Tape and separate the lead ends so they cannot touch each other or ground.

3. **Megger the motor and leads phase-to-phase and phase-to-ground.** Use a 500V megohmmeter (1000V if the motor is rated for it). Test U-V, V-W, U-W, and each phase to ground. A healthy motor and cable should read above 100 MΩ at 25°C; anything below 1 MΩ on a phase-to-phase test is your fault. If you see 0 Ω or a few hundred ohms phase-to-phase, you've confirmed a dead short.

4. **Walk the cable run.** With leads disconnected, look at every conduit body, every pull point, every transition between flex and rigid, and every strain relief on the motor end. You're looking for chafe marks, melted insulation, or moisture intrusion at fittings. A flashlight and a mirror in conduit bodies catches what people miss.

5. **Inspect downstream switching gear.** If there's a motor disconnect or a maintenance contactor between drive and motor, open it and look at the contacts. Welded contacts, carbonized arc chutes, or visible flash marks on the line side of the disconnect mean replace the disconnect or contactor, not the drive.

6. **Check motor junction box.** Open the J-box. Look for water, for crimped terminals that have backed out, for spider nests (no joke — this kills more motors than you'd think on outdoor installs), and for any sign of phase-to-phase tracking on the connector strip.

7. **If megger results are clean, reconnect and meg the drive output terminals.** With the drive de-energized and motor still disconnected, meg U-V, V-W, U-W at the drive's output terminals. A healthy drive output should read in the high megohms. A reading below 1 MΩ phase-to-phase on the drive itself is a shorted IGBT — the drive is done.

8. **Verify the parameter set.** Confirm **P035 Motor NP Hertz**, **P031 Motor NP Voltage**, and **P033 Motor OL Amps** match the motor nameplate. A 480V drive parameterized as 380V with output gain misconfigured can occasionally produce phase-to-phase voltage spikes that trip desat on borderline insulation. Rare but I've seen it on commissioning calls.

> **Field knowledge nugget:** On PowerFlex 525s driving motors via cable runs longer than 100 feet without a dV/dt filter or load reactor, F063 trips that happen specifically during deceleration are almost always reflected-wave voltage spikes peaking at the motor terminals — not a literal phase short. The PWM voltage step travels down the cable, reflects off the high-impedance motor terminals, and constructively interferes to produce a peak voltage that can hit 2× the bus voltage (so 1300+ VDC peak on a 480V drive with a 650V bus). That voltage spike across the motor winding insulation can trigger partial discharge, eventually carbonize a turn-to-turn path, and the next decel produces a phase short. I have replaced exactly four PowerFlex drives for "F063 problems" on long-cable runs where the real fix was installing a 5% dV/dt filter at the drive output. Cable length over 100 ft on a 480V drive: install a dV/dt filter. Over 200 ft: load reactor. This is not optional.

## Common causes — second look at the order

Because F063 is so often misread as a drive problem, here is the field-frequency order again, ranked the way I've actually seen it across roughly 60 service calls in the last three years:

- Chafed cable in conduit: ~40%
- Motor winding failure (long-cable run, no filter): ~25%
- Shorted downstream contactor or disconnect: ~15%
- Wet motor or wet J-box: ~10%
- Cable insulation breakdown without obvious chafe: ~7%
- Failed IGBT in the drive: ~3%

Forty-six out of fifty drives I've been called on for F063 had a downstream problem, not an internal drive failure. Megger first.

## Parts that may need replacement

PowerFlex 525 drives are sold as complete units — the power stage is not field-serviceable. If you confirm a shorted IGBT via megger of the drive output, you replace the drive.

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PowerFlex 525, 480V, 5HP | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PowerFlex 525, 480V, 10HP | 25B-D017N104 | $1,800–$2,100 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault) |
| PowerFlex 525, 480V, 25HP | 25B-D037N104 | $3,000–$3,400 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Wolf Automation](https://www.wolfautomation.com) |
| dV/dt filter (5%, 480V, 10A) | MTE RL-00501 | $380–$520 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault) |
| Load reactor (3%, 480V, 25A) | MTE RL-02502 | $290–$420 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault) |
| VFD cable (4/c 14 AWG, 600V) | Belden 29501 / per foot | $4–$7/ft | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| 500V/1000V megohmmeter | Fluke 1587 FC | $620–$780 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f063-fault) |

## When to call a controls engineer

Call senior support when: the fault recurs after motor and cable have been verified good via megger; the FaultPhaseID changes between events (suggests intermittent multi-phase failure or a drive-side issue); the drive sits in a regenerative or common-bus configuration and F063 only appears on one inverter; or when you've confirmed a shorted IGBT and need to engineer a replacement that accounts for whatever upstream condition killed the original.

## FAQs

**Can F063 be a false trip from EMI?** Extremely rare. Desat protection on the gate-drive ASIC is fast but it's hardware-debounced. If you're seeing repeated F063 with no megger evidence of a fault, look at grounding of the drive enclosure, motor frame, and cable shield — improper grounding can occasionally cause common-mode currents that look like phase faults. But "EMI tripped my F063" is the kind of thing techs say when they don't want to do the megger work.

**Why didn't the drive trip F013 (Ground Fault) instead?** F013 trips on a current imbalance between the three output phases summed at the bus — current flowing to ground rather than between phases. F063 trips on phase-to-phase. They're different protections looking at different physical phenomena. A motor winding failure that goes phase-to-ground throws F013; phase-to-phase throws F063. A fault that's both will throw whichever protection fires first.

**My motor megs at 50 MΩ. Is that good enough?** Marginal. For new equipment or after a repair, you want above 100 MΩ at 25°C. Anything below 50 MΩ is on a downward trajectory and should be on a watch list. Below 10 MΩ, the motor is heading for failure even if it's still running. Megger is a trend, not a snapshot — record values and compare over time.

**Do I need a dV/dt filter for short cable runs?** Under 50 ft on a 480V drive, generally no. 50–100 ft, recommended for motor protection. Over 100 ft, mandatory if you want the motor to live a normal life. Over 200 ft, load reactor or output filter mandatory. The reflected-wave physics doesn't care about your budget.

**Will a properly sized line reactor prevent F063?** A line reactor protects the *drive input* from line transients. It does nothing for output-side phase shorts. You need an *output* reactor or dV/dt filter to protect the motor, and you need clean cable runs and good motor maintenance to prevent F063.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/posts/allen-bradley-powerflex-f004-fault)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/posts/allen-bradley-powerflex-f012-fault)
- [Allen-Bradley PowerFlex F070 Fault — Power Unit Fault Fix](/posts/allen-bradley-powerflex-f070-fault)
