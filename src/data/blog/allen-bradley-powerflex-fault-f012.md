---
title: "Allen-Bradley PowerFlex Fault F012 — Causes & Fix"
description: "What Allen-Bradley PowerFlex fault F012 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Motor (replacement)"
most_likely_cause: "Motor winding short circuit (phase to phase)"
---

## Allen-Bradley PowerFlex Fault F012 — What It Means

Allen-Bradley PowerFlex fault F012 is an output phase-to-phase overcurrent fault. The drive's current sensing detected output current exceeding 200–300% of drive rated current — a condition that indicates a very low impedance path across the output phases, such as a motor winding short, an output phase-to-phase cable fault, or a power factor correction capacitor improperly connected to the drive output. F012 trips instantaneously via hardware protection and cannot be inhibited through software. This makes it distinct from the software-adjustable overload faults (F005, F007) and indicates a genuine power circuit fault.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding short circuit (phase to phase)** — The motor has developed an inter-turn or phase-to-phase short in the windings, creating near-zero impedance between two output terminals.
- **Short circuit in output cable** — Physical damage (pinching, abrasion, rodent damage) to the output cable between the drive and motor creates a direct conductor-to-conductor short.
- **Power factor correction capacitors on output** — PF capacitors installed on the load side of the drive cause massive current transients when the drive's switching frequency excites them. Never install PF capacitors between a VFD and its motor.
- **Wrong motor connected or wired incorrectly** — A delta-wired motor connected in wye, a wrong-voltage motor, or wiring errors in the terminal box can create low-impedance conditions that trip F012 on startup.

## Step-by-Step Fix {#fix}

1. **Disconnect the motor and output cable from the drive** — Remove all wiring from T1, T2, T3. Attempt to clear the fault with the output disconnected. If F012 clears (and doesn't return on a run command with no motor), the fault is external to the drive.
2. **Measure resistance between output phases** — With the drive output disconnected and all power off, measure T1-T2, T2-T3, and T1-T3. All three should be equal (matching the motor winding resistance). Any near-zero reading indicates a short in the motor or cable.
3. **Megger test motor and cable separately** — Disconnect the cable at the motor terminal box. Megger each cable conductor against ground and against each other. Megger each motor terminal against the others and against ground.
4. **Inspect motor terminal box for wiring errors** — Open the motor junction box. Verify the correct connection pattern (wye or delta) for the supply voltage. Look for accidentally bridged terminals.
5. **Remove any PF capacitors from the load circuit** — If PF capacitors are present in the circuit between the drive and motor, remove them immediately. Relocate any PF correction to the input side of the drive if required.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor (replacement) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-fault-f012&k=Motor+%28replacement%29&tag=errorcodefixes-20) \| If winding short is confirmed; compare repair cost vs. replacement |
| Output cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-fault-f012&k=Output+cable&tag=errorcodefixes-20) \| Replace complete run if cable short is found |
| Drive output power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-fault-f012&k=Drive+output+power+module&tag=errorcodefixes-20) \| If drive's internal current sensing or IGBT triggered incorrectly; verify externally first |
## When to Call a Pro

If the drive itself trips F012 with nothing connected to the output terminals, the fault is internal to the drive's power electronics. This requires a Rockwell-authorized service technician or a drive repair depot — do not attempt to clear this condition by parameter adjustment.

## Related Articles

- [Allen-Bradley MicroLogix 1400 Common Fault Codes](/posts/allen-bradley-micrologix-fault/)
- [Allen-Bradley PowerFlex 40 Complete Fault Code Guide](/posts/allen-bradley-powerflex-40-complete-guide/)
- [Allen Bradley PowerFlex 40 F2 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f2-fault/)
- [Allen-Bradley PowerFlex 40 F3 Fault — Power Loss](/posts/allen-bradley-powerflex-40-f3/)
- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)

## See Also

- [Allen Bradley PowerFlex 40 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-40-f7-fault/)
- [Allen Bradley PowerFlex 525 F005 Fault, Overvoltage Causes & Fix](/posts/allen-bradley-powerflex-525-fault-f005/)
- [Allen Bradley PowerFlex 525 F7 Fault — Causes & Fix](/posts/allen-bradley-powerflex-525-f7-fault/)
- [Allen-Bradley PowerFlex VFD Fault F7 — Motor Stalled Fix](/posts/allen-bradley-powerflex-fault-7-motor-stalled/)
