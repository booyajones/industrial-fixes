---
title: "Mitsubishi U2 Error Code — Causes & Fix"
description: "What Mitsubishi mini-split U2 error code means, why overcurrent or power supply faults trigger, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
---

## Mitsubishi U2 Error Code — What It Means

The Mitsubishi U2 error code indicates an **overcurrent or abnormal high voltage** condition detected at the outdoor unit. The outdoor unit's inverter board monitors the DC bus voltage and compressor current; if either exceeds safe operating limits, U2 trips to protect the compressor and inverter components. This can occur due to power supply problems (high or unstable voltage), a failing compressor drawing excessive current, or a fault in the inverter circuit itself.

[Jump to Fix](#fix)

## Common Causes

- **High supply voltage** — Voltage spikes or sustained overvoltage from the utility can trip U2; check if other equipment on the same circuit is affected.
- **Weak or unstable power supply** — Voltage fluctuations, undersized wiring, or loose connections cause instability that the inverter reads as overcurrent.
- **Failing compressor** — A compressor with winding breakdown or bearing wear draws excess current during startup and trips the inverter's current limit.
- **Faulty inverter board** — The outdoor PCB's overcurrent sensing circuit can fail, triggering false U2 faults even with a healthy compressor.

## Step-by-Step Fix {#fix}

1. **Check supply voltage** — With a true RMS multimeter, measure voltage at the outdoor unit disconnect. It should be within ±10% of nameplate voltage (typically 208–240V). Measure during startup to catch sag.
2. **Inspect wiring and connections** — Check the main power wiring at the outdoor unit for loose terminals, undersized wire gauge, or corrosion. Loose connections cause voltage drop under load.
3. **Power-cycle the system** — Turn off the outdoor unit breaker for 10 minutes. This allows the capacitors to discharge and the fault to reset. Power back on and test.
4. **Check for other symptoms** — If U2 only trips after running for several minutes, compressor overload (caused by dirty coils, low refrigerant, or a failing compressor) is more likely than a power issue.
5. **Clean the outdoor coil** — A fouled condenser coil causes high head pressure, which loads the compressor and can trip overcurrent protection. Clean with coil cleaner and a hose (not a pressure washer).
6. **Measure compressor resistance** — With power off and capacitors discharged, measure resistance between each compressor winding terminal. Severely unbalanced or near-zero readings indicate a failing compressor.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Inverter PCB (outdoor unit board) | If board is confirmed faulty; Mitsubishi-specific — match model exactly |
| Compressor | Only after full electrical diagnosis confirms winding fault |
| Surge protector / line conditioner | If utility voltage quality is poor |

## When to Call a Pro

U2 involving compressor issues requires refrigerant system handling. Compressor replacement requires EPA 608 certification and specialized equipment. If the board is the suspect, Mitsubishi inverter PCBs are expensive — confirm with a certified technician before ordering.
