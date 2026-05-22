---
title: "Schneider Altivar OCF Fault — Overcurrent Fix"
description: "Schneider Altivar OCF (Overcurrent Fault) on the ATV320, ATV340, ATV630, ATV930, and most legacy ATV61/71 drives means the drive's IGBT power module..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: schneider-altivar-fault-code-ocf
featured: false
draft: false
tags:
  - schneider-electric
  - vfd
  - industrial-maintenance
  - drives
  - overcurrent-fault
---
## Quick answer

Schneider Altivar OCF (Overcurrent Fault) on the ATV320, ATV340, ATV630, ATV930, and most legacy ATV61/71 drives means the drive's IGBT power module detected current exceeding the trip threshold during a run — typically 1.5-3x the motor's nameplate current. The most common single root cause in industrial environments is a short circuit in the motor cable from cable carrier wear or coolant intrusion, not motor or drive failure. Always megger the motor and cable before assuming the drive is bad. Read the fault history via parameter 7.30 before clearing.

## What OCF means on Schneider Altivar

Schneider Electric Altivar drives use 3-letter fault codes (mostly upper case) — a clean naming convention that's much easier to remember than Allen-Bradley's F-numbers or Yaskawa's hex codes:

- **OCF** — Overcurrent Fault (this guide)
- **OSF** — Overspeed Fault
- **USF** — Undervoltage Fault
- **OHF** — Overheat Fault (drive heatsink)
- **OLF** — Overload Fault (motor thermal)
- **CFF** — Configuration Fault
- **SLF** — Modbus Communication Fault
- **EPF** — External Fault (digital input)

OCF specifically fires when the drive's instantaneous current measurement exceeds approximately 200-300% of the drive's rated continuous current. The trip is fast (typically within 1-5 milliseconds of the event) because at this level the IGBTs are at risk of thermal failure within milliseconds. The drive's protection is non-resettable until power-cycled or a fault reset command is issued.

The Altivar parameter set includes a fault history accessed via parameter **7.30** (or the menu path FAULT → HISTORY on newer ATV630/930 models). The history stores the last 8-15 faults with timestamps, motor current at trip, DC bus voltage at trip, drive temperature at trip, and the run state at trip. **Always read 7.30 before clearing OCF** — once cleared, the diagnostic context is lost.

The Altivar Soft Programming Tool (SoMove) or the local HMI (the Graphic Display Terminal on ATV630/930, the basic 7-segment on ATV320) can both display 7.30. SoMove via Bluetooth or USB allows downloading the full fault history to a PC for analysis — useful when you need to share data with a Schneider field application engineer.

## Common causes (ranked by frequency)

In industrial Altivar service experience:

1. **Short circuit in motor cable (phase-to-phase or phase-to-ground)** — about 25%. Cable carrier wear, mechanical damage, coolant intrusion.
2. **Motor winding insulation breakdown (ground fault)** — about 18%. Aged motor, water/coolant exposure.
3. **Mechanical load step or jam (sudden inrush)** — about 15%. Conveyor jammed, pump cavitating, fan blade fouled.
4. **Wrong acceleration time setting (parameter 3.10)** — about 10%. Accel too aggressive for high-inertia load.
5. **Loose connection at drive output terminals** — about 8%. Arcing creates current pulse.
6. **Drive at end of life (IGBT degraded)** — about 7%. Older drives become sensitive.
7. **Brake circuit issue on drives with dynamic braking** — about 5%. Brake stuck partially engaged.
8. **Output filter (LC filter or dV/dt filter) wired wrong or failed** — about 5%.
9. **Motor wrong size for the drive** — about 4%. Undersized motor draws more current than spec'd.
10. **Wrong parameter 4.01 (motor nameplate current)** — about 3%. Incorrect setup.

**Pro nugget:** Altivar drives provide a parameter **6.10 (Inst I)** that shows real-time motor current — accessible from the local HMI under MONITORING. **The trick**: if OCF is intermittent, run the drive in normal operation and watch parameter 6.10 in real-time. Current should remain below 110% of nameplate during steady-state, and below 150% during acceleration. If you see spikes to 200%+ momentarily, you have a load issue (mechanical jam, hydraulic spike, sudden process step), not a drive issue. If you see steady-state current creeping up over hours of running, you have a thermal/mechanical issue (bearing degrading, motor overheating). The drive itself only sees current — but watching the current behavior over time tells you whether OCF is downstream (motor/load) or internal (drive). Use the SoMove trending tool to log current over time for hard-to-catch faults.

## Step-by-step diagnosis

Before you start: lock and tag the disconnect, verify zero voltage at the drive DC bus terminals (typically labeled BR+ and BR-) with a CAT-IV meter after the recommended discharge time (5 minutes for ATV320, longer for higher-power frames).

1. **Read fault history without clearing.** Access parameter 7.30 via the HMI: 7 (faults menu) → 30 (history). Note: motor current at trip (parameter 7.31), DC bus voltage at trip (7.32), drive temp at trip (7.33), and the prior 3-5 faults. Take photos of the screen if needed.

2. **For an OCF at startup:** Disconnect the motor cable from the drive output terminals (U, V, W). Re-power and try to start — if OCF clears without the motor, the issue is in the motor or cable.

3. **For an OCF during acceleration:** Check parameter 3.10 (acceleration time). Default is typically 3 seconds. For high-inertia loads, increase to 10-30 seconds. Re-test.

4. **For an OCF at steady-state run:** Watch parameter 6.10 (instantaneous current) on the HMI during operation. Compare against motor nameplate (parameter 4.01). If current is climbing toward trip threshold during normal operation, you have a load or motor issue.

5. **Megger the motor.** With the motor cable disconnected from the drive (U-V-W leads pulled), use a 500V megger to test each phase to ground. Anything below 1 megohm at 25°C indicates degraded insulation; below 100 kΩ and you have a ground fault that will trip OCF on every start.

6. **Continuity test motor cable.** With the cable disconnected at both ends (drive end and motor end), check continuity between conductors. Should be open (OL) between each pair of phases and between each phase and ground/cable shield. Any short = damaged cable.

7. **Inspect drive output terminals for arcing.** Pull the drive's terminal cover, inspect U, V, W lugs for discoloration, missing screws, or melted insulation. Re-torque to spec (ATV320 frame B is typically 8-12 in-lbs).

8. **Verify motor parameters match nameplate.** Parameters 4.01 (motor current), 4.02 (motor voltage), 4.03 (motor frequency), 4.04 (motor speed), 4.05 (motor power factor) must match the nameplate on the motor exactly. Mismatch causes the drive to over-current the motor.

9. **For repeated OCF after motor and cable check OK:** The drive's IGBT power module may be degraded. Replacement drive needed; not field-repairable.

10. **Set up SoMove logging if intermittent.** Connect SoMove via Bluetooth or USB, configure a trend for parameter 6.10 and DC bus voltage, log for 24-48 hours, identify the event timing.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Altivar ATV320 1.5kW 480V | Schneider ATV320U15N4C | $585-885 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| Altivar ATV320 5.5kW 480V | Schneider ATV320U55N4C | $1,485-1,985 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| Altivar ATV630 22kW 480V | Schneider ATV630D22N4 | $4,200-5,800 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf), [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| Altivar ATV930 55kW 480V (closed loop) | Schneider ATV930D55N4 | $9,800-13,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| Graphic display terminal (HMI) | Schneider VW3A1101 | $385-485 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| SoMove software (free) | Schneider | Free | Schneider download |
| Bluetooth dongle for SoMove | Schneider VW3A8114 | $185-245 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf), [Amazon](https://www.amazon.com) |
| Motor cable, shielded VFD-rated (per ft) | Belden 29504 / similar | $5-12/ft | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| Megger insulation tester (500V) | Fluke 1577 | $385-485 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |
| Phoenix Contact torque screwdriver | Phoenix 1212597 | $185-235 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=schneider-altivar-fault-code-ocf) |

Altivar drives are sold complete units only — Schneider does not field-replace power modules, control boards, or capacitors as separate parts. Refurb drives are widely available through Galco at 40-60% of new pricing.

## When to call a controls engineer

Call senior controls support when:

- Multiple OCF events with widely varying motor current at trip. Suggests intermittent power quality or drive aging.
- OCF on a cold morning only. Capacitor degradation; drive replacement coming.
- OCF paired with USF (undervoltage). Power supply issue, not drive.
- The drive is on a regenerative or common DC bus configuration. Special parameter setup required.
- The motor is a permanent-magnet synchronous motor (PMSM). PM motors have different overcurrent characteristics than induction; tuning required.

## FAQs

**Why does OCF happen only on the first start of the morning?**
Cold motor has slightly different impedance than warm. If the drive is set up with default parameters and the motor is at the edge of fitting the drive's curve, cold starts can cause OCF where warm starts don't. Tune the drive using parameter 5.01 (auto-tuning) when the motor is at cold-start temperature.

**Can I just increase the trip threshold to clear OCF?**
There's no direct "trip threshold" parameter — OCF threshold is hard-coded in firmware based on the drive's IGBT spec. You can only address OCF by reducing actual current draw (longer accel time, lower torque limit) or fixing the underlying issue.

**Should I add a line reactor for OCF?**
A line reactor (3-5% impedance) on the drive *input* doesn't directly address OCF — OCF is an output-side fault. A dV/dt filter or output reactor on the *output* can reduce voltage spike on the motor cable and is sometimes useful on long motor cable runs.

**Difference between OCF and OLF?**
OCF = instantaneous overcurrent (fast trip, IGBT protection). OLF = thermal overload (slow trip based on I²t accumulated heat). Different protection mechanisms; OCF catches sudden events, OLF catches sustained moderate overload.

**Will SoMove require a special license?**
No, SoMove is free from Schneider. Download from Schneider's website. The Bluetooth dongle is an inexpensive accessory ($185-245) but USB connection is free.

## Related guides

- [Schneider Altivar OSF Fault — Overspeed Fix](/posts/schneider-altivar-fault-code-osf)
- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/allen-bradley-powerflex-f004-fault/)
- [Allen-Bradley PowerFlex F005 Fault — Overvoltage Fix](/allen-bradley-powerflex-f005-fault/)
