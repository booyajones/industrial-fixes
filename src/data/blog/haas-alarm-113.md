---
title: "Haas Alarm 113 — Spindle Encoder Fault Causes & Fix"
description: "What Haas alarm 113 spindle encoder fault means, why it triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 113 — Spindle Encoder Fault: What It Means

Haas Alarm 113 is a **spindle encoder fault** — the CNC detected that the spindle encoder signal is missing, intermittent, or out of specification. The spindle encoder provides position and speed feedback to the control, enabling tapping cycles, C-axis positioning, and spindle synchronization for threading. Without a valid encoder signal, these functions cannot operate safely and the control faults out. Alarm 113 can appear at spindle startup or during a tapping or threading operation.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose encoder cable** — The encoder cable from the spindle motor or spindle head to the control cabinet is one of the most common failure points; it runs through the machine and is subject to flex fatigue and coolant exposure.
- **Failed spindle encoder** — The encoder disk, bearings, or internal electronics fail, producing no or corrupted feedback signal.
- **Contaminated encoder** — Coolant or chips entering the encoder housing corrupt the optical disk and cause erratic signals.
- **Loose encoder connector at the control cabinet** — The encoder connector on the servo driver or main I/O board backs out, breaking the signal path.

## Step-by-Step Fix {#fix}

1. **Check the encoder cable and connectors** — Trace the spindle encoder cable from the spindle motor to the control cabinet. Inspect for visible damage, kinking, or coolant ingress. Check both ends for connector security — reseat any loose connectors.
2. **Verify signal at the control** — On the Haas control, go to Diagnostics → Inputs/Outputs and find the spindle encoder signal. Command a slow spindle speed (50–100 RPM) manually and watch for encoder count increments on the diagnostic screen. No count change = no signal reaching the control.
3. **Inspect the encoder at the spindle** — If accessible, inspect the encoder housing at the spindle motor or spindle head for coolant damage or physical impact. Look for cracked housings or contaminated encoder windows.
4. **Test cable continuity** — With the cable disconnected at both ends, use a multimeter to test continuity on all encoder cable conductors. An open circuit on any conductor indicates a broken wire.
5. **Swap with a test cable if available** — If a spare cable is on hand, temporarily substitute it to isolate whether the cable or encoder is the fault source.
6. **Contact Haas service** — Haas encoders are often integrated into the spindle motor assembly; replacement typically requires ordering through a Haas Factory Outlet (HFO) and may involve spindle removal.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle encoder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-113&k=Spindle+encoder+cable&tag=errorcodefixes-20) \| Haas model-specific, shielded; order by machine model and serial |
| Spindle encoder | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-113&k=Spindle+encoder&tag=errorcodefixes-20) \| Integrated with spindle motor on many Haas models; order through HFO |
## When to Call a Pro

Spindle encoder replacement on Haas machines often requires pulling the spindle motor and precise encoder alignment. Incorrect alignment causes tapping errors and control faults. Have a Haas Factory Outlet technician perform encoder replacement if you're not experienced with spindle disassembly.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas Alarm 119 — Spindle Not At Speed Causes & Fix](/posts/haas-alarm-119/)
- [Haas Alarm 121 — ATC Arm Fault](/posts/haas-alarm-121/)
- [Haas Alarm 103 Overheating — CNC Machine Thermal Fault Diagnosis and Fix](/posts/haas-alarm-103-overheating/)
- [Haas SL-20 Lathe Common Alarms — What They Mean and How to Fix Them](/posts/haas-sl-20-lathe-alarms/)
