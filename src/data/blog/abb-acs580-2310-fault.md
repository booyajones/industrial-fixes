---
title: "ABB ACS580 Fault 2310 — Overcurrent Fix"
description: "ABB ACS580 fault 2310 (Overcurrent) means the drive's output current exceeded the internal hardware overcurrent trip point — typically about 3.5× the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: abb-acs580-2310-fault
featured: false
draft: false
tags:
  - abb
  - vfd
  - industrial-maintenance
  - drives
  - overcurrent
---
## Quick answer

ABB ACS580 fault 2310 (Overcurrent) means the drive's output current exceeded the internal hardware overcurrent trip point — typically about 3.5× the drive's continuous rating for the trip to fire. In the field this is almost always a load-side problem: shorted motor lead, stalled motor under a sudden load step, output-side ground fault, or an acceleration ramp set too aggressively for the load. The drive itself is rarely the failure point.

## What fault 2310 means

The ABB ACS580 measures output phase current with high-speed transducers and feeds the readings into both the firmware current regulator and a hardware overcurrent comparator. The hardware comparator is the last line of defense — it trips faster than the firmware can respond, shutting off all six IGBTs within microseconds when peak phase current exceeds approximately 350% of drive rated current.

Fault 2310 logs the trip cause as "Overcurrent." The ACS580 firmware does not distinguish in the fault code itself between overcurrent from a phase-to-phase short (which would be a sharp, fast event) and overcurrent from a stalled motor (which is a slower rise). Both end up as 2310. The differentiation comes from the auxiliary fault data — read the fault buffer in Drive Composer or on the assistant control panel ACS-AP-W.

The ACS580 is part of ABB's all-compatible drive family — it shares much of its parameter structure with the ACS880, ACS380, and others. Fault 2310 logic is consistent across these platforms. Parameter **03.01 Status word 1** captures real-time drive status, and the fault history is in parameter group 04 (Fault and warning).

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a parts swap. **Do not clear the fault before you read the history.**

Open Drive Composer (free Entry version is fine for diagnostics, Pro is needed for some advanced features). Connect via USB through the assistant panel or via Ethernet if your drive has the FENA-21 option. Navigate to the Fault Log.

Alternatively, on the ACS-AP-W assistant control panel: from the main menu, go to **Diagnostics → Fault log**. You'll see the last 16 events with timestamps.

Capture for each 2310 event:

- **Aux code** — fault auxiliary data. On the ACS580, 2310's aux code is a hexadecimal value where bits indicate which phase tripped (U/V/W) and whether the trip was on positive or negative cycle.
- **Parameter 04.01 Tripping fault** — most recent fault code
- **Parameter 04.02 Active fault 2** through **04.05 Active fault 5** — earlier faults
- **Operating data at trip** — output current, output frequency, DC voltage, control mode. The ACS580 stores this with each fault event.

**Field insight on fault 2310:** the aux code is the differentiator. A consistent aux code across multiple trips means the fault is on a specific phase — chase that phase. A varying aux code means the fault is symmetric — likely a stall, ramp issue, or motor data mismatch. Pull the aux code before clearing.

## Read parameter 03.01 first

ABB's diagnostic philosophy is that parameter 03.01 (Status word 1) gives you the drive's real-time state — running, faulted, ramping, current-limited, voltage-limited, etc. Before clearing a fault, snapshot 03.01 — it captures the last state the drive was in. This is especially useful when 2310 follows a sequence of warnings (current-limit-active, IGBT temp warning) that explain why the drive eventually tripped.

## Common causes (ranked by frequency)

1. **Motor stall under sudden load** — pump sucks debris, conveyor jams, grinder bites oversized material. Current spikes faster than firmware regulator can respond.
2. **Phase-to-phase short in motor leads** — chafed cable, water in J-box, shorted downstream disconnect.
3. **Phase-to-ground fault** — usually trips fault 2330 (Earth fault) first, but a hard ground short can trip 2310 first if the magnitude is large enough.
4. **Acceleration ramp too aggressive** — parameter **23.12 Acceleration time 1** set too short for load inertia. Drive hits current limit, then trips 2310 if the limit is exceeded.
5. **Motor parameters mismatched** — wrong values in **99.06 Motor nominal current**, **99.07 Motor nominal voltage**, **99.10 Motor nominal power**. Drive's torque control is fighting actual motor characteristics.
6. **Drive undersized for application** — ACS580 is sized one frame too small for actual peak demands during a high-inertia start or process load step.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time (minimum 5 minutes on ACS580 frame R1, longer on larger frames), verify zero DC link energy at the DC+ and DC- terminals with a CAT-IV meter.

1. **Read the fault log and aux code before clearing.** Record fault code, aux code, output current at trip, output frequency at trip, and any precedent warnings (2.x.x series).

2. **Megger the motor and output cable.** Disconnect U2, V2, W2 from the drive output terminals. Use a 500V megohmmeter (1000V if rated). Test U-V, V-W, U-W, and each phase to ground. Healthy: above 100 MΩ at 25°C. Phase-to-phase below 1 MΩ = your fault.

3. **Walk the cable run.** Conduit bodies, strain reliefs, transitions. Look for crushed cable, abrasion, melted insulation.

4. **Verify motor parameters match the nameplate.** Open Drive Composer or the assistant panel, navigate to parameter group 99 (Motor data). Confirm: **99.06 Motor nominal current**, **99.07 Motor nominal voltage**, **99.08 Motor nominal frequency**, **99.09 Motor nominal speed**, **99.10 Motor nominal power**, **99.11 Motor cos phi**. All values must match the nameplate. A drive set up for a 5.5kW motor driving a 7.5kW motor will hit current limit on every start.

5. **Run motor identification.** Set **99.13 ID run requested** to **1 (Normal)** or **2 (Reduced)**. Normal ID rotates the motor slowly and is most accurate; Reduced is at standstill if mechanical considerations don't allow rotation. The drive measures stator resistance, leakage inductance, main inductance, and tunes the regulator. Without ID, torque control is approximate and overcurrent trips become more likely under transients.

6. **Check ramp times.** **23.12 Acceleration time 1** must allow load inertia to follow the speed reference without exceeding current limit. For high-inertia applications, 30–120 second ramps are normal. **23.13 Deceleration time 1** likewise. Start conservative and reduce only if process demands it.

7. **Verify current limit settings.** **30.17 Maximum current** sets the firmware current limit, typically 150–200% of motor rated current. If set too low, the drive can't supply normal inrush; if set above hardware capability, the hardware comparator trips first as 2310.

8. **Check parameter 03.01 status word.** During a normal run cycle, 03.01 should show steady "running" without the current-limit-active bit set. If you see the limit bit asserted before each 2310, your ramp or load is over-demanding the drive.

> **Field knowledge nugget:** On ABB ACS580 drives in mixer applications — paint mixers, ink dispersion mixers, large food-grade batch mixers — fault 2310 trips that happen specifically after the batch process changes viscosity (e.g., adding a thickener) are almost always a torque-demand step the drive's current limit can't supply, not a drive problem. The mixer suddenly needs more torque, current spikes, and either the firmware regulator hits the limit and backs off (eventually stalling the mixer) or the hardware overcurrent trips. The fix on a constant-torque application is parameter **30.17 Maximum current** sized to peak process demand plus margin, AND the drive sized for the peak — sometimes one frame above what a steady-state torque calculation suggests. I worked with a Sherwin-Williams pigment mixer that chronically tripped 2310 on thickener addition. Up-sized from ACS580 7.5kW to 11kW, raised 30.17 to 180% — no more trips, and the motor lived because torque was supplied without saturation. Don't undersize mixer drives; the load is not constant.

## Parts that may need replacement

ABB ACS580 drives are sold as complete units in frames R1–R5. Higher frame drives (R6+) may have field-replaceable modules but require ABB-trained service.

| Part | Order Code | Typical Cost | Where to Buy |
|---|---|---|---|
| ACS580-01-12A6-4, 5.5kW, 400V | ACS580-01-12A6-4 | $1,300–$1,700 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault) |
| ACS580-01-018A-4, 7.5kW, 400V | ACS580-01-018A-4 | $1,700–$2,200 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault) |
| ACS580-01-030A-4, 15kW, 400V | ACS580-01-030A-4 | $2,800–$3,400 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault), [Wolf Automation](https://www.wolfautomation.com) |
| Assistant control panel | ACS-AP-W | $295–$385 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault) |
| FENA-21 Ethernet/IP adapter | FENA-21 | $385–$520 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault), [Wolf Automation](https://www.wolfautomation.com) |
| Output choke (du/dt filter) | NOCH 80-V-26-575 family | $620–$890 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault) |
| 500V/1000V megohmmeter | Fluke 1587 FC | $620–$780 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=abb-acs580-2310-fault) |

## When to call ABB or a controls engineer

Call senior support when: fault 2310 recurs after motor megger results are clean and motor ID run has completed successfully; the application is constant-torque (mixers, crushers, hoists) and you suspect drive sizing issues — ABB Application Engineering can validate sizing against your load curve; you need to integrate the drive with safety functions (STO, SLS) that require specific parameter configuration; or when 2310 only appears during specific process events you cannot reproduce on a service call.

## FAQs

**Why does ABB use number codes (2310) instead of letter prefixes (F2310)?** ABB's all-compatible drive family uses an IEC-aligned fault numbering system where the code itself maps to a defined fault category. 2310 specifically lives in the overcurrent block of the code space. The number is the fault — there's no separate prefix in ABB's nomenclature.

**Difference between fault 2310 and warning 2.0.0 (Current limit)?** 2310 is a hard trip — the drive stops. The 2.x.x series are warnings that signal the regulator is actively limiting current to prevent a trip. Warnings precede trips on properly tuned systems; if you see continuous current-limit warnings without a 2310, the regulator is doing its job but you're hammering the drive — re-evaluate the application.

**Can I disable the overcurrent protection?** No. The hardware comparator is not user-adjustable in any way, and the firmware-level current limit (30.17) has a minimum value tied to drive rating. The fault is hardware protection and removing it means destroyed IGBTs.

**My ACS580 fault log shows multiple faults in quick succession (2310, then 2330, then 7510). What happened?** Cascading faults. 2310 was the first to trip; as the drive shut down, the asymmetric current condition produced a residual that briefly looked like a ground fault (2330); the loss of drive output to the upstream system triggered a comm-loss fault (7510). The root cause is whatever caused the first 2310. The others are downstream consequences.

**Does motor ID need to be re-run periodically?** Only after physical changes — replacing the motor, replacing the cable run, changing the load coupling significantly. Once ID has been run and the drive has accurate motor parameters, they don't drift. ABB recommends re-running ID if motor maintenance has changed the stator (rewinding, brush replacement on DC, etc.).

## Related guides

- [Siemens SINAMICS F30001 Fault — Power Module Overcurrent Fix](/posts/siemens-sinamics-f30001-fault)
- [Allen-Bradley PowerFlex F012 Fault — HW Overcurrent Fix](/posts/allen-bradley-powerflex-f012-fault)
- [Allen-Bradley PowerFlex F063 Fault — Phase Short Fix](/posts/allen-bradley-powerflex-f063-fault)
