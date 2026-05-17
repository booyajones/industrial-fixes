---
title: "Yaskawa VFD Fault OC — Overcurrent Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: yaskawa-vfd-fault-oc-overcurrent
featured: false
draft: false
tags:
  - electrical
  - vfd
  - yaskawa
  - overcurrent
description: "Yaskawa VFD fault OC means overcurrent on J1000, V1000, and A1000 series drives — here's how to diagnose and fix it."
---

## Error Code: Yaskawa VFD Fault OC

**What it means:** The OC fault on Yaskawa J1000, V1000, and A1000 series variable frequency drives indicates that the output current exceeded 200% of the drive's rated output current. The drive's hardware overcurrent comparator (independent of software current limiting) detected this condition and shut down the output IGBTs in under 10 microseconds to prevent drive damage. This is a hardware-level trip, not a software protection — it means the current spike was severe and instantaneous.

OC is distinct from Yaskawa's OL1 (motor overload) and OL2 (drive overload) faults, which are software-based thermal models that trip on sustained overcurrent. OC is a fast, hard trip from a momentary spike.

## Common Causes

- **Output phase-to-phase or phase-to-ground short circuit** — The most dangerous cause. A failed motor winding, damaged motor cable, or contaminated motor terminal box can create a direct short that generates an instantaneous current spike far above 200% rated. This is the first thing to rule out.
- **Acceleration too fast** — Insufficient acceleration ramp time causes the motor to draw excess current as it tries to build flux faster than the rotor can respond. On V1000 drives in V/f mode, this is extremely common.
- **Motor insulation breakdown at startup** — As voltage ramps during acceleration, degraded motor insulation breaks down at the point where it can no longer hold off the applied voltage, causing a momentary overcurrent spike.
- **Contactor or bypass switch closing across drive output while running** — Any hard connection across the drive's output terminals while the drive is running causes an immediate OC fault and typically destroys the output stage.
- **Ground fault in the motor cable** — A phase conductor shorted to the cable shield or conduit creates a ground fault current that trips OC.
- **Drive output IGBT failure** — A failed IGBT that shorts its collector-to-emitter path causes a current path that appears as a load short. In this case, the drive itself is the cause.

## Step-by-Step Fix {#step-by-step-fix}

1. **Do not clear and restart immediately.** An OC fault from a short circuit will destroy the drive's output stage if you reset and restart without investigation. The drive has already done its job by shutting down in microseconds — give it the same respect and investigate before re-energizing.

2. **Disconnect the motor leads from the drive output terminals (T1/U, T2/V, T3/W).** With LOTO applied, physically disconnect all three output phase leads from the drive. This isolates the drive from the motor and cable.

3. **Test the motor for winding and insulation faults.** Using a 500V megohmmeter, measure from each phase lead to motor frame ground. Minimum acceptable reading is 1 MΩ; healthy motors read 100 MΩ+. Also measure phase-to-phase resistance at the motor terminals — balance within 5% is expected. Any short, ground, or unbalanced winding reading means the motor is failed.

4. **Test the motor cable for ground faults.** With the motor disconnected from the cable at the motor terminal box, measure resistance from each conductor to the cable shield or conduit. Any reading below 1 MΩ indicates a damaged cable that needs replacement.

5. **With motor and cable disconnected, attempt a drive-only test.** Reconnect power to the drive (without motor leads connected). Attempt to run the drive to 60 Hz on the digital operator (LOCAL mode). If OC occurs with no motor connected, a drive output IGBT has failed — the drive requires repair or replacement.

6. **Increase the acceleration time (C1-01 on A1000, b1-17 on V1000, C1-01 on J1000).** If motor and cable tested good, the fault was caused by excessive acceleration rate. On Yaskawa drives, C1-01 is Acceleration Time 1. Increase by 50–100% and test with the motor reconnected. For V/f mode applications, also consider enabling the stall prevention function (L3-01 through L3-04 on A1000).

7. **Verify motor insulation for a drive application.** Yaskawa drives produce high dV/dt output waveforms (voltage rise times of 500–2000 V/µs). Standard NEMA B motors with older insulation systems can fail at the first winding turn due to this stress. If the motor is older than 10 years and the OC fault appears at a specific point in every acceleration, consider replacing the motor with an inverter-duty rated unit or adding a Yaskawa dV/dt filter (part LCRD series) at the drive output.

8. **Check and clear the fault history.** Yaskawa drives store the last 4 faults in U2 monitors (U2-01 through U2-04 on A1000). U2-02 shows the output current at the time of the fault, U2-03 shows output frequency. This data helps confirm whether the OC was at startup (0 Hz, indicating a wiring short) or mid-acceleration (indicating a ramp time issue).

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy | ------ | ------------ | ------------- | ------------- |  | Yaskawa dV/dt Output Filter | LCRD series (size by drive A) | $150–$600 | Yaskawa distributor |
|------|------|------|------|------|------|------|------|------|------|------|------|------|
| Inverter-duty Motor | NEMA MG1 Part 31 rated | $300–$2000+ | [Amazon](https://www.amazon.com/s?i=industrial&k=NEMA+MG1+Part+31+rated+NEMA+MG1+Part+31+rated&tag=errorcodefixes-20) \| Grainger / motor shop | Replacement J1000 Drive | CIMR-JU2A0004FAA (varies)&tag=) | $300–$700 | Yaskawa distributor / Amazon |  | Motor Cable (THHN shielded) | By footage | $2–$8/ft | Grainger / electrical supply |

##

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
