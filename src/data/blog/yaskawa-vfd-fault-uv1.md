---
title: "Yaskawa VFD Fault UV1 — Causes & Fix"
description: "What Yaskawa UV1 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault UV1 — What It Means

Yaskawa fault UV1 means main circuit undervoltage — the DC bus voltage dropped below the low-voltage detection level during operation. On Yaskawa V1000, A1000, and GA700 drives, UV1 is a protective shutdown that occurs when input voltage is lost or drops significantly during operation. Unlike UV2 (control power undervoltage) or UV3 (soft-charge circuit fault), UV1 specifically indicates the main power circuit lost its voltage source. The drive can't maintain motor control with insufficient DC bus voltage, so it trips cleanly rather than allow uncontrolled deceleration.

[Jump to Fix](#fix)

## Common Causes

- **Momentary power interruption** — A utility voltage dip, a breaker trip, or a large inrush from other equipment on the same panel causes the DC bus to fall below threshold. UV1 often appears during heavy-start cycles elsewhere in the building.
- **Phase loss on input** — If one of the three input phases is missing (blown fuse, open contactor pole, loose terminal), the drive attempts to run on two phases and DC bus voltage sags.
- **Input fuse failure** — A blown fuse on one input phase is invisible without measuring. The drive runs at reduced bus voltage until UV1 trips.
- **Degraded DC bus capacitors** — Older drives with aged electrolytic capacitors lose capacitance. Under load, the bus sags more than it should and drops into UV1 territory.

## Step-by-Step Fix {#fix}

1. **Measure all three input phases** — With the drive idle and powered, measure L1-L2, L2-L3, L1-L3 at the drive terminals. All three must be within 5% of each other. A low or missing phase is the first thing to rule out.
2. **Check input fuses** — Pull or test each input fuse (Yaskawa drives typically use class J semiconductor fuses). Open fuse = replace and trace why it blew.
3. **Check event log** — Yaskawa drives log fault history. Use the keypad to navigate to the fault log and check whether UV1 appeared alone or alongside other faults (like OC or OV) that might indicate a different root cause.
4. **Check for voltage sags during starts** — If UV1 only occurs during motor startup, the input feeder may be undersized, or the acceleration ramp is drawing more current than the supply can sustain.
5. **Reset the system** — Press the RESET key or use the remote reset input after correcting the power supply issue. Restart and monitor DC bus voltage (parameter U1-07 on most Yaskawa drives).

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Input fuses (semiconductor type)](https://www.amazon.com/s?k=Input%20fuses%20(semiconductor%20type)&tag=errorcodefixe-20) | Yaskawa specifies fuse type and current rating in the drive manual |
| [DC bus capacitors](https://www.amazon.com/s?k=DC%20bus%20capacitors&tag=errorcodefixe-20) | Replacement is practical on larger drives; requires capacitor reformation procedure |
| [Line reactor](https://www.amazon.com/s?k=Line%20reactor&tag=errorcodefixe-20) | Reduces the impact of utility voltage sags on the DC bus |

## When to Call a Pro

Aged capacitor diagnosis requires a capacitance meter and knowledge of proper capacitor reformation procedures. For drives over 5 years old with frequent UV1, a Yaskawa service tech can evaluate bus capacitor health.
