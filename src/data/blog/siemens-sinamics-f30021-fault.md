---
title: "Siemens SINAMICS G120 F30021 Fault — Ground Fault Fix"
description: "SINAMICS G120 F30021 (Ground Fault) means the Power Module's output current sensors saw an imbalance — current flowing out the U, V, W phases summed to a..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: siemens-sinamics-f30021-fault
featured: false
draft: false
tags:
  - siemens
  - vfd
  - industrial-maintenance
  - drives
  - ground-fault
---
## Quick answer

SINAMICS G120 F30021 (Ground Fault) means the Power Module's output current sensors saw an imbalance — current flowing out the U, V, W phases summed to a non-zero value, which means current is escaping the motor circuit and returning through ground. In the field this is almost always a wet motor, a chafed motor lead grounding against the conduit, or a degraded motor winding insulation finally giving way to ground. The drive itself is a very distant cause.

## What F30021 means

In a healthy three-phase motor circuit, the instantaneous currents in U, V, W sum to approximately zero — what flows out one phase must return through the other two. The G120 Power Module measures each phase current independently via Hall-effect transducers and computes the residual sum. If the residual exceeds a threshold (typically 50% of motor rated current for a debounce period of 5–20 ms), F30021 fires. The drive trips to protect itself from sustained ground-current flow that would eventually damage the IGBT bridge and to protect personnel from the ground-fault condition.

The threshold and debounce window vary by Power Module size — larger Power Modules have higher absolute thresholds because their normal phase current is larger. The firmware sets this dynamically based on Power Module identification and motor parameters.

F30021 is independent of upstream ground-fault protection (GFCIs, differential breakers). The drive's internal detection sees ground faults on the *output* side that upstream protection cannot see because the drive's output is isolated from line ground by the rectifier and DC bus. This is the only ground-fault protection the motor circuit has.

A key subtlety: PWM-driven motors have inherent capacitive common-mode currents to ground (especially with long cable runs and no output filter). The firmware filters this out and trips only on resistive ground faults — current flowing through an actual leakage path, not the capacitive coupling. But on systems with very long cable runs and no dV/dt filter, the capacitive component can grow large enough that the firmware confuses it with a resistive fault.

## Read the fault history first

This is the step that separates a 20-minute diagnosis from chasing parts. **Do not clear the fault before you read the history.**

Open STARTER or TIA Portal with Startdrive. Connect via PROFINET or USB. Drive object → Diagnostics → Faults and alarms.

Capture:

- **r0945** F30021 entries
- **r0948** timestamps
- **r0949** — supplemental fault value indicating estimated ground-fault current magnitude at trip
- **r0021 Smoothed output current** — current motor current value
- **r2122** — alarm history; A30032 (output ground fault warning) often precedes F30021

**Field insight on F30021:** the r0949 value tells you how aggressive the ground fault was. A small r0949 (just above the trip threshold) suggests a marginal fault — wet insulation, partially degraded winding, capacitive coupling at the edge. A large r0949 (multiple times the threshold) suggests a dead short to ground — burned winding, cable cut through to conduit. Different magnitudes drive different urgency: marginal faults you might try to dry out; dead shorts mean the motor or cable is done.

## Common causes (ranked by frequency)

1. **Wet motor** — water ingress through a failed conduit fitting, flooded pit, washdown without proper IP rating. The water creates a phase-to-ground path. Often dryable on a salvageable motor.
2. **Cable insulation breakdown to ground** — motor lead chafed against conduit wall over time, cable jacket cut during install and not repaired, abrasion at a strain relief.
3. **Motor winding insulation failure** — aged motor where varnish has degraded enough that a turn shorts to the iron stator. Usually irreversible.
4. **Excessive cable length without dV/dt filter** — capacitive common-mode current grows with cable length; long runs (>100 m) without filtering can produce capacitive current that the firmware misinterprets as ground fault.
5. **Failed motor surge suppressor or capacitive snubber** — some applications use surge protectors at the motor; when they fail short to ground, F30021 fires.
6. **Drive output sensor failure** — least common, but real. A failed current sensor in the Power Module can fake a ground-fault signature.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait 5 minutes minimum for DC link discharge, verify zero voltage at DC link terminals with a CAT-IV meter.

1. **Read r0945, r0949, r2122 before clearing.** Note the magnitude of r0949 and whether A30032 warnings preceded the trip.

2. **Disconnect motor leads at the Power Module output.** U2, V2, W2 terminals. Tape and separate the lead ends.

3. **Megger the motor and cable phase-to-ground.** Use a 500V megohmmeter (1000V if motor is rated for it). Test each phase to ground (cable+motor combined). Healthy: above 100 MΩ at 25°C. Below 10 MΩ = marginal, on the watch list. Below 1 MΩ = your fault. Test all three phases — sometimes only one phase is compromised.

4. **Separate motor from cable.** If megger shows fault on the combined run, disconnect the motor leads at the motor J-box and re-megger cable only and motor only. This isolates whether the fault is in the cable run or in the motor.

5. **Inspect motor J-box.** Open the J-box and look for: water (a common find), spider/insect nests with hygroscopic debris, corroded terminal lugs, signs of carbon tracking on the terminal block, evidence of arcing at the lugs. Clean and inspect; sometimes a J-box dryout restores the motor to spec.

6. **Walk the cable run.** Conduit bodies, strain reliefs, transitions from flex to rigid, any pulled point. Look for crushed cable, abrasion marks, or sections that have moved against sharp edges. Replace damaged cable rather than tape it.

7. **Verify with motor connected and load disconnected.** If the motor is direct-coupled to a pump or fan that could itself be wet or compromised (motor-driven pump submerged in liquid, for example), uncouple the load and megger again. Sometimes the "motor" fault is actually a coupled pump issue.

8. **Check for excessive cable length.** Measure the actual cable run from drive to motor. On a G120 driving 400V motors, runs over 100 m without a dV/dt filter risk capacitive-current false ground-fault trips. Install a Siemens dV/dt filter (6SL3000-2DE38-4AA0 family) if your run exceeds the manufacturer's limit.

9. **Dry the motor if megger shows marginal (5–20 MΩ) results.** Lock the rotor mechanically, apply low DC voltage (typically 10–20% of nameplate) to two phases to circulate enough current to generate gentle heat in the winding. Run for 12–24 hours, then re-megger. Many wet motors recover. A motor that won't dry above 50 MΩ is finished.

> **Field knowledge nugget:** On Siemens G120 drives controlling sewer lift station pumps and similar submersible-motor applications, F30021 trips during the spring after winter are extremely common and almost never a drive problem. Submersible cables have a slow water-migration mode — over years, water wicks up the cable jacket from the submerged end, fills voids around the conductors, and eventually creates a phase-to-ground leakage path inside the cable jacket. The motor megger fine but the cable doesn't. I have diagnosed this exact failure at six different wastewater plants — replace the submersible cable from drive to motor, megger the motor separately to confirm it's good, and the F30021 goes away. Don't replace the pump motor first; replace the cable first. Submersible cable is cheaper than pump motors and far easier to swap.

## Parts that may need replacement

| Part | Order Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PM240-2 Power Module, 7.5kW, 400V | 6SL3210-1PE22-8UL0 | $1,200–$1,600 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault) |
| PM240-2 Power Module, 15kW, 400V | 6SL3210-1PE24-5UL0 | $1,900–$2,400 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault), [Wolf Automation](https://www.wolfautomation.com) |
| Siemens dV/dt filter | 6SL3000-2DE38-4AA0 | $1,400–$1,900 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault), [Wolf Automation](https://www.wolfautomation.com) |
| VFD-rated submersible cable (per ft) | Belden 9D050810 or equiv | $7–$12/ft | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault), [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Output choke (motor reactor), 18A | 6SL3203-0CD22-2AA0 | $290–$420 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault) |
| 500V/1000V megohmmeter | Fluke 1587 FC | $620–$780 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault) |
| Motor dryout heater controller | (varies) | $180–$320 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=siemens-sinamics-f30021-fault) |

Note: Siemens does not sell replacement Hall-effect current sensors for G120 Power Modules as field-replaceable parts. Power Modules are sold as complete units.

## When to call a Siemens engineer or motor shop

Call senior support when: the motor megs out below 1 MΩ phase-to-ground and the motor is critical (process-critical, high-value, or in a hazardous-area location requiring re-certification); cable testing shows fault between drive panel and motor and the run is in conduit that requires permit work; or when F30021 recurs after motor and cable have both been verified above 100 MΩ — that points to a Power Module sensor failure or a configuration issue you can't isolate on-site.

Call a qualified motor shop for: any motor that needs winding repair (carbon tracking, partial winding burn, requested rewind); evaluation of whether a marginal motor (10–50 MΩ) is worth drying or should be replaced; or motors in hazardous-area service that lose their explosion-proof certification when repaired by non-certified shops.

## FAQs

**Why does F30021 sometimes happen only on a rainy day?** Humidity infiltration. A motor or J-box with a marginal seal absorbs moisture from humid air, drops its insulation resistance for a few hours, and trips F30021 during a high-humidity event. Clear sky returns and the moisture evaporates — by the time you get there to investigate, the megger reads fine. This is a real fault and a sign the motor sealing has degraded. Address before it becomes permanent.

**Can a dV/dt filter prevent F30021?** Only F30021 caused by capacitive common-mode current on long cable runs. It does nothing for actual resistive ground faults. The cable still gets damaged, the motor still gets wet — those are still your problems. The filter just prevents the false-trip mode.

**My motor megs at 12 MΩ. Run it or replace it?** Run it, but put it on a watch list. Re-megger monthly. If it drops below 5 MΩ, schedule replacement. If it holds above 10 MΩ for 6 months, you may be fine — some motors live indefinitely at marginal megger values. But never let an installation run below 1 MΩ; the F30021 will become continuous and the motor will eventually fail to ground catastrophically.

**Difference between F30021 and F07803 (Earth fault)?** F30021 is the Power Module-side ground-fault detection on G120 standard drives. F07803 (when present) is a Control Unit-side fault used on Active Line Module configurations and S120 platforms. Different code, similar protection, different drive class.

**Can a frequency-dependent ground fault exist?** Yes — capacitive common-mode coupling is frequency-dependent. A motor that megs fine at DC (megger test) can still couple substantial current to ground at high PWM switching frequencies. This is why long cable runs need filtering; the megger doesn't tell you the whole story for VFD-driven motors.

## Related guides

- [Siemens SINAMICS F30001 Fault — Power Module Overcurrent Fix](/posts/siemens-sinamics-f30001-fault)
- [Siemens SINAMICS F30002 Fault — DC Link Overvoltage Fix](/posts/siemens-sinamics-f30002-fault)
- [Siemens SINAMICS F30011 Fault — Phase Loss Fix](/posts/siemens-sinamics-f30011-fault)
