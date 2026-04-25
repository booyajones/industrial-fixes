---
title: "Siemens SINAMICS G120 Complete Guide - Setup, Fault Codes, and Commissioning"
description: "Complete Siemens SINAMICS G120 guide covering setup, commissioning, major fault codes, parameter basics, and practical fixes for overcurrent, overvoltage, undervoltage, and motor faults."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The Siemens SINAMICS G120 is one of the most common modular variable frequency drives used in industrial HVAC, pumps, conveyors, and process equipment. It combines a Control Unit with a matching Power Module, which makes it flexible but also a little more intimidating for first-time commissioning and troubleshooting.

The good news is that the G120 is extremely transparent once you know where to look. Fault codes are structured, commissioning follows a repeatable sequence, and most nuisance trips trace back to a short list of causes: aggressive ramps, weak incoming power, bad motor data, ground faults, or poor wiring practices.

This guide gives you a practical, field-focused overview of the SINAMICS G120. It covers what the main alarms and faults mean, what parameters matter most, how to commission the drive correctly, and when a fault points to real hardware damage instead of a setup mistake.

## What Does Siemens SINAMICS G120 Fault Data Mean?

On a SINAMICS G120, faults and alarms appear as codes such as **F30001**, **F30002**, **F30005**, or **A0501** depending on the control unit and firmware family. In practice, technicians often refer to the short meaning rather than the full number: overcurrent, DC link overvoltage, undervoltage, motor overload, communication fault, or encoder fault.

A few important rules help you interpret G120 diagnostics correctly:

- **Faults (F-codes)** stop the drive and require reset after the root cause is addressed.
- **Alarms (A-codes)** warn of a problem or limit condition but may not stop operation.
- The drive stores fault history, operating state, frequency, current, voltage, and sometimes temperature data at the time of trip.
- The exact numbering can vary slightly by Control Unit and firmware revision, but the root causes stay consistent.

Here are the G120 fault groups you will see most often in the field:

| Fault / Alarm | Meaning | Typical Root Cause |
|---|---|---|
| F30001 | Overcurrent | Short acceleration time, jammed load, shorted motor cable |
| F30002 | DC link overvoltage | Decel too fast, regenerative load, missing brake resistor |
| F30003 | DC link undervoltage | Low incoming voltage, supply dip, blown fuse |
| F30005 | I2t overload / drive overload | Sustained high load current |
| F30021 | Ground fault | Motor winding to ground, damaged output cable |
| F30035 | Motor stalled or blocked | Mechanical seizure, heavy starting load |
| F30050 | Power module overtemperature | Dirty heatsink, failed fan, hot enclosure |
| F07011 / comms faults | Fieldbus communication problem | PLC offline, broken Profibus/Profinet link |
| A0501 | Current limit active | Drive is protecting itself during acceleration |
| A0910 | Parameterization warning | Setup mismatch or incomplete commissioning |

What matters most is **when** the fault happens.

- If it trips **at startup**, suspect wiring, acceleration, or incorrect motor data.
- If it trips **during deceleration**, suspect regeneration and DC bus overvoltage.
- If it trips **after running for 20 to 60 minutes**, suspect thermal loading, poor cooling, or overload.
- If it trips **randomly**, suspect loose terminals, insulation breakdown, or unstable incoming power.

The G120 also depends heavily on correct motor nameplate data. If rated current, voltage, frequency, or motor model data are wrong, the drive's current regulator and slip calculations are wrong too. That creates nuisance faults that look like hardware issues but are really setup problems.

## How to Fix It

**1. Start with the fault memory, not the fault reset button**

Before resetting anything, record:
- Fault number
- Output frequency at trip
- Motor current at trip
- DC bus voltage at trip
- Drive heatsink temperature if available
- Whether the trip happened during start, run, or stop

If you clear the fault first, you erase useful context and make the problem harder to solve.

**2. Verify incoming power quality**

Many G120 faults begin on the line side.

- Measure incoming voltage phase-to-phase at the line input terminals.
- Confirm voltage balance between phases is within about 2 percent.
- Check input fuses, disconnects, and line reactor connections.
- Look for browned or overheated terminals.

Low or unstable input voltage causes undervoltage trips, weak torque, and sometimes false overcurrent behavior under load.

**3. Check the motor cable and motor insulation**

With power locked out:
- Disconnect the motor leads from the drive output.
- Meg the motor and output cable phase-to-ground.
- Check phase-to-phase resistance balance.
- Inspect cable terminations for loose strands or insulation damage.

If insulation is weak, the drive may fault on ground fault or overcurrent instantly at startup.

**4. Slow the acceleration ramp**

If the drive faults during startup, increase the ramp time first. This is one of the fastest and most effective fixes.

A ramp that's too short forces the drive to deliver excessive torque instantly. On fans, pumps, and conveyors with inertia, that pushes current above safe levels.

- Double the acceleration time and retest.
- If the drive now starts normally, the previous ramp was too aggressive.
- If current limit alarms appear without a hard trip, you are close but still demanding too much torque.

**5. Slow the deceleration ramp or add braking**

If the drive faults when stopping, the motor is regenerating energy back into the DC bus. That energy has to go somewhere.

- Increase deceleration time.
- Enable ramp shaping if available.
- Add or verify the braking resistor on regenerative applications.
- Check that brake chopper wiring is correct.

Common offenders are high-inertia fans, centrifuges, and conveyors that are forced to stop too quickly.

**6. Verify motor nameplate parameters carefully**

A properly commissioned G120 depends on correct motor data. Check the programmed values against the nameplate for:
- Rated voltage
- Rated current
- Rated frequency
- Rated speed
- Rated power
- Power factor if required by your application mode

Even one bad value can distort current regulation and thermal protection.

**7. Run motor identification / optimization**

After entering correct motor data, run the appropriate identification routine if your control mode supports it. This improves current control, torque response, and speed stability.

On many G120 setups, skipping this step leads to unstable low-speed operation or nuisance overcurrent trips under changing load.

**8. Inspect cooling and enclosure conditions**

A G120 with restricted airflow will fault even if everything else is correct.

- Clean heatsinks and fan filters.
- Verify cooling fans are running.
- Measure enclosure temperature.
- Check that the drive has the minimum side and top clearance required by Siemens.

Heat-related faults often appear after the machine has been running fine for a while, then trips once the power module reaches its thermal limit.

**9. Check the mechanical load, not just the drive**

If the motor is trying to move a jammed or overloaded machine, the G120 is doing its job by faulting.

- Rotate the load manually if possible.
- Check bearings, gearboxes, couplings, and driven equipment.
- Look for product buildup, seized dampers, or stuck pump impellers.

Drive faults are often symptoms of mechanical trouble.

**10. Review fieldbus and control wiring**

If the drive runs from PLC commands over Profinet or Profibus, unstable communications can create intermittent trips or loss-of-run command issues.

- Check shield termination.
- Verify address and node configuration.
- Confirm PLC watchdog and comm timeout settings.
- Inspect control terminals for loose wires on enable, fault reset, or STO circuits.

A loose STO loop or enable contact can mimic a drive failure.

### Common commissioning flow for a new G120

A clean commissioning process prevents most first-start faults.

1. Verify drive frame, power module, and control unit match the motor and line voltage.
2. Confirm motor is correctly wired for the available voltage.
3. Enter motor nameplate data exactly.
4. Set acceleration and deceleration ramps conservatively.
5. Select the right control mode for the application.
6. Run motor identification if supported.
7. Test the motor uncoupled if practical.
8. Verify direction of rotation.
9. Reconnect the load and test under real operating conditions.
10. Save a backup of the final parameter set.

### Practical fault patterns and what they usually mean

- **Trips immediately on RUN:** shorted motor cable, bad motor data, jammed load, or failed power module.
- **Trips only on stop:** decel too short or no braking resistor.
- **Trips only at high speed:** weak incoming power, poor cooling, or mechanical overload.
- **Trips randomly after rain or washdown:** moisture intrusion in motor terminal box or cable.
- **Shows current limit alarm but keeps running:** ramp is too aggressive or load torque is close to drive size limit.

## Parts You May Need

| Part | Use | Amazon Link |
|---|---|---|
| Megohmmeter insulation tester | Check motor and cable insulation before startup | [View on Amazon](https://www.amazon.com/s?k=megohmmeter+insulation+tester+motor&tag=errorcodefixes-20) |
| True RMS clamp meter | Measure phase current and line voltage during operation | [View on Amazon](https://www.amazon.com/s?k=true+rms+clamp+meter+industrial&tag=errorcodefixes-20) |
| Braking resistor for VFD applications | Prevent DC bus overvoltage on fast stops | [View on Amazon](https://www.amazon.com/s?k=vfd+braking+resistor+industrial&tag=errorcodefixes-20) |
| Shielded VFD motor cable | Replace damaged output cable and reduce noise | [View on Amazon](https://www.amazon.com/s?k=shielded+vfd+motor+cable&tag=errorcodefixes-20) |
| Panel cooling fan and filter kit | Improve enclosure cooling around the drive | [View on Amazon](https://www.amazon.com/s?k=electrical+panel+cooling+fan+filter+kit&tag=errorcodefixes-20) |

## When to Call a Pro

Call a qualified drive technician or Siemens integrator when:
- The drive trips on overcurrent with the motor disconnected.
- Insulation readings are low and you are not equipped to isolate whether the fault is in the cable or motor.
- Power module overtemperature returns after cleaning and fan replacement.
- You suspect a failed IGBT power stage or control unit.
- The application uses encoder feedback, STO, or fieldbus integration and the commissioning is incomplete.
- The machine is mission-critical and repeated trial-and-error restarts risk damage.

A good rule is simple: if the fault points to line power, motor insulation, power electronics, or machine safety circuits, get a pro involved before you turn a nuisance trip into a burned drive.

## FAQ

**Q: What is the most common SINAMICS G120 startup fault?**

A: Overcurrent at startup is the most common. Usually the cause is a ramp that's too short, incorrect motor data, a jammed mechanical load, or a motor cable fault.

**Q: Why does my G120 fault only when stopping?**

A: That usually means regenerative energy is pushing the DC bus voltage too high. Increase decel time or add a braking resistor if the application needs fast stops.

**Q: Can I reset a G120 fault and keep running if it only happens once in a while?**

A: You can reset it, but you should still investigate. Random trips often mean loose wiring, marginal insulation, or unstable power. Those problems usually get worse, not better.

**Q: Do I always need motor identification on a Siemens G120?**

A: Not always, but it is highly recommended for better current control and torque performance. For demanding loads, skipping motor ID often creates nuisance faults later.

**Q: What is the difference between an alarm and a fault on the G120?**

A: An alarm warns you that the drive is close to a limit or sees an issue. A fault stops operation and requires reset after the root cause is addressed.
