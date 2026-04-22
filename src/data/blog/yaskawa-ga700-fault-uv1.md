---
title: "Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix"
description: "What Yaskawa GA700 fault UV1 means, why main circuit undervoltage trips the drive, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA700 Fault UV1 — What It Means

UV1 on a Yaskawa GA700 drive (GA700 = Yaskawa's heavy-duty industrial drive platform, successor to the A1000) indicates Main Circuit Undervoltage — the DC bus voltage has dropped below the minimum operating level. The GA700 monitors the DC bus continuously and trips UV1 when the bus falls below approximately 190 VDC on 200 V class drives or 380 VDC on 400 V class drives. UV1 is a protective fault; running the drive on an undervoltage bus would cause output waveform distortion, increased motor heating, and possible damage to the drive's capacitors and power devices.

[Jump to Fix](#fix)

## Common Causes

- **Low or missing input supply voltage** — Supply voltage below the GA700's rated minimum (−15% of nominal on 200 V class, −10% on 400 V class) will pull the DC bus below the UV1 trip threshold.
- **Input phase loss** — A blown fuse or failed contactor on one input phase reduces the rectified DC bus voltage by roughly 30%, immediately triggering UV1.
- **Momentary power interruption** — A utility voltage sag or brief outage trips UV1. Check parameter E2-05 (UV Detection Time) — a very short setting causes false UV1 trips during normal supply transients.
- **Soft-charge circuit issue** — If the inrush current limiting circuit (pre-charge relay or NTC thermistor) fails to close after capacitor pre-charge, the bus stays at a reduced voltage and UV1 trips at startup.
- **Capacitor bank degradation** — Aged DC capacitors on older GA700 drives hold less charge during momentary voltage dips, causing UV1 trips that did not occur when the drive was new.

## Step-by-Step Fix {#fix}

1. **Measure input voltage at R, S, T** — With appropriate PPE, measure all three L-L voltages at the drive's input terminals. The GA700 requires supply voltage within ±10–15% of the nameplate rating.
2. **Check input fuses and circuit breaker** — Inspect all three poles of the upstream protective device. Replace any blown fuses with the correct semiconductor-type fuses specified in the GA700 installation manual.
3. **Review fault history** — Access Fault History (U3-01 through U3-10) on the GA700 operator panel. If UV1 is logged with short duration, a momentary supply sag is likely. If it is logged with long duration, the supply is chronically low.
4. **Check parameter E2-05 (UV Detection Time)** — If the setting is very short (< 0.5 sec), the drive may trip on normal utility transients. Increase to 2.0 seconds to filter out brief sags if the application allows.
5. **Inspect the soft-charge circuit** — If UV1 trips every time at startup but clears after a power cycle wait, the pre-charge relay or inrush thermistor may be failing. This typically requires board-level or drive swap.
6. **Reset the fault** — Press the RESET key on the operator panel or send a fault reset command via fieldbus after correcting the root cause.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (semiconductor) | Use Yaskawa-specified fuse type for GA700 ampere rating |
| Soft-charge relay or thermistor | GA700 frame-size specific; order from Yaskawa |

## When to Call a Pro

UV1 on a GA700 driving a large motor (over 30 kW) should be investigated by a qualified drive technician. Incorrect supply voltage or a failing capacitor bank on a large drive can cause dangerous fault-trip energy releases during reset attempts.
