---
title: "Yaskawa GA700 OC Fault — Overcurrent Fix"
description: "What the Yaskawa GA700 OC overcurrent fault means, why it triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA700 OC Fault — What It Means

The Yaskawa GA700 is the latest generation general-purpose inverter, succeeding the A1000 series. The OC fault (Overcurrent) appears when the drive's output current exceeds 200% of the drive's rated current. The GA700 has enhanced current detection compared to earlier Yaskawa drives and can distinguish between acceleration overcurrent (oC1), deceleration overcurrent (oC2), and constant-speed overcurrent (oC3), giving you a more precise indication of when in the operating cycle the fault occurs.

[Jump to Fix](#fix)

## OC Sub-Faults on the GA700

| Code | When It Occurs |
|------|---------------|
| oC1 | During acceleration |
| oC2 | During deceleration |
| oC3 | At constant speed |

## Common Causes

- **oC1 (During acceleration)** — Acceleration time too short for the load inertia, mechanical obstruction (seized bearing, jammed conveyor), or a winding-to-winding short in the motor. Extend the acceleration ramp (parameter C1-01) and verify the load is unobstructed.
- **oC2 (During deceleration)** — Deceleration time too short for a high-inertia load. The motor is being regenerated too aggressively and the current spikes. Extend the deceleration time (parameter C1-02) or add a dynamic braking resistor/unit.
- **oC3 (At constant speed)** — A sudden mechanical overload: a pump running against a closed valve, a conveyor carrying a jammed object, a fan blade striking debris. Also caused by motor winding damage or a ground fault.
- **Motor cable too long** — Long motor cables (over 100 feet) create capacitive charging currents that the drive reads as overcurrent. This is more common on the GA700's high-frequency carrier (default 2 kHz).
- **Incorrect motor parameters** — If the motor nameplate data entered in the GA700's parameter groups (E1-02 through E1-09 for motor ratings) doesn't match the actual motor, the drive's overcurrent protection may trigger at the wrong level.

## Step-by-Step Fix {#fix}

1. **Note the exact sub-fault code (oC1, oC2, or oC3)** — The sub-fault tells you when in the cycle the overcurrent occurs, which directs you to the right fix.
2. **For oC1** — Increase the acceleration time in parameter C1-01. Start by doubling the current value. Also verify the load is freely rotating by hand (with power off) before restarting.
3. **For oC2** — Increase the deceleration time in parameter C1-02. If the load has very high inertia (large fans, centrifuges), add a dynamic braking unit and resistor to absorb regenerative energy.
4. **For oC3** — Check the mechanical load. Remove the obstruction if present. Measure motor phase currents with a clamp meter during steady-state operation — they should be balanced and below nameplate FLA.
5. **Megger the motor** — With the motor disconnected from the drive and power off, test insulation resistance phase-to-ground (500V DC megger). Values below 1 MΩ indicate deteriorating insulation that will produce intermittent OC faults.
6. **Check motor cable length and shielding** — If the cable run exceeds 100 feet, add a load reactor (output choke) at the drive output terminals to reduce capacitive charging current.
7. **Verify motor parameters** — Navigate to the GA700's E1 parameter group and confirm motor voltage (E1-01), motor rated current (E1-03), motor rated frequency (E1-04), and motor rated speed (E1-05) all match the motor nameplate.
8. **Run auto-tune** — After confirming motor parameters, run the GA700's auto-tune function (T1-00 parameter). Auto-tune measures the actual motor characteristics and optimizes the drive's control performance, which can eliminate OC faults caused by improper vector control tuning.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Output reactor (load reactor) | [Amazon](https://www.amazon.com/s?k=Output+reactor+%28load+reactor%29&tag=errorcodefixes-20) \| For long cable runs >100 ft; reduces capacitive OC faults |
| Dynamic braking resistor/unit | [Amazon](https://www.amazon.com/s?k=Dynamic+braking+resistor%2Funit&tag=errorcodefixes-20) \| For oC2 on high-inertia loads |
| Motor (replacement) | [Amazon](https://www.amazon.com/s?k=Motor+%28replacement%29&tag=errorcodefixes-20) \| If megger test shows insulation breakdown |
## When to Call a Pro

If oC3 persists with a confirmed healthy motor, correct cable length, and properly tuned drive parameters, the GA700's IGBT output stage may have developed a fault. Yaskawa's Technical Support Center (1-800-927-5292) can walk through advanced diagnostics, or the drive can be sent to a Yaskawa authorized repair center for board-level testing.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)
- [Yaskawa Sigma-7 SGD7S Servo Drive Alarm Codes — Diagnosis & Fix](/posts/yaskawa-sigma7-sgd7s-alarm-codes/)
