---
title: "Mitsubishi FR-A700 Fault Codes - What It Means and How to Fix It"
description: "The Mitsubishi FR-A700 series uses fault codes to protect the drive, motor, and connected equipment. This guide explains the most common FR-A700 alarm codes, what causes them, and how to troubleshoot them step by step."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Mitsubishi FR-A700 is a heavy-duty variable frequency drive used on conveyors, fans, extruders, pumps, compressors, and packaging equipment. It is popular because it is reliable, flexible, and well supported, but when something goes wrong the display throws a compact alarm code like **E.OC1**, **E.OV3**, or **E.THT**. If you do not speak Mitsubishi fault-code shorthand, those alarms can slow a repair down fast.

The good news is the FR-A700 is actually pretty honest. Its fault codes usually point you toward the problem area immediately. The trick is understanding whether the alarm happened during acceleration, constant speed, or deceleration, because Mitsubishi uses that context to narrow down the cause.

## What Does Mitsubishi FR-A700 Fault Codes Mean?

The FR-A700 fault list is broad, but most field service calls revolve around a small group of repeated alarms. Here are the ones technicians see most often.

### E.OC1, E.OC2, E.OC3 — Overcurrent During Acceleration, Constant Speed, or Deceleration

These are among the most common FR-A700 faults. The drive detected output current above a safe threshold.

- **E.OC1** happens during acceleration. Common causes are acceleration time set too short, motor cable short, or load jam.
- **E.OC2** happens at constant speed. Common causes are sudden load increase, mechanical binding, or incorrect motor parameter tuning.
- **E.OC3** happens during deceleration. Common causes are an abrupt stop command, regenerative load behavior, or a braking setup issue.

### E.OV1, E.OV2, E.OV3 — Overvoltage During Acceleration, Constant Speed, or Deceleration

These mean the DC bus voltage inside the drive rose too high.

- **E.OV1** during acceleration is less common but can happen with unstable line voltage.
- **E.OV2** at constant speed often points to incoming power issues or an overhauling load.
- **E.OV3** during deceleration is classic regeneration. The motor is sending energy back into the drive faster than the DC bus can absorb it.

### E.THT — Heatsink Overtemperature

The drive's internal temperature sensor saw the heatsink get too hot. That usually means the cooling fan has failed, the air path is blocked with dust, the panel is too hot, or the drive is overloaded.

### E.THM — Motor Overload

The electronic thermal model calculated that the motor is overheating. This can come from an overloaded machine, bad motor data entered in the parameters, low motor speed with high torque demand, or a motor that is simply undersized.

### E.GF — Ground Fault

The drive sees leakage current to ground on the output side. Causes include damaged motor cable insulation, moisture in the motor junction box, failed motor windings, or contamination inside the drive.

### E.PE — Parameter Storage or Memory Error

The drive has a parameter memory issue. This may happen after a power event, failed keypad programming session, or internal control-board fault.

### E.UVT — Undervoltage

The DC bus dropped too low. Common causes are weak incoming power, a missing phase on the input, or voltage sag during startup of another large machine on the same service.

## How to Fix It

1. **Write down the exact code and when it occurred.** The number after the code matters, because E.OC1 and E.OC3 are not the same problem.
2. **Check whether the fault happened during acceleration, run, or deceleration.** That tells you whether to inspect load changes, braking, or line power first.
3. **Inspect the driven equipment mechanically.** Belts, couplings, gearboxes, fan wheels, and pump impellers cause plenty of false "drive" problems. A jammed machine can create overcurrent instantly.
4. **Measure incoming voltage.** For undervoltage or overvoltage alarms, confirm the line-side supply at R/L1, S/L2, and T/L3 is stable and balanced.
5. **Inspect motor leads and insulation.** For ground-fault or overcurrent alarms, disconnect the motor and megger the cable and motor separately.
6. **Increase acceleration or deceleration time.** If E.OC1 or E.OV3 happens during speed changes, lengthen the ramp settings before replacing anything.
7. **Check the cooling path.** For E.THT, verify the cooling fan runs, clean the heatsink fins, and make sure the enclosure has ventilation.
8. **Review motor parameter data.** Wrong motor full-load amps, base frequency, or control mode can trigger nuisance overloads.
9. **Inspect braking hardware.** If the application stops quickly, make sure any external braking resistor is connected correctly and sized for the duty cycle.
10. **Power-cycle only after inspection.** Resetting repeatedly without checking the cause can damage the motor or drive further.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Mitsubishi-compatible braking resistor | Helps resolve E.OV3 decel overvoltage faults | $40–$140 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-a700-fault-codes&k=Mitsubishi+VFD+braking+resistor&tag=errorcodefixes-20) |
| Cooling fan for FR-A700 drive | Fixes E.THT overheating when fan stops | $20–$60 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-a700-fault-codes&k=Mitsubishi+FR-A700+cooling+fan&tag=errorcodefixes-20) |
| Insulation resistance tester | Needed to diagnose E.GF ground-fault conditions | $60–$200 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-a700-fault-codes&k=insulation+resistance+tester+megger&tag=errorcodefixes-20) |
| Shielded VFD motor cable | Replaces damaged output cable causing E.GF or E.OC faults | $50–$200 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-a700-fault-codes&k=shielded+VFD+motor+cable&tag=errorcodefixes-20) |
| Line reactor | Helps with unstable incoming power and nuisance voltage faults | $80–$250 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-a700-fault-codes&k=three+phase+line+reactor+VFD&tag=errorcodefixes-20) |
| Mitsubishi FR-A700 replacement keypad or drive | Needed if E.PE or control hardware faults persist | $100–$800 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-fr-a700-fault-codes&k=Mitsubishi+FR-A700+drive&tag=errorcodefixes-20) |

## When to Call a Pro

Call a VFD technician or industrial electrician if:

- You get **E.GF** and the motor or cable fails insulation testing
- The drive throws **E.PE** repeatedly after re-entering parameters
- Overcurrent faults persist after mechanical checks and ramp adjustments
- The drive overheats even though the fan is working and the enclosure is clean
- You suspect an internal IGBT, rectifier, or control-board failure
- The machine is production-critical and trial-and-error downtime is too expensive

Ground faults, repeated overcurrent trips, and memory faults can all point to bigger failures. The sooner you separate line-side problems, motor problems, and drive problems, the less money you burn.

## Frequently Asked Questions

**Q: What is the difference between E.OC1, E.OC2, and E.OC3 on a Mitsubishi FR-A700?**

A: They are all overcurrent faults, but the timing changes the likely cause. E.OC1 is usually acceleration-related, E.OC2 is usually a running-load issue, and E.OC3 often points to deceleration or regenerative behavior. Same family of problem, different moment in the cycle.

**Q: Can I just increase the acceleration time to fix E.OC1?**

A: Sometimes yes, and it is one of the first things to try. But if the machine is mechanically jammed, the motor cable is damaged, or the motor parameters are wrong, increasing the ramp only hides the problem for a while.

**Q: Why does the FR-A700 keep showing E.OV3 when the machine stops?**

A: That is the classic deceleration overvoltage fault. The load is pushing energy back into the drive. A longer decel time or a properly sized braking resistor usually fixes it.

**Q: How do I know if the motor or the drive caused E.GF?**

A: Disconnect the motor leads from the drive and insulation-test the motor and cable separately. If the motor fails to ground, the problem is downstream. If both test clean and the drive still faults, the issue may be inside the drive.

**Q: Is the FR-A700 worth repairing?**

A: Usually yes if the problem is a fan, keypad, parameter issue, or external braking hardware. If the power section has failed on an older unit and replacement parts are scarce, replacement can make more economic sense than repair.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
