---
title: "SEW-Eurodrive Fault F01 (Overcurrent): Causes, Sub-Codes, and How to Isolate Drive vs Motor vs Cable"
description: "SEW-Eurodrive F01 is an output-stage overcurrent trip on MOVIDRIVE B and MOVITRAC B. Decode sub-error codes 0–14, apply the P138 ramp-limit fix, and use one lockout-and-meter session to prove whether the drive, the motor, or the cable is at fault."
author: "Error Code Fixes Editorial Team"
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
slug: sew-eurodrive-fault-f01-overcurrent
featured: false
draft: true
tags:
  - vfd
  - sew-eurodrive
most_likely_cause: "Short circuit in the motor cable or motor at the inverter output"
money_part: "Insulation resistance tester (megohmmeter)"
free_checks:
  - "Read the sub-error code from the drive's fault memory before touching anything — it tells you whether this is a wiring problem, a parameter problem, or an internal hardware problem"
  - "Check whether the P138 ramp limit is deactivated and the ramp time is set very short (the sub-code 5 signature) — that fix costs nothing but a parameter change"
  - "After lockout and full DC bus discharge, disconnect the motor cable at the drive's output terminals and see whether F01 still trips on enable — if it does, the fault is inside the drive, not in the motor or cable"
---

## What this code means

SEW-Eurodrive fault F01 is **overcurrent in the output stage**. The drive's response is immediate disconnection: the output transistors switch off at once and the drive latches the fault, because the current it measured leaving the output stage exceeded what the hardware can survive. F01 appears across the SEW inverter families — it is listed in the official error tables for both MOVIDRIVE MDX60B/61B and MOVITRAC B.

Per SEW's own error list, F01 has four documented causes:

1. **Short circuit at the inverter output** — in the motor cable, the terminations, or the motor windings.
2. **Motor too large for the inverter** — the connected motor exceeds what the drive is rated to feed.
3. **Defective output stage** — the drive's own power transistors have failed.
4. **Ramp limit deactivated with too short a ramp time** — the drive gets stuck in its hardware current limit trying to follow an impossible ramp (this is sub-error code 5 on MOVIDRIVE B, and it has a pure parameter fix: activate P138 and/or lengthen the ramp).

Three of those four live outside the parameter set, which is why F01 is fundamentally a *meter* fault, not a *keypad* fault. The job is to prove which of three physical zones failed — drive, motor, or cable — before you spend money on any of them. The good news: one lockout and one test-instrument session settles it.

## Common Causes

- **Short circuit at the output** — By far the most common field cause. Chafed or crushed motor cable, water or conductive dust in a junction box or the motor terminal box, a failed cable termination, or shorted motor windings. The drive sees a near-zero-impedance load and trips instantly, often the moment you enable.
- **Motor too large for the inverter** — After a motor swap or a "temporary" substitution, the connected motor draws more than the drive can source. SEW's documented fix is blunt: connect a smaller motor (or fit a correctly sized drive).
- **Ramp limit off + ramp too short (sub-code 5)** — With the P138 ramp limit deactivated and an aggressive ramp time, the drive slams into its hardware current limit and cannot get out — SEW describes the unit as stuck ("hangs") in the hardware current limit. Nothing is broken; the configuration is asking for current the hardware will not deliver.
- **Defective output stage** — A failed power transistor inside the drive. The tell: F01 trips even with the motor cable completely disconnected from the output terminals. This is an SEW Service repair, not a field fix.
- **Phase-module signal-line interruption (sub-codes 6–14, MOVIDRIVE B)** — Internal monitoring of the individual phase modules detected a problem on phase U, V, W, or a combination. Also hardware, also SEW Service territory.

## MOVIDRIVE B F01 sub-error codes

On MOVIDRIVE B, the fault memory stores a sub-error code alongside F01, and it is the single fastest triage input you have. Read it from the keypad fault memory or MOVITOOLS MotionStudio **before** you start pulling cables. The documented sub-error codes for F01 are 0, 1, and 5–14:

| Sub-code | What the drive detected | Where to look first |
| --- | --- | --- |
| 0, 1 | Overcurrent in the output stage — the general detection, with no more specific hardware pointer | Work the full drive/motor/cable isolation procedure below |
| 5 | Unit stuck in the hardware current limit: ramp limit deactivated and ramp time too short | Parameters, not hardware — activate the P138 ramp limit and/or increase the ramp time |
| 6, 7, 8 | Phase-module VCE/undervoltage monitoring on phase U, V, W respectively | Drive-internal phase module hardware — contact SEW Service |
| 9–14 | Signal-line interruption to the phase modules, in combinations of phases U/V/W | Drive-internal signal wiring/modules — contact SEW Service |

The split matters: sub-code 5 is a free parameter fix, sub-codes 6–14 are internal hardware you cannot repair in the field, and sub-codes 0/1 are the ones where your meter earns its keep. On MOVITRAC B the fault list carries the same F01 overcurrent definition and causes; work it with the same isolation procedure.

## Step-by-Step Fix: Isolate Drive vs Motor vs Cable {#fix}

**Safety first, and this is not boilerplate:** everything below the parameter checks involves opening high-voltage power connections. A VFD's DC bus capacitors hold a lethal charge after power is removed. Lock out and tag out the supply, wait the full discharge time stated on the drive or in the manual, and verify zero volts with a meter rated for the work before touching any power terminal. Insulation-resistance (megger) testing and DC bus measurements are work for a qualified/licensed electrician. If that is not you, stop at step 2 and call one.

1. **Read the fault memory and sub-code.** Note the sub-error code (MOVIDRIVE B) and the operating state at the moment of the trip: at enable, during acceleration, at constant speed. F01 at the instant of enable smells like a hard short or a dead output stage; F01 during hard acceleration with sub-code 5 smells like the ramp-limit configuration.

2. **Check the sizing and the parameters — the free fixes.** Confirm the motor nameplate current against the drive's rating; if the motor is too large for the inverter, no amount of cable testing will fix F01 — SEW's documented remedy is to connect a smaller motor. If the sub-code is 5, activate the P138 ramp limit and/or lengthen the ramp time, reset, and test. If either of these closes the case, you are done without opening a terminal.

3. **Lock out, discharge, verify dead.** Then open the drive's output terminals and disconnect the motor cable at the drive end. Inspect while you are in there: carbon tracking, discolored or melted insulation, loose strands bridging terminals, and moisture are all findings, not coincidences.

4. **Test the cable and motor together, then separately.** With the cable disconnected from the drive (never insulation-test into the drive — the test voltage destroys output-stage semiconductors), insulation-test each conductor to ground and conductor-to-conductor. A low reading tells you the fault is downstream of the drive. Now split the system: disconnect the cable at the motor terminal box and test the cable alone, then the motor alone. This is exactly the "megger motor and cable separately" discipline SEW's error list prescribes for ground faults, and it is the step that stops you from replacing a good motor because of a bad cable (or vice versa).

5. **Check winding balance.** With the motor isolated, measure phase-to-phase winding resistance (U–V, V–W, W–U) with a low-resistance meter. The three readings should closely match. One leg significantly low suggests shorted turns — a motor rewind or replacement, not a drive problem.

6. **Prove or clear the drive.** If cable and motor test clean, reconnect nothing yet: if F01 trips with the motor cable still disconnected from the output, the output stage itself is the prime suspect. SEW's remedy for a defective output stage is to contact SEW Service — the output stage is not a user-replaceable part on these units.

7. **Rectify, reconnect, and test under the real duty cycle.** Repair or replace whatever failed, torque the terminations, reset the fault, and run a full accelerate/run/decelerate cycle at working load. An F01 that only returns under load points back at marginal insulation or an undersized drive-motor pairing.

## Rule out F03 and F04 in the same meter session

Two neighboring SEW faults share hardware and symptoms with F01, and the meter session above already gathers the evidence for both — so check them while everything is disconnected:

| Code | Meaning (per SEW error list) | Why it belongs in this session |
| --- | --- | --- |
| F03 | Ground fault — immediate disconnection. Documented locations: in the motor lead, in the inverter, or in the motor. On MOVITRAC B, the F03 entry also covers overcurrent conditions as in F01. | Your insulation test to ground in step 4 is the F03 diagnostic. A phase-to-ground insulation failure trips F03; a phase-to-phase failure tends toward F01. Same cable, same megger, same disconnect points. If the ground fault is internal to the drive, that unit needs service — do not keep resetting into it. |
| F04 | Brake chopper fault — immediate disconnection. Documented causes: too much regenerative power, braking resistor circuit interrupted, short circuit in the braking resistor circuit, brake resistance value too high, defective brake chopper; on MOVITRAC B, also ground fault. | The braking resistor circuit is the other high-current power wiring on the drive. While locked out, check the supply cable to the braking resistor for interruption or shorts and verify the resistor's value against SEW's specified technical data — a resistance value that is too high is itself a documented F04 cause. If regenerative energy is the issue, extend the deceleration ramps. A defective internal brake chopper means replacing the drive. |

If you are seeing F01 on some trips and F03 or F04 on others, do not treat them as separate mysteries — they are usually one physical problem (failing insulation, a damaged power circuit) being caught by different monitors depending on the moment of failure.

## Parts Often Needed

| Part | Notes |
| --- | --- |
| Insulation resistance tester (megohmmeter) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sew-eurodrive-fault-f01-overcurrent&k=Insulation+resistance+tester+megohmmeter&tag=errorcodefixes-20) \| The one instrument that separates motor from cable — always disconnect the drive before testing |
| Shielded VFD motor cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sew-eurodrive-fault-f01-overcurrent&k=Shielded+VFD+motor+cable&tag=errorcodefixes-20) \| Replace, don't splice, a cable that fails insulation testing |
| Clamp meter (true-RMS) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-sew-eurodrive-fault-f01-overcurrent&k=True+RMS+clamp+meter&tag=errorcodefixes-20) \| Verify actual motor current against the nameplate after the repair |

## When to Call a Pro

Draw the line at the power terminals. Reading the fault memory, checking P138 and ramp times, and comparing nameplate data are safe for any competent operator. Lockout/tagout, DC bus verification, insulation-resistance testing, and any work inside terminal boxes are for a qualified/licensed electrician — the voltages involved are lethal and megger test voltages will destroy a connected drive.

Call SEW Service (or an SEW-authorized repair shop) when the evidence points inside the unit: F01 with the motor cable disconnected, sub-error codes 6–14 on MOVIDRIVE B, a ground fault that persists with motor and cable removed, or a dead brake chopper. The output stage and phase modules are not field-repairable, and repeatedly resetting a drive into a hard short only converts a repairable fault into a scrapped unit.

## Frequently asked questions

### Can I just reset F01 and keep running?

No. F01 is an immediate-disconnection fault protecting the output transistors. If the cause is a short circuit and you keep resetting into it, each restart hammers the output stage with fault current and can turn a cable repair into a drive replacement. Reset once to observe behavior if you must, then diagnose.

### What does F01 sub-error code 5 mean on a MOVIDRIVE B?

Sub-code 5 means the unit is stuck in its hardware current limit because the ramp limit function is deactivated while the ramp time is set too short. It is the one F01 variant with a pure parameter fix: activate the P138 ramp limit and/or increase the ramp time. No wiring work required.

### How do I know whether the drive's output stage caused F01?

Eliminate everything downstream first. With the system locked out and the DC bus verified discharged, disconnect the motor cable at the drive's output terminals. If cable and motor pass insulation and winding-resistance tests but F01 still occurs with the output disconnected, the output stage is the remaining suspect — and per SEW's error list, a defective output stage means contacting SEW Service.

### What is the difference between F01 and F03 on these drives?

Both are immediate-disconnection faults on the output power path. F01 is overcurrent in the output stage — classically a phase-to-phase short, an oversized motor, or the output stage itself. F03 is a ground fault — current leaking to earth from the motor lead, the motor, or inside the inverter. The MOVITRAC B fault list notes F03 can also cover overcurrent conditions like F01, which is why the same disconnect-and-megger session should always test both to ground and phase-to-phase.

### Which SEW drives use this F01 definition?

The error tables cited below are from the official operating instructions for MOVIDRIVE MDX60B/61B and MOVITRAC B. Other SEW families use similar F-numbering, but always confirm against the manual for your specific unit before acting on a code.

## Sources

- *Compact Operating Instructions — MOVIDRIVE MDX60B/61B* (SEW-Eurodrive doc 16920813), Section 6.2.3 Error list: [archived official PDF](https://web.archive.org/web/20130124101658/http://download.sew-eurodrive.com/download/pdf/16920813.pdf)
- *MOVITRAC B Operating Instructions, 2009-05* (SEW-Eurodrive doc 16810813), Section 7.2 List of faults: [archived official PDF](https://web.archive.org/web/20210805131920/https://download.sew-eurodrive.com/download/pdf/16810813.pdf)
- *Operating Instructions — MOVIDRIVE MDX60B/61B Inverter* (SEW-Eurodrive doc 11696613), manufacturer's canonical source: [download.sew-eurodrive.com](https://download.sew-eurodrive.com/download/pdf/11696613.pdf) (SEW's download portal was serving a maintenance page at the time of writing; content verified via the archived official PDFs above)
